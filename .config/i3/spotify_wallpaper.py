import spotipy
import spotipy.util as util
import sys
import requests
import uuid
import os
import subprocess
import sys, getopt

USERNAME = "b0ix1wxpnacxzobxryzbot6zk"
SECRET = "066d6581d7724519bc36f221f9aa8a66"
SCOPE = "user-library-read"
URI = "http://localhost/callback"
ID = "0c25ab63fab84ad580f86eb4fec69aba"

def get_token():
    '''
    This will open a new browser window if the developer account information
    above is correct. Follow the instructions that appear in the console dialog.
    After doing this once the token will auto refresh as long as the .cache file exists
    in the root directory.
    '''

    token = util.prompt_for_user_token(USERNAME, SCOPE, ID, SECRET, URI)
    return token


def get_current_playing(token):
    '''
    Returns information about the current playing song. If no song is currently
    playing the most recent song will be returned.
    '''
    
    spotify = spotipy.Spotify(auth=token)
    
    name= subprocess_return
    results = spotify.search(q='track:' + name, type='track')
    items = results['tracks']['items']
    if len(items) > 0:
        artist = items[0]
        image_data = artist['album']['images'][0]['url']
        os.system('convert ' + image_data + ' -crop 1280x720+70+70 -gaussian-blur 0x27 ' + "'/tmp/" + name + ".jpg'")
        os.system('feh --bg-fill ' + "'/tmp/" + name + ".jpg'")

if __name__ == "__main__":
    token = get_token()

    subprocess = subprocess.Popen("~/.config/i3/get_spotify_status.sh", shell=True, stdout=subprocess.PIPE)
    subprocess_return = str(subprocess.stdout.read())
    subprocess_return = subprocess_return.replace("'",'')
    subprocess_return = subprocess_return.replace("b",'',1)
    subprocess_return = subprocess_return.replace(" -",'',1)
    subprocess_return = subprocess_return[:-2]
    get_current_playing(token)
