#!/usr/bin/env python
# -*- coding: utf-8 -*-
import copy, itertools

from pyquery import PyQuery as pq

from bulva.parsers import MTParser

class Parser(MTParser):
    URL = 'http://www.kinosvetozor.cz/cz/program/'
    URL_BASE = 'http://www.kinosvetozor.cz'

    def get_items(self):
        items = []
        data = self._get_data(self.URL)
        if not data:
            return items

        data = pq(data.content)
        for day, big, small in zip(data.find('h2.dnes'), data.find('table.programDen'),
            data.find('table.malySal')):
            date = self._parse_date(pq(day).text())

            for one in itertools.chain(pq(big).find('tr')[1:-1],pq(small).find('tr')[1:-1]):
                movie, ef, time = map(lambda x: pq(x), pq(one).find('td'))
                item = copy.copy(self.item)
                item['cycle'], item['start'] = movie.find('span a').attr('title'), self._mk_start_date(time.text(),
                    date=date)
                item['title'], item['url'] = movie.find('a').attr('title'), '%s%s' % (
                    self.URL_BASE, movie.find('a').attr('href'))
                items.append(item)
        return items