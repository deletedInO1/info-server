import json
import time

import requests

import main


# from matplotlib import pyplot as plt
import command_executer
command_executer.start_program()

def run(prompt):
    #PORT PUBLIC
    myobj = {"prompt": prompt}
    x = main.interpret_request(myobj)
    d = x
    return d["answer"]

# while True:
#     myobj = dict()
#     x = requests.post(url+"online", json=myobj)
#     print(x.content)
#     if len(x.content) > 0:
#         break
#     time.sleep(1)

times = []
for i in range(20):
    t1 = time.time()
    run("hi")
    t2 = time.time()
    t = t2 - t1
    print(t)
    times.append(t)
    time.sleep(0.1)

with open("speed_test_local.json", "w") as f:
    json.dump(times, f)

with open("speed_test_local.json", "r") as f:
    times = json.load(f)

avg_time = sum(times) / len(times)
times_sorted = sorted(times)
if len(times_sorted) % 2 == 0:
    median_time = times_sorted[len(times_sorted)//2]
else:
    print("median avg")
    median_time = (times_sorted[len(times_sorted)//2]+times_sorted[len(times_sorted)//2+1])/2

print("average", avg_time)
print("median", median_time)