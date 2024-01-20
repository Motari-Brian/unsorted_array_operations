#Python insert element into an unsorted array
#element will be k

def insert_element(arr, k):
    arr.append(k)
# Driver's code
if __name__ == '__main__':
    # declaring array and key to insert
    arr = [12, 16, 20, 40, 50, 70]
    k = 26
 
    # array before inserting an element
    print("Before Inserting: ")
    print(arr)
 
    # array after Inserting element
    insert_element(arr, k)
    print("After Inserting: ")
    print(arr)