import spotipy
from spotipy.oauth2 import SpotifyOAuth
from tqdm import tqdm
import os


class Sync():

    def __init__(self, playlist=""):
        self.playlistName = playlist

    def createPlaylistandSync(self, c, sc, trackIds, username):
        scope = "playlist-modify-public"

        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=c, client_secret=sc, redirect_uri='http://localhost/'))

        flag = False
        playlistId = None
        playlists = sp.current_user_playlists()
        for pl in playlists['items']:
            if pl['name'] == self.playlistName:
                flag = True
                playlistId = pl['id']
                break
        if not flag:
            result = sp.user_playlist_create(username, name=self.playlistName)
            playlistId = result["id"]
        
        for tid in tqdm(trackIds, desc="Synchronizing songs"):
            trackId = "spotify:track:" + tid
            sp.user_playlist_add_tracks(username, playlistId, [trackId])