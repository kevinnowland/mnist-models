""" module of classes holding modles, pretrained or otherwise """

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC


class MnistModel:
    """ class for models """

    def __init__(self, model):
        self.__model = model
        self.__accuracy = None
        self.__is_trained = False

    @property
    def model(self):
        """ the model itself """
        return self.__model

    @property
    def accuracy(self):
        """ the accuracy, once fit """
        return self.__accuracy

    @property
    def is_trained(self):
        return self.__is_trained

    def fit(self, X_train, y_train, X_test, y_test):
        """ fit the model and record accuracy from test set"""

        if self.model is not None:
            self.model.fit(X_train, y_train)
            y_pred = self.model.predict(X_test)
            self.__accuracy = accuracy_score(y_test, y_pred)
            self.__is_trained = True

    def predict(self, X):
        """ predict with the model """

        if self.model is not None:
            return self.model.predict(X)


class SVMModel(MnistModel):
    """ class for the SVM model """

    def __init__(self):
        super().__init__(SVC())

    def __str__(self):
        return "SVMModel(is_trained={})".format(self.is_trained)


class LogisticModel(MnistModel):
    """ class for logistic regression model  """

    def __init__(self):
        super().__init__(LogisticRegression())

    def __str__(self):
        return "LogisticModel(is_trained={})".format(self.is_trained)
