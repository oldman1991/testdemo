# coding: utf-8
""" 
@author: oldman
@file: 0103_day_of_year_for_date.py 
@time: 2022-05-11 18:54
"""

from datetime import date


def day_of_yera_for_date(given_date: date) -> int:
    if not isinstance(given_date, date):
        return -1
    year = given_date.year
    month = given_date.month
    day = given_date.day

    sencond_month_days = 29 if year % 4 == 0 else 28

    months_days = [31, sencond_month_days, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    days = 0

    for i in range(1, month):
        days += months_days[i - 1]

    days += day

    return days


if __name__ == "__main__":
    assert day_of_yera_for_date(20) == -1
    assert day_of_yera_for_date(date(2020, 1, 1)) == 1
    assert day_of_yera_for_date(date(2019, 3, 1)) == 60
    assert day_of_yera_for_date(date(2016, 5, 1)) == 122
