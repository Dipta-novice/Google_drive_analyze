import pandas as pd

def parse_csv(path, max_rows=30):
    """
    Reads CSV and converts it into text format.
    Limits rows to avoid token overflow.
    """
    df = pd.read_csv(path)

    preview = df.head(max_rows)
    text = f"""
    CSV File Summary:
    - Columns: {list(df.columns)}
    - Total Rows: {len(df)}

    Sample Data:
    {preview.to_string(index=False)}
    """
    return text
