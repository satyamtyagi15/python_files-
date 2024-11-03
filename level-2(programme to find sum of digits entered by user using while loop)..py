#LEVEL-2:QUESTIONS;
#1)PROGRAMME TO FIND SUM OF DIGITS OF A NUMBER ENTERED BY USER.
a=int(input('ENTER THE NUM WHOSE DIGITS YOU WANT TO ADD.'));
Sum=0;
while a>0:
    Sum=Sum+a%10;
    a=a//10;
print('Sum of the Digits of the Number Entered by You is',Sum,);
