class Solution:
    def isValid(self, s: str) -> bool:
        i=0
        opening_stuff = ['(','[','{']
        closing_stuff = [')',']','}']
        temp_arr = []
        while(i< len(s)):
            if s[i] in opening_stuff:
                temp_arr.append(s[i])
                i+=1
            elif s[i] in closing_stuff and len(temp_arr):
                if opening_stuff.index(temp_arr[-1])==closing_stuff.index(s[i]):
                    temp_arr.pop(-1)
                    i+=1
                else:
                    return False
            else:
                return False
        if not len(temp_arr):
            return True 
        else:
            return False
