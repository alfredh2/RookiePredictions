import joblib
import pandas as pd

# Load your models
models = [joblib.load(f'model_{i}.joblib') for i in range(7)]

# Define the feature names (ensure they match the training data)
feature_names = ['Age', 'G', 'Pct', 'Yds', 'Y/A', 'AY/A', 'TD', 'Int', 'Rate', 'Att_R',
                 'Yds_R', 'Avg_R', 'TD_R', 'Conf', 'Height', 'Weight', '40yd',
                 'Vertical', 'Broad Jump', '3Cone', 'Shuttle', 'Drafted', 'OvrPick']

def predict_metrics(features):
    """
    Predicts the 7 metrics based on input features.

    Parameters:
    features (list): A list of feature values [feature1, feature2, ..., featureN]

    Returns:
    dict: A dictionary containing the predictions for each metric
    """
    metrics = ['Passing Yards', 'Passing Touchdowns', 'QBR', 'Passer Rating', 'Completion Percentage', 'Rushing Yards', 'Rushing Touchdowns']
    predictions = {}
    
    # Create a DataFrame from the input features
    input_data = pd.DataFrame([features], columns=feature_names)
    
    for i, model in enumerate(models):
        predictions[metrics[i]] = model.predict(input_data)[0]

    return predictions

'''
List in this order, reference columns.txt:
['Age', 'G', 'Pct', 'Yds', 'Y/A', 'AY/A', 'TD', 'Int', 'Rate', 'Att_R',
'Yds_R', 'Avg_R', 'TD_R', 'Conf', 'Height', 'Weight', '40yd',
'Vertical', 'Broad Jump', '3Cone', 'Shuttle', 'Drafted', 'OvrPick']
'''

features = [23, 12, 72.2, 3812, 11.7, 13.6, 40, 4, 208.0, 135, 1334, 8.4, 10, 'SEC', 76, 210, 4.35, 36, 115, 7.2, 4.39, 1, 3]  # Replace with your feature values
predictions = predict_metrics(features)
print(predictions)
