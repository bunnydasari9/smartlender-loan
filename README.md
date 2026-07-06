[Smart-Lender
Repository navigation
Code
Issues
Pull requests
🏦 Smart Lender – Loan Eligibility Prediction Using Machine Learning

 0 stars
 0 forks
 0 watching
 1 Branch
 0 Tags
 Activity
Public repository
bunnydasari9/smartlender-loan
Name	
bunnydasari9
bunnydasari9
yesterday
README.md
yesterday
Repository files navigation
README
Smart-Lender
🏦 Smart Lender – Loan Eligibility Prediction System
An intelligent Machine Learning-based web application that predicts loan eligibility using applicant information and assists financial institutions in making faster, more accurate, and data-driven lending decisions.

📌 Project Overview
Smart Lender is a Machine Learning-based web application developed to predict the eligibility of loan applicants. The system automates the loan approval process by analyzing applicant information and predicting whether a loan should be Approved or Rejected.

The application compares multiple classification algorithms and integrates the best-performing model (XGBoost) into a Flask web application for real-time loan prediction.

🎯 Problem Statement
Traditional loan approval processes require extensive manual verification, making them time-consuming and prone to inconsistencies.

Smart Lender addresses this challenge by automating credit risk assessment using Machine Learning, enabling banks and financial institutions to:

Reduce manual effort
Improve decision accuracy
Minimize lending risks
Speed up loan approvals
🚀 Key Features
Feature	Description
✅ Loan Eligibility Prediction	Predicts loan approval or rejection instantly
✅ Data Preprocessing	Cleans and prepares applicant data
✅ Feature Engineering	Improves model performance
✅ Exploratory Data Analysis	Understands data patterns and relationships
✅ Multiple ML Models	Compares various classification algorithms
✅ Best Model Selection	Automatically selects the highest-performing model
✅ Flask Web Application	Real-time prediction through an interactive web interface
✅ Loan Rejection Suggestions	Provides recommendations when a loan is rejected
✅ IBM Cloud Ready	Easily deployable on IBM Cloud
🏗️ System Architecture
                    +----------------------+
                    |      User Layer      |
                    |----------------------|
                    | Loan Applicants      |
                    | Credit Officers      |
                    | Financial Analysts   |
                    +----------+-----------+
                               |
                               ▼
                    +----------------------+
                    |   Frontend Layer     |
                    |----------------------|
                    | HTML Templates       |
                    | CSS                  |
                    | Responsive Forms     |
                    +----------+-----------+
                               |
                               ▼
                    +----------------------+
                    | Flask Application    |
                    |----------------------|
                    | Request Handling     |
                    | Input Validation     |
                    | Prediction Engine    |
                    | Result Rendering     |
                    +----------+-----------+
                               |
                               ▼
                    +----------------------+
                    | Machine Learning     |
                    |----------------------|
                    | Data Preprocessing   |
                    | Feature Engineering  |
                    | Model Training       |
                    | Model Evaluation     |
                    | XGBoost Prediction   |
                    +----------+-----------+
                               |
                               ▼
                    +----------------------+
                    | Deployment Layer     |
                    |----------------------|
                    | IBM Cloud            |
                    | Web Browser Access   |
                    +----------------------+
📊 Dataset Information
Feature	Description
Gender	Applicant Gender
Married	Marital Status
Dependents	Number of Dependents
Education	Education Level
Self Employed	Employment Status
Applicant Income	Monthly Income
Coapplicant Income	Co-applicant Income
Loan Amount	Requested Loan Amount
Loan Amount Term	Loan Repayment Period
Credit History	Previous Credit Record
Property Area	Urban / Rural / Semi-Urban
🔍 Data Preprocessing
The following preprocessing techniques were applied before model training:

Missing Value Handling
Mean Imputation
Mode Imputation
Label Encoding
Feature Transformation
Data Cleaning
Data Validation
🤖 Machine Learning Models
The following classification algorithms were trained and evaluated.

Model	Status
Decision Tree Classifier	✅ Trained
Random Forest Classifier	✅ Trained
K-Nearest Neighbors (KNN)	✅ Trained
XGBoost Classifier	⭐ Best Model
📈 Model Performance
Metric	Value
Best Algorithm	XGBoost Classifier
Training Accuracy	94.7%
Testing Accuracy	81.1%
Prediction Type	Binary Classification
The trained XGBoost model was selected for deployment due to its superior performance.

⚙️ Technology Stack
Programming Language
Python
Libraries
Library	Purpose
NumPy	Numerical Computing
Pandas	Data Manipulation
Matplotlib	Data Visualization
Seaborn	Statistical Visualization
Scikit-learn	Machine Learning
XGBoost	Classification Model
Web Framework
Flask
Frontend
HTML5
CSS3
JavaScript
Deployment
Browser based(local host)
📂 Project Structure
Smart-Lender/
│
├── data/
├── models/
├── static/
│   ├── css/
│   ├── images/
│   └── js/
│
├── templates/
│   ├── index.html
│   ├── landing.html
│   └── result.html
│
├── app.py
├── trained_model.pkl
├── requirements.txt
├── README.md
└── .gitignore
🔄 Application Workflow
User enters applicant information.
Flask validates the input.
Data is preprocessed.
Features are transformed.
XGBoost model predicts eligibility.
Loan status is displayed.
Suggestions are provided if the application is rejected.
💼 Business Use Cases
Use Case	Description
Fast Loan Approval	Quickly approve low-risk applicants
Credit Risk Analysis	Identify risky loan applications
Bulk Screening	Process thousands of applications efficiently
Decision Support	Assist loan officers with AI-driven insights
🎓 Learning Outcomes
Through this project, the following skills were developed:

Machine Learning Model Development
Data Cleaning & Preprocessing
Feature Engineering
Exploratory Data Analysis (EDA)
Classification Algorithms
Model Evaluation
Flask Web Development
Machine Learning Deployment
End-to-End AI Application Development
🚀 Installation
Clone the Repository
git clone https://github.com/varshith-git17/Smart-Lender
Navigate to the Project
cd Smart-Lender
Install Dependencies
pip install -r requirements.txt
Run the Application
python app.py
🌐 Usage
Open the application in your browser.
Enter the applicant's details.
Click Predict.
View the loan approval or rejection result.
If rejected, review the suggested improvements.
🔮 Future Enhancements
User Authentication
Loan EMI Calculator
Credit Score Integration
Explainable AI (SHAP/LIME)
Dashboard Analytics
Cloud Database Integration
REST API Support
Docker Deployment
👨‍💻 Author
D.BUUNY
🎓 B.Tech – Computer Science & Engineering (AI & ML)

🏫 Anantha Lakshmi Institute of Technology and Sciences

📫 Connect with Me
Platform	Profile
🐙 GitHub	https:https://github.com/bunnydasari9/smartlender-loan
💼 LinkedIn	http:https://www.linkedin.com/in/bunny-dasari-4209752b6?utm_source=share_via&utm_content=profile&utm_medium=member_android
⭐ Acknowledgements
This project was developed as part of the Artificial Intelligence & Machine Learning curriculum to demonstrate the practical application of Machine Learning and Flask in solving real-world loan eligibility prediction problems.

Special Thanks
Faculty members and mentors for their guidance and support.
Anantha Lakshmi Institute of Technology and Sciences for providing the academic environment to complete this project.
The open-source community for providing powerful libraries such as NumPy, Pandas, Scikit-learn, XGBoost, and Flask.
Everyone who contributed feedback and ideas during the development of this project.
This project is intended for educational and learning purposes.](https://github.com/bunnydasari9/smartlender-loan)
## Verified
- `train.py` pipeline runs end-to-end (verified locally with a fallback classifier
  in place of XGBoost, since this sandbox has no internet to install it — your
  local install will use real XGBoost per the script).
- `app.py`'s `/predict` endpoint tested against both scenarios from the guide's
  Part 8.5: the low-risk profile returned "approved" with ~99.9% confidence, and
  the high-risk profile returned "rejected" with ~99.2% confidence.
