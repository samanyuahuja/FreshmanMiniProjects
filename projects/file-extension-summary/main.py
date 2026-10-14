"""Command-line interface for the file extension summary tool."""

from __future__ import annotations

import argparse

from extension_summary import summarize_extensions


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Count files by extension in a directory.",
    )
    parser.add_argument("directory", help="Directory to inspect")
    parser.add_argument(
        "--recursive",
        action="store_true",
        help="Include files in nested directories",
    )
    args = parser.parse_args()

    counts = summarize_extensions(args.directory, recursive=args.recursive)
    if not counts:
        print("No files found.")
        return

    for extension, count in counts.items():
        print(f"{extension}: {count}")


if __name__ == "__main__":
    main()
