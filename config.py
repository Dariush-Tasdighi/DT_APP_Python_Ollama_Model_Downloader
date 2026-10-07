"""
Dariush Tasdighi - Custom Ollama Model Downloader Module
"""

import os

from typing import Final
from dt_utility import prevent_direct_execution

OLLAMA_PATH: Final[str] = r"D:\OLLAMA_MODELS"
# - Note: '~' -> C:\Users\USERNAME
# OLLAMA_PATH: Final[str] = os.path.expanduser(path="~/.ollama/models")

# > ollama rm gemma3:270m
#   deleted 'gemma3:270m'
#   Error: model 'gemma3:270m' not found
# > ollama pull gemma3:270m
# > ollama run gemma3:270m
MODEL_FULL_NAME: Final[str] = "gemma3:270m".strip().lower()

# > ollama rm gemma4:12b
# > ollama pull gemma4:12b
# > ollama run gemma4:12b
# MODEL_FULL_NAME: Final[str] = "gemma4:12b".strip().lower()

# > ollama rm gemma4:e2b
# > ollama pull gemma4:e2b
# > ollama run gemma4:e2b
# MODEL_FULL_NAME: Final[str] = "gemma4:e2b".strip().lower()

# > ollama rm gemma4:e4b
# > ollama pull gemma4:e4b
# > ollama run gemma4:e4b
# MODEL_FULL_NAME: Final[str] = "gemma4:e4b".strip().lower()

# > ollama rm qwen3.5:0.8b
# > ollama pull qwen3.5:0.8b
# > ollama run qwen3.5:0.8b
# MODEL_FULL_NAME: Final[str] = "qwen3.5:0.8b".strip().lower()

# > ollama rm qwen3.5:2b
# > ollama pull qwen3.5:2b
# > ollama run qwen3.5:2b
# MODEL_FULL_NAME: Final[str] = "qwen3.5:2b".strip().lower()

# > ollama rm qwen3.5:4b
# > ollama pull qwen3.5:4b
# > ollama run qwen3.5:4b
# MODEL_FULL_NAME: Final[str] = "qwen3.5:4b".strip().lower()

# > ollama rm qwen3.5:9b
# > ollama pull qwen3.5:9b
# > ollama run qwen3.5:9b
# MODEL_FULL_NAME: Final[str] = "qwen3.5:9b".strip().lower()

TAG_NAME: Final[str] = MODEL_FULL_NAME.split(sep=":")[1]
MODEL_NAME: Final[str] = MODEL_FULL_NAME.split(sep=":")[0]

BASE_URL: Final[str] = f"https://registry.ollama.ai/v2/library/{MODEL_NAME}"

DOWNLOAD_PATH: Final[str] = "./downloads"
LINKS_FILE_PATH: Final[str] = f"{DOWNLOAD_PATH}/{MODEL_NAME}_{TAG_NAME}_links.txt"
MANIFEST_FILE_PATH: Final[str] = f"{DOWNLOAD_PATH}/{MODEL_NAME}_{TAG_NAME}_manifest.json"
# LINKS_FILE_PATH: Final[str] = os.path.join(DOWNLOAD_PATH, f"{MODEL_NAME}_{TAG_NAME}_links.txt")
# MANIFEST_FILE_PATH: Final[str] = os.path.join(DOWNLOAD_PATH, f"{MODEL_NAME}_{TAG_NAME}_manifest.json")

OLLAMA_BLOBS_PATH: Final[str] = os.path.join(OLLAMA_PATH, "blobs")
OLLAMA_MANIFESTS_PATH: Final[str] = os.path.join(OLLAMA_PATH, "manifests", "registry.ollama.ai", "library")

MODEL_MANIFESTS_PATH: str = os.path.join(OLLAMA_MANIFESTS_PATH, MODEL_NAME)
DESTINATION_MANIFEST_FILE_PATH: Final[str] = os.path.join(MODEL_MANIFESTS_PATH, TAG_NAME)

IDM_FILE_PATH: Final[str] = r"C:\Program Files (x86)\Internet Download Manager\IDMan.exe"

if __name__ == "__main__":
    prevent_direct_execution()
