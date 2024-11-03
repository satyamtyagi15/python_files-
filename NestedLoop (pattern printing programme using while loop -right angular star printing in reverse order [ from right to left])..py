#Nested Loop;
#Programme to print stars in right triangular shape in reverse manner from right to left;
#Now here we have to pogramme this code according to the decreasing spaces.
a=int(input('Enter the num of rows you want :'));
i=1;
while i<=a:
    j=1;
    spaces=1;
    while spaces<=a-i:
        print(' ',end='');
        spaces=spaces+1;
    while j<=i:
        print('*',end='');
        j=j+1;
    print();
    i=i+1;

#Programme to Print Numbers in Reverse order from Right to Left.
a=int(input('Enter the num of rows you want:'));
i=1;
while i<=a:
    j=1;
    spaces=1;
    while spaces<=a-i:
        print(' ',end='');
        spaces=spaces+1;
    while j<=i:
        print(j,end='');
        j=j+1;
    print();
    i=i+1;

#Programme to print numbers in right angular shape in reverse order (part-2)from right to left. 
a=int(input('Enter the Number of Rows You Want:'));
i=1;
while i<=a:
    j=1;
    spaces=1;
    while spaces<=a-i:
        print(' ',end='');
        spaces=spaces+1;
    while j<=i:
        print(i,end='');
        j=j+1;
    print();
    i=i+1;
    
    



















    

    















