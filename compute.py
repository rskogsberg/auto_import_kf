import pandas as pd
import numpy as np
import os

# path for .xls that is to be converted to .csv
path = 'S:/Departments/Analytics/Chemical Analytics/Richard/kf_import_csv'

os.chdir(path)

# constant variables for dataframe construction
method = '874 - Coulometer - water content'
temperature = 150
unit = 'mg'


def xls_to_csv(xls_file):
    xls_df = pd.read_excel(xls_file)
    xls_df = xls_df.drop(['Position', 'Sequence Sample Name','Weight (g)', 'Method Name', 'Type'], axis=1)

    csv_df = pd.DataFrame(columns=['Method', 'Position', 'Sample Label','Temperature'])

    df_length = len(xls_df['Sample Label'])

    csv_df['Method'] = [method for i in range(df_length)]
    csv_df['Position'] = [i+5 for i in range(df_length)]
    csv_df['Sample Label'] = xls_df['Sample Label']
    csv_df['Temperature'] = [temperature for i in range(df_length)]
    for i in range(1,7):
        title = 'Blank {}'.format(i)
        csv_df[title] = ['' for i in range(df_length)]
    csv_df['Multiplier'] = xls_df['Correction Factor/Multiplier']
    csv_df['Unit'] = [unit for i in range(df_length)]

    return csv_df.to_csv('{}.csv'.format(xls_file.split('.')[0]), encoding='utf-8', header=False, index=False)