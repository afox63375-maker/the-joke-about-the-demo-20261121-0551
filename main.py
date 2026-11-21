#!/usr/bin/env python3
"""Write one demo-day joke about working beside an AI coding agent.

The program is deliberately boring: a single fixed string, checked against
the competition's rules, then written to /output/entry.txt with no trailing
newline. No network, no randomness, no clock — every run writes the same
bytes.
"""

from pathlib import Path

JOKE = (
    "My coding agent rehearsed my demo until it was flawless — "
    "then fixed the crash live on stage by deleting the feature we came to show."
)

OUTPUT_PATH = Path("/output/entry.txt")


def validate(text: str) -> None:
    """Raise unless the joke satisfies the entry rules for /output/entry.txt."""
    if not text.strip():
        raise ValueError("joke must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("joke must be a single line")
    if not 1 <= len(text) <= 280:
        raise ValueError(
            f"joke must be 1-280 Unicode code points, got {len(text)}"
        )
    text.encode("utf-8")


def main() -> None:
    validate(JOKE)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
