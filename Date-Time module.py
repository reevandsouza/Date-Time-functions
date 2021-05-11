"""
Project for Week 4 of "Python Programming Essentials".
Collection of functions to process dates.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import datetime

def days_in_month(year, month):
    '''
    This function takes year and month as input and returns the
    number of days in it.
    '''
    if datetime.MINYEAR <= year <= datetime.MAXYEAR:
        if 1 <= month < 12:
            lesser_date = datetime.date(year, month, 1)
            greater_date = datetime.date(year, month+1, 1)
            difference = greater_date-lesser_date
            return difference.days
        elif month == 12:
            return 31
        else:
            return False
    else:
        return False
# test function 1 
# This statement is to check the functioning of the first function
#print(days_in_month(2008, 12))

def is_valid_date(year, month, day):
    '''
    This function takes year month and day as input and returns
    true or false according to the validity of the date
    '''
    day_check = days_in_month(year, month)
    if datetime.MINYEAR <= year <= datetime.MAXYEAR:
        if 1 <= month <= 12:
            if 1 <= day <= day_check:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
#check function 2
# This statement is to check the functioning of the second function
#print(is_valid_date(1998, 12, 31))

def days_between(year1, month1, day1, year2, month2, day2):
    '''
    This function takes 2 dates as input, the previous date first
    preceding the latest date and returns the number of days in
    between
    '''
    if is_valid_date(year1, month1, day1):
        date_1 = datetime.date(year1, month1, day1)
        if is_valid_date(year2, month2, day2):
            date_2 = datetime.date(year2, month2, day2)
            difference = date_2 - date_1
            if difference.days > 0:
                return difference.days
            else:
                return 0
        else:
            return 0
    else:
        return 0
#test function 3
# This statement is to check the functioning of the third function
#print(days_between(2003, 3, 4, 2005, 4, 2))

def age_in_days(year, month, day):
    '''
    This function takes your date of birth as input and returns the
    age of a person in days.
    '''
    if is_valid_date(year, month, day):
        dob = datetime.date(year, month, day)
        from datetime import date
        date_today = date.today()
        final_answer = date_today - dob
        return final_answer.days
    else:
        return 0
#test function 4
# This statement is to check the functioning of the fourth function
#print(age_in_days(1978,6,25))
