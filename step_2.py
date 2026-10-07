# **************************************************
# from config import (
#     IDM_FILE_PATH,
#     LINKS_FILE_PATH,
# )

# from rich import print

# from dt_utility import (
#     clear_screen,
#     display_divider,
#     display_main_divider,
#     check_file_exists_force,
# )

# clear_screen()
# display_main_divider()

# check_file_exists_force(file_path=LINKS_FILE_PATH)
# print(f"Links File Path: '{LINKS_FILE_PATH}'")

# check_file_exists_force(file_path=IDM_FILE_PATH)
# print(f"'IDM' File Path: '{IDM_FILE_PATH}'")

# with open(file=LINKS_FILE_PATH, mode="rt", encoding="utf-8") as file:
#     links: list[str] = file.readlines()

# for link in links:
#     link = link.strip()
#     if not link:
#         continue

#     file_name: str = link.split(sep="/")[-1].replace(":", "-")

#     display_divider()
#     print(f"File Name: '{file_name}'")
#     print(link)

# display_main_divider()
# print()
# **************************************************


# **************************************************
import os

# NEW
import shutil
import subprocess

from rich import print

from config import (
    IDM_FILE_PATH,
    LINKS_FILE_PATH,
    # NEW
    OLLAMA_BLOBS_PATH,
    MANIFEST_FILE_PATH,
    MODEL_MANIFESTS_PATH,
    DESTINATION_MANIFEST_FILE_PATH,
)

from dt_utility import (
    clear_screen,
    display_divider,
    display_main_divider,
    # NEW
    check_file_exists_force,
    display_warning_message,
    display_information_message,
)

message: str

clear_screen()
display_main_divider()

# NEW
os.makedirs(name=OLLAMA_BLOBS_PATH, exist_ok=True)
os.makedirs(name=MODEL_MANIFESTS_PATH, exist_ok=True)

check_file_exists_force(file_path=LINKS_FILE_PATH)
print(f"Links File Path: '{LINKS_FILE_PATH}'")

check_file_exists_force(file_path=IDM_FILE_PATH)
print(f"'IDM' File Path: '{IDM_FILE_PATH}'")

# NEW
shutil.copy2(
    src=MANIFEST_FILE_PATH,
    dst=DESTINATION_MANIFEST_FILE_PATH,
)

with open(file=LINKS_FILE_PATH, mode="rt", encoding="utf-8") as file:
    links: list[str] = file.readlines()

for link in links:
    link = link.strip()
    if not link:
        continue

    file_name: str = link.split(sep="/")[-1].replace(":", "-")

    target_file_path: str = os.path.join(OLLAMA_BLOBS_PATH, file_name)
    if os.path.exists(path=target_file_path):
        display_divider()
        message = f"The file '{file_name}' already exists. Skipping download"
        display_warning_message(message=message)
        continue

    display_divider()

    cmd: list[str] = [
        IDM_FILE_PATH,
        "/n",
        "/a",
        "/d",
        link,
        "/p",
        OLLAMA_BLOBS_PATH,
        "/f",
        file_name,
    ]

    subprocess.run(args=cmd, check=True, shell=False)

    message = f"The file '{file_name}' has been queued in 'IDM' for downloading"
    display_information_message(message=message)

subprocess.run(args=[IDM_FILE_PATH, "/s"], check=True, shell=False)

message = "'IDM' started downloading..."
display_divider()
display_information_message(message=message)

display_main_divider()
print()
# **************************************************
