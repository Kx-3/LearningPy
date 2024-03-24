def sort_list(arr):
    sorted_list = []
    while len(arr) > 0:
        for i in range(len(arr)):
            if i == 0:
                min = arr[i]
            else:
                if arr[i] < min:
                    min = arr[i]
        sorted_list.append(min)
        arr.remove(min)
    print(sorted_list)
    print(arr)
        # print(f"{arr[i]} is at index {i}")

my_list = [34,5,76,8,3,6,7,12,54,234,32,53,65,32,4,6,8,78]
sort_list(my_list)