import matplotlib.pyplot as plt
import sklearn.metrics as mt
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier


def Random_Forest_Classifier(met_train,met_test,aqi_train,aqi_test):
    model = RandomForestClassifier(n_estimators=266,
                                   criterion='gini',random_state=0)
    model.fit(met_train,aqi_train)

    accuracy = mt.accuracy_score(aqi_test, model.predict(met_test))*100
    return model, accuracy


def KNN(met_train,met_test,aqi_train,aqi_test):
    model = KNeighborsClassifier(n_neighbors=10,algorithm='auto')
    model.fit(met_train,aqi_train)
    acc = mt.accuracy_score(aqi_test,model.predict(met_test))
    accuracy = mt.accuracy_score(aqi_test,model.predict(met_test))*100
    return model, accuracy


def Decision_tree(met_train,met_test,aqi_train,aqi_test):
    model = DecisionTreeClassifier(criterion='entropy', random_state=0, max_leaf_nodes=6)
    model.fit(met_train,aqi_train)
    accuracy = mt.accuracy_score(aqi_test,model.predict(met_test))
    return model, accuracy



def SVM(met_train,met_test,aqi_train,aqi_test):
    from sklearn.svm import SVC
    model = SVC(kernel='rbf', random_state=0)
    model.fit(met_train, aqi_train)
    accuracy = mt.accuracy_score(aqi_test,model.predict(met_test))*100
    return model, accuracy


def plot(model, model_name,met_test,aqi_test):
    plt.plot(np.array(np.arange(1,174,1)),model.predict(met_test),color='red')
    plt.plot(np.array(np.arange(1,174,1)),aqi_test,alpha=0.5)
    plt.title("actual value vs predicted value using "+model_name+" Classifier")
    plt.legend(('predicted value', 'actual value'),loc='lower left')
    plt.xlabel("days-->")
    plt.ylabel("Aqi category -->")
    plt.show()
    plt.show()

