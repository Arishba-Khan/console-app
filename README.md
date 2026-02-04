# Todo Console – In-Memory Task Manager

A CLI-based task manager that stores tasks in memory only. Perfect for quick task tracking without persistence requirements.

## Features

- Add, view, update, delete, and mark tasks as complete/incomplete
- Organize tasks with priorities and tags
- Search, filter, and sort tasks
- Set due dates and manage recurring tasks
- Colorful terminal interface
- Overdue task detection
- Rich command-line interface with extensive error handling

## Installation

This project requires Python 3.13+ and uv package manager.

1. Clone the repository
2. Install dependencies with `uv sync`
3. Run with `uv run todo`

## Usage

```bash
todo                    # Start the interactive CLI
todo --help            # Show available commands
```

### Available Commands:

#### Basic Operations:
- `add "task title"` - Add a new task
- `add "task title" --priority=High --due=2026-12-31 --tag=work` - Add a task with options
- `view` - View all tasks
- `update <id> "new title"` - Update a task
- `update <id> "new title" --priority=Low --due=2026-12-31` - Update a task with options
- `delete <id>` - Delete a task
- `complete <id>` - Mark task as complete
- `incomplete <id>` - Mark task as incomplete
- `help` - Show help
- `quit` or `exit` - Exit the application

#### Advanced Operations:
- `search <keyword>` - Search tasks by keyword in title or description
- `filter --status=pending --priority=high --tag=work` - Filter tasks by multiple criteria
- `sort --by=priority --order=desc` - Sort tasks (by priority, title, or created_at)
- `view` - View all tasks with rich formatting showing status, priority, tags, due dates, and recurrence

## Development

To contribute to this project:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests for new functionality
5. Run the test suite: `python -m pytest`
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

## Architecture

The application follows a clean architecture with three main layers:

- **CLI Layer**: Handles user input/output and command parsing
- **Service Layer**: Contains business logic for task management
- **Data Layer**: Defines the Task model using dataclasses

## Testing

Run the full test suite with:
```bash
python -m pytest
```

To run with coverage:
```bash
python -m pytest --cov=src
```