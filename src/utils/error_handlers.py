"""
Error handling utilities for the Todo Console application.

This module provides centralized error handling and validation functions
to ensure consistent error messages and proper handling of edge cases.
"""

from typing import Union
from datetime import datetime
import sys


def validate_task_id(task_id: str) -> int:
    """
    Validate and convert a task ID string to an integer.
    
    Args:
        task_id: String representation of the task ID
        
    Returns:
        Integer representation of the task ID
        
    Raises:
        ValueError: If the task ID is not a valid integer
    """
    try:
        return int(task_id)
    except ValueError:
        raise ValueError(f"Invalid task ID: '{task_id}'. Task ID must be a number.")


def validate_date_format(date_string: str) -> bool:
    """
    Validate that a date string is in the correct format (YYYY-MM-DD).
    
    Args:
        date_string: String representation of the date
        
    Returns:
        True if the date format is valid, False otherwise
    """
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def handle_error(error: Exception, error_context: str = "") -> None:
    """
    Handle an error by printing an appropriate message to stderr.
    
    Args:
        error: The exception that occurred
        error_context: Additional context about where the error occurred
    """
    error_msg = f"Error: {str(error)}"
    if error_context:
        error_msg = f"{error_context}: {error_msg}"
    
    print(error_msg, file=sys.stderr)


def format_error_message(message: str, error_type: str = "Error") -> str:
    """
    Format an error message with a standardized prefix.
    
    Args:
        message: The error message to format
        error_type: The type of error (e.g., "Error", "Warning", "Info")
        
    Returns:
        Formatted error message
    """
    return f"{error_type}: {message}"


def validate_priority(priority: str) -> bool:
    """
    Validate that a priority value is one of the allowed values.
    
    Args:
        priority: The priority value to validate
        
    Returns:
        True if the priority is valid, False otherwise
    """
    valid_priorities = ["High", "Medium", "Low"]
    return priority in valid_priorities