import glob
import pandas as pd
import os

#Select the columns of data you don't want to convert to category codes
columns_to_exlude = [0, 1, 37]

output_file_sufix = "_CATCODE"

# Get data file and exclude file with indixcated file sufix.
def get_file(file_extension, output_file_sufix_to_exlude):
    files = glob.glob('./*' + file_extension)
    number_of_files = len(files)

    if number_of_files != 0 and number_of_files < 3:
        for file in files:
            file_name_without_extension = os.path.splitext(file)[0]
            file_name_sufix = file_name_without_extension[-len(output_file_sufix_to_exlude):]
            if file_name_sufix !=  output_file_sufix_to_exlude:
                return file
    return " "

# Output data file as .csv with category codes data excluding the columns that wouldn't convert.
def df_to_cat_codes(input_data_file, output_file_sufix, columns_to_exlude):
    df = pd.read_csv(input_data_file) 
    df_categorical = df.drop(df.columns[columns_to_exlude],axis=1)

    data_conversion_list_to_print = []

    for column in df_categorical.columns:
        for column_to_exclude in columns_to_exlude:
            if(df_categorical[column].dtype == 'object'):

                # Dictionary Keys List
                df_categorical_unique_string = df_categorical[column].astype('string').unique()

                # Get columns categories and transform to codes
                df_categorical[column]= df_categorical[column].astype('category')
                df_categorical[column] = df_categorical[column].cat.codes

                # Dictionary Values List
                df_categorical_unique = df_categorical[column].unique()

                # Create Dictionary
                column_zip_iterator = zip(df_categorical_unique_string, df_categorical_unique)
                column_dictionary = dict(column_zip_iterator)
                column_dictionary = dict(sorted(column_dictionary.items(), key=lambda item: item[1]))
                data_conversion_list_to_print.append(column_dictionary)

                col_counter =+ 1
        
    # Export data conversion reference
    filename = "data_reference.txt"
    # Writing the list of dict objects to a file
    with open(filename, mode='w') as f:
        for data_element in data_conversion_list_to_print:
            f.write(str(data_element) + "\n")

    header_name = list(df)

    for column_to_exclude in columns_to_exlude:
        col = df.iloc[:, column_to_exclude]
        df_final = df_categorical.insert(column_to_exclude, header_name[column_to_exclude], col)
    
    df_categorical.to_csv(os.path.splitext(input_data_file)[0] + output_file_sufix + '.csv')

# Get data file name with extension
data_file = get_file(".csv", output_file_sufix)

# Export data frame with categorical values
if data_file != " ":
    df_to_cat_codes(data_file, output_file_sufix, columns_to_exlude)