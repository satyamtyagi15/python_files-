#programme to find sum of first n even numbers.
a=int(input('ENTER THE NUM OF EVEN NUM YOU WANT TO ADD:'));
i=2;
Sum=0;
count=1;
while count<=a:
    Sum=Sum+i;
    count=count+1;
    i=i+2;
print('SUM OF FIRST',a,'EVEN NUM IS: ',Sum,);
#Alternate way.
a=int(input('ENTER THE NUM OF FIRST EVEN NOS YOU WANT TO ADD:'));
i=1;
Sum=0;
count=0;
while count<a:
    if i%2==0:
        Sum=Sum+i;
        count=count+1;
    i=i+1;
print('THE SUM OF FIRST',a,'EVEN NUM IS: ',Sum,);



    
