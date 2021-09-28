print("To find gcd")
a = int(input("Type the first number here:"))
b = int(input("Type the second number here:"))
def gcd(a,b):
    if( b == 0):
        return a
    else:
        return gcd(b, a % b)
print("The gcd of a and b is:",gcd(a,b))