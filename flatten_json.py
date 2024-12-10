# flatten nested JSON lists where they appear in any row of an column
# assumes that required imports are present - Pandas, etc.

def contains_list(series):
    return any(isinstance(item, list) for item in series)

def flatten_json(data):
    nested_columns = [c for c in data.columns if contains_list(data[c])]

    while len(nested_columns) > 0:
        # dict to store all expanded columns
        expanded_cols = {}
        
        for nested_col in nested_columns:
            # For each col that has a nested JSON object within, explode the nested lists of dictionaries
            expanded_series = data[nested_col].explode()

            if not expanded_series.dropna().empty:
                # Normalise the column containing nested objects
                expanded_col = expanded_series.dropna().apply(pd.Series)
                expanded_col_normalised = pd.json_normalize(expanded_col.to_dict(orient='records'))

                # Rename columns to reflect original structure
                expanded_col_normalised.columns = [f'{nested_col}.{col}{i}' for i, col in enumerate(expanded_col_normalised.columns)]

                # collect expanded columns
                expanded_cols[nested_col] = expanded_col_normalised
            
        # Drop original nested columns and concatenate all expanded columns at once
        data = data.drop(columns=nested_columns).join(pd.concat(expanded_cols.values(), axis=1))

        nested_columns = [c for c in data.columns if contains_list(data[c])]
        
    return data
