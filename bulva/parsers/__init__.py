#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime, locale, re, logging

import requests

__all__ = ['oko',
           'mat',
           'aero',
           #'svetozor',
           # 'evald',
           # 'atlas',
]

locale.setlocale(locale.LC_ALL, ("cs_CZ"))
now = datetime.datetime.now()


class MTParser(object):
    item = dict(cycle=None,
        price=None,
        title=None,
        title_orig=None,
        url=None,
        reservation_url=None,
        start=None,
        length=None,
        subtitles=None,
        teaser=None
    )

    RE_NUM = re.compile(r'^.*?([\d]+).*$')

    def _get_data(self, url):
        data = requests.get(url)
        if not data:
            logging.error('No data returned from "%s"' % url)
            return False
        return data

    def _mk_start_date(self, hm_str, date, split_with=':'):
        hour, minute = hm_str.split(split_with)
        return datetime.datetime(year=date.year, month=date.month, day=date.day, hour=int(hour), minute=int(minute))

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
        raise NotImplementedError

