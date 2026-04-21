from __future__ import annotations

import csv
from pathlib import Path


DOWNLOADS_DIR = Path.home() / "Downloads"
NAME_HINTS = ("financial", "tweet")


def find_matching_csvs(directory: Path) -> list[Path]:
    matches: list[Path] = []
    for csv_file in directory.rglob("*.csv"):
        name = csv_file.name.lower()
        if all(hint in name for hint in NAME_HINTS):
            matches.append(csv_file)
    return sorted(matches)


def preview_csv(csv_path: Path, limit: int = 5) -> None:
    with csv_path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file)
        for index, row in enumerate(reader):
            print(row)
            if index + 1 >= limit:
                break


def main() -> None:
    csv_files = find_matching_csvs(DOWNLOADS_DIR)
    if not csv_files:
        raise SystemExit("Nenhum CSV parecido com 'financial_tweet' foi encontrado em Downloads.")

    print("Arquivos encontrados em Downloads:")
    for csv_file in csv_files:
        print(f"- {csv_file}")

    chosen_file = csv_files[0]
    print(f"\nUsando arquivo: {chosen_file}")
    print("\nPrevia:")
    preview_csv(chosen_file)


if __name__ == "__main__":
    main()
