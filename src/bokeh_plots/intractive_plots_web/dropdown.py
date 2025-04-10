from bokeh.io import curdoc
from bokeh.models import CustomJS, Dropdown

# Define the dropdown menu
menu = [("Item 1", "item_1"), ("Item 2", "item_2"), None, ("Item 3", "item_3")]

# Create the Dropdown widget
dropdown = Dropdown(label="Dropdown button", button_type="warning", menu=menu)

# Add a JavaScript callback
dropdown.js_on_event("menu_item_click", CustomJS(code="console.log('dropdown: ' + this.item, this.toString())"))

# Add the Dropdown to the Bokeh server document
curdoc().add_root(dropdown)
curdoc().title = "Dropdown Example"
