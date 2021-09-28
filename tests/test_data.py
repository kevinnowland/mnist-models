""" module for testing the data module  """

import mnist_models.data as da


def test_get_data():
    """ test the get_data function """

    X, y = da._get_data('test', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    assert len(X.shape) == 2, "length not correct"
    assert X.shape[0] == y.shape[0], "data and labels have different lengths"

    X_zero_one, y_zero_one = da._get_data('test', [0, 1])

    assert X_zero_one.shape[0] == y_zero_one.shape[0], \
        "data and labels of 0-1 data have different lengths"
    assert X_zero_one.shape[0] < X.shape[0], \
        "0-1 data has length >= full data"
    assert 0 in y_zero_one, "0 missing"
    assert 1 in y_zero_one, "1 missing"
    assert 2 not in y_zero_one, "2 unexpectedly present"
    assert 3 not in y_zero_one, "3 unexpectedly present"
    assert 4 not in y_zero_one, "4 unexpectedly present"
    assert 5 not in y_zero_one, "5 unexpectedly present"
    assert 6 not in y_zero_one, "6 unexpectedly present"
    assert 7 not in y_zero_one, "7 unexpectedly present"
    assert 8 not in y_zero_one, "8 unexpectedly present"
    assert 9 not in y_zero_one, "9 unexpectedly present"


def test_train_test_data():

    X_train, y_train = da.train_data()
    X_test, y_test = da.test_data()

    X_train_zero, y_train_zero = da.train_data([0, 1])
    X_test_zero, y_test_zero = da.test_data([0, 1])

    assert X_train_zero.shape[0] < X_train.shape[0], \
        "0-1 train_data longer than full train data"
    assert X_test.shape[0] < X_train.shape[0], \
        "more sampels in test than train data"
