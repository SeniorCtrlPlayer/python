x=0 #x为合格人数统计
y=0 #y为不合格人数统计
#print("please input a standard num")
a=int(input())
b=input()
while b != ' ':
    b=int(b)
    if b>a:
        x+=1
    else:
        y+=1
    b=input()
print("合格率为""%.2f" %(x/(x+y)*100))
