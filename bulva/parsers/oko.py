#!/usr/bin/env python
# -*- coding: utf-8 -*-
import copy

from pyquery import PyQuery as pq

from bulva.parsers import MTParser

class Parser(MTParser):
    URL = 'http://www.biooko.net/cz/program/'
    URL_BASE = 'http://www.biooko.net'

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