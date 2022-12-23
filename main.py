import streamlit as st
import pandas as pd
from numpy import array

from normalize import *
from clasification import *
from sorting import *

st.set_page_config('Class Division', layout='wide')

st.title('CADIV - Class Division')

uploaded_file = st.file_uploader('Insert Excel File', accept_multiple_files=False)
checkbox = st.checkbox('My Excel has header')

col_type = {0: str, 1: str}
col1, col2 = st.columns(2, gap='large')

with col1:
    st.write('### Starting Class')
    year = st.number_input('Entry year', value=0)
    people_per_class = st.number_input('Person per class', value=0)
    process_button = st.button('Process', type='primary')

    if process_button and uploaded_file and year and people_per_class:
        st.write('#### Raw Data')
        if checkbox:
            df = pd.read_excel(uploaded_file, usecols='A, B', converters=col_type)
        else:
            df = pd.read_excel(uploaded_file, header=None, usecols='A, B', converters=col_type)
        
        st.write(df)

        df = normalize_df(df, year)
        faculty = getFaculty(df)
        people_faculty = getPersonFaculty(df, faculty)

        sortPerFaculty(people_faculty)

        assignClass(people_faculty, people_per_class)

        st.write('#### Result Class')
        for i, fp in enumerate(people_faculty):
            st.write(f'##### {faculty[i]}')
            st.write(DataFrame(fp, columns=['NIM', 'Name', 'Class']))

        with pd.ExcelWriter('student_class.xlsx') as writer:
            for i, fp in enumerate(people_faculty):
                new_df = DataFrame(fp, columns=['NIM', 'Nama', 'Class'])
                new_df.to_excel(writer, index=False, sheet_name=str(faculty[i]))

        with open('student_class.xlsx', 'rb') as excel:
            st.write('Class division ready to download!')
            st.download_button('Download', excel, 'Student Class.xlsx')

with col2:
    st.write('### Major Division')
    sort_first = st.checkbox('Sort my data first')
    major_count = st.number_input('Number of majors', value=0)

    divide_button = st.button('Divide', type='primary')

    if divide_button and uploaded_file:
        if checkbox:
            df = pd.read_excel(uploaded_file, usecols='A, B', converters=col_type)
        else:
            df = pd.read_excel(uploaded_file, header=None, usecols='A, B', converters=col_type)
        
        df = df.values.tolist()
        df = [df]
        
        if sort_first:
            sortPerFaculty(df)

        assignMajor(df[0], major_count - 1)

        st.write('#### Result Major')
        st.write(DataFrame(df[0], columns=['NIM', 'Name', 'Major']))

        new_df = DataFrame(df[0], columns=['NIM', 'Nama', 'Major'])
        new_df.to_excel('student_major.xlsx', index=False)

        with open('student_major.xlsx', 'rb') as excel:
            st.write('Class division ready to download!')
            st.download_button('Download', excel, 'Student Major.xlsx')