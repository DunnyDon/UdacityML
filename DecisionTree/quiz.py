# Import statements 
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
# Read the data.
data = np.asarray(pd.read_csv('data.csv', header=None))
# Assign the features to the variable X, and the labels to the variable y. 
X = data[:,0:2]
y = data[:,2]
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.05, random_state=42) 

# TODO: Create the decision tree model and assign it to the variable model.
# You won't need to, but if you'd like, play with hyperparameters such
# as max_depth and min_samples_leaf and see what they do to the decision
# boundary.
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# TODO: Fit the model.

# TODO: Make predictions. Store them in the variable y_pred.
y_pred = model.predict(X_test)

# TODO: Calculate the accuracy and assign it to the variable acc.
acc = accuracy_score(y_test,y_pred)
