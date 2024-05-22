import requests
from bs4 import BeautifulSoup
import urllib.request

# Prompt user for the Spotify playlist link
playlist_link = input("Enter the Spotify playlist link: ")

# Send a GET request to the Spotify playlist link
response = requests.get(playlist_link)

# Parse the HTML content of the playlist page
soup = BeautifulSoup(response.text, 'html.parser')

# Extract track information and download the tracks
tracks = soup.find_all('li', class_='tracklist-row')
for track in tracks:
    track_name = track.find('span', class_='track-name').text
    artist_name = track.find('a', class_='tracklist-row__artist-name-link').text
    preview_url = track.find('div', class_='react-contextmenu-wrapper')['data-testid']

    # Download the track
    if preview_url is not None:
        urllib.request.urlretrieve(preview_url, f'{track_name} - {artist_name}.mp3')
        print(f'Downloaded: {track_name} - {artist_name}')
    else:
        print(f'Skipped: {track_name} - {artist_name} (No preview available)')
