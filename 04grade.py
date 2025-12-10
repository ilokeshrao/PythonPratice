
Marks  = int(input("Enter the marks : "))


if(Marks<=100 and Marks>=90):
    grade = "A"

elif(Marks<90 and Marks>=80):
    grade = "b"

elif(Marks<80 and Marks>=70):
    grade = "c"
elif(Marks<70 and Marks>=60):
    grade = "d"
elif(Marks<60 and Marks>=50):
    grade = "e"

elif(Marks<50):
    grade = "f"

print(" your grade is ",grade)
 