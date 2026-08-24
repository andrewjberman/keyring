# CERT — ADVI_STITCH Phase-A stage-3 decomp

**Certifier:** `3.0.0_SA_CVO` · **Requested:** COO 66825 · **Subject:**
`workflows/atom_decomposition/runs/advi-stitch/20260824T222500Z/DECOMP.md` @`3ee0bec43b`
**Date:** 2026-08-24 ~22:3xZ · **LOCAL at cert time** (rides integration; stated, not called landed).
**Bar:** `CERT_BAR_v2_20260824.md` — **the first cert run under v2, i.e. the first to carry check 7
(ORACLE VIABILITY).** Alternate post-invalidation signer: base `1.0.0_SA_CTO` only.
**Third and last of the three 49F decomps in the CTO dispatch order (PERFRP → INSURE → STITCH-A).**

## VERDICT

**CERTIFIED on the ENUMERATION. 32 of 32, both symmetric differences EMPTY, criterion-bearing 26,
check 7 PASSES on a stated sample. No P1. No correction owed.**

## MECHANICAL — measured at this seat

| | measured by me | COO stated |
|---|---|---|
| cells declared (leading table cell, markup-stripped, `STI-` qualified) | **32** | 32 |
| by surface | **inv 6 · a 4 · b 6 · c 2 · d 6 · e 2 · g 6** | — |
| duplicates | **EMPTY** | — |
| mentioned-but-not-declared | **EMPTY** | — |
| declared-but-not-mentioned | **EMPTY** | — |
| criterion-bearing (32 − 6 boundary `g`) | **26** | 26 |
| criteria → cells | **0 → NOT-YET-EVALUABLE** | stated as such |

**Extractor controls: 5/5** — `inv-2` PRESENT ✓ · `b-0` PRESENT ✓ · `g-5` PRESENT ✓ · `zz-9` ABSENT ✓
· `g-99` ABSENT ✓.

⛔ **MY EXTRACTOR FAILED FIRST, AND ITS CONTROLS ARE THE ONLY REASON I KNOW.** My first pass returned
**0 declared** against COO's claim of 32 — a result that, taken at face value, would have been a
catastrophic false finding against a clean document. **I had guessed the id prefix `STC-` from the
project name STITCH; the document uses `STI-`.** The controls fired immediately (`inv-2` and `b-0`
both expected PRESENT, both read ABSENT), which is what sent me to the source instead of to a
message. **Fourth extractor adaptation this session, and the same class MSTR filed against themselves
an hour ago: A PREFIX I DID NOT READ FROM SOURCE IS A GUESS, AND A GUESS THAT RETURNS ZERO IS
UNRESOLVED, NOT ABSENT.** *(Also excluded as a substring artifact of my own regex: `e-2024`, which is
"pre-2024" in prose. Inspected, not reported.)*

## CHECK 7 — ORACLE VIABILITY (new in v2). **SAMPLED: 5 artifacts. THE DENOMINATOR IS STATED BECAUSE THE CHECK IS NOT EXHAUSTIVE.**

| # | oracle's named artifact | measured | verdict |
|---|---|---|---|
| 1 | `opal-data-bd` top-level prefix count (`b-0`/`g-5`, "4 in / 30 present") | **30** | EXACT |
| 2 | the four in-scope prefixes `backfill_v2/`, `forwardfill_v2/`, `silver/`, `gold/` | all **PRESENT** | PASS |
| 3 | `b-1` sizing "292 + 636 keys" | `backfill_v2/` = **292**, `forwardfill_v2/` = **636** | **EXACT, both** |
| 4 | the three BD-calculated gold series source (`gold/canonical/`) | **21,828** keys, present | PASS |
| 5 | `c-1`'s key of record `dim_account_xref` (BD-side, `opal-data-assets/blackdiamond/49f/silver/`) | **PRESENT** | PASS |
| — | **negative control**: a fabricated prefix | **0 keys** | the probe discriminates |

**Every sampled oracle names an artifact that exists, and two sizings reproduce to the key.** Oracles
whose artifacts do not yet exist (`bronze_legacy/`, `silver_legacy/`, the landed censuses) are
**declared NOT-YET-BUILT with the act that creates them** — which is exactly what check 7 asks for
instead of existence.

## AGAINST MY PRE-STATED STITCH ITEMS (66357), each measured

| stated item | verdict |
|---|---|
| (a) Phase-B cells **ABSENT BY DESIGN**, stated on the face so absence is not read as a CE miss | **MET, and exceeded** — declared in the stage-3 open AND the Phase-B surfaces **enumerated as boundary cells `g-1..g-4`**, so the absence is *visible* rather than asserted |
| (b) `bronze_legacy`/`silver_legacy` four-postulate record at decomp | **MET** — `R-s1`, and it earns (iii) on the STATE distinction (live-refreshed vs frozen-never-refreshed = two states on one tier axis) and (iv) on the asymmetry (a live tier's shape change is normal; a legacy tier's would be a Rule-25 DEFECT — that asymmetry IS the reason for separate names) |
| (c) census-first on the 2,152 absent and the 826 as UNKNOWN(elsewhere-candidate) | **MET** — `d-1`, `d-2`, with a DROPPED verdict on an open BD account **FORBIDDEN in Phase A** |
| (d) copy-as-is invariants, nothing re-derived | **MET** — `inv-2` (sha256 source == destination) + `inv-5` (closed-period immutable) |
| (e) `dim_account_xref` as key of record, never re-derived, seed 5,375 measured against the landed copy | **MET** — `c-1` + `inv-3` |

## THE FINDING IN THE DECOMP THAT I WANT CITED ELSEWHERE

**"Migrate the BD history" is FOUR PREFIXES OF THIRTY.** The PRD's territory names four; the other 26
include a `bronze/`, a `canonical/`, a `platinum/` and a `schwab/`. `b-0` declares the migration's
SCOPE SET **before any object moves**, and `g-5` records the 26 as out-of-territory.

**A MIGRATION SCOPED TO A BUCKET RATHER THAN AN ENUMERATED PREFIX SET HAS NO DENOMINATOR, AND ITS
COMPLETENESS CAN NEVER BE CHECKED.** That is COO's sentence and it is the most reusable thing in this
run. I verified the 30 independently and the four are all present.

## WHAT I DID NOT VERIFY (declared)

- **Check 7 is a 5-artifact SAMPLE.** I did not verify every oracle in 26 criterion-bearing cells, and
  a certifier who did would be re-doing the DS lane's work.
- **The seed-xref count 5,375** is COO's measurement; I confirmed the prefix EXISTS, not the row count.
- **Q-s1's live question** (whether the parquet-deny bucket policy reaches `bronze_legacy` as a
  distinct segment) is routed to CTO and **UNVERIFIED by me** — COO is right that if the mechanical
  guard does not reach the legacy tier, the no-parquet property rests on `inv-2` alone. That is a real
  residual, correctly surfaced rather than assumed.
- **No exercise.** Every oracle here fires at TO time.

## WHAT COO SHOULD HAVE ASKED BUT DID NOT

**What happens to the 26 out-of-territory prefixes when `opal-data-bd` is eventually decommissioned —
and who is holding that clock?** `g-5` correctly scopes them OUT and points their disposition at
DATA_PIPMAP's grammar work. But STITCH's own purpose is that the BD history is *kept* because it
matters for backfill and SI attribution — so this project is establishing that **four prefixes are
worth migrating**, while 26 remain in a bucket whose whole reason for existing is being migrated away
from. **Nothing in either project's decomp owns the question of whether any of those 26 carries
something the 49F program will later need.** The cheap form is not a migration: it is `b-0`'s scope
list gaining a one-line *reason-not-in-scope* per excluded prefix, written now while the person who
enumerated them still remembers why. **A scope set that records what was excluded but not WHY cannot
be re-audited by anyone except its author** — and this is the third decomp today whose sharpest risk
is a seam neither of two live projects owns.

— `3.0.0_SA_CVO`
