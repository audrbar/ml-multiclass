import os
import pandas as pd

# Read base source directory
DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
MODELS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../models"))

print(f"Data directory set to: {DATA_DIR}")
print(f"Models directory set to: {MODELS_DIR}")

def adjust_pandas_display(max_rows=None, max_columns=None, width=None):
    """Adjust pandas display settings."""
    pd.set_option('display.max_rows', max_rows)
    pd.set_option('display.max_columns', max_columns)
    pd.set_option('display.width', width)
    pd.set_option('display.max_colwidth', None)

def load_csv(filename):
    """Loads CSV into DataFrame."""
    try:
        return pd.read_csv(filename, delimiter=',', on_bad_lines='skip')
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return None

def load_excel(filename):
    """Loads Excel file into DataFrame."""
    try:
        return pd.read_excel(filename, encoding='utf-8-sig', index=False, on_bad_lines='skip')
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return None

def write_csv(data_frame, output_file, index=False):
    """Writes DataFrame to CSV."""
    try:
        data_frame.to_csv(output_file, index=index)
    except Exception as e:
        print(f"Error writing to CSV: {e}")
