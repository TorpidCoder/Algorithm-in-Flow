import sys,time

def binarySearch(arr,low,high,num):

    if(high>=low):

        mid = int(low+(high-low)/2)

        if(arr[mid] == num):
            return mid;

        elif(arr[mid]>num):
            return binarySearch(arr,low,mid-1,num)

        else:
            return binarySearch(arr,mid-1,high,num)

    else:
        return -1

print()
print("What is the size of your array ? ")
arr = []
limit = int(input())

for vals in range(0,limit):
    arr.append(int(input("Enter the numbers : ")))

print(arr)


print("Now,you have done with your array , Please enter the number you want to search")
num = int(input())

new_arr = sorted(arr)
print(new_arr)

if(arr != new_arr):
    print("The array presented by you is not sorted ")
    sys.exit("good bye")
else:
    print("The array is sorted , Proceeding.......")
    # sys.setrecursionlimit(1500)
    #time.sleep(5)
    result = binarySearch(arr,0,len(arr)-1,num)

    if(result != -1 ):
        print("The number is present")
    else:
        print("The Number is not present")
