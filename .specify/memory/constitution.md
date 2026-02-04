<!-- SYNC IMPACT REPORT
Version change: N/A -> 1.0.0
Modified principles: N/A (new constitution)
Added sections: All sections (new constitution)
Removed sections: N/A
Templates requiring updates: ⚠ pending review - plan-template.md, spec-template.md, tasks-template.md
Follow-up TODOs: None
-->
# Todo Console – In-Memory Task Manager Constitution

## Core Principles

### I. Library-First Architecture
Every feature starts as a well-defined module within the TodoService; Modules must be self-contained, independently testable, and properly documented; Clear purpose required - no organizational-only modules that don't serve a specific functionality.

### II. CLI Interface Standard
Every functionality must be accessible via CLI; Text in/out protocol: stdin/args → stdout, errors → stderr; Support both human-readable and structured formats as needed.

### III. Test-First Development (NON-NEGOTIABLE)
TDD mandatory: Tests written → User approved → Tests fail → Then implement; Red-Green-Refactor cycle strictly enforced; All public methods in TodoService must have unit tests with >85% coverage.

### IV. Clean Code Standards
Follow Robert C. Martin's clean code principles: meaningful names, small functions, single responsibility, DRY, SOLID where applicable; Use type hints everywhere and comprehensive docstrings (Google style) on every public class/method/function.

### V. Memory-Only Persistence (Phase 1)
Store tasks purely in memory using a simple list[Task] inside TodoService; No file/database persistence in Phase 1; This constraint ensures simplicity and speed for initial development and testing.

### VI. Extensibility & Maintainability
Use dataclasses for Task model and composition over inheritance; Project structure must be clean and standard with proper separation of concerns between models, services, CLI interface, and utilities.

## Additional Constraints

### Technology Stack Requirements
- Primary coding agent: Qwen (all code generation, refactoring, and test writing must be done by Qwen)
- Package manager: uv (preferred over pip/venv)
- Python version: 3.13+
- Target User: Developers and power users who want a fast, keyboard-driven task tracker in the terminal
- Use rich library for colorful and clear user-facing output

### Feature Implementation Order
Implement features incrementally in this exact order:
1. Basic Level: Add, View, Update, Delete, Mark Complete tasks
2. Intermediate Level: Priority, Tags/Categories, Search, Filter, Sort
3. Advanced Level: Due Date, Recurring Tasks, Reminders

## Development Workflow

### Code Quality Standards
- Use meaningful names for variables, functions, and classes
- Functions should be small with single responsibility
- Use type hints from typing import everywhere
- Write comprehensive docstrings in Google style
- Use dataclasses for Task model with field from dataclasses import
- Prefer composition over inheritance
- No global variables except for the main app instance or task store if justified
- Follow PEP 8 standards

### Testing Requirements
- Write unit tests with pytest for every public method in TodoService
- Aim for >85% coverage on core logic
- Every new feature must include corresponding tests
- Tests must run cleanly via `uv run pytest`
- All tests must be written before implementation (TDD approach)

### User Experience Guidelines
- Use clear numbered IDs for tasks (1-based, stable until delete)
- Show status indicators (e.g. [x] Done, [ ] Pending)
- Support help command listing all available commands
- Implement graceful error handling (e.g. "Task 99 not found")
- Create REPL-style loop: accept commands until "quit" or "exit"
- Ensure all user-facing output is clear, aligned, and colorful

## Governance

This constitution supersedes all other development practices for the Todo Console project. All amendments must be documented with proper approval and migration plans. All pull requests and reviews must verify compliance with these principles. Complexity must be justified with clear benefits to the user experience or system reliability.

**Version**: 1.0.0 | **Ratified**: 2026-02-05 | **Last Amended**: 2026-02-05