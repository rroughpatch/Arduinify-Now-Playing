import os, spotipy, serial, time, requests
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = os.getenv('SPOTIPY_REDIRECT_URI')
ARDUINO_COM_PORT = 'com3'

scope = 'user-read-currently-playing user-read-playback-state'

def init_spotify():
    return spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                                     client_secret=SPOTIPY_CLIENT_SECRET,
                                                     redirect_uri=SPOTIPY_REDIRECT_URI,
                                                     scope=scope))

def get_artist_with_features(track_info):
    main_artist = track_info['item']['artists'][0]['name']
    if len(track_info['item']['artists']) > 1:
        featured_artists = ", ".join(artist['name'] for artist in track_info['item']['artists'][1:])
        return f"{main_artist}, ft. {featured_artists}"
    return main_artist

sp = init_spotify()

def init_serial():
    try:
        return serial.Serial(ARDUINO_COM_PORT, 9600)
    except serial.SerialException:
        print("Failed to connect to Arduino. Check the connection.")
        return None

arduino_uno = init_serial()
time.sleep(2)

last_track_info = None
script_running = True

while script_running:
    if arduino_uno is None:
        arduino_uno = init_serial()
        time.sleep(10)
        continue

    try:
        track_info = sp.current_playback()

        if track_info and track_info['is_playing']:
            artist = get_artist_with_features(track_info)
            track_name = track_info['item']['name']
            current_track_info = f"{track_name}~{artist}"

            if current_track_info != last_track_info:
                encoded_string = current_track_info.encode()
                arduino_uno.write(encoded_string + b'+')
                print(f"Encoded String: {encoded_string}")
                last_track_info = current_track_info

            time.sleep(0.1)

        time.sleep(3.5)

    except KeyboardInterrupt:
        print("\nExiting gracefully...")
        script_running = False 

    except spotipy.SpotifyException as spotify_error:
        print(f"Spotify error: {spotify_error}")

    except requests.exceptions.RequestException as request_error:
        print(f"HTTP error: {request_error}")

    except serial.SerialException as serial_error:
        print(f"Serial communication error: {serial_error}")
        if arduino_uno:
            arduino_uno.close()
            arduino_uno = None
            time.sleep(5)

    except Exception as general_error:
        print(f"An unexpected error occurred: {general_error}")
        time.sleep(5)

if arduino_uno:
    arduino_uno.close()
    print("Arduino connection closed.")

print("Script ended.")
