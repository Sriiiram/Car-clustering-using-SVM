import warnings
warnings.filterwarnings('ignore')

import os
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder


cars = pd.read_csv('CARSs.csv', delimiter=',')
print cars

lux_cars=cars.loc[(cars['Type']=='Sedan')]


X=lux_cars[['MSRP','Cylinders','Horsepower','Weight','Length']]
yy=lux_cars['Model']
le = LabelEncoder()

le.fit(list(yy))
y = le.transform(yy)


##from sklearn.svm import SVC
##
##clf =SVC()
from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier(n_neighbors=3)
#clf =OneVsOneClassifier(SVC())
clf.fit(X, y) 
#clf.fit(X, y) 

##car_MSRP=input("Enter MSRP")
##car_Weight=input("Enter Weight")
##car_Length=input("Enter Length")
def get_detail(car_MSRP,car_Cylinders,car_HP,car_Weight,car_Length):
    df={'col1':[car_MSRP],'col2':[car_Cylinders],'col3':[car_HP],'col4':[car_Weight],'col5':[car_Length]}

    x_test=pd.DataFrame(df)
    pred, neigh=clf.predict(x_test)
    temp_label=[]
    temp_ans=[]
    neigh_pred=neigh[0]
    for i in range(0,len(neigh_pred)):
        temp_le=le.inverse_transform([neigh_pred[i]])
        ans=cars.loc[(cars['Model']==temp_le[0])]
        ans=str(ans)
        #ans=str(ans[:-20:1])
        temp_label.append(ans)
    seperator = '\n'
    result=seperator.join(temp_label)
    result=" ".join(result.split("[1 rows x 15 columns]"))
    result=" ".join(result.split("[2 rows x 15 columns]"))
    return result
    '''pred_y=le.inverse_transform(pred)
    ans=cars.loc[(cars['Model']==pred_y[0])]
    return (ans.iloc[0].values)'''
if __name__=="__main__":
    #print(get_detail(89765,17,24))
    print "luxury n performance cars"
