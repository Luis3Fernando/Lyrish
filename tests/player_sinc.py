import time
from src.parser import parse_lrc
from src.player import MusicPlayer

def test_sinc():
    player = MusicPlayer()
    path_audio = 'data/01 - Hush.mp3'
    path_lyrics = 'data/01 - Hush.lrc'
    lyrics = parse_lrc(path_lyrics)
    
    if not lyrics:
        print("No lyrics found. Test cannot proceed.")
        
    player.player(path_audio)
    
    print("Starting playback...")
    
    try:
        while player.is_playing():
            time_now = player.get_time()
            phrase_show = ""
            
            for item in lyrics:
                if time_now >= item['time']:
                    phrase_show = item['lyric']
                else:
                    break
                
            print(f"Time: {time_now:.2f} - Lyric: {phrase_show}")
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("Test interrupted by user.")
        
if __name__ == "__main__":
    test_sinc()
