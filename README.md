# NTU EEE EE0005 2021 Semester 1 Group 8 Mini Project
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
- data.csv: Final Clean Data for Application (exported from 3_Final_Clean.ipynb)


The Python Notebook files
- 1_Explore.ipynb : Clean, Explore, Clustering, BMI
- 2_Model.ipynb : Model exploration
- 3_Final_Clean.ipynb: Final Cleaning for Application

Python Streamlit Application
- Main.py : Main page 


# OUTLINE OF THE NOTEBOOKS

## 1_Explore
- Observer Raw data
	- ap_hi, ap_lo outlier 
	- convert to categorical blood pressure (bp)
- Comment on the overall distribution of all features
- Comment on the distribution between people with and without disease
	- Numerical
	- Categorical: Bayesian Probability
- Correlation
- Feature Engineering: BMI
	- Distribution
	- Obesity category
- Clustering (KMean)
	- On height and weight
	- On all numerical variables


## 2_Model
- Concepts & Experiment (Using Decision Tree)
	- Feature Scaling
	- Train-Test-split
	- Confusion Matrix & ROC curve
	- GridSearchCV & Validation

- Fine Tune Decision Tree
	- Finalized the data cleaning process (3_Final_Clean)
	- Final Data Distribution check
	- Use the above concepts with (3_Final_Clean) data

- Explore Models
	- Use the above concepts and metrics with (3_Final_Clean) data for
		- Random Forest Classifier
		- Gradient Boosting Classifier
		- AdaBoost Classifier



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


