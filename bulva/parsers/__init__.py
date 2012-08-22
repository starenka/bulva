#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

__all__ = ['oko',
           'mat',
           # 'aero',
           # 'svetozor',
           # 'evald',
           # 'atlas',
]


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

    def _mk_start_date(self, hm_str, date, split_with=':'):
        hour, minute = hm_str.split(split_with)
        return datetime.datetime(year=date.year, month=date.month, day=date.day, hour=int(hour), minute=int(minute))


    def get_items(self):
        raise NotImplementedError

