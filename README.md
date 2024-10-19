# Inventory System Application

This repository contains a Python application with GitHub Actions workflow for continuous integration.

## Project Structure

- `python-app.yml`: GitHub Actions workflow file for running tests and linting

## Getting Started

### Prerequisites

- Python 3.x
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/Shilpaj1994/InventorySystem.git
   cd InventorySystem
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running Tests

Tests are automatically run by the GitHub Actions workflow. To run tests locally:

```
pytest tests
```

## Linting

This project uses flake8 for linting. To run linting locally:

```
flake8 .
```
