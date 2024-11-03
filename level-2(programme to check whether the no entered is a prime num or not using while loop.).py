#Level-2;
#Question-Programme To Check Whether The Entered Number Is Prime Or Not.
a=int(input('Enter The Number To Check Whether It Is Prime Or Not: '));
i=1;
Count=0;
while i<=a:
    if a%i==0:
        Count=Count+1;
    i=i+1
if Count==2:
    print('The Num Entered By You Is a Prime Number.');
else:
    print('The Num Entered By You Is a Composite Number.');
    
