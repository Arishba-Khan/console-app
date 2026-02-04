"""
TaskService implementation for the Todo Console application.

This module defines the TaskService class which manages the collection
of tasks in memory and provides CRUD operations and other task management
functionalities.

.. moduleauthor:: Todo Console Team
.. versionadded:: 0.1.0
"""

from typing import List, Optional
from datetime import date
from src.models.task import Task


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
        """
        Add a new task to the collection.

        Args:
            title: The title of the task
            description: Optional description of the task
            priority: Priority level (High, Medium, Low)
            tags: Optional list of tags
            due_date: Optional due date
            recurrence_pattern: Optional recurrence pattern

        Returns:
            The newly created Task object
        """
        task = Task(
            id=self.next_id,
            title=title,
            description=description,
            priority=priority,
            tags=tags,
            due_date=due_date,
            recurrence_pattern=recurrence_pattern
        )
        self.tasks.append(task)
        self.next_id += 1
        return task

    def get_task(self, task_id: int) -> Optional[Task]:
        """
        Retrieve a task by its ID.

        Args:
            task_id: The ID of the task to retrieve

        Returns:
            The Task object if found, None otherwise
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks in the collection.

        Returns:
            A list of all Task objects
        """
        return self.tasks.copy()

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
        """
        Update an existing task.

        Args:
            task_id: The ID of the task to update
            title: New title (optional)
            description: New description (optional)
            status: New status (optional)
            priority: New priority (optional)
            tags: New tags (optional)
            due_date: New due date (optional)
            recurrence_pattern: New recurrence pattern (optional)

        Returns:
            The updated Task object if successful, None if task not found
        """
        task = self.get_task(task_id)
        if not task:
            return None

        if title is not None:
            task.title = title
        if description is not None:
            task.description = description
        if status is not None:
            task.status = status
        if priority is not None:
            task.priority = priority
        if tags is not None:
            task.tags = tags
        if due_date is not None:
            task.due_date = due_date
        if recurrence_pattern is not None:
            task.recurrence_pattern = recurrence_pattern

        return task

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID.

        Args:
            task_id: The ID of the task to delete

        Returns:
            True if the task was deleted, False if not found
        """
        task = self.get_task(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False

    def mark_task_complete(self, task_id: int) -> bool:
        """
        Mark a task as complete.

        Args:
            task_id: The ID of the task to mark complete

        Returns:
            True if successful, False if task not found
        """
        task = self.get_task(task_id)
        if task:
            task.status = True
            return True
        return False

    def mark_task_incomplete(self, task_id: int) -> bool:
        """
        Mark a task as incomplete.

        Args:
            task_id: The ID of the task to mark incomplete

        Returns:
            True if successful, False if task not found
        """
        task = self.get_task(task_id)
        if task:
            task.status = False
            return True
        return False

    def search_tasks(self, keyword: str) -> List[Task]:
        """
        Search tasks by keyword in title or description.

        Args:
            keyword: The keyword to search for

        Returns:
            A list of Task objects that match the keyword
        """
        keyword_lower = keyword.lower()
        matching_tasks = []

        for task in self.tasks:
            if (keyword_lower in task.title.lower() or
                (task.description and keyword_lower in task.description.lower())):
                matching_tasks.append(task)

        return matching_tasks

    def filter_tasks(
        self,
        status: Optional[str] = None,
        priority: Optional[str] = None,
        tags: Optional[List[str]] = None
    ) -> List[Task]:
        """
        Filter tasks by status, priority, or tags.

        Args:
            status: Filter by status ('pending', 'completed', or 'all')
            priority: Filter by priority ('High', 'Medium', 'Low')
            tags: Filter by tags (list of tag strings)

        Returns:
            A list of Task objects that match the filter criteria
        """
        filtered_tasks = []

        for task in self.tasks:
            # Check status filter
            if status:
                if status.lower() == 'pending' and task.status:
                    continue
                elif status.lower() == 'completed' and not task.status:
                    continue
                elif status.lower() != 'all' and status.lower() not in ['pending', 'completed']:
                    # Invalid status, skip
                    continue

            # Check priority filter
            if priority and task.priority != priority:
                continue

            # Check tags filter
            if tags:
                if not any(tag in task.tags for tag in tags):
                    continue

            filtered_tasks.append(task)

        return filtered_tasks

    def sort_tasks(self, sort_by: str) -> List[Task]:
        """
        Sort tasks by priority, title, or creation time.

        Args:
            sort_by: Field to sort by ('priority', 'title', 'created_at')

        Returns:
            A list of Task objects sorted by the specified field
        """
        if sort_by == 'priority':
            # Define priority order: High > Medium > Low
            priority_order = {'High': 1, 'Medium': 2, 'Low': 3}
            return sorted(self.tasks, key=lambda t: priority_order.get(t.priority, 99))
        elif sort_by == 'title':
            return sorted(self.tasks, key=lambda t: t.title.lower())
        elif sort_by == 'created_at':
            return sorted(self.tasks, key=lambda t: t.created_at)
        else:
            # Default to ID if sort_by is not recognized
            return sorted(self.tasks, key=lambda t: t.id)

    def get_overdue_tasks(self) -> List[Task]:
        """
        Get tasks that are past their due date and not completed.

        Returns:
            A list of Task objects that are overdue
        """
        from datetime import date
        overdue_tasks = []

        for task in self.tasks:
            if (task.due_date and
                not task.status and
                task.due_date < date.today()):
                overdue_tasks.append(task)

        return overdue_tasks

    def handle_recurring_task_completion(self, task_id: int) -> Optional[Task]:
        """
        Handle recurring tasks when marked complete by creating a new instance.

        Args:
            task_id: The ID of the completed recurring task

        Returns:
            The new recurring task instance if created, None otherwise
        """
        task = self.get_task(task_id)
        if not task or not task.recurrence_pattern:
            return None

        # Mark the current task as complete
        self.mark_task_complete(task_id)

        # Create a new instance based on the recurrence pattern
        # For simplicity, we'll just create a new task with the same properties
        # but reset the status and update the due date based on the pattern
        new_due_date = self._calculate_next_occurrence(task.due_date, task.recurrence_pattern)

        new_task = self.add_task(
            title=task.title,
            description=task.description,
            priority=task.priority,
            tags=task.tags,
            due_date=new_due_date,
            recurrence_pattern=task.recurrence_pattern
        )

        return new_task

    def _calculate_next_occurrence(self, last_date: date, pattern: str) -> date:
        """
        Calculate the next occurrence date based on the recurrence pattern.

        Args:
            last_date: The date of the last occurrence
            pattern: The recurrence pattern (e.g., 'daily', 'weekly', 'monthly')

        Returns:
            The calculated next occurrence date
        """
        from datetime import timedelta

        if pattern.lower() == 'daily':
            return last_date + timedelta(days=1)
        elif pattern.lower() == 'weekly':
            return last_date + timedelta(weeks=1)
        elif pattern.lower() == 'monthly':
            # Simple monthly calculation (adding ~30 days)
            return last_date + timedelta(days=30)
        elif pattern.lower() == 'yearly':
            return last_date + timedelta(days=365)
        else:
            # Default to daily if pattern is unrecognized
            return last_date + timedelta(days=1)