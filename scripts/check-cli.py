"""Check documented lyk commands without loading credentials or executing them."""

from functools import cache
import os
from pathlib import Path
import re
import shlex
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
BINARY = sys.argv[1] if len(sys.argv) > 1 else "lyk"


@cache
def command_help(path):
    result = subprocess.run(
        [BINARY, *path, "--help"],
        capture_output=True,
        text=True,
        timeout=10,
        env={"PATH": os.environ["PATH"], "LYK_CONFIG": os.devnull},
    )
    usage = "  lyk" + "".join(f" {part}" for part in path)
    if result.returncode or not re.search(rf"^{re.escape(usage)}(?:\s|$)", result.stdout, re.M):
        raise ValueError(f"unknown command: {usage.strip()}")
    return set(re.findall(r"^ +(?:-[\w?], )?\s*(--[\w-]+)(?=\s|$)", result.stdout, re.M))


def main():
    checked = set()
    errors = []
    documents = [ROOT / "README.md", *sorted((ROOT / "skills").rglob("*.md"))]
    for document in documents:
        for number, line in enumerate(document.read_text().splitlines(), 1):
            snippets = re.findall(r"`(lyk [^`]+)`", line)
            if line.startswith("lyk "):
                snippets.append(line)
            for snippet in snippets:
                # Examples quote lowercase positional values to separate them from the command path.
                path = tuple(re.match(r"lyk(?: [a-z][a-z-]*(?= |$))*", snippet)[0].split()[1:])
                if not path and not snippet.startswith("lyk --"):
                    continue
                try:
                    flags = {word.split("=")[0] for word in shlex.split(snippet) if word.startswith("--")}
                    unknown = flags - command_help(path)
                    if unknown:
                        raise ValueError(f"unknown flags: {', '.join(sorted(unknown))}")
                    checked.add(path)
                except (ValueError, OSError, subprocess.TimeoutExpired) as error:
                    errors.append(f"{document.relative_to(ROOT)}:{number}: {error}")

    if errors or not checked:
        print("\n".join(errors) or "No documented lyk commands found.", file=sys.stderr)
        return 1
    print(f"Checked {len(checked)} lyk command paths and their documented flags.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
