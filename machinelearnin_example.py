
#Pandas for data analysis
import pandas as pd

#Sklearn for modeling
from sklearn.tree import DecisionTreeClassifier

#Import data
music_data = pd.read_csv('music.csv')

#Set X to the data, minus the genre (since we want to predict this)
X = music_data.drop(columns=['genre'])

#Set y to the dependent variable
y = music_data['genre']

#Create the model 
model = DecisionTreeClassifier()
#fit the model
model.fit(X,y)

#make a couple hardcoded predictions.
model.predict([[21,1], [22,0]])


