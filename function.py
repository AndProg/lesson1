def get_summ(one, two, delimiter = '&'):
    one = str(one)
    two = str(two)
    print(one,delimiter,two,sep='')
    return one+delimiter+two

print(get_summ('Learn','Python').upper())

print(get_summ(543,'Python').upper())
