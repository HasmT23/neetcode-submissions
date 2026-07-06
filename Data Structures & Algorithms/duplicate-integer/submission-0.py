class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashseen = set()

        for n in nums:
            if n in hashseen:
                return True
            hashseen.add(n)
        return False
            
            