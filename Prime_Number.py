def check_prime(n):
    i=2
    c=0
    check = True
    while(i<=n/2):
        if(n%i==0):
            check = False
        i+=1
    return check

num = int(input())

for i in range(2,num):
    if(check_prime(i)):
        print(i)