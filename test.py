import scrapetube
import json

import sys
import io

# Fix for Windows console emoji printing
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def test_functionality():
    print("=== Testing scrapetube Functionality ===\n")

    # 1. Test get_video with the provided ID
    video_id = "sfjby3-A5m4"
    print(f"--- Testing get_video for ID: {video_id} ---")
    try:
        video = scrapetube.get_video(video_id)
        print(f"Title: {video['title']['runs'][0]['text']}")
        
        if 'game_info' in video:
            print(f"Game Info: {video['game_info']['title']} ({video['game_info']['subtitle']})")
        else:
            print("Game Info: Not found")
            
        if 'song_info' in video:
            print(f"Song Info: Found {len(video['song_info'])} songs")
        else:
            print("Song Info: Not found")
            
        if 'storyboard_info' in video:
            print(f"Storyboard Spec: {video['storyboard_info']['spec'][:50]}...")
        else:
            print("Storyboard Info: Not found")
    except Exception as e:
        print(f"Error in get_video: {e}")
    print()

    # 2. Test get_video with a song (to verify song_info)
    song_video_id = "m36494ifS_c"
    print(f"--- Testing get_video for Song ID: {song_video_id} ---")
    try:
        video = scrapetube.get_video(song_video_id)
        if 'song_info' in video:
            print(f"Song Info: Found {len(video['song_info'])} songs")
            for i, song in enumerate(video['song_info'][:2], 1):
                print(f"  {i}. {song['title']} - {song['subtitle']} ({song.get('secondary_subtitle', 'N/A')})")
        else:
            print("Song Info: Not found")
    except Exception as e:
        print(f"Error in get_video (song): {e}")
    print()

    # 3. Test get_channel
    channel_id = "UC9-y-6csu5WGm29I7JiwpnA" # MrBeast
    print(f"--- Testing get_channel for ID: {channel_id} (limit 5) ---")
    try:
        videos = scrapetube.get_channel(channel_id, limit=5)
        count = 0
        for video in videos:
            count += 1
            print(f"  {count}. {video['videoId']}")
        print(f"Fetched {count} videos from channel.")
    except Exception as e:
        print(f"Error in get_channel: {e}")
    print()

    # 4. Test get_search
    query = "python programming"
    print(f"--- Testing get_search for query: '{query}' (limit 5) ---")
    try:
        videos = scrapetube.get_search(query, limit=5)
        count = 0
        for video in videos:
            count += 1
            print(f"  {count}. {video['videoId']}")
        print(f"Fetched {count} search results.")
    except Exception as e:
        print(f"Error in get_search: {e}")
    print()

    # 5. Test get_playlist
    playlist_id = "PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU" # Corey Schafer Python
    print(f"--- Testing get_playlist for ID: {playlist_id} (limit 5) ---")
    try:
        videos = scrapetube.get_playlist(playlist_id, limit=5)
        count = 0
        for video in videos:
            count += 1
            print(f"  {count}. {video['videoId']}")
        print(f"Fetched {count} videos from playlist.")
    except Exception as e:
        print(f"Error in get_playlist: {e}")
    print()

if __name__ == "__main__":
    test_functionality()
