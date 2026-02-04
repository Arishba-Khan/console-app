# Data Model for Todo Console – In-Memory Task Manager

## Task Entity

The Task entity represents a single task in the system with the following attributes:

```python
from dataclasses import dataclass
from datetime import date
from typing import List, Optional

@dataclass
class Task:
    """
    Represents a single task in the todo manager.
    
    Attributes:
        id: Unique identifier for the task (integer)
        title: Required title of the task (string)
        description: Optional description of the task (string)
        status: Boolean indicating if the task is completed (default False)
        priority: Priority level of the task (High, Medium, Low - default Medium)
        tags: List of tags associated with the task (list of strings)
        due_date: Optional due date for the task (date object)
        recurrence_pattern: Optional recurrence pattern for recurring tasks (string)
        created_at: Timestamp when the task was created (datetime)
    """
    id: int
    title: str
    description: Optional[str] = None
    status: bool = False  # False means pending, True means completed
    priority: str = "Medium"  # Values: "High", "Medium", "Low"
    tags: List[str] = None
    due_date: Optional[date] = None
    recurrence_pattern: Optional[str] = None
    created_at: date = None
    
    def __post_init__(self):
        """Initialize optional fields with default values."""
        if self.tags is None:
            self.tags = []
        if self.created_at is None:
            from datetime import date
            self.created_at = date.today()
```

## TaskService Entity

The TaskService manages the collection of tasks in memory and provides CRUD operations:

```python
from typing import List, Optional
from datetime import date

class TaskService:
    """
    Service class to manage tasks in memory.
    
    Provides methods for:
    - Creating new tasks
    - Reading/retrieving tasks
    - Updating existing tasks
    - Deleting tasks
    - Searching, filtering, and sorting tasks
    """
    
    def __init__(self):
        """Initialize the service with an empty task list."""
        self.tasks: List[Task] = []
        self.next_id: int = 1
    
    def add_task(
        self, 
        title: str, 
        description: Optional[str] = None, 
        priority: str = "Medium",
        tags: Optional[List[str]] = None,
        due_date: Optional[date] = None,
        recurrence_pattern: Optional[str] = None
    ) -> Task:
        """Add a new task to the collection."""
        pass
    
    def get_task(self, task_id: int) -> Optional[Task]:
        """Retrieve a task by its ID."""
        pass
    
    def get_all_tasks(self) -> List[Task]:
        """Get all tasks in the collection."""
        pass
    
    def update_task(
        self, 
        task_id: int, 
        title: Optional[str] = None,
        description: Optional[str] = None,
        status: Optional[bool] = None,
        priority: Optional[str] = None,
        tags: Optional[List[str]] = None,
        due_date: Optional[date] = None,
        recurrence_pattern: Optional[str] = None
    ) -> Optional[Task]:
        """Update an existing task."""
        pass
    
    def delete_task(self, task_id: int) -> bool:
        """Delete a task by its ID."""
        pass
    
    def mark_task_complete(self, task_id: int) -> bool:
        """Mark a task as complete."""
        pass
    
    def mark_task_incomplete(self, task_id: int) -> bool:
        """Mark a task as incomplete."""
        pass
    
    def search_tasks(self, keyword: str) -> List[Task]:
        """Search tasks by keyword in title or description."""
        pass
    
    def filter_tasks(
        self, 
        status: Optional[str] = None, 
        priority: Optional[str] = None, 
        tags: Optional[List[str]] = None
    ) -> List[Task]:
        """Filter tasks by status, priority, or tags."""
        pass
    
    def sort_tasks(self, sort_by: str) -> List[Task]:
        """Sort tasks by priority, title, or creation time."""
        pass
    
    def get_overdue_tasks(self) -> List[Task]:
        """Get tasks that are past their due date and not completed."""
        pass
```

## CLI Interface Entity

The CLI interface handles user input and displays formatted output:

```python
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
        pass
    
    def parse_command(self, command_line: str) -> dict:
        """Parse a command line into action and arguments."""
        pass
    
    def display_help(self):
        """Display help information for all available commands."""
        pass
    
    def display_tasks(self, tasks: List[Task]):
        """Display a list of tasks in a formatted way."""
        pass
    
    def display_task(self, task: Task):
        """Display a single task in a formatted way."""
        pass
```