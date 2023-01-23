from django.shortcuts import render;
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn import metrics
def home(request):
    return render(request,'home.html')

def predict(request):
    return render(request,'predict.html')

def result(request):
    df=pd.read_csv("C:\\Users\\param\\OneDrive\\Desktop\\USA_Housing.csv")
    df=df.drop(['Address'],axis=1)
    X=df.drop(['Price'],axis=1)
    Y=df['Price']
    x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=.30)
    model=LinearRegression()
    model.fit(x_train,y_train)
    var1=float(request.GET['n1'])
    var2=float(request.GET['n2'])
    var3=float(request.GET['n3'])
    var4=float(request.GET['n4'])
    var5=float(request.GET['n5'])
    
    pred=model.predict(np.array([var1,var2,var3,var4,var5]).reshape(1,-1))
    pred=round(pred[0])
    price="The Predicted Price is $"+str(pred)

    return render(request,'predict.html',{"result":price})