import pandas as pdfrom sklearn import datasetsfrom sklearn.metrics import confusion_matrix, accuracy_scoreimport numpy as npfrom sklearn.model_selection import train_test_splitfrom sklearn.tree import DecisionTreeClassifierfrom joblib import dump, loaddata_set=NoneX=y=None# dividing X, y into train and test datadef dttrain(X,y):    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)    # Create Decision Tree classifer object    clf = DecisionTreeClassifier()    # Train Decision Tree Classifer    clf = clf.fit(X_train, y_train)    dump(clf,'dtmodel.joblib')    yp=clf.predict(X_test)    print("Score for Decision Tree is :",accuracy_score(y_test, yp))    from sklearn.metrics import classification_report    target_names = ['Negative', 'positive']    print("Classification Report")    print(classification_report(y_test, yp, target_names=target_names))X=[]y=[]import numpy as np# using loadtxt()arr = np.loadtxt("landslide_dataset.csv",delimiter=",", dtype=str)ii=0for i in arr:    if ii!=0:        row=[float(i[0]),             float(i[1]),             float(i[2]),             float(i[3]),             float(i[4]),             float(i[5]),             float(i[6]),             float(i[7]),             float(i[8]),             ]        X.append(row)        y.append(int(i[9]))    ii=ii+1dttrain(X,y)