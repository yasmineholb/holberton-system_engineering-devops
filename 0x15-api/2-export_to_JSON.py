#!/usr/bin/python3
"""Python script that, for a given employee ID, returns information """
import json
import requests
import sys
if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    idd = sys.argv[1] 
    userId = int(sys.argv[1])
    user = requests.get(url + "/users/{}".format(userId))
    td = requests.get(url + '/todos')
    name = user.json().get('username')
    file = sys.argv[1] + '.json'
    ks = []
    for t in td:
        tsk = {}
        tsk["task"] = t.get('title')
        tsk["completed"] = t.get('completed')
        tsk["username"] = name
        tasks.append(task_dict)
    jf = {}
    jf[idd] = ks
    with open("{}.json".format(idd), 'w') as f:
        json.dump(jf, f)
