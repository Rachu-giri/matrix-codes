def largest(arr, n):
    max = arr[0]
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max


arr = [20,5,55,34,70]
n = len(arr)
solution = largest(arr, n)
print("Largest in given array ", solution)