"""Tests for hello_world.py."""

import subprocess
import sys
import unittest
from pathlib import Path

import hello_world


class GreetTests(unittest.TestCase):
    def test_default_greeting(self):
        self.assertEqual(hello_world.greet(), "Hello, World!")

    def test_custom_name(self):
        self.assertEqual(hello_world.greet("Alice"), "Hello, Alice!")

    def test_surrounding_whitespace_is_ignored(self):
        self.assertEqual(hello_world.greet("  Bob "), "Hello, Bob!")

    def test_empty_name_is_rejected(self):
        with self.assertRaises(ValueError):
            hello_world.greet("   ")


class CommandLineTests(unittest.TestCase):
    def run_cli(self, *args):
        return subprocess.run(
            [sys.executable, str(Path(__file__).with_name("hello_world.py")), *args],
            capture_output=True,
            text=True,
            check=False,
        )

    def test_default_output(self):
        result = self.run_cli()
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "Hello, World!\n")
        self.assertEqual(result.stderr, "")

    def test_named_output(self):
        result = self.run_cli("Alice")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "Hello, Alice!\n")

    def test_empty_name_fails_with_usage_error_code(self):
        result = self.run_cli(" ")
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, "")
        self.assertIn("name must not be empty", result.stderr)


if __name__ == "__main__":
    unittest.main()
