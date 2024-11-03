#Break and Continue;
#break terminates the whole loop when encountered.
#continue terminates the loop when encountered at a particular situation and then continues it.

#Programme shippet for Break statement.
i=1;
while i<=5:
    if i==3:
        break;
    print(i);
    i=i+1;
#Programme shippet for Continue statement.
i=0;
while i<=5:
    i=i+1;
    if i==3:
        continue;
    else:
        print(i);

    
    
