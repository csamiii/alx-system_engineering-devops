#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    userApi = requests.get(url + "users/{}".format(argv[1])).json()['username']
    todos = requests.get(url + "todos?userId=" + argv[1]).json()

    with open("{}.csv".format(argv[1]), "w") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todos:
           writer .writerow([argv[1], userApi, todo['completed'], todo['title']])
