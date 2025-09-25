# can also do with slow, fast pointer or saving outputs (look for repetition with a set)

def check_happy_number(n):
    # exit checks
    print(n)
    if n == 1:
        return True
    if n == 4:
        return False
    temp = n
    sum_of_squares = 0
    
    # find next happy number
    
    while temp>0:
        digit = temp%10
        sum_of_squares += digit * digit
        temp //=10
    
    return check_happy_number(sum_of_squares)

number = int(input("Enter your input number = "))
result = "true" if check_happy_number(number) else "false"
print("for ",number," = "+result)