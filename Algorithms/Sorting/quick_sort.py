import math
def quick_sort(arr):
    pivot = math.floor((len(arr) + 1) / 2)
    #left side of pivot will contain items less than pivot and right greater
    print("pivot element", arr[pivot])
    arr[pivot], arr[len(arr) - 1] = arr[len(arr) - 1],arr[pivot]
    p1 = 0
    p2 = len(arr) - 2
    while p1 < p2:
        if arr[p1] > arr[pivot]:


        elif arr[p1] < arr[pivot]:
            p2 -= 1
    print(arr)


print(quick_sort([2,6,5,3,8,7,1,0]))
