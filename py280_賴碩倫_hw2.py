#Homework 2
n=int(input("please insert a number:"))
print("Use \"for\"")

for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,'x',j,"=",i*j)
else:
    print("Use \"while\"")

a=1
b=1
while a<=n:
    while b<=n:
        print(a,'x',b,'=',a*b)
        b+=1
    a+=1
    b-=n
else:
    print('done')
