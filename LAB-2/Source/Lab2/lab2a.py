import matplotlib.pyplot as plot

from sklearn import datasets
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Load the dataset
iris = datasets.load_iris()

#load the details into variables
data = iris.data
target = iris.target
input_data = iris.target_names

# Split the data into test and training sets
X_train_Data, X_test_Data, y_train_Data, y_test_Data = train_test_split(data, target, test_size=0.732)

# apply knnclassifier: neighbors=5 and create a model for training data
classifier_input = KNeighborsClassifier(n_neighbors=5)
classifier_input.fit(X_train_Data, y_train_Data)

# Predict the value of Y using test X
y_predictor = classifier_input.predict(X_test_Data)

#Apply LDA
lda_data = LinearDiscriminantAnalysis(n_components=2)
X_r2 = lda_data.fit(X_test_Data, y_predictor).transform(data)

plot.figure()
colors_array = ['red', 'green', 'blue']
lw = 2

#Plot the graph
for color, i, target_name in zip(colors_array, [0, 1, 2], input_data):
    plot.scatter(X_r2[target == i, 0], X_r2[target == i, 1], alpha=.8, color=color,
                label=target_name)
plot.legend(loc='best', shadow=False, scatterpoints=1)
plot.title('Prediction Model-Iris data using LDA')

plot.show()