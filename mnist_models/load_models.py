""" module to handle loading of the pretrained models """

import pickle
import os
import sys

sys.path.append(os.path.dirname(__file__))


def _load_model(name):

    path = os.path.dirname(__file__)
    model_path = path + '/pretrained_models/'

    with open(model_path + name, 'rb') as f:
        model = pickle.load(f)

    return model


def load_full_logistic():

    return _load_model("logistic_full.pkl")


def load_zero_one_logistic():

    return _load_model("logistic_zero_one.pkl")


def load_full_svm():

    return _load_model("svm_full.pkl")


def load_zero_one_svm():

    return _load_model("svm_zero_one.pkl")
