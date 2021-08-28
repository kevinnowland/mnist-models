""" module to interface with the mnist data """

import mnist
import numpy as np


def _get_data(train_or_test, digits):
    """ helper function called by train_data() and test_data() """

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


def train_data(digits=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
    """ returns train data """
    return _get_data('train', digits)


def test_data(digits=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
    """ returns test data  """
    return _get_data('test', digits)
