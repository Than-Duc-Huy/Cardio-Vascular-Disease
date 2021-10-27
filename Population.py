import streamlit as st

def render(data):
	st.header("Population Statistics")
	st.write("Explore the population Cardiovascular health statistics")
	st.write(data.describe())