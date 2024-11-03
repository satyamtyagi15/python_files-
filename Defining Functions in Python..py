#Programme to Define Functions:
def message():
    print('Hello Shivam');
message();

#Programme to Add 2 Numbers Using Functions:
def add():
    x=int(input('Enter The First Number:'));
    y=int(input('Enter The Second Number:'));
    print('Addition Of Your Numbers ',x ,'and',y,'=',x+y);
add();
#Programme to Add 2 Numbers  Using Functions with Parameters:
def Add(a,b):
    print('Addition of',a,'and',b,'=',a+b);
#now to run above code we need values of 'a' and 'b' from user therefore:
a=int(input('Enter The First Number:'));
b=int(input('Enter The Second Number:'));
Add(a,b);
    
