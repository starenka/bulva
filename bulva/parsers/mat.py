#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging, datetime, copy, re

import requests
from pyquery import PyQuery as pq

from bulva.parsers import MTParser

now = datetime.datetime.now()


class Parser(MTParser):
    URL = 'http://www.mat.cz/matclub/cz/kino/mesicni-program'
    RE_NUM = re.compile(r'^.*?([\d]+).*$')

    def _parse_date(self, date_str):
        day, month = ''.join(date_str.split(' ')[1:]).split('.')[:-1]
        return datetime.datetime(year=now.year, month=int(month), day=int(day))

    def get_items(self):
        data = requests.get(self.URL)
        items = []

        if not data:
            logging.error('No data returned from %s' % self.URL)
            return items

        data = pq(data.content)
        for one in data.find('div.content1 div'):
            one = pq(one)
            if one.attr('class') not in ('kalendar', 'film', 'filmtxt'):
                continue

            if one.hasClass('kalendar'):
                date = self._parse_date(one.text())
            elif one.hasClass('film'):
                info = one.find('div.filmtable td')
                if len(info) == 1:
                    continue
                titles, time, subtitles, length, price, dummy = map(lambda x: pq(x), info)

                item = copy.copy(self.item)
                item['subtitles'], item['length'] = subtitles.text(), int(
                    re.search(self.RE_NUM, length.text()).group(1))
                item['price'] = int(re.search(self.RE_NUM, price.text()).group(1))
                item['title'], item['title_orig'] = titles.find('h4').text(), titles.find('h5').text()
                item['start'] = self._mk_start_date(time.text(), date=date, split_with='.')
            elif one.hasClass('filmtxt'):
                item['url'] = one.find('div.filmface1 a').attr('href')
                item['teaser'] = one.find('p').text().replace(u'... (více)', '')
                items.append(item)

        return items