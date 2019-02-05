import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

from sklearn.preprocessing import normalize
import pickle
#hidden_layers = [(100,100,100),(400,200),(1000,500),(200,500),(450,234,567),(450,213,123),(123,432,234),(200,500)]
hidden_layers = [(100,100,100)]
results = []
# X = np.load("X_otsu.npy")
# y = np.load("y_otsu.npy")
X = np.load("X_otsu_50.npy")
y = np.load("y_otsu_50.npy")
models = []
X = X/255.0
fileName = "model_ostu_50"
print("done loading")
print(X.shape,y.shape)
print("split is done")


for i in hidden_layers:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    model = MLPClassifier(hidden_layer_sizes=i, solver='adam',max_iter=500, alpha=0.003, verbose=True,
                          random_state=42,tol=0.000000001)
    print("Learning started: ",i)
    clf = model.fit(X_train,y_train)
    pickle.dump(clf,open(fileName,'wb'))
    y_pred = clf.predict(X_test)
    score = accuracy_score(y_test,y_pred)


    print("DONE: ",score)
    results.append([i,score])

for i in results:
    print(i)
