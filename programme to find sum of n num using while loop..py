# programme to find sum of n numbers.
a=int(input('ENTER THE NUMBER UPTO WHICH YOU WANT TO SUM:'));
Sum=0;
while a>0:
    Sum = Sum+a;
    a=a-1;
print(Sum);
# alternate way.
a=int(input('ENTER THE NUM UPTO WHICH YOU WANT TO SUM:'));
i=1;
Sum=0;
while i<=a:
    Sum=Sum+i;
    i=i+1;
print('sum of num upto',a, 'is',Sum,);

    
