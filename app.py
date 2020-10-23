from flask import Flask,render_template,request
import numpy as np
import pickle
import pandas as pd

app = Flask(__name__,template_folder='Templates')

tree = pickle.load(open('./Models/Decision_Tree.sav','rb'))
lr = pickle.load(open('./Models/Logistic_Regression.sav','rb'))
scaler = pickle.load(open('./Models/scaler.sav','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods = ["POST"])
def predict():
     
    name = request.form["name"]
    age = int(request.form["age"])
    gender = int(request.form["gender"])
    married = int(request.form["married"])
    dependents = int(request.form["dependents"])
    education = int(request.form["education"])
    chistory = int(request.form["chistory"])
    employement = int(request.form["employement"])
    aincome = int(request.form["aincome"])
    caincome = int(request.form["caincome"])
    loan = int(request.form["loan"])
    duration = int(request.form["duration"])
    region = int(request.form["region"])
    model = int(request.form["model"])

    if model == 0:

        dt_feat = np.array([[gender,married,dependents,education,employement,aincome,
                        caincome,loan,duration,chistory,region,aincome+caincome,loan/(aincome+caincome)]])
        #print(dt_feat)
        pred = tree.predict(dt_feat)

    elif model == 1:
        
        cont_feat = np.array([[aincome,caincome,loan,duration,aincome+caincome,loan/(aincome+caincome)]])
        #print('Raw data :',cont_feat)
        cont_feat = scaler.transform(cont_feat)
        #print('Transformed data :',cont_feat)
        index = [0,1,2]
        cont_feat = np.delete(cont_feat,index)  # duration,aincome+caincome,loan/(aincome+caincome)
        dep = 1 if dependents == 2 else 0
        reg = 1 if region == 1 else 0
        lr_feat = np.array([[married,cont_feat[0],chistory,cont_feat[1],dep,reg,cont_feat[2]]])
        #print('LR features :',lr_feat)
        pred = lr.predict(lr_feat)
    
    elif model == 2:
        dt_feat = np.array([[gender,married,dependents,education,employement,aincome,
                        caincome,loan,duration,chistory,region,aincome+caincome,loan/(aincome+caincome)]])
        #print('Decision tree features :',dt_feat)
        dt_proba = tree.predict_proba(dt_feat)[:,1]
        

        cont_feat = np.array([[aincome,caincome,loan,duration,aincome+caincome,loan/(aincome+caincome)]])
        #print('Raw data :',cont_feat)
        cont_feat = scaler.transform(cont_feat)
        #print('Transformed data :',cont_feat)
        index = [0,1,2]
        cont_feat = np.delete(cont_feat,index)  # duration,aincome+caincome,loan/(aincome+caincome)
        dep = 1 if dependents == 2 else 0
        reg = 1 if region == 1 else 0
        lr_feat = np.array([[married,cont_feat[0],chistory,cont_feat[1],dep,reg,cont_feat[2]]])
        #print('LR features :',lr_feat)
        lr_proba = lr.predict_proba(lr_feat)[:,1]
        #print('LR probability is :',lr_proba)
        #print('DT probability is :',dt_proba)
        final = (dt_proba+lr_proba)/2
        #print('Final probability is :',final)
        if final < 0.5:
            pred = 0
        else:
            pred = 1

    if pred == 0:
        text = 'Sorry '+ name +', you are not eligible for a loan! Please contact the team for further details.'
    else:
        text = 'Hi '+ name +', you are eligible for a loan! Please contact the team for further information.' 

    return render_template('response.html',prediction_text = text, 
                            name_text = name,age_text = str(age),
                            gender_text = str(gender),married_text = str(married),
                            dep_text = str(dependents),grad_text = str(education),
                            chistory_text = str(chistory),emp_text = str(employement),
                            aincome_text = str(aincome),caincome_text = str(caincome),
                            loan_text = str(loan),dur_text = str(duration),reg_text = str(region),
                            model_text = str(model))



if __name__ == "__main__":
    app.run(host = '0.0.0.0',port = 7000,debug=True)