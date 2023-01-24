import numpy as np
import pandas as pd

# Read in the training and test data
def read_file(url):
    """
    Takes in a Github url as an argument and pulls the CSV file.
    Returns: pandas dataframe of CSV file content
    """
    url += "?raw=true"
    df = pd.read_csv(url)

    return df


