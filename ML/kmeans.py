# -*- coding: utf-8 -*-

from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.preprocessing import Normalizer
import matplotlib.pyplot as plt

iris = datasets.load_iris()
#归一化数据
iris.data = Normalizer().fit_transform(iris.data)


X = iris.data[:,[0,3]]
Y = iris.target

'''plt.scatter(X[Y==0,0],X[Y==0,1],color = "r")
plt.scatter(X[Y==1,0],X[Y==1,1],color = "b")
plt.scatter(X[Y==2,0],X[Y==2,1],color = "y")
'''
figure1 = plt.figure()
plt.scatter(X[:,0],X[:,1],c=Y)


model = KMeans(n_clusters = 3)
model.fit(iris.data)
Y_ = model.predict(iris.data)

figure2 = plt.figure()
plt.scatter(X[:,0],X[:,1],c=Y_)
plt.title("predict")

