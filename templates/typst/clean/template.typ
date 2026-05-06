#import "@preview/tablex:0.0.9": tablex, cellx, rowspanx, colspanx, hlinex, vlinex

// table style dicts expected by mystmd-generated tablex calls
#let tableStyle = (stroke: 0.5pt + luma(210))
#let columnStyle = (:)

// MSU green palette
#let green = rgb("#18453B")
#let green-light = green.lighten(88%)

#set page(
  paper: "us-letter",
  margin: (top: 1in, bottom: 1in, left: 1.25in, right: 1.25in),
  footer: context {
    align(center, text(fill: luma(80), size: 9pt, font: "Roboto")[
      #counter(page).display()
    ])
  },
)

#set text(font: "Roboto", size: 11pt, fill: luma(30))
#set par(leading: 0.7em, spacing: 1.1em)
#set list(marker: text(fill: green)[•])

// h1 — document title / top section
#show heading.where(level: 1): it => {
  v(1.4em)
  text(fill: green, weight: "bold", size: 15pt, it.body)
  v(0.25em)
  line(length: 100%, stroke: 0.4pt + green.lighten(55%))
  v(0.4em)
}

// h2
#show heading.where(level: 2): it => {
  v(1em)
  text(fill: green, weight: "semibold", size: 12.5pt, it.body)
  v(0.25em)
}

// h3
#show heading.where(level: 3): it => {
  v(0.75em)
  text(fill: luma(50), weight: "semibold", size: 11pt, it.body)
  v(0.15em)
}

// inline code
#show raw.where(block: false): it => box(
  fill: green-light,
  inset: (x: 4pt, y: 1pt),
  radius: 2pt,
  text(fill: green.darken(10%), size: 0.9em, it),
)

// code blocks
#show raw.where(block: true): it => block(
  width: 100%,
  fill: green-light,
  inset: 10pt,
  radius: 3pt,
  text(size: 0.88em, it),
)

[-CONTENT-]
