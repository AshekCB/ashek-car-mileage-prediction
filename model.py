import pandas as pd
import math as m
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

df=pd.read_csv("https://github.com/AshekCB/ashek-car-mileage-prediction/raw/main/car%20mileage%20prediction.csv")
df=df.drop(['Unnamed: 0'],axis=1)
x=df.drop(['mpg'],axis=1)
y=df['mpg']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)


model=RandomForestRegressor()
model.fit(x_train,y_train)

def predict(cyl,dis,hp,wt,acc,model_y,origin):
    d={
        "cylinders":cyl,
        "displacement":dis,
        "horsepower":hp,
        "weight":wt,
        "acceleration":acc,
        "model_year":model_y,
        "origin":origin
    }
    test_df=pd.DataFrame(d,index=[0])
    res=model.predict(test_df)
    return m.ceil(res[0])
#8	307.0	130.0	3504	12.0	70	usa-->18
#print(predict(8,307,130,3504,12,70,0))
