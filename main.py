import streamlit as st
import pandas as pd

from normalize import *
from clasification import *
from sorting import *

st.set_page_config('Class Division', layout='wide')

st.title('CADIV - Class Division')

col_type = {0: str, 1: str}
col1, col2 = st.columns(2, gap='large')

with col1:
    uploaded_file = st.file_uploader('Insert Excel File', accept_multiple_files=False)
    checkbox = st.checkbox('My Excel has header')

    year = st.number_input('Entry year', value=0)
    people_per_class = st.number_input('Person per class', value=0)
    process_button = st.button('Process', type='primary')

with col2:
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
            with col1:
                st.download_button('Download', excel, 'Student Class.xlsx')