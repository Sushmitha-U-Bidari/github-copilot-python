# Sudoku Game using Flask and GitHub Copilot

## Project Overview

This project is an enhanced version of a Flask-based Sudoku web
application developed as part of a GitHub Copilot learning assignment.
The application was refactored and extended using GitHub Copilot while
ensuring that every AI-generated suggestion was manually reviewed,
tested, and refined before being accepted.

The project demonstrates modern software development practices including
modular design, backend validation, automated testing, responsive user
interface development, and responsible AI-assisted programming.

------------------------------------------------------------------------

# Project Objectives

The primary objectives of this project were to:

-   Refactor an existing Sudoku application while preserving its core
    functionality.
-   Improve code readability, maintainability, and modularity.
-   Implement additional gameplay features.
-   Improve backend request validation and error handling.
-   Enhance the overall user experience.
-   Increase automated test coverage.
-   Demonstrate responsible GitHub Copilot usage.
-   Produce a production-ready Sudoku web application.

------------------------------------------------------------------------

# Features

## Gameplay Features

### Difficulty Selection

Supports three difficulty levels:

-   Easy
-   Medium
-   Hard

Each difficulty level generates Sudoku puzzles with different numbers of
prefilled cells while ensuring a unique solution.

### Unique Sudoku Puzzle Generation

Each generated Sudoku board is validated to ensure it has exactly one
valid solution.

### Hint System

-   Reveals one correct value at a time
-   Fills only empty cells
-   Never overwrites player-entered values
-   Locks hinted cells
-   Tracks hint usage

### Check Solution

Players can validate their progress without revealing the complete
solution.

Features include:

-   Detect incorrect entries
-   Highlight correct entries
-   Continue gameplay after checking

### Automatic Puzzle Completion

When the puzzle is solved correctly:

-   Timer stops automatically
-   Congratulations message is displayed
-   Leaderboard updates automatically

### Timer

-   Starts automatically
-   Updates every second
-   Stops after successful completion

### Leaderboard

Stores the Top 10 fastest completed games.

Each record contains:

-   Player Name
-   Completion Time
-   Difficulty
-   Hint Count

Leaderboard data is stored using browser Local Storage and persists
after page refresh.

------------------------------------------------------------------------

# Validation Features

## Real-Time Validation

The application validates user input while playing and highlights
incorrect values immediately.

## Conflict Detection

Conflicts are detected in:

-   Rows
-   Columns
-   3×3 sub-grids

## Backend Validation

The Flask backend validates:

-   Missing JSON requests
-   Missing Sudoku board
-   Invalid board dimensions
-   Invalid board values
-   Malformed requests

Appropriate HTTP status codes and JSON error responses are returned.

------------------------------------------------------------------------

# Modular and Reusable Components

The project follows a modular architecture where each component has a
single responsibility.

## app.py

Responsible for:

-   Flask route handling
-   HTTP request processing
-   Request validation
-   Calling reusable Sudoku helper functions
-   Returning JSON responses

Business logic is separated from routing logic.

## sudoku_logic.py

Contains reusable Sudoku algorithms including:

-   Puzzle generation
-   Sudoku solving
-   Board validation
-   Safe move checking
-   Unique solution verification

These functions are reused throughout the application, reducing
duplicate code.

## static/main.js

Handles all client-side functionality including:

-   Timer updates
-   Hint requests
-   Solution checking
-   Live validation
-   Leaderboard management
-   Dark mode
-   User interaction

## templates/index.html

Contains only the presentation layer.

Separating presentation from backend logic improves maintainability.

------------------------------------------------------------------------

# Error Handling

The application uses defensive programming techniques to improve
reliability.

## Request Validation

Every request is validated before processing by checking:

-   JSON body exists
-   Board is provided
-   Board contains 9 rows
-   Every row contains 9 columns
-   Cell values are valid

## API Error Handling

Invalid requests return descriptive JSON responses with appropriate HTTP
status codes.

Examples include:

-   Missing JSON
-   Missing board
-   Invalid board size
-   Invalid values

## Defensive Programming

All user input is validated before Sudoku algorithms execute, preventing
runtime failures.

------------------------------------------------------------------------

# User Interface

The application includes:

-   Responsive layout
-   Dark mode
-   Improved leaderboard
-   Mobile-friendly design
-   Clean Sudoku board
-   Better user feedback

------------------------------------------------------------------------

# Technologies Used

## Backend

-   Python
-   Flask

## Frontend

-   HTML5
-   CSS3
-   JavaScript
-   Bootstrap

## Testing

-   Pytest

## Version Control

-   Git
-   GitHub

## AI Development

-   GitHub Copilot

------------------------------------------------------------------------

# Project Structure

``` text
github-copilot-python/
│
├── starter/
│   ├── app.py
│   ├── sudoku_logic.py
│   ├── requirements.txt
│   ├── instruction.md
│   ├── templates/
│   ├── static/
│   ├── tests/
│
├── README.md
├── LICENSE.txt
└── CODEOWNERS
```

------------------------------------------------------------------------

# Installation

``` bash
git clone https://github.com/Sushmitha-U-Bidari/github-copilot-python.git
cd github-copilot-python/starter

python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate

pip install -r requirements.txt
```

------------------------------------------------------------------------

# Running the Application

``` bash
python app.py
```

Open:

``` text
http://127.0.0.1:5000
```

------------------------------------------------------------------------

# Running Automated Tests

``` bash
python -m pytest -q
```

Expected output:

``` text
16 passed
```

------------------------------------------------------------------------

# Manual Testing Checklist

Verify:

-   Difficulty selection
-   New Game generation
-   Hint functionality
-   Check Solution
-   Live validation
-   Conflict highlighting
-   Puzzle completion
-   Congratulations message
-   Timer
-   Leaderboard
-   Leaderboard persistence
-   Dark mode
-   Responsive layout

------------------------------------------------------------------------

# GitHub Copilot Usage

GitHub Copilot assisted with:

-   Refactoring Python code
-   Flask route generation
-   Sudoku algorithms
-   JavaScript development
-   HTML and CSS improvements
-   Automated tests
-   Backend validation
-   Debugging

Every Copilot suggestion was manually reviewed, tested, refined, or
rejected where necessary before being merged into the final
implementation.

------------------------------------------------------------------------

# Testing Strategy

## Automated Testing

Pytest verifies:

-   Sudoku generation
-   Difficulty generation
-   Hint API
-   Check API
-   Backend validation
-   Invalid request handling

Current status:

``` text
16 tests passed
```

## Manual Testing

Verified:

-   Gameplay
-   Hint correctness
-   Timer
-   Leaderboard
-   Responsive layout
-   Dark mode
-   Local Storage persistence

## Successful Build Verification

The application was validated after every major refactoring by:

-   Running the Flask application locally
-   Executing all automated tests
-   Testing gameplay manually

This confirmed that refactoring did not introduce regressions.

------------------------------------------------------------------------

# Screenshots

Include screenshots demonstrating:

-   GitHub Copilot prompts
-   GitHub Copilot responses
-   Refactoring
-   Running application
-   Automated testing
-   Hint feature
-   Leaderboard
-   Puzzle completion

------------------------------------------------------------------------

# Documentation

Additional implementation details are available in:

``` text
starter/instruction.md
```

Code comments have been added to explain Sudoku generation, backend
validation, Flask routes, timer logic, leaderboard updates, and
JavaScript event handling.

------------------------------------------------------------------------

# Live Demo

After deployment, add your Render URL here:

``` text
https://github-copilot-python-sushmitha-u-bidari.onrender.com
```

------------------------------------------------------------------------

# Learning Outcomes

This project demonstrates experience with:

-   Flask web development
-   Python programming
-   Frontend integration
-   Automated testing using Pytest
-   Git and GitHub
-   GitHub Copilot
-   Code refactoring
-   Prompt engineering
-   Modular software design
-   Backend API validation
-   Error handling
-   Software debugging

------------------------------------------------------------------------

# Future Enhancements

Potential improvements include:

-   User authentication
-   Online leaderboard
-   Save and resume games
-   Multiple Sudoku board sizes
-   Accessibility improvements
-   Keyboard shortcuts
-   Theme customization

------------------------------------------------------------------------

# Conclusion

This project successfully transforms the original Sudoku application
into a feature-rich, responsive, modular, and well-tested web
application. GitHub Copilot supported development throughout the
project, while all generated code was carefully reviewed, tested, and
refined. The final application demonstrates good software engineering
practices, reliable backend validation, automated testing, and an
improved user experience.
