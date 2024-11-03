# programme to find the sum of squares of first n num.
a=int(input('ENTER THE NUM UPTO WHICH YOU WANT TO FIND SUM OF SQUARES OF NATURAL NUM: '));
Sum=0;
i=1;
while i<=a:
    Sum=Sum+i*i;
    i=i+1;
print('SUM OF SQUARES OF NATURAL NUM UPTO',a,'IS: ', Sum,);

# ALTERNATE WAY.
a=int(input('ENTER THE NUM UPTO WHICH YOU WANT SUM OF SQUARES OF ALL NATURAL NUM: '));
Sum=0
while a>0:
    Sum = Sum+a*a;
    a=a-1;
print('SUM OF SQUARES OF NUM IS',Sum);

#NOTE: SIMILAR CODE CAN BE USED TO FIND CUBE OF NATURAL NUMBERS UPTO N.
#(JUST IN 1ST CODE MULTIPLY 'i' 3 TIMES AND IN 2ND CODE MULTIPLY 'a' 3 TIMES.)


