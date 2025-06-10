
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
7. Add `fastapi` and `uvicorn` as dependencies - for creating fastapi server
8. Add `pydantic-setting` for environment variables configuration

# Install the project as a package to avoid relative imports

`src` is the root folder in the project. Instead of relatively importing the modules, using setuptools install the project as a package and import the modules accordingly.

(Use the latest setup tool version)
More info on setup tools - 

1. Add the below line in the `pyproject.toml` file

```
        [build-system]
        requires = ["setuptools>=61.0.0"]
        build-backend = "setuptools.build_meta"

        [tool.setuptools.packages.find]
        where = ["."]
        include = ["src*"]
```
2. Run `uv sync` to update the project.

# Using the same project

1. Create the virtual environment using uv
2. Activate the venv
3. Install the dependencies using `uv sync`

# Configuration file for env variables

1. Add a new file named `config.py` and copy the contents from here
2. Use the `.env.example` for the basic envs needed for running the project

# Start the project

1. `uv run src/main.py` to start the application at the `local host` under the port `8000` (Automatically installs the packages and starts the application)