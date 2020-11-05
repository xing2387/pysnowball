from __future__ import absolute_import
import json
import os
from . import cons
from . import api_ref
from . import utls


def quotec(symbols):
    url = api_ref.realtime_quote+symbols
    return utls.fetch_without_token(url)


def quotec2(symbols):
    url = api_ref.realtime_quote_2_format(symbols)
    return utls.fetch(url)


def pankou(symbol):
    url = api_ref.realtime_pankou+symbol
    return utls.fetch_without_token(url)

