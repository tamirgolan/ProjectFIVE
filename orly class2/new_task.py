grade=int(input("please enter number:"))

while grade<=0 or grade>=100:
    print("inavlied grade")
    grade = int(input("please enter number:"))

if grade>=70:
    print("pass")
else:
    print("faild")
