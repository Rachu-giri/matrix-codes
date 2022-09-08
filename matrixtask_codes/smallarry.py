arr = [5,88,7,4,3,2,1]

min = arr[0]

for i in range(0, len(arr)):

    if(arr[i] < min):
        min = arr[i]

print("Smallest number in given array: " + str(min))