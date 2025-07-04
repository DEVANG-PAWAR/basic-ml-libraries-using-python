from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix

X = [
    [150, 50],
    [160, 60],
    [170, 65],
    [180, 80]
]

y = [0, 0, 1, 1]

model = DecisionTreeClassifier()
model.fit(X, y)

y_pred = model.predict(X)

cm = confusion_matrix(y, y_pred)
print("Confusion Matrix:")
print(cm)