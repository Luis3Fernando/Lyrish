import time
import keyboard
from utils import explore_songs
from ui import show_welcome, request_song_selection, typewriter_print, console
from player import MusicPlayer
from parser import parse_lrc

def main():
    while True:
        songs = explore_songs("data")
        if not songs: 
            print("No se encontraron canciones.")
            break

        show_welcome()
        song_selected = request_song_selection(songs)
        
        if song_selected is None:
            console.print("[bold yellow]¡Gracias por usar Lyrish! Adiós.[/bold yellow]")
            break
        
        player = MusicPlayer()
        player.player(f"data/{song_selected}.mp3")
        lyrics_data = parse_lrc(f"data/{song_selected}.lrc")
        
        console.clear()
        console.print(f"[dim]Presiona [bold white]ESPACIO[/bold white] para volver al menú[/dim]\n")
        last_phrase = ""

        try:
            while player.is_playing():
                if keyboard.is_pressed('space'):
                    player.stop()
                    console.print("\n[bold red]Canción cancelada por el usuario.[/bold red]")
                    time.sleep(1)
                    break

                current_time = player.get_time()
                current_phrase = ""

                for item in lyrics_data:
                    if current_time >= item['time']:
                        current_phrase = item['lyric']
                    else:
                        break
                
                if current_phrase and current_phrase != last_phrase:
                    typewriter_print(current_phrase)
                    last_phrase = current_phrase

                time.sleep(0.005)
                
        except KeyboardInterrupt:
            player.stop()
            break 

if __name__ == "__main__":
    main()