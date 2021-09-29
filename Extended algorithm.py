print("To Solve the Extended Euclidean Algorithm")
a = int(input("Type the first number here:"))
b = int(input("Type the second number here:"))
def eea(a,b):
    if( a == 0):
        return b, 0, 1
    else:
        gcd, x, y = eea(b % a , a)
        return gcd, y - (b // a) * x, x

gcd, x, y = eea(a,b)
print("The GCD is", gcd)
print(f"The coefficient of a = {x}, The coefficient of b = {y}")