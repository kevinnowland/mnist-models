import os
import sys

path = os.path.join(os.path.dirname(__file__), '..')
abspath = os.path.abspath(path)
sys.path.insert(0, abspath)

from mnist_models.data import train_data, test_data
from mnist_models.models import SVMModel, LogisticModel
import pickle


# train full models
X_train, y_train = train_data()
X_test, y_test = test_data()

print("training logistic model")
lm = LogisticModel()
lm.fit(X_train, y_train, X_test, y_test)

print("training SVM")
svm = SVMModel()
svm.fit(X_train, y_train, X_test, y_test)

# save full models
model_dir_path = "../mnist_models/pretrained_models/"

with open(model_dir_path + "logistic_full.pkl", "wb") as f:
    pickle.dump(lm, f)

with open(model_dir_path + "svm_full.pkl", "wb") as f:
    pickle.dump(svm, f)


# train 0-1 models
X_train, y_train = train_data([0, 1])
X_test, y_test = test_data([0, 1])

print("training 0-1 logistic")
lm = LogisticModel()
lm.fit(X_train, y_train, X_test, y_test)

print("training 0-1 SVM")
svm = SVMModel()
svm.fit(X_train, y_train, X_test, y_test)

# save 0-1 models
model_dir_path = "../mnist_models/pretrained_models/"

with open(model_dir_path + "logistic_zero_one.pkl", "wb") as f:
    pickle.dump(lm, f)

with open(model_dir_path + "svm_zero_one.pkl", "wb") as f:
    pickle.dump(svm, f)
