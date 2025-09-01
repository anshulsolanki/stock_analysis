# my_functions.py

"""
This module contains a collection of useful functions for data analysis,
visualization, and general utility purposes.
"""

import pandas as pd
import numpy as np

def greet_user(name: str) -> str:
    """
    Greets a user by their name.

    Args:
        name (str): The name of the user.

    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}! Welcome to the world of Python functions."

def calculate_average(numbers: list) -> float:
    """
    Calculates the average of a list of numbers.

    Args:
        numbers (list): A list of numerical values.

    Returns:
        float: The average of the numbers.
    """
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

def create_dataframe(data: dict) -> pd.DataFrame:
    """
    Creates a pandas DataFrame from a dictionary.

    Args:
        data (dict): A dictionary where keys are column names and values are lists of data.

    Returns:
        pd.DataFrame: A pandas DataFrame.
    """
    return pd.DataFrame(data)

def main():
    """
    This is an example of how the functions can be used when the script is run directly.
    This block will not run when the module is imported into a Jupyter Notebook.
    """
    print(greet_user("Alice"))
    print(f"The average of [1, 2, 3, 4, 5] is: {calculate_average([1, 2, 3, 4, 5])}")
    
    sample_data = {'col1': [1, 2, 3], 'col2': ['A', 'B', 'C']}
    df = create_dataframe(sample_data)
    print("\nSample DataFrame:")
    print(df)

if __name__ == "__main__":
    main()