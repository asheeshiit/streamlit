from bokeh.plotting import figure, curdoc
from bokeh.models import Slider
from bokeh.layouts import column

# Create a simple plot
plot = figure(title="Interactive Bokeh Plot", x_axis_label="X", y_axis_label="Y")
x = list(range(10))
y = [i**2 for i in x]
line = plot.line(x, y, line_width=2)

# Add interactivity with a slider
slider = Slider(start=0, end=10, value=1, step=0.1, title="Scale")

# Callback to update the plot
def update(attr, old, new):
    scale = slider.value
    line.data_source.data['y'] = [i**2 * scale for i in x]

slider.on_change('value', update)

# Layout and add to document
layout = column(plot, slider)
curdoc().add_root(layout)
