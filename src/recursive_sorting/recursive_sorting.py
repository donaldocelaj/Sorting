# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    while len(arrA) > 0 and len(arrB) > 0:
        smallest = min(arrA[0], arrB[0])
        if smallest == arrA[0]:
            arrA.pop(0)
            merged_arr.append(smallest)
        else:
            arrB.pop(0)
            merged_arr.append(smallest)

    if len(arrA) > 0:
        for i in arrA:
            merged_arr.append(i)
    else:
        for i in arrB:
            merged_arr.append(i)

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    if len(arr) > 1:
        # divide
        left = merge_sort( arr[ 0: int(len(arr)/2) ] )
        right = merge_sort( arr[ int(len(arr)/2) :] )
        arr = merge(left, right)

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
