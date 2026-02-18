from utils import explore_songs
from ui import show_menu, request_song_selection
from player import MusicPlayer
from parser import parse_lrc

def main():
    songs = explore_songs("data")
    
    if not songs:
        print("No valid songs found in the directory.")
        return
    
    show_menu(songs)
    idx = request_song_selection(songs)
    
    if idx is not None:
        song_selected = songs[idx]
        print(f"\n start: {song_selected}")
        
if __name__ == "__main__":
    main()
    