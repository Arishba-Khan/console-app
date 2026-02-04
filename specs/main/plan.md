# Implementation Plan: Todo Console – In-Memory Task Manager

## 1. Title & Metadata
- **Project Name**: Todo Console – In-Memory Task Manager
- **Plan Version**: 1.0.0
- **Date**: 2026-02-05
- **Status**: Draft
- **Author**: Qwen AI Assistant

## 2. Overall Development Strategy & Milestones

### Strategy
- Follow a library-first architecture with clean separation between business logic (TodoService) and presentation (CLI)
- Implement features incrementally following the priority order defined in the specification
- Use TDD approach with pytest for all business logic
- Maintain clean code practices with type hints and comprehensive documentation

### Milestones
- **Milestone 1**: Basic task management (Add, View, Update, Delete, Mark Complete)
- **Milestone 2**: Task organization features (Priority, Tags, Search, Filter, Sort)
- **Milestone 3**: Advanced features (Due dates, Recurring tasks, Overdue indicators)
- **Milestone 4**: CLI interface refinement and error handling
- **Milestone 5**: Testing and documentation completion

## 3. High-Level Architecture & Module Breakdown

### Architecture Overview
```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   CLI Layer     │───▶│  Service Layer   │───▶│   Data Layer    │
│                 │    │                  │    │                 │
│  TodoCLI        │    │  TaskService     │    │  Task (dataclass) │
│  (argparse,     │    │  (business logic)│    │  (validation)   │
│   rich)         │    │                  │    │                 │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

### Module Breakdown
- **models/**: Contains dataclass definitions (Task)
- **services/**: Business logic implementation (TaskService)
- **cli/**: Command-line interface implementation (TodoCLI)
- **utils/**: Helper functions and constants
- **tests/**: Unit and integration tests

## 4. Key Technical Decisions & Conventions

### Technology Stack
- Python 3.13+ (as specified in constitution)
- uv package manager (as specified in constitution)
- rich library for CLI formatting (as specified in constitution)
- pytest for testing (as specified in constitution)
- dataclasses for data modeling (as specified in constitution)

### Coding Conventions
- Follow PEP 8 standards
- Use type hints everywhere
- Write comprehensive docstrings in Google style
- Use meaningful variable and function names
- Keep functions small with single responsibility
- Use composition over inheritance

### Error Handling
- Provide clear error messages to stderr
- Handle invalid inputs gracefully
- Implement proper validation for all user inputs
- Return appropriate exit codes

## 5. Incremental Implementation Roadmap

### Phase 1: Basic Level Features
1. **Create Task dataclass** with required attributes (id, title, description, status)
2. **Implement TaskService** with basic CRUD operations
   - add_task()
   - get_task()
   - get_all_tasks()
   - update_task()
   - delete_task()
   - mark_task_complete()/mark_task_incomplete()
3. **Build basic CLI interface** with REPL loop
   - Parse commands: add, view, update, delete, complete, incomplete, quit
   - Display tasks in a readable format
4. **Write unit tests** for all basic operations
5. **Implement help command** showing available commands

### Phase 2: Intermediate Level Features
1. **Extend Task model** with priority and tags attributes
2. **Enhance TaskService** with:
   - search_tasks() - search by keyword in title/description
   - filter_tasks() - filter by status, priority, tags
   - sort_tasks() - sort by priority, title, creation time
3. **Update CLI interface** to support new commands:
   - search <keyword>
   - filter --status=<status> --priority=<priority> --tag=<tag>
   - sort --by=<field> --order=<asc|desc>
4. **Write unit tests** for intermediate features

### Phase 3: Advanced Level Features
1. **Extend Task model** with due_date and recurrence_pattern attributes
2. **Enhance TaskService** with:
   - get_overdue_tasks() - identify tasks past their due date
   - handle recurring tasks - create new instances when completed
3. **Update CLI interface** to support:
   - Setting due dates when adding/updating tasks
   - Visual indication of overdue tasks
   - Recurring task management
4. **Write unit tests** for advanced features

## 6. Testing Strategy

### Unit Testing
- Test each public method in TaskService individually
- Achieve >85% code coverage on core logic
- Test edge cases and error conditions
- Use pytest fixtures for test data setup

### Integration Testing
- Test CLI interface with sample commands
- Verify end-to-end functionality
- Test error handling and validation

### Test Categories
- Basic CRUD operations
- Search and filter functionality
- Sorting capabilities
- Priority and tagging features
- Due date and recurring task handling
- Error conditions and invalid inputs

## 7. Risks, Trade-offs & Mitigations

### Risks
- **Performance**: Large numbers of tasks might slow down search/filter operations
  - *Mitigation*: Implement efficient algorithms and consider indexing if needed in future phases

- **Data Loss**: In-memory storage means tasks are lost when program exits
  - *Mitigation*: This is by design for Phase 1; persistence will be added in future phases

- **Complexity Creep**: Adding too many features too quickly
  - *Mitigation*: Strictly follow the phased implementation approach

### Trade-offs
- **Simplicity vs. Features**: Prioritizing core functionality over advanced features in Phase 1
- **Memory Usage**: Storing all tasks in memory for simplicity vs. efficiency
- **Development Speed vs. Robustness**: Balancing quick delivery with proper error handling

## 8. Next Steps after this plan

1. **Break this plan into detailed tasks** using the sp.tasks workflow
2. **Set up the project structure** with appropriate directories and initial files
3. **Create the Task dataclass** based on the data model
4. **Implement the basic TaskService** with CRUD operations
5. **Begin TDD cycle** by writing tests first, then implementing functionality
6. **Build the CLI interface** once core functionality is stable
7. **Iterate through phases** following the incremental roadmap