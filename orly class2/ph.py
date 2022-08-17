# input age

age=int(input("please enter age:"))

if age>=0 and age<=18:
    print("chiled")
elif age>=19 and age<=60:
    print("adult")
elif age>=61 and age<=120:
    print("senior")

