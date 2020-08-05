def isolate(iso, n_rows):
    """
    Isolate a variable by applying the mean to all other variables.
    
    Parameters:
    iso: the column name of the variable to isolate
    n_rows: the number of unique values in the target column
    
    """
    mean_df = X.loc[:n_rows - 1]
    iso_series = np.linspace(X[iso].min(), 
                             X[iso].max(), n_rows)
    for col in X.columns:
        mean_df.loc[:, col] = X[col].mean()
    mean_df.loc[:, iso] = iso_series
    return mean_df