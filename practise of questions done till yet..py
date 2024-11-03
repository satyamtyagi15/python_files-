#programme to find sum of first n numbers.
a=int(input('Enter the num upto which you want to find sum of first n numbers:'));
sum=0;
i=1;
while i<=a:
    sum=sum+i;
    i=i+1;
print(sum);

#programme to find sum of first n even numbers.
a=int(input('Enter the num upto which you want to find sum of first n even numbers:'));
i=1;
sum=0;
count=1;
while count<=a:
    if i%2==0:
        count=count+1;
        sum=sum+i;
    i=i+1;
print(sum);
#programme to find sum of digits of a num entered by user.
a=int(input('Enter the num to find sum:'));
sum=0;
while a>0:
    sum=sum+a%10;
    a=a//10;
print(sum);
#programme to find sum of squares of digits of a given number.
a=int(input('Enter the num to find sum:'));
sum=0;
while a>0:
    sum=sum+(a%10)**2;
    a=a//10;
print(sum);

#programme to check whether a number is armstrong number or not.
b=a=int(input('Enter the number to check whether a num is armstrong num or not:'));
sum=0;
count=0;
while a>0:
    a=a//10;
    count=count+1;
a=b;
while a>0:
    sum=sum+(a%10)**count;
    a=a//10;
if sum==b:
    print('your num is an armstrong num');
else:
    print('your num is not an armstrong num');

#programme to find product of digits.
a=int(input('Enter the num to find product of its digits:'));
product=1;
while a>0:
    product=product*(a%10);
    a=a//10;
print('product of the digits of your num:',product);

#programme to find sum of even and product of odd digits of a num;
a=int(input('Enter the number to find sum of even while product of its odd digits:'));
sum=0;
product=1;
while a>0:
    digit=a%10;
    if digit%2==0:
        sum=sum+digit;
    else:
        product=product*digit;
    a=a//10;
print('sum of the even digits of your number:',sum);
print('product of the odd digits of your num:',product);
#progamme to find the reverse of a number;
a=int(input('Enter the number to find its reverse:'));
rev=0;
while a>0:
    rev=rev*10+a%10;
    a=a//10;
print('reverse of your number is:', rev);

#programme to check whether a number is pallindrome or not.
b=a=int(input('Enter the number to check whether it is pallindrome or not:'));
reverse=0;
while a>0:
    reverse=reverse*10+(a%10);
    a=a//10;
if reverse==b:
    print('your num is pallindrome');
else:
    print('your num is not pallindrome');

#programme to check whether a number is prime number or not.
a=int(input('Enter the number to check whether it is prime or not:'));
i=1;
count=0;
while i<=a:
    if a%i==0:
        count=count+1;
    i=i+1;
if count==2:
    print('your num is a prime number');
else:
    print('your num is not a prime number');

#programme to find factorial of a number entered by user.
a=int(input('Enter the number to find its factorial:'));
factorial=1;
while a>0:
    factorial=factorial*a;
    a=a-1;
print('The factorial of your number is :',factorial);

#programme to print fibonacci series;
a=int(input('Enter the number upto which you want to print fibonacci series:'));
x=0;
y=1;
z=0;
while z<=a:
    print(z);
    x=y;
    y=z;
    z=x+y;

#code shippet of a code consisting of nested loop;
i=1;
while i>5:
    j=1;
    while j<5:
        print(j);
        j=j+1;
    i=i+1;

        







    





        

    


        
        









    





    



    















    
     









    






