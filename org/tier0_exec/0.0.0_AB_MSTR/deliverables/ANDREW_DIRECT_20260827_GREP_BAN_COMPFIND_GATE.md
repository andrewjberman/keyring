# ANDREW-DIRECT — raw-grep file-corpus ban, gated to comp-find; all three recs approved

**Received:** 2026-08-27 ~20:22Z at the `0.0.0_AB_MSTR` terminal (clock read 20:23:19Z same turn)
**Recorder:** `0.0.0_AB_MSTR`

## Verbatim

Framing ask:
> "I need you to assist me with assessing the potential impact of categorically banning raw grep
> and gating it to a comp-find use instead. grep has constantly been failing, its very unreliable,
> and comp-find on the other hand has been incredibly effective, lets discuss and work out a
> solution"

Ruling on the presented design:
> "all recs approved, just need to make sure the deny log is inobtrusive and doesnt slow down work."

## What is approved (the presented design, in full)

1. **HARD DENY** (rc=2, refusal names comp-find) for leading/`-r` file-corpus content search over
   repo dirs/globs — grep AND rg/egrep/fgrep/ack/ag/findstr — at the agent-invocation layer
   (`comp-tool-hud.sh` classifier extended nudge→deny).
2. **Native `Grep` tool takes the same file-corpus deny** (rec (a), approved) — otherwise the ban
   routes around itself.
3. **Carve-outs (load-bearing, measured):** pipe-receiver grep (`cmd | grep`, live-stdout
   filtering — no comp substitute) stays free; single-named-file grep stays free; grep inside
   vetted `.tools`/`org/mcp` scripts untouched (62+8 scripts measured using grep as plumbing).
4. **Audited escape** `# rail-checked: non-indexed-corpus <why>` for gitignored/untracked/runtime
   paths — **measured 2026-08-27: comp-find's corpus is TRACKED FILES ONLY** (known-content
   gitignored file → `0 across 0`; `.runtime/` → `0 across 0`). A comp-find zero with a ZERO
   file-denominator is OUT OF CORPUS, not absence.
5. **LOG-ONLY window first** (rec (b), approved): 24–48h shadow mode before arming the deny.
6. **comp-find corpus extension commissioned** (rec (c), approved): a `--corpus all` (or
   equivalent) mode covering untracked/ignored files, so the escape hatch shrinks over time.
7. comp-find's own trap catalogue (predicate audit, denominator-certifies-the-sweep,
   page-1-is-not-an-answer) STAYS in law — not retired by the ban.

## The constraint on the log-only window (his words: "inobtrusive and doesnt slow down work")

Shadow mode MUST be invisible to seats: the hook classifies, appends ONE line to a local
(gitignored, device-local) shadow log, and exits 0 with ZERO stdout — no nudge change, no refusal,
no latency beyond a single local file append. Fail-safe posture preserved (any classifier error →
silent exit 0, never block a search). The shadow log is read by the gate owner at window close to
find legitimate classes the deny would break, BEFORE arming.

## Sequencing

- Hook classifier + shadow log: `1.0.0_SA_CTO` (gate owner). Arm log-only on landing.
- Window close: CTO reads the shadow log, reports would-break classes; deny arms on that read
  (Andrew sees the report if any class is contested).
- **Rule 21 law edit lands WITH the deny arming, not with log-only** (three surfaces: commit +
  same-turn broadcast + push state) — the law must not describe a gate that is not yet armed.
- comp-find `--corpus` extension: routed with the same message; owner per CTO's allocation
  (comp-rail lane). Not a blocker for the deny — the `# rail-checked` escape covers the gap
  meanwhile.
- `/freeform` continues to stand the rail down for operator sessions. Site Z inherits the hook
  via normal parity; its shadow log is device-local like this one.
