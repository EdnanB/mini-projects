import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


url = 'https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv'
data = pd.read_csv(url)


train_data = pd.read_csv("FuelConsumption (1).csv")
test_data = pd.read_csv("FuelConsumption (1).csv")


features = ['ENGINE SIZE','CYLINDERS','FUEL CONSUMPTION','COEMISSIONS ']
X = train_data[features]
y = train_data['FUEL CONSUMPTION']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = LinearRegression()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')