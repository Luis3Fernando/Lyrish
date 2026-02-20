import time
from rich.live import Live
from utils import explore_songs
from ui import show_welcome, request_song_selection, layout_player, console
from player import MusicPlayer
from parser import parse_lrc

def main():
    songs = explore_songs("data")
    
    if not songs:
        console.print("[red]No valid songs found in the directory.[/red]")
        return
    
    show_welcome()
    song_selected = request_song_selection(songs)
    
    if song_selected:
        player = MusicPlayer()
        path_audio = f"data/{song_selected}.mp3"
        path_lyrics = f"data/{song_selected}.lrc"
        
        lyrics_data = parse_lrc(path_lyrics)
        total_duration = 300 

        player.player(path_audio)
        
        lyrics_history = []
        last_phrase = ""

        try:
            with Live(console=console, screen=True, auto_refresh=True) as live:
                while player.is_playing():
                    current_time = player.get_time()
                    current_phrase = ""

                    for item in lyrics_data:
                        if current_time >= item['time']:
                            current_phrase = item['lyric']
                        else:
                            break
                    
                    if current_phrase and current_phrase != last_phrase:
                        lyrics_history.append(current_phrase)
                        last_phrase = current_phrase
                        
                        if len(lyrics_history) > 10:
                            lyrics_history.pop(0)

                    visual_layout = layout_player(
                        song_selected, 
                        lyrics_history, 
                        current_time, 
                        total_duration
                    )
                    
                    live.update(visual_layout)
                    time.sleep(0.05)

        except KeyboardInterrupt:
            player.stop()
        finally:
            console.clear()
            console.print(f"[bold magenta]Lyrish:[/bold magenta] Finalizó la reproducción de [cyan]{song_selected}[/cyan]")

if __name__ == "__main__":
    main()