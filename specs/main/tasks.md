# Todo Console – In-Memory Task Manager - Tasks

## Phase 1: Project Setup & Infrastructure

### Task 1: Create project structure
**Description:** Set up the initial project structure with all required directories
**Files to create / modify:** 
- pyproject.toml
- README.md
- .gitignore
- src/__init__.py
- src/models/__init__.py
- src/services/__init__.py
- src/cli/__init__.py
- src/utils/__init__.py
- tests/__init__.py
**References:** Implementation plan section 3 (Module Breakdown), Constitution (Technology Stack Requirements)
**Acceptance Criteria:**
- [ ] Project structure follows the architecture overview in plan
- [ ] pyproject.toml includes required dependencies (rich, pytest)
- [ ] .gitignore contains appropriate entries for Python projects
- [ ] All __init__.py files created to make directories Python packages
**Notes / Constraints:** Use uv for package management as specified in constitution

### Task 2: Install and configure dependencies
**Description:** Set up the Python project with uv and install required dependencies
**Files to create / modify:** 
- pyproject.toml
- uv.lock (generated)
**References:** Constitution (Technology Stack Requirements)
**Acceptance Criteria:**
- [ ] pyproject.toml specifies Python 3.13+ requirement
- [ ] rich library is included as a dependency
- [ ] pytest is included as a dev dependency
- [ ] uv.lock file is generated with resolved dependencies
**Notes / Constraints:** Follow the technology stack requirements from constitution

## Phase 2: Core Domain Model & Basic Service

### Task 3: Create Task dataclass
**Description:** Implement the Task dataclass with all required attributes
**Files to create / modify:** 
- src/models/task.py
**References:** Data model document, FR-001, FR-002, FR-006, FR-012, FR-013
**Acceptance Criteria:**
- [ ] Task class implemented as a dataclass with type hints
- [ ] Includes all required attributes: id, title, description, status, priority, tags, due_date, recurrence_pattern, created_at
- [ ] Proper default values for optional fields
- [ ] __post_init__ method to initialize optional fields with defaults
- [ ] Comprehensive docstring in Google style
**Notes / Constraints:** Follow dataclass implementation decision from research.md

### Task 4: Create TaskService skeleton
**Description:** Implement the basic TaskService class with in-memory storage
**Files to create / modify:** 
- src/services/task_service.py
**References:** Data model document, Implementation plan section 5 (Phase 1)
**Acceptance Criteria:**
- [ ] TaskService class with proper initialization
- [ ] In-memory storage using list[Task] as specified in constitution
- [ ] next_id counter for generating unique IDs
- [ ] Proper type hints and Google-style docstrings
**Notes / Constraints:** Follow memory-only persistence requirement from constitution

## Phase 3: Basic CLI Features (User Story 1 - Basic Task Management)

### Task 5: [US1] Implement basic TaskService methods
**Description:** Implement core CRUD operations for TaskService
**Files to create / modify:** 
- src/services/task_service.py
**References:** Data model document, User Story 1, FR-001, FR-003, FR-004, FR-005
**Acceptance Criteria:**
- [ ] add_task method creates new task with unique ID and default values
- [ ] get_task method retrieves task by ID
- [ ] get_all_tasks method returns all tasks
- [ ] update_task method updates specified fields of a task
- [ ] delete_task method removes task by ID
- [ ] mark_task_complete method sets task status to True
- [ ] mark_task_incomplete method sets task status to False
- [ ] Proper error handling for invalid task IDs
- [ ] Type hints and Google-style docstrings for all methods
**Notes / Constraints:** Follow basic level features from implementation plan

### Task 6: [US1] Create TodoCLI skeleton
**Description:** Implement the basic CLI class structure
**Files to create / modify:** 
- src/cli/todo_cli.py
**References:** Data model document, Implementation plan section 5 (Phase 1)
**Acceptance Criteria:**
- [ ] TodoCLI class with proper initialization accepting TaskService
- [ ] run method that starts the REPL loop
- [ ] parse_command method to handle user input
- [ ] display_tasks and display_task methods for output
- [ ] Type hints and Google-style docstrings
**Notes / Constraints:** Follow CLI interface standard from constitution

### Task 7: [US1] Implement basic CLI commands
**Description:** Add support for basic commands: add, view, update, delete, complete, incomplete, quit
**Files to create / modify:** 
- src/cli/todo_cli.py
**References:** User Story 1, FR-015, FR-016
**Acceptance Criteria:**
- [ ] Add command to create new tasks
- [ ] View command to display all tasks
- [ ] Update command to modify existing tasks
- [ ] Delete command to remove tasks
- [ ] Complete/incomplete commands to toggle task status
- [ ] Quit command to exit the application
- [ ] Help command to show available commands
- [ ] Proper error handling and user-friendly messages
**Notes / Constraints:** Follow REPL-style interface requirement from constitution

### Task 8: [US1] Implement task display formatting
**Description:** Format task display with ID, title, description, and status indicator
**Files to create / modify:** 
- src/cli/todo_cli.py
- src/utils/__init__.py
- src/utils/display_utils.py (new)
**References:** User Story 1, FR-002
**Acceptance Criteria:**
- [ ] Tasks displayed with ID, title, truncated description, and status indicator
- [ ] Status shown as [x] for completed and [ ] for pending
- [ ] Rich library used for formatting as specified in constitution
- [ ] Proper handling of long descriptions with truncation
**Notes / Constraints:** Use rich library for colorful output as specified in constitution

### Task 9: [US1] Create main application entry point
**Description:** Create the main entry point that initializes and runs the application
**Files to create / modify:** 
- src/main.py
- src/__init__.py
**References:** Implementation plan section 5 (Phase 1)
**Acceptance Criteria:**
- [ ] Main function that creates TaskService and TodoCLI instances
- [ ] Proper initialization of the application
- [ ] Starts the CLI REPL loop
- [ ] Entry point configured in pyproject.toml
**Notes / Constraints:** Follow library-first architecture from constitution

### Task 10: [US1] Write basic unit tests
**Description:** Create unit tests for basic TaskService functionality
**Files to create / modify:** 
- tests/test_task_service.py
**References:** User Story 1, Testing Strategy section in plan
**Acceptance Criteria:**
- [ ] Tests for add_task method
- [ ] Tests for get_task and get_all_tasks methods
- [ ] Tests for update_task method
- [ ] Tests for delete_task method
- [ ] Tests for mark_task_complete and mark_task_incomplete methods
- [ ] Tests cover edge cases like invalid task IDs
- [ ] Test coverage >85% for core logic
**Notes / Constraints:** Follow TDD approach as specified in constitution

## Phase 4: Intermediate Features (User Story 2 - Task Organization & Usability)

### Task 11: [US2] Enhance TaskService with search, filter, and sort
**Description:** Implement search, filter, and sort functionality in TaskService
**Files to create / modify:** 
- src/services/task_service.py
**References:** User Story 2, FR-009, FR-010, FR-011
**Acceptance Criteria:**
- [ ] search_tasks method that finds tasks by keyword in title/description
- [ ] filter_tasks method that filters by status, priority, or tags
- [ ] sort_tasks method that sorts by priority, title, or creation time
- [ ] Proper type hints and Google-style docstrings
**Notes / Constraints:** Follow intermediate level features from implementation plan

### Task 12: [US2] Add CLI commands for search, filter, and sort
**Description:** Implement CLI commands for search, filter, and sort functionality
**Files to create / modify:** 
- src/cli/todo_cli.py
**References:** User Story 2, FR-009, FR-010, FR-011
**Acceptance Criteria:**
- [ ] Search command to find tasks by keyword
- [ ] Filter command with options for status, priority, and tags
- [ ] Sort command with options for different sorting criteria
- [ ] Proper command parsing and error handling
**Notes / Constraints:** Follow CLI interface standard from constitution

### Task 13: [US2] Write tests for intermediate features
**Description:** Create unit tests for search, filter, and sort functionality
**Files to create / modify:** 
- tests/test_task_service.py
**References:** User Story 2, Testing Strategy section in plan
**Acceptance Criteria:**
- [ ] Tests for search_tasks method
- [ ] Tests for filter_tasks method
- [ ] Tests for sort_tasks method
- [ ] Test coverage >85% for new functionality
**Notes / Constraints:** Follow TDD approach as specified in constitution

## Phase 5: Advanced Features (User Story 3 - Advanced Task Features)

### Task 14: [US3] Enhance TaskService with due date and recurring task functionality
**Description:** Implement overdue detection and recurring task handling
**Files to create / modify:** 
- src/services/task_service.py
**References:** User Story 3, FR-012, FR-013, FR-014
**Acceptance Criteria:**
- [ ] get_overdue_tasks method to identify tasks past their due date
- [ ] Logic to handle recurring tasks when marked complete
- [ ] Proper date handling and comparison
- [ ] Type hints and Google-style docstrings
**Notes / Constraints:** Follow advanced level features from implementation plan

### Task 15: [US3] Add CLI commands for due dates and recurring tasks
**Description:** Implement CLI commands to set due dates and manage recurring tasks
**Files to create / modify:** 
- src/cli/todo_cli.py
**References:** User Story 3, FR-012, FR-013, FR-014
**Acceptance Criteria:**
- [ ] Ability to set due dates when adding/updating tasks
- [ ] Visual indication of overdue tasks in display
- [ ] Support for recurring task patterns
- [ ] Proper date format validation
**Notes / Constraints:** Follow CLI interface standard from constitution

### Task 16: [US3] Update display formatting for advanced features
**Description:** Modify task display to show due dates and indicate overdue tasks
**Files to create / modify:** 
- src/cli/todo_cli.py
- src/utils/display_utils.py
**References:** User Story 3, FR-014
**Acceptance Criteria:**
- [ ] Due dates displayed for tasks that have them
- [ ] Overdue tasks visually indicated (e.g., with color or symbol)
- [ ] Rich library used for formatting as specified in constitution
**Notes / Constraints:** Use rich library for colorful output as specified in constitution

### Task 17: [US3] Write tests for advanced features
**Description:** Create unit tests for due date and recurring task functionality
**Files to create / modify:** 
- tests/test_task_service.py
**References:** User Story 3, Testing Strategy section in plan
**Acceptance Criteria:**
- [ ] Tests for get_overdue_tasks method
- [ ] Tests for recurring task handling
- [ ] Test coverage >85% for new functionality
- [ ] Tests for edge cases like invalid date formats
**Notes / Constraints:** Follow TDD approach as specified in constitution

## Phase 6: Testing & Polish

### Task 18: Implement comprehensive error handling
**Description:** Add robust error handling throughout the application
**Files to create / modify:** 
- src/services/task_service.py
- src/cli/todo_cli.py
- src/utils/error_handlers.py (new)
**References:** FR-017, Edge Cases in spec
**Acceptance Criteria:**
- [ ] Clear error messages for invalid operations
- [ ] Proper handling of non-existent task IDs
- [ ] Validation for date formats and other inputs
- [ ] Error messages sent to stderr as appropriate
**Notes / Constraints:** Follow error handling conventions from implementation plan

### Task 19: Add integration tests
**Description:** Create integration tests covering end-to-end functionality
**Files to create / modify:** 
- tests/test_integration.py (new)
**References:** Testing Strategy section in plan
**Acceptance Criteria:**
- [ ] Tests covering the complete workflow from task creation to deletion
- [ ] Tests for CLI command processing
- [ ] Tests for error conditions and edge cases
**Notes / Constraints:** Follow TDD approach as specified in constitution

### Task 20: Documentation and final polish
**Description:** Complete documentation and perform final code review
**Files to create / modify:** 
- README.md
- src/models/task.py (docstring improvements)
- src/services/task_service.py (docstring improvements)
- src/cli/todo_cli.py (docstring improvements)
**References:** All specifications and implementation plan
**Acceptance Criteria:**
- [ ] README.md includes usage instructions
- [ ] All public methods have comprehensive docstrings
- [ ] Code follows clean code principles from constitution
- [ ] All type hints are correct and complete
**Notes / Constraints:** Follow clean code standards from constitution

## Dependencies

- User Story 1 (Basic Task Management) must be completed before User Story 2 and 3
- User Story 2 (Task Organization) depends on foundational components but can be developed in parallel with User Story 3 after US1 completion
- User Story 3 (Advanced Features) depends on the basic functionality from User Story 1

## Parallel Execution Examples

- Tasks 11 and 12 can be developed in parallel ([P] tasks) as they work on different aspects of the same feature
- Tasks 14 and 15 can be developed in parallel ([P] tasks) as they implement backend and frontend for the same feature
- Unit tests (Tasks 10, 13, 17) can be developed alongside their respective feature implementations

## Implementation Strategy

- Start with MVP focusing on User Story 1 (Basic Task Management)
- Deliver incrementally by completing each user story fully before moving to the next
- Follow TDD approach with tests written before implementation
- Maintain >85% test coverage as specified in the constitution