import json
def binarysearch(data, first, last, key):
    if(first <= last):
        mid = int(input(f"Enter an index between {first} and {last} to start the search as 'mid' "))
    if(key == data[mid]):
        return mid
    elif (key < data[mid]):
        return binarysearch(data, first, mid-1, key)
    elif (key > data[mid]):
        return binarysearch(data, mid+1, last, key)
    return -1

with open("ex7data.json", 'r', encoding="utf-8") as inF:
    content = json.load(inF)