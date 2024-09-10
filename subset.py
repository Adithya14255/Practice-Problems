# https://www.hackerrank.com/challenges/py-check-subset/problem?isFullScreen=true
n = int(input())
a1 = [[int(input()),list(map(int,input().split()))] for i in range(n*2)]
for i in range(0,len(a1)-1,2):
    flag=0
    for j in a1[i][1]:
        if j not in a1[i+1][1]:
            print("False")
            flag=1
            break
    if flag==0:    
        print("True")