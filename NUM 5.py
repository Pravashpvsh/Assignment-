#Write a program to print the Fibonacci series. 

n=int(input("Enter a number of terms:"))
x=0
y=1
print(x,y,end=' \n')
for i in range(n-1):
    m=x+y
    print(m,end=' \n')
    x=y
    y=m
