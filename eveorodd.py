number=int(input("enter the number:"))
print(number)
last_digit=number%10
if(last_digit == 0 or last_digit == 2 or last_digit == 4 or last_digit == 6 or last_digit == 8):
    print("number is even")
else :
    print("the number is odd")
