import numpy as np
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, RangeTool
from bokeh.plotting import figure, curdoc
from bokeh.sampledata.stocks import AAPL

# Prepare data
dates = np.array(AAPL['date'], dtype=np.datetime64)
source = ColumnDataSource(data=dict(date=dates, close=AAPL['adj_close']))

# Create the main plot
p = figure(
    height=300, width=800, tools="xpan", toolbar_location=None,
    x_axis_type="datetime", x_axis_location="above",
    background_fill_color="#efefef", x_range=(dates[1500], dates[2500])
)

p.line('date', 'close', source=source)
p.yaxis.axis_label = 'Price'

# Create the selection range tool
select = figure(
    title="Drag the middle and edges of the selection box to change the range above",
    height=130, width=800, y_range=p.y_range,
    x_axis_type="datetime", y_axis_type=None,
    tools="", toolbar_location=None, background_fill_color="#efefef"
)

range_tool = RangeTool(x_range=p.x_range, start_gesture="pan")
range_tool.overlay.fill_color = "navy"
range_tool.overlay.fill_alpha = 0.2

select.line('date', 'close', source=source)
select.ygrid.grid_line_color = None
select.add_tools(range_tool)

# Combine the plots into a layout
layout = column(p, select)

# Add the layout to the current document
curdoc().add_root(layout)
curdoc().title = "Stock Price Range Selector"
