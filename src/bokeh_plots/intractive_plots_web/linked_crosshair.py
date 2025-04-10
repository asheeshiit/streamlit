from random import random
from bokeh.layouts import row
from bokeh.models import CrosshairTool, Span
from bokeh.plotting import figure, curdoc

# Generate random data
x = [random() * 10 for _ in range(200)]
y = [random() * 10 for _ in range(200)]

# Create horizontal and vertical span lines
width_span = Span(location=0, dimension="width", line_dash="dashed", line_width=2)
height_span = Span(location=0, dimension="height", line_dash="dotted", line_width=2)

# Create the first plot
p1 = figure(height=400, width=1000, x_range=(0, 10), y_range=(0, 10),
            tools="hover", toolbar_location=None)
p1.add_layout(width_span)
p1.add_layout(height_span)
p1.add_tools(CrosshairTool())
p1.circle(x, y, radius=0.2, alpha=0.3, hover_alpha=1.0)

# Create the second plot
p2 = figure(height=400, width=1000, x_range=(0, 10), y_range=(0, 10),
            tools="hover", toolbar_location=None)
p2.add_layout(width_span)
p2.add_layout(height_span)
p2.add_tools(CrosshairTool())
p2.circle(x, y, radius=0.2, alpha=0.3, hover_alpha=1.0)

# Layout the plots side by side
layout = row(p1, p2)

# Add layout to the current document for deployment with Bokeh server
curdoc().add_root(layout)
curdoc().title = "Interactive Scatter Plots with Crosshairs"
