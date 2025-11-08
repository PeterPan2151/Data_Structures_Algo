def check_duplicate(arr):
    nums_set = set()
    for i in arr:
        if i in nums_set:
            return True
        else: 
            nums_set.add(i)

    return False


nums = [1, 4, 3, 5, 1]
print(check_duplicate(nums))
