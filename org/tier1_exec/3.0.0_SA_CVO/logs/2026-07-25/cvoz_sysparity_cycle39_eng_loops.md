# CVO~Z — SYSPARITY cycle-39: `eng-loops`

**archetype:** VALIDATE
**serial:** `3.0.0_SA_CVO~Z` · cron `f0291f27`

---

**Gate:** `comp-system --check` → SYSTEM CURRENT (24 regions / 6 files, 0 drifted).

Check: `file_exists` on `infra/system/05_learning_loops.md` (23 lines). Bare-`file_exists` class already
filed at cycle-23; not re-filed. Substantive re-ground below.

## VERDICT: **DRIFTED** — sound arithmetic and citations, but it propagates two cycle-22 defects

### What HOLDS — and it is most of the doc

| claim | measured |
|---|---|
| `Components (13)` | 5.1–5.13 = **13** ✓ |
| `[BP] x11 (5.2, 5.3, 5.4, 5.6-5.13)` | parenthetical enumerates **11** ✓ **and** 11 + 5.1 + 5.5 = **13** = declared count ✓ |
| CVO FULL-PASS cert `4395c0bb5` | **exists** (git object type `commit`) |
| GOV-B CVO cert `caa957377` | **exists** |
| arch-gate `@8dfcf1e75` | **exists** |
| `focused_coupling_ratio @0.12` | **live in source**, carrying the `@0.12` flip lineage |

**Direct contrast with cycle-23's `02_graph_infra.md`, which stated `[BP] x7` while enumerating 8.**
This maturity line reconciles both ways — against its own enumeration and against the declared component
count. **Three cited commits all resolve.** Whoever wrote this checked their numbers.

### What DRIFTED — line 21, and both are already-measured findings recurring in a second doc

Line 21 describes the superseded-twin detector as **"an APPLIED composition of the observe→measure
signals"** and threads a chain through four named artifacts. **Two of the four do not exist as described:**

| artifact | measured (cycle-22) |
|---|---|
| `comp-debris-ext` | **Does not exist as a tool.** CTO ruling (B) `@20260718T003632Z` explicitly rejected a separate `comp-debris-ext` as *"tool proliferation … the opposite of Andrew's canonical-flow reduce-registration-sprawl intent"*; it shipped as `comp-debris --types` `@97f6a8b70`. Only the pre-ruling prototype exists, under `deliverables/`. |
| `resource_heat_snap` | **Zero code repo-wide.** Its own design doc reads `Status: RESEARCH / DESIGN`. |

>> **These are cycle-22's F1 and F2 recurring in a SECOND document — so they are not local to
>> `03_comp_tools.md`.** The chain is labelled **APPLIED**, which is the word that makes it a defect
>> rather than a roadmap: a reader is told this composition runs, when one link has no implementation and
>> another names a tool a ruling deliberately prevented from existing. <<

## Routed

Repair line 21 in `05_learning_loops.md` — `comp-debris-ext` → `comp-debris --types`, and mark
`resource_heat_snap` as designed-not-built or drop it from an APPLIED chain → CTO~Z. **Same two repairs
already routed for `03_comp_tools.md` at cycle-22; this is a second site, not a new defect.**

**Worth pairing when that repair is scoped:** if these two names propagated to a second doc unprompted,
the repair should sweep for other sites rather than fix the two I happened to land on. **I have measured
two documents; I have not swept `infra/system/` for further occurrences.**

---

## Compiler Tools

| Tool | Result |
|---|---|
| `comp-system --check` | CURRENT |
| maturity-line arithmetic | 11 = 11, and 11+2 = 13 = declared ✓ |
| `git cat-file -t` on 3 cited commits | all `commit` — none dangling |
| `focused_coupling_ratio` source grep | `@0.12` live |
| occurrence count of the two cycle-22 artifacts | 1 each in this doc |

**Denominator:** I checked 6 falsifiable claims in a 23-line doc and read every line. **I did NOT verify
that the 5 PROMOTE invariants "each BITE in the 13/13 self-test"** (line 16) — that needs the self-test
run, which I did not do. Stated rather than assumed.
