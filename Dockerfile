FROM ubuntu:24.04 AS base


RUN apt-get update && apt-get upgrade -y \
    && apt-get install git -y

WORKDIR /project


# Install python dependencies
RUN \
    --mount=type=secret,id=NETRC,target=/root/.netrc \
    --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    --mount=from=ghcr.io/astral-sh/uv:0.7.3,source=/uv,target=/bin/uv \
    ["uv", "sync", "--frozen", "--no-install-project", "--no-dev", "--no-editable"]

# set up venv
ENV VIRTUAL_ENV=/project/.venv
ENV PATH="/project/.venv/bin:$PATH"

COPY . ./

RUN \
    --mount=type=secret,id=NETRC,target=/root/.netrc \
    --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    --mount=from=ghcr.io/astral-sh/uv:0.7.3,source=/uv,target=/bin/uv \
    ["uv", "sync", "--frozen",  "--no-dev", "--no-editable"]

CMD ["uvicorn", "app.endpoints:api", "--host", "0.0.0.0", "--port", "8000"]
