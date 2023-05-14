#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""
import json
import requests
from sys import argv

if __name__ == '__main__':
    apiEndpoint = 'https://jsonplaceholder.typicode.com'
    apiUser = requests.get(apiEndpoint + '/users/' + argv[1]).json()['username']
    todos = requests.get(apiEndpoint + '/todos?userId=' + argv[1]).json()

    with open("{}.json".format(argv[1]), "w") as jsonfile:
        json.dump({argv[1]: [{
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": apiUser
            } for todo in todos]}, jsonfile)
