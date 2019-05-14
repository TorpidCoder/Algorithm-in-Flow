def linearSearch(arr,num):

    for values in range(len(arr)):
        if(num == arr[values]):
            return values

    return -1

arr = [1,2,3,4,5]
num=9

result = linearSearch(arr,num)

if(result != -1 ):
    print("Number is present")
else:
    print("Number is not present")
