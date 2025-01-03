#My Implemented Solution after 30 Minutes
class Solution:
    def threeSum(self, nums):
        result = []
        tracker = []

        for i,num in enumerate(nums):
            tracker = [num]
            j = i + 1
            while (j < len(nums)):
                tracker.append(nums[j])
                if sum(tracker) == 0 and tracker not in result and len(tracker) == 3:
                    result.append(tracker)
                    tracker = [num]
                elif len(tracker) == 3:
                    tracker = [num]
                j += 1
        return result
    
#Optimal Solution 

# class Solution:
#     def threeSum(self, nums):
#         nums.sort()  # Step 1: Sort the array
#         result = []

#         for i in range(len(nums)):
#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue  # Skip duplicates for the first element
            
#             target = -nums[i]
#             left, right = i + 1, len(nums) - 1

#             while left < right:
#                 current_sum = nums[left] + nums[right]

#                 if current_sum == target:
#                     result.append([nums[i], nums[left], nums[right]])
#                     left += 1
#                     right -= 1

#                     # Skip duplicates for the second and third elements
#                     while left < right and nums[left] == nums[left - 1]:
#                         left += 1
#                     while left < right and nums[right] == nums[right + 1]:
#                         right -= 1

#                 elif current_sum < target:
#                     left += 1
#                 else:
#                     right -= 1

#         return result

    
print("3Sum of [1,-1,-1,0]: " + str(Solution.threeSum(Solution, [1,-1,-1,0])))