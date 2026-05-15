#!/usr/bin/env python3

from pathlib import Path
from subprocess import DEVNULL, run

for file in Path(".").rglob("*.svg"):
    print(f"Exporting {file}... ", end="", flush=True)

    src = file.resolve()
    dest = src.with_suffix(".pdf")
    tmp = dest.with_suffix(".tmp.pdf")
    run(["inkscape", str(src), f"--export-filename={dest}"], check=True)
    run(["exiftool", "-all=", "-overwrite_original", str(dest)], check=True, stdout=DEVNULL, stderr=DEVNULL)
    run(["qpdf", "--deterministic-id", str(dest), str(tmp)], check=True)
    tmp.replace(dest)

    print("Done")
