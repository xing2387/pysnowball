from __future__ import absolute_import
import json
import os
from . import cons
from . import api_ref
from . import utls


def report(symbol):
    url = api_ref.report_latest_url+symbol
    return utls.fetch(url)


def earningforecast(symbol):
    url = api_ref.report_earningforecast_url+symbol
    return utls.fetch(url)
