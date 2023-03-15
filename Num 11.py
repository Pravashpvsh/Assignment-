#Write a program to print the following pattern:

for p in range(1,6):
    s=1
    for s in range(1,p+1):
        print("*",end = ' ')
    print()
for p in range(6,1,-1):
    s=1
    for s in range(1,p-1):
        print("*",end = ' ')
    print()
