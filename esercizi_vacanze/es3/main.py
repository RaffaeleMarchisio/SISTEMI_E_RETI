N=int(input('Quanti numeri?: ' ))
a,b=1,1
print(a, end=' ')
print(b, end=' ')

for i in range(N):
    c=a+b
    a=b
    b=c
    print(c, end=' ')