"""
Unit tests for the TaskService class in the Todo Console application.

This module contains tests for all the basic TaskService functionality
to ensure proper behavior and maintain >85% code coverage.
"""

import pytest
from datetime import date
from src.services.task_service import TaskService
from src.models.task import Task


class TestTaskService:
    """Test suite for TaskService class."""

    def setup_method(self):
        """Set up a fresh TaskService instance for each test."""
        self.service = TaskService()

    def test_add_task(self):
        """Test adding a new task."""
        task = self.service.add_task("Test task")
        
        assert task.id == 1
        assert task.title == "Test task"
        assert task.status is False
        assert task.priority == "Medium"
        assert task.tags == []
        assert task.created_at == date.today()
        
        assert len(self.service.tasks) == 1
        assert self.service.tasks[0] == task

    def test_get_task_found(self):
        """Test retrieving an existing task."""
        task = self.service.add_task("Test task")
        retrieved_task = self.service.get_task(task.id)
        
        assert retrieved_task is not None
        assert retrieved_task.id == task.id
        assert retrieved_task.title == task.title

    def test_get_task_not_found(self):
        """Test retrieving a non-existing task."""
        retrieved_task = self.service.get_task(999)
        
        assert retrieved_task is None

    def test_get_all_tasks(self):
        """Test retrieving all tasks."""
        task1 = self.service.add_task("Task 1")
        task2 = self.service.add_task("Task 2")
        
        all_tasks = self.service.get_all_tasks()
        
        assert len(all_tasks) == 2
        assert task1 in all_tasks
        assert task2 in all_tasks

    def test_update_task_title(self):
        """Test updating a task's title."""
        task = self.service.add_task("Original title")
        
        updated_task = self.service.update_task(task.id, title="New title")
        
        assert updated_task is not None
        assert updated_task.title == "New title"
        assert updated_task.id == task.id  # ID should remain the same

    def test_update_task_status(self):
        """Test updating a task's status."""
        task = self.service.add_task("Test task")
        
        # Initially pending
        assert task.status is False
        
        # Update to complete
        updated_task = self.service.update_task(task.id, status=True)
        
        assert updated_task is not None
        assert updated_task.status is True

    def test_update_task_priority(self):
        """Test updating a task's priority."""
        task = self.service.add_task("Test task")
        
        updated_task = self.service.update_task(task.id, priority="High")
        
        assert updated_task is not None
        assert updated_task.priority == "High"

    def test_update_task_not_found(self):
        """Test updating a non-existing task."""
        result = self.service.update_task(999, title="New title")
        
        assert result is None

    def test_delete_task_success(self):
        """Test successfully deleting a task."""
        task = self.service.add_task("Test task")
        
        result = self.service.delete_task(task.id)
        
        assert result is True
        assert len(self.service.tasks) == 0
        assert self.service.get_task(task.id) is None

    def test_delete_task_not_found(self):
        """Test deleting a non-existing task."""
        result = self.service.delete_task(999)
        
        assert result is False

    def test_mark_task_complete(self):
        """Test marking a task as complete."""
        task = self.service.add_task("Test task")
        
        # Initially pending
        assert task.status is False
        
        result = self.service.mark_task_complete(task.id)
        
        assert result is True
        assert task.status is True

    def test_mark_task_complete_not_found(self):
        """Test marking a non-existing task as complete."""
        result = self.service.mark_task_complete(999)
        
        assert result is False

    def test_mark_task_incomplete(self):
        """Test marking a task as incomplete."""
        task = self.service.add_task("Test task")
        
        # Mark as complete first
        self.service.mark_task_complete(task.id)
        assert task.status is True
        
        # Then mark as incomplete
        result = self.service.mark_task_incomplete(task.id)
        
        assert result is True
        assert task.status is False

    def test_mark_task_incomplete_not_found(self):
        """Test marking a non-existing task as incomplete."""
        result = self.service.mark_task_incomplete(999)
        
        assert result is False

    def test_unique_ids(self):
        """Test that tasks receive unique IDs."""
        task1 = self.service.add_task("Task 1")
        task2 = self.service.add_task("Task 2")
        task3 = self.service.add_task("Task 3")

        ids = [task1.id, task2.id, task3.id]
        assert len(ids) == len(set(ids))  # All IDs should be unique
        assert ids == [1, 2, 3]  # IDs should be sequential starting from 1

    def test_search_tasks_by_title(self):
        """Test searching tasks by keyword in title."""
        task1 = self.service.add_task("Buy groceries")
        task2 = self.service.add_task("Walk the dog")
        task3 = self.service.add_task("Grocery shopping")

        results = self.service.search_tasks("grocery")

        assert len(results) == 2
        assert task1 in results
        assert task3 in results
        assert task2 not in results

    def test_search_tasks_by_description(self):
        """Test searching tasks by keyword in description."""
        task1 = self.service.add_task("Task 1", description="This is about groceries")
        task2 = self.service.add_task("Task 2", description="Something else")
        task3 = self.service.add_task("Task 3", description="More grocery notes")

        results = self.service.search_tasks("groceries")

        assert len(results) == 2
        assert task1 in results
        assert task3 in results
        assert task2 not in results

    def test_search_tasks_case_insensitive(self):
        """Test that search is case insensitive."""
        task = self.service.add_task("GROCERY shopping")

        results = self.service.search_tasks("grocery")

        assert len(results) == 1
        assert task in results

    def test_filter_tasks_by_status_pending(self):
        """Test filtering tasks by pending status."""
        pending_task = self.service.add_task("Pending task")
        completed_task = self.service.add_task("Completed task")
        self.service.mark_task_complete(completed_task.id)

        results = self.service.filter_tasks(status="pending")

        assert len(results) == 1
        assert pending_task in results
        assert completed_task not in results

    def test_filter_tasks_by_status_completed(self):
        """Test filtering tasks by completed status."""
        pending_task = self.service.add_task("Pending task")
        completed_task = self.service.add_task("Completed task")
        self.service.mark_task_complete(completed_task.id)

        results = self.service.filter_tasks(status="completed")

        assert len(results) == 1
        assert completed_task in results
        assert pending_task not in results

    def test_filter_tasks_by_priority(self):
        """Test filtering tasks by priority."""
        high_task = self.service.add_task("High priority", priority="High")
        medium_task = self.service.add_task("Medium priority", priority="Medium")
        low_task = self.service.add_task("Low priority", priority="Low")

        results = self.service.filter_tasks(priority="High")

        assert len(results) == 1
        assert high_task in results
        assert medium_task not in results
        assert low_task not in results

    def test_filter_tasks_by_tags(self):
        """Test filtering tasks by tags."""
        tagged_task = self.service.add_task("Tagged task")
        tagged_task.tags = ["work", "important"]
        untagged_task = self.service.add_task("Untagged task")
        partially_tagged_task = self.service.add_task("Partial tag task")
        partially_tagged_task.tags = ["personal"]

        results = self.service.filter_tasks(tags=["work"])

        assert len(results) == 1
        assert tagged_task in results
        assert untagged_task not in results
        assert partially_tagged_task not in results

    def test_sort_tasks_by_priority(self):
        """Test sorting tasks by priority."""
        low_task = self.service.add_task("Low priority", priority="Low")
        high_task = self.service.add_task("High priority", priority="High")
        medium_task = self.service.add_task("Medium priority", priority="Medium")

        sorted_tasks = self.service.sort_tasks("priority")

        # High priority should come first, then Medium, then Low
        assert sorted_tasks[0] == high_task
        assert sorted_tasks[1] == medium_task
        assert sorted_tasks[2] == low_task

    def test_sort_tasks_by_title(self):
        """Test sorting tasks by title."""
        task_c = self.service.add_task("Zebra")
        task_a = self.service.add_task("Apple")
        task_b = self.service.add_task("Banana")

        sorted_tasks = self.service.sort_tasks("title")

        # Should be sorted alphabetically: Apple, Banana, Zebra
        assert sorted_tasks[0] == task_a
        assert sorted_tasks[1] == task_b
        assert sorted_tasks[2] == task_c

    def test_sort_tasks_by_created_at(self):
        """Test sorting tasks by creation date."""
        task1 = self.service.add_task("First task")
        task2 = self.service.add_task("Second task")
        task3 = self.service.add_task("Third task")

        sorted_tasks = self.service.sort_tasks("created_at")

        # Tasks should be sorted by creation order
        assert sorted_tasks[0] == task1
        assert sorted_tasks[1] == task2
        assert sorted_tasks[2] == task3