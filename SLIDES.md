# MARP Slides Workflow for CMSE 101

How lecture decks are written, built, and published.

## How it fits together

```
slides/                          # SOURCES — you edit these
  _theme.css                     #   shared accessible theme
  images/                        #   deck images
  lecture-01-welcome.md          #   one file per lecture
  lecture-02-....md

static/slides/                   # GENERATED — gitignored, never edit
  lecture-01-welcome.html        #   interactive deck
  lecture-01-welcome.pdf         #   download / D2L upload
  images/                        #   copied so HTML image srcs resolve

data/slides.yaml                 # GENERATED — committed, feeds the index page
content/slides/_index.md         # the /slides/ landing page copy
layouts/slides/list.html         # renders the deck table from data/slides.yaml
```

Two rules explain the layout:

1. **Sources live in `slides/`, not `content/slides/`.** Anything under
   `content/` gets rendered by Hugo as a normal page. A MARP deck rendered that
   way is a mess — every `---` slide break, every `<!-- _class: -->` directive,
   and every speaker note dumped onto one long page.
2. **Output goes to `static/slides/`, not `public/`.** Hugo wipes and rebuilds
   `public/` on every run, and `public/` is gitignored, so anything written
   there is thrown away. Hugo copies `static/` through verbatim, so
   `static/slides/lecture-01-welcome.html` is served at
   `/slides/lecture-01-welcome.html`.

## Setup

You need Node.js. The build script pins the MARP version and fetches it through
`npx`, so there is nothing to install globally.

PDF export needs Chrome, Edge, or Firefox installed — MARP renders PDFs through
a real browser. On a Mac with Chrome you are already set.

## Writing a deck

Create `slides/lecture-NN-topic.md`. Frontmatter:

```markdown
---
title: "Lecture 02: Where AI Came From"
date: 2026-08-28
description: "Optional one-line summary, shown on the slides index"
marp: true
size: 16:9
paginate: true
---
```

`title` and `date` are what appear on the `/slides/` index, so keep them
accurate. You do **not** need a `theme:` line — the build script applies
`slides/_theme.css` to every deck and overrides whatever frontmatter says.

### Slide types

Content slide (default):

```markdown
# Slide Title

Content here. Use **bold**, *italic*, and `code` as needed.

- Bullet point
- Another point
```

Title slide:

```markdown
<!-- _class: title -->
# Main Title
## Subtitle
```

Break / section slide:

```markdown
<!-- _class: break -->
# Section Title
```

### Presenter notes

```markdown
# Slide Title

Visible content here.

<!--_speaker_note:
Talking points, timing, cues. Visible in presenter view (press `p`), not on
the slide itself.
-->
```

Notes are **not** stripped from the published HTML — they are in the page
source, and anyone who presses `p` can read them. Do not put anything in a
speaker note you would not want a student to see.

### Images

Put them in `slides/images/` and reference them relatively:

```markdown
![Description of the image for screen readers w:900](./images/dtpa.png)
```

The alt text is everything before the MARP sizing directive (`w:900`), so write
a real description there.

### Emphasis box and two columns

```markdown
<div class="emphasize">
**This is important.**
</div>
```

```markdown
<div class="columns">
<div class="column">

### Left
- Point 1

</div>
<div class="column">

### Right
- Point A

</div>
</div>
```

## Building

```bash
./build-slides.sh                     # every deck
./build-slides.sh lecture-01-welcome  # just one
```

Each run produces, per deck, an HTML file and a PDF in `static/slides/`, copies
`slides/images/` next to them, and regenerates `data/slides.yaml` across *all*
decks so the index page never goes stale.

To preview in the site as students will see it:

```bash
./build-slides.sh && hugo server
```

Then open `/slides/`.

In the HTML deck: arrow keys or space to advance, `f` for fullscreen, `p` for
presenter view with notes.

## Publishing

Commit the source and push:

```bash
git add slides/ data/slides.yaml
git commit -m "Add lecture 02 slides"
git push
```

CI does the rest. `.github/workflows/build-deploy.yml` runs `./build-slides.sh`
before `hugo`, so the decks are rebuilt from source on every deploy. Generated
HTML and PDFs are **never committed** — `static/slides/` is gitignored.

`data/slides.yaml` is the one generated file that *is* committed. CI regenerates
it anyway, so the deployed index is always correct; committing it just means
`hugo server` shows the right index without running the slide build first.

### D2L

`./build-slides.sh lecture-NN-topic`, then upload
`static/slides/lecture-NN-topic.pdf` to D2L Content. Same PDF the site serves,
so students who use either route get identical slides.

## Accessibility

The theme provides WCAG AA contrast, a 24px minimum readable sans-serif,
semantic heading structure, visible focus indicators, and keyboard navigation.

Before publishing a deck:

- [ ] Every image has descriptive alt text
- [ ] Headings nest logically (no h1 → h3 skips)
- [ ] Color is never the only carrier of meaning
- [ ] No flashing or animated content
- [ ] Speaker notes contain nothing student-facing you would not share
- [ ] The PDF is readable and nothing is clipped

Test with keyboard-only navigation, a screen reader (VoiceOver / NVDA), and
200% browser zoom.

## Troubleshooting

**Images missing from the PDF.** The build needs `--allow-local-files` for the
headless browser to read `slides/images/`. Without it MARP prints a warning and
silently drops every local image. This is already in `build-slides.sh`; if you
run `marp` by hand, include it.

**Images broken in the HTML.** MARP leaves HTML image srcs relative
(`./images/foo.png`), so the images must sit beside the generated HTML.
`build-slides.sh` copies `slides/images/` into `static/slides/images/` on every
run — if you invoke MARP directly, you have to do that yourself.

**The theme isn't applying.** The flag is `--theme`, not `--css`. There is no
`--css` option; MARP accepts it silently and ignores it, and the deck renders in
MARP's built-in default theme with no error.

**PDF generation fails.** MARP needs a Chromium-based browser. Install Chrome,
or set `CHROME_PATH` to a browser binary. As a fallback, open the HTML in Chrome
and print to PDF.

**A deck isn't on the /slides/ index.** The index reads `data/slides.yaml`,
which only lists files matching `slides/lecture-*.md`. Check the filename
prefix, then rerun `./build-slides.sh`.

**A deck renders as a mangled web page.** Its source is in `content/` instead of
`slides/`. Move it.
