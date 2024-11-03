#level-2;
#Wap to check whether a programme is palindrome or Not.
#If The Reverse Of The Number Entered By User Is Same As The Number Itself Then, Such Number Is Known As Pallindrome.
b=a=int(input('Enter The Number To Check Whether The Num is Pallindrome Or Not: '));
reverse=0;
while a>0:
    reverse=(reverse*10)+(a%10);
    a=a//10;
if reverse==b:
    print('The Num Entered By You Is Pallindrome');
else:
    print('The Num Entered By you Is Not Pallindrome.');
