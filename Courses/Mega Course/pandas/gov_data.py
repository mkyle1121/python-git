import pandas

df1 = pandas.read_csv('zip_code.csv')
print (df1)

print (len(df1.index))

print (df1.iloc[1:4,0:4])

print (df1.loc[9,'PERCENT FEMALE'])

print (df1['COUNT PARTICIPANTS'])

df1['mikes new column']=df1.shape[0]*['some new text here']

print (df1.iloc[:,:])

df1['mikes new column']=df1.shape[0]*['some new text']

df1=df1.T

print (df1)

#df1['mikes new column']=['HEADER 1','HEADER2']

print (df1)

df1=df1.T

print (df1)

df1=df1.drop('mikes new column',1)

print (df1)

print (df1.columns)
print (df1.index)
