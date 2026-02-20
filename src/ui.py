from rich.console import Console  
from rich.layout import Layout
from rich.panel import Panel
from rich.progress import ProgressBar
from rich.console import Group
from rich.text import Text
import questionary

console = Console()

def show_welcome():
    console.clear()
    console.clear()
    console.print(Panel.fit(
        "[bold magenta]LYRISH[/bold magenta] \n[dim]Reproductor con letras sincronizadas[/dim]",
        style="bold blue",
        border_style="cyan"
    ))

def request_song_selection(list_songs):
    if not list_songs:
        return None
        
    choice = questionary.select(
        "Selecciona una canción:",
        choices=list_songs + [questionary.Separator(), "Exit"],
        style=questionary.Style([
            ('qmark', 'fg:magenta bold'),    
            ('question', 'bold'),              
            ('highlighted', 'fg:cyan bold'),    
            ('selected', 'fg:green'),         
            ('pointer', 'fg:cyan bold'),
        ]),
        pointer=">"
    ).ask()

    if choice == "Exit":
        return None
    return choice

def layout_player(titulo, letras_acumuladas, tiempo_actual, total_segundos=180):
    layout = Layout()
    header = Panel(f"[bold cyan]Reproduciendo:[/bold cyan] {titulo}", style="magenta")
    
    body_text = Text()
    for i, frase in enumerate(letras_acumuladas):
        estilo = "bold white" if i == len(letras_acumuladas) - 1 else "dim white"
        body_text.append(frase + "\n", style=estilo)
    
    body = Panel(body_text, title="Lyrics", border_style="blue", expand=True)

    progreso = ProgressBar(total=total_segundos, completed=tiempo_actual, width=None)
    footer = Panel(Group(f"Tiempo: {tiempo_actual:.2f}s", progreso), title="Progress", border_style="green")

    layout.split_column(
        Layout(header, size=3),
        Layout(body, minimum_size=10),
        Layout(footer, size=5)
    )
    return layout