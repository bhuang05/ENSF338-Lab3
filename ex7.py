import json
import timeit
import sys
import matplotlib.pyplot as plt

sys.setrecursionlimit(20000)

def binarysearch(data, first, last, mid, key):
    if first <= last:
        if key == data[mid]:
            return mid
        elif key < data[mid]:
            return binarysearch(data, first, mid-1, (first+mid-1)//2, key)
        elif key > data[mid]:
            return binarysearch(data, mid+1, last, (mid+1+last)//2, key)
    return -1


def midsearch(data, tasks, mid):
    results = []
    for task in tasks:
        execution_time = timeit.timeit(lambda: binarysearch(data, 0, len(data)-1, mid, task), number=1)
        results.append((task, execution_time))
    return results

with open("ex7data.json", 'r', encoding="utf-8") as inF:
    data = json.load(inF)
with open("ex7tasks.json",'r', encoding="utf-8") as inT:
    tasks = json.load(inT)
    print(len)

midpoints = [0, 200, 4245, 14040, 42551, 145514, 267901, 389761, len(data)//2, 514234, 690134, 779001, 851004, 942324, len(data) -1]

best_midpoints = {}
for midpoint in midpoints:
    results = midsearch(data, tasks, midpoint)
    for task, execution_time in results:
        if task not in best_midpoints or best_midpoints[task][1] > execution_time:
            best_midpoints[task] = (midpoint, execution_time)
tasks = [task for task in best_midpoints.keys()]
midpoints = [best_midpoints[task][0] for task in tasks]

tasks = [task for task in best_midpoints.keys()]
midpoints = [best_midpoints[task][0] for task in tasks]

plt.scatter(tasks, midpoints)  
plt.xlabel('Tasks')
plt.ylabel('Best Chosen Midpoints')
plt.title('Scatterplot of Tasks and Corresponding Chosen Midpoints')
plt.show()