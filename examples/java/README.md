# Java example

Requires JDK 21 or newer. The program is launched directly from source, so no
build tool is needed.

```console
$ java HelloWorld.java
Hello, World!

$ java HelloWorld.java Alice
Hello, Alice!
```

A blank name prints an error on stderr and exits with status 2:

```console
$ java HelloWorld.java " "
error: name must not be empty
```

CI runs a smoke test for the two default commands (see
`.github/workflows/ci.yml`).
