

a=int(input("Enter the first no: "))
b=int(input("Enter the second no: "))
c=int(input("Enter the third no: ")) 

if a>b and a>c:
    max=a;
elif b>a and b>c:
    max=b;
else:
    max=c;
    print("Maximum Number:",max)
             
        