from bokeh.io import curdoc
from bokeh.models import CustomJS, MultiSelect

# Define the options for MultiSelect
OPTIONS = [("1", "foo"), ("2", "bar"), ("3", "baz"), ("4", "quux")]

# Create the MultiSelect widget
multi_select = MultiSelect(value=["1", "2"], options=OPTIONS)

# Add a JavaScript callback
multi_select.js_on_change("value", CustomJS(code="""
    console.log('multi_select: value=' + this.value, this.toString())
"""))

# Add the MultiSelect widget to the Bokeh server document
curdoc().add_root(multi_select)
curdoc().title = "MultiSelect Example"
