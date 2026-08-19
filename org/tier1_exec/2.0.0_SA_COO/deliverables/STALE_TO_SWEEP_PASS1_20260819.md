# STALE-TO SWEEP — PASS 1 (mechanical classification)

**Authorization:** Andrew-direct 2026-08-19 ~20:12Z, VERBATIM *"All approved"* on COO `/open-calls`
card 9 (record @1e0ec3b079). **Scope as authorized: CLASSIFY + re-seat-or-supersede. NOT a deletion
warrant** (Rule 25 binds — dormant licenses stop-treating-as-live, never `rm`).
**Instrument:** `python .tools/to-check.py --all` (the `--all` flag is load-bearing; the default view
scopes to PRDs <=14d and goes blind to exactly the longest-stalled TOs).

---

## DENOMINATOR FIRST — AND THE REASON IT LEADS

**359 open (non-complete) task orders across 133 projects.**

| Slice | Count | Share |
|---|---|---|
| Rows carrying a resolvable age | **201** | 56% |
| Rows with **NO resolvable age** (`(?)`) | **158** | **44%** |

⚠ **MY OWN FIRST PASS PARSED 200 OF 359 AND WOULD HAVE REPORTED "ZERO DORMANT TASK ORDERS."** The
regex required an age token, so the 158 undated rows were dropped **silently** — a clean, confident,
well-formed answer over 56% of the board, presented as if it covered all of it. It was caught only
by printing the parse count beside the census self-report. This is the retrieval-control class
exactly, and it is recorded here because the sweep's own instrument nearly produced the reassuring
version of the finding.

---

## FINDING 1 (the headline, and it is NOT "we have dormant TOs")

**THE 90-DAY DORMANCY BAR IS UNEVALUABLE ON 44% OF THE OPEN BOARD.**

- Of the **201 dated** rows: age range **7d - 72d**. **ZERO at or over the 90-day bar.**
- Of the **158 undated** rows: **age is unknown**, so Rule 25 cannot be applied to them at all.

**So the honest verdict is not "no dormant work exists" — it is "on the half we can measure, none is
dormant; on the other half, we cannot ask the question."** Concluding dormancy-free from the dated
half alone would be a firm-scope-style error: the right question asked cleanly over the wrong set.

**REMEDY (pass 2 input):** the undated rows lack a resolvable `Issued:` date. That is a **corpus
defect, not a dormancy finding** — backfill the dates (or fix what prevents `to-check` resolving
them), THEN re-run the bar. Do not re-seat or supersede anything on the basis of an unknown age.

---

## FINDING 2 — THE DEAD-SEAT CLASS (this is the #42 class, and it is AGE-INDEPENDENT)

**~23 open TOs are addressed to seats that are not in the live roster.** This is the class that let
sovereign TO #42 sit **36 days** at `0.5.0_AE_OpalETL~A` — and note it did **not** need to be
dormant by age to be invisible. **A TO at a dead seat has no reader; nothing about its age reveals
that.**

| Seat named | Open TOs |
|---|---|
| `DS_PortfolioAnalytics` | 6 |
| `AE_OpalETL` | 6 |
| `DT_PortfolioAnalytics` | 6 |
| `DE_MarketIntelligence` | 2 |
| `RD_Positioning` | 2 |
| `DS_MarketIntelligence` (+1 joint) | 2 |
| `AE_OpalETL~A` / `~Z` / joint | 3 |
| `DE_PortfolioAnalytics` | 1 |

**This is the highest-value slice of the sweep** and it needs no date backfill to adjudicate.
`AE_OpalETL~A`'s row is already dispositioned: **#42 is SUPERSEDED** by the D7+D9 PRDs
(Andrew-direct, CTO record @3c8c3f1035).

---

## FINDING 3 — 13 UNASSIGNED TOs, ALL UNDATED

`(unassigned)` holds **13 open TOs, 13 of them undated (100%)**. No owner AND no date: neither the
seat axis nor the age axis can reach them. **They are structurally invisible to both halves of this
sweep** and need a human/owner read.

---

## FINDING 4 — LOAD CONCENTRATION (context for pass 2, not a defect)

`AE_CloudOps` **66** · `DS_ClientPlatform` **56** · `AE_CloudComp` **27**. Tonight's D-wave cut added
to the first two. Not a finding in itself — but re-seating dead-seat work onto these two would
deepen a concentration that is already the estate's tightest, so pass 2 should route deliberately
rather than defaulting to the busiest lanes.

---

## WHAT PASS 1 DELIBERATELY DID NOT DO

**No TO was re-seated, superseded, closed, or deleted by this pass** (beyond the two the sovereign
ruled explicitly: `NFRA_AGENTBUS.AB-ACTIVATE` and `NFRA_COMPTEAM.B2-ACTIVATE`, both marked
SUPERSEDED with reasons, neither deleted).

**Adjudicating 359 task orders is a multi-pass job and doing it fast would be worse than doing it
deliberately.** Pass 2 (per-TO disposition) needs: (a) the date backfill from Finding 1, (b) the
dead-seat list from Finding 2 worked with MSTR for re-seat-or-supersede, (c) an owner read on
Finding 3's 13.

**Stated plainly so the authorization is not read as discharged:** the sweep is AUTHORIZED and
STARTED, not FINISHED.
