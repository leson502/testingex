
def count_diff(arr: list, k: int):
    table = {}
    result = 0

    assert 10**5 >= len(arr) > 0, "array must be not empty"
    assert 1000 >= k >= 0, " 0<= k < 1000"

    for num in arr:
        assert 10**9 >= num > 0, "0 < Arr[i] <= 10^9"
        if num not in table:
            table[num] = 1
        else:
            table[num] += 1
    
    if k == 0:
        for item in table:
            result += table[item] * (table[item] - 1) // 2
        return result
    
    for item in table:
        if (item - k) in table:
            result += table[item - k] * table[item]

    return result


if __name__ == "__main__":
    print(count_diff([1, 2, 3, 3, 3, 4, 5, 5, 5, 102, 103, 104] * 4, 2))
    
    
