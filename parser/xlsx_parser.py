import pandas as pd

def parse_xlsx(path, max_rows=20):
    """
    Reads all sheets and converts them into text.
    """
    excel = pd.ExcelFile(path)
    full_text = ""

    for sheet in excel.sheet_names:
        df = excel.parse(sheet).head(max_rows)
        full_text += f"""
        Sheet Name: {sheet}
        Columns: {list(df.columns)}

        Sample Rows:
        {df.to_string(index=False)}
        \n
        """

    return full_text
