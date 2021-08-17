import pandas
import matplotlib

import pylab as pl

from sklearn.cluster import KMeans
import numpy as np
from sklearn.decomposition import PCA
import datetime
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn import preprocessing
from sklearn.dummy import DummyClassifier
#from sklearn.cross_validation import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix, recall_score, accuracy_score, precision_score
import itertools
#from mpl_toolkits.basemap import Basemap

def kmean_plot():
    variables = pandas.read_csv('cleaned_data.csv')
    variables_new = variables[variables['Primary Type']=='THEFT']
    Y = np.array(variables_new[['Latitude']])

    X = np.array(variables_new[['Longitude']])

    X_train, X_test, y_train, y_test = train_test_split(X,Y,test_size=.1, random_state=42)

    '''
    kmeans
    '''

    kmeans_obj=KMeans(n_clusters=3)

    #train
    kmeans_obj.fit(X_train)

    labels = kmeans_obj.predict(X_train)
    print(labels.shape)
    print(X_train.shape)
    print(y_train.shape)

    '''
    output
    '''
    plt.scatter(X_train[:, 0], y_train[:, 0], c=labels)
    plt.show()

    '''
    perdict kmeans?!?!?!?
    '''

    perdict_new_sample_lables = kmeans_obj.predict(X_test)

    plt.scatter(X_train[:, 0], y_train[:, 0], c=labels)
    plt.scatter(X_test[:, 0], y_test[:, 0], c=perdict_new_sample_lables, marker="x")
    plt.show()
