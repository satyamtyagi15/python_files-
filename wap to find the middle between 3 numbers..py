# WAP TO FIND THE MIDDLE NUM AMONG THE 3 GIVEN NUM.
a=int(input('ENTER YOUR NUM:'));
b=int(input('ENTER YOUR NUM:'));
c=int(input('ENTER YOUR NUM:'));
if (a>b and a<c) or (a>c and a<b):
    print(a , 'the middle num');
elif (b>a and b<c) or (b>c and b<c):
    print(b, 'is the middle num');
else:
    print(c, 'is the middle num');
    
