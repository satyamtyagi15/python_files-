# wap a programme to find sum of all the even num from 1 to n.
a=int(input('ENTER THE NUM UPTO WHICH YOU WANT TO ADD ALL THE EVEN NUM.'));
Sum=0;
i=1;
while i<=a:
    if i%2==0:
        Sum=Sum+i;
    i=i+1;
print('SUM OF YOUR EVEN NUM IS',Sum,);
# Alternate way.
a=int(input('ENTER NUM UPTO WHICH YOU WANT TO FIND SUM OF YOUR EVEN NUMBERS.'));
i=2;
Sum=0;
while i<=a:
    Sum=Sum+i;
    i=i+2;
print('SUM OF YOUR EVEN NOS IS ',Sum,);


