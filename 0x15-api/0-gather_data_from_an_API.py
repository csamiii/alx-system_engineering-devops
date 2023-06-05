#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/1").json()
    todos = requests.get(url + "todos", params={"userId": 1}).json()

    completed = []
    for todo in todos:
        if todo.get("completed") is True:
            completed.append(todo.get("title"))

    print("Employee {} is done tasks with ({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    for i in completed:
        print("\t{}".format(num, i))
