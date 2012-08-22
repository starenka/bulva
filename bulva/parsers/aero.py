#!/usr/bin/env python
# -*- coding: utf-8 -*-
import copy, re

import requests
from pyquery import PyQuery as pq

from bulva.parsers import MTParser

class Parser(MTParser):
    URL = 'http://www.kinoaero.cz/cz/program/'
    URL_BASE = 'http://www.kinoaero.cz'

    def get_items(self):
        items = []
        data = self._get_data(self.URL)
        if not data:
            return items

        data = pq(data.content)
        for one in data.find('table.program tr'):
            one = pq(one)
            if one.hasClass('day'):
                date = self._parse_date(one.text())
                print date
            else:
                item = copy.copy(self.item)
                cycle, time, movie, price, reservation, ef = map(lambda x: pq(x), one.find('td'))
                item['cycle'], item['start'] = cycle.find('a').attr('title'), self._mk_start_date(time.text(), date=date)
                item['price'] = int(re.search(self.RE_NUM, price.text()).group(1))
                item['title'], item['url'] = movie.find('a').attr('title'), '%s%s' % (self.URL_BASE, movie.find('a').attr('href'))
                items.append(item)

        return items