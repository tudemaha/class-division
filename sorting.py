def buble_sort(data):
    count = len(data)

    for i in range(count):
        for j in range(0, count - i - 1):
            if data[j][0] > data[j + 1][0]:
                data[j], data[j + 1] = data[j + 1], data[j]

def sortPerFaculty(people_faculty):
    for pf in people_faculty:
        buble_sort(pf)