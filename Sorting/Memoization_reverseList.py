def rev_1(lst):

    if not lst:
        return lst
    else:
        return lst[-1:] + rev_1(lst[:-1])

print(rev_1(['s','a','h']))
