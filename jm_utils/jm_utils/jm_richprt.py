'''
jm_richprt
'''
# copilot

__version__ = "0.1.0"
__description__ = "Utilities I use frequently - Several modules"
__author__ = "Jorge Monti"
__email__ = "jorgitomonti@gmail.com"
__license__ = "MIT"
__status__ = "Development"
__python_requires__ = ">=3.11"
__last_modified__ = "2025-06-15"


# Standard Libs
from datetime import datetime

# Third-Party Libs
from rich.console import Console


console = Console()


def prtmsg(kind='inf', msg='Default message', mark=''):
    ''' Prints a message with a specific kind (ok, error, warning, info) and an optional mark.
        kind: 'ok', 'err', 'warn', 'inf'
    '''
    if kind not in ('ok', 'err', 'warn', 'inf'):
        raise ValueError(f"Invalid kind: {kind}. Must be one of 'ok', 'err', 'warn', 'info'.")
    
    if kind == "ok":
        if not mark:
            mark = '#'
        console.print(f"[bold green]{mark}[/bold green] [green]OK >[/green]  {msg}")
    elif kind == "err":
        if not mark:
            mark = 'X'
        console.print(f"\n [bold red]{mark}[/bold red] [red]ERROR >[/red]  {msg}\n")
    elif kind == "warn":
        if not mark:
            mark = '!'
        console.print(f"[bold yellow]{mark}[/bold yellow] [yellow]Warning >[/yellow]  {msg}")
    elif kind == "inf":
        if not mark:
            mark = 'i'
        console.print(f"\n [bold blue]{mark}[/bold blue] [blue]Info >[/blue]  {msg}\n")


def prt_title_log(prg, title, log='No log'):
    timestamp = datetime.now().strftime('%b %d %H:%M:%S')
    console.print(
        f'''\n[cyan]{timestamp} >[/cyan] Iniciando la ejecución de: [cyan]{prg}[/cyan]
[cyan]~~~~~[/cyan] {title} [cyan]~~~~~[/cyan]
                [cyan]>[/cyan] LOG: [cyan]{log}[/cyan]\n'''
     )
    

def prt_title(title):
    console.print(f"\n[cyan]~~~~~[/cyan] {title} [cyan]~~~~~[/cyan]\n")



def demo_prtmsg():
    for knd in 'ok', 'err', 'warn', 'inf':
        print()
        prtmsg(knd)


if __name__ == '__main__':
    demo_prtmsg()
