# level-2;
#Programme to find sum of even digits as well as product of odd digits of a number.
b=a=int(input('Enter any desired number:'));
Sum=0;
Product=1;
while a>0:
    digit=a%10;
    if digit%2==0:
        Sum=Sum+digit;
    else:
        Product=Product*digit;
    a=a//10;
print('Sum of all the even digits in Your Number is:',Sum,'and Product of all the odd digits in your Number is:',Product,);


