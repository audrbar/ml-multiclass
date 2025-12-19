import os

import pandas as pd
import logging
from utils import adjust_pandas_display, load_csv, load_excel, print_unique_values_count, write_csv, print_column_value_counts, print_distinct_values_from_csv_column, get_distinct_values_from_csv_column, print_dataframe_characteristics, DATA_DIR

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

pd.options.display.max_columns = None


# Define paths for storing data
RAW_DATA = os.path.join(DATA_DIR, "visi_duom.xlsx")
PREPROCESSED_DATA = os.path.join(DATA_DIR, "preprocessed.csv")

# 1. Load and Explore Data
df = load_excel(RAW_DATA)

if df is not None:
    # Print comprehensive dataframe characteristics
    print_dataframe_characteristics(df)

    # print(f"\nDF HEAD:\n {df.head()}\n")
    # print(f"\nDF COLUMNS:\n {df.columns}\n")
    # print(f"\nDF DATA TYPES:\n {df.dtypes}\n")

    # # Print column value counts
    # print_column_value_counts(df, max_display=20)

    # # Get distinct values from comma-separated column with counts
    # distinct_items = get_distinct_values_from_csv_column(df, 'ix_rdo_docs_chief_executors.ORG_NAME as Pagrindinis vykdytojas')
    # print(f"\nFound {len(distinct_items)} distinct items")

    # Show all columns' unique counts (sorted by highest first)
    # print_unique_values_count(df)

    # # Print them nicely with counts
    # print_distinct_values_from_csv_column(df, 'ix_rdo_docs_chief_executors.ORG_NAME as Pagrindinis vykdytojas')
    # print_distinct_values_from_csv_column(df, 'ix_tdo_docs.chief_executor as VISI VYKDYTOJAI', limit=250)
    # print_distinct_values_from_csv_column(df, 'ix_rdo_docs.TITLE')
else:
    print("Error: Could not load data!")

# print("\nUniques:\n")
# print(f"IS_ELECTRO: {df['ix_rdo_docs.IS_ELECTRO'].nunique()}")
# print(f"Senders: {df['ix_rdo_docs_senders.org_name as SIUNTEJAI'].nunique()}")
# print(f"Receivers: {df['ix_rdo_docs_receivers.org_name as GAVEJAI'].nunique()}")
# print(f"Assignees: {df['ix_rdo_docs_assignees.ORG_NAME as Rezoliucija paskirta ID'].nunique()}")
# print(f"Chief Executor: {df['ix_rdo_docs_chief_executors.ORG_NAME as Pagrindinis vykdytojas'].nunique()}")
# print(f"All Executors: {df['ix_tdo_docs.chief_executor as VISI VYKDYTOJAI'].nunique()}")
# print(f"Assignment Task Type: {df['ix_tdo_docs.ASSIGNMENT_TASK_TYPE as Veiklos uzduotis'].nunique()}")
# print(f"Control Type: {df['ix_tdo_docs.CONTROL_TYPE'].nunique()}")
# print(f"Controller: {df['ix_tdo_docs.CONTROLLER'].nunique()}")
# print(f"Curator: {df['ix_tdo_docs.CURATOR'].nunique()}")
# print(f"Other Executors: {df['ix_tdo_docs.EXECUTORS as KITI VYKDYTOJAI'].nunique()}")
# print(f"Assignment Task Coordinator: {df['ix_tdo_docs.ASSIGNMENT_TASK_COORD as Veiklos uzduoties kuratorius'].nunique()}")
