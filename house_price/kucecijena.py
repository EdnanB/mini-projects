import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


train_data = pd.read_csv("train.csv")
test_data = pd.read_csv("test.csv")

print(train_data.dtypes)


numerical_columns = train_data.select_dtypes(include=['float64', 'int64']).columns
train_data[numerical_columns] = train_data[numerical_columns].fillna(train_data[numerical_columns].mean())


features = ['LotArea', 'OverallQual', 'YearBuilt']
X = train_data[features]
y = train_data['SalePrice']


X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)


model = LinearRegression()
model.fit(X_train, y_train)


X_test = test_data[features]
predictions = model.predict(X_test)


predictions_df = pd.DataFrame({'Predictions': predictions})


predictions_df.to_csv('predictions.csv', index=False)
