import uuid

from ioservice import write_json, read_json, write_new_json
from utils import create_new_project_data, read_number


def create_project(user):
    data = create_new_project_data()
    data_obj = dict(data)
    id = uuid.uuid1().hex
    data_obj["id"] = id
    data_obj["user_id"] = user["id"]
    write_json(data_obj, mode="projects")


def read_projects():
    raw_data = read_json(mode="projects")

    for i, item in enumerate(raw_data):
        show_item(i, item)

    if len(raw_data) == 0:
        print("No projects found")
        return


def show_item(i, item):
    print(f"{i})", item["title"], item["details"], item["total_target"], item["start_date"], item["end_date"])


def get_my_projects(user_id):
    raw_data = read_json(mode="projects")
    l = []

    for i, item in enumerate(raw_data):
        if item["user_id"] == user_id:
            l.append(item)

    return l


def edit_project(user_info):
    # projects = get_my_projects(user_info["id"])
    projects = read_json(mode="projects")

    for i, item in enumerate(projects):
        show_item(i, item)

    if len(projects) == 0:
        print("No projects found")
        return

    project_index = read_number("Please select the number of project you wish to edit: ")

    if int(project_index) not in range(len(projects)):
        print("Invalid option\nTry again")
        edit_project(user_info)
    elif projects[int(project_index)]["user_id"] != user_info["id"]:
        print("Choose projects you created you cannot edit other projects.\nTry again")
        edit_project(user_info)
    else:
        project = projects[int(project_index)]
        print(project)
        data = create_new_project_data()
        data_obj = dict(data)
        data_obj["id"] = project["id"]
        data_obj["user_id"] = project["user_id"]

        projects[int(project_index)] = data_obj
        print(projects)

        write_new_json(projects)


def delete_project(user_info):
    # projects = get_my_projects(user_info["id"])
    projects = read_json(mode="projects")
    projects = list(projects)

    for i, item in enumerate(projects):
        show_item(i, item)

    if len(projects) == 0:
        print("No projects found")
        return

    project_index = read_number("Please select the number of project you wish to delete: ")

    if int(project_index) not in range(len(projects)):
        print("Invalid option\nTry again")
        delete_project(user_info)
    elif projects[int(project_index)]["user_id"] != user_info["id"]:
        print("Choose projects you created you cannot delete other projects.\nTry again")
        delete_project(user_info)
    else:
        index = int(project_index)
        projects.remove(projects[index])
        print(projects)
        write_new_json(projects)
