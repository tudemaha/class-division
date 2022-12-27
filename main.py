# import streamlit and pandas library
import streamlit as st
import pandas as pd

# import module
from normalize import *
from clasification import *
from sorting import *

# set the config for website, set 'Class Division' as website title and use the wide layout
st.set_page_config('Class Division', layout='wide')

# show the website title on the top of page
st.title('CADIV - Class Division')

# file uploader section to upload the excel file (not accept multiple file upload)
uploaded_file = st.file_uploader('Insert Excel File', accept_multiple_files=False)
# the checkbox to accept the user's choice about the excel file has a header or not
checkbox = st.checkbox('My Excel has header')

# prepare the columns data type for the DataFrame that hold the excel data
# first column contains student's ID (NIM) and the second one contains the student's name
col_type = {0: str, 1: str}
# prepare the layout for website (this website has 2 columns)
col1, col2 = st.columns(2, gap='large')

# prepare the first column
with col1:
    # write down the subtitle
    st.write('### Starting Class')
    # input entry year (angkatan) of the student
    year = st.number_input('Entry year', value=0)
    # input number of people per class
    people_per_class = st.number_input('Person per class', value=0)
    # process button to start the class division
    process_button = st.button('Process', type='primary')

    # if the process button clicked, excel file uploaded, entry year and number of people per class entered
    if process_button and uploaded_file and year and people_per_class:
        # show the 'Raw Data' fro excel
        st.write('#### Raw Data')
        # if checkbox checked
        if checkbox:
            # read the excel file and use the first row as header
            df = pd.read_excel(uploaded_file, usecols='A, B', converters=col_type)
        #else
        else:
            # read the excel file without use the first row as header
            df = pd.read_excel(uploaded_file, header=None, usecols='A, B', converters=col_type)
        
        # display the data have read from excel
        st.write(df)

        # normalize the data first
        # (because the member of PKKMB not just the new student, it needs to normalize first)
        df = normalize_df(df, year)
        # get the faculty (in FMIPA the first seven digits is the faculty code, so the faculty shown in code)
        faculty = getFaculty(df)
        # divide the student into their faculty
        people_faculty = getPersonFaculty(df, faculty)

        # sort the people by their student ID (NIM)
        sortPerFaculty(people_faculty)

        # assign the class for them
        assignClass(people_faculty, people_per_class)

        # display the 'Result Class'
        st.write('#### Result Class')
        # do iteration per faculty
        for i, fp in enumerate(people_faculty):
            # display the faculty code
            st.write(f'##### {faculty[i]}')
            # display the students per faculty with the class assigned
            st.write(DataFrame(fp, columns=['NIM', 'Name', 'Class']))

        # write an Excel file from the data of students per faculty with their class
        with pd.ExcelWriter('student_class.xlsx') as writer:
            # do iteration per faculty (for the sheet name)
            for i, fp in enumerate(people_faculty):
                # create a dataframe of the students in current faculty
                new_df = DataFrame(fp, columns=['NIM', 'Nama', 'Class'])
                # insert the dataframe as sheet of the Excel file
                new_df.to_excel(writer, index=False, sheet_name=str(faculty[i]))

        # open the Excel file created before in mode "read binary"
        with open('student_class.xlsx', 'rb') as excel:
            # display the message
            st.write('Class division ready to download!')
            # create a download button to download the Excel file
            st.download_button('Download', excel, 'Student Class.xlsx')

# prepare the second column
with col2:
    # display 'Major Division'
    st.write('### Major Division')
    # the checkbox to accept the user's choice to sort the list first or no
    sort_first = st.checkbox('Sort my data first')
    # number input for the number of major on a faculty
    major_count = st.number_input('Number of majors', value=0)

    # divide button to start the major division
    divide_button = st.button('Divide', type='primary')

    # if the button clicked and Excel file uploded
    if divide_button and uploaded_file:
        # if the ckeckbox (to check the excel file has header or not)
        if checkbox:
            # read the excel file and use the first row as header
            df = pd.read_excel(uploaded_file, usecols='A, B', converters=col_type)
        else:
            # read the excel file without use the first row as header
            df = pd.read_excel(uploaded_file, header=None, usecols='A, B', converters=col_type)
        
        # change the dataframe to list
        df = df.values.tolist()
        # place the data into an empty list to use the same sortPerFaculty function that used before
        df = [df]
        
        # if sort_first checkbox checked
        if sort_first:
            # sort the student by their student ID (NIM)
            sortPerFaculty(df)

        # assign the major to the students
        assignMajor(df[0], major_count - 1)

        # display the 'Result Major'
        st.write('#### Result Major')
        # display the students with their major
        st.write(DataFrame(df[0], columns=['NIM', 'Name', 'Major']))

        # write an Excel file from the data of students with their major
        new_df = DataFrame(df[0], columns=['NIM', 'Nama', 'Major'])
        # insert the dataframe as sheet of the Excel file
        new_df.to_excel('student_major.xlsx', index=False)

        # open the Excel file created before in mode "read binary"
        with open('student_major.xlsx', 'rb') as excel:
            # display the message
            st.write('Class division ready to download!')
            # create a download button to download the Excel file
            st.download_button('Download', excel, 'Student Major.xlsx')