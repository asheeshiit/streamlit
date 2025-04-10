# To Run single script available in a folder
bokeh serve --show /home/asheeshm/workspace/streamlit/src/bokeh_plots/intractive_plots/slider.py
# Run all the script available in a folder
bokeh serve --show /home/asheeshm/workspace/streamlit/src/bokeh_plots/intractive_plots/*.py
# Run from custom IP/port
bokeh serve --port 8000 --allow-websocket-origin=localhost:8000 /home/asheeshm/workspace/streamlit/src/bokeh_plots/intractive_plots/*.py


bokeh serve --port 8000 --allow-websocket-origin=localhost:8000 /home/asheeshm/workspace/streamlit/src/bokeh_plots/test/dd/*.py

