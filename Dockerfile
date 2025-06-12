FROM ghcr.io/astral-sh/uv:0.7.12-python3.13-alpine

# This is just so `stdout` and `stderr` are unbuffered by default
# https://docs.python.org/3/using/cmdline.html#envvar-PYTHONUNBUFFERED
# This allows statements and log messages to immediately appear in the Knative logs
ENV PYHTONUNBUFFERED=1

WORKDIR /app

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1

# Copy from the cache instead of linking since it's a mounted volume
ENV UV_LINK_MODE=copy

# Install the project's dependencies using the lockfile and settings
RUN --mount=type=cache,target=/root/.cache/uv \
	--mount=type=bind,source=uv.lock,target=uv.lock \
	--mount=type=bind,source=pyproject.toml,target=pyproject.toml \
	uv sync --locked --no-install-project --no-dev

# Then, add the rest of the project source code and install it
# Installing separately from its dependencies allows optimal layer caching
COPY . /app
RUN --mount=type=cache,target=/root/.cache/uv \
	uv sync --locked --no-dev

# Place executables in the environment at the front of the path
ENV PATH="/app/.venv/bin:$PATH"

# Reset the entrypoint, don't invoke `uv`
ENTRYPOINT []

# Set the port to 8080 if it is not already set and expose it
EXPOSE ${PORT:-8080}

# Run the app
CMD ["uv", "run", "main.py"]
