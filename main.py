"main.py"

import os
import platform
import logging
import datetime
import pandas as pd
import app

logging.debug('App started')

# initialize variables
user_name = os.getlogin()
user_date = datetime.datetime.now()
user_platform = platform.system()


def clear_console(users_platform):
    '''checks platform to do cls or clear'''
    if users_platform == 'Windows':
        os.system('cls')
        logging.debug('CMD cleared')
    else:
        os.system('clear')
        logging.debug('bash cleared')


def welcome():
    '''Displays a welcome screen'''
    clear_console(user_platform)
    print(f"""
Grade Calculator

{user_date} - {user_name}



    """)
    logging.debug('Printed welcome screen')


def raise_func(ex):
    '''use to raise an exception in a lambda function'''
    raise ex

# TODO turn the max points into a function
# get query as df and find threshold date for max points
max_points_query = pd.read_sql('select * from thresholds', app.database.connect_to_db.conn)


# returns the max points of the last passed date threshold
max_points_df = pd.DataFrame(max_points_query)

for row in reversed(max_points_df['date']):
    if user_date >= row:
        max_points = max_points_df[max_points_df.date == row].iloc[0, 2]
        break


def main():
    welcome()
    while True:
        def validate(users_input):
            if users_input > max_points:
                raise Exception(f'\nPoints entered are higher than the current max points of {max_points}\n')

        try:
            user_points = int(input("Enter your current total points: "))
            validate(user_points)
        except ValueError:
            print('Please only enter numbers.')
            logging.warning('User entered non-numbers in total_points')
        except Exception:
            print(f'Points entered are higher than the current max points of {max_points}')
            logging.warning('User entered points higher than max available points')
        else:
            logging.info('User entered input correctly')
            break

    # get grade percent
    grade_percent = user_points / max_points
    logging.info('User - max points: %s, input points: %s', max_points, user_points)

    # grade scale as index
    grade_scale_query = pd.read_sql('select * from grade_scale', app.database.connect_to_db.conn)
    grade_scale_query = pd.DataFrame(grade_scale_query)
    for record in grade_scale_query['grade_percent']:
        print(record)

    logging.debug('End of main()')



main()
