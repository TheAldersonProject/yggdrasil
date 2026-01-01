"""Project configuration."""

from pathlib import Path

CURRENT_FILE_PATH = Path(__file__).resolve()
SRC_FOLDER = CURRENT_FILE_PATH.parent
PROJECT_ROOT = SRC_FOLDER.parent

ASSETS_FOLDER = PROJECT_ROOT / "assets"
DATA_CONTRACTS = ASSETS_FOLDER / "data-contracts"
MODELS_FOLDER = SRC_FOLDER / "models"
MODELS_EXAMPLE_FOLDER = MODELS_FOLDER / "model_templates"
