#level-2;
#Programme to find the Product of the given Number.
a=int(input('Enter the num whose Product of digits You want to Obtain.'));
product=1;
while a>0:
    product=product*(a%10);
    a=a//10;
print('Product of the digits of the Number Entered is: ',product);
