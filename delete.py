#Python delete unsorted listdone by linear search.
if __name__ == '__main__':

#Declaring array and key to dlete
    arr = [20,30,30,50,60]
    key = 50

    print("Array before delete")
    print(arr)

    print("Array after deleting")
    arr.remove(key)
    print(arr)