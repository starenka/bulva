#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pprint, datetime

from bulva.parsers.oko import Oko

#all
pprint.pprint(Oko().get_items())

#today
now = datetime.datetime.now()
pprint.pprint(filter(lambda x: x['start'].date() == now.date(), Oko().get_items()))

#tomorow
pprint.pprint(filter(lambda x: x['start'].date() == (now + datetime.timedelta(days=1)).date(), Oko().get_items()))