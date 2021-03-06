#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest, datetime

from bulva import parsers
from bulva.parsers import MTParser

class TestMTParser(unittest.TestCase):
    def test_parse_date(self):
        parser = MTParser()
        parsers.now = datetime.datetime(year=2012, month=8, day=24)
        self.assertEqual(parser._parse_date('jueves, 24. srpna'),
            datetime.datetime(year=2012, month=8, day=24))
        self.assertEqual(parser._parse_date('viernes, 24. Srpna'),
            datetime.datetime(year=2012, month=8, day=24))
        self.assertEqual(parser._parse_date('monday 24. Srpna'),
            datetime.datetime(year=2012, month=8, day=24))

        parsers.now = datetime.datetime(year=2012, month=8, day=24)
        self.assertEqual(parser._parse_date('utorok, 1. Října'),
            datetime.datetime(year=2012, month=9, day=1))

        parsers.now = datetime.datetime(year=2012, month=12, day=24)
        self.assertEqual(parser._parse_date('nedele, 2. ledna'),
            datetime.datetime(year=2013, month=1, day=2))