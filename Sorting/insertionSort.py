def insertion(arr):

    for i in arr:
        j = arr.index(i)

        while(j>0):
            if(arr[j-1]>arr[j]):
                arr[j-1],arr[j] = arr[j],arr[j-1]
            else:
                break
            j-=1
    print("The sorted arr is : ", arr)


arr=[]

size=int(input("Please enter the size of element : "))

for val in range(0,size):
    arr.append(int(input("Please enter the elements : ")))

print(arr)

insertion(arr)
