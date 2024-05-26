import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
import os

# Ensure the models directory exists
os.makedirs('models', exist_ok=True)

# Sample data for demonstration
data = pd.DataFrame({
    'extraversion_1': [5, 3, 4, 2, 5, 3, 4, 2, 1, 5],
    'extraversion_2': [4, 2, 3, 3, 5, 3, 4, 2, 1, 4],
    'extraversion_3': [3, 4, 5, 2, 4, 3, 4, 2, 1, 4],
    'agreeableness_1': [4, 5, 3, 4, 2, 4, 5, 3, 2, 3],
    'agreeableness_2': [3, 4, 5, 4, 2, 3, 5, 3, 2, 3],
    'agreeableness_3': [4, 5, 3, 4, 3, 3, 5, 3, 2, 3],
    'conscientiousness_1': [5, 3, 5, 4, 3, 2, 1, 4, 5, 4],
    'conscientiousness_2': [4, 5, 3, 4, 3, 4, 2, 5, 5, 4],
    'conscientiousness_3': [3, 4, 5, 4, 3, 2, 1, 4, 5, 4],
    'neuroticism_1': [2, 1, 2, 3, 4, 5, 3, 4, 3, 2],
    'neuroticism_2': [3, 2, 3, 2, 4, 5, 3, 4, 3, 2],
    'neuroticism_3': [2, 1, 2, 3, 4, 5, 3, 4, 3, 2],
    'openness_1': [4, 3, 2, 5, 4, 1, 2, 5, 4, 1],
    'openness_2': [5, 4, 3, 5, 4, 1, 2, 5, 4, 1],
    'openness_3': [4, 3, 2, 5, 4, 1, 2, 5, 4, 1],
    'trait_score': [80, 75, 85, 70, 65, 55, 60, 78, 68, 72]
})

# Prepare features and target variable
X = data.drop('trait_score', axis=1)
y = data['trait_score']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the model to a file
MODEL_PATH = 'models/personality_model.pkl'
with open(MODEL_PATH, 'wb') as f:
    pickle.dump(model, f)
