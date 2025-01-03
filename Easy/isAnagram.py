class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sumOne = 0
        sumTwo = 0

        for i in range(len(s)):
            sumOne += ord(s[i])
            sumTwo += ord(t[i])
        
        if sumOne == sumTwo:
            return True
        
        return False
    
print("fe and ja: " + str(Solution.isAnagram(Solution, "fe", "ja")))