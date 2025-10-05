<!--
Guidance for AI coding agents working on the `bookbot` repository.
Focus on actionable, repository-specific facts and examples so an agent can be productive immediately.
-->

# Copilot instructions for bookbot

Purpose
- Small, single-repo Python project that reads a book text and computes simple statistics.

Big picture
- `main.py` is a tiny CLI-style runner: it reads `books/frankenstein.txt` (hard-coded) and calls helpers in `stats.py`.
- `stats.py` exposes pure helper functions for text analysis (word counts and per-character counts).
- No external dependencies or build system; this is plain Python source suitable for quick edits and tests.

Key files to reference
- `main.py` — entrypoint and example usage. Note: `main()` is called at import-time (no `if __name__ == "__main__"` guard).
- `stats.py` — functions to change or extend. Current public functions:
  - `get_num_words(text) -> int`
  - `get_num_unique_characters(text) -> (unique_characters, counts)` — see "quirks" below.
- `books/frankenstein.txt` — sample data used by `main.py`.
- `README.md` — minimal project description.

Quick run / developer workflow
- Run the app locally:

  python3 main.py

- Quick one-liners for experimentation (examples):

  python3 -c "from stats import get_num_words; print(get_num_words('hello world'))"
  python3 -c "from stats import get_num_unique_characters; print(get_num_unique_characters('aa BB!!'))"

Patterns & conventions (repo-specific)
- Small, procedural code. Functions in `stats.py` are intended to be importable and unit-testable.
- File I/O is done with plain `open(path)` and default encoding — expect platform-default encoding behavior.
- `main.py` currently demonstrates how the helpers are consumed; changing a helper's signature requires updating `main.py`.

Discoverable quirks and gotchas
- `get_num_unique_characters` returns a two-tuple: `(unique_characters, counts)`. In the current implementation `unique_characters` is an empty dict while `counts` contains the actual per-letter counts (lower-cased and filtered by `str.isalpha()`).
  - If you modify the return shape, update `main.py` which unpacks the result into `num_unique_characters, character_counts`.
- `main.py` calls `main()` at the bottom without a `if __name__ == "__main__"` guard. Importing `main` will execute the script — avoid importing `main` in tests or refactors unless you intentionally want that behaviour.
- Text processing filters letters using `char.isalpha()` and lowercases via `text.lower()`; punctuation and digits are ignored for the per-character counts.

Safe-edit advice for agents (concrete, local changes)
- If adding or changing a function signature in `stats.py`, update `main.py`'s call sites (example: unpacking of `get_num_unique_characters`).
- Prefer edits that preserve the existing function contracts unless you're also changing callers.
- If you add tests or import `main.py` in tooling, first add a guard:

  if __name__ == "__main__":
      main()

  This prevents accidental execution when importing.

Examples from the codebase
- Word count implementation (exact): `return len(text.split())` in `get_num_words` — splitting by whitespace.
- Character counts implementation (exact): lower-cased iteration filtering `char.isalpha()` and aggregating in a dict.

Testing & debugging notes
- There are no automated tests in the repo. To test functions interactively import `stats` (safe) and call helpers. Avoid importing `main` unless you expect the script to run.
- Use the hard-coded path `books/frankenstein.txt` to reproduce the default execution path used by `main.py`.

Integration points
- No external APIs, databases, or packages — changes are local to the source files.

When in doubt
- Read `main.py` to see how the helpers are used; preserve return shapes and side-effects unless you update callers.
- Look for `counts` in `stats.py` when implementing character-related features — it's the canonical per-character map.

If anything in these notes looks incomplete or you'd like the agent to enforce a refactor (for example: fixing the unused `unique_characters` return value), ask and I will update this guidance and propose a minimal patch.
