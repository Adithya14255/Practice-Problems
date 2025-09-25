# simple stack implementation

def validate_string(string):
    if len(string) <= 1:
        return False
    stack = []
    opening_brackets = ['(','[','{']
    for bracket in string:
        if bracket in opening_brackets:
            stack.append(bracket)
        else:
            if len(stack) == 0:
                return False
            if (bracket == ')' and stack[-1] == '(') or (bracket == ']' \
                and stack[-1] == '[') or (bracket == '}' and stack[-1] == '{'):
                stack.pop(-1)
            else:
                return False
    if len(stack) > 0:
        return False
    else:
        return True

            
input_string = input("Enter your input = ")
result = "true" if validate_string(input_string) else "false"
print("for "+input_string+" = "+result)