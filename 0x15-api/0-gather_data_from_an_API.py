#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
from sys import argv

if __name__ == '__main__':
    # Get the employee respose
    appEndpoint = 'https://jsonplaceholder.typicode.com'
    userResponse = requests.get(appEndpoint + '/users/' + argv[1]).json()

    # Get the sum number of tasks
    todos = requests.get(appEndpoint + '/todos?userId=' + argv[1]).json()

    # Get completed tasks plus titles
    tasksTitle = [todo['title'] for todo in todos if todo['completed']]

    print('Employee {} is done with tasks({}/{}):'
          .format(userResponse['name'], len(tasksTitle), len(todos)))

    [print('\t {}'.format(title)) for title in tasksTitle]
