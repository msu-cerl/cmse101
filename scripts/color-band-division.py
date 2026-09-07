#!/usr/bin/env python3
"""Split an image into RGB intensity bands, each rendered in color and in black-and-white.

For each channel (red, green, blue) the channel's 0-255 range is divided into
N equal-width bands. For every (channel, band) pair two PNGs are written:
  - color:  the channel's raw intensity, masked to pixels in that band, other
            channels zeroed (e.g. a red band looks reddish/black).
  - bw:     a grayscale image of the channel's raw intensity, masked to pixels
            in that band, zero elsewhere.
"""

import argparse
from pathlib import Path

import numpy as np
from PIL import Image

CHANNELS = ("red", "green", "blue")


def band_edges(num_bands: int) -> list[tuple[int, int]]:
    step = 256 / num_bands
    edges = []
    for i in range(num_bands):
        lo = int(round(i * step))
        hi = int(round((i + 1) * step)) - 1 if i < num_bands - 1 else 255
        edges.append((lo, hi))
    return edges


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="path to the source image")
    parser.add_argument("--bands", type=int, default=1, help="number of intensity bands per channel (default: 1, i.e. one image per channel)")
    parser.add_argument("--scale", type=float, default=1.0, help="fractional scale for output size, e.g. 0.5 (default: 1.0)")
    parser.add_argument("--outdir", type=Path, default=None, help="output directory (default: alongside input)")
    args = parser.parse_args()

    if args.bands < 1:
        parser.error("--bands must be at least 1")
    if not (0 < args.scale <= 1.0):
        parser.error("--scale must be in (0, 1.0]")

    img = Image.open(args.input).convert("RGB")
    if args.scale != 1.0:
        new_size = (max(1, round(img.width * args.scale)), max(1, round(img.height * args.scale)))
        img = img.resize(new_size, Image.LANCZOS)

    arr = np.asarray(img)  # H x W x 3, uint8

    outdir = args.outdir if args.outdir is not None else args.input.parent
    outdir.mkdir(parents=True, exist_ok=True)
    stem = args.input.stem

    edges = band_edges(args.bands)

    single_band = len(edges) == 1

    for ch_idx, ch_name in enumerate(CHANNELS):
        channel = arr[:, :, ch_idx]
        for band_idx, (lo, hi) in enumerate(edges):
            mask = (channel >= lo) & (channel <= hi)
            suffix = "" if single_band else f"_band{band_idx}_{lo}-{hi}"

            color = np.zeros_like(arr)
            color[:, :, ch_idx] = np.where(mask, channel, 0)
            color_path = outdir / f"{stem}_{ch_name}{suffix}_color.png"
            Image.fromarray(color, mode="RGB").save(color_path)

            bw = np.where(mask, channel, 0).astype(np.uint8)
            bw_path = outdir / f"{stem}_{ch_name}{suffix}_bw.png"
            Image.fromarray(bw, mode="L").save(bw_path)

    print(f"Wrote {len(CHANNELS) * len(edges) * 2} images to {outdir}")


if __name__ == "__main__":
    main()
