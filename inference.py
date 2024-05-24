#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 19:06:27 2024

@author: johnomole
"""

import pickle
import pandas as pd
import sqlite3
import sys


def load_model(model_path):
    """
    Load the trained model from a file.

    Parameters
    ----------
    model_path : str
        Path to the trained model file.

    Returns
    -------
    model : object
        Loaded model object.
    """
    with open(model_path, "rb") as file:
        model = pickle.load(file)
    return model


def load_scaler(scaler_path):
    """
    Load the scaler from a file.

    Parameters
    ----------
    scaler_path : str
        Path to the scaler file.

    Returns
    -------
    scaler : object
        Loaded scaler object.
    """
    with open(scaler_path, "rb") as file:
        scaler = pickle.load(file)
    return scaler


def classification(model, scaler, input_file):
    """
    Classify samples using the loaded model.

    Parameters
    ----------
    model : object
        Loaded model object.
    scaler : object
        Loaded scaler object.
    input_file : str
        Path to the input CSV file.

    Returns
    -------
    ids : pandas.Series
        IDs from the input data.
    predictions : pandas.Series
        Predicted classes for the input data.
    """
    data = pd.read_csv(input_file)
    ids = data["id"]
    features = data.drop(columns=["id"])
    scaled_features = scaler.transform(features)
    predictions = model.predict(scaled_features)
    return ids, predictions


def save_to_db(ids, predictions, db_path):
    """
    Save the classification results to an SQLite database.

    Parameters
    ----------
    ids : pandas.Series
        IDs for the classification results.
    predictions : pandas.Series
        Predicted classes.
    db_path : str
        Path to the SQLite database file.

    Returns
    -------
    None
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS water_potability
                      (id INTEGER PRIMARY KEY, class INTEGER)"""
    )
    for id_, pred in zip(ids, predictions):
        cursor.execute(
            """INSERT INTO water_potability (id, class)
                          VALUES (?, ?)""",
            (id_, int(pred)),
        )  # Ensure prediction is cast to integer
    conn.commit()
    conn.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python inference.py <model_path> <scaler_path> <input_file>")
        sys.exit(1)

    model_path = sys.argv[1]
    scaler_path = sys.argv[2]
    input_file = sys.argv[3]
    db_name = "ds_pro.db"

    # Load the model
    model = load_model(model_path)

    # Load the scaler
    scaler = load_scaler(scaler_path)

    # Classify the samples
    ids, predictions = classification(model, scaler, input_file)

    # Save the results to the database
    save_to_db(ids, predictions, db_name)

    print(
        "Classification of the water potability completed and results saved to the database."
    )
