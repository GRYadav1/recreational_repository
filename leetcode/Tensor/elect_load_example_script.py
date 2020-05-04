
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
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

df=pd.read_csv('elec_load_data.csv')
df['Date'] = pd.to_datetime(df['Date'])
df.index = df['Date'] #setting date as the index
del df['Date']
#df.index.freq='H'
#df['hour'] = df.index.hour
#df['month'] = df.index.month
#df['weekday'] = df.index.dayofweek
#df['dayofyear'] = df.index.dayofyear
#df['T2'] = df.Temp.pow(2)
#df['T3'] = df.Temp.pow(3)
#    
       
        

#df=df.fillna(method='backfill')
    

x=df.iloc[:,1:]
y=df.iloc[:,0]

#scalar = MinMaxScaler()
#scalar.fit(x)
#x = scalar.transform(x)
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3334,random_state=36, shuffle=False) #splitting the dataset

##########RAndom Forest################


#########RAndom
from sklearn.ensemble import RandomForestRegressor
XGB = RandomForestRegressor(n_estimators=350)
XGB.fit(x_train,y_train)
y_pred=XGB.predict(x_test)
mape=mean_absolute_percentage_error(y_test, y_pred)
print('MAPE', mape)

##############GB = GradientBoostingRegressor(n_estimators=150)

from sklearn.ensemble import GradientBoostingRegressor
GB = GradientBoostingRegressor(n_estimators=150)
GB.fit(x_train,y_train)
y_pred=GB.predict(x_test)
mape=mean_absolute_percentage_error(y_test, y_pred)
print('GB', mape)
#################MLPRegressor##################ANN
from sklearn.neural_network import MLPRegressor

Neural_MLP = MLPRegressor(hidden_layer_sizes=(50,),max_iter=250)
#Neural_MLP = MLPRegressor()
Neural_MLP.fit(x_train,y_train) #Fitting the Model
y_pred = Neural_MLP.predict(x_test) #Predicting on Test DataSet
mape=mean_absolute_percentage_error(y_test, y_pred)
print('MAPE', mape)
#################################LASSO###############
from sklearn.linear_model import LassoLarsCV
#from sklearn import preprocessing
Lasso_model=LassoLarsCV()
Lasso_model.fit(x_train,y_train)
y_pred = Lasso_model.predict(x_test) # we are predicting the values from the test dataset
mape=mean_absolute_percentage_error(y_test, y_pred)
print('MAPE', mape)

#########linear regression
from sklearn.linear_model import LinearRegression 
lm = LinearRegression() #creatingan object of linear regression model
lm.fit(x_train,y_train) #running the model.
y_pred = lm.predict(x_test)
mape=mean_absolute_percentage_error(y_test, y_pred)
print('MAPE', mape)




