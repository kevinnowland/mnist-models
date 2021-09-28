""" module for testing the data module  """

import mnist_models.load_models as lm


def test_hello_world():
    pass


def test_load_logistic():

    try:
        full_model = lm.load_full_logistic()
        assert full_model.is_trained, "full logistic model is not trained"
    except ModuleNotFoundError:
        raise

    try:
        zero_one_model = lm.load_zero_one_logistic()
        assert zero_one_model.is_trained, "zero one logistic model is not trained"
    except ModuleNotFoundError:
        raise


def test_load_svm():

    try:
        full_model = lm.load_full_svm()
        assert full_model.is_trained, "full svm model is not trained"
    except ModuleNotFoundError:
        raise

    try:
        zero_one_model = lm.load_zero_one_svm()
        assert zero_one_model.is_trained, "zero one svm model is not trained"
    except ModuleNotFoundError:
        raise
