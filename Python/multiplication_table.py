def mult_table(x):
    for row in range(1,x + 1):
        for col in range(1,x + 1):
            if col >8 and (row * col) < 100:
                print "", row * col,
            elif (row * col) < 10:
                print "", row * col,
            else:
                print row * col,
        print

mult_table(12)
