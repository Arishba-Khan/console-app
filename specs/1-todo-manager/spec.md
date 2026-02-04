# Feature Specification: Todo Console – In-Memory Task Manager

**Feature Branch**: `1-todo-manager`
**Created**: 2026-02-05
**Status**: Draft
**Input**: User description: "Todo Console – In-Memory Task Manager"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Basic Task Management (Priority: P1)

As a user, I want to add, view, update, delete, and mark tasks as complete/incomplete so that I can manage my daily tasks efficiently from the command line.

**Why this priority**: This is the core functionality that enables the basic task management workflow. Without these capabilities, the application has no value.

**Independent Test**: Can be fully tested by adding tasks, viewing the list, updating task details, deleting tasks, and toggling completion status. Delivers the fundamental task management capability.

**Acceptance Scenarios**:

1. **Given** an empty task list, **When** I add a new task with title "Buy groceries", **Then** the task appears in the list with a unique ID and pending status
2. **Given** a list with multiple tasks, **When** I view the task list, **Then** all tasks are displayed with their ID, title, description (truncated if long), and status indicator
3. **Given** a task with ID 1, **When** I update its title to "Buy weekly groceries", **Then** the task's title is changed in the list
4. **Given** a task with ID 1, **When** I delete it, **Then** the task is removed from the list and no longer appears when viewing
5. **Given** a pending task with ID 1, **When** I mark it as complete, **Then** its status changes to completed and is reflected in the list view

---

### User Story 2 - Task Organization & Usability (Priority: P2)

As a user, I want to organize tasks with priorities, tags, and filtering capabilities so that I can focus on important tasks and find specific tasks quickly.

**Why this priority**: This enhances usability by allowing users to prioritize and categorize tasks, making the tool more practical for real-world usage.

**Independent Test**: Can be fully tested by creating tasks with different priorities and tags, then applying filters and sorting. Delivers enhanced organization and search capabilities.

**Acceptance Scenarios**:

1. **Given** a task being created, **When** I assign it a high priority and "work" tag, **Then** the task is saved with these properties and appears appropriately when filtered
2. **Given** multiple tasks with different priorities, **When** I sort by priority, **Then** tasks appear in order from high to low priority
3. **Given** multiple tasks with different tags, **When** I filter by a specific tag, **Then** only tasks with that tag are displayed

---

### User Story 3 - Advanced Task Features (Priority: P3)

As a user, I want to set due dates for tasks and have recurring tasks automatically created so that I can manage deadlines and routine activities effectively.

**Why this priority**: This adds intelligent features that make the tool more powerful for managing time-sensitive and repetitive tasks.

**Independent Test**: Can be fully tested by creating tasks with due dates, marking recurring tasks as complete, and observing automatic creation of next instances. Delivers deadline management and automation capabilities.

**Acceptance Scenarios**:

1. **Given** a task being created, **When** I assign it a due date, **Then** the due date is stored and visible in the task list
2. **Given** a completed recurring task, **When** it's marked as complete, **Then** a new instance of the task is automatically created for the next recurrence period
3. **Given** tasks with past due dates, **When** I view the task list, **Then** overdue tasks are visually indicated

---

### Edge Cases

- What happens when a user tries to update/delete a task that doesn't exist?
- How does the system handle invalid date formats when entering due dates?
- What occurs when a user enters a command with incorrect syntax?
- How does the system handle very long titles or descriptions that exceed display limits?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST allow users to add tasks with a required title and optional description
- **FR-002**: System MUST display all tasks with their ID, title, truncated description, and status indicator
- **FR-003**: Users MUST be able to update task title and/or description by specifying the task ID
- **FR-004**: Users MUST be able to delete tasks by specifying the task ID
- **FR-005**: Users MUST be able to toggle task completion status by specifying the task ID
- **FR-006**: System MUST assign tasks a default "Medium" priority if none is specified
- **FR-007**: Users MUST be able to assign High, Medium, or Low priority to tasks
- **FR-008**: Users MUST be able to assign multiple tags to tasks as a list of strings
- **FR-009**: System MUST allow users to search tasks by keyword in title or description
- **FR-010**: System MUST allow users to filter tasks by status (all/pending/completed), priority, or tag
- **FR-011**: System MUST allow users to sort tasks by priority (high→low), title (a-z), or creation time
- **FR-012**: Users MUST be able to assign optional due dates to tasks in YYYY-MM-DD format
- **FR-013**: System MUST support recurring tasks that automatically create new instances when completed
- **FR-014**: System MUST visually indicate overdue tasks in the task list
- **FR-015**: System MUST provide a REPL-style interface that accepts commands until 'quit' or 'exit'
- **FR-016**: System MUST provide a 'help' command that lists all available commands
- **FR-017**: System MUST provide clear error messages when invalid operations are attempted
- **FR-018**: System MUST store all tasks in memory only (no file/database persistence in Phase 1)

### Key Entities

- **Task**: Represents a single task with properties: ID (integer), title (string, required), description (string, optional), status (boolean, default false), priority (enum: High/Medium/Low, default Medium), tags (list of strings), due_date (date string, optional), recurrence_pattern (string, optional)
- **TaskService**: Manages the collection of tasks in memory, provides CRUD operations and search/filter capabilities
- **CLI**: Command-line interface that parses user commands and displays formatted output

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can add, view, update, delete, and mark tasks as complete with 100% success rate
- **SC-002**: Task operations (add, update, delete) complete within 1 second in normal conditions
- **SC-003**: Users can successfully filter and sort tasks by priority, status, or tags with 100% accuracy
- **SC-004**: 95% of users can successfully navigate the CLI and perform basic task operations on first attempt
- **SC-005**: The system correctly identifies and visually marks overdue tasks in the task list
- **SC-006**: All commands provide appropriate error messages when invalid inputs or operations are attempted