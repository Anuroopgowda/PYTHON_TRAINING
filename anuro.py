# def fibo(num):
#     num1=0
#     num2=1
#     # print(num1)
#     # print(num2)
#     lst=[]
#     lst.append(num1)
#     lst.append(num2)
#     for _ in range(num-2):
#         num1,num2=num2,num1+num2
#         lst.append(num2)
#     return lst
#
# flag=True
# while flag:
#     try:
#         number=int(input("enter the number:"))
#         flag=False
#     except:
#         print("enter a integer")
#
# result=fibo(number)
# print(" ".join(map(str,result)))

str1="Shikha is working in Wipro. She is from Jhanshi. Jhanshi is the automotive hub in India. Wipro is not having a office in Coimbatore"
str2="Wipro is HQ in Bangalore and it works in different domains like Automotive, aerospace etc. Wipro may open a centre in Jhanshi soon"
lst1=str1.split(" ")
lst2=str2.split(" ")
import re
lst3=[]
lst4=[]
for i in range(len(lst1)):
    if re.search(lst1[i],str2): 
        lst4.append(lst1[i])
        continue
    lst3.append(lst1[i])
print("the common words:",lst4)
print("common words removed in str1:"," ".join(map(str,lst3)))


