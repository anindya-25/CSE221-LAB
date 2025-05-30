def bubbleSort(arr):                                                    
    for i in range(len(arr)-1):
        swap_flag = False
        for j in range(len(arr)-i-1): 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap_flag = True
        if swap_flag == False:
            break

N = int(input())
arr = list(map(int,input().split()))
bubbleSort(arr)
for i in range(len(arr)):
    if i == len(arr)-1:
        print(arr[i])
    else:
        print(arr[i], end=" ")
