#Programme to Print Stars in Right Triangular Shape in  both Reverse manner i.e. from Top to Bottom as well as Right to Left.
a=int(input('Enter the Num of Rows You Want:'));
x=a;
while a>0:
    j=1;
    spaces=x;
    while spaces>a:
        print(' ',end='');
        spaces=spaces-1;
    while j<=a:
        print('*',end='');
        j=j+1;
    print();
    a=a-1;
#Programme to print Numbers in Right Triangular Shape in both Reverse Manner i.e. from Right to left as well as Top to Bottom.
a=int(input('Enter the Num of Rows You Want:'));
x=a;
while a>0:
    j=1;
    spaces=x;
    while spaces>a:
        print(' ',end='');
        spaces=spaces-1;
    while j<=a:
        print(j,end='');
        j=j+1;
    print();
    a=a-1;
#Programme to Print Numbers in Right Triangular Shape in both Reverse Manner i.e. from Top to Bottom and Left to Right.(part-2);
a=int(input('Enter The Num of Rows You Want:'));
x=a;
while a>0:
    j=1;
    spaces=x;
    while spaces>a:
        print(' ',end='');
        spaces=spaces-1;
    while j<=a:
        print(a,end='');
        j=j+1;
    print();
    a=a-1;
#Programme to Print Stars in Pyramidal Shape in reverse order.
#Note: This Programme is giving You no of Stars in First Row = num of Rows ;
a=int(input('Enter the Number of Rows You Want:'));
x=a;
y=x;
while a>0:
    j=1;
    spaces=x;
    while spaces>y:
        print(' ',end='');
        spaces=spaces-1;
    while j<=a:
        print('*',end='');
        j=j+1;
    print();
    a=a-2;
    y=y-1;
#Now if You Want only specific Num of Rows let say '5', and Stars more than that of num of Rows let say '9' Therefore we have to edit our code accordingly.
a=int(input('Enter the num of Rows You Want :'));
x=a;
while a>0:
    j=1;
    spaces=x;
    while spaces>a:
        print(' ',end='');
        spaces=spaces-1;
    while j<=(a*2)-1:
        print('*',end='');
        j=j+1;
    print();
    a=a-1;

#Alternate Code for Printing Just Above Code.
a=int(input('Enter the Num of Rows You Want:'));
i=1;
while a>0:
    j=1;
    spaces=1;
    while spaces<i:
        print(' ',end='');
        spaces=spaces+1;
    while j<=(a*2)-1:
        print('*',end='');
        j=j+1;
    print();
    a=a-1;
    i=i+1;
#Programme to Print Numbers in Pyramidal Shape in Reverse Order.
a=int(input('Enter the Num of Rows You Want:'));
a=x;
while a>0:
    j=1;
    spaces=x;
    while spaces>a:
        print(' ',end='');
        spaces=spaces-1;
    while j<=(a*2)-1:
        print(j,end='');
        j=j+1;
    print();
    a=a-1;
#Alternate Way;
a=int(input('Enter the Num of Rows You Want:'));
i=1;
while a>0:
    j=1;
    spaces=1;
    while spaces<i:
        print(' ',end='');
        spaces=spaces+1;
    while j<=(a*2)-1:
        print(j,end='');
        j=j+1;
    print();
    a=a-1;
    i=i+1;
#Now For Next Part of This Pattern;
a=int(input('Enter the Num of Rows You Want:'));
x=a;
while a>0:
    j=1;
    spaces=x;
    while spaces>a:
        print(' ',end='');
        spaces=spaces-1;
    while j<=(a*2)-1:
        print(a,end='');
        j=j+1;
    print();
    a=a-1;
#Now if we want to Print from '1' and carry till '5' in above code instead of from '5' to '1'.
a=int(input('Enter The Num of Rows You Want:'));
x=a;
z=1;
while a>0:
    j=1;
    spaces=x;
    while spaces>a:
        print(' ',end='');
        spaces=spaces-1;
    while j<=(a*2)-1:
        print(z,end='');
        j=j+1;
    print();
    a=a-1;
    z=z+1;
#To Print the above code You can also just change the print statement in alternate way from 'j' to 'i';
#Like This:
a=int(input('Enter the Num of Rows You Want:'));
i=1;
while a>0:
    j=1;
    spaces=1;
    while spaces<i:
        print(' ',end='');
        spaces=spaces+1;
    while j<=(a*2)-1:
        print(i,end='');
        j=j+1;
    print();
    a=a-1;
    i=i+1;
    
    
    
    


    
    
    
            





















    

        







 








