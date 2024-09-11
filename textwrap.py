#https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true
def wrap(string, max_width):
    string1=""
    temp=0
    for i in range(max_width,len(string),max_width):
        string1+= string[temp:i]+"\n"
        temp+=max_width
    string1+= string[temp:]
    return string1


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)