# division is a bit weird with negative numbers

def solve_polish_notation(notation):
    if len(notation)<1:
        return "invalid expression"
    operators = ['+','-','*','/']
    if len(notation) == 1 and notation[0].isdigit():
        return notation[0]
    stack = []
    for char in notation:
        if char in operators:
            if len(stack) < 2:
                return "invalid expression"
            x = stack.pop(-1)
            y = stack.pop(-1)
            if char == '+':
                stack.append(y+x)
            elif char == '-':
                stack.append(y-x)
            elif char == '*':
                stack.append(y*x)
            elif char == '/':
                res = y/x
                if res<0 and res>-1:
                    res = 0
                    stack.append(res)
                else:
                    stack.append(y//x)

        else:
            stack.append(int(char))
    if len(stack) > 1:
        return "invalid expression"
    else:
        return stack[0]

            
tokens = list(map(str,input("Enter your tokens seperated by space = ").strip().split()))
print(tokens)
result = solve_polish_notation(tokens)
print("for ",*tokens," = ",result)