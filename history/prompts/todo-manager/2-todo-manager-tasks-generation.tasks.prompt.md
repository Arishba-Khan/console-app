---
id: 2
title: "Todo Manager Tasks Generation"
stage: "tasks"
date_iso: "2026-02-05"
surface: "agent"
model: "Qwen"
feature: "todo-manager"
branch: "main"
user: "user"
command: "/sp.tasks"
labels: ["tasks", "planning", "todo-manager"]
links:
  spec: "null"
  ticket: "null"
  adr: "null"
  pr: "null"
files_yaml:
  - "D:/Arish/hackathon-03/phase-01/specs/main/tasks.md"
tests_yaml:
  - "N/A - Task definition phase"
prompt_text: |
  /sp.tasks Generate an actionable, dependency-ordered tasks.md for the feature based on available design artifacts.
  
  You **MUST** consider the user input before proceeding (if not empty).

  ## Outline

  1. **Setup**: Run `.specify/scripts/powershell/check-prerequisites.ps1 -Json` from repo root and parse FEATURE_DIR and AVAILABLE_DOCS list. All paths must be absolute. For single quotes in args like "I'm Groot", use escape syntax: e.g 'I'\''m Groot' (or double-quote if possible: "I'm Groot").

  2. **Load design documents**: Read from FEATURE_DIR:
     - **Required**: plan.md (tech stack, libraries, structure), spec.md (user stories with priorities)
     - **Optional**: data-model.md (entities), contracts/ (API endpoints), research.md (decisions), quickstart.md (test scenarios)
     - Note: Not all projects have all documents. Generate tasks based on what's available.

  3. **Execute task generation workflow**:
     - Load plan.md and extract tech stack, libraries, project structure
     - Load spec.md and extract user stories with their priorities (P1, P2, P3, etc.)
     - If data-model.md exists: Extract entities and map to user stories
     - If contracts/ exists: Map endpoints to user stories
     - If research.md exists: Extract decisions for setup tasks
     - Generate tasks organized by user story (see Task Generation Rules below)
     - Generate dependency graph showing user story completion order
     - Create parallel execution examples per user story
     - Validate task completeness (each user story has all needed tasks, independently testable)

  4. **Generate tasks.md**: Use `.specify/templates/tasks-template.md` as structure, fill with:
     - Correct feature name from plan.md
     - Phase 1: Setup tasks (project initialization)
     - Phase 2: Foundational tasks (blocking prerequisites for all user stories)
     - Phase 3+: One phase per user story (in priority order from spec.md)
     - Each phase includes: story goal, independent test criteria, tests (if requested), implementation tasks
     - Final Phase: Polish & cross-cutting concerns
     - All tasks must follow the strict checklist format (see Task Generation Rules below)
     - Clear file paths for each task
     - Dependencies section showing story completion order
     - Parallel execution examples per story
     - Implementation strategy section (MVP first, incremental delivery)

  5. **Report**: Output path to generated tasks.md and summary:
     - Total task count
     - Task count per user story
     - Parallel opportunities identified
     - Independent test criteria for each story
     - Suggested MVP scope (typically just User Story 1)
     - Format validation: Confirm ALL tasks follow the checklist format (checkbox, ID, labels, file paths)

  Context for task generation: You are an expert Spec-Driven Development (SDD) engineer using Spec-Kit Plus methodology. Your task is to create the initial task breakdown in the form of sp.tasks.md (or multiple sp.task-*.md files if preferred), which will be used by an AI coding agent (Qwen) to implement the project step-by-step. Strictly follow these rules: - Output ONLY valid Markdown content — no extra explanations, no introductions, no code. - Structure the output as a single well-organized sp.tasks.md file containing a numbered list of concrete tasks. - Each task MUST be: - Small and focused (ideally completable in one generation pass) - Sequenced logically (dependencies respected) - Clearly titled - Containing: description, acceptance criteria, files to create/modify, references to spec/constitution/plan sections - Prioritized: Basic level first, then Intermediate, then Advanced - Group tasks into major phases (using headings) that match the plan: 1. Project Setup & Infrastructure 2. Core Domain Model & Basic Service 3. Basic CLI Features (Add, View, Update, Delete, Mark Complete) 4. Intermediate Features (Priority, Tags, Search, Filter, Sort) 5. Advanced Features (Due Date, Recurring, Overdue) 6. Testing & Polish - Number tasks sequentially (1., 2., 3., …) across all phases - Use this task format for each item: ### Task N: Short Title **Description:** Clear explanation of what to do **Files to create / modify:** list of paths (e.g. src/models.py, src/service.py, tests/test_*.py) **References:** relevant sections from sp.specification and sp.plan **Acceptance Criteria:** - bullet list of testable conditions - must include: correct behavior, type hints, docstrings, clean code **Notes / Constraints:** any important rules (e.g. no new dependencies unless allowed) Project rules (never contradict): - In-memory only (no file/db persistence) - Python 3.13+, uv, type hints everywhere, Google-style docstrings, dataclasses for models - Clean project structure as defined in constitution - All code generated by Qwen — no manual coding - REPL-style CLI loop - Basic → Intermediate → Advanced order strictly respected Existing artifacts (follow exactly — do NOT contradict): Now, write the complete sp.tasks.md file content. Start with basic setup tasks and progress logically through all feature levels. Aim for 20–35 reasonably sized tasks in total to cover the entire project.

  The tasks.md should be immediately executable - each task must be specific enough that an LLM can complete it without additional context.

  ## Task Generation Rules

  **CRITICAL**: Tasks MUST be organized by user story to enable independent implementation and testing.

  **Tests are OPTIONAL**: Only generate test tasks if explicitly requested in the feature specification or if user requests TDD approach.

  ### Checklist Format (REQUIRED)

  Every task MUST strictly follow this format:

  ```text
  - [ ] [TaskID] [P?] [Story?] Description with file path
  ```

  **Format Components**:

  1. **Checkbox**: ALWAYS start with `- [ ]` (markdown checkbox)
  2. **Task ID**: Sequential number (T001, T002, T003...) in execution order
  3. **[P] marker**: Include ONLY if task is parallelizable (different files, no dependencies on incomplete tasks)
  4. **[Story] label**: REQUIRED for user story phase tasks only
     - Format: [US1], [US2], [US3], etc. (maps to user stories from spec.md)
     - Setup phase: NO story label
     - Foundational phase: NO story label  
     - User Story phases: MUST have story label
     - Polish phase: NO story label
  5. **Description**: Clear action with exact file path

  **Examples**:

  - ✅ CORRECT: `- [ ] T001 Create project structure per implementation plan`
  - ✅ CORRECT: `- [ ] T005 [P] Implement authentication middleware in src/middleware/auth.py`
  - ✅ CORRECT: `- [ ] T012 [P] [US1] Create User model in src/models/user.py`
  - ✅ CORRECT: `- [ ] T014 [US1] Implement UserService in src/services/user_service.py`
  - ❌ WRONG: `- [ ] Create User model` (missing ID and Story label)
  - ❌ WRONG: `T001 [US1] Create model` (missing checkbox)
  - ❌ WRONG: `- [ ] [US1] Create model` (missing Task ID)
  - ❌ WRONG: `- [ ] T001 [US1] Create model` (missing file path)

  ### Task Organization

  1. **From User Stories (spec.md)** - PRIMARY ORGANIZATION:
     - Each user story (P1, P2, P3...) gets its own phase
     - Map all related components to their story:
       - Models needed for that story
       - Services needed for that story
       - Endpoints/UI needed for that story
       - If tests requested: Tests specific to that story
     - Mark story dependencies (most stories should be independent)

  2. **From Contracts**:
     - Map each contract/endpoint → to the user story it serves
     - If tests requested: Each contract → contract test task [P] before implementation in that story's phase

  3. **From Data Model**:
     - Map each entity to the user story(ies) that need it
     - If entity serves multiple stories: Put in earliest story or Setup phase
     - Relationships → service layer tasks in appropriate story phase

  4. **From Setup/Infrastructure**:
     - Shared infrastructure → Setup phase (Phase 1)
     - Foundational/blocking tasks → Foundational phase (Phase 2)
     - Story-specific setup → within that story's phase

  ### Phase Structure

  - **Phase 1**: Setup (project initialization)
  - **Phase 2**: Foundational (blocking prerequisites - MUST complete before user stories)
  - **Phase 3+**: User Stories in priority order (P1, P2, P3...)
    - Within each story: Tests (if requested) → Models → Services → Endpoints → Integration
    - Each phase should be a complete, independently testable increment
  - **Final Phase**: Polish & Cross-Cutting Concerns
response_text: |
  Successfully generated a comprehensive tasks.md file for the Todo Console – In-Memory Task Manager project with:
  - 20 well-defined tasks across 6 phases
  - Proper organization by user story (US1, US2, US3)
  - Clear acceptance criteria and file paths for each task
  - Adherence to the checklist format with proper labeling
  - Dependency tracking and parallel execution opportunities
  - Focus on MVP approach starting with basic functionality
outcome: "Tasks successfully created with proper structure and adherence to project requirements"
evaluation: "Complete task breakdown with proper organization by user stories and clear implementation path"
---