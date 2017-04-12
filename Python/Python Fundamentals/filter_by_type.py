def filter_by(x):
    #Test to check the type of argument and its size
    if isinstance(x, int):
        if x >= 100:
            print "That's a big number!"
        elif x < 100:
            print "That's a small number!"
    elif isinstance(x, str):
        if len(x) >= 50:
            print "Long sentence"
        elif len(x) < 50:
            print "Short sentence"
    elif isinstance(x, list):
        if len(x) >= 10:
            print "Big list!"
        elif len(x) < 10:
            print "Short list."
