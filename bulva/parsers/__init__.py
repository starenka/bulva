#!/usr/bin/env python
# -*- coding: utf-8 -*-

__all__ = ['oko',
        # 'mat'
        # 'aero'
        # 'svetozor'
        # 'atlas'
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

    def get_items(self):
        raise NotImplementedError

