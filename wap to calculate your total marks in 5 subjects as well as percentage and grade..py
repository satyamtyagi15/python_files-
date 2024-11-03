# wap to calculate total marks of 5 subjects(full marks=100) as well as
# % of marks and division as per condition given.
# percentage>=80-grade A, percentage>=60-grade B,
# percentage>=40-grade C, percentage<40-grade D.
phys=int(input('enter marks in physics: '));
chem=int(input('enter marks in chemistry: '));
maths=int(input('enter marks in maths: '));
eng=int(input('enter marks in english: '));
comp=int(input('enter marks in computer science: '));
total=phys+chem+maths+eng+comp
print('TOTAL MARKS =',total,'out of 500');
percent=(total/500)*100;
print('percentage=',percent);
if percent>=80:
    print('congo you got A grade.');
elif percent>=60:
    print('you got B grade.');
elif percent>=40:
    print('you got C grade.');
else:
    print('you got D grade.');
print('THANKYOU')





        
