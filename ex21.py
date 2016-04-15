def add(a, b):
    print "ADDING %d + %d "  %(a, b)
    return a+b

def substract(a, b):
    print "SUBSTRACTING %d -%d "%(a, b)
    return a-b
	
def multiply(a, b):
    print "MULTUPLYING %d * %d" %(a, b)
    return a*b

def divide(a, b):
    print "DIVIDING %d / %d "%(a, b)
    return a/b

print "LET'S DO SOME MATH WITH JUST FUNCTIONS!"

 
a1 = float(raw_input("enter the a and b \n>>"))
b1 = float(raw_input())

age = add(a1,b1)
height = substract(a1,b1)
weight = multiply(a1,b1)
iq = divide(a1,b1)

print "Age: %d, Height :%d , Weight: %d ,IQ: %d."%(age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.

print "Here is a puzzle."

what = add(age, substract(height, multiply(weight, divide(iq,2))))

print "That become:", what, "Can you do it by hand?"
