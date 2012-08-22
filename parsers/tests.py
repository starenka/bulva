#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest, datetime

from parsers import oko

class TestOko(unittest.TestCase):
    def test_parse_date(self):
        o = oko.Oko()
        oko.now = datetime.datetime(year=2012, month=8, day=24)
        self.assertEqual(o._parse_date('den, 24. srpna'),
            datetime.datetime(year=2012, month=8, day=24))
        self.assertEqual(o._parse_date('den, 24. Srpna'),
            datetime.datetime(year=2012, month=8, day=24))

        oko.now = datetime.datetime(year=2012, month=8, day=24)
        self.assertEqual(o._parse_date('den, 1. Října'),
            datetime.datetime(year=2012, month=9, day=1))

        oko.now = datetime.datetime(year=2012, month=12, day=24)
        self.assertEqual(o._parse_date('den, 2. ledna'),
            datetime.datetime(year=2013, month=1, day=2))