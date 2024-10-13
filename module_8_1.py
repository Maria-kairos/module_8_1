def add_everything_up(a, b):
    try:
        c = a + b
        print(c)
    except TypeError:
        if type(a) == int or type(a) == float:
            a = str(a)
        else:
            b = str(b)
        c = a + b
        print(c)


add_everything_up(68698, 'hool')
add_everything_up('fool', 'hool')
add_everything_up('coth', 54.6)
