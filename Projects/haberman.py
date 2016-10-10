#%%
import pandas as pd
#%matplotlib inline 
import matplotlib.pyplot as plt
#from sklearn import linear_model
from sklearn import metrics
from sklearn.cross_validation import train_test_split
plt.style.use('ggplot')
#%%
df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/haberman/haberman.data', header=None)
print(df[3].value_counts())
print(df[3].value_counts(normalize = True))
#print(df[3][df[2] > 0][df[0] >= 60].value_counts(normalize = True))
X = df.drop(3 , 1).values 
y = df[3].values
#%%
pd.DataFrame.hist(df, figsize = [15,15]); 
#%%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=12) 
#lr = linear_model.LogisticRegression()
#%%
## fit the model
#lr = lr.fit(X_train, y_train)
#Y_pred = lr.predict(X_test)
#Y_pred_prob=lr.predict_proba(X_test)
##print(Y_pred)
#print(Y_pred_prob)
#print(lr.score(X_train, y_train))
#
#print(lr.score(X_test, Y_pred))
#%%
#y_true, y_pred = y_test, lr.predict(X_test)
#print(metrics.confusion_matrix(y_true, y_pred))
##print(classification_report(y_true, y_pred)) 
#print(metrics.classification_report(y_true, y_pred))
#%%
print df.shape
print df.describe()
print len(df[0]>60)
#%%
#using random forests
from sklearn.ensemble import RandomForestClassifier
forest = RandomForestClassifier(max_depth = 10, min_samples_split=10, n_estimators = 100, random_state = 1)
my_forest = forest.fit(X_train, y_train)
print(my_forest.score(X_train, y_train))
y_true, y_pred = y_test, my_forest.predict(X_test)
print my_forest.score(X_test, y_test)
print(metrics.classification_report(y_true, y_pred))
#%%
#forest = RandomForestClassifier(max_depth = 10, min_samples_split=6, n_estimators = 100, random_state = 1)
#my_forest = forest.fit(X_train, y_train)
#print(my_forest.score(X_train, y_train))
#y_true, y_pred = y_test, my_forest.predict(X_test)
#print my_forest.score(X_test, y_test)
#print(classification_report(y_true, y_pred))
#%%
#forest = RandomForestClassifier(max_depth = 10, min_samples_split=8, n_estimators = 100, random_state = 1)
#my_forest = forest.fit(X_train, y_train)
#print(my_forest.score(X_train, y_train))
#y_true, y_pred = y_test, my_forest.predict(X_test)
##print my_forest.score(X_test, y_test)
#print(classification_report(y_true, y_pred))
#%%
#forest = RandomForestClassifier(max_depth = 10, min_samples_split=10, n_estimators = 100, random_state = 1)
#my_forest = forest.fit(X_train, y_train)
#print(my_forest.score(X_train, y_train))
#y_true, y_pred = y_test, my_forest.predict(X_test)
#print my_forest.score(X_test, y_test)
#print(classification_report(y_true, y_pred))
#%%
#forest = RandomForestClassifier(max_depth = 10, min_samples_split=12, n_estimators = 100, random_state = 1)
#my_forest = forest.fit(X_train, y_train)
#print(my_forest.score(X_train, y_train))
#y_true, y_pred = y_test, my_forest.predict(X_test)
#print my_forest.score(X_test, y_test)
#print(classification_report(y_true, y_pred))
#%%
#change random number
#forest = RandomForestClassifier(max_depth = 10, min_samples_split=10, n_estimators = 100, random_state = 5)
#my_forest = forest.fit(X_train, y_train)
#print(my_forest.score(X_train, y_train))
#y_true, y_pred = y_test, my_forest.predict(X_test)
#print my_forest.score(X_test, y_test)
#print(classification_report(y_true, y_pred))
