# POSN_ASTTAX -- ROUND 1 DECOMPOSITION: ONE cell

**archetype:** DIAGNOSE

**Owner (L5-L6):** `2.0.0_SA_COO~Z` · **Date:** 2026-09-11 ~05:5xZ · **Directive:** D4 · **Macro:** POSN
**PRD:** `../prd/POSN_ASTTAX_PRD.md` v0.1, content pin `66e4398f5042`
**Project rectangle (all seven cells):** `POSN_ASTTAX_DECOMP.md` -- this file is ROUND 1's slice of it.

---

## Why this file exists, and it is a gate refusal rather than a preference

`.tools/to-pipeline-gate.py` enforces spine v3.0 L6 literally: **ONE issuance covers EVERY cell of the
decomposition it names.** The round-1 issuance names ONE order, and the project rectangle declares
seven cells, so pointing the order at the rectangle refused with *"owns 1 of 8 cell(s) ... MISSING:"*
and the offer of an audited `# pipeline-override:`.

⛔ **THE OVERRIDE WAS AVAILABLE AND IS DELIBERATELY NOT TAKEN.** The estate's own precedent is a
decomposition PER ROUND (`NFRA_OPSEC202609_DECOMP_round3.md`, `..._round4.md`, the latter covering a
single cell), and a per-round file expresses "this round is one cell" as DATA the gate can grade,
where an override expresses it as prose the gate is told to ignore. **An override would have bought the
same commit at the cost of turning a graded invariant into an unchecked assertion** -- and the
invariant it suspends is precisely the one that stops a cell being cut into no order, which is the
defect this seat dissented on in `NFRA_REPORT` six hours ago.

## The round-1 cell

| cell id | readable name | PRD surface row | outcome | order |
|---|---|---|---|---|
| **`AT1-s-1`** | S1-a MAKE ONE PLACE THE ONE PLACE | S1 | FWD-5 | `POSN_ASTTAX.TO-S1A-1` |

**COVERAGE:** cells in this round 1, cells covered by the issuance 1, **uncovered 0.**

### The boundary

The SERVING source is settled -- Andrew-direct 2026-09-11 ~04:2xZ (*"I think ETFClassifier is the real
one"* / *"check to see what is already hooked up to Positioning page"*), confirmed at
`yang-generate-positioning/lambda_function.py:25,:31`. **What is open is the AUTHORING end.**
`seed-etf-classifications.py:58` writes the DynamoDB table FROM the hardcoded dict, so FWD-5's "one
place" has two candidates with opposite failure modes: edit the table and the next seed overwrites you;
edit the dict and nothing serves it until the seed re-runs -- and **that trigger is UNMEASURED.**

This cell MEASURES both ends and the drift between them, and **changes nothing**. Naming which end
becomes the single source is an architecture call graded at L9 on the cell's facts, not made inside it.

## Why round 1 is ONE cell and not seven

The rectangle's dependency chain puts `AT1-s-1` at the head with no predecessor and states that it runs
alone. Every later cell WRITES a class definition, and a class definition must be written **where it
survives the seed** -- which is exactly what this cell establishes. A cell cut beside it would be
writing against an unknown write surface, and a worker's write surface is exactly the `<paths>` its
order names. The six later cells (`AT1-s-<n>`, n=2..7 in the rectangle) are **NOT cut, NOT staged and
NOT assigned**; they belong to a round that opens on this round's analysis.

## Fan-out

`fanout: 1 of 1 chains, cap 8` -- one chain head, one order, one worker slot
(`0.9.0_WK_POSN_ASTTAX~1`).

## What this round does NOT do

No code change, no infrastructure change, no class-edge decision (`C-MEMBERSHIP-AT-L5` reserves those),
no retirement of either classifier module, no PRD amendment, and no new scheduled job or monitor -- a
finding that the seed has no trigger is a ROW and a report, explicitly not authorization to build one.

**Push state:** LOCAL at authorship; `0.0.0_AB_MSTR~Z` holds all pushes.
