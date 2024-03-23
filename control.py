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
        "arr": [TV.nom_a]* (TV.max_l + 2),
        "k": 500,
        "expected": "error",
        "tag": "flow1-1"
    },
    {
        "arr": [],
        "k": 500,
        "expected": "error",
        "tag": "flow1-2"
    },
    {
        "arr": [500],
        "k": -1,
        "expected": "error",
        "tag": "flow2-1"
    },
    {
        "arr": [500],
        "k": TV.max_k + 5,
        "expected": "error",
        "tag": "flow2-2"
    },
    {
        "arr": [-2],
        "k": 500,
        "expected": "error",
        "tag": "flow3-1"
    },
    {
        "arr": [TV.max_a + 5],
        "k": 500,
        "expected": "error",
        "tag": "flow3-2"
    },
    {
        "arr": [1, 2, 1, 1],
        "k": 500,
        "expected": 0,
        "tag": "flow3-2"
    },
    {
        "arr": [1, 2, 1, 1],
        "k": 0,
        "expected": 3,
        "tag": "flow4"
    },
    {
        "arr": [1, 2, 1, 1],
        "k": 1,
        "expected": 3,
        "tag": "flow5"
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

    