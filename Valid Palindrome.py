class Solution:
    def isPalindrome(self, s: str) -> bool:
        list1=[]
        for i in s:
            if i.isalpha() or i.isdigit():
                list1.append(i.lower())
        return list1==list1[::-1]
