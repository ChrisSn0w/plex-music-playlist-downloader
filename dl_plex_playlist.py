#! /usr/bin/python3

# login to plex

from pathlib import Path

#see Getting a PlexServer Instance from https://github.com/pkkid/python-plexapi

from plexapi.server import PlexServer
baseurl = 'http://192.168.0.1:32400/'
token = 'qwertyuiop_asdfgh'
plex = PlexServer(baseurl, token)

# download playlist tracks to current folder. 
for playlist in plex.playlists(playlistType='audio'): #only output audio playlists
    tracks = playlist.items()
    for track in range(len(tracks)): #loop over tracks 
        p = Path(tracks[track].locations[0]) #get the path
        path = Path(playlist.title+"/"+p.name) #It will save each playlist in its own folder
        if path.is_file(): #skips files that already exist
            print(f'File {path} exists - skipping')
        else:
            print(f'Creating {path}')
            tracks[track].download(keep_original_name=True,savepath=playlist.title) #download the file if it doesn't exist
