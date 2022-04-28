# import stuff
import pandas as pd
import altair as alt
import numpy as np
# read csv data
rauch = pd.read_csv("DataVisRauchen.CSV", sep=";")
# make data frame
df = pd.DataFrame(rauch)
# check and display
df
# install vega dataset for chart
!pip install vega_datasets==0.9.0
# make chart
from vega_datasets import data
source = df
alt.Chart(source).mark_bar().encode(
    alt.X('Reason'),
    y='count()',
    color='Reason'
).properties(
  title = 'Reasons to Smoke',
  width=400,
  height=500
).configure_title(
    fontSize=20,
    font='Arial',
    anchor='start',
    color='red'
    )
# chart shows a lot of null dont know where this is coming from
# must be an error in csv conversion i guess
# dont know how to work with the date and time in this example somehow the
# spacing and filling of not included times is strange 
