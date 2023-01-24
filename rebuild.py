import os
import platform


def clear_console():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def welcome():
    clear_console()
    print("""
Grade Calculator



[1] Total Points
[2] Grade %
    """)


def point_or_percent(choice):
    if choice == 1:
        print(1)
    else:
        print("not 1")


def main():
    welcome()
    # while True:
    #     try:
    #         point_or_percent(int(input("test")))
    #     except:
    #         print("enter an integer")
    #         continue
    #     break
    x = input()


main()
