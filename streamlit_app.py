import streamlit as st
import pandas as pd
import numpy as np
from numpy.random import default_rng as rng



st.title('Streamlit by Elaine')
st.write("""
# My First app
Hello *world!*
""")

# https://docs.streamlit.io/develop/api-reference/charts/st.line_chart

df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["a", "b", "c"])
st.line_chart(df)

# try my own data

df2 = pd.read_csv("my_data.csv",header=0, usecols=['time','distance'],index_col=False)
#df2
st.line_chart(df2,x="time",y="distance",x_label="Time (s)",y_label="Distance (m)",alt="Three series over a shared x-axis")
