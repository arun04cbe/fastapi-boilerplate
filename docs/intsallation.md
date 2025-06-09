
# Dependencies to be installed
1. uv - Package Management
2. Python - 3.12.4
3. IDE - VS Code


# VS Code Extensions
1. Python (Microsoft)

# Steps Followed
1. Add a `.python-version` file - 3.12.4
2. `uv init` for initializing a uv python project
3. `uv venv` for creating a virtual environment
4. `.venv/Scripts/activate` to activalte the virtual environment
5. Delete the `main.py` file created by uv
6. Create a separate folder `src` and create a file `main.py`
7. Add `fastapi` and `uvicorn` as dependencies.

# Start the project

1. `uv run src/main.py` to start the application at the local host under the port `8000` (Automatically installs the packages and starts the application)