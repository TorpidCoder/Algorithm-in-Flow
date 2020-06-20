def twoSum(arr,target):
    for i in range(0,len(arr)-1):
        for j in range(i+1,len(arr)):
            if(arr[i]+arr[j]== target):
                print(arr[i],arr[j])
                return True
    return "Not found"


# hash table example

def twoSumHash(arr,target):
    hash_table = dict()
    for i in range(0,len(arr)-1):
        if(arr[i] in hash_table):
            print(hash_table[arr[i]],arr[i])
            return True
        else:
            hash_table[target-arr[i]] = arr[i]

    return False


# indices part

def two_sum_indices(arr,target):
    ht = dict()
    for i in range(0,len(arr)):
        if(arr[i] in ht):
            return [ht[arr[i]],i]
        else:
             ht[target- arr[i]] = i

print(twoSumHash([1,2,3,4,5],9))

