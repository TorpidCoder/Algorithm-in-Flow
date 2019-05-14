def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]

arr = [34,76,7,12,45,3]
bubbleSort(arr)

for values in arr:
    print(values , end=' ')
