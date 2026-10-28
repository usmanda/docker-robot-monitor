from datetime import datetime

from rich.console import Console
from rich.progress_bar import ProgressBar
from rich.table import Table


console = Console()


def battery_status(level):
    if not 0 <= level <= 100:
        raise ValueError("Battery percentage must be between 0 and 100.")

    if level >= 50:
        return "Ready for a mission", "green"
    elif level >= 20:
        return "Plan to recharge soon", "yellow"
    else:
        return "Return to charging station", "red"


def main():
    console.print("\n[bold cyan]Robot Battery Monitor[/bold cyan]")

    try:
        level = float(console.input("Enter battery percentage (0–100): "))
        status, colour = battery_status(level)
    except ValueError:
        console.print("[red]Please enter a number between 0 and 100.[/red]")
        return

    table = Table(title="Robot-01 Battery Report")
    table.add_column("Item", style="cyan")
    table.add_column("Reading")

    table.add_row("Battery", f"{level:g}%")
    table.add_row("Status", f"[{colour}]{status}[/{colour}]")
    table.add_row("Checked at", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    console.print(table)
    console.print(
        ProgressBar(
            total=100,
            completed=level,
            complete_style=colour,
            finished_style=colour,
        )
    )


if __name__ == "__main__":
    main()