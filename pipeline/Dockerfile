# what we base our docker image from 
# (slim) a smaller Docker image with fewer pre-installed system packages (smaller size)
# Base image: lightweight Python runtime
FROM python:3.13.11-slim

# Copy uv binary from official uv image (multi-stage build pattern)
# This allows us to use uv to create a virtual environment and install dependencies.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/ 

# Set the working directory in the Docker image to /code. This is where the application code will be 
# copied and executed.
WORKDIR /code

# Set the PATH environment variable to include the virtual environment's bin directory. 
# This allows us to run Python and installed packages from the virtual environment without needing 
# to specify the full path.
ENV PATH="/code/.venv/bin:$PATH"


# Copy dependency definitions first (enables Docker layer caching)
COPY pyproject.toml .python-version uv.lock ./

# Create a virtual environment in the Docker image and install dependencies from pyproject.toml 
# using the versions pinned in uv.lock files.
# Add a virtual environment to the Docker image, which is a self-contained Python environment that 
# allows you to install packages without affecting the system-wide Python installation.
RUN uv sync --locked


# copy the file pipeline.py in the current folder into the current working directory in Docker Container
# Copy application code into container
COPY pipeline.py . 

# entrypoint makes it faster
# ENTRYPOINT ["uv", "run", "python", "pipeline.py" ]
# Run the script when container starts 
ENTRYPOINT ["python", "pipeline.py" ] 


