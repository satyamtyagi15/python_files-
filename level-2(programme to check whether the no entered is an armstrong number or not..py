# level-2 Questions.
# Programme to check whether a given Number is Armstrong or Not.
a=i=int(input('Enter the num to check whether it is an Armstrong Number or not: '));
Sum=0;
count=0;
while i>0:
    i=i//10;
    count=count+1;
i=a;
while i>0:
        digit=i%10;
        x=1;


        product=1;
        while x<=count:
            product=product*digit;
            x=x+1;
        Sum=Sum+product;
        i=i//10;
if Sum==a:
    print('Your no is an Armstrong Number');
else:
    print('Your no is not an Armstrong Number');        
