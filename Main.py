import streamlit as st
import pandas as pd
import numpy as np

st.header("EE0005 DSAI Group 8")
st.header("Mini app to analyze your Cardiovascular disease risk")

@st.cache
def loaddata():
	data = pd.read_csv('cardio_train.csv', sep = ';')
	return data

data = loaddata()


try: a = st.session_state['page']
except: st.session_state['page'] = 0

st.write("What do you want to know?")
left, mid, right = st.columns(3)
left_button = left.button("Personal Diagnosis")
mid_button = mid.button("Population Statistics")
right_button = right.button("Model Exploration")

if left_button:
	st.session_state['page'] = 1


if mid_button:
	st.session_state['page'] = 2

if right_button:
	st.session_state['page'] = 3


if st.session_state['page'] == 1:
	import Personal   # PErson page
	Personal.render(data)

if st.session_state['page'] == 2:
	import Population # Pop page
	Population.render(data)

if st.session_state['page'] == 3:
	import Model #Model page
	Model.render(data)


st.session_state['page']