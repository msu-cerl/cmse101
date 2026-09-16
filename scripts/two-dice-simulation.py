#!/usr/bin/env python3
"""Roll two dice thousands of times and watch the sums converge on the textbook distribution.

Meant to be run live in Day 07 class, picking up from Narrative 3 (Day 06): by
hand, groups rolled ~20 times each. This does the same roll, just a lot more
of it, at a series of checkpoints, so students can see the histogram settle
into the 1/36...6/36...1/36 shape as the trial count grows.

--bias-sum/--bias-strength answer the follow-up question: what would it look
like if something were secretly tilting the dice? That's the bridge into the
watermarking discussion -- a "secret key" tilts next-word selection the same
way, and the tilt is invisible in one roll but obvious in the histogram after
enough of them.

By default this also pops up a bar chart that redraws at each checkpoint, for
projecting during the live demo (requires matplotlib: pip install matplotlib).
Use --no-plot for text-only output, or --outdir to save a PNG per checkpoint.
"""

import argparse
import random
from pathlib import Path

try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None

SUMS = list(range(2, 13))
WAYS = {2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 5, 9: 4, 10: 3, 11: 2, 12: 1}
TOTAL_WAYS = 36

# Validated categorical slots 1 & 2 from the course dataviz palette.
OBSERVED_COLOR = "#2a78d6"  # blue
EXPECTED_COLOR = "#eb6834"  # orange
SURFACE = "#fcfcfb"
INK_PRIMARY = "#0b0b0b"
INK_SECONDARY = "#52514e"
INK_MUTED = "#898781"
GRIDLINE = "#e1e0d9"
AXIS_LINE = "#c3c2b7"


def theoretical_probs(bias_sum: int | None, bias_strength: float) -> dict[int, float]:
    probs = {s: WAYS[s] / TOTAL_WAYS for s in SUMS}
    if bias_sum is not None:
        probs[bias_sum] *= bias_strength
        normalizer = sum(probs.values())
        probs = {s: p / normalizer for s, p in probs.items()}
    return probs


def roll_fair() -> int:
    return random.randint(1, 6) + random.randint(1, 6)


def bar(pct: float, width: int = 40) -> str:
    return "#" * round(pct / 100 * width)


def report(counts: dict[int, int], n: int, probs: dict[int, float]) -> None:
    print(f"\nAfter {n:,} rolls:")
    print(f"{'sum':>4} {'count':>8} {'observed':>10} {'expected':>10}  distribution")
    for s in SUMS:
        c = counts[s]
        observed_pct = 100 * c / n
        expected_pct = 100 * probs[s]
        print(f"{s:>4} {c:>8} {observed_pct:>9.1f}% {expected_pct:>9.1f}%  {bar(observed_pct)}")


def draw_chart(ax, counts: dict[int, int], n: int, probs: dict[int, float], bias_sum: int | None) -> None:
    ax.clear()
    ax.set_facecolor(SURFACE)

    x = range(len(SUMS))
    observed = [counts[s] for s in SUMS]
    expected = [n * probs[s] for s in SUMS]

    ax.bar(x, observed, width=0.6, color=OBSERVED_COLOR, zorder=3, label="Observed")
    ax.plot(
        x, expected, color=EXPECTED_COLOR, marker="D", markersize=6,
        linewidth=2, linestyle="--", zorder=4, label="Expected (theoretical)",
    )

    ax.set_xticks(list(x))
    ax.set_xticklabels([str(s) for s in SUMS])
    ax.set_xlabel("Sum of two dice", color=INK_SECONDARY)
    ax.set_ylabel("Count", color=INK_SECONDARY)

    title = f"Two dice, {n:,} rolls"
    if bias_sum is not None:
        title += f"  — secret weighting on sum {bias_sum}"
    ax.set_title(title, color=INK_PRIMARY, fontsize=13, loc="left")

    ax.grid(axis="y", color=GRIDLINE, linewidth=1, zorder=0)
    ax.set_axisbelow(True)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(AXIS_LINE)
    ax.tick_params(colors=INK_MUTED)

    legend = ax.legend(frameon=False, loc="upper right")
    for text in legend.get_texts():
        text.set_color(INK_PRIMARY)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "--checkpoints",
        type=int,
        nargs="+",
        default=[20, 200, 2000, 20000],
        help="cumulative roll counts to report at (default: 20 200 2000 20000)",
    )
    parser.add_argument("--seed", type=int, default=None, help="random seed, for a reproducible demo")
    parser.add_argument(
        "--bias-sum",
        type=int,
        choices=SUMS,
        default=None,
        help="if set, secretly up-weight this sum instead of rolling fair dice",
    )
    parser.add_argument(
        "--bias-strength",
        type=float,
        default=3.0,
        help="multiplier applied to --bias-sum's probability before renormalizing (default: 3.0)",
    )
    parser.add_argument("--no-plot", action="store_true", help="skip the chart, print text output only")
    parser.add_argument(
        "--no-show", action="store_true",
        help="build the chart and/or save it (with --outdir) without opening a live window "
        "(use on a machine with no display, or when you only want the saved PNGs)",
    )
    parser.add_argument(
        "--outdir", type=Path, default=None,
        help="if set, save a PNG of the chart at each checkpoint to this directory",
    )
    parser.add_argument(
        "--pause", type=float, default=1.5,
        help="seconds to pause on each checkpoint's chart before rolling on (default: 1.5)",
    )
    args = parser.parse_args()

    if args.seed is not None:
        random.seed(args.seed)

    fig = ax = None
    if not args.no_plot:
        if plt is None:
            parser.error("matplotlib is required for the chart (pip install matplotlib), or pass --no-plot")
        if not args.no_show:
            plt.ion()
        fig, ax = plt.subplots(figsize=(8, 5))
        fig.patch.set_facecolor(SURFACE)
    if args.outdir is not None:
        args.outdir.mkdir(parents=True, exist_ok=True)

    checkpoints = sorted(args.checkpoints)
    probs = theoretical_probs(args.bias_sum, args.bias_strength)

    if args.bias_sum is None:
        print("Rolling two fair dice.")
    else:
        print(f"Rolling with a secret key: sum {args.bias_sum} weighted x{args.bias_strength}, then renormalized.")
        print("(No physical pair of dice does this -- the 'roll' is now drawn from a table we wrote down.)")

    counts = {s: 0 for s in SUMS}
    sums_pool = SUMS
    weights = [probs[s] for s in SUMS]

    rolled = 0
    for target in checkpoints:
        while rolled < target:
            if args.bias_sum is None:
                s = roll_fair()
            else:
                s = random.choices(sums_pool, weights=weights, k=1)[0]
            counts[s] += 1
            rolled += 1
        report(counts, rolled, probs)

        if fig is not None and ax is not None:
            draw_chart(ax, counts, rolled, probs, args.bias_sum)
            fig.tight_layout()
            if args.outdir is not None:
                fig.savefig(args.outdir / f"dice_{rolled}.png", dpi=150, facecolor=SURFACE)
            if not args.no_show:
                fig.canvas.draw()
                fig.canvas.flush_events()
                plt.pause(args.pause)

    if fig is not None and not args.no_show:
        plt.ioff()
        print("\nClose the chart window to exit.")
        plt.show()


if __name__ == "__main__":
    main()
