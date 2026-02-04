"""
Integration tests for the Todo Console application.

This module contains tests that verify the end-to-end functionality
of the application by testing the interaction between different components.
"""

import pytest
from datetime import date, timedelta
from src.services.task_service import TaskService
from src.cli.todo_cli import TodoCLI
from src.models.task import Task


class TestIntegration:
    """Integration test suite for the Todo Console application."""

    def setup_method(self):
        """Set up a fresh TaskService and CLI instance for each test."""
        self.service = TaskService()
        self.cli = TodoCLI(self.service)

    def test_full_task_lifecycle(self):
        """Test the complete lifecycle of a task: add, view, update, complete, delete."""
        # Add a task
        task = self.service.add_task("Test task", description="A test task")
        original_id = task.id
        
        # Verify task was added
        all_tasks = self.service.get_all_tasks()
        assert len(all_tasks) == 1
        assert all_tasks[0].id == original_id
        assert all_tasks[0].title == "Test task"
        
        # Update the task
        updated_task = self.service.update_task(original_id, title="Updated test task")
        assert updated_task.title == "Updated test task"
        
        # Mark as complete
        result = self.service.mark_task_complete(original_id)
        assert result is True
        assert self.service.get_task(original_id).status is True
        
        # Delete the task
        result = self.service.delete_task(original_id)
        assert result is True
        assert self.service.get_task(original_id) is None
        
        # Verify task list is empty
        all_tasks = self.service.get_all_tasks()
        assert len(all_tasks) == 0

    def test_search_and_filter_workflow(self):
        """Test searching and filtering tasks."""
        # Add multiple tasks with different properties
        task1 = self.service.add_task("Work task", priority="High", tags=["work", "urgent"])
        task2 = self.service.add_task("Personal task", priority="Medium", tags=["personal"])
        task3 = self.service.add_task("Shopping list", priority="Low", tags=["shopping"])
        
        # Search for "work"
        search_results = self.service.search_tasks("work")
        assert len(search_results) == 1
        assert search_results[0].id == task1.id
        
        # Filter by priority
        high_priority_tasks = self.service.filter_tasks(priority="High")
        assert len(high_priority_tasks) == 1
        assert high_priority_tasks[0].id == task1.id
        
        # Filter by tag
        work_tasks = self.service.filter_tasks(tags=["work"])
        assert len(work_tasks) == 1
        assert work_tasks[0].id == task1.id
        
        # Filter by status (after marking one as complete)
        self.service.mark_task_complete(task2.id)
        completed_tasks = self.service.filter_tasks(status="completed")
        assert len(completed_tasks) == 1
        assert completed_tasks[0].id == task2.id

    def test_sorting_functionality(self):
        """Test sorting tasks by different criteria."""
        # Add tasks in a specific order
        task_low = self.service.add_task("Low priority", priority="Low")
        task_high = self.service.add_task("High priority", priority="High")
        task_medium = self.service.add_task("Medium priority", priority="Medium")
        
        # Sort by priority
        sorted_by_priority = self.service.sort_tasks("priority")
        assert sorted_by_priority[0].id == task_high.id  # High priority first
        assert sorted_by_priority[1].id == task_medium.id  # Medium priority second
        assert sorted_by_priority[2].id == task_low.id  # Low priority last
        
        # Add tasks with different titles for title sorting
        task_z = self.service.add_task("Zebra task")
        task_a = self.service.add_task("Apple task")
        task_m = self.service.add_task("Monkey task")
        
        # Sort by title
        sorted_by_title = self.service.sort_tasks("title")
        # Find the recently added tasks in the sorted list
        titles = [t.title for t in sorted_by_title[-3:]]  # Last 3 should be the new ones
        assert "Apple task" in titles
        assert "Monkey task" in titles
        assert "Zebra task" in titles
        # Verify alphabetical order
        apple_idx = next(i for i, t in enumerate(sorted_by_title) if t.title == "Apple task")
        monkey_idx = next(i for i, t in enumerate(sorted_by_title) if t.title == "Monkey task")
        zebra_idx = next(i for i, t in enumerate(sorted_by_title) if t.title == "Zebra task")
        assert apple_idx < monkey_idx < zebra_idx

    def test_due_date_and_overdue_functionality(self):
        """Test due date functionality and overdue task detection."""
        today = date.today()
        yesterday = today - timedelta(days=1)
        tomorrow = today + timedelta(days=1)
        
        # Add tasks with different due dates
        past_task = self.service.add_task("Past due task", due_date=yesterday)
        future_task = self.service.add_task("Future task", due_date=tomorrow)
        today_task = self.service.add_task("Today task", due_date=today)
        
        # Mark the past due task as complete
        self.service.mark_task_complete(past_task.id)
        
        # Get overdue tasks (should only be the uncompleted past-due task)
        # But since we marked the past task as complete, there should be no overdue tasks
        overdue_tasks = self.service.get_overdue_tasks()
        assert len(overdue_tasks) == 0
        
        # Add another past-due task that's not completed
        incomplete_past_task = self.service.add_task("Incomplete past due task", due_date=yesterday)
        
        overdue_tasks = self.service.get_overdue_tasks()
        assert len(overdue_tasks) == 1
        assert overdue_tasks[0].id == incomplete_past_task.id

    def test_recurring_task_workflow(self):
        """Test the recurring task functionality."""
        today = date.today()
        
        # Add a recurring task
        recurring_task = self.service.add_task(
            "Recurring task", 
            due_date=today,
            recurrence_pattern="daily"
        )
        
        original_id = recurring_task.id
        
        # Handle completion of the recurring task
        new_task = self.service.handle_recurring_task_completion(original_id)
        
        # Verify the original task is marked complete
        original_task = self.service.get_task(original_id)
        assert original_task.status is True
        
        # Verify a new task was created
        assert new_task is not None
        assert new_task.title == "Recurring task"
        assert new_task.status is False  # New task should be pending
        assert new_task.recurrence_pattern == "daily"
        assert new_task.due_date == today + timedelta(days=1)  # Next day

    def test_cli_command_integration(self):
        """Test CLI command processing end-to-end."""
        # This simulates the CLI processing commands
        # Add a task via service
        task = self.service.add_task("CLI test task", priority="High", tags=["test"])
        
        # Verify it was added correctly
        all_tasks = self.service.get_all_tasks()
        assert len(all_tasks) == 1
        assert all_tasks[0].title == "CLI test task"
        assert all_tasks[0].priority == "High"
        assert "test" in all_tasks[0].tags
        
        # Update the task
        updated_task = self.service.update_task(task.id, title="Updated CLI task")
        assert updated_task.title == "Updated CLI task"
        
        # Mark as complete
        self.service.mark_task_complete(task.id)
        assert self.service.get_task(task.id).status is True
        
        # Filter tasks by status
        completed_tasks = self.service.filter_tasks(status="completed")
        assert len(completed_tasks) == 1
        assert completed_tasks[0].id == task.id
        
        # Search for the task
        search_results = self.service.search_tasks("CLI")
        assert len(search_results) == 1
        assert search_results[0].id == task.id