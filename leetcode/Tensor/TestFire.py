'''
Created on 27-Feb-2019

@author: gaurav
'''
import pandas as pd
from pandas.plotting import scatter_matrix
import numpy as np
import seaborn as sns
#import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import pyplot    


from pandas.plotting import autocorrelation_plot
from sklearn.model_selection import train_test_split # importing the function from sklearb which splits data into training and test
from sklearn.preprocessing import MinMaxScaler

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import GridSearchCV
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn import metrics #importing the function metrics from sklearn 
from sklearn.metrics import explained_variance_score

def mean_absolute_percentage_error(y_true, y_pred): 
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    #print(y_true, y_pred)
    x=np.mean(np.abs((y_true - y_pred) / y_true)) * 100
    #print(x)
    return x

def writetocsv(y):
    csv = open('PredictionPower.csv', "w")
    heading = 'Power' + '\n' 
    csv.write(heading)
    for i in y:
        row= str(i)+"\n"
        csv.write(row)
        
        
# Training code #
df=pd.read_csv('elec_load_data.csv',delimiter='\t')
#print(df['Date'])
df['Date'] = pd.to_datetime(df['Date'])
x=df.iloc[:,1:]
df['Moving_Temp']= df['Temp'].rolling(3234).mean()

df.index = df['Date'] #setting date as the index
#print(df.index)
del df['Date']
print(df['Moving_Temp'])


print("----")

y=df.iloc[:,0]
print(y)

#print(df.keys())
#print(x)
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3334,random_state=36, shuffle=False) #splitting the dataset

#Prediction Code #

df_final = pd.read_csv('actual_data.csv',delimiter=',')
#print(df_final['Date'])
df_final['Date'] = pd.to_datetime(df_final['Date'])
#print(df_final.keys())
df_final.index = df_final['Date']


del df_final['Date']

x_final = df_final.iloc[:,0:]

#***********Linear Regression
from sklearn.linear_model import LinearRegression 
lm = LinearRegression() #creatingan object of linear regression model
lm.fit(x_train,y_train) #running the model.
y_pred = lm.predict(x_test)

mape=mean_absolute_percentage_error(y_test, y_pred)

print('(LR)-MAPE', mape)

#################################LASSO###############
from sklearn.linear_model import LassoLarsCV
#from sklearn import preprocessing
Lasso_model=LassoLarsCV(cv=5)
Lasso_model.fit(x_train,y_train)
y_pred1 = Lasso_model.predict(x_test) # we are predicting the values from the test dataset
mape=mean_absolute_percentage_error(y_test, y_pred1)
print('LASSO-MAPE', mape)

##########RAndom Forest################
#########RAndom
from sklearn.ensemble import RandomForestRegressor
XGB = RandomForestRegressor(n_estimators=350)
XGB.fit(x_train,y_train)
y_pred=XGB.predict(x_test)
y_final = XGB.predict(x_final)
print("Random Forest Regression:-------------------")
#print(y_final)
mape=mean_absolute_percentage_error(y_test, y_pred)
print('Random Forest -MAPE', mape)

##############GB = GradientBoostingRegressor(n_estimators=150)

from sklearn.ensemble import GradientBoostingRegressor
GB = GradientBoostingRegressor(n_estimators=150)
GB.fit(x_train,y_train)
y_pred=GB.predict(x_test)
y_final = GB.predict(x_final)
print("GB Regression:-------------------")
print(y_final)
print("Result written to file PredictionPower.csv!!")
writetocsv(y_final)
mape=mean_absolute_percentage_error(y_test, y_pred)
print('GB Mape:', mape)

#################MLPRegressor##################ANN
from sklearn.neural_network import MLPRegressor

Neural_MLP = MLPRegressor(hidden_layer_sizes=(50,),max_iter=250)
#Neural_MLP = MLPRegressor()
Neural_MLP.fit(x_train,y_train) #Fitting the Model
y_pred = Neural_MLP.predict(x_test) #Predicting on Test DataSet
y_final = Neural_MLP.predict(x_final)
print("MLRegression:-------------------")
#print(y_final)
mape=mean_absolute_percentage_error(y_test, y_pred)
print('ML Regressor MAPE:', mape)
############################

##Let the prediction begin....

##########Ridge Regression 

from sklearn.linear_model import Ridge

ridgeReg = Ridge(alpha=1)
ridgeReg.fit(x_train,y_train)
y_pred = ridgeReg.predict(x_test)
y_final = ridgeReg.predict(x_final)
print("Ridge Regression:-------------------")
print(y_final)
mape = mean_absolute_percentage_error(y_test, y_pred)
print("Ridge MAPE:",mape)

#Huber Regression

from sklearn.linear_model import HuberRegressor

hr = HuberRegressor().fit(x_train,y_train)
print(hr.score(x_train,y_train) )
y_pred=hr.predict(x_test)
y_final=hr.predict(x_final)
mape = mean_absolute_percentage_error(y_test, y_pred)

print("Huber Regressor:-------------------")
#print(y_final)
print("MAPE",mape)

############# Decision Tree Regressor ############
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(x_train, y_train)
y_pred=regressor.predict(x_test)
y_final=regressor.predict(x_final)
mape = mean_absolute_percentage_error(y_test, y_pred)
print("Decision Tree:-------------------")
#print(y_final)
print("MAPE",mape)
