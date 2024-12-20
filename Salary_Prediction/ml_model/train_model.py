import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

# Simulated data (replace with your actual dataset)
data = {
    'YearsExperience': [1, 2, 3, 4, 5, 6, 7, 8],
    'EducationLevel': ['High School', "Bachelor's", "Master's", 'PhD', 'High School', "Bachelor's", "Master's", 'PhD'],
    'Salary': [40000, 45000, 50000, 60000, 55000, 60000, 65000, 70000]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Encode categorical 'EducationLevel' column
le = LabelEncoder()
df['EducationLevel'] = le.fit_transform(df['EducationLevel'])

# Split the dataset into features and target
X = df[['YearsExperience', 'EducationLevel']]  # Features: 'YearsExperience' and 'EducationLevel'
y = df['Salary']  # Target: 'Salary'

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the model using pickle
with open('salary_model.pkl', 'wb') as file:
    pickle.dump(model, file)

with open('label_encoder.pkl', 'wb') as file:
    pickle.dump(le, file)


print("Model and Label Encoder trained and saved as 'salary_model.pkl' and 'label_encoder.pkl'")
