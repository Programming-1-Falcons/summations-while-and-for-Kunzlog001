def loop(num):
    result = 0
    i = 0
    while i < num:
        result += i
        i += 1
    finresult = result + num
    return finresult


user_num = int(input("Enter A number: "))




print(loop(user_num))
