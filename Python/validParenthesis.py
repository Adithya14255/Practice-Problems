class Solution:
    def isValid(self, s: str) -> bool:
        opening_stuff = ['(','[','{']
        closing_stuff = [')',']','}']
        temp_arr = []
        for i in s:
            if i in opening_stuff:
                temp_arr.append(i)
            elif i in closing_stuff and len(temp_arr):
                if opening_stuff.index(temp_arr[-1])==closing_stuff.index(i):
                    temp_arr.pop(-1)
                else:
                    return False
            else:
                return False
        return False if len(temp_arr) else True
