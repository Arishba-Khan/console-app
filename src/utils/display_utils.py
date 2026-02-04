"""
Utility functions for displaying tasks in the Todo Console application.

This module provides functions for formatting task display with rich colors
and proper layout as specified in the requirements.
"""

from typing import List
from rich.console import Console
from rich.table import Table
from rich.text import Text
from datetime import date
from src.models.task import Task


console = Console()


def display_tasks(tasks: List[Task]):
    """Display a list of tasks in a formatted way using rich."""
    if not tasks:
        console.print("[italic]No tasks found.[/italic]")
        return

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("ID", style="dim", width=5)
    table.add_column("Status", width=10)
    table.add_column("Title", min_width=20)
    table.add_column("Priority", width=10)
    table.add_column("Tags", min_width=15)
    table.add_column("Due Date", width=12)
    table.add_column("Recurrence", width=12)

    for task in tasks:
        status = "[green][x][/green]" if task.status else "[red][ ][/red]"
        priority_color = {
            "High": "[red]High[/red]",
            "Medium": "[yellow]Medium[/yellow]",
            "Low": "[blue]Low[/blue]"
        }.get(task.priority, task.priority)

        tags_str = ", ".join(task.tags) if task.tags else ""

        due_date_str = ""
        if task.due_date:
            due_date_str = str(task.due_date)
            # Highlight overdue tasks
            if not task.status and task.due_date < date.today():
                due_date_str = f"[red]{due_date_str} (OVERDUE)[/red]"

        recurrence_str = task.recurrence_pattern if task.recurrence_pattern else ""

        table.add_row(
            str(task.id),
            status,
            task.title,
            priority_color,
            tags_str,
            due_date_str,
            recurrence_str
        )

    console.print(table)


def display_task(task: Task):
    """Display a single task in a formatted way using rich."""
    if not task:
        console.print("[italic red]Task not found.[/italic red]")
        return

    console.print(f"[bold]{task.id}.[/bold] {'[green][x][/green]' if task.status else '[red][ ][/red]'} {task.title}")

    if task.description:
        console.print(f"  [italic]{task.description}[/italic]")

    priority_color = {
        "High": "[red]High[/red]",
        "Medium": "[yellow]Medium[/yellow]",
        "Low": "[blue]Low[/blue]"
    }.get(task.priority, task.priority)
    console.print(f"  [bold]Priority:[/bold] {priority_color}")

    if task.tags:
        console.print(f"  [bold]Tags:[/bold] {', '.join(task.tags)}")

    if task.due_date:
        due_date_str = str(task.due_date)
        if not task.status and task.due_date < date.today():
            due_date_str = f"[red]{due_date_str} (OVERDUE)[/red]"
        console.print(f"  [bold]Due:[/bold] {due_date_str}")

    if task.recurrence_pattern:
        console.print(f"  [bold]Recurrence:[/bold] {task.recurrence_pattern}")

    console.print(f"  [bold]Created:[/bold] {task.created_at}")