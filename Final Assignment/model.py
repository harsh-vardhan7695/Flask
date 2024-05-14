import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
import category_encoders as ce
from sklearn.metrics import r2_score
from sklearn.preprocessing import MinMaxScaler

data = pd.read_csv('House_Rent_Dataset.csv')

data=data.drop(columns="Posted On")

X = data.drop(columns = "Rent")
y = data['Rent']
encoder = ce.LeaveOneOutEncoder(return_df=True)
X=encoder.fit_transform(X,y)

scaler = MinMaxScaler()
for col in X.columns[:-1]:
    scaler.fit(X[[col]])
    X[col] = scaler.transform (X[[col]])

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
model = LinearRegression()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)
r2 = r2_score(y_test,y_pred)

# Save the trained model to a pickle file
with open('house_rent_model.pkl', 'wb') as f:
    pickle.dump(model, f)