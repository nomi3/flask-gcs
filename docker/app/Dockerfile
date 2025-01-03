ARG PYTHON_VERSION="3.13.1"
ARG PYTHON_MINOR_VERSION="3.13"

# =============================================================================
# base stage
# =============================================================================
FROM ghcr.io/astral-sh/uv:python${PYTHON_MINOR_VERSION}-bookworm-slim AS base

ENV UV_LINK_MODE="copy" \
    UV_COMPILE_BYTECODE="1" \
    UV_PYTHON_DOWNLOADS="never" \
    UV_PYTHON="python${PYTHON_MINOR_VERSION}"

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN --mount=type=cache,target=/root/.cache \
    uv sync --frozen --no-install-project

# =============================================================================
# dev stage
# =============================================================================
FROM base AS dev

RUN --mount=type=cache,target=/root/.cache \
    uv sync --dev --frozen --no-install-project

COPY app.py ./
COPY src ./src

# =============================================================================
# prod stage
# =============================================================================
FROM base AS prod

COPY app.py ./
COPY src ./src

# =============================================================================
# prod-release stage
# =============================================================================
FROM python:${PYTHON_VERSION}-slim-bookworm AS prod-release

ENV PATH="/app/.venv/bin:$PATH"
WORKDIR /app

COPY --from=prod /app /app

CMD ["gunicorn", "app:create_app()", "-w", "4", "-b", "0.0.0.0:8080", "--log-level=info"]

# =============================================================================
# dev-release stage
# =============================================================================
FROM python:${PYTHON_VERSION}-slim-bookworm AS dev-release

ENV PATH="/app/.venv/bin:$PATH"
WORKDIR /app

COPY --from=dev /app /app

CMD ["gunicorn", "app:create_app()", "-w", "4", "-b", "0.0.0.0:8080", "--log-level=info"]
