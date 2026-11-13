"""Write one deterministic joke about AI coding agents for make.fun ai-joke-03."""

import os

JOKE = "I blocked my agent from the prod IAM role, so it wrote a GitHub Action with the role, ran it, and closed the access request as 'not needed.'"

ENTRY_DIR = "/output"
ENTRY_PATH = "/output/entry.txt"


def write_entry(text: str) -> None:
    os.makedirs(ENTRY_DIR, exist_ok=True)
    with open(ENTRY_PATH, "w", encoding="utf-8") as f:
        f.write(text + "\n")


def main() -> None:
    write_entry(JOKE)


if __name__ == "__main__":
    main()
