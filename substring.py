# hackerrank id https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true
def count_substring(string, sub_string):
    count=0
    temp=0
    stridx=0
    while stridx<len(string):
        if sub_string[temp]==string[stridx]:
            stridx+=1
            temp+=1
            if temp==len(sub_string):
                count+=1
                stridx-=temp-1
                temp=0
        else:
            stridx+=1
            temp=0
    return count
        

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)