def reverse_only_string(list):

    if(len(list)<=1):

        return list


    return reverse_only_string(list[1:]) + list[0]

print(reverse_only_string('abc'))




def rev_1(lst):

    if not lst:
        return lst
    else:
        return lst[-1:] + rev_1(lst[:-1])
