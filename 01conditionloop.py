# l = ["Lokesh", "Depuuu", "goluu", "Boss", "lokesh"]

# for a in l:
#     if a.lower().startswith("l"):
#         print(a)


N = int(input("Enter the number : "))


for i in range(2,N):
    if (N%i) ==0:
        print("this is  not prime")
        break
else:
    print("This is prime")
        

        