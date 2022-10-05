# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from utils import read_number
from auth import register, login


def init():
    print("1) Register\n2) Login")

    action = int(read_number("\nPlease choose your action: "))

    if action == 1:
        return register()
    elif action == 2:
        return login()
    else:
        print("Try again")
        return init()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    init()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
