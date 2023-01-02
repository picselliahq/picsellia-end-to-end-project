import os
from pathlib import Path

from dotenv import load_dotenv
from picsellia.sdk.model import Framework
from picsellia.types.enums import InferenceType

# Parses the .env file and loads all the variables found as environment variables.
load_dotenv()

# Environment variables
API_TOKEN = os.getenv("API_TOKEN")
ORGANIZATION_NAME = os.getenv("ORGANIZATION_NAME")

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

# Dataset 
DATASET_NAME = "conveyor-belt-dataset"
DATASET_DESCRIPTION = "Carton type detection dataset with images from a conveyor belt"
NB_OF_DATA = None
TAGS = ["Cartons", "test"]

# Dataset version
DATASET_VERSION = "test"
DATASET_VERSION_DESCRIPTION = "testing version"
DATASET_TYPE = InferenceType.OBJECT_DETECTION
LABELS = ["Energy_Tiffin","Energy_Regular"] 

# Project 
PROJECT_NAME = "Conveyor-belt-project"

# Model 
MODEL_NAME = "efficientdet-d3"
MODEL_VERSION = 0
MODEL_DESCRIPTION = "A custom efficientdet-d3 model"

# Experiment 
EXPERIMENT_NAME = "experiment-efficientdet-d3"
EXPERIMENT_DESCRIPTION = "experiment using model efficientdet-d3"
EXPERIMENT_DATASET_VERSION = "train"
EXPERIMENT_DATASET_NAME = "conveyor-belt-dataset"

# Trained models & weights directories
MODELS_DIR = ROOT_DIR / "models" 
ARTIFACTS_DIR = MODELS_DIR / "efficientdet-d3"
ARTIFACTS_NAME = "efficientdet-d3-model"

# Custom model parameters 
STEPS = 1000
LR_TYPE = "exponential_decay"
BATCH_SIZE = 4
DECAY_STEPS = 500
DECAY_FACTOR = 0.9
LEARNING_RATE = 0.001
ANNOTATION_TYPE = "rectangle"

# Custom model framework 
FRAMEWORK = Framework.TENSORFLOW

# Deployment & Inference 
DEPLOYMENT_NAME = "scalding-version"
INFERENCE_DATA_DIR = VALID_DATA_DIR