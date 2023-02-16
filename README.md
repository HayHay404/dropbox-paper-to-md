# Paper to MD
A simple converter to download all your Dropbox Paper documents as Markdown files while maintaining the same folder structure.

## Installation
```bash
$ git clone
$ cd paper-to-md
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Usage
```bash
python script.py
```

## Configuration
1. You need to create a Dropbox app and generate an access token. You can do that [here](https://www.dropbox.com/developers/apps/create).
2. You'll need the following permissions to the app before generating the token:
    - account_info.write
    - account_info.read
    - files.metadata.read
    - files.content.read
3. Replace the `YOUR_ACCESS_TOKEN` in `script.py` with the generated token.
4. Run the script.

## License
MIT