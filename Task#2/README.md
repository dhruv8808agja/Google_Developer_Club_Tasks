#Installation Steps
```
pip3 install lyrics-extractor
```
```
python setup.py install
```
```
pip3 install -r requirements.txt
```
```
./ngrok http 3000
```
```
change slack slack/events endpoint
```
```
python3 slackbot_events_api.py
```

# What it does

This is a slackbot that uses events_api from slack api's to facilitate a use case for lyrics extraction.
This project uses 'ngrok' that forwards all remote requests to a localhost port.

Basically, it forwards all post requests which contain a challenge that slack will provide on behalf of a slack-user which is nothing but a string that represents a 'song-name'.

We'll extract the song-name and use GCS to extract lyrics from a set of specified sites.

And return back it to the channel using slack_event_adapter's api.