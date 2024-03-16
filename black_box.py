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
        "arr": [TV.nom_a]* TV.min_l,
        "k": 500,
        "expected": 0,
        "tag": "edge1"
    },
    {
        "arr": [TV.nom_a] * (TV.min_l + 1),
        "k": TV.nom_k,
        "expected": 0,
        "tag": "edge2"        
    },
    {
        "arr": [TV.nom_a]*TV.max_l,
        "k": TV.nom_k,
        "expected": 0,
        "tag": "edge3"        
    },
    {
        "arr": [TV.nom_a]*(TV.max_l-1),
        "k": TV.nom_k,
        "expected": 0,
        "tag": "edge4"        
    },
    {
        "arr": [TV.min_a]*(TV.nom_l),
        "k": TV.nom_k,
        "expected": 0,
        "tag": "edge5"        
    },
    {
        "arr": [TV.min_a+1]*(TV.nom_l),
        "k": TV.nom_k,
        "expected": 0,
        "tag": "edge6"        
    },
    {
        "arr": [TV.max_a]*(TV.nom_l),
        "k": TV.nom_k,
        "expected": 0,
        "tag": "edge7"        
    },
    {
        "arr": [TV.max_a-1]*(TV.nom_l),
        "k": TV.nom_k,
        "expected": 0,
        "tag": "edge8"        
    },
    {
        "arr": [TV.nom_a]*(TV.nom_l),
        "k": TV.min_k,
        "expected": TV.nom_l * (TV.nom_l-1) // 2,
        "tag": "edge9"        
    },
    {
        "arr": [TV.nom_a]*(TV.nom_l),
        "k": TV.min_k+1,
        "expected": 0,
        "tag": "edge10"        
    },
    {
        "arr": [TV.nom_a]*(TV.nom_l),
        "k": TV.max_k,
        "expected": 0,
        "tag": "edge11"        
    },
    {
        "arr": [TV.nom_a]*(TV.nom_l),
        "k": TV.max_k-1,
        "expected": 0,
        "tag": "edge12"        
    },
    {
        "arr": [TV.nom_a]*(TV.nom_l),
        "k": TV.max_k-1,
        "expected": 0,
        "tag": "edge12"        
    },
    {
        "arr": [],
        "k": TV.max_k-1,
        "expected": "error",
        "tag": "edge12"        
    },
    {
        "arr": [TV.nom_a] * (TV.max_l + 33),
        "k": TV.nom_k,
        "expected": "error",
        "tag": "dec1"        
    },
    {
        "arr": [TV.nom_a] * (TV.min_l - 2),
        "k": TV.nom_k,
        "expected": "error",
        "tag": "dec2"        
    },
    {
        "arr": [TV.min_a-2] * (TV.nom_l),
        "k": TV.nom_k,
        "expected": "error",
        "tag": "dec3"        
    },
    {
        "arr": [TV.max_a+2] * (TV.nom_l),
        "k": TV.nom_k,
        "expected": "error",
        "tag": "dec4"        
    },
    {
        "arr": [TV.nom_a] * (TV.nom_l),
        "k": TV.max_k+2,
        "expected": "error",
        "tag": "dec5"        
    },
    {
        "arr": [TV.nom_a] * (TV.nom_l),
        "k": TV.min_k-2,
        "expected": "error",
        "tag": "dec6"        
    },
    {
        "arr": [1, 2, 3, 3, 3, 4, 5, 5, 5, 102, 103] * 4,
        "k": 2,
        "expected": 208,
        "tag": "dec7"        
    },
    {
        "arr": [1, 2, 3, 3, 3, 4, 5, 5, 5, 102, 104, 103] * 4,
        "k": 2,
        "expected": 224,
        "tag": "dec8"        
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

    