def dir_reduc(arr):
    original_arr = arr.copy()

    for x in range(len(arr) - 1):
        if arr[x] == "NORTH":
            if arr[x + 1] == "SOUTH":
                arr.pop(x)
                arr.pop(x)
                break
        if arr[x] == "SOUTH":
            if arr[x + 1] == "NORTH":
                arr.pop(x)
                arr.pop(x)
                break
        if arr[x] == "EAST":
            if arr[x + 1] == "WEST":
                arr.pop(x)
                arr.pop(x)
                break
        if arr[x] == "WEST":
            if arr[x + 1] == "EAST":
                arr.pop(x)
                arr.pop(x)
                break

    if arr == original_arr:
        return arr
    else:
        return dir_reduc(arr)
