import os
from pathlib import Path

from dotenv import load_dotenv


# Parses the .env file and loads all the variables found as environment variables.
load_dotenv()

# Environment variables
API_TOKEN = os.getenv("API_TOKEN")
ORGANIZATION_ID = os.getenv("ORGANIZATION_ID")


# Project & data Directories
ROOT_DIR = Path.cwd().resolve()
RAW_DATA_DIR = ROOT_DIR / "data" / "raw"
TRAIN_DATA_DIR = RAW_DATA_DIR / "train"
TEST_DATA_DIR = RAW_DATA_DIR / "test"
VALID_DATA_DIR = RAW_DATA_DIR / "valid"

# Data tags in the Datalake 
TRAIN_TAG = "train"
TEST_TAG = "test"
VALID_TAG = "valid"
CARTONS_TAG = "Cartons"
REGULAR_ENERGY_TAG = "Energy_Regular"
ENERGY_TIFFIN_TAG = "Energy_Tiffin"



