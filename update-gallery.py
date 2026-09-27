"""Rebuild the published gallery list from images in gallery/*/."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent / "gallery"
GROUPS = ("portrait", "social", "work", "interest")
EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".avif"}


def main():
    gallery = {}
    for group in GROUPS:
        folder = ROOT / group
        folder.mkdir(parents=True, exist_ok=True)
        gallery[group] = [
            photo.name
            for photo in sorted(folder.iterdir(), key=lambda item: (item.name.casefold(), item.name))
            if photo.is_file()
            and not photo.name.startswith(".")
            and photo.suffix.lower() in EXTENSIONS
        ]
    (ROOT / "photos.json").write_text(
        json.dumps(gallery, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print("Gallery updated: " + ", ".join(f"{group} {len(gallery[group])}" for group in GROUPS))


if __name__ == "__main__":
    main()
