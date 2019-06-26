from sklearn import tree
from sklearn.model_selection import GridSearchCV
import csv
import random

path = "C:\\Users\\stanc\\OneDrive\\Desktop\\MyData5.csv"
file = open(path, newline='')
reader = csv.reader(file)
header = next(reader)

data = []
dataEvent = []
for row in reader:
    Tp = float(row[2])
    Cl = float(row[3])
    pH = float(row[4])
    Redox = float(row[5])
    Leit = float(row[6])
    Trueb = float(row[7])
    Cl_2 = float(row[8])
    Fm = float(row[9])
    Fm_2 = float(row[10])
    if row[11] == 'FALSE':
        EVENT = 0
    else:
        EVENT = 1
    data.append([Tp, Cl, pH, Redox, Leit, Trueb, Cl_2, Fm, Fm_2])
    dataEvent.append(EVENT)

param_dist = {"max_depth": [3, None],
              "min_samples_split": [2, 3, 4, 5, 6, 7, 8, 9, 10],
              "criterion": ["gini", "entropy"]}

tree = tree.DecisionTreeClassifier()

grid_search = GridSearchCV(estimator=tree,
                           param_grid=param_dist,
                           cv=10)

grid_search = grid_search.fit(data, dataEvent)


print(grid_search.best_params_)