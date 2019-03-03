# Statement for enabling the development environment
DEBUG = True
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

TRAIN_RAW_DATA_DIR = "assets/data/stage_2_train_images"
TRAIN_CLEAN_DATA_DIR = "assets/data/stage_2_train_images_png"

TEST_RAW_DATA_DIR = "data/stage_2_test_images"
TEST_CLEAN_DATA_DIR = "data/stage_2_test_images_png"
TRAINING_SPLIT_DIR = "training_splits"
DETAILED_CLASS_INFO = "data/stage_2_detailed_class_info.csv"
TRAIN_LABELS = "data/stage_2_train_labels.csv"
CLASSIFICATION_WEIGHTS_DIR = "classification/weights"
CLASSIFICATION_RESULTS_DIR = "classification/results"
DETECTION_WEIGHTS_DIR = "detection/weights"
DETECTION_RESULTS_DIR = "detection/results"
