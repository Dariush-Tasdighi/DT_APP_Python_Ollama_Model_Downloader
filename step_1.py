# **************************************************
# from config import (
#     BASE_URL,
#     TAG_NAME,
#     MODEL_NAME,
#     MODEL_FULL_NAME,
# )

# from rich import print

# from dt_utility import (
#     clear_screen,
#     display_divider,
#     display_main_divider,
#     display_title_message,
# )

# clear_screen()
# display_main_divider()

# message: str

# message = f"Fetching manifest for '{MODEL_FULL_NAME}'"
# display_title_message(message=message)

# message = f"Model Name: {MODEL_NAME}"
# display_divider()
# print(message)

# message = f"Base    URL: {BASE_URL}"
# display_divider()
# print(message)

# request_url: str = f"{BASE_URL}/manifests/{TAG_NAME}"
# message = f"Request URL: {request_url}"
# print(message)

# display_main_divider()
# print()
# **************************************************


# **************************************************
# # NEW
# import os
# import json

# from config import (
#     BASE_URL,
#     TAG_NAME,
#     MODEL_FULL_NAME,
#     # NEW
#     DOWNLOAD_PATH,
#     MANIFEST_FILE_PATH,
# )

# from rich import print

# from dt_utility import (
#     clear_screen,
#     display_divider,
#     display_main_divider,
#     display_title_message,
#     display_success_message,
# )

# # NEW
# from urllib.request import (
#     Request,
#     urlopen,
# )

# clear_screen()
# display_main_divider()

# message: str

# message = f"Fetching manifest for '{MODEL_FULL_NAME}'"
# display_title_message(message=message)

# message = f"Base    URL: {BASE_URL}"
# display_divider()
# print(message)

# request_url: str = f"{BASE_URL}/manifests/{TAG_NAME}"
# message = f"Request URL: {request_url}"
# display_divider()
# print(message)

# # NEW
# display_divider()

# # NEW
# headers: dict = {"Accept": "application/vnd.docker.distribution.manifest.v2+json"}

# # NEW
# request = Request(url=request_url, headers=headers, method="GET")
# response = urlopen(url=request)
# manifest = json.load(fp=response)

# # NEW
# message = f"Manifest fetched successfully"
# display_success_message(message=message)

# # NEW
# display_divider()
# print(manifest)

# # NEW
# os.makedirs(name=DOWNLOAD_PATH, exist_ok=True)

# # NEW
# with open(file=MANIFEST_FILE_PATH, mode="wt", encoding="utf-8") as file:
#     json.dump(obj=manifest, fp=file)

# # NEW
# message = f"Manifest saved successfully. File Name: '{MANIFEST_FILE_PATH}'"
# display_divider()
# display_success_message(message=message)

# display_main_divider()
# print()
# **************************************************


# **************************************************
# **************************************************
# **************************************************
# list_1: list[str] = ["A", "B", "C"]
# list_2: list[str] = ["D", "E", "F", "G"]

# my_list: list[str] = list_1 + list_2
# print(my_list)
# **************************************************
# **************************************************
# **************************************************


# **************************************************
# **************************************************
# **************************************************
# def human(number: int) -> str:
#     number_float = float(number)
#     for unit in ("B", "KB", "MB", "GB", "TB"):
#         if number_float < 1024 or unit == "TB":
#             result: str = f"{int(number_float)} B"
#             if unit != "B":
#                 result = f"{int(number_float)} {unit}"
#             return result
#         number_float /= 1024
#     return ""


# print(human(517))
# print()
# print(human(1024))
# print(human(1024 * 517))
# print()
# print(human(1024 * 1024))
# print(human(1024 * 1024 * 517))
# print()
# print(human(1024 * 1024 * 1024))
# print(human(1024 * 1024 * 1024 * 517))
# print()
# print(human(1024 * 1024 * 1024 * 1024))
# print(human(1024 * 1024 * 1024 * 1024 * 517))
# print(human(1024 * 1024 * 1024 * 1024 * 1024))
# **************************************************
# **************************************************
# **************************************************


# **************************************************
import os
import sys
import json

from config import (
    TAG_NAME,
    BASE_URL,
    DOWNLOAD_PATH,
    LINKS_FILE_PATH,
    MODEL_FULL_NAME,
    MANIFEST_FILE_PATH,
)

from rich import print

from dt_utility import (
    clear_screen,
    display_divider,
    display_main_divider,
    display_title_message,
    display_success_message,
)

from urllib.request import (
    Request,
    urlopen,
)


# NEW
def human(number: int) -> str:
    number_float = float(number)
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if number_float < 1024 or unit == "TB":
            result: str = f"{int(number_float)} B"
            if unit != "B":
                result = f"{int(number_float)} {unit}"
            return result
        number_float /= 1024
    return ""


clear_screen()
display_main_divider()

message: str

message = f"Fetching manifest for '{MODEL_FULL_NAME}'"
display_title_message(message=message)

message = f"Base    URL: {BASE_URL}"
display_divider()
print(message)

request_url: str = f"{BASE_URL}/manifests/{TAG_NAME}"
message = f"Request URL: {request_url}"
print(message)

display_divider()

headers: dict = {"Accept": "application/vnd.docker.distribution.manifest.v2+json"}

request = Request(url=request_url, headers=headers, method="GET")
response = urlopen(url=request)
manifest = json.load(fp=response)

message = f"Manifest fetched successfully"
display_success_message(message=message)

# display_divider()  # For Debugging!
# print(manifest)  # For Debugging!
# sys.exit(0)  # For Debugging!

os.makedirs(name=DOWNLOAD_PATH, exist_ok=True)

with open(file=MANIFEST_FILE_PATH, mode="wt", encoding="utf-8") as file:
    json.dump(obj=manifest, fp=file)

message = f"Manifest file saved successfully. File Name: '{MANIFEST_FILE_PATH}'"
display_divider()
display_success_message(message=message)

# NEW
layers = [manifest["config"]] + manifest["layers"]

# display_divider()  # For Debugging!
# print(layers)  # For Debugging!
# sys.exit(0)  # For Debugging!

# - NEW - For Debugging!
# display_divider()
# for index, layer in enumerate(iterable=layers, start=1):
#     size: int = int(layer["size"])
#     digest: str = str(layer["digest"])
#     print(f"{index:2d}: {digest} {human(size):>10}")
# sys.exit(0)

# - NEW - For Debugging!
# display_divider()
# for layer in layers:
#     digest: str = str(layer["digest"])
#     url: str = f"{BASE_URL}/blobs/{digest}"
#     print(url)
# sys.exit(0)

# NEW
with open(file=LINKS_FILE_PATH, mode="wt", encoding="utf-8") as file:
    for layer in layers:
        digest: str = str(layer["digest"])
        url: str = f"{BASE_URL}/blobs/{digest}"
        file.write(f"{url}\n")

message = f"Links file saved successfully. File Name: '{LINKS_FILE_PATH}'"
display_divider()
display_success_message(message=message)

display_main_divider()
print()
# **************************************************
