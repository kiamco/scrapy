from datetime import datetime, timedelta
import re
import requests
import json

def iso_date(date_string):
    if any(char.isdigit() for char in date_string) == False:
        date_N_days_ago = datetime.now().date()
        return date_N_days_ago
    else:
        parsed_date = int(re.findall(r'\d+', date_string)[0])
        date_N_days_ago = datetime.now().date() - timedelta(days=parsed_date)
        return date_N_days_ago
    

def iso_date2(date_string):
    if any(char.isdigit() for char in date_string) == False:
        datetime_object = datetime.now().date()
        return datetime_object
    else:
        datetime_object = datetime.strptime(date_string, '%b %d').date()
        x = datetime.today().year
        datetime_object = datetime_object.replace(year = x)
        return datetime_object


def remove_unwanted(value):
    x = value.replace(u'\n', "")
    x = value.replace(u'\n ', "")
    x = x.lstrip()
    return x


