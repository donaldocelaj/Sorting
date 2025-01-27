# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr - 1)):
        cur_index = i
        smallest_index = cur_index

        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        
        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp

    return arr



# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swaps_occurred = True

    while swaps_occurred:
        swaps_occurred = False

        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                swaps_occurred = True

    return arr    

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr