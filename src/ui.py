from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def show_menu(list_songs):
    table = Table(title="Lyrish - Main Menu", show_header=False, header_style="bold magenta")
    table.add_column("#", style="dim", width=4)
    table.add_column("Name", style="bold cyan")
    table.add_column("Status", justify="center")
    
    for i, song in enumerate(list_songs, start=1):
        table.add_row(str(i), song, "[green]Available[/green]")
        
    console.clear()
    console.print(Panel("Select a song to play:", style="bold blue"))
    console.print(table)
    
def request_song_selection(list_songs):
    while True:
        try:
            choice = int(console.input("Enter the number of the song to play (or 0 to exit): "))
            if choice == 0:
                return None
            elif 1 <= choice <= len(list_songs):
                return list_songs[choice - 1]
            else:
                console.print("[red]Invalid selection. Please try again.[/red]")
        except ValueError:
            console.print("[red]Please enter a valid number.[/red]")