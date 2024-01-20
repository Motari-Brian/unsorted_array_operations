#Search for an element in an unsorted array// This can be done in a linear search.
def find_element(arr, n, key):
    for i in range(n):
        if(arr[i] == key):
         return i
    
    #If key not found
    return -1

# Driver's code
if __name__ == '__main__':
    arr = [12, 34, 10, 6, 40]
    key = 40
    n = len(arr)
 
    # search operation
    index = find_element(arr, n, key)
    if index != -1:
        print("Element Found at position: " + str(index + 1))
    else:
        print("Element not found")