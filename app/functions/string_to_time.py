'''Takes string in 12/31/19 and turns it into %m/%d/%y datetime'''
import datetime


def string_to_time(string):
    '''Takes string in 12/31/19 and turns it into %m/%d/%y datetime'''
    return datetime.datetime.strptime(string, '%m/%d/%y')
