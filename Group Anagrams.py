class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m=[]
        purse=dict()
        for i in strs:
            k=list(i)
            k.sort()
            if str(k) not in purse:
                m.append([i])
                purse[str(k)]=m.index([i])
            else:
                m[purse[str(k)]].append(i)
        return m
        
        
            
