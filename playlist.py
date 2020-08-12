import json
import os

import requests

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time
from exceptions import ResponseException
from secrets import spotify_token, spotify_user_id, spotify_song_token, sp, client_id, client_secret
import spotipy.util as util

class CustomPlaylist:

    def getTrackIDs(self, user, playlist_id):
        ids = []
        playlist = sp.user_playlist(user, playlist_id)
        for item in playlist['tracks']['items']:
            track = item['track']
            ids.append(track['id'])
        return ids

    def getDiscoverWeeklySongs(self):
        """Get Songs from Discover Playlist"""
        playlist_id = "37i9dQZEVXcCQpauWAUHoQ"
        ids = self.getTrackIDs('caylaseaman', playlist_id)
        print(ids)
        return ids
    
    
    def getReleaseRadarsongs(self):
        """Get Songs from Release Redar Playlist"""
        playlist_id = "37i9dQZEVXbvAO1IKDPXPL"
        ids = self.getTrackIDs('caylaseaman', playlist_id)
        print(ids)
        return ids
    
    def get_songs(self, playlist_id):
        """Get Songs from Playlist"""
        ids = self.getTrackIDs('caylaseaman', playlist_id)
        print(ids)
        return ids

    def create_playlist(self):
        """Create A New Playlist"""
        request_body = json.dumps({
            "name": "Test",
            "description": "a new playlist",
            "public": True
        })

        query = "https://api.spotify.com/v1/users/{}/playlists".format(
            spotify_user_id)
        response = requests.post(
            query,
            data=request_body,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(spotify_token)
            }
        )
        response_json = response.json()

        # playlist id
        return response_json["id"]

    def get_spotify_uri(self, song_name, artist):
        """Search For the Song"""
        song_name = "Frustration"
        artist = "Indica Wave"
        query = "https://api.spotify.com/v1/search?query=track%3A{}+artist%3A{}&type=track&offset=0&limit=20".format(
            song_name,
            artist
        )
        response = requests.get(
            query,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(spotify_token)
            }
        )
        response_json = response.json()
        print(response_json)
        songs = response_json["tracks"]["items"]
        print("SPACE")
        print(songs)
        # only use the first song
        uri = songs[0]["uri"]

        return uri

    def add_song_to_playlist(self, playlist_id):
        """Add songs into a new Spotify playlist"""
       
        uris = self.get_songs(playlist_id)

        playlist_id = "5dGW9I9SqKZyWcOYuMtPfA"
        username = "caylaseaman"
        scope = 'playlist-modify-public'
        redirect_uri = 'https://example.com/callback/'
        token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

        sp = spotipy.Spotify(auth=token)
        
        results = sp.user_playlist_add_tracks(username, playlist_id, uris)
        # print(results)
        return results
       


if __name__ == '__main__':
    cp = CustomPlaylist()
    playlist_idR = "37i9dQZEVXbvAO1IKDPXPL"
    playlist_idD = "37i9dQZEVXcCQpauWAUHoQ"
    test = "04ksl1Qz1yLVmWRH6f67zI"
    cp.add_song_to_playlist(test)
