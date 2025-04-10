from bokeh.layouts import gridplot
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, curdoc
from bokeh.sampledata.penguins import data
from bokeh.transform import factor_cmap

# Define constants
SPECIES = sorted(data.species.unique())
TOOLS = "box_select,lasso_select,help"

# Create a data source
source = ColumnDataSource(data)

# Left plot
left = figure(width=300, height=400, title=None, tools=TOOLS,
              background_fill_color="#fafafa")
left.scatter("bill_length_mm", "body_mass_g", source=source,
             color=factor_cmap('species', 'Category10_3', SPECIES))

# Right plot
right = figure(width=300, height=400, title=None, tools=TOOLS,
               background_fill_color="#fafafa", y_axis_location="right")
right.scatter("bill_depth_mm", "body_mass_g", source=source,
              color=factor_cmap('species', 'Category10_3', SPECIES))

# Create a grid layout
layout = gridplot([[left, right]])

# Add layout to the current document
curdoc().add_root(layout)
curdoc().title = "Penguin Data Visualization"
