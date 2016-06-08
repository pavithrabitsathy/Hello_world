# 96
count=0
num=input("enter a number")
a=num
while(a!=0):
 a=a/10
 count=count+1
print(count)
fdigit=num
ldigit=num
while(count>1):
 fdigit=fdigit/10
 ldigit=ldigit%10
 count=count-1
print(fdigit)
print(ldigit)
