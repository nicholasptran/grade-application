import os

# clear console
def clear_console():
    os.system('cls')

# displays welcome screen
def welcome():
    print('\nGrade Calculator\n')
    print('\nWould you like to use:')
    print('\n\t[1] Total Points \n\t[2] Grade %\n')

# choose option
def choose_option():
    point_or_percent = input('Enter selected choice: ')

    if point_or_percent.isdigit():
        if point_or_percent == 1:
            total_points()
        else:
            grade_percent()

    else:
        print('Please only enter digits.\n')
        choose_option()

# they selected option 1
def total_points():
    clear_console()
    points_input = input('Enter the total points: ')

# option 2
def grade_percent():
    clear_console()
    percent_input = input('Enter your grade %: ')


def main():
    clear_console()
    welcome()
    choose_option()


main()