# import pandas DataFrame
from pandas import DataFrame

# normalize_df function to remove the student that not in the entry year
def normalize_df(df, entry_year):
    # prepare the new data as a empty list
    new_data = []
    
    # do iteration per index in dataframe
    for idx in df.index:
        # if the first two digits of the student ID (column 0) is the same as the entry year
        if df[df.columns[0]][idx][:2] == str(entry_year):
            # append the student's data into new_data
            new_data.append([df[df.columns[0]][idx], df[df.columns[1]][idx]])

    # return the new_data as a dataframe
    return DataFrame(new_data, columns=df.columns)
