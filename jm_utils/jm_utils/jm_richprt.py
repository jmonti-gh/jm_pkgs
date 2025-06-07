

# Third-Party Libs
from rich.console import Console

console = Console()


def prt_msg(kind='info', msg='Default message'):
    if kind == "ok":
        console.print(f"[bold green]#[/bold green] [green]OK >[/green]  {msg}")
        # console.print(f"[bold green]#[/bold green] [green]>[/green]  {msg}")
    elif kind == "error":
        console.print(f"[bold red]X[/bold red] [red]ERROR >[/red]  {msg}")
        # console.print(f"[bold red]X[/bold red] [red]>[/red]  {msg}")
    elif kind == "warning":
        console.print(f"[bold yellow]![/bold yellow] [yellow]Warning >[/yellow]  {msg}")
        # console.print(f"[bold yellow]![/bold yellow] [yellow]>[/yellow]  {msg}")
    elif kind == "info":
        console.print(f"[bold blue]i[/bold blue] [blue]Info >[/blue]  {msg}")
        # console.print(f"[bold blue]i[/bold blue] [blue]>[/blue]  {msg}")

def prt_title():
    pass


def demo_prt_msg():
    for knd in 'ok', 'error', 'warning', 'info':
        print()
        prt_msg(knd)


if __name__ == '__main__':
    demo_prt_msg()
