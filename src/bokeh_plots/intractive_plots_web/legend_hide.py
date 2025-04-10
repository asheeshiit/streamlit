import pandas as pd
from bokeh.palettes import Spectral4
from bokeh.plotting import figure, curdoc
from bokeh.sampledata.stocks import AAPL, GOOG, IBM, MSFT

# Create the figure
p = figure(width=800, height=250, x_axis_type="datetime")
p.title.text = 'Click on legend entries to hide the corresponding lines'

# Add lines for each stock
for data, name, color in zip([AAPL, IBM, MSFT, GOOG], ["AAPL", "IBM", "MSFT", "GOOG"], Spectral4):
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])
    p.line(df['date'], df['close'], line_width=2, color=color, alpha=0.8, legend_label=name)

# Configure legend
p.legend.location = "top_left"
p.legend.click_policy = "hide"

# Add the figure to the current document
curdoc().add_root(p)
curdoc().title = "Stock Prices"
