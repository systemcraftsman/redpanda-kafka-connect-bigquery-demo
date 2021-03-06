import random
import time
import json 


def str_time_prop(start, end, time_format, prop):
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))


def random_date():
    return str_time_prop("2018-01-01T13:30:00", "2021-01-01T04:50:00", '%Y-%m-%dT%H:%M:%S', random.random())

def random_int():
    return random.randint(1, 10001)

def get_json_data():
    data = {}

    data["userId"] = random_int()
    data["classifiedId"] = random_int()
    data["visitCount"] = random_int()
    data["lastVisitDate"] = random_date()

    return json.dumps(data) 

file_object = open('classified-ad-visits-data.json', 'a')

for _ in range(20000):
    json_data = get_json_data()
    file_object.write(f"{json_data}\n")
    print(json_data)

file_object.close()

