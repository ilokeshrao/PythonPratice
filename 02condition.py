
marks1 =  int(input("enter the subject marks hindi  : "))

marks2 =  int(input("enter the subject marks chemistry : "))

marks3 =  int(input("enter the subject marks Math  : "))



total_parcentage =  (100*(marks1+marks2+marks3))/300

if (total_parcentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print(" You are the passed ",total_parcentage)

else:
    print("you are failed try to next year",total_parcentage)
    
       

