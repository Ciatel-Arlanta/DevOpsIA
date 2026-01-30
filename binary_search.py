arr = [5,6,1,10,27,32,11,4,65,34]

def binary_search(arr, target):
    #accepts a sorted array and searches for the target

    low = 0
    mid = len(arr)//2
    high = len(arr) - 1

    while(True):
        if arr[mid] == target:
            print(f"Found at {mid}")
            return
        elif arr[mid] > target:
            high = mid - 1
        
        elif arr[mid] < target:
            low = mid + 1
        
        else:
            print("Not Found Target")
            return
        

binary_search(sorted(arr), 32)