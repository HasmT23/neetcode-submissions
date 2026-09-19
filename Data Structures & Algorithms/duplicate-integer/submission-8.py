class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Set and intailize the hash set beaucse its a faster way to quickly find duplicates
        hashset = set()

        # next we simply loop the enitre array to find if our elements are in the hashset 
        for num in nums:
            # if num is in our hashset then we can just return ture because that means we have a duplicate 
            if num in hashset:

                return True
            # if we dont have a duplicate this means that we can add the element into our hashset 
            hashset.add(num)
        return False
            

