from datetime import datetime
from pandas_datareader import data
from bokeh.plotting import figure, show, output_file

START = datetime.datetime(2019, 3, 1)
END = datetime.datetime(2019, 3, 10)
df = data.DataReader(name='AAPL', data_source='google', start=START, end=END)
p = figure(x_axis_type='datetime', width=1000, height=300)
p.title = "Candlestick Chart"
