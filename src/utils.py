import os
import pandas as pd

# Read base source directory
DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
MODELS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../models"))

# print(f"Data directory set to: {DATA_DIR}")
# print(f"Models directory set to: {MODELS_DIR}")

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
    """
    Loads Excel file into DataFrame with automatic date column detection and conversion.

    Args:
        filename (str): Path to the Excel file

    Returns:
        pd.DataFrame: DataFrame with date columns properly converted
    """
    try:
        df = pd.read_excel(filename)

        # Auto-detect and convert date columns
        date_keywords = ['ix_rdo_docs.CREATED_DATE', 'ix_rdo_docs.REGISTRATION_DATE', 'ix_rdo_docs.DOCUMENT_DATE']
        date_columns = [col for col in df.columns if any(keyword in col.lower() for keyword in date_keywords)]

        for col in date_columns:
            try:
                df[col] = pd.to_datetime(df[col], infer_datetime_format=True, errors='coerce')
                print(f"✓ Converted column '{col}' to datetime")
            except Exception as e:
                print(f"⚠ Could not convert column '{col}': {e}")

        return df
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return None
    except Exception as e:
        print(f"Error loading Excel file: {e}")
        return None

def write_csv(data_frame, output_file, index=False):
    """Writes DataFrame to CSV."""
    try:
        data_frame.to_csv(output_file, index=index)
    except Exception as e:
        print(f"Error writing to CSV: {e}")

def print_column_value_counts(data_frame, max_display=10):
    """
    Print a count of each dataframe column's unique items.

    Args:
        data_frame (pd.DataFrame): The dataframe to analyze
        max_display (int): Maximum number of values to display per column (default: 10)
    """
    print("\n" + "="*80)
    print("COLUMN VALUE COUNTS")
    print("="*80)

    for column in data_frame.columns:
        unique_count = data_frame[column].nunique()
        null_count = data_frame[column].isnull().sum()

        print(f"\n{column}")
        print(f"  Total unique values: {unique_count}   Null values: {null_count}")
        print(f"  Value counts (top {max_display}):")

        value_counts = data_frame[column].value_counts().head(max_display)
        for value, count in value_counts.items():
            print(f"    {value}: {count}")

def get_distinct_values_from_csv_column(data_frame, column_name, strip_whitespace=True):
    """
    Extract distinct values from a column containing comma-separated strings with counts.

    Args:
        data_frame (pd.DataFrame): The dataframe to analyze
        column_name (str): Name of the column containing comma-separated values
        strip_whitespace (bool): Whether to strip whitespace from each value (default: True)

    Returns:
        dict: Dictionary with distinct values as keys and their appearance counts as values
    """
    if column_name not in data_frame.columns:
        print(f"✗ Column '{column_name}' not found in dataframe")
        return {}

    value_counts = {}

    for cell_value in data_frame[column_name].dropna():
        # Split by comma and process each value
        if isinstance(cell_value, str):
            values = cell_value.split(',')
            for value in values:
                if strip_whitespace:
                    value = value.strip()
                if value:  # Only add non-empty values
                    value_counts[value] = value_counts.get(value, 0) + 1

    return value_counts

def print_distinct_values_from_csv_column(data_frame, column_name, strip_whitespace=True, sort_by='count'):
    """
    Print distinct values from a column containing comma-separated strings with appearance counts.

    Args:
        data_frame (pd.DataFrame): The dataframe to analyze
        column_name (str): Name of the column containing comma-separated values
        strip_whitespace (bool): Whether to strip whitespace from each value (default: True)
        sort_by (str): Sort order - 'count' (descending) or 'name' (alphabetical, default: 'count')
    """
    value_counts = get_distinct_values_from_csv_column(data_frame, column_name, strip_whitespace)

    if not value_counts:
        print(f"✗ No values found in column '{column_name}'")
        return

    print(f"\n{'='*80}")
    print(f"DISTINCT VALUES FROM COLUMN: {column_name}")
    print(f"{'='*80}")
    print(f"Total distinct values: {len(value_counts)}\n")

    # Sort based on preference
    if sort_by.lower() == 'count':
        sorted_values = sorted(value_counts.items(), key=lambda x: x[1], reverse=True)
    else:  # sort by name
        sorted_values = sorted(value_counts.items(), key=lambda x: x[0])

    for i, (value, count) in enumerate(sorted_values, 1):
        print(f"{i}. {value:<50} | Count: {count}")

def print_dataframe_characteristics(data_frame):
    """
    Print comprehensive dataframe characteristics including size, columns, data types, and missing values.

    Args:
        data_frame (pd.DataFrame): The dataframe to analyze
    """
    print(f"\n{'='*80}")
    print("DATAFRAME CHARACTERISTICS")
    print(f"{'='*80}")

    # Basic info
    print(f"\n📊 SHAPE AND SIZE:")
    print(f"  Rows: {data_frame.shape[0]:,}")
    print(f"  Columns: {data_frame.shape[1]}")
    print(f"  Total cells: {data_frame.shape[0] * data_frame.shape[1]:,}")
    print(f"  Memory usage: {data_frame.memory_usage(deep=True).sum() / 1024**2:.2f} MB")

    # Data types summary
    print(f"\n📋 DATA TYPES:")
    dtype_summary = data_frame.dtypes.value_counts()
    for dtype, count in dtype_summary.items():
        print(f"  {str(dtype):<15} : {count}")

    # Missing values
    print(f"\n❓ MISSING VALUES:")
    missing_data = data_frame.isnull().sum()
    missing_percent = (missing_data / len(data_frame)) * 100
    columns_with_missing = missing_data[missing_data > 0]

    print(f"  Total columns: {len(data_frame.columns)}")
    print(f"  Columns with missing values: {len(columns_with_missing)}")
    print(f"  Columns without missing values: {len(data_frame.columns) - len(columns_with_missing)}\n")

    # Print all columns with their missing value counts
    print(f"  {'Column Name':<70} | Values  | Missing | %")
    print(f"  {'-'*70}-+---------+---------+--------")

    for col in data_frame.columns:
        values_count = len(data_frame) - missing_data[col]
        missing_count = missing_data[col]
        missing_pct = missing_percent[col]
        status = "✓" if missing_count == 0 else "✗"
        print(f"  {status} {col:<68} | {values_count:>7,} | {missing_count:>7} | {missing_pct:>5.1f}%")

    print(f"\n{'='*80}\n")
