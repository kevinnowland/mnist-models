""" module to test models module  """

import context
context.init()

import mnist_models.models as mo
import mnist_models.data as da
from sklearn.dummy import DummyClassifier


X_train_, y_train_ = da.train_data([0, 1])
X_test_, y_test_ = da.test_data([0, 1])

X_train = X_train_[:40]
y_train = y_train_[:40]
X_test = X_test_[:10]
y_test = y_test_[:10]


def test_base_class():
    """ test the base class works """

    model = mo.MnistModel(DummyClassifier())

    assert model.accuracy is None, "accuracy not None"
    assert not model.is_trained, "model claims it is trained before training"

    model.fit(X_train, y_train, X_test, y_test)

    assert model.accuracy is not None, "accuracy none after fitting"
    assert model.is_trained, "model claims it is not trained after training"

    X_test_ = X_test[:2]
    y_pred = model.predict(X_test_)

    assert y_pred.shape[0] == X_test_.shape[0], "prediction shape not matching"


def test_svm():

    model = mo.SVMModel()
    model.fit(X_train, y_train, X_test, y_test)
    y_pred = model.predict(X_test)

    assert y_pred.shape[0] == X_test.shape[0], "prediction shape not matching"


def test_logistic():

    model = mo.LogisticModel()
    model.fit(X_train, y_train, X_test, y_test)
    y_pred = model.predict(X_test)

    assert y_pred.shape[0] == X_test.shape[0], "prediction shape not matching"
