#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 19:06:27 2024

@author: johnomole
"""

import sqlite3
import pandas as pd
import logging
import sys
from sklearn.metrics import accuracy_score


def load_ground_truth(ground_truth_file):
    """
    Load the ground truth from a CSV file.

    Parameters
    ----------
    ground_truth_file : str
        Path to the CSV file containing the ground truth.

    Returns
    -------
    ground_truth : pandas.DataFrame
        DataFrame containing the ground truth data.
    """
    try:
        ground_truth = pd.read_csv(ground_truth_file)
        return ground_truth
    except FileNotFoundError:
        logging.error("Ground truth file not found: %s", ground_truth_file)
        sys.exit(1)
    except Exception as e:
        logging.error("Error loading ground truth: %s", str(e))
        sys.exit(1)


def get_predictions_from_db(db_path):
    """
    Retrieve the predictions from the SQLite database.

    Parameters
    ----------
    db_path : str
        Path to the SQLite database file.

    Returns
    -------
    predictions : pandas.DataFrame
        DataFrame containing the predictions retrieved from the database.
    """
    try:
        conn = sqlite3.connect(db_path)
        predictions = pd.read_sql_query("SELECT * FROM water_potability", conn)
        return predictions
    except Exception as e:
        logging.error("Error retrieving predictions from database: %s", str(e))
        sys.exit(1)
    finally:
        conn.close()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python test.py <groundtruth>")
        sys.exit(1)

    ground_truth_file = sys.argv[1]

    db_path = "ds_pro.db"

    # Load ground truth and predictions
    ground_truth = load_ground_truth(ground_truth_file)
    predictions = get_predictions_from_db(db_path)
    assert len(ground_truth) == len(
        predictions
    ), "Number of rows in ground truth and predictions do not match"

    assert (
        accuracy_score(ground_truth["Potability"], predictions["class"]) * 100 > 60
    ), "Accuracy is way below test generated in Jupyter notebook"

    print("Test passed: Predicted classes match ground truth.")
