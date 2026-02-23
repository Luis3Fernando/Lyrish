from rich.console import Console
from rich.panel import Panel
import questionary
import time

console = Console()

def show_welcome():
    console.clear()
    console.print(Panel.fit(
        "[bold magenta]LYRISH[/bold magenta] \n[dim]Reproductor Minimalista[/dim]",
        style="bold blue",
        border_style="cyan"
    ))

def request_song_selection(list_songs):
    if not list_songs: return None
    choice = questionary.select(
        "Selecciona una canción:",
        choices=list_songs + [questionary.Separator(), "Exit"],
        style=questionary.Style([
            ('highlighted', 'fg:cyan bold'),
            ('selected', 'fg:green'),
        ]),
        pointer=">"
    ).ask()
    return None if choice == "Exit" else choice

def typewriter_print(texto, velocidad=0.05):
    """Imprime el texto letra por letra para efecto de tipografía."""
    for letra in texto:
        console.print(letra, end="", style="bold white")
        time.sleep(velocidad)
    console.print()