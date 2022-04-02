#Karatsuba Algorithm
#x and y are both given with the same length
#Math from course

def karatsuba(x,y):
    n = len(str(x))
    half = n // 2
    A = x // (10 ** (half))
    B = x % (10 ** (half))
    C = y // (10 ** (half))
    D = y % (10 ** (half))
    AC = A * C
    BD = B * D
    ADBC = (A * D) + (B * C)
    return AC * (10 ** (2 * half)) + (ADBC * (10 ** half)) + BD

print(karatsuba(3141592653589793238462643383279502884197169399375105820974944592, 2718281828459045235360287471352662497757247093699959574966967627))

#Double Check answer
print(3141592653589793238462643383279502884197169399375105820974944592 * 2718281828459045235360287471352662497757247093699959574966967627)
