import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle

data = pd.read_csv("student-mat.csv", sep=";")

data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]

predict = "G3"

X = np.array(data.drop([predict], axis=1))
y = np.array(data[predict])

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size = 0.1)

linear = linear_model.LinearRegression()

linear.fit(x_train, y_train)
acc = linear.score(x_test, y_test)
print("Accuracy => ",acc)

print('Coefficient: \n', linear.coef_)
print('Intercept: \n', linear.intercept_)

predictions = linear.predict(x_test)
print("")
print("Predictions    |    X_test        |    Y_Test")
for x in range(len(predictions)):
    print(predictions[x], x_test[x], y_test[x])





"""
Output:

Accuracy =>  0.7784638497923726
Coefficient: 
 [ 0.15376169  0.98377844 -0.19966673 -0.29971716  0.03524388]
Intercept: 
 -1.5242400342188986

Predictions    |    X_test        |    Y_Test
8.301501458493377 [8 9 2 0 4] 10
6.890517768254666 [10  8  1  3  3] 7
12.20852577291098 [12 12  1  0  8] 12
14.98576670746834 [14 15  2  0  0] 15
7.836709668745266 [10  8  2  0 10] 8
6.192969075116317 [8 7 2 0 0] 8
8.409358105427264 [10  9  3  0  4] 9
15.669176209996486 [16 15  1  0  5] 16
8.338870350078391 [10  9  3  0  2] 10
14.43770098279664 [15 14  2  0  8] 14
3.782306107913522 [ 6  5  1  3 16] 5
9.592803275377957 [10 10  2  0  4] 10
10.050973685145632 [10 10  2  0 17] 10
15.210016153089676 [15 15  2  0  2] 14
8.820488105084921 [10  9  2  0 10] 10
7.708520337622236 [11  8  2  0  2] 8
9.728798823585716 [11 10  2  1 12] 10
10.789034624903366 [11 11  1  0  0] 10
8.314287638068093 [9 9 2 0 0] 10
14.296725472098894 [15 14  2  0  4] 14
4.1293520879387 [6 5 2 0 6] 6
7.176747511455973 [8 8 2 0 0] 0
4.0588643325898275 [6 5 2 0 4] 6
10.589367891292328 [11 11  2  0  0] 10
7.176747511455973 [8 8 2 0 0] 9
8.006764257523166 [7 9 2 0 0] 8
17.601489205001364 [16 17  1  0  4] 18
13.159185345486776 [14 13  2  0  4] 13
10.38876098087501 [13 10  2  1 22] 11
5.580748568621214 [7 7 2 2 4] 9
16.34755627970179 [16 16  2  0  2] 17
7.030792038268244 [9 8 2 1 0] 0
12.710686454244103 [12 13  2  0  0] 14
7.445912353276748 [ 7  8  2  0 12] 8
15.210016153089676 [15 15  2  0  2] 16
14.272142760088595 [14 14  1  0  2] 14
-1.8542498068482027 [5 0 1 3 0] 0
5.8395406512328165 [7 7 3 0 0] 8
9.052494297458134 [10 10  4  0  0] 10
11.726908017904448 [12 12  2  0  0] 11
"""
