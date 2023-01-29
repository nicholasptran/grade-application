"main.py"

import os
import platform
import logging
import datetime
import warnings
import pandas as pd
from sqlalchemy import text, insert, table, column
import app
from app.database.connect_to_db import engine

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

{user_name}
Max points are {max_points} as of {user_date}

    """)
    logging.debug('Printed welcome screen')


# get query as df and find threshold date for max points
def get_max_points():
    '''gets max possible points based on the day it is'''

    query = text("select top 1 * from thresholds where date <= :x order by date desc")
    with engine.connect() as conn:
        logging.debug("Executing max points query")
        max_points = conn.execute(query, {'x': user_date})
        max_points = pd.DataFrame(max_points)

    max_points = max_points.iloc[0,2]
    return max_points

max_points = get_max_points()


# get max possible grade
def get_max_grade(input_points, max_possible_points):
    '''take user input points and max points to lookup id for grade and return the grade'''
    grade_percent = input_points / max_possible_points

    query = text("select top 1 * from grade_scale where grade_percent <= :x")

    with engine.connect() as conn:
        logging.debug("Executing grade query")
        grade_scale = conn.execute(query, {'x': grade_percent})
        grade_scale = pd.DataFrame(grade_scale)

    # insert into db
    grade_audit = table("grade_audit",
                        column("username"),
                        column("date"),
                        column("grade_scale_id"))

    # assign index locations to variables, if empty query then id = 12 as fail
    try:
        letter_grade = grade_scale.iloc[0,1]
        gpa = grade_scale.iloc[0,3]
        grade_scale_id = grade_scale.iloc[0,0]
    except IndexError:
        grade_scale_id = 12
        return "You've failed :("
    finally:
        insert_query = (
    insert(grade_audit).
    values(username=user_name, date=text('getdate()'), grade_scale_id = int(grade_scale_id))
    )
        with engine.connect() as conn:
            conn.execute(insert_query)
            conn.commit()
            logging.info("Created new record")

    return_string = f'\n{input_points} points out of {max_possible_points} possible is a {letter_grade} or a {gpa}.'

    return return_string


def main():
    logging.info("Started main()")
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


    grade = get_max_grade(user_points, max_points)
    print(grade)



    logging.info('End of main()')



main()
