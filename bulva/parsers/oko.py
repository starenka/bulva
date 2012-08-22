#!/usr/bin/env python
# -*- coding: utf-8 -*-
import locale, logging, datetime, copy

import requests
from pyquery import PyQuery as pq

from bulva.parsers import MTParser

locale.setlocale(locale.LC_ALL, ("cs_CZ"))
now = datetime.datetime.now()


class Parser(MTParser):
    URL = 'http://www.biooko.net/cz/program/'
    URL_BASE = 'http://www.biooko.net'

    def _parse_date(self, date_str):
        day, month_abb = date_str.split(', ')[1].split('. ')

        if now.strftime('%b') == month_abb.lower()[:3]:
            date = datetime.datetime(year=now.year, month=now.month, day=int(day))
        else:
            if now.month == 12:
                date = datetime.datetime(year=now.year + 1, month=1, day=int(day))
            else:
                date = datetime.datetime(year=now.year, month=now.month + 1, day=int(day))

        return date

    def get_items(self):
        data = requests.get(self.URL)
        items = []

        if not data:
            logging.error('No data returned from %s' % self.URL)
            return items

        data = pq(data.content)
        for one in data.find('table.program tr'):
            one = pq(one)
            if one.hasClass('day'):
                date = self._parse_date(one.text())
            else:
                item = copy.copy(self.item)
                item['cycle'], tr, movie = one.find('td.cycle a').attr('title'), pq(
                    one.find('td.time_reservation')), pq(
                    one.find('span.movie_name_block strong a'))
                item['title'], item['url'] = movie.attr('title'), '%s%s' % (self.URL_BASE, movie.attr('href'))
                item['reservation_url'] = tr.find('a.time').attr('href')
                item['start'] = self._mk_start_date(tr.find('a.time').text(), date=date)
                items.append(item)
        return items