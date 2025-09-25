# recursive approach
valid_parenthesis_set = set()

def generate_parenthesis(limit,n,curr):
    if len(curr) == limit*2:
        valid_parenthesis_set.add(curr)
    if n>0:
        generate_parenthesis(limit,n-1,"()"+curr)
        generate_parenthesis(limit,n-1,"("+curr+")")
        generate_parenthesis(limit,n-1,curr+"()")
    return

number = int(input("Enter number of pairs = "))
result = generate_parenthesis(number,number,"")
print("for ",number,"pairs = ",valid_parenthesis_set)