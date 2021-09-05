class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern) != len(s.split()):
            return False
        words={}
        words2 = {}
        for i in range(len(pattern)):
            if pattern[i] not in words:
                words[pattern[i]] = s.split()[i]
        for k in words:
            words2[words[k]] = k
        for j in range(len(pattern)):
            if s.split()[j] not in words2:
                return False
            if words2[s.split()[j]] != pattern[j]:
                return False
        return True
        
