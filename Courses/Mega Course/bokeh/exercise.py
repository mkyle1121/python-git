import pandas
from bokeh.plotting import figure,output_file, show

df = pandas.read_excel('verlegenhuken.xlsx')

temp_list=[]
pres_list=[]
for temp,pres in zip(df['Temperature'],df['Pressure']):
    temp=temp/10
    pres=pres/10
    temp_list.append(temp)
    pres_list.append(pres)

#also df['Temperature']=df['Temperature']/10    #can be used instead of list

df['Temperature']=temp_list
df['Pressure']=pres_list

graph = figure()
graph.title.text='Temperature and Air Pressure'
graph.xaxis.axis_label='Temperature'
graph.yaxis.axis_label='Pressure'

graph.circle(df['Temperature'],df['Pressure'],size=1)

output_file('exercise.html')
show(graph)