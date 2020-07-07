import pandas as pd

#Create Data Frame one
r1 = pd.read_excel(r'filePath',sheet_name = 'Sheet1')

df = pd.DataFrame(r1,columns=['columnName'])

print(df)

#Create Data Frame Two
r2 = pd.read_excel(r'filePath',sheet_name = 'Sheet2')

df1 = pd.DataFrame(r2,columns=['columnName'])

print(df1)

#Concatinate both Data Frames
df2 = pd.concat([df,df1])
#Reset the index
df2 = df2.reset_index(drop=True)
print(df2)
#Group by columns
df_gpby = df2.groupby(list(df2.columns))
#Get the index of unique item
idx = [x[0] for x in df_gpby.groups.values() if len(x) == 1]
#Write Data to excel file
df2.reindex(idx).to_excel('filePath')