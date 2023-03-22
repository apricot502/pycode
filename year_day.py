# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 12:17:42 2023

@author: 23257
"""

def totalday(year):
    total_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    year_day=sum(total_month);
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        year_day=year_day+1;
    return year_day;
if __name__ == '__main__':
    for i in range(2018,2022):
        print(i,"year",totalday(i));
    