import os
import pandas as pd
import logging
from utils import adjust_pandas_display, load_csv, load_excel, write_csv, DATA_DIR

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Define paths for storing data
RAW_DATA = os.path.join(DATA_DIR, "visi_duom.xlsx")
PREPROCESSED_DATA = os.path.join(DATA_DIR, "preprocessed.csv")

# 1. Load and Explore Data
df = pd.read_excel(RAW_DATA)
print(df.head())
print(df.info())
print("\nUniques:\n")
print(f"IS_ELECTRO: {df['ix_rdo_docs.IS_ELECTRO'].nunique()}")
print(f"Senders: {df['ix_rdo_docs_senders.org_name as SIUNTEJAI'].nunique()}")
print(f"Receivers: {df['ix_rdo_docs_receivers.org_name as GAVEJAI'].nunique()}")
print(f"Assignees: {df['ix_rdo_docs_assignees.ORG_NAME as Rezoliucija paskirta ID'].nunique()}")
print(f"Chief Executor: {df['ix_rdo_docs_chief_executors.ORG_NAME as Pagrindinis vykdytojas'].nunique()}")
print(f"All Executors: {df['ix_tdo_docs.chief_executor as VISI VYKDYTOJAI'].nunique()}")
print(f"Assignment Task Type: {df['ix_tdo_docs.ASSIGNMENT_TASK_TYPE as Veiklos uzduotis'].nunique()}")
print(f"Control Type: {df['ix_tdo_docs.CONTROL_TYPE'].nunique()}")
print(f"Controller: {df['ix_tdo_docs.CONTROLLER'].nunique()}")
print(f"Curator: {df['ix_tdo_docs.CURATOR'].nunique()}")
print(f"Other Executors: {df['ix_tdo_docs.EXECUTORS as KITI VYKDYTOJAI'].nunique()}")
print(f"Assignment Task Coordinator: {df['ix_tdo_docs.ASSIGNMENT_TASK_COORD as Veiklos uzduoties kuratorius'].nunique()}")