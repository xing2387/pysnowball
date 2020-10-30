from __future__ import absolute_import
import json
import os
import sys
from . import cons
from . import api_ref
from . import utls



def cash_flow(symbol, is_annals=0, count=10):

    url = api_ref.finance_cash_flow_url+symbol
    
    if is_annals == 1:
        url = url + '&type=Q4'
    
    url = url + '&count='+str(count)

    return utls.fetch(url)


def indicator(symbol, is_annals=0, count=10):
    
    url = api_ref.finance_indicator_url+symbol
    
    if is_annals == 1:
        url = url + '&type=Q4'
    
    url = url + '&count='+str(count)

    return utls.fetch(url)


def balance(symbol, is_annals=0, count=10):

    url = api_ref.finance_balance_url+symbol

    if is_annals == 1:
        url = url + '&type=Q4'

    url = url + '&count='+str(count)

    return utls.fetch(url)


def income(symbol, is_annals=0, count=10):
    
    url = api_ref.finance_income_url+symbol

    if is_annals == 1:
        url = url + '&type=Q4'

    url = url + '&count='+str(count)

    return utls.fetch(url)


def business(symbol, is_annals=0, count=10):

    url = api_ref.finance_business_url+symbol

    if is_annals == 1:
        url = url + '&type=Q4'

    url = url + '&count='+str(count)

    return utls.fetch(url)
 
