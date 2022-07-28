#Pandas for data analysis
import pandas as pd

#Sklearn for modeling
from sklearn.tree import DecisionTreeClassifier
import joblib

#Import data
music_data = pd.read_csv('music.csv')
X = music_data.drop(columns=['genre'])
y = music_data['genre']

#Create a test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

#Create the model 
model = DecisionTreeClassifier()
model.fit(X.values,y.values)

# model = joblib.dump(model, 'music-recommender.joblib')
# model = joblib.load('music-recommender.joblib')
#fit the model
#model.fit(X_train,y_train)

#make a hardcoded prediction, 21 year old male.. should like "Hip-Hop", check that array states this.
predictions = model.predict([[21,1]])


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


#This was updated from my laptop instead of desktop.
# Attempt new branch.
