def num(a):
    if (a%2==0):
        print("even")
    else:
        print("odd") 
def leap(b):
    if (b%4==0):
        print("leap year")
    else:
        print("not a leap year")
def positiveornot(c):
    if(c>0):
        print("positive")
    elif(c<0):
        print("negative")
    else:
        print("zero")
def big(a,b,c):
    if(a>b) and (a>c):
        print(a," is big")
    elif(b>c):
        print(b,"is big")
    else:
        print(c,"is big")
def factorial(h):
    for i in h:
        f=1
        f=f*i
print(f)

