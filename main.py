"main.py"

import os
import platform
import logging
import datetime
import warnings
import pandas as pd
import app

warnings.filterwarnings('ignore')

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


# get query as df and find threshold date for max points
def get_max_points():
    '''gets max possible points based on the day it is'''
    max_points_query = pd.read_sql('select * from thresholds', app.database.connect_to_db.conn)

    # returns the max points of the last passed date threshold
    max_points_df = pd.DataFrame(max_points_query)

    # instead of using reversed, I could have changed the order by in the sql statement
    for row in reversed(max_points_df['date']):
        if user_date >= row:
            max_points = max_points_df[max_points_df.date == row].iloc[0, 2]
            return max_points

max_points = get_max_points()


def get_max_grade(input_points, max_possible_points):
    '''take user input points and max points to lookup id for grade and return the grade'''
    grade_percent = input_points / max_possible_points
    logging.info('User - max points: %s, input points: %s', max_possible_points, input_points)

    grade_scale_query = pd.read_sql('select * from grade_scale', app.database.connect_to_db.conn)
    grade_scale_query = pd.DataFrame(grade_scale_query)


    # for record in grade_scale_query['grade_percent']:
    #     if grade_percent >= record:
    #         grade_scale_id = grade_scale_query[grade_scale_query.grade_percent == record].iloc[0, 0]
    #         print(grade_scale_id)
    #         return grade_scale_id
    return grade_scale_query




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
            logging.error("Exception Occurred", exc_info=True)
        else:
            logging.info('User entered input correctly')
            break
    
    test = get_max_grade(user_points, max_points)
    
    print(test)




    logging.debug('End of main()')



main()
