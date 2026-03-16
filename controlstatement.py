#write a script that checks if someone is eligible to vote
age=int(input("Enter age: "))

if age>=18:
    print("you are eligible to vote")
else:
    print("you are not viable to vote.underage.....")
    #Write a script that checks if a number is odd or even
    number=int(input("enter number"))
    if number % 2 ==0:
        print(f"{number } is even number")
    else:
        print(f"{number} is odd number")


#write a script that check("python123") is valid
#else wrong password
password=input("enter the password:")
if password=="python123":
    print("valid password")
else:
    print("wrong password") 
    #write a script that checks the largest number of the three number
    num1=int(input("enter the first number:"))
    num2=int(input("enter the second number:"))
    num3=int(input("enter the third number:"))
if num1>num2 and num1>num3:
    print(f"{num1}is the largest number")
elif num2>num1 and num2>num3:
    print(f"{num2} is the largest number")
elif num3>num1 and num3>num2:
    print(f"{num3}is the largest number")
else:
    print("they are equal ")

