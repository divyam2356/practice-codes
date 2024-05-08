def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example usage:
arr = [3, 5, 1, 8, 2, 7, 4]
target = 8
index = linear_search(arr, target)
if index != -1:
    print(f"Target {target} found at index {index}.")
else:
    print("Target not found in the array.")
