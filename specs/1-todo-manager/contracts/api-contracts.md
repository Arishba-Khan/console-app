# API Contracts for Todo Console – In-Memory Task Manager

## Task Management Endpoints

### Add Task
- **Method**: POST
- **Endpoint**: /tasks
- **Description**: Add a new task to the collection
- **Request Body**:
```json
{
  "title": "string (required)",
  "description": "string (optional)",
  "priority": "string (optional, default: 'Medium', values: 'High', 'Medium', 'Low')",
  "tags": "array of strings (optional)",
  "due_date": "string (optional, format: 'YYYY-MM-DD')",
  "recurrence_pattern": "string (optional)"
}
```
- **Response**:
```json
{
  "id": "integer",
  "title": "string",
  "description": "string",
  "status": "boolean (default: false)",
  "priority": "string",
  "tags": "array of strings",
  "due_date": "string or null",
  "recurrence_pattern": "string or null",
  "created_at": "date string"
}
```
- **Errors**: 400 Bad Request if title is missing

### Get Task
- **Method**: GET
- **Endpoint**: /tasks/{id}
- **Description**: Retrieve a specific task by ID
- **Parameters**: id (path parameter)
- **Response**: Same as Add Task response
- **Errors**: 404 Not Found if task doesn't exist

### Get All Tasks
- **Method**: GET
- **Endpoint**: /tasks
- **Description**: Retrieve all tasks
- **Query Parameters**:
  - status: "string (optional, values: 'all', 'pending', 'completed')"
  - priority: "string (optional, values: 'High', 'Medium', 'Low')"
  - tag: "string (optional, filter by specific tag)"
- **Response**:
```json
{
  "tasks": [
    {
      // Array of task objects as defined above
    }
  ]
}
```

### Update Task
- **Method**: PUT
- **Endpoint**: /tasks/{id}
- **Description**: Update an existing task
- **Parameters**: id (path parameter)
- **Request Body** (all fields optional):
```json
{
  "title": "string (optional)",
  "description": "string (optional)",
  "status": "boolean (optional)",
  "priority": "string (optional, values: 'High', 'Medium', 'Low')",
  "tags": "array of strings (optional)",
  "due_date": "string (optional, format: 'YYYY-MM-DD')",
  "recurrence_pattern": "string (optional)"
}
```
- **Response**: Updated task object
- **Errors**: 404 Not Found if task doesn't exist

### Delete Task
- **Method**: DELETE
- **Endpoint**: /tasks/{id}
- **Description**: Delete a task by ID
- **Parameters**: id (path parameter)
- **Response**: 204 No Content
- **Errors**: 404 Not Found if task doesn't exist

### Mark Task Complete/Incomplete
- **Method**: PATCH
- **Endpoint**: /tasks/{id}/status
- **Description**: Toggle task completion status
- **Parameters**: id (path parameter)
- **Request Body**:
```json
{
  "status": "boolean (true for complete, false for incomplete)"
}
```
- **Response**: Updated task object
- **Errors**: 404 Not Found if task doesn't exist

## Search and Filter Endpoints

### Search Tasks
- **Method**: GET
- **Endpoint**: /tasks/search
- **Description**: Search tasks by keyword in title or description
- **Query Parameters**:
  - q: "string (required, search keyword)"
- **Response**: Same as Get All Tasks

### Filter Tasks
- **Method**: GET
- **Endpoint**: /tasks/filter
- **Description**: Filter tasks by various criteria
- **Query Parameters**:
  - status: "string (optional, values: 'all', 'pending', 'completed')"
  - priority: "string (optional, values: 'High', 'Medium', 'Low')"
  - tags: "string (optional, comma-separated list of tags)"
- **Response**: Same as Get All Tasks

### Sort Tasks
- **Method**: GET
- **Endpoint**: /tasks/sort
- **Description**: Sort tasks by various criteria
- **Query Parameters**:
  - by: "string (required, values: 'priority', 'title', 'created_at')"
  - order: "string (optional, values: 'asc', 'desc', default: 'asc')"
- **Response**: Same as Get All Tasks

## Advanced Features Endpoints

### Get Overdue Tasks
- **Method**: GET
- **Endpoint**: /tasks/overdue
- **Description**: Get all tasks that are past their due date and not completed
- **Response**: Same as Get All Tasks

### Create Recurring Task Instance
- **Method**: POST
- **Endpoint**: /tasks/{id}/recurring/next
- **Description**: Create the next instance of a recurring task after completing the current one
- **Parameters**: id (path parameter)
- **Response**: New task instance object
- **Errors**: 404 Not Found if task doesn't exist or isn't recurring