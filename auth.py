from utils import read_registration_data
import json
from ioservice import read_json, write_json
from utils import read_email, read_alphanumeric, create_new_project_data, read_number
import uuid
from projects import create_project, read_projects, edit_project, delete_project


def register():
    data = read_registration_data()

    registration_info = dict(data)
    id = uuid.uuid1().hex
    registration_info["id"] = id
    print(registration_info)
    user_info = registration_info
    write_json(registration_info)
    print(read_json())


def login():
    l = read_json()

    while True:
        email = read_email("Enter your email: ")
        password = read_alphanumeric("Enter your password: ")

        found = False
        for user in l:
            if user["email"] == email:
                if user["password"] == password:
                    print("Logged in successfully.")
                    main_menu(user)
                    found = True
                else:
                    print("Incorrect password")
            else:
                print("Incorrect email or password")

        if found:
            break


def main_menu(user_info):
    print("1) Create Project\n2) Edit Project\n3) Delete Project\n4) View all projects\n")

    option = read_number("Please choose your option: ")
    option = int(option)

    if option == 1:
        create_project(user_info)
    elif option == 2:
        edit_project(user_info)
    elif option == 3:
        delete_project(user_info)
    elif option == 4:
        read_projects()
    else:
        print("Incorrect option!\nTry again\n")

    print()
    main_menu(user_info)

