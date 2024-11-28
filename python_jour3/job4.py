i = 0

while i < 101:
    if i % 5 == 0 and i % 3 == 0:  
        print("fizz buzz")
    elif i % 5 == 0:  
        print("fizz")
    elif i % 3 == 0:  
        print("buzz")
    else:  
        print(i)
    i += 1  
