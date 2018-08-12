from pandas_datareader import data
import datetime
from bokeh.plotting import figure, show, output_file

start = datetime.datetime(2017,1,1)
end = datetime.datetime(2017,1,31)
list_of_tickers = ['GOOG','MSFT','FB','AAPL','WMT']
df1 = data.DataReader(name='GOOG', data_source='google', start=start,end=end)
df2 = data.DataReader(name='MSFT', data_source='google', start=start,end=end)
df3 = data.DataReader(name='FB', data_source='google', start=start,end=end)
df4 = data.DataReader(name='AAPL', data_source='google', start=start,end=end)

#print(df1,df2,df3,df4)

p = figure(x_axis_type='datetime', width=1000, height=800, title='Stock Market Data')
p.line(df1.index,df1.Close,color='green')
p.line(df2.index,df2.Close,color='yellow')
p.line(df3.index,df3.Close,color='blue')
p.line(df4.index,df4.Close,color='red')



output_file('my_finance_graph.html')
show(p)
