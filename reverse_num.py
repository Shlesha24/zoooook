def reverse(string):
    str = ""
    for i in string:
        str = i + str
    return str 

string=input("enter a string:")
print("original string:{}".format(string))
print("reversed string:{}".format(reverse(string)))

