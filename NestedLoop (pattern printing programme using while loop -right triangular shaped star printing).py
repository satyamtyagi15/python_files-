
#Pattern Printing with help of Nested Loop using while loop.
#Q1-Printing Right Triangular Shape with stars using while loop.
a=int(input ('Enter No Of Rows You Want:'));
i=1;
while i<=a:
    j=1;
    while j<=i:
        print('*',end='');
        j=j+1;
    print();
    i=i+1;
    

#Q2-Printing Right Triangular Shaped Numbers Using while loop(part-1);
# This programme will Print Numbers increasing Column Wise With Same Number In Each Column.
a=int(input('Enter The Number Of Rows You Want:'));
i=1;
while i<=a:
    j=1;
    while j<=i:
        print(j,end='');
        j=j+1;
    print();
    i=i+1;

#Q3-Printing Right Triangular Shaped Numbers Using while loop(part-2);
#This programme will Print Numbers increasing Row Wise With Same Number In Each Row.
a=int(input('Enter The Number Of Rows You Want:'));
i=1;
while i<=a:
    j=1;
    while j<=i:
        print(i,end='');
        j=j+1;
    print();
    i=i+1;



    
    
    
