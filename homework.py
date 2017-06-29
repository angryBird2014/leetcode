import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegressionCV
from sklearn.metrics import accuracy_score

tuned_parameters = [{'kernel': ['rbf'], 'gamma': [1e-3, 1e-4],
                     'C': [1, 10, 100, 1000]},
                    {'kernel': ['linear'], 'C': [1, 10, 100, 1000]}]

tuned_parameters_logicRegression = [0.01,1,10,100]
score = 'accuracy'

def loadData(trainFileName,testFileName):
    trainData = pd.read_csv(trainFileName,delim_whitespace=True,names=['one','two','three'])
    testData = pd.read_csv(testFileName,delim_whitespace=True,names=['one','two','three'])
    plt.scatter(trainData['one'], trainData['two'], c=['r','b'])
    plt.show()
    return trainData.loc[:,['one','two']],trainData.loc[:,['three']],testData.loc[:,['one','two']],testData.loc[:,['three']]

def SVMEstimator(x_train,x_test,y_train,y_test,testData,testDataLabel):
    r,c = y_train.shape
    y_train =y_train.values.reshape(r,)
    r_,c_ = y_test.shape
    y_test = y_test.values.reshape(r_)
    clf = GridSearchCV(SVC(C=1), tuned_parameters, cv=5,scoring=score)
    clf.fit(x_train,y_train)
    print("Best parameters set found on development set:")
    print(clf.best_params_)
    print("Grid score on development set:")
    y_predict = clf.predict(x_test)
    print("accuracy_%s" % accuracy_score(y_test,y_predict))
    print("SVM on test set:")
    test_predict = clf.predict(testData)
    print("accuracy_%s" % accuracy_score(testDataLabel, test_predict))

def Logistic_Regression_estimator(x_train,x_test,y_train,y_test,testData,testDataLabel):
    r, c = y_train.shape
    y_train = y_train.values.reshape(r, )
    r_, c_ = y_test.shape
    y_test = y_test.values.reshape(r_)
    clf = LogisticRegressionCV(tuned_parameters_logicRegression)
    clf.fit(x_train, y_train)
    print("Best parameters set found on development set:")
    print(clf.get_params())
    y_predict = clf.predict(x_test)
    print("accuracy_%s" % accuracy_score(y_test, y_predict))
    print("logisticRegression on test set:")
    test_predict = clf.predict(testData)
    print("accuracy_%s" % accuracy_score(testDataLabel, test_predict))

if __name__ == '__main__':
    trainFileName = 'train.txt'
    testFileName = 'test.txt'
    trainData,trainDataLabel,testData,testDataLabel = loadData(trainFileName,testFileName)
    x_train,x_test,y_train,y_test = train_test_split(trainData,trainDataLabel,test_size=0.4,random_state=0)
    print(x_train.shape,y_train.shape)
    print("-----svm------")
    SVMEstimator(x_train,x_test,y_train,y_test,testData,testDataLabel)
    print("-----logisticRegression------")
    Logistic_Regression_estimator(x_train,x_test,y_train,y_test,testData,testDataLabel)