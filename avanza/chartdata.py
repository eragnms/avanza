import logging

from .constants import constants, BASE_URL
from .base import Base

def overview_chartdata(timePeriod):
    """ Returns chartdata from overview page """
    timePeriod = timePeriod.lower()
    url = f"{BASE_URL}{constants['paths']['CHARTDATA_OVERVIEW']}".format(timePeriod)
    if Base()._check_timePeriod(timePeriod):
        return Base()._request(url, auth=True)
    else:
        raise Exception("Invalid timePeriod!")

def distribution_chartdata():
    """ Returns values from account distribution chart """
    return Base()._request(f"{BASE_URL}{constants['paths']['CHARTDATA_DISTRIBUTION']}", auth=True)

def ticker_chartdata(orderbookId, timePeriod='today'):
    """ Returns chartdata of ticker """
    timePeriod = timePeriod.lower()
    url = f"{BASE_URL}{constants['paths']['CHARTDATA_PATH']}".format(orderbookId, timePeriod)
    if Base()._check_timePeriod(timePeriod):
        return Base()._request(url)
    else:
        raise Exception("Invalid timePeriod!")