x=input()
if '.' in x:
    x=float(x)
else:
    x=int(x)
k=int(input())
print('runing')
for i in range(0,k+1):
    print(pow(x,i))
