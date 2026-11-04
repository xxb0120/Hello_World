# Hello_World

A small collection of "Hello, World!" examples, one per language. Every example
is self-contained: a runnable entry point, an automated test and a short README
with the commands to run and test it.

## Quick start

```console
$ python3 examples/python/hello_world.py
Hello, World!

$ python3 examples/python/hello_world.py Alice
Hello, Alice!
```

## Examples

| Language | Entry point | Run | Test |
| --- | --- | --- | --- |
| Python 3.11+ | [`examples/python/hello_world.py`](examples/python/hello_world.py) | `python3 examples/python/hello_world.py [name]` | `python3 -m unittest discover -s examples/python` |
| Java 21+ | [`examples/java/HelloWorld.java`](examples/java/HelloWorld.java) | `java examples/java/HelloWorld.java [name]` | CI smoke test |

## Repository layout

```text
.
├── .github/workflows/ci.yml   # tests, doctests, lint and Java smoke test
├── docs/IMPROVEMENT_PLAN.md   # how this repository is organised and what comes next
├── examples/
│   ├── java/
│   └── python/
├── CONTRIBUTING.md            # how to add a new example
├── LICENSE
└── README.md
```

## Adding a new example

Create `examples/<language>/` with a runnable entry point, a test and a README,
then add a CI job and a row to the table above. See
[CONTRIBUTING.md](CONTRIBUTING.md) for the details.

## License

[MIT](LICENSE)
