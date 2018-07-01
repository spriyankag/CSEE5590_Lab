from sklearn import neighbors, datasets
from sklearn import metrics

# import data
iris = datasets.load_iris()
data1 = iris.data[:, :]
data2 = iris.target

# Splitting the dataset into the training set and test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(data1, data2, test_size = 0.2, random_state = 123)

# consider the neighbors
neighbours =  [1,10,15,25,50]

#Iterate through the neighbors and predict the value of Y for each x value
for n in neighbours:
    clf = neighbors.KNeighborsClassifier(n)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print("Accuracy Score for K = ",n)
    print(metrics.accuracy_score(y_test, y_pred))