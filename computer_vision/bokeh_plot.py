import datetime as dt
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.models import HoverTool, ColumnDataSource
from video_capture import df

df['Start_str'] = df['Start'].dt.strftime("%y-%m-%d %H:%M:%S")
df['End_str'] = df['End'].dt.strftime("%y-%m-%d %H:%M:%S")

cds = ColumnDataSource(df)

p = figure(x_axis_type="datetime", height=100, width=500, title="Motion Graph")
p.sizing_mode = 'scale_width'
p.yaxis.minor_tick_line_color = None
p.ygrid[0].ticker.desired_num_ticks = 1

hover = HoverTool(tooltips=[("Start: ", "@Start_str"), ("End: ", "@End_str")])
p.add_tools(hover)

q = p.quad(left='Start', right='End', bottom=0,
           top=1, color="Green", source=cds)

output_file('Graph.html')
show(p)
