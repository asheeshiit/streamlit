from bokeh.io import curdoc
from bokeh.models import CustomJS, MultiChoice

# Define the options for MultiChoice
OPTIONS = ["foo", "bar", "baz", "quux"]

# Create the MultiChoice widget
multi_choice = MultiChoice(value=["foo", "baz"], options=OPTIONS)

# Add a JavaScript callback
multi_choice.js_on_change("value", CustomJS(code="""
    console.log('multi_choice: value=' + this.value, this.toString())
"""))

# Add the MultiChoice widget to the Bokeh server document
curdoc().add_root(multi_choice)
curdoc().title = "MultiChoice Example"
