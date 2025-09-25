# both are > O(n)

# def longest_consequtive_sequence(array):
#     # check with a set for O(1) lookups
#     max_count = 1
#     check_set = set(array)
#     # less than O(n^2) 
#     for i in check_set:
#         temp = i
#         count = 1
#         while temp+1 in check_set:
#             temp +=1
#             count +=1
#             max_count = count if count>max_count else max_count
#     return max_count

def longest_consequtive_sequence_with_sort(arr):
    # sort using insertion sort
    for i in range(len(arr)-1):
        min = i
        for j in range(i+1,len(arr)):
            if arr[min] > arr[j]:
                min = j
        if min != i:
            arr[min],arr[i] = arr[i],arr[min]
    max_count = 1
    count = 1
    
    # O(n) to find longest sequence
    for i in range(len(arr)-1):
        if arr[i+1] == arr[i]:
            continue
        if arr[i+1] == arr[i] + 1:
            count+=1
            max_count = count if count>max_count else max_count
        else:
            count = 1
    return max_count
        
        


input_array = list(map(int,input("Enter list of elements with space ").strip().split()))
# result = longest_consequtive_sequence(input_array)
# print("for input - ",input_array," = ",result)
result = longest_consequtive_sequence_with_sort(input_array)
print("for input - ",input_array," = ",result)