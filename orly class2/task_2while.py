# please enter age

age=int(input("please enter number:"))

while 0<=age<=120:
    if 0<=age<=18:
        print("child")
    if 19<=age<=60:
        print("adult")
    if 61<=age<=120:
        print("senior")
    age = int(input("please enter number:"))
    






















