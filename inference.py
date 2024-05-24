import pickle
import pandas as pd
import sqlite3
import sys

def load_model(model_path):
    """
    Load the trained model from a file.

    Parameters
    ----------
    model_path : TYPE
        DESCRIPTION.

    Returns
    -------
    model : TYPE
        DESCRIPTION.

    """

    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model

def classification(model, input_file):
    """
    Classify samples using the loaded model.

    Parameters
    ----------
    model : TYPE
        DESCRIPTION.
    input_file : TYPE
        DESCRIPTION.

    Returns
    -------
    ids : TYPE
        DESCRIPTION.
    predictions : TYPE
        DESCRIPTION.

    """
    data = pd.read_csv(input_file)
    ids = data['id']
    features = data.drop(columns=['id'])
    predictions = model.predict(features)
    return ids, predictions

def save_to_db(ids, predictions, db_path):
    """
    Save the classification results to an SQLite database.

    Parameters
    ----------
    ids : TYPE
        DESCRIPTION.
    predictions : TYPE
        DESCRIPTION.
    db_path : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS water_potability
                      (id INTEGER PRIMARY KEY, class INTEGER)''')
    for id_, pred in zip(ids, predictions):
        cursor.execute('''INSERT INTO water_potability (id, class)
                          VALUES (?, ?)''', (id_, pred))
    conn.commit()
    conn.close()

if __name__ == '_main_':
    if len(sys.argv) != 4:
        print("Usage: python classify_samples.py <model_path> <scaler> <input_file>")
        sys.exit(1)

    model_path = sys.argv[1]
    scaler_path = sys.argv[2]
    input_file = sys.argv[2]
    db_name = 'ds_pro'

    # Load the model
    model = load_model(model_path)

    # Classify the samples
    ids, predictions = classification(model, scaler_path, input_file)

    # Save the results to the database
    save_to_db(ids, predictions, db_name)

    print("Classification completed and results saved to the database.")
