from datetime import date
from random import randint

from bokeh.io import curdoc
from bokeh.models import ColumnDataSource, DataTable, DateFormatter, TableColumn

# Define the data source
data = dict(
    dates=[date(2014, 3, i + 1) for i in range(10)],
    downloads=[randint(0, 100) for i in range(10)],
)
source = ColumnDataSource(data)

# Define table columns
columns = [
    TableColumn(field="dates", title="Date", formatter=DateFormatter()),
    TableColumn(field="downloads", title="Downloads"),
]

# Create the DataTable
data_table = DataTable(source=source, columns=columns, width=400, height=280)

# Add the DataTable to the Bokeh server document
curdoc().add_root(data_table)
curdoc().title = "Data Table Example"
