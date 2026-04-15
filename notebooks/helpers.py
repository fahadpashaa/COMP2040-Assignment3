"""
helpers.py
A small collection of helper functions used throughout the analysis notebook.

This file keeps the notebook cleaner by moving repeated logic into one place.
Any function that I use more than once in the analysis section will live here.
"""


def hello():
    return "helpers.py is working"


def filter_by_year(df, year):
    """
    Filter the dataset to only include rows where the crime occurred
    in the given year. This keeps the notebook cleaner when I want
    to focus on a specific time period.
    """
    return df[df['DATE OCC'].dt.year == year]


def count_by_column(df, column):
    """
    Return value counts for any column. This is useful for quickly
    checking which categories appear the most without rewriting the
    same line of code each time.
    """
    return df[column].value_counts()


def top_n(df, column, n=10):
    """
    Show the top N most frequent values in a column. I use this when
    I want a quick summary of the most common crime types, areas, or
    any other categorical field.
    """
    return df[column].value_counts().head(n)

    
