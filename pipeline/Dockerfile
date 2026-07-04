# what we base our docker image from 
# (slim) a smaller Docker image with fewer pre-installed system packages (smaller size)
FROM python:3.13.11-slim

# Copy uv binary from official uv image (multi-stage build pattern)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

WORKDIR /code
ENV PATH="/code/.venv/bin:$PATH"

COPY pyproject.toml .python-version uv.lock ./
# RUN uv sync --locked download dependencies from the uv.lock file, the dependencies we have installed in the uv.lock is the same as our virtual env
RUN uv sync --locked
# copy the file pipeline.py in the current folder into the current working directory in Docker Container
COPY pipeline.py . 


# entrypoint makes it faster
# ENTRYPOINT ["uv", "run", "python", "pipeline.py" ] 
ENTRYPOINT ["python", "pipeline.py" ] 


