num=5
while num<=15:
    print(num)
    num+=2
    #create a script starting with 50
    num2=50
    secret=7
    guess=0
    while guess!=secret:
        guess=int(input("enter the number"))
        if guess==secret:
            print("correct")
        else:
            print("try again")
                
            