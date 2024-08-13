### Get the data - Lets use the penguins set as a simple example
import pandas as pd
data = pd.read_csv('penguins.csv')
data

### Clean the data - Do we have any missing values?
data.isnull().sum()

# We do so lets look at them so we can decide how to deal with missing values
data_with_missing = data[data.isna().any(axis=1)]

# drop ones with most of the data missing
data.dropna(thresh=6, inplace=True)
data

# look again
data.isnull().sum()

# create unknown for missing genders
data.fillna({'gender':'unknown'}, inplace=True)
data.isnull().sum()

# Handling categorical data - one hot encoding
data = pd.get_dummies(data, columns=['island', 'gender'], drop_first=True)


### Exploratory data analysis
# Let's get some basic information about the data set
data.info()

# We have 8 features that descrbe the penguin species. 4 are continuous 
# numerical values, 4 are binary integer values. We have one class label, the 
# species of penguin, and it is a categorical value.
summary = data.describe()
summary
# It looks like we dont have any wild outliers in the data.


# Take a look at each feature as a histogram to get an idea about their 
# distribution. We can also plot each variable versus the others to see what 
# kind of relationships they have with each other. This here is called a 
# "pair plot" and encapsulates a lot of information in a concise plot.
import seaborn as sns
sns.pairplot(data.iloc[:,:5], hue='species')


# How about class balance?
grouped = data.groupby('species')
print("Class size:\n", grouped.size())
# It looks like we do not have any significant class imbalance issues.


# Some summary statistics
stats = grouped.mean()
print("\nClass averages:\n", grouped.mean())
# There are some interesting things about the features which add information.


'''How does each feature correlate with the species?
We need to maipulate the data a little here then do the computation.
Here we are encoding the species (text) as a number so we can compute a correlation.
We use Spearman rank correlation since the response variable is categorical.'''
from sklearn.preprocessing import LabelEncoder
enc = LabelEncoder().fit_transform(data.species)
corr_data = data.iloc[:,1:]
corr_data['species'] = enc
corr_matrix = corr_data.corr(method='spearman')
corr_matrix["species"].sort_values(ascending=False)[1:]
# So overall, it looks like there is a lot of information content in the 
# data that can help us create a machine learning model for predicting 
# species from data

# drop gender features
data.drop(['gender_male', 'gender_unknown'], axis=1, inplace=True)
data.columns


# Lets refomat the data so the features are in a separate dataframe from the class labels
# lets first shuffle the data since it is ordered by species in the dat frame

data = data.sample(frac=1).reset_index(drop=True)
X = data.iloc[:,1:]
y = data.species




# splitting the data into train and test sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)



### Model building

# random forest model
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier()

clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

from sklearn.metrics import accuracy_score
accuracy_score(y_test, y_pred)


# k-fold cross validation
from sklearn.model_selection import cross_val_score
scores = cross_val_score(clf, X, y, cv=3)
print("Average accuracy: ", scores.mean())
print("Standard deviation: ", scores.std())



# train final model on all the data
final_model = RandomForestClassifier()
final_model.fit(X, y)

## predicting unknowns with our model
#	bill_length,	bill_depth, flipper_length, body_mass, island_Dream, island_Torgersen
import numpy as np
unknown = np.array([45.5, 13.7, 214, 4650, 0, 0])
result = final_model.predict(unknown.reshape(1, -1))
print(result)



# appendix

# demo of one-hot encoding
categorical = pd.DataFrame({'Category': ["A", "B", "A", "B"]})
categorical
pd.get_dummies(categorical, columns=['Category'], drop_first=True)


