from slackeventsapi import SlackEventAdapter
from slackclient import SlackClient
import json

##########lyricsLibraryPart
try:
    from lyrics_extractor.lyrics import Song_Lyrics
    from lyrics_extractor.settings import GCS_API_KEY, GCS_ENGINE_ID
except:
    from lyrics_extractor import Song_Lyrics

    # Assign credentials by replacing None for GCS_API_KEY and GCS_ENGINE_ID
    GCS_API_KEY = "AIzaSyAcEySS1hs3jQMacEIuplph4bNduO96iok"
    GCS_ENGINE_ID = "006481353291060610324:nu4qc-yea-c"
import unittest
import time

if GCS_API_KEY == None or GCS_ENGINE_ID == None:
        print("Error in getting the Google custom search API key and/or Engine ID.")
        raise TypeError

try:
    extract_lyrics = Song_Lyrics(GCS_API_KEY, GCS_ENGINE_ID)
except:
    print("Incorrect API key passed for Google custom search and/or Engine ID.")
    raise ValueError

############


tokens = {}
with open('configs.json') as json_data:
    tokens = json.load(json_data)

slack_events_adapter = SlackEventAdapter(tokens.get("slack_signing_secret"), "/slack/events")
slack_client = SlackClient(tokens.get("slack_bot_token"))


@slack_events_adapter.on("message")
def handle_message(event_data):
    message = event_data["event"]
    if message.get("subtype") is None:
        song_title, song_lyrics = extract_lyrics.get_lyrics(message.get('text'))
        
        channel = message["channel"]
        #send_message = "Responding to `BOT TEST` message sent by user <@%s>" % message["user"]
        slack_client.api_call("chat.postMessage", channel=channel, text=song_lyrics)


@slack_events_adapter.on("error")
def error_handler(err):
    print("ERROR: " + str(err))


slack_events_adapter.start(port=3000)