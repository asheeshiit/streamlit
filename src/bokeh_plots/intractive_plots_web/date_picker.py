from bokeh.io import curdoc
from bokeh.models import CustomJS, DatePicker

# Create the DatePicker widget
date_picker = DatePicker(
    title="Select date",
    value="2019-09-20",
    min_date="2019-08-01",
    max_date="2019-10-30",
)

# Add a JavaScript callback
date_picker.js_on_change("value", CustomJS(code="""
    console.log("date_picker: value=" + this.value, this.toString())
"""))

# Add the DatePicker to the Bokeh server document
curdoc().add_root(date_picker)
curdoc().title = "Date Picker Example"
