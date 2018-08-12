import pandas
import matplotlib.pyplot as plt

df1=pandas.read_csv('cereal.csv', sep=';')

#print(df1)

#print(df1['calories'])

#df1['calories']=df1.astype(int)

print('---------------------------')

#df1['calories']=df1['calories'].convert_objects(convert_numeric=True)
#print(df1['calories'].convert_objects(convert_numeric=True).dtypes)

print(df1['calories'].dtypes)

#df1['calories'].convert_objects(convert_numeric=True).dtypes

#print(df1['calories'])

print(df1['calories'].plot())
plt.show()