from program import count_diff
import random

class TV:
    nom_l = 5*10**4
    min_l = 1
    max_l = 10**5
    nom_a = 5*10**8
    min_a = 1
    max_a = 10**9
    nom_k = 500
    min_k = 0
    max_k = 1000


test_case = [
   {
        "arr": [1],
        "k": -1,
        "expected": "error",
        "tag": "1"
    },
    {
        "arr": [],
        "k": 1,
        "expected": "error",
        "tag": "2"
    },
    {
        "arr": [1, -1],
        "k": 1,
        "expected": "error",
        "tag": "3"
    },
    {
        "arr": [-1],
        "k": 1,
        "expected": "error",
        "tag": "4"
    },
    {
        "arr": [1, 1, -1],
        "k": -1,
        "expected": "error",
        "tag": "5"
    },
    {
        "arr": [1],
        "k": 0,
        "expected": 0,
        "tag": "6"
    },
    {
        "arr": [1],
        "k": 1,
        "expected": 0,
        "tag": "7"
    },
    {
        "arr": [2, 1],
        "k": 1,
        "expected": 1,
        "tag": "8"
    },
    {
        "arr": [1, 1, 2],
        "k": 0,
        "expected": 1,
        "tag": "9"
    },
    {
        "arr": [1, 1, 1],
        "k": 0,
        "expected": 3,
        "tag": "10"
    },
    {
        "arr": [1, 1],
        "k": 0,
        "expected": 1,
        "tag": "11"
    },
    {
        "arr": [1, 1],
        "k": 0,
        "expected": 1,
        "tag": "12"
    },
    {
        "arr": [1, 1],
        "k": 1,
        "expected": 0,
        "tag": "13"
    },
    {
        "arr": [1, 1, 2],
        "k": 1,
        "expected": 2,
        "tag": "14"
    },
    
]

for k, item in enumerate(test_case):
    print(f"Test {item['tag']}: ", end="")
    try:
        count = count_diff(item["arr"], item["k"])
    except: 
        if (item['expected'] == "error"):
            print("Pass")
        else:
            print("Failed")
    else:
        if (item['expected'] == count):
            print("Pass")
        else:
            print("Failed")

    