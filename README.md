# Scrapetube v2.9.4
This module will help you scrape youtube without the official youtube api and without selenium.

With this module you can:


* Get all videos from a Youtube channel.
* Get all videos from a playlist.
* Search youtube.
* Get detailed metadata for a single video.

# Installation

```bash
pip3 install scrapetube
```

# Usage
Here's a few short code examples.

## Get all videos for a channel
```python
import scrapetube

videos = scrapetube.get_channel("UCCezIgC97PvUuR4_gbFUs5g")

for video in videos:
    print(video['videoId'])
```

## Get all videos for a playlist
```python
import scrapetube

videos = scrapetube.get_playlist("PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU")

for video in videos:
    print(video['videoId'])
```

## Make a search
```python
import scrapetube

videos = scrapetube.get_search("python")

for video in videos:
    print(video['videoId'])
```

## Get a single video
```python
import scrapetube

video = scrapetube.get_video("m36494ifS_c")

print(video['title']['runs'][0]['text'])

# Get game info if present
if 'game_info' in video:
    print(f"Game: {video['game_info']['title']}")

# Get song info if present (list of songs)
if 'song_info' in video:
    for song in video['song_info']:
        print(f"Song: {song['title']} by {song['subtitle']}")

# Get storyboard info if present
if 'storyboard_info' in video:
    print(f"Storyboard Spec: {video['storyboard_info']['spec']}")
```

# Full Documentation

[https://scrapetube.readthedocs.io/en/latest/](https://scrapetube.readthedocs.io/en/latest/)
