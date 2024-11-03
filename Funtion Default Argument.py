#Function Default Argument:
def add(a,b,c=1):
    return(a+b+c);
x=add(1,2,3);
i=add(1,2);
print('When All The Arguments are  Passed Addition =',x);
print('When All Required Arguments are not Passed Addition=',i);
#Note: If You Provide a Variable Default Argument From between then you would have to provide each variable an Default Argument.
