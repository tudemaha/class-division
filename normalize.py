from pandas import DataFrame

def normalize_df(df, entry_year):
    new_data = []
    
    for idx in df.index:
        if df[df.columns[0]][idx][:2] == str(entry_year):
            new_data.append([df[df.columns[0]][idx], df[df.columns[1]][idx]])

    return DataFrame(new_data, columns=df.columns)
