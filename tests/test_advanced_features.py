"""
Unit tests for the advanced features of TaskService in the Todo Console application.

This module contains tests for due date and recurring task functionality
to ensure proper behavior and maintain >85% code coverage.
"""

import pytest
from datetime import date, timedelta
from src.services.task_service import TaskService


class TestTaskServiceAdvanced:
    """Test suite for advanced TaskService functionality."""

    def setup_method(self):
        """Set up a fresh TaskService instance for each test."""
        self.service = TaskService()

    def test_get_overdue_tasks_empty(self):
        """Test getting overdue tasks when there are none."""
        overdue_tasks = self.service.get_overdue_tasks()
        
        assert len(overdue_tasks) == 0

    def test_get_overdue_tasks_with_completed_tasks(self):
        """Test that completed tasks are not returned as overdue."""
        past_date = date.today() - timedelta(days=1)
        completed_task = self.service.add_task("Completed task", due_date=past_date)
        self.service.mark_task_complete(completed_task.id)
        
        overdue_tasks = self.service.get_overdue_tasks()
        
        assert len(overdue_tasks) == 0

    def test_get_overdue_tasks_with_overdue_tasks(self):
        """Test getting overdue tasks."""
        past_date = date.today() - timedelta(days=1)
        overdue_task = self.service.add_task("Overdue task", due_date=past_date)
        
        not_overdue_task = self.service.add_task("Not overdue task", due_date=date.today() + timedelta(days=1))
        
        overdue_tasks = self.service.get_overdue_tasks()
        
        assert len(overdue_tasks) == 1
        assert overdue_task in overdue_tasks
        assert not_overdue_task not in overdue_tasks

    def test_get_overdue_tasks_with_future_tasks(self):
        """Test that future tasks are not returned as overdue."""
        future_date = date.today() + timedelta(days=1)
        future_task = self.service.add_task("Future task", due_date=future_date)
        
        overdue_tasks = self.service.get_overdue_tasks()
        
        assert len(overdue_tasks) == 0
        assert future_task not in overdue_tasks

    def test_handle_recurring_task_completion_nonexistent_task(self):
        """Test handling completion of a non-existent recurring task."""
        result = self.service.handle_recurring_task_completion(999)
        
        assert result is None

    def test_handle_recurring_task_completion_non_recurring_task(self):
        """Test handling completion of a non-recurring task."""
        task = self.service.add_task("Non-recurring task")
        
        result = self.service.handle_recurring_task_completion(task.id)
        
        assert result is None
        assert task.status is True  # Task should still be marked complete

    def test_handle_recurring_task_completion_daily_pattern(self):
        """Test handling completion of a daily recurring task."""
        today = date.today()
        original_task = self.service.add_task(
            "Daily recurring task", 
            due_date=today,
            recurrence_pattern="daily"
        )
        
        new_task = self.service.handle_recurring_task_completion(original_task.id)
        
        assert new_task is not None
        assert new_task.title == original_task.title
        assert new_task.status is False  # New task should be pending
        assert new_task.due_date == today + timedelta(days=1)  # Next day
        assert new_task.recurrence_pattern == original_task.recurrence_pattern
        assert original_task.status is True  # Original task should be complete

    def test_handle_recurring_task_completion_weekly_pattern(self):
        """Test handling completion of a weekly recurring task."""
        today = date.today()
        original_task = self.service.add_task(
            "Weekly recurring task", 
            due_date=today,
            recurrence_pattern="weekly"
        )
        
        new_task = self.service.handle_recurring_task_completion(original_task.id)
        
        assert new_task is not None
        assert new_task.title == original_task.title
        assert new_task.status is False  # New task should be pending
        assert new_task.due_date == today + timedelta(weeks=1)  # Next week
        assert new_task.recurrence_pattern == original_task.recurrence_pattern
        assert original_task.status is True  # Original task should be complete

    def test_calculate_next_occurrence_daily(self):
        """Test calculating next occurrence for daily pattern."""
        from datetime import date, timedelta
        test_date = date(2023, 1, 1)
        
        next_date = self.service._calculate_next_occurrence(test_date, "daily")
        
        expected = test_date + timedelta(days=1)
        assert next_date == expected

    def test_calculate_next_occurrence_weekly(self):
        """Test calculating next occurrence for weekly pattern."""
        from datetime import date, timedelta
        test_date = date(2023, 1, 1)
        
        next_date = self.service._calculate_next_occurrence(test_date, "weekly")
        
        expected = test_date + timedelta(weeks=1)
        assert next_date == expected

    def test_calculate_next_occurrence_monthly(self):
        """Test calculating next occurrence for monthly pattern."""
        from datetime import date, timedelta
        test_date = date(2023, 1, 1)
        
        next_date = self.service._calculate_next_occurrence(test_date, "monthly")
        
        expected = test_date + timedelta(days=30)
        assert next_date == expected

    def test_calculate_next_occurrence_yearly(self):
        """Test calculating next occurrence for yearly pattern."""
        from datetime import date, timedelta
        test_date = date(2023, 1, 1)
        
        next_date = self.service._calculate_next_occurrence(test_date, "yearly")
        
        expected = test_date + timedelta(days=365)
        assert next_date == expected

    def test_calculate_next_occurrence_invalid_pattern(self):
        """Test calculating next occurrence for invalid pattern (defaults to daily)."""
        from datetime import date, timedelta
        test_date = date(2023, 1, 1)
        
        next_date = self.service._calculate_next_occurrence(test_date, "invalid")
        
        expected = test_date + timedelta(days=1)  # Should default to daily
        assert next_date == expected