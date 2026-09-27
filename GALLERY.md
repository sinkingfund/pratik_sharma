# Manage photos

Put your images in one of these folders:

| Folder | Where photos appear |
| --- | --- |
| `gallery/portrait/` | Large portrait slider |
| `gallery/social/` | Social slider |
| `gallery/work/` | Work slider |
| `gallery/interest/` | Interest slider |

Add, remove, or rename images freely. Filenames do not need a prefix or a number. JPG, JPEG, PNG, WebP, GIF, and AVIF are supported; use unique names within each folder. The site displays every valid image in the corresponding folder, in a different order each day. If a folder is empty, its slider shows a safe empty state; an empty portrait folder uses `pratik-sharma.jpeg` as a fallback.

After changing photos, run `python update-gallery.py` from the project folder. This regenerates `gallery/photos.json` from the folders. Commit and push the updated files to the GitHub repository that hosts your GitHub Pages site. If you are using Sites hosting instead, send me the updated gallery ZIP and I can publish it there. Do not edit `photos.json` manually.
