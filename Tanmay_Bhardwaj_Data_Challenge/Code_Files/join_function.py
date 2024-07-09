import pandas as pd

def merge_dataframes(df1, df2, merge_columns, how='left'):
    """
    Merges two DataFrames on specified columns.

    Parameters:
    df1 (pd.DataFrame): The first DataFrame.
    df2 (pd.DataFrame): The second DataFrame.
    merge_columns (list): List of columns to merge on.
    how (str): Type of join to perform, default is 'left'.

    Returns:
    pd.DataFrame: The merged DataFrame.
    """
    if not isinstance(df1, pd.DataFrame) or not isinstance(df2, pd.DataFrame):
        raise ValueError("Both df1 and df2 need to be pandas DataFrames.")
    
    if not isinstance(merge_columns, list):
        raise ValueError("merge_columns should be a list of column names.")
    
    merged_df = df1.merge(df2, on=merge_columns, how=how)
    
    return merged_df
