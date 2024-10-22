def loop(num):
    result = 0
    for i in range(num):
        result += i
    finresult = result + num
    return finresult



user_num = int(input("Enter A number: "))




print(loop(user_num))
