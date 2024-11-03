#level-2;
#Q3-Programme to check whether a Number is Armstrong Number or not using while loop.
#On adding the digits of the given number, each digit raised to the Power of Total No of Digits if we get the same number back then,that number is known as Armstrong Number.
b=a=int(input('Enter the Number to check whether the Number is Armstrong Number or not: '));
Sum=0;
while a>0:
    Sum=Sum+(a%10)**3;
    a=a//10;
if Sum==b:
    print('Your No is an Armstrong Number.');
else:
    print('Your No is not an Armstrong Number.');
    
    
    

