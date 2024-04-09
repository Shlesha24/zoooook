number = int(input("enter a number:"))
temp = number
l = len(str(number))
print(l)
sum = 0

for i in range(temp) :
    digit = temp % 10
    sum = sum + digit**l
    temp = temp // 10
print(sum)

if (sum == number):
    print("yes")
else:
    print("no")