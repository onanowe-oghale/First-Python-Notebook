def we_add(x , y):
    print(f"This is the result of adding {y} to {x}")
    return x + y

def we_sub(x , y):
    print(f"this is the result of subtracting {y} frorm {x}")
    return x - y 

def we_div(x, y):
    print(f"This is the result gotten from dividing {x} by {y}")
    return x / y

def we_X(x , y):
    print(f"this would multiply {x} by {y}")
    return x * y

added = we_add(45 , 31)
sbbed = we_sub(39 , 12)
dvved = we_div(45, 9)
xed  = we_X(221 , 7) 

print(f"so when we added we got {added} when we subtracted the given argument we got {sbbed} when we divided the given arguments we got {dvved} and we lastly multiplied the arguments we had on our hands which gave us {xed}")
fer = we_sub(sbbed, we_X(xed, we_div((added-2),dvved)))

print(f"The result from {fer} should be satisfactory")


s_added = we_add(8 , 8)
s_sbbed = we_sub(102 , 7)
s_dvved = we_div(28 , 2)
s_xed = we_X (2 , 4)

sec_oper = we_add(s_added, we_add(we_X(s_sbbed,s_dvved),(we_sub(s_xed, we_sub(290 ,29)))))

print(f"With the help of our return function we are able to calculate {s_added} + {sbbed} X {s_dvved} + {s_xed} - 290 - 29")
print(f"The answer we get is {sec_oper}")

