#Level-2;
#Programme To Print Fibonacci Series.
a=int(input('Enter The Number Upto Which You Want To Print Fibonacci Series: '));
x=0;
y=1;
while x<=a:
    x=x+y;
    y=y+1;
    print(x);
    print(y);
    
