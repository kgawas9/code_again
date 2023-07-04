"""
Find the position in array
"""

def find_pos(arr, num_to_find_pos):
    sorted_list = sorted(arr)
    print(sorted_list)
    try:
        start_index = sorted_list.index(num_to_find_pos)

        for i in sorted_list[start_index:]:
            if i > num_to_find_pos:
                end_index = sorted_list.index(i) - 1
                break

        return [start_index, end_index]
    except:
        return [-1, -1]


if __name__ == '__main__':
    arr_list = [1,4,5,7,3,4,5,4,5,3,0,9]
    num = 5
    result = find_pos(arr_list, num)
    print(result)