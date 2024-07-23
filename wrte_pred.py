import joblib
import pandas as pd

# Load your models
models = [joblib.load(f'wrte_model_{i}.joblib') for i in range(3)]

# Define the feature names (ensure they match the training data)
feature_names = ['Age', 'G', 'Rec', 'Yds', 'TD', 'Conf', 'Height', 'Weight', '40yd',
       'Vertical', 'Broad Jump', 'Drafted', 'OvrPick']

def predict_metrics(features):
    """
    Predicts the 7 metrics based on input features.

    Parameters:
    features (list): A list of feature values [feature1, feature2, ..., featureN]

    Returns:
    dict: A dictionary containing the predictions for each metric
    """
    metrics = ['Receptions', 'Receiving Yards', 'Receiving Touchdowns']
    predictions = {}
    
    # Create a DataFrame from the input features
    input_data = pd.DataFrame([features], columns=feature_names)
    
    for i, model in enumerate(models):
        predictions[metrics[i]] = model.predict(input_data)[0]

    return predictions

'''
List in this order, reference columns.txt:
['Age', 'G', 'Rec', 'Yds', 'TD', 'Conf', 'Height', 'Weight', '40yd',
'Vertical', 'Broad Jump', 'Drafted', 'OvrPick']
'''

features = [21, 12, 67, 1211, 14, 'Big Ten', 76, 209, 4.46, 30.60, 128, 1, 4]  # Replace with your feature values
predictions = predict_metrics(features)
print(predictions)
