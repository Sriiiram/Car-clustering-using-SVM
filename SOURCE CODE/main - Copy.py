import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.feature_extraction.text import TfidfVectorizer

import re

'''======================================================
==========Read Data & Checking Missing Values============
========================================================='''

data = pd.read_csv('CARS.csv',na_values = [None, 'NaN','Nothing'], header = 0,error_bad_lines=False)
print(data.head())
data.info()
print data
print ("Checking Missing Values \n")
print data.isnull()

'''======================================================
======================Categories=========================
========================================================='''

labels = data['Type'].astype('category').cat.categories.tolist()
replace_map_comp = {'Type' : {k: v for k,v in zip(labels,list(range(1,len(labels)+1)))}}
print("Checking Categories \n")
print(replace_map_comp)



'''======================================================
======================Pre-processing=====================
========================================================='''
data['normalizedInvoice'] = StandardScaler().fit_transform(data['Invoice'].values.reshape(-1,1))
data = data.drop(['Invoice'],axis=1)
print(data.head())
data.info()
print "Pre-processing \n"
print(data['normalizedInvoice'])
'''======================================================
======================PCA Algorithm======================
========================================================='''



'''======================================================
======================Feature Extraction=================
========================================================='''
tvec = TfidfVectorizer(max_features=100000,ngram_range=(1, 3))
x_train_tfidf = tvec.fit_transform(data)
print("Feat_Ext_Values \n")
print(x_train_tfidf)

data.head()

data.head()

X = data.iloc[:, data.columns != 'Type']
y = data.iloc[:, data.columns == 'Type']
print("Input Data",X)
print("Input label",y)
y.head()















































