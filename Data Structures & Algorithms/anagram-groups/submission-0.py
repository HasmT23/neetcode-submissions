class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = defaultdict(list)
        
        for st in strs:
            sortedstr = "".join(sorted(st))
            result[sortedstr].append(st)
        return list(result.values())


            

    

        
            
        
     
        

