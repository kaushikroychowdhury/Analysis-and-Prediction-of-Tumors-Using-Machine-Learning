import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

raw_data = pd.read_csv("data.csv")
data = pd.read_csv("data.csv")

raw_data.drop('Unnamed: 32', axis = 1, inplace = True)
x = raw_data.iloc[:,:]
y = raw_data.iloc[:,1]
x.drop(['id', 'diagnosis'], axis = 1,  inplace = True)

B,M = y.value_counts()
#print(B,M)

# There are 357 Benign cells and 212 Malignant cells

# Let's Split the data into Train and Test Sections ................................................

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=1)

print("FITTING & TESTING DIFFERENT CLASSIFICATION MODELS ( without scaling the data )")

# Random Forest Classifier
model = RandomForestClassifier(n_estimators = 100)
model.fit(x_train, y_train)
prediction = model.predict(x_test)
print("Random Forest : ", metrics.accuracy_score(prediction, y_test)*100)

# Decision Tree Classifier
model = DecisionTreeClassifier()
model.fit(x_train, y_train)
prediction = model.predict(x_test)
print("Decision Tree : ", metrics.accuracy_score(prediction, y_test)*100)

# SVM ( Support Vector Machine )
model = svm.SVC()
model.fit(x_train, y_train)
prediction = model.predict(x_test)
print("Support Vector Machine : ", metrics.accuracy_score(prediction, y_test)*100)

# KNN (K Nearest Neighbour Classifier )
model = KNeighborsClassifier(n_neighbors=5)
model.fit(x_train, y_train)
prediction = model.predict(x_test)
print("K Nearest Neighbours : ", metrics.accuracy_score(prediction, y_test)*100)

# Gaussian Naive Bayes Algorithm
model = GaussianNB()
model.fit(x_train, y_train)
prediction = model.predict(x_test)
print("Naive Bayes Algorithm : ", metrics.accuracy_score(prediction, y_test)*100)

## Random Forest and Naive Bayes Algorithm performs best ..
## SVM performs worst ..

###  Now let's Scale the Data .....................................................................................

scale = StandardScaler()
x = scale.fit_transform(x)

# splitting the data into Train and Test Section

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)
print(" ")
print("FITTING & TESTING DIFFERENT CLASSIFICATION MODELS ( with scaled data )")

# Random Forest Classifier
model = RandomForestClassifier(n_estimators = 100)
model.fit(x_train, y_train)
prediction = model.predict(x_test)
print("Random Forest : ", metrics.accuracy_score(prediction, y_test)*100)

# Decision Tree Classifier
model = DecisionTreeClassifier()
model.fit(x_train, y_train)
prediction = model.predict(x_test)
print("Decision Tree : ", metrics.accuracy_score(prediction, y_test)*100)

# SVM ( Support Vector Machine )
model = svm.SVC()
model.fit(x_train, y_train)
prediction = model.predict(x_test)
print("Support Vector Machine : ", metrics.accuracy_score(prediction, y_test)*100)

# KNN (K Nearest Neighbour Classifier )
model = KNeighborsClassifier(n_neighbors=5)
model.fit(x_train, y_train)
prediction = model.predict(x_test)
print("K Nearest Neighbours : ", metrics.accuracy_score(prediction, y_test)*100)

# Gaussian Naive Bayes Algorithm
model = GaussianNB()
model.fit(x_train, y_train)
prediction = model.predict(x_test)
print("Naive Bayes Algorithm : ", metrics.accuracy_score(prediction, y_test)*100)

### After Scaling the Data .. SVM performs best of all