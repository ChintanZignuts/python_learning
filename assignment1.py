N=input("enter the number ");

def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n ** 0.5)+1):
        if n%i==0:
            return False
    return True

prime=[]
num=2
while len(prime)<int(N):
    if is_prime(num):
        prime.append(num)
    num=num+1

sum=sum(prime)

print(sum,"is the sum of the first",N,"prime numbers")