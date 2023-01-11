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
        point_or_percent = int(point_or_percent)

        if point_or_percent == 1:
            clear_console()
            total_points()
        else:
            clear_console()
            grade_percent()

    else:
        print('Please only enter digits.\n')
        choose_option()

# they selected option 1
def total_points():
    points_input = input('\nEnter the total points: ')

    if points_input.isdigit():
        points_input = int(points_input)
        
        if points_input > 5000:
            clear_console()
            print('Total points must be equal or less than 5000')
            total_points()
        elif points_input >= 4350:
            clear_console()
            print(points_input, 'points is an A')
        elif points_input >= 4200:
            clear_console()
            print(points_input, 'points is an A-')
        elif points_input >= 4050:
            clear_console()
            print(points_input, 'points is a B+')
        elif points_input >= 3900:
            clear_console()
            print(points_input, 'points is a B')
        elif points_input >= 3750:
            clear_console()
            print(points_input, 'points is a B-')
        elif points_input >= 3600:
            clear_console()
            print(points_input, 'points is a C+')
        elif points_input >= 3450:
            clear_console()
            print(points_input, 'points is a C')
        elif points_input >= 3300:
            clear_console()
            print(points_input, 'points is a C-')
        elif points_input >= 3150:
            clear_console()
            print(points_input, 'points is a D+')
        elif points_input >= 3000:
            clear_console()
            print(points_input, 'points is a D')
        elif points_input >= 2822:
            clear_console()
            print(points_input, 'points is a D-')
        else:
            clear_console()
            print(points_input, 'points is a fail :(')

    else:
        clear_console()
        print('Please only enter digits\n')
        total_points()

# option 2
def grade_percent():
    percent_input = input('\nEnter your grade %: ')

    if percent_input.isdigit():
        percent_input = int(percent_input)

        if percent_input > 100:
            clear_console()
            print('Grade must be equal or less than 100%')
            grade_percent()
        elif percent_input >= 87:
            clear_console()
            print(percent_input, 'is an A\n')
        elif percent_input >= 84:
            clear_console()
            print(percent_input, 'is an A-\n')
        elif percent_input >= 81:
            clear_console()
            print(percent_input, 'is a B+\n')
        elif percent_input >= 78:
            clear_console()
            print(percent_input, 'is a B\n')
        elif percent_input >= 75:
            clear_console()
            print(percent_input, 'is a B-\n')
        elif percent_input >= 72:
            clear_console()
            print(percent_input, 'is a C+\n')
        elif percent_input >= 69:
            clear_console()
            print(percent_input, 'is a C\n')
        elif percent_input >= 66:
            clear_console()
            print(percent_input, 'is a C-\n')
        elif percent_input >= 63:
            clear_console()
            print(percent_input, 'is a D+\n')
        elif percent_input >= 60:
            clear_console()
            print(percent_input, 'is a D\n')
        elif percent_input >= 57:
            clear_console()
            print(percent_input, 'is a D-\n')
        else:
            clear_console()
            print(percent_input, 'is a fail :(')

    else:
        clear_console()
        print('Please only enter digits\n')
        grade_percent()


def main():
    clear_console()
    welcome()
    choose_option()


main()
