#Programme to find reverse of an entered Number using while loop.
a=int(input('Enter the Number whose Reverse You Want: '));
reverse=0;
while a>0:
    reverse=(reverse*10)+(a%10);
    a=a//10;
print('The Reverse of the Entered Number is:',reverse,);

