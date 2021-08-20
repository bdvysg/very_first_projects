def generator(*args):
    if len(args) == 1:
        first_num = 0
        last_num = args[0]
        step = 1

    elif len(args) == 2:
        first_num = args[0] 
        last_num = args[1]
        step = 1
        
    elif len(args) == 3:
        first_num = args[0] 
        last_num = args[1]
        step = args[2]
    
    while first_num < last_num:
            yield first_num
            first_num += step
        


x = generator(10, 100, 5)
for i in x:
    print(next(x))


