# AV-Loan-Application-Approval-System
Flask app on AV Hackathon on Loan approval prediction system with Docker images

Author : Patnana Manikantha Devasish

Approach :

1. Exploratory Data Analysis : Task involves data exploration, cleaning, build visualisations in a loop.
2. Model Building : Build basic classifiers LogisticRegression and DecisionTree and assess the performance of the model with the metrics chosen.
3. Flask Application : Build a flask application which exposes the model through User interface and allows input values from the Front End and shows the results instantly on the Front End. 
4. Docker Image : Containerize the docker application and build an image for the application.

Note : The application is built on few libraries and they are captured in requirements.txt

Choice of Classifiers :
Firstly, I chose to start with basic classfier examine the metrics and then try a boosintg based ensemble model but, with the amount of data present boosing based models could not be implemented. So, I have decided to implement a basic decision tree classifier. Both the implementations have fetched me similar results in terms of Metrics. So I have  experimented with the idea of stacking the prediction probabilities and average the values and predict the outcome of the loan application. The stacked model has not been tested on the Notebooks with respect to the metrics but has been implemented on the Flask Application due to lack of time. Hence this feature has to be tested thoroughly. 

Steps to launch the app:

1. Create a virtual environment and install the required libraries from requirements.txt .
2. Open command prompt in the directory where the file app.py resides and run the command 'python app.py'.

or alternatively

Use the Dockerfile present in the application and install the application. 

Prerequisites : Dockers is installed.

Steps to launch the app via Dockers :

1. Pull the git repo and navigate to the path where file named 'Dockerfile' resides and launch a commandline terminal and navigate to the application.
2. Execute the following commands:

docker build -t flask_loan_app .

docker run --rm -p <Internal Port>:7000 flask_loan_app  # Replace <Internal Port> with an appropriate port available on your system  

Ex : docker run --rm -p 5000:7000 flask_loan_app

3. If the above step is successful, launch the docker via http://localhost:<Internal Port>/ on a Browser(Preferred Google Chrome).

In case there is a need to debug the container or the code inside the docker, please follow the steps:
1. Launch the CLI inside the Docker.
2. Run the following commands.

apt-get update

apt-get install vim   # Press Y when prompted for any download alert

Challenges and Limitations :

1. Even though the data size is low, imputation of missing data in few features had to be carried out carefully with lot of thought, assumptions and multiple iterations.
2. The application built is a light weight application.

Future Work :

1. Attach a database to the Backend and keep track of the applications.
2. Create a login page where the application can be accessed based on the role assigned. The selection of classifier on the UI can be updated, maintained and also be used as a configuration setting for final production environment.
3. If the credit History of the customer is available on the platform, display few insights on a separate page.

Demo of the App:

![Landing page](https://github.com/mdevasish/Feige_Loan_Application_Approvals/blob/master/Screenshots/Demo.gif)

View the app at https://loanapplicationapproval.herokuapp.com/
