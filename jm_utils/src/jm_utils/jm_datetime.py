"""
To get useful values of datetime
===============================

- last_day_of_month(yyyymm: str, format: str):
- ...
"""

__author__ = "Jorge Monti"
__version__ = "0.1.0"
__date__ = "2025-05-28"
__status__ = "Development"             # Development, Beta, Production



### Libraries
import datetime as dtm


def datetime_YMD_conversion(datetime: dtm.datetime, output_type: str='string'):
    '''
    format:
        'string':
        'date':
        'datetime':
    '''
    if output_type not in ['string', 'date', 'datetime']:
        raise ValueError(f"output_type solemente puede tomar los valores 'string', 'date', 'datetime', no {output_type}")

    if not isinstance(datetime, dtm.datetime):
        raise TypeError(f"{datetime} debe ser del tipo 'datetime.date' y no {type(datetime)}")
    
    if output_type == 'string':
        return datetime.strftime('%Y%m%d')
    elif output_type == 'date':
        return datetime.date()
    elif output_type == 'datetime':
        return datetime


def last_day_of_month(yyyymm: str, output_type: str='string'):
    '''
    Get last day of the month in yyyymm

    yyyymm: str         -> Valid every year
    output_type: str    -> 'string' (default), 'date', 'datetime'
    '''
    try:
        yyyymm_as_dtm = dtm.datetime.strptime(yyyymm, '%Y%m')
    except ValueError:
        raise ValueError(f"El valor '{yyyymm}' no tiene el formato 'YYYYMM' válido.")
                      
    # day 25 exists in every month. 9 days later, it's always next month
    nxt_mnth = yyyymm_as_dtm.replace(day=25) + dtm.timedelta(days=9)
    # subtracting the number of days of nxt_mnth we'll get last day of original month
    last_day_mnth_dtm = nxt_mnth - dtm.timedelta(days=nxt_mnth.day)
    return datetime_YMD_conversion(last_day_mnth_dtm, output_type)


def last_day_month_past_year(yyyymm: str, output_type: str='string'):
    yyyymm_as_date = dtm.datetime.strptime(yyyymm, '%Y%m').date()
    yyyymm_past_year = yyyymm_as_date.replace(year= yyyymm_as_date.year - 1)
    ym_past_year_str = dtm.datetime.strftime(yyyymm_past_year, '%Y%m')
    return last_day_of_month(ym_past_year_str, output_type)



if __name__ == '__main__':

    date = '202502'
    
    # last_day_of_month() AND last_day_month_past_year()
    for format in 'string', 'date', 'datetime':
        output = last_day_of_month(date, format)
        print('Last day of Month:', output, type(output))
        o2 = last_day_month_past_year(date, format)
        print('Last day of Month past Year:', o2, type(o2))
        print()








