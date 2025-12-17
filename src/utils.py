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
