import os
import dropbox
from pathlib import Path

# Dropbox access token
ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'

# Create a Dropbox object
dbx: dropbox.Dropbox = dropbox.Dropbox(ACCESS_TOKEN)

# Folder path in Dropbox Paper
PAPER_PATH = ''

# Folder path to save downloaded files
DOWNLOAD_PATH = './downloaded'

# Create folder to save downloaded files
Path(DOWNLOAD_PATH).mkdir(parents=True, exist_ok=True)

for entry in dbx.files_search(PAPER_PATH, '.paper').matches:
    entry = entry.metadata
    dropbox_path = os.path.dirname(f"./downloaded{entry.path_lower}")
    if dropbox_path:
        dropbox_path = f"{dropbox_path}"
        Path(dropbox_path).mkdir(parents=True, exist_ok=True)
    
    dbx.files_export_to_file(os.path.join(dropbox_path, entry.name.replace(".paper", ".md")), entry.path_lower, "markdown")
    print(f'Downloaded and converted {entry.name} to Markdown format')