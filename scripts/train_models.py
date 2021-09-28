import mnist_models.data as da
import mnist_models.models as mo
import pickle


# train full models
X_train, y_train = da.train_data()
X_test, y_test = da.test_data()


print("training logistic model")
lm = mo.LogisticModel()
lm.fit(X_train, y_train, X_test, y_test)

print("training SVM")
svm = mo.SVMModel()
svm.fit(X_train, y_train, X_test, y_test)

# save full models
model_dir_path = "../mnist_models/pretrained_models/"

with open(model_dir_path + "logistic_full.pkl", "wb") as f:
    pickle.dump(lm, f)

with open(model_dir_path + "svm_full.pkl", "wb") as f:
    pickle.dump(svm, f)


# train 0-1 models
X_train, y_train = da.train_data([0, 1])
X_test, y_test = da.test_data([0, 1])

print("training 0-1 logistic")
lm = mo.LogisticModel()
lm.fit(X_train, y_train, X_test, y_test)

print("training 0-1 SVM")
svm = mo.SVMModel()
svm.fit(X_train, y_train, X_test, y_test)

# save 0-1 models
with open(model_dir_path + "logistic_zero_one.pkl", "wb") as f:
    pickle.dump(lm, f)

with open(model_dir_path + "svm_zero_one.pkl", "wb") as f:
    pickle.dump(svm, f)
