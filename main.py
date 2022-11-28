from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

iris = datasets.load_iris()
data_train, data_test, target_train, target_test = train_test_split(iris.data, iris.target)
clf = MLPClassifier()
clf.fit(data_train, target_train)
print(clf.score(data_test, target_test))