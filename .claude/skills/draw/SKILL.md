---
name: draw
description: Render a system, pipeline or data-flow as a monospace ASCII diagram in the two-plane house style (a build/identity/data plane and a query/access plane), plus one analogy table and a concrete end-to-end example. Use on "draw", "diagram", "visualize", "sketch", "map out", or "in the same style".
---

# /draw — house-style ASCII system diagrams

Produce a plain-text architecture diagram that someone can read in a terminal and
immediately understand both *how the system is built* and *how a person uses it*. The
style is deliberate and consistent — reproduce it exactly.

## Output rules

- Emit the whole diagram inside a single fenced ``` block so it renders monospaced.
- ASCII box-drawing only: `┌ ┐ └ ┘ │ ─ ├ ┤ ┬ ┴ ┼` for boxes/tables; `▼ ► ◄ │ ─` for flow.
- **Label every edge** with what flows across it AND any trigger/timing/cardinality
  (e.g. `nightly 02:00Z`, `real-time 1-2 min`, `per-user token`, `single-commit upsert`).
  An unlabeled arrow is a bug.
- Use the **real names** — actual files, paths, components, services, commit pins, env
  flags from the system at hand. Never generic ("Service A"). Ground it.
- Keep boxes narrow enough to align; favor clarity over density.
- No emojis, no color, no decoration that doesn't carry information.

## Structure — two planes, numbered

**`1. The <X> plane — how <the thing is produced / secured / flows>`**
Trace from sources of truth → derivation/transform → versioned/canonical store →
the engine that answers. Put **column headers** across the top naming each stage
(e.g. `SOURCES OF TRUTH   DERIVATION   VERSIONED STORE   QUERY ENGINE`, or for an
auth system `DEVICE   ACCESS LAYER   GATEWAY   UPSTREAM`). Nest sub-boxes when one
component contains structured parts (tables inside a store, controls inside a layer).

**`2. The query plane — how a <terminal user / caller> reaches the result`**
Start at `YOU (terminal)` with a realistic quoted question, go through the agent/tool
that picks the right lens, into the engine, and **end with a concrete "ANSWER back in
your terminal:"** block showing the actual payoff in the system's own vocabulary.

## The analogy table (mandatory)

Include exactly one table that captures the system's central conceptual mapping — the
"this is to that what A is to B" insight, or a two-column before/after or local/remote
comparison. Introduce it with one line: `The <X ↔ Y> analogy is exact and deliberate:`
or `The "<core principle>" model is exact and deliberate:`. This table is where the
design's *why* lives.

```
  ┌────────────────────┬───────────────────────────────────────────────────┐
  │  <left concept>    │  <right concept>                                  │
  ├────────────────────┼───────────────────────────────────────────────────┤
  │ <pair>             │ <pair>                                            │
  └────────────────────┴───────────────────────────────────────────────────┘
```

## Closing prose

After the planes/table, 1-3 sentences naming the **"story"** each part tells — the
audit story, the control story, the privacy story, the freshness story. Name what the
diagram lets the reader *now ask or trust* that they couldn't before. Short.

## Skeleton to fill

```
TITLE — one line of what this system is

1. The <X> plane — how <...>

   HEADER A          HEADER B          HEADER C          HEADER D
   ────────          ────────          ────────          ────────
  ┌───────────┐  what flows ┌───────────┐ what flows ┌───────────┐
  │  SOURCE   │ ───────────►│  DERIVE   │ ──────────►│   STORE   │ ──► ...
  └───────────┘  (trigger)  └───────────┘ (timing)   └───────────┘

2. The query plane — how a user reaches the result
    YOU (terminal)
        │  "<a real question>"
        ▼
   ┌───────────┐  picks the lens: <tool> / <tool> / <tool>
   │   AGENT   │
   └─────┬─────┘
         ▼
   ┌───────────┐── reads ──► <engine/store>
   │  TOOLS    │
   └───────────┘
         ▼
   ANSWER back in your terminal: "<concrete payoff in system vocabulary>"

  The <core> analogy is exact and deliberate:
  ┌──────────┬───────────────────────────────┐
  │  left    │  right                        │
  └──────────┴───────────────────────────────┘
```

Then close with the "story" sentences.

## Notes

- Two planes is the default; a simple system may need only one, a complex one may add a
  third (e.g. a control/governance plane). Keep the numbered-plane + labeled-edge +
  analogy-table + concrete-answer spine regardless.
- If you lack a real detail, ask or inspect the codebase — do not invent component names.
