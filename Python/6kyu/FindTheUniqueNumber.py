from collections import Counter

def find_uniq(arr):
    counts = Counter(arr)
    for num in counts:
        if counts[num] == 1:
            return num
