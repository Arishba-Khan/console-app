"""
Main entry point for the Todo Console application.

This module provides the main function that initializes and runs
the application.
"""

from src.services.task_service import TaskService
from src.cli.todo_cli import TodoCLI


def main():
    """Main function that creates TaskService and TodoCLI instances and starts the application."""
    task_service = TaskService()
    cli = TodoCLI(task_service)
    cli.run()


if __name__ == "__main__":
    main()