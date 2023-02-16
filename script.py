import os
import dropbox
from pathlib import Path

# Dropbox access token
ACCESS_TOKEN = 'sl.BY5mqRa4uiXya7tMB4GZhqbvrE-npa78bKUBA5oCww6xf2xLWUoMoS7MpBQCqbqFf63T9ek_n_6WPzzDGJIM0wnhTkZRxyU0fsMYS8DNeU84STzJiKAKkhvU9ovUjKtCnnAexey-U_T0'

# Create a Dropbox object
dbx = dropbox.Dropbox(ACCESS_TOKEN)

# Folder path in Dropbox Paper
PAPER_PATH = ''

# Folder path to save downloaded files
DOWNLOAD_PATH = './downloaded'

# Create folder to save downloaded files
Path(DOWNLOAD_PATH).mkdir(parents=True, exist_ok=True)

# List all files in the root folder of Dropbox
# for entry in dbx.files_list_folder(PAPER_PATH).entries:
for entry in dbx.files_search(PAPER_PATH, '.paper').matches:
    print(entry.metadata, "\n\n")
    entry = entry.metadata
    md, res = dbx.files_export(entry.path_lower)

    with open(os.path.join(DOWNLOAD_PATH, entry.name.replace(".paper", ".html")), 'wb') as f:
        f.write(res.content)
    

# print(f'Downloaded and converted {entry.name} to Markdown format')



    # if isinstance(entry, dropbox.files.FileMetadata):
    #     print(entry.metadata)
    #     if entry.name.endswith('.paper'):
    #         md, res = dbx.files_download(entry.path_lower)
        
    #         with open(os.path.join(DOWNLOAD_PATH, entry.name), 'wb') as f:
    #             f.write(res.content)

            
    #         # Convert the file to Markdown format
    #         dbx.files_download_to_file(os.path.join(DOWNLOAD_PATH, entry.name + '.md'), entry.path_lower, rev=None)

    #         print(f'Downloaded and converted {entry.name} to Markdown format')

