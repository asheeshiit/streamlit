import numpy as np
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, Slider
from bokeh.plotting import figure, curdoc

# Data preparation
x = np.linspace(0, 10, 500)
y = np.sin(x)

source = ColumnDataSource(data=dict(x=x, y=y))

# Plot configuration
plot = figure(y_range=(-10, 10), width=1000, height=400)
plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)

# Slider widgets
amp = Slider(start=0.1, end=10, value=1, step=.1, title="Amplitude")
freq = Slider(start=0.1, end=10, value=1, step=.1, title="Frequency")
phase = Slider(start=-6.4, end=6.4, value=0, step=.1, title="Phase")
offset = Slider(start=-9, end=9, value=0, step=.1, title="Offset")

# Callback function to update the data
def update(attr, old, new):
    A = amp.value
    k = freq.value
    phi = phase.value
    B = offset.value
    source.data = dict(x=x, y=B + A * np.sin(k * x + phi))

# Attach callbacks to sliders
amp.on_change('value', update)
freq.on_change('value', update)
phase.on_change('value', update)
offset.on_change('value', update)

# Layout the application
layout = row(plot, column(amp, freq, phase, offset))

# Add the layout to the current document for the Bokeh server
curdoc().add_root(layout)
curdoc().title = "Interactive Sine Wave"
