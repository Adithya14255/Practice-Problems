#hackerrank id: https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true
if __name__ == '__main__':
    check = {"alphanum":False, "alpha":False, "digit":False, "lower":False, "upper":False}
    s = input()
    for i in str(s):
        if i.isalpha():
            check["alpha"]=True
            check["alphanum"]=True
            if i.isupper():
                    check["upper"]=True
            else:
                    check["lower"]=True
        if i.isdigit():
                check["digit"]=True
                check["alphanum"]=True
                
    print(*check.values(),sep="\n")