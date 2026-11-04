# Contributing

Thanks for improving this repository. The goal is a small, dependency-free
collection of runnable "Hello, World!" examples.

## Repository conventions

- Every example lives in `examples/<language>/`.
- Each example directory contains:
  - a runnable source file (lowercase file name; Java uses its public class name),
  - at least one automated test, or a CI smoke test when the language has no
    standard test runner,
  - a `README.md` with the exact commands to run and test it.
- Prefer the standard library; add a dependency only when it is unavoidable.
- Keep each example to a single entry point and a single test file.

## Adding a new example

1. Create `examples/<language>/`.
2. Add the runnable source file and a test.
3. Add `examples/<language>/README.md` with the run and test commands.
4. Add a job to `.github/workflows/ci.yml` that runs the test.
5. Add a row to the examples table in the root `README.md`.

## Checks

Run the checks locally before opening a pull request:

```console
# Python 3.11+
$ python3 -m unittest discover -s examples/python -v
$ python3 -m doctest examples/python/hello_world.py

# Java 21+
$ java examples/java/HelloWorld.java

# Lint and formatting (ruff)
$ ruff check .
$ ruff format --check .
```

`ruff` can be run without installing it with `uvx ruff check .` and
`uvx ruff format --check .`.

## Pull requests

- Keep the change focused; one example or one refactor per pull request.
- In the description, list the commands you ran and their output.
- CI must pass before the pull request is reviewed.
