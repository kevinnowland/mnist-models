"""module of classes holding models, pretrained or otherwise. The
SVMModel and LogisticModel classes do not admit any hyperparameter
changes, so any change requires using the basic MnistModel class.
"""

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC


class MnistModel:
    """Base class from which model specific classes will be built.

    :param model: an untrained model object to wrap into this class. must
        have fit(X, y) and predict(y) functions.
    :type: sklearn style model object
    """

    def __init__(self, model):
        """constructor method
        """
        self.__model = model
        self.__accuracy = None
        self.__is_trained = False

    @property
    def model(self):
        """the model the class contains

        :return: the model
        :rtype: model object
        """
        return self.__model

    @property
    def accuracy(self):
        """accuracy on test set once the model has been fit

        :return: test set accuracy
        :rtype: float or None
        """
        return self.__accuracy

    @property
    def is_trained(self):
        """whether the model has been trained or not

        :return: whether the model has been trained or not
        :rtype: boolean
        """
        return self.__is_trained

    def fit(self, X_train, y_train, X_test, y_test):
        """fit the model and record accuracy from test set."""

        if self.model is not None:
            self.model.fit(X_train, y_train)
            y_pred = self.model.predict(X_test)
            self.__accuracy = accuracy_score(y_test, y_pred)
            self.__is_trained = True

    def predict(self, X):
        """predict with the model

        :param X: set to predict on
        :type X: numpy array of form (num_samples, num_features)
        :return: predictions
        :rtype: numpy.array or None if model is not trained
        """

        if self.is_trained:
            return self.model.predict(X)


class SVMModel(MnistModel):
    """class for the SVM model """

    def __init__(self):
        """constructor
        """
        super().__init__(SVC())

    def __str__(self):
        """string representation
        """
        return "SVMModel(is_trained={})".format(self.is_trained)


class LogisticModel(MnistModel):
    """class for logistic regression model  """

    def __init__(self):
        """constructor
        """
        super().__init__(LogisticRegression(max_iter=1000))

    def __str__(self):
        """string representation
        """
        return "LogisticModel(is_trained={})".format(self.is_trained)
