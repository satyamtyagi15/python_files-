#Nested Loop-Pattern Printing.
#Programme to Print Stars in Pyramidal Shape.
a=int(input('Enter the number of Rows You Want:'));
i=1;
x=1;
while i<=a:
    spaces=1;
    while spaces<=a-i:
        print(' ',end='');
        spaces=spaces+1;
    j=1;
    while j<=x:
        print('*',end='');
        j=j+1;
    print();
    i=i+1;
    x=x+2;

#Programme to Print Numbers in Pyramidal Shape (Part-1).
a=int(input('Enter the Num of Rows you want:'));
i=1;
x=1;
while i<=a:
    j=1;
    spaces=1;
    while spaces<=a-i:
        print(' ',end='');
        spaces=spaces+1;
    while j<=x:
        print(j,end='');
        j=j+1;
    print();
    x=x+2;
    i=i+1;
#Programme to Print Numbers in Pyramidal Shape (Part-2);
a=int(input('Enter the Num of Rows You Want:'));
i=1;
x=1;
while i<=a:
    j=1;
    spaces=1;
    while spaces<=a-i:
        print(' ',end='');
        spaces=spaces+1;
    while j<=x:
        print(x,end='');
        j=j+1;
    print();
    x=x+2;
    i=i+1;

#Programme to Print Numbers in Pyramidal Shape (Part-3);
a=int(input('Enter the Num of Rows You Want:'));
i=1;
x=1;
while i<=a:
    j=1;
    spaces=1;
    while spaces<=a-i:
        print(' ',end='');
        spaces=spaces+1;
    while j<=x:
        print(i,end='');
        j=j+1;
    print();
    x=x+2;
    i=i+1;
    
























    
    
    
