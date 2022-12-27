# prepare the list of classes
class_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# function to get the faculty list of the students
def getFaculty(df):
    # prepare the faculty list as a empty list
    faculty = []
    
    # do iteration per index in dataframe that store the students data
    for idx in df.index:
        # if the first seven digits of the student ID (column 0) is not in the faculty list
        if df[df.columns[0]][idx][:7] not in faculty:
            # append the first seven digits of the student ID (column 0) into faculty list
            faculty.append(df[df.columns[0]][idx][:7])

    # return the faculty list
    return faculty

# function to get the students data per faculty
def getPersonFaculty(df, faculty):
    # prepare the students data per faculty as a empty list
    people_faculty = []

    # do iteration per faculty
    for _ in faculty:
        # append an empty list into people_faculty to store the students data per faculty
        people_faculty.append([])

    # do iteration per faculty
    for i, fac in enumerate(faculty):
        # do iteration per index in dataframe that store the students data
        for idx in df.index:
            # if the first seven digits of the student ID (column 0) is the same as the faculty code
            if fac == df[df.columns[0]][idx][:7]:
                # append the current student's data into people_faculty list
                people_faculty[i].append([df[df.columns[0]][idx], df[df.columns[1]][idx]])

    # return the students data per faculty
    return people_faculty

# function to assign the class to the students
def assignClass(people_faculty, max_people):
    # do iteration of list of student's data per faculty
    for pf in people_faculty:
        # calculate the number of class
        class_count = len(pf) / max_people
        # if class_count in float is greater than the number of class in integer
        if class_count > len(pf) // max_people:
            # increment the number of class by 1 (ceil)
            class_count += 1

        # set the current class as 0
        current_class = 0
        # do iteration per student's data in list of student's data per faculty
        for people in pf:
            # append the class to the student's data
            people.append(class_list[current_class])
            
            # if the current class is less than the number of class
            if current_class < class_count:
                # increment the current class by 1
                current_class += 1
            # else
            else:
                # set the current class back to 0
                current_class = 0

# function to assign the major to the students
def assignMajor(people, major_count):

    # set the current major as 0
    current_major = 0
    # do iteration per student's data in list of student's data
    for p in people:
        # append the major to the student's data
        p.append(class_list[current_major])

        # if the current major is less than the number of major
        if current_major < major_count:
            # increment the current major by 1
            current_major += 1
        # else
        else:
            # set the current major back to 0
            current_major = 0