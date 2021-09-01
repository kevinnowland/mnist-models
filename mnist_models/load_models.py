"""module to handle loading of the pretrained models.
"""

import pickle
import os
import sys

sys.path.append(os.path.dirname(__file__))


def _load_model(name):
    """helper function to load pickled model files

    :param name: name of the model to load, must be one of
        `logistic_full`, `logistic_zero_one`, `svm_full`, `svm_zero_one`
    :type name: str
    :return: unpickled MNIST model
    :rtype: MnistModel
    """

    path = os.path.dirname(__file__)
    model_path = path + '/pretrained_models/'

    with open(model_path + name, 'rb') as f:
        model = pickle.load(f)

    return model


def load_full_logistic():
    """load in the logistic model trained on all digits

    :return: logistic regression model
    :rtype: LogisticModel
    """

    return _load_model("logistic_full.pkl")


def load_zero_one_logistic():
    """load in the logistic model trained on only zeros and ones

    :return: logistic regression model
    :rtype: LogisticModel
    """

    return _load_model("logistic_zero_one.pkl")


def load_full_svm():
    """load in the SVM model trained on all digits

    :return: SVM classification model
    :rtype: SVMModel
    """

    return _load_model("svm_full.pkl")


def load_zero_one_svm():
    """load in the SVM model trained on only zeros and ones

    :return: SVM classification model
    :rtype: SVMModel
    """

    return _load_model("svm_zero_one.pkl")
