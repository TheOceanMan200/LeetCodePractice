def twoSum(nums, target: int):
    complement = {}

    for i,j in enumerate(nums):
        if target - j in complement:
            return [complement[target - j], i]
        complement[j] = i
    return []

print("Two sum of [20, 30, 40, 50] is " + str(twoSum([20, 30, 40, 50], 70)))