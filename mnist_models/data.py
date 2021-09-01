"""module to interface with the mnist data. In particular, we flatten
the data into numpy arrays of the form (num_samples, num_features) and
scale the features to be between 0 and 1.
"""

import mnist
import numpy as np
from typing import List


def _get_data(train_or_test: str, digits: List[int]) -> np.array:
    """helper function called by train_data() and test_data()

    :param train_or_test: whether to pull training or test data, must be 'train' or 'test'
    :type train_or_test: str
    :param digits: list of digits to include
    :type digits: list[int]
    :return: numpy array of shape (num_samples, num_features)
    :rtype: numpy.array
    """

    if train_or_test == 'train':
        images_ = mnist.train_images()
        labels_ = mnist.train_labels()
    elif train_or_test == 'test':
        images_ = mnist.test_images()
        labels_ = mnist.test_labels()
    else:
        raise Exception("invalid value, must be 'train' or 'test'")

    images = images_[np.isin(labels_, digits)]
    labels = labels_[np.isin(labels_, digits)]

    images_reshaped = images.reshape(images.shape[0],
                                     images.shape[1] * images.shape[2])

    return images_reshaped / 255.0, labels


def train_data(digits: List[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
    """get train data of the specified digis

    :param digits: list of digits to include
    :type digits: list[int]
    :return: numpy array of shape (num_samples, num_features)
    :rtype: numpy.array
    """
    return _get_data('train', digits)


def test_data(digits: List[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
    """get test data of the specified digis

    :param digits: list of digits to include
    :type digits: list[int]
    :return: numpy array of shape (num_samples, num_features)
    :rtype: numpy.array
    """
    return _get_data('test', digits)
