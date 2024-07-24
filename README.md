# RookiePredictions

## Introduction
Welcome to the Rookie Predictions Project! This project aims to build a predictive model that effectively predicts the success of offensive NFL rookie players for the upcoming season based on their college performance and other relevant data. The core of this project is implemented in a Jupyter Notebook.

## Technologies
- **Programming Language:** Python 3
- **Libraries and Frameworks:** Pandas, NumPy, Seaborn, Matplotlib, Scikit-Learn, XGBoost, AWS SageMaker
- **Environment:** Jupyter Notebook

## Dataset
The dataset used in this project includes historical performance data of NFL rookies, their college performance metrics, and other relevant features. The data was collected from various sources and compiled for this project.

### Data Collection Files
- `college_passing_unclean.py`: Scrapes college passing data from sports-reference.com and saves it to `college_passing_unclean.csv`.
- `college_receiving_unclean.py`: Scrapes college receiving data from sports-reference.com and saves it to `college_receiving_unclean.csv`.
- `college_rushing_unclean.py`: Scrapes college rushing data from sports-reference.com and saves it to `college_rushing_unclean.csv`.
- `nfl_passing_unclean.py`: Scrapes NFL passing data from sports-reference.com and saves it to `nfl_passing_unclean.csv`.
- `nfl_receiving_unclean.py`: Scrapes NFL receiving data from sports-reference.com and saves it to `nfl_receiving_unclean.csv`.
- `nfl_rushing_unclean.py`: Scrapes NFL rushing data from sports-reference.com and saves it to `nfl_rushing_unclean.csv`.

### Data Storage
- `bucket.py`: Uploads the collected CSV files to an S3 bucket on AWS.
  ```python
  import boto3

  # Initialize S3 client
  s3 = boto3.client('s3')

  bucket_name = 'rookieprojectbucket'

  # Upload files to S3 with prefixes
  s3.upload_file('combine.csv', bucket_name, 'raw/combine.csv')
  s3.upload_file('combine.csv', bucket_name, 'backups/combine.csv')

  s3.upload_file('college_passing_unclean.csv', bucket_name, 'raw/college_passing_unclean.csv')
  s3.upload_file('college_passing_unclean.csv', bucket_name, 'backups/college_passing_unclean.csv')

  s3.upload_file('nfl_passing_unclean.csv', bucket_name, 'raw/nfl_passing_unclean.csv')
  s3.upload_file('nfl_passing_unclean.csv', bucket_name, 'backups/nfl_passing_unclean.csv')

  s3.upload_file('nfl_rushing_unclean.csv', bucket_name, 'raw/nfl_rushing_unclean.csv')
  s3.upload_file('nfl_rushing_unclean.csv', bucket_name, 'backups/nfl_rushing_unclean.csv')

  s3.upload_file('nfl_receiving_unclean.csv', bucket_name, 'raw/nfl_receiving_unclean.csv')
  s3.upload_file('nfl_receiving_unclean.csv', bucket_name, 'backups/nfl_receiving_unclean.csv')

  s3.upload_file('college_rushing_unclean.csv', bucket_name, 'raw/college_rushing_unclean.csv')
  s3.upload_file('college_rushing_unclean.csv', bucket_name, 'backups/college_rushing_unclean.csv')

  s3.upload_file('college_receiving_unclean.csv', bucket_name, 'raw/college_receiving_unclean.csv')
  s3.upload_file('college_receiving_unclean.csv', bucket_name, 'backups/college_receiving_unclean.csv')
  ```

### Database
- `db.py`: Uploads cleaned datasets to an AWS RDS PostgreSQL database.
  ```python
  import os
  import pandas as pd
  from sqlalchemy import create_engine

  # Retrieve database connection details from environment variables
  db_type = 'postgresql'
  username = os.getenv('DB_USERNAME')
  password = os.getenv('DB_PASSWORD')
  host = os.getenv('DB_HOST')
  port = os.getenv('DB_PORT')
  database = os.getenv('DB_NAME')

  # Create the SQLAlchemy engine
  engine = create_engine(f'{db_type}://{username}:{password}@{host}:{port}/{database}')

  # Load your cleaned datasets
  df1 = pd.read_csv('qb.csv')
  df2 = pd.read_csv('rb.csv')
  df3 = pd.read_csv('wrte.csv')

  # Upload the DataFrame to AWS RDS
  df1.to_sql('qb', con=engine, if_exists='replace', index=False)
  df2.to_sql('rb', con=engine, if_exists='replace', index=False)
  df3.to_sql('wrte', con=engine, if_exists='replace', index=False)

  print("DataFrames successfully uploaded to AWS RDS")
  ```

### Data Cleaning Notebooks
- `DataCleaningQB.ipynb`: Processes and cleans the quarterback (QB) data and outputs `qb.csv`.
- `DataCleaningRB.ipynb`: Processes and cleans the running back (RB) data and outputs `rb.csv`.
- `DataCleaningWRTE.ipynb`: Processes and cleans the wide receiver/tight end (WR/TE) data and outputs `wrte.csv`.

### Exploratory Data Analysis (EDA) Notebooks
- `QB_EDA.ipynb`: Exploratory data analysis for quarterbacks.
- `RB_EDA.ipynb`: Exploratory data analysis for running backs.
- `WRTE_EDA.ipynb`: Exploratory data analysis for wide receivers/tight ends.

### Modeling Notebooks
- `QB_Modeling.ipynb`: Builds and evaluates models for predicting QB success using Random Forest Regressor.
- `RB_Modeling.ipynb`: Builds and evaluates models for predicting RB success using Random Forest Regressor.
- `WRTE_Modeling.ipynb`: Builds and evaluates models for predicting WR/TE success using Random Forest Regressor.

### Prediction Scripts
- `qb_pred.py`: Uses the trained model to make predictions for quarterbacks based on input features.
- `rb_pred.py`: Uses the trained model to make predictions for running backs based on input features.
- `wrte_pred.py`: Uses the trained model to make predictions for wide receivers/tight ends based on input features.

## Installation
To run this project, follow these steps:

1. Ensure that Python 3 and Jupyter Notebook are installed on your machine.
2. Clone this repository:
   ```bash
   git clone https://github.com/alfredh2/RookiePredictions.git
   ```
3. Navigate to the cloned repository.
4. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Notebook
1. Open a terminal and navigate to the project directory.
2. Start Jupyter Notebook:
   ```bash
   jupyter notebook
   ```
3. Open the desired notebook (e.g., `QB_Modeling.ipynb`).
4. Run the cells in the notebook to see the analysis and model predictions.

## Results
The notebooks include detailed analyses of model performance and accuracy metrics. We evaluate the models' predictions and discuss the best-performing model for each position. To read about my experience working on this project, visit my Medium article on it: https://medium.com/@alfredpmhofmann/project-rookie-predictions-predicting-nfl-rookie-success-701608844450
