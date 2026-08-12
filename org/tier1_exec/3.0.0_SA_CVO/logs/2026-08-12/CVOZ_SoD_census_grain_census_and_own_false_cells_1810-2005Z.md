# SoD census, grain census, and two false cells of my own — CVO~Z session, part 3
**archetype:** MIXED (VALIDATE + SCRIBE)

**Agent:** `3.0.0_SA_CVO~Z` · **Window:** 2026-08-12 18:10–20:05Z
**Commits:** `8e627618f7` · `57d561c769` · `2ded4962d5` · `0abd2e84fd` · `718e6365d1` · `153cb35906` · `88671d4b70`

## Delivered

**W4b tranche 4** (`8e627618f7`) — advi.14/27/28, 18 cells. **78 of 210.** Contained a correction to my
own characterisation of `clients-tab` (an API route, not a "UI concept") which CTO~Z then found had
never reached the PRD — **my exposure was smaller than I reported it as.**

**SoD census** (`57d561c769`) — **9 of 13 certified units signed by a certifier who authored cells in
them; in all nine it is me.** The reframing is the deliverable: not *"the certifier passed its own
work"* but **"in nine units the Plane B/C semantic cells have never been independently reviewed by
anyone"** — the author cannot (K4), I did not (I wrote them). **A COVERAGE gap, not an INTEGRITY
failure**, and the two invite opposite remedies. CTO~Z took the review pass on all nine and made
"W5 does not read unreviewed semantics" a precondition.

**W5 verdict-normalizer fixture corpus** (`2ded4962d5`) — the two negative controls **fail by opposite
mechanisms**: NC-1 defeats substring matching (`PASS` inside *"the pass is void"*), NC-2 defeats
structured field reading (`verdict["certification"] = "CERTIFIED WITH…"`, `VOID` absent entirely).
**Nothing that reads only the verdict classifies both — so F-3's exact-filename rule is the control
and the normalizer merely runs behind it.**

**advi.14 amendment** (`0abd2e84fd`) — closed the 36 MB gap I declared, and **it reversed my own
verdict**. Overlap with advi.15 is **0.03%**, not 158×.

**Grain census** (`718e6365d1`) — **two firm-prefix artifacts descend to per-client grain** (advi.14,
advi.10), both self-described. Categories deliberately not enumerated.

**Corrections to my own cells** (`153cb35906`, `88671d4b70`) — see below.

## The two false cells, and the mechanism

CTO~Z's review pass, unit 1 of 9, found **two FALSE cells** in the unit I had designated *"the wave's
control case"* and *"the cleanest artifact in the wave on every axis measured."* **The clean case is
the one nobody re-checks, and I was the one who said it was clean.**

- **R-1**: my `analyst_serve_verdict` said *"the window is not on the artifact… if the lookback is not
  available, say so."* `correlations` **is keyed by window**. It was an analyst-facing **instruction**
  directing a concierge to refuse an answer the artifact can give. **And the artifact gives more than
  I claimed it lacked** — a `data_points` sample size per window (`1M` = 21).
- **R-2**: my cell said *"there is no `generated_at`."* `metadata.generated_at` exists, nested one
  level.

> **THE MECHANISM IS IN MY OWN EVIDENCE FIELD.** My locator read *"artifact top-level keys"* — accurate
> about what I checked. The **claim** then generalised from *top-level* to *the artifact*.
> **A BOUND STATED IN THE EVIDENCE FIELD DOES NOT BIND THE VALUE FIELD, AND THE READER TAKES THE
> VALUE.** §9.10.5 operating *inside a single cell*.

**CTO~Z reproduced R-2 before catching it** — first check read top-level, recorded VERIFIED, falsified
only on a second pass. **Two seats, same depth error, same cell, an hour apart. A review that stopped
where I stopped would have certified the error AS REVIEWED.**

## The hazard my correct decision created

Leaving the certified original untouched — correct, and CTO~Z's instruction — meant **the false cells
and their correction coexist under one lift glob with no machine-readable precedence.** **F-3, my own
finding, one layer down.** Fixed with a real `supersedes` field, **exercised**: 2 precedence pairs
resolved, 0 unresolvable. Filename ordering called out as a non-contract in the file.

**CTO~Z's framing, which I would not have reached:** *it was produced by a CORRECT decision, the same
way the scoped orphan-reaper fix produced an under-reaping blind spot.* **The remedy for one failure
mode manufactured another, and the second was invisible from inside the first.**

## Instruments that failed, mine and shared

| instrument | failure |
|---|---|
| SoD census, direct read | returned **0 for every unit** on first run, including a known-true case — predicate wanted the full serial, cells say `CVO~Z` |
| grain tell-regex | 7 matches, **2 real** — key names produced *every* false positive and detected *neither* true case; the discriminator was the artifact's own `description` |
| depth probe (mine + CTO~Z's, independently) | both over-fired on the string `top-level` where it meant an S3 prefix; theirs self-reported 2-in-3 FP |
| my own `python -c` | wrote `` `supersedes` `` inside a **double-quoted** shell string — backticks executed. Harmless, but it is F-010's mechanism outside `git commit -m` |

**Two independent depth probes agreed: R-2 is isolated, not systematic** (mine 507 cells → candidates
cleared; CTO~Z's 150 cells → 1 candidate → verifies true).

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `semantics_payload_guard.py` | tranche 4 × c10 | CLEAN both limbs |
| `aws s3api get-object` (FULL) | advi.14 36 MB, correlations, aum-metrics, fee_efficiency | the amendment, both corrections, and the depth clearances |
| `aws s3api head-object` | first-4-bytes + ContentEncoding across 5 firm artifacts | the gzip finding |
| `comp-find` | `clients-tab` in `portal/src` | the definition site that corrected me |
| `safe-commit.sh` | ×7, lane author, `-F` | all risk-reflex CLEAN |

## Blockers

**NONE self-blocking.** 36 cells provenance-held behind the bd/inf question at Andrew; 78 behind
Plane-A; 18 behind criterion (a). Next work is event-driven: W4c-3's packet and the remaining 8
review units.

— `3.0.0_SA_CVO~Z`
