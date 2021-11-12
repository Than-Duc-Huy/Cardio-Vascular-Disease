# IMPORT LIBRARY
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import plotly.express as px




st.header("Cardiovascular disease risk diagnosis")

# LOAD CLEAN DATA
@st.cache  # To store data in cache
def loaddata():
	data = pd.read_csv('data.csv')
	return data


num_attribs = ['age', 'height', 'weight', 'ap_hi', 'ap_lo']

data = loaddata()

# Split into 4 columns
one, two, three, four = st.columns(4)
gender = one.radio("Gender",('Male','Female'))
gender = 1 if gender == 'Male'else 0

one.write(gender)

age = two.slider("Age",5,100,20,1)
height = three.slider("Height in cm",100,300,160,1)
weight = four.slider("Weight in kg",20.0,150.0,50.0,0.1)

# Split into 3 columns
one2, two2, three2 = st.columns(3)
smoke = one2.radio("Do you smoke?", ('Yes','No'))
smoke = 1 if smoke == 'Yes' else 0
one2.write(smoke)

alcohol = two2.radio("Do you drink frequently?", ('Yes','No'))
alcohol = 1 if alcohol == 'Yes' else 0
two2.write(alcohol)

active = three2.radio("Do you exercise frequently?", ('Yes','No'))
active = 1 if active == 'Yes' else 0
three2.write(active)

# Examinable Section
st.write("#### Examinable")
exam = st.radio("Do you have a recent health check?", ('Yes','No'), index = 1)
if  exam == 'Yes':
	one3, two3, three3 = st.columns(3)
	systolic = one3.slider("Systolic Blood Pressure",40,200,120,1)
	diastolic = one3.slider("Diastolic Blood Pressure",40,200,80,1)
	if systolic < diastolic:
		st.warning("Systolic blood pressure has to be higher than Diastolic blood pressure")


	glucose = two3.radio("Glucose Level", ("Normal","Above normal","Well above normal"))
	glucose = 1 if glucose == "Normal" else (2 if glucose == "Above normal" else 3)
	two3.write(glucose)

	cholesterol = three3.radio("Cholesterol Level", ("Normal","Above normal","Well above normal"))
	cholesterol = 1 if cholesterol == "Normal" else (2 if cholesterol == "Above normal" else 3)
	three3.write(cholesterol)
else:
	systolic = 0
	diastolic = 0
	glucose = 1
	cholesterol = 1


# Calculated Risk Section
st.subheader("Calculated Risks")
BMI = weight/(height/100)**2
if BMI < 18.5:
	obesity = "Underweight"
elif BMI < 25:
	obesity = "Healthy"
elif BMI < 30:
	obesity = "Overweight"
else:
	obesity = "Obese"
st.write("According to your BMI of ",round(BMI,1), ", you are ", obesity)
obesity = 0 if obesity == "Underweight" else (1 if obesity == "Healthy" else(2 if obesity =="Overweight" else 3))


# Plot BMI Graph
if "graph" not in st.session_state:
	if "ax" not in st.session_state:
		st.session_state.graph, st.session_state.ax = plt.subplots(1,figsize = (20,10))
		st.session_state.ax.scatter(x = "weight",y = "height", c = "grey", data = data, label = "")
		x_val = np.arange(0,300)
		bmi18 = st.session_state.ax.plot(x_val,np.sqrt(x_val/18.5)*100, c = "orange", label = "BMI = 18.5")
		bmi25 = st.session_state.ax.plot(x_val,np.sqrt(x_val/25)*100, c = "green", label = "BMI = 25")
		bmi30 = st.session_state.ax.plot(x_val,np.sqrt(x_val/30)*100, c = "blue", label = "BMI = 30")
		st.session_state.ax.set_xlim([0, data["weight"].max()])
		st.session_state.ax.set_ylim([0, data["height"].max()])
		st.session_state.graph.legend(prop = {'size': 20})


# Highlight Red dot
st.session_state.ax.scatter(x = weight, y = height, color = "red")
with st.spinner("Plotting BMI Graph ..."):
	st.pyplot(st.session_state.graph)
st.session_state.ax.scatter(x = weight, y = height, color = "gray")


# Construct the person's Variable
person = pd.DataFrame({"age": [age],"gender": [gender],"height": [height],"weight": [weight],"ap_hi": [systolic],"ap_lo": [diastolic],"cholesterol": [cholesterol],"gluc": [glucose],"smoke": [smoke],"alco": [alcohol],"active": [active]})



# Feature scaling
scaler = StandardScaler()
# Target feature
data_Y = data["cardio"]
# Model Score initialization
score = 0
# Model with Examinable data
if exam == 'Yes':
	person[num_attribs] = scaler.fit_transform(person[num_attribs])
	if 'model_exam' not in st.session_state:
		data_X = data.drop(columns = ["cardio"])
		data_X[num_attribs] = scaler.fit_transform(data_X[num_attribs])
		with st.spinner("Initialising Random Forest Classifier with Examinable data"):
			st.session_state.model_exam = RandomForestClassifier(max_depth = 9, n_estimators= 350, random_state = 42)
			st.session_state.model_exam.fit(data_X, data_Y)
			if 'model_exam_score' not in st.session_state:
				st.session_state.model_exam_score = round(st.session_state.model_exam.score(data_X,data_Y),4)

	forest = st.session_state.model_exam
	score = st.session_state.model_exam_score


# Model without Examinable data
else :
	exam_var = ["ap_hi","ap_lo","cholesterol","gluc"]
	person = person.drop(columns = exam_var)
	person[['age','height','weight']] = scaler.fit_transform(person[['age','height','weight']])
	if 'model' not in st.session_state:
		data = data.drop(columns = exam_var)
		data_X = data.drop(columns = ["cardio"])
		data_X[['age','height','weight']] = scaler.fit_transform(data_X[['age','height','weight']])
		with st.spinner("Initialising Random Forest Classifier without Examinable data"):
			st.session_state.model = RandomForestClassifier(max_depth = 9, n_estimators= 350, random_state = 42)
			st.session_state.model.fit(data_X, data_Y)
			if 'model_score' not in st.session_state:
				st.session_state.model_score = round(st.session_state.model.score(data_X,data_Y),4)

	forest = st.session_state.model
	score = st.session_state.model_score

with st.spinner("Calculating risk..."):
	cardio = forest.predict(person)

st.write("Using Random Forest, the with training accuracy ",score)
if cardio == 0:
	st.write("You are **NOT at risk** of having cardiovascular disease")
else:
	st.write("You are **AT RISK** of having cardiovascular disease")

if exam == "No":
	st.warning("Consider providing Examinable information for better prediction!")	
