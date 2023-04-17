# import pandas as pd
#
# df = pd.read_csv('Complete-data.csv')
#
# print(df['Landslide'])

import numpy as np

# using loadtxt()
arr = np.loadtxt("Complete-data1.csv",
                 delimiter=",", dtype=int)
print(arr)
x=arr[:,1:13]
y=arr[:,0]





import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report



X_train, X_test, y_train, y_test = train_test_split(
        x, y, test_size=0.3, random_state=100)

clf_gini = DecisionTreeClassifier(criterion="gini",
                                      random_state=100, max_depth=3, min_samples_leaf=5)

# Performing training
clf_gini.fit(X_train, y_train)
y_pred = clf_gini.predict(X_test)

print("Confusion Matrix: ",
          confusion_matrix(y_test, y_pred))

print("Accuracy : ",
      accuracy_score(y_test, y_pred) * 100)

print("Report : ",classification_report(y_test, y_pred))

# Define a new data point as a dictionary with the same column names as your dataset
new_data_point = {'Aspect': 30, 'Curvature': 10, 'Earthquake': 0, 'Elevation': 500, 'Flow': 100,
                  'Lithology': 0, 'NDVI': 0.1, 'NDWI': 0.2, 'Plan': 0.8, 'Precipitation': 200, 'Profile': 1,
                  'Slope': 10}

# Create a Pandas dataframe with the new data point
new_data_df = pd.DataFrame([new_data_point])

# Use the trained model to make a prediction on the new data point
prediction = clf_gini.predict(new_data_df)

# Print the predicted class label
print(prediction)