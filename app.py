import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_plotly
import palmerpenguins  # This package provides the Palmer Penguins dataset

# Use the built-in function to load the Palmer Penguins dataset
# Columns include:
# - species: chinstrap, adelie, and gentoo
# - island: island name: Dream, torgensen, or Biscoe - islands in the Palmer Archipelago
# - bill_length_mm: length of bill in mm
# - bill_depth_mm: depth of bill in mm
# - flipper_length_mm: flipper length in mm
# - body_mass_g: body mass in grams
# - sex: male or female

# it is then loaded into a pandas dataframe
penguins_df = palmerpenguins.load_penguins()


# Build the UI
ui.page_opts(title="gjrich's penguin review", fillable=True)
with ui.layout_columns():

    @render_plotly
    def plot1():
        return px.histogram(px.data.tips(), y="tip")

    @render_plotly
    def plot2():
        return px.histogram(px.data.tips(), y="total_bill")
