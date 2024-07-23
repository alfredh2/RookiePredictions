import joblib
import pandas as pd

# Load your models
models = [joblib.load(f'rb_model_{i}.joblib') for i in range(5)]

# Define the feature names (ensure they match the training data)
feature_names = ['Age', 'G', 'Att_R', 'Yds_R', 'TD_R', 'Rec', 'Yds', 'TD', 'Conf',
       'Height', 'Weight', '40yd', 'Vertical', 'Broad Jump', 'Drafted',
       'OvrPick']

def predict_metrics(features):
    """
    Predicts the 7 metrics based on input features.

    Parameters:
    features (list): A list of feature values [feature1, feature2, ..., featureN]

    Returns:
    dict: A dictionary containing the predictions for each metric
    """
    metrics = ['Rushing Yards', 'Rushing Touchdowns', 'Receptions', 'Receiving Yards', 'Receiving Touchdowns']
    predictions = {}
    
    # Create a DataFrame from the input features
    input_data = pd.DataFrame([features], columns=feature_names)
    
    for i, model in enumerate(models):
        predictions[metrics[i]] = model.predict(input_data)[0]

    return predictions

'''
List in this order, reference columns.txt:
['Age', 'G', 'Att_R', 'Yds_R', 'TD_R', 'Rec', 'Yds', 'TD', 'Conf',
'Height', 'Weight', '40yd', 'Vertical', 'Broad Jump', 'Drafted',
'OvrPick']
'''

features = [21, 11, 187, 1139, 10, 21, 254, 2, 'SEC', 76, 210, 4.35, 36, 115, 1, 21]  # Replace with your feature values
predictions = predict_metrics(features)
print(predictions)
