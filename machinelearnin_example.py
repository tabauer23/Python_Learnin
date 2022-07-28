
#Pandas for data analysis
import pandas as pd

#Sklearn for modeling
from sklearn.tree import DecisionTreeClassifier
from sklearn.externals import joblib
=======

>>>>>>> 31db6185e2a2690babf134a92575561d129b68bc
#Import data
music_data = pd.read_csv('music.csv')

#Set X to the data, minus the genre (since we want to predict this)
X = music_data.drop(columns=['genre'])

#Set y to the dependent variable
y = music_data['genre']

<<<<<<< HEAD
#Create a test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

#Create the model 
model = DecisionTreeClassifier()
#fit the model
model.fit(X_train,y_train)

#make a couple hardcoded predictions.
predictions = model.predict(X_test)


#general rule of thumb ~70-80% of the data for training, and the rest for testing.

#Create two sets of data for testing and training.

score = accuracy_score(y_test, predictions)
score
=======
#Create the model 
model = DecisionTreeClassifier()
#fit the model
model.fit(X,y)

#make a couple hardcoded predictions.
model.predict([[21,1], [22,0]])


>>>>>>> 31db6185e2a2690babf134a92575561d129b68bc
