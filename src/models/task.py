"""
Task dataclass implementation for the Todo Console application.

This module defines the Task dataclass which represents a single task
in the todo manager with all its properties and behaviors.

.. moduleauthor:: Todo Console Team
.. versionadded:: 0.1.0
"""

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
        created_at: Timestamp when the task was created (date)
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
            self.created_at = date.today()