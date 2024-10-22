def counting(num):
    result = 0
    for i in range(num):
        result = result + i
    finresult = result + num
    return finresult

def script():
    user_num = int(input("Enter A Number: "))
    choice = "f"
    if choice.lower() == "f":
        print(counting(user_num))
    elif choice.lower() == "w":
        result = 0
        i = 0
        while i < user_num:
            result += i
            i +=1

        finresult = result + user_num
        print(finresult)

        
script()

restart = str(input("Restart? y/n: "))
if restart.lower() == "y":
    script()
else:
    print("byeee")

#for Summation code here
