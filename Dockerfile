FROM python:3.8-slim

WORKDIR Spotify

COPY ["requirements.txt", "readMusicFiles.py", "searchMusic.py", "SyncMusic.py", "Spotify/"]

RUN python3 -m pip install -r Spotify/requirements.txt
CMD ["python3", "Spotify/searchMusic.py"]
