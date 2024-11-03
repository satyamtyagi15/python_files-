#level-2;
#Q2) programme to find sum of squares of digits of given number entered by user.
a=int(input('Enter The Number Whose  Square Of Digits You Want To Add:'));
Sum=0;
while a>0:
    Sum=Sum+(a%10)**2;
    a=a//10;
print('Sum of the Square of Digits of the Number Entered by You: ',Sum,);

#Note: If you want to find the Sum of the Cubes of the Digits of the Entered Number just replace the '2'in above code with '3'.

