#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pprint, datetime, importlib

#query single parser
from bulva.parsers.mat import Parser

#all
all = Parser().get_items()
pprint.pprint(all)

#today
now = datetime.datetime.now()
pprint.pprint(filter(lambda x: x['start'].date() == now.date(), all))

#tomorrow
pprint.pprint(filter(lambda x: x['start'].date() == (now + datetime.timedelta(days=1)).date(), all))

#get data from all parsers
from bulva import parsers


all_parsers = dict()
for one in parsers.__all__:
    mod = importlib.import_module('bulva.parsers.%s' % one)
    all_parsers[one] = mod.Parser().get_items()

pprint.pprint(all_parsers)