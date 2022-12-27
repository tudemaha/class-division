# insertion sort algorithm to sort the student by their student ID (NIM)
def insertion_sort(data):
    # get the number of the data
    count = len(data)

    # do iteration per data from index 1 to the last data
    for i in range(1, count):
        # set the key as the current data
        key = data[i]
        # set the j as the index before the current data
        j = i - 1
        # do iteration while j is greater than or equal to 0 and the data in index j is greater than the key
        while j >= 0 and data[j] > key:
            # swap the data in index j + 1 with the data in index j
            data[j + 1] = data[j]
            # decrement j by 1
            j -= 1
        # set the data in index j + 1 as the new key
        data[j + 1] = key

# function to sort the student by their student ID (NIM) per faculty
def sortPerFaculty(people_faculty):
    # do iteration per faculty
    for pf in people_faculty:
        # call insertion_sort function to sort the student by their student ID (NIM)
        insertion_sort(pf)