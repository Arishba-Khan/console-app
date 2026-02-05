"""
Main entry point for the Todo Console application.

This module provides the main function that initializes and runs
the application.
"""

from services.task_service import TaskService
from cli.todo_cli import TodoCLI


def main():
    """Main function that creates TaskService and TodoCLI instances and starts the application."""
    task_service = TaskService()
    cli = TodoCLI(task_service)
    cli.run()


if __name__ == "__main__":
    main()