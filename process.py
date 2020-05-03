# import modules to work with
# Pandas for reading csv file
# Os for the directory indexing
import pandas as pd
import os
from modify_name import get_name_neatly

# get the name and targeted columns
csv_folder = "./sheets"
get_col = ['Name', 'Shortlist Result']

# get all the files
list_sheets = os.listdir(csv_folder)

# Loop all the files and clean the data
for sheet in list_sheets:
    # get the file path
    sheet_path = os.path.join(csv_folder, sheet)

    # read the file
    dataframe = pd.read_csv(sheet_path)

    # clean the columns by getting on some columns
    cleaned_dataframe = dataframe.filter(get_col)

    # select all the people who pass
    pass_volunteer = cleaned_dataframe.where(cleaned_dataframe[get_col[1]] == 'Pass')

    # drop the nan value for the false value
    # and get the name
    cleaned_pass = pass_volunteer.dropna()[get_col[0]]

    print(get_name_neatly(cleaned_pass))
