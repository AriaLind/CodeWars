def divisors(integer):

    numbers = []

    for i in range(integer):
        if (i < 2 or i == integer):
            continue
        
        if (integer % i == 0):
            numbers.append(int(integer / i))
            print(f"Iter {i}: {integer / i}")

    if (len(numbers) == 0):
        return f"{integer} is prime"

    return numbers[::-1]