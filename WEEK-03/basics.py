# inta = 12
# floatb = 24.3
# stings = "65"
# sum = inta+floatb
# print(sum)
# print(type(stings))
# st2 = int(stings)
# sum += st2
# print(sum)
# print(type(sum))

# def check(n1,n2,s):
#     sum = n1+n2
#     return sum
# s = check(int(input("enter n1:")),int(input("enter n2:")),input("enter string:"))
# print(s)


def check(n1,n2,s):
    sum = n1+n2
    sum = sum + int(s)
    return sum
s = check(int(input("enter n1:")),float(input("enter n2:")),input("enter string:"))
print(s)
print(type(s))