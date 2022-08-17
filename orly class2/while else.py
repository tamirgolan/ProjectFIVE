#
# grade=int(input("please enter number:"))
# count_invalid=0
#
#
# while 0<grade<=100:
#     count_invalid+=1
#     if count_invalid==5:
#         break
#     print("please insert more greade")
#     grade = int(input("please enter number:"))
#
# else:
#     print("invalid grade")
# ------------------------------------------------------------------------------------------
# grade=int(input("please enter number:"))
# count_test=0
#
#
# while 0<grade<=100:
#     count_test+=1
#     if count_test==5:
#         break
#     print("please insert more greade")
#     grade = int(input("please enter number:"))
#
# else:
#     print("invalid grade")
# ------------------------------------------------------------------------------------------
# for i in range(1,10):
#     print(i)
# ------------------------------------------------------------------------------------------
# for i in range(10,1,-1):
#     print(i)
# ------------------------------------------------------------------------------------------
# for i in range(0,99,3):
#     print(i)
# ------------------------------------------------------------------------------------------
# for i in range(1000,99,-3):
#     print(i)
# ------------------------------------------------------------------------------------------
# for i in range (0,260,2):
#     print(i)
# total=0
# count=0
# ------------------------------------------------------------------------------------------
# for i in range(6):
#     num=int(input(f"please enter number{i+1}:"))
#     total+=num
#     count+=1
#
#
# print("total",total)
# print("average",total/count)
# ------------------------------------------------------------------------------------------
#
# total=0
# count=0
#
# for i in range(6):
#     num=int(input(f"please enter number{i+1}:"))
#     if num%2==0:
#         total+=num
#         count+=1
#
#
#
# print("total",total)
# print("average",total/count)
# for i in range(10,99):
#     if i%10==7:
#         print(i)
# ------------------------------------------------------------------------------------------
# total=0
# count=0
# for i in range(10,100):
#     if i%10==0:
#         total+=i
#         count+=1
# print(total)
# ------------------------------------------------------------------------------------------
# grade = int(input(f"please enter grade :"))
# sum=0
# count=0
# count_1=0
# sum_faill=0
#
# while 0<=grade<=100:
#     if grade>=60:
#         sum+=grade
#         count+=1
#     else:
#         sum_faill+=grade
#         count_1+=1
#     grade = int(input(f"please enter grade :"))
#
#
#
# print(sum/count)
# print(sum_faill/count_1)
#
# # ------------------------------------------------------------------------------------------
# count=0
# sum=0
#
# for i in range(0,5):
#     num=int(input(f"please enter number {i+1}:"))
#     if 10<=num:
#         num=num%10
#         sum+=num
#         count+=1
#
# print(sum)
#
# num=int(input("please enter num:"))
#
# for i in range(1,num+1):
#     if i%5==0:
#         print(i)
#
#
# # ------------------------------------------------------------------------------------------
# num=int(input("please enter num:"))
#
# for i in range(2,num+1):
#     if i%2==0:
#         print(i)
#
# num=int(input("please enter number:"))
# count=0
# count_2=0
# while 0!=num:
#     num = int(input("please enter number:"))
#     if num%7==0:
#         count+=1
#     else:
#         if num%3==0:
#             count_2+=1
#
# print(count+count_2)
# num=int(input("please enter num:"))
# num2=int(input("please enter num:"))
# for i in range (num,num2):
#     if i % 2== 0:
#         print(i)
# -----------------------------------------------------------------------------------------------------------------------
# num=int(input("please enter num:"))


# for i in range(2,num):
#     if num%i==0:
#         print("not prime number")
#         break
# else:
#     print("prime number")

# from random import randint
# num_rand=randint(1,9)
# num=int(input("please enter number:"))
#
#
# while num_rand!=num:
#     if num>num_rand:
#         print("you went to hige")
#     if num<num_rand:
#         print("you went to low")
#
#     num = int(input("please enter number:"))
#
# else:
#     print("lucky number")



#
# from random import randint
# guss=randint(1,100)
# num=int(input("please enter number:"))
# counter=0
# counter_dos=0
#
#
# while num_rand!=num:
#     if num>num_rand:
#         print("you went to hige")
#         counter_dos+=1
#     if num<num_rand:
#         print("you went to low")
#         counter+=1
#
#     num = int(input("please enter number:"))
#
# else:
#     print("lucky number")
#     print(counter+counter_dos)


from random import randint
num=int(input("please enter number betwin 1 and 100:"))
count=0

while num>=1 and num<=100:
    num2=randint(1,100)
    count+=1
    if num==num2:
        print(count+1)
    break





















































