class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        a = []
        
        for i in nums:
            if -i in nums:
                a.append(i)
                
        a.sort()
        print(a)
        print(i)
        if i in a:
            return a[-1]
        else:
            return -1
num = [14,33,40,-33,8,-24,-42,30,-18,-34]
b = Solution()
print(b.findMaxK(num))