from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'home.html')

def getPred(pclass, sex, age, sibsp, parch, embarked):
    import joblib
    from sklearn.preprocessing import StandardScaler
    import pandas as pd
    model=joblib.load('titanic_model.sav')
    sc=joblib.load('scaled.sav')
    prediction=model.predict(sc.transform([[pclass,sex,age,sibsp,parch,embarked]]))

    if prediction == 0:
        return "Dead"
    elif prediction==1:
        return "Survived"
    else:
        return "error"

def result(request):
    lst=[]
    if request.POST['pclass']=='':
        lst.append("pclass")
    if request.POST['sex']=='':
        lst.append("sex")
    if request.POST['age']=='':
        lst.append("age")
    if request.POST['sibsp']=='':
        lst.append("Sibling/Spouse")
    if request.POST['parch']=='':
        lst.append("Parent/Children")
    if request.POST['embarked']=='':
        lst.append("embarked")
    if len(lst)==0:
        #lst=[]
        pclass=int(request.POST['pclass'])
        sex=int(request.POST['sex'])
        age=int(request.POST['age'])
        sibsp=int(request.POST['sibsp'])
        parch=int(request.POST['parch'])
        embarked=int(request.POST['embarked'])
        result=getPred(pclass,sex,age,sibsp,parch,embarked)
        return render(request,'result.html',{'result':result})
    else:
        return render(request,'messages.html',{'list':lst})



def again(request):
    return render(request,'home.html')

def retreat(request):
    return render(request,'home.html')