#Function  to Add Programme Using return statement using Parameters:
def add(a,b):
    return a+b;
x=int(input('Enter the 1st Number to Add:'));
i=int(input('Enter the 2nd Number to Add:'));
z=add(x,i);
print(z);

#Function to Add Programme Using REURN statement without Passing Parameters:
def addition():
    a=int(input('Enter 1st Number to Add:'));
    b=int(input('Enter 2nd Number to Add:'));
    return(a+b);
x=addition();
print('Addition Of Your Numbers=',x);
