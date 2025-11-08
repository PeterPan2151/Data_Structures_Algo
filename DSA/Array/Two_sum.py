def two_sum(arr, target):
    nums_dict = {}
    for i, j in enumerate(arr):
        remaining = target - j

        if remaining in nums_dict:
            return [nums_dict[remaining], i]
        
        nums_dict[j] = i
        
arr = [1, 7, 3, 2]
target = 9
print(two_sum(arr, target))
