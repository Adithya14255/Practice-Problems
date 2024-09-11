# https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true
N,M = map(int,input().split())
for j in range(N//2,0,-1):
    temp=".|"
    if j!=N//2:
            temp = temp + "..|"*(2*(N//2-j))
    temp+="."
    print('-'*(j*3)+temp+'-'*(j*3))
print('-'*((N//2)*3-2)+"WELCOME"+'-'*((N//2)*3-2))
for j in range(1,(N//2)+1):
    temp=".|"
    if j!=N//2:
            temp = temp + "..|"*(2*(N//2-j))
    temp+="."
    print('-'*(j*3)+temp+'-'*(j*3))