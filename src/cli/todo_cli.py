"""
TodoCLI implementation for the Todo Console application.

This module defines the TodoCLI class which handles the command-line
interface for the todo manager, parsing user commands and displaying
formatted output.

.. moduleauthor:: Todo Console Team
.. versionadded:: 0.1.0
"""

from typing import List
from services.task_service import TaskService
from models.task import Task
from utils.display_utils import display_tasks, display_task
from utils.error_handlers import validate_task_id, validate_date_format, handle_error, format_error_message


class TodoCLI:
    """
    Command-line interface for the todo manager.

    Handles parsing user commands and displaying formatted output.
    """

    def __init__(self, task_service: TaskService):
        """Initialize the CLI with a task service."""
        self.task_service = task_service

    def run(self):
        """Start the REPL loop to accept commands until 'quit' or 'exit'."""
        print("Welcome to Todo Console! Type 'help' for available commands.")
        while True:
            try:
                command_line = input("> ").strip()
                if command_line.lower() in ['quit', 'exit']:
                    print("Goodbye!")
                    break
                
                result = self.parse_command(command_line)
                if result == "quit":
                    break
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except Exception as e:
                print(f"Error: {e}")

    def parse_command(self, command_line: str) -> str:
        """Parse a command line into action and arguments."""
        if not command_line:
            return ""

        parts = command_line.split()
        command = parts[0].lower()

        if command == "help":
            self.display_help()
            return ""
        elif command == "add":
            # Extract the title (everything after 'add')
            title = " ".join(parts[1:]) if len(parts) > 1 else ""
            if title:
                task = self.task_service.add_task(title=title)
                print(f"Added task #{task.id}: {task.title}")
            else:
                print("Error: Please provide a task title")
            return ""
        elif command == "view":
            tasks = self.task_service.get_all_tasks()
            self.display_tasks(tasks)
            return ""
        elif command == "update":
            if len(parts) >= 3:
                try:
                    task_id = validate_task_id(parts[1])
                    new_title = " ".join(parts[2:])
                    updated_task = self.task_service.update_task(task_id, title=new_title)
                    if updated_task:
                        print(f"Updated task #{updated_task.id}: {updated_task.title}")
                    else:
                        print(f"Task with ID {task_id} not found")
                except ValueError as e:
                    print(format_error_message(str(e)))
            else:
                print("Error: Please provide both task ID and new title")
            return ""
        elif command == "delete":
            if len(parts) >= 2:
                try:
                    task_id = validate_task_id(parts[1])
                    if self.task_service.delete_task(task_id):
                        print(f"Deleted task #{task_id}")
                    else:
                        print(f"Task with ID {task_id} not found")
                except ValueError as e:
                    print(format_error_message(str(e)))
            else:
                print("Error: Please provide a task ID")
            return ""
        elif command == "complete":
            if len(parts) >= 2:
                try:
                    task_id = validate_task_id(parts[1])
                    if self.task_service.mark_task_complete(task_id):
                        print(f"Marked task #{task_id} as complete")
                    else:
                        print(f"Task with ID {task_id} not found")
                except ValueError as e:
                    print(format_error_message(str(e)))
            else:
                print("Error: Please provide a task ID")
            return ""
        elif command == "incomplete":
            if len(parts) >= 2:
                try:
                    task_id = validate_task_id(parts[1])
                    if self.task_service.mark_task_incomplete(task_id):
                        print(f"Marked task #{task_id} as incomplete")
                    else:
                        print(f"Task with ID {task_id} not found")
                except ValueError as e:
                    print(format_error_message(str(e)))
            else:
                print("Error: Please provide a task ID")
            return ""
        elif command == "search":
            if len(parts) >= 2:
                keyword = " ".join(parts[1:])
                tasks = self.task_service.search_tasks(keyword)
                self.display_tasks(tasks)
            else:
                print("Error: Please provide a search keyword")
            return ""
        elif command == "filter":
            # Parse filter options
            status = None
            priority = None
            tags = []

            i = 1
            while i < len(parts):
                if parts[i] == "--status" and i + 1 < len(parts):
                    status = parts[i + 1]
                    i += 2
                elif parts[i] == "--priority" and i + 1 < len(parts):
                    priority = parts[i + 1]
                    i += 2
                elif parts[i] == "--tag" and i + 1 < len(parts):
                    tags.append(parts[i + 1])
                    i += 2
                else:
                    i += 1

            tasks = self.task_service.filter_tasks(status=status, priority=priority, tags=tags)
            self.display_tasks(tasks)
            return ""
        elif command == "sort":
            # Parse sort options
            sort_by = "id"  # default
            order = "asc"  # default

            i = 1
            while i < len(parts):
                if parts[i] == "--by" and i + 1 < len(parts):
                    sort_by = parts[i + 1]
                    i += 2
                elif parts[i] == "--order" and i + 1 < len(parts):
                    order = parts[i + 1]
                    i += 2
                else:
                    i += 1

            tasks = self.task_service.sort_tasks(sort_by)

            # Apply reverse if descending order is requested
            if order.lower() == "desc":
                tasks.reverse()

            self.display_tasks(tasks)
            return ""
        elif command == "add":
            # Enhanced add command to support due dates and tags
            if len(parts) < 2:
                print("Error: Please provide a task title")
                return ""

            # Parse options like --due, --priority, --tag
            title_parts = []
            due_date = None
            priority = "Medium"  # default
            tags = []

            i = 1
            while i < len(parts):
                if parts[i] == "--due" and i + 1 < len(parts):
                    due_date = parts[i + 1]
                    i += 2
                elif parts[i] == "--priority" and i + 1 < len(parts):
                    priority = parts[i + 1]
                    i += 2
                elif parts[i] == "--tag" and i + 1 < len(parts):
                    tags.append(parts[i + 1])
                    i += 2
                else:
                    title_parts.append(parts[i])
                    i += 1

            title = " ".join(title_parts)
            if title:
                # Convert due date string to date object if provided
                from datetime import datetime
                parsed_due_date = None
                if due_date:
                    if validate_date_format(due_date):
                        try:
                            parsed_due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
                        except ValueError:
                            print(format_error_message(f"Invalid date format '{due_date}'. Use YYYY-MM-DD."))
                            return ""
                    else:
                        print(format_error_message(f"Invalid date format '{due_date}'. Use YYYY-MM-DD."))
                        return ""

                task = self.task_service.add_task(
                    title=title,
                    priority=priority,
                    tags=tags,
                    due_date=parsed_due_date
                )
                print(f"Added task #{task.id}: {task.title}")
            else:
                print("Error: Please provide a task title")
            return ""
        elif command == "update":
            if len(parts) < 3:
                print("Error: Please provide both task ID and new title")
                return ""

            try:
                task_id = validate_task_id(parts[1])

                # Parse options like --due, --priority, --tag
                title_parts = []
                due_date = None
                priority = None
                tags = None

                i = 2
                while i < len(parts):
                    if parts[i] == "--due" and i + 1 < len(parts):
                        due_date = parts[i + 1]
                        i += 2
                    elif parts[i] == "--priority" and i + 1 < len(parts):
                        priority = parts[i + 1]
                        i += 2
                    elif parts[i] == "--tag" and i + 1 < len(parts):
                        if tags is None:
                            tags = []
                        tags.append(parts[i + 1])
                        i += 2
                    else:
                        title_parts.append(parts[i])
                        i += 1

                new_title = " ".join(title_parts) if title_parts else None

                # Convert due date string to date object if provided
                from datetime import datetime
                parsed_due_date = None
                if due_date:
                    if validate_date_format(due_date):
                        try:
                            parsed_due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
                        except ValueError:
                            print(format_error_message(f"Invalid date format '{due_date}'. Use YYYY-MM-DD."))
                            return ""
                    else:
                        print(format_error_message(f"Invalid date format '{due_date}'. Use YYYY-MM-DD."))
                        return ""

                updated_task = self.task_service.update_task(
                    task_id,
                    title=new_title,
                    priority=priority,
                    tags=tags,
                    due_date=parsed_due_date
                )

                if updated_task:
                    print(f"Updated task #{updated_task.id}: {updated_task.title}")
                else:
                    print(f"Task with ID {task_id} not found")
            except ValueError as e:
                print(format_error_message(str(e)))
            return ""
        elif command == "quit" or command == "exit":
            return "quit"
        else:
            print(f"Unknown command: {command}. Type 'help' for available commands.")
            return ""

    def display_help(self):
        """Display help information for all available commands."""
        help_text = """
Available commands:
  add <title>                    - Add a new task
  view                           - View all tasks
  update <id> <title>            - Update a task's title
  delete <id>                    - Delete a task
  complete <id>                  - Mark a task as complete
  incomplete <id>                - Mark a task as incomplete
  search <keyword>               - Search tasks by keyword
  filter --status=<status>       - Filter tasks by status (pending/completed)
           --priority=<priority> - Filter tasks by priority (High/Medium/Low)
           --tag=<tag>           - Filter tasks by tag
  sort --by=<field>             - Sort tasks by field (priority/title/created_at)
       --order=<asc/desc>       - Sort order (asc/desc, default asc)
  help                          - Show this help message
  quit/exit                     - Exit the application
        """
        print(help_text)

    def display_tasks(self, tasks: List[Task]):
        """Display a list of tasks in a formatted way."""
        display_tasks(tasks)

    def display_task(self, task: Task):
        """Display a single task in a formatted way."""
        display_task(task)