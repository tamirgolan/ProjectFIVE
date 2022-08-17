# please input day/month/year

day=int(input("please enter day:"))
month=int(input("please enter month:"))
year=int(input("please enter year:"))
year2=int(input("please enter: "))

if 1<=day<=31:
    if 1<=month<=12:
        if 1960<=year<=2020:
            print(f" {day}/{month}/{year%10}{year2//10%10}")
        else:
            print("invalid year")
    else:
        print("invalid month")
else:
    print("inavlid day")











