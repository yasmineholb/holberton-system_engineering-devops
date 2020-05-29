#!/usr/bin/python3
"""Python script that, for a given employee ID, returns information """
import requests
import sys
if __name__ == '__main__':
    emp_id = int(sys.argv[1])
    u = "https://jsonplaceholder.typicode.com"
    url = requests.get(u + "/users/{}".format(emp_id)).json()
    td = requests.get(u + "/todos?userId={}".format(emp_id)).json()
    num = []
    for n in td:
        if n.get('completed') is True:
            num.append(n.get('title'))
    print("Employee {} is done with tasks({}/{}):".
          format(url.get('name'), len(num), len(td)))
    for n in num:
        print("\t {}".format(n))
