import re
from datetime import datetime

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


def read_alpha(message=""):
    var = input(message)

    if var.isalpha():
        return var

    print("Incorrect format\nTry again")
    return read_alpha(message)


def read_number(message=""):
    var = input(message)

    if var.isdigit():
        return var

    print("Incorrect format\nTry again")
    return read_number(message)


def read_alphanumeric(message=""):
    var = input(message)

    if var.isalnum():
        return var

    print("Incorrect format\nTry again")
    return read_alphanumeric(message)


def read_email(message):
    var = input(message)

    if re.fullmatch(regex, var):
        return var
    print("Invalid email\nTry again")
    return read_email(message)


def read_password():
    password = read_alphanumeric("Enter your password: ")
    confirm_password = read_alphanumeric("Confirm your password: ")

    if str(password) != str(confirm_password):
        print("Passwords do not match!\nTry again")
        return read_password()
    return password


def read_registration_data():
    fname = read_alpha("Enter your first name: ")
    lname = read_alpha("Enter your last name: ")
    email = read_email("Enter your email: ")
    password = read_password()
    mobile = read_number("Enter your phone number: ")

    return ("fname", fname), ("lname", lname), ("email", email), ("password", password), ("mobile", mobile)


def read_date():
    format = "%d-%m-%Y"

    start_date = input("Enter your start date: [dd-mm-yyyy] ")
    try:
        bool(datetime.strptime(start_date, format))
    except ValueError:
        print("Invalid format!\nTry again")
        return read_date()

    end_date = input("Enter your end date: [dd-mm-yyyy] ")
    try:
        bool(datetime.strptime(end_date, format))
    except ValueError:
        print("Invalid format!\nTry again")
        return read_date()
    else:
        if start_date > end_date:
            print("End date should be after the start date.\nTry again")
            return read_date()

    return start_date, end_date


def create_new_project_data():
    title = read_alpha("Enter your project title: ")
    details = read_alpha("Enter your project details: ")
    total_target = read_number("Enter your total target from this campaign: ")
    start_date, end_date = read_date()

    return ("title", title), ("details", details), ("total_target", total_target), ("start_date", start_date), ("end_date", end_date)
