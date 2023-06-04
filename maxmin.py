test_arr = [5,2,0,-4,10,13,3]

def find_min(array):
    min = array[0]
    for i in range(len(array)):
        if array[i] < min:
            min = array[i]
    return min

def find_max(array):
    max = array[0]
    for i in range(len(array)):
        if array[i] > max:
            max = array[i]
    return max

def min_max_arr(min, max):
    return [min, max]
print(min_max_arr(find_min(test_arr), find_max(test_arr)))