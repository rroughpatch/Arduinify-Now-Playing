# Arduinify - Spotify Now Playing Interface for Arduino

<p align="center">
  <img src="https://github.com/rroughpatch/Arduinify-Now-Playing/blob/main/assets/logo.png" alt="Project Image">
</p>

## Overview

This project allows you to create a "Now Playing" interface for Arduino, displaying real-time information about your currently playing track on Spotify. The project consists of a Python script that communicates with Spotify's API to retrieve data, and an Arduino (.ino) project that receives and displays the information.

## Features

- Real-time display of the current song, artist, and features on the song on your Arduino device.
- Python script to interact with Spotify's API and retrieve song information.
- Seamless communication between the Python script and Arduino via serial communication.

## Prerequisites

Before getting started, make sure you have the following:

- Python 3.x
- Arduino IDE
- Spotify account and an API token
- An Arduino

## Setup

Follow these steps to set up the project:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/rroughpatch/Arduinify-Now-Playing.git

2. **Navigate to the Project Directory:**
   ```bash
   cd Arduinify-Now-Playing

3. **Install Required Python Packages:**
   ```bash
   pip install -r requirements.txt

4. **Configure Spotify API Credentials:**
   - Create a Spotify Developer account and set up a new application
   - Obtain your SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET
   - Update the SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET variables in the dotenv environment

5. **Connect Arduino and Update Firmware:**
   - Open the Arduino (.ino) file in the Arduino IDE
   - Connect your Arduino board to your computer
   - Select the correct board and port in the Arduino IDE
   - Upload the firmware to your Arduino board

6. **Update Arduino Serial Port in Configuration:**
   - Open the Data.py file
   - Update the ARDUINO_COM_PORT variable with the correct serial port (e.g., "/dev/ttyUSB0" or "com3")

7. **Run the Python Script:**
    ```bash
    python Data.py




# **Enjoy your Spotify "Now Listening" Interface for Arduino!**
