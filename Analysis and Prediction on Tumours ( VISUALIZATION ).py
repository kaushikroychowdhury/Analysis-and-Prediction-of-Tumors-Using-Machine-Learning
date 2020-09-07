import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

raw_data = pd.read_csv("data.csv")
data = pd.read_csv("data.csv")
#print(data.columns)

## BASIC PRE-PROCESSING OF THE DATASET ..........................................................

raw_data.drop('Unnamed: 32', axis = 1, inplace = True)
x = raw_data.iloc[:,:]
y = raw_data.iloc[:,1]
x.drop(['id', 'diagnosis'], axis = 1,  inplace = True)

#print(x.info())
# print(y)

## VISUALIZATION .....................................................................................................

plt.style.use(['ggplot'])
sns.pairplot(data.loc[:,'diagnosis':'area_mean'], hue="diagnosis")
print(plt.show())

y.value_counts().plot(kind ="pie", colors=['r','b'])
print(plt.show())

y.value_counts().plot(kind ="bar",  color ='b')
print(plt.show())

data_B = data[data.diagnosis != 'M']
data_M = data[data.diagnosis != 'B']

data_B.plot(kind='density', x= 'radius_mean', y= 'concavity_mean')
plt.xlabel("Radius Mean For Benign")
plt.ylabel("Concavity Mean For Benign")
print(plt.show())

data_M.plot(kind='density', x= 'radius_mean', y= 'concavity_mean')
plt.xlabel("Radius Mean For Malignant")
plt.ylabel("Concavity Mean For Malignant")
print(plt.show())

g = sns.jointplot(x = data_B['radius_mean'], y = data_B['texture_mean'], data=data_B, kind="hex", color='b')
g.set_axis_labels("$mean radius for malignant$", "$mean texture for malignant$")
print(plt.show())

g = sns.jointplot(x = data_M['radius_mean'], y = data_M['texture_mean'], data=data_M, kind="hex")
g.set_axis_labels("$mean radius for malignant$", "$mean texture for malignant$")
print(plt.show())

g = sns.PairGrid(data_B.loc[:,'radius_mean':'smoothness_mean'])
g.map_diag(sns.kdeplot)
g.map_offdiag(sns.kdeplot, color = 'b')
print(plt.show())

g=sns.PairGrid(data_M.loc[:,'radius_mean':'smoothness_mean'])
g.map_diag(sns.kdeplot, color='b')
g.map_offdiag(sns.kdeplot)
print(plt.show())

## Correlation map

f,ax = plt.subplots(figsize=(18, 18))
sns.heatmap(x.corr(), annot=True, linewidths=.5, fmt= '.1f',ax=ax)
print(plt.show())