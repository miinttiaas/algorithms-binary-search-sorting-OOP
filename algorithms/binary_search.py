def binary_search(goal, low, high,counter=0):
    half = (high+low)//2
    print(f"№{counter} {half}")
    if half > goal:
        counter += 1
        return  1 + binary_search(goal, low, half,)
    elif half < goal:
        counter += 1
        return 1 + binary_search(goal, half, high,counter)
    return counter
print(binary_search(10, 1, 100))