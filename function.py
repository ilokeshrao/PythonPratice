
def avg():
    print("Jai Shree Ram")

avg()


def avg(name,ending):

    print("Jai Shree Ram " + name)
    print(ending)

avg("Lokesh" ,"thankuu")
avg("Depuuu" ,"thankuu yr")


def fact():
    n = int(input("Enter number: "))

    f = 1
    for i in range(1, n + 1):
        f *= i

    print("Fact =", f)

fact()


def grater(a,b,c):
   
    if(a>b and a>c):
      return a
    elif(b>c and b>a):
      return b
    elif(c>a and c>b):
      return c


a=  3
b= 4
c= 7

print(grater(a,b,c) )  



