class_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def getFaculty(df):
    faculty = []
    
    for idx in df.index:
        if df[df.columns[0]][idx][:7] not in faculty:
            faculty.append(df[df.columns[0]][idx][:7])

    return faculty

def getPersonFaculty(df, faculty):
    people_faculty = []

    for _ in faculty:
        people_faculty.append([])

    for i, fac in enumerate(faculty):
        for idx in df.index:
            if fac == df[df.columns[0]][idx][:7]:
                people_faculty[i].append([df[df.columns[0]][idx], df[df.columns[1]][idx]])

    return people_faculty

def assignClass(people_faculty, max_people):
    for pf in people_faculty:
        class_count = len(pf) / max_people
        if class_count > len(pf) // max_people:
            class_count += 1

        current_class = 0
        for people in pf:
            people.append(class_list[current_class])
            
            if current_class < class_count:
                current_class += 1
            else:
                current_class = 0

def assignMajor(people, major_count):

    current_major = 0
    for p in people:
        p.append(class_list[current_major])

        if current_major < major_count:
            current_major += 1
        else:
            current_major = 0