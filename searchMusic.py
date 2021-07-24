from readMusicFiles import ReadMusicData
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from tqdm import tqdm
from SyncMusic import Sync
from dotenv import load_dotenv
load_dotenv()
import os


class SearchMusic():

    def __init__(self):
        self.musicName = ""
        self.rm = ReadMusicData("Music")
        self.sync = Sync(os.environ["PLAYLISTNAME"])
        self.availableSongs = []
        self.unavailableSongs = []
        self.clientId = os.environ["CLIENTID"]
        self.secret_client_id = os.environ["CLIENTSECRET"]
        self.sp = self.authorize()
        self.username = os.environ["USERNAME"]

    def search(self):
        for song in tqdm(self.rm.music, desc="Searching songs on spotify"):
            if song["title"] is None:
                if song["artist"] is None:
                    query = song["name"].replace("\x00", " ")
                else:
                    query = song["artist"].replace("\x00", " ")
            else:
                query = song["title"].replace("\x00", " ")
            results = None
            try:
                results = self.sp.search(q=query, limit=1)
            except:
                pass
            if results['tracks']['items']:
                for idx, track in enumerate(results['tracks']['items']):
                    self.availableSongs.append(track['id'])
            else:
                self.unavailableSongs.append(query)

    def getLocalMusic(self):
        self.rm.readFolder()

    def authorize(self):
        return spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=self.clientId,
                                                                     client_secret=self.secret_client_id))

    def createAndSync(self):
        self.sync.createPlaylistandSync(self.clientId, self.secret_client_id, self.availableSongs, self.username)

    def logUnavailableTracks(self):
        with open("UnavailableTracks.log", 'w', encoding="utf-8") as utl:
            for ut in self.unavailableSongs:
                utl.write("Track Name -- > \t" + ut + "\n")


if __name__ == '__main__':
    sm = SearchMusic()
    sm.getLocalMusic()
    sm.search()
    sm.logUnavailableTracks()
    sm.createAndSync()
    print("-------------------Synchronization Complete-----------------")
