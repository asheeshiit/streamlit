import pandas as pd
from bokeh.palettes import Spectral4
from bokeh.plotting import figure, curdoc
from bokeh.sampledata.stocks import AAPL, GOOG, IBM, MSFT

# Create the figure
p = figure(width=800, height=250, x_axis_type="datetime")
p.title.text = 'Click on legend entries to mute the corresponding lines'

# Add stock lines to the plot
for data, name, color in zip([AAPL, IBM, MSFT, GOOG], ["AAPL", "IBM", "MSFT", "GOOG"], Spectral4):
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])
    p.line(
        df['date'], df['close'], line_width=2, color=color, alpha=0.8,
        muted_color=color, muted_alpha=0.2, legend_label=name
    )

# Configure legend
p.legend.location = "top_left"
p.legend.click_policy = "mute"

# Add the plot to the Bokeh server document
curdoc().add_root(p)
curdoc().title = "Stock Price Viewer"
