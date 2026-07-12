class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        for n in nums:
            new_num = nums + nums
        return new_num
            
        