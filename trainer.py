import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import joblib

data = pd.read_csv('myPreprocessed.csv')

venue_encoder = LabelEncoder()
team_encoder = LabelEncoder()

data['venue'] = venue_encoder.fit_transform(data['venue'])
data['batting_team'] = team_encoder.fit_transform(data['batting_team'])
data['bowling_team'] = team_encoder.fit_transform(data('bowling_team'))


anArray = data.to_numpy()

X,y = anArray[:,:3],anArray[:, 3]

X = np.concatenate((np.eye(42)[anArray[:, 0]],
                    np.eye(2)[anArray[:, 1] -1],
                   np.eye(15)[anArray[:, 2]],
                   np.eye(15)[anArray[:,3]],
                   ),axis = 1)

X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.25)

LinearRegressor = LinearRegression()

LinearRegressor.fit(X_train, y_train)


joblib.dump(LinearRegressor, 'regressor_model.joblib')
joblib.dump(venue_encoder, 'venue_encoder.joblib')
joblib.dump(team_encoder, 'team_encoder.joblib')

print(LinearRegression.score(X_test, y_test))
