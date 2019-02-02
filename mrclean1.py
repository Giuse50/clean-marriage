import pandas as pd #import pandas library

#read xlsx file and save the data structure as "marriage"
marriage= pd.read_excel('state-marriage-rates-90-95-99-17.xlsx',
                        skiprows=4,  #skip the first four rows to remove meta data
                        header=[0,1], #make the header first and second row
                        skipfooter=7, # skip last 7 rows of the excel file
                        na_values='NA',
                        index_col=[0])  #index column is first row and there are no multi-indexs

marriage = marriage.stack()             #pivot years and rate of marriage from columns to row
marriage = marriage.reset_index()          #reset index
marriage.rename(columns={marriage.columns[1] : 'year'}      # renaming column two of the index to "year"
              , inplace=True)
marriage.drop(columns=[])                                      # drop a column that was numbering the states

marriage.to_excel(excel_writer='marriage_clean.xlsx',           #write all of the above into a new excel file
                  sheet_name='Marriage rate',                   # naming the worksheet
                  index = False)




print(marriage)