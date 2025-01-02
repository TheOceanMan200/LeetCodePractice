class Solution:
    def hasDuplicate(self,nums) -> bool:
        placeholder = []
        for num in nums:
            if num in placeholder:
                return True
            placeholder.append(num)
        return False

print("IS THERE A DUPE IN [1,2,3,4]? "+ str(Solution.hasDuplicate(Solution, [1,2,3,3])))