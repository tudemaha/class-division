def buble_sort(data):
    count = len(data)

    for i in range(1, count):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key

def sortPerFaculty(people_faculty):
    for pf in people_faculty:
        buble_sort(pf)