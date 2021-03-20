def task(array):
    i = 0
    while (i <= len(array)):
        if (array[i] == '0'):
            print("First zero index is", i)
            break
        i += 1

print(task("111111111111111111111111100000000")) 
print("The complexity of this algorithm is O(n)")