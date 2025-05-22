# Test Project

An example rpoject for running FastAPI, Docker, and UV

## Getting Started

Prerequisites:

- `podman` or `docker`
- `uv` (to build from source)
- `~/.netrc` file with the following information

If pulling packages from a private repo, you will need a ~/.netrc file with the following contents which will be passed as a secret to the docker build command.

    ```bash
    machine registry-gitlab.dle.afrl.af.mil
    login __token__
    password PERSONAL_ACCESS_TOKEN
    ```

## Updating the lock file

```bash
uv sync -U --native-tls --no-install-project
```

## Building the container

```bash
# With secret
docker build --secret id=NETRC,src=$HOME/.netrc -t test-project --target=build .

# Without secret
docker build - -t test-project --target=build .
```

## Running the container

```bash
docker run --rm test-project
```
