import os
import eyed3
from tqdm import tqdm
import re
eyed3.log.setLevel("ERROR")


class ReadMusicData():

    def __init__(self, folder=""):
        self.folder = folder
        self.music = []

    def readFolder(self):
        music_data = os.listdir(self.folder)
        for song in tqdm(music_data, desc="Searching for local music"):
            file = eyed3.load(self.folder + os.sep + song)
            title, artist, name = self.processData(file, song)
            try:
                data = {"name": name, "artist": artist, "title": title}
            except:
                data = {"name": song}
            self.music.append(data)

    def processData(self, file, song):
        try:
            titleInfo = re.split("-|\(|\)|-|[0-9]|\.", file.tag.title)
            artistInfo = re.split("-|\(|\)|-|[0-9]|\.", file.tag.artist)
            songInfo = re.split("-|\(|\)|-|[0-9]|\.", song)
        except:
            songInfo = re.split("-|\(|\)|-|[0-9]\.", song)
            titleInfo = None
            artistInfo = None

        title = None
        artist = None
        name = None
        if titleInfo is not None:
            for t in titleInfo:
                if len(t) > 1:
                    title = t
                    break
        if artistInfo is not None:
            for a in artistInfo:
                if len(a) > 1:
                    artist = a
                    break
        if songInfo is not None:
            for s in songInfo:
                if len(s) > 1:
                    name = s
                    break
        return title, artist, name