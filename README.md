# NTU EEE EE0005 2021 Semester 1 EE 06 Group 8 Mini Project
Github Link: https://github.com/Than-Duc-Huy/Cardiovascular-Disease

This is the work of EE005 Group 8 Mini Project
Team members:
- Than Duc Huy
- Nguyen Hoang Minh
- Low Thien Shawn
- Ling Zijie
- Tan Xin Lin


# FILES
The data files
- Description.txt : Data description
- cardio_train.csv : Downloaded from Kaggle (https://www.kaggle.com/sulianova/cardiovascular-disease-dataset), `;` separated
- databp.csv: to transfer data from 1_Explore.ipynb to 2_Model.ipynb
- data.csv: Final Clean Data for Application (exported from 3_Final_Clean.ipynb)


The Python Notebook files
- 1_Explore.ipynb : Clean, Explore, Clustering, BMI
- 2_Model.ipynb : Model exploration
- 3_Final_Clean.ipynb: Final Cleaning for Application

Python Streamlit Application
- Main.py : Main page 
- requirements.txt: libraries requirements for Application to run

Presentation
- EE0005 Group 8.pptx


# OUTLINE OF THE NOTEBOOKS

## 1_Explore
1. Import Libraries
2. Raw Data
3. Data Processing
	- 3.1 First Glance
	- 3.2 Blood Pressure
		- 3.2.1 Filter ap_hi, ap_lo
		- 3.2.2 Categorize Blood Pressure
	- 3.3 Distribution
		- 3.3.1 Numerical features
		- 3.3.2 Categorical features
4. Correlation Exploration
	- 4.1 Numerical features
	- 4.2 Categorical features
		- 4.2.1 Overview
		- 4.2.2 Individual
	- 4.3 Correlations
	- 4.4 Export databp.csv for 2_Model.ipynb
5. Clustering
	- 5.1 Body Mass Index (BMI)
	- 5.2 K-means Clustering
		- 5.2.1 K-means on Height and Weight
		- 5.2.2 K-means on Numerical Features



## 2_Model
- Use databp.csv exported by 1_Explore.ipynb
6. Concepts and Experimentation
	- 6.1 Feature Scaling
	- 6.2 Train Test Split
	- 6.3 Metrics: Accuracy, Precision, Recall, F1, ROC, AUC
	- 6.4 Grid Search
	- 6.5 Cross Validation

7. Fine-tune Model
	- 7.1 Reprocess the Data (Same as 3_Final_Clean.ipynb)
	- 7.2 Distribution, Correlation Check
	- 7.3 Prepare
	- 7.4 Train Model
		- 7.4.1 Train and Evaluate on Train set
		- 7.4.2 Evaluate on Test set

8. More Classification Models
	- 8.1. Random Forest Classifier
		- 8.1.1 Train and Evaluate on Training Set
		- 8.1.2 Evaluate on Test Set
	- 8.2. Gradient Boosting Classifier
		- 8.2.1 Train and Evaluate on Training Set
		- 8.2.2 Evaluate on Test Set
	- 8.3. AdaBoosting Classifier
		- 8.3.1 Train and Evaluate on Training Set
		- 8.3.2 Evaluate on Test Set
9. Final Decision
	- 9.1 Model Decision
	- 9.2 Conclusion

## 3_Final_Clean
- Clean the raw data for Application
- Relevant Changes
	- Drop Index
	- Convert Age to years
	- Calculate BMI (but does not use BMI because they are heavily related to height, weight)
	- Filter humanly possible range:
		- ap_hi [40,200]
		- ap_lo [40,140]
		- BMI [10,80]



# APPLICATION

## Cloud
Streamlit Application Link: https://share.streamlit.io/than-duc-huy/cardiovascular-disease/main/Main.py


## Local
To run the streamlit library, install streamlit library
`pip install streamlit`

In the command prompt (Windows) or Bash (Linux), run the command
`streamlit run Main.py`


