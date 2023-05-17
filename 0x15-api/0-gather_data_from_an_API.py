#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""

import requests
from sys import argv

if __name__ == "__main__":
    if (len(argv) > 1):
        userId = argv[1]
        url = 'https://jsonplaceholder.typicode.com'
        userData = requests.get("{}/users/{}".format(url, userId)).json()
        userName = userData.get("name")
        if userName is not None:
            allTasks = requests.get(
                "{}/todos?userId={}".format(url, userId)).json()
            completedTasks = []
            for task in allTasks:
                if task.get("completed"):
                    completedTasks.append(task)
            print("Employee {} is done with tasks({}/{}):"
                  .format(userName, len(completedTasks), len(allTasks)))
            for task in completedTasks:
                print("\t {}".format(task.get("title")))
