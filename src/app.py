import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from model import multiplier

df = pd.read_csv("tests/data/example_data.csv")
model = multiplier(df, times=5)

fig, ax = plt.subplots(1, 1)
ax.scatter(model.time, model.value)

st.pyplot(fig)
