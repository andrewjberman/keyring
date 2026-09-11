# Two corrections from Andrew in one stretch, and the second one found a CHAIN where I had written a FORK -- 2.0.0_SA_COO~Z

**archetype:** MIXED

**Date:** 2026-09-11
**Task Order:** none held at open; SEATED mid-stretch on POSN_ASTTAX (`1.0.0_SA_CTO~Z` msg 21150, Andrew-direct "do it")
**Status:** Both seated tasks COMPLETE. Every next act gated on Andrew, the CTO, or the sign-offs.

---

## Objective

Continue from the 0155-0215Z log. Ended up: dissenting on one PRD, authoring a macro-enum record that
differs from the one I was handed, and being corrected by Andrew twice -- once on judgement, once on
instrument.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| prd-stamp | `--self-test`; `status` x12 (every PRD in the tree) | PASS / 16 arms 0 fail | 12 of 12 read `NEXT: L4`; see "What failed" -- the escalation was withdrawn |
| comp-find | `\bPOSN\b`, `\bETFS\b`, `\bPOS\b`, `\bposn\b`, `ETFClassifier`, `get_asset_class`, `rv0057-f001`, `--name stamps` | PASS | the `get_asset_class` DEF census is what located the six vendored classifier copies |
| comp-read | `etf_classification.py`, `etf_classifications_dynamodb.py` (`--for`) | PASS | surfaced BOTH modules' "single source of truth" self-claims, and the `ETFClassifier` class Andrew named |
| comp-surprise | `--project NFRA_OPSEC202609 --armed --json` | PASS | 193 items / 0 OPEN / **95 ARMED**, 54 naming this lane |
| to-check | `--all --assignee` x2, `--project` | PASS | 0 active TOs at this seat |
| safe-commit | x4 (log, dissent, D4 record, Andrew-direct + L5 draft) | PASS | all gates clean; all four verified ON ORIGIN by ls-remote |
| git (anchored author) | `--author "2.0.0_SA_COO~Z <"` | PASS | after the naive form returned a SIBLING lane's commits -- banked |

**What worked:** running `comp-surprise --armed` at all. `0 OPEN` is what a close is graded against and
it was right; nobody had asked the adjacent question and the adjacent question had 95 in it. The CTO
ruled terminal-by-closure and I verified its guard per-row (95/95) instead of citing back the aggregate
we had both already used.

**What failed -- TWICE, and both are Andrew's corrections, not mine:**
1. ⛔ **I graded a tool built 40 minutes earlier against PRDs authored before it existed.** Reported "12
   of 12 PRDs read NEXT: L4, 0 stamps estate-wide" as a finding with denominators and a discrimination
   test. Andrew: *"the stamp is a new tool, you cant judge things on other fabrics at other time based
   on a tool that was just created right now."* Correct. An empty ledger on a new instrument is its
   expected state. Worse, I had it both ways -- wrote "cold-start, not a logic bug" and then built the
   message around a FALSE HOLD hazard whose victim required a COO lane to ignore its own dispatch,
   register and decomp. Withdrawn in full (21140). ⭐ **The rigor is what made it dangerous:** printed
   denominators and an independent instrument applied to a question that should not have been asked
   produce a finding-shaped artifact, which recruits a reader's trust before its premise is examined.
2. ⛔ **I audited the instrument instead of doing the work.** Andrew: *"what you should be doing is
   reading the PRD critically and either stamping or dissenting."* The stamp is a JUDGEMENT act. I had
   never opened the document.

**Gap found:** on NFRA_REPORT's 95 armed rows, 77 read `UNDER_INVESTIGATION` in their OWN disposition
field -- graduation lives only in the LATEST CARRIER. A seat re-deriving from the row field gets 77 OPEN
on a closed project and reopens a correct close.

---

## Work Completed

### 1. NFRA_OPSEC202609 post-close residue -> a ruling

95 ARMED / 0 OPEN measured AFTER the close, 54 naming this lane. Surfaced to CTO+CVO with the five
substantive rows named (cleartext JWT signing secret on a live auth path; a third undeclared grant on
`table/opal-users`; Terraform as an unseen second writer of all four blocked-IP sets; the rotation
blocked in three places; opalinvest.com outside this AWS account). `1.0.0_SA_CTO~Z` RULED
terminal-by-closure, no bulk-disarm. Guard verified per-row 95/95, discriminator returned.

### 2. NFRA_REPORT v0.8 -- READ IN FULL, **DISSENTED** @`0ea9ef712d`

756 lines. Three grounds: **FWD-13 and FWD-15 are served by NO engine row** (subtraction: 21 declared,
19 covered) while s.8 still prints "12 of 12, 0 uncovered"; prose v0.7 vs JSON v0.8 with no v0.8
changelog entry (v0.8 added the nine FWD-13..21); S1 names two axes while s.6 rules a third lands at L5.
Sign-offs recorded as a CONSTRAINT on my act, explicitly not as a criticism of the L4 delivery -- that
gate postdates the PRD, and repeating error (1) two hours later was the thing to avoid.

### 3. POSN_ASTTAX seated -- TASK 1: the D4 Rule 24 record @`425b11ccb1`

**REC `[POSN, ETFS]`, differing from the `[POSN]` I was handed.** ETFS_CANON reads `status: scoping`,
its code CONFORMS, and Andrew's own re-entry condition (*"We can revisit ETFS_CANON After INGEST is
done"*) has FIRED -- ETFS_INGEST is complete. `[POSN]` alone would bar it permanently on day one. D9's
precedent points the other way once read at its REASON rather than its shape. Domain falsified by an
unscoped read before subtracting (360 rows; D4 = the 6 declared; holds). Own census with positive,
negative and case controls.
⚠ **Disclosed against myself in the record:** my first unscoped probe split Windows paths on `/`, so no
basename matched and it reported all six rows OUTSIDE the domain -- "subtraction VOID", the most
dramatic line available, from a bug.

### 4. TASK 2: the L5 decomposition draft @`6ffdaa8ccb`, and Andrew's second correction

Drafted 7 cells over the PRD's 3 engine rows, coverage 6 of 6 by subtraction. Grounded it first --
which is where it got interesting. Both candidate classifiers **self-describe as the single source of
truth**, so I could not break the tie by reading either. Andrew: *"I think ETFClassifier is the real
one"* / *"check to see what is already hooked up to Positioning page thats how youll kow for sure."*

Executed: `yang-generate-positioning/lambda_function.py:25-31` imports and instantiates
`ETFClassifier`. **He is right.** ⭐ **And following his instrument all the way falsified my own draft:**
`seed-etf-classifications.py:58` writes the DynamoDB table FROM the hardcoded dict, so it is **one
chain, not a fork** -- authoring -> seed -> store -> serving. Corrected in the same commit as the record.

Two further measurements, both landing on outcomes: the live Positioning vocabulary is FOUR values and
matches no document (three docs, three vocabularies, none the ratified five); and **three unknown-ticker
defaults in one file that disagree** (`:209`->fixed_income, `:360`/`:520`->equity), which absorbs an
unrecognised vol product into Equity by a route independent of the vol/hedge mapping -- so FWD-1 grades
GREEN on the broken system. Cut as its own cell.

### 5. Merge window

Held on 21164, resumed on 21171. Verified all four commits ON ORIGIN by my own ls-remote read rather
than the integrator's line, and checked the merge's 90 commits against the seven files my records cite:
**0 touched.** Every citation holds at the new head.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Withdraw 21139 in full rather than defend the surviving half | the premise was wrong; the CTO found and fixed the narrow half itself |
| DISSENT on NFRA_REPORT rather than stamp | decomposing it cuts 19 of 21 and L6's id-scoped limb passes anyway |
| Differ from the CTO on the D4 enum | ETFS_CANON is live, conforming, and its re-entry condition has fired |
| Do NOT flip MACROS.yaml | ratification is Andrew's alone; a record is not a flip |
| Correct the L5 draft in the same commit as the Andrew record | a wrong framing already committed is not fixed by a later note |

---

## Blockers

**None at this seat.** Everything ahead is someone else's act, named:
- **Andrew:** ratify D4 (`[POSN, ETFS]` rec); the `ASSETCLASS_TAXONOMY` -> `POSN_ASTTAX` rename -- ⛔ the
  macro alone does NOT clear the tree grammar, the current code is REFUSED.
- **`1.0.0_SA_CTO~Z`:** tree registration after the ratify; the NFRA_REPORT L4 edit that unblocks its L5.
- **CRO + CVO:** the L4-R sign-offs, which gate L6 issuance, not L5.

## Current State

0 open TOs · 0 unread · zero crons · `/drive` correctly unarmed (stop condition met on both limbs) ·
Monitor `b8ern07oc` live and parent-tied. Five commits tonight, all verified ON ORIGIN
(`origin/SITEZ 26faa1485e`, ls-remote read).

## Next Steps

1. **[Andrew]** the D4 word. One word either way; it unblocks the whole tree path.
2. **[`1.0.0_SA_CTO~Z`]** NFRA_REPORT L4 edit -> this seat decomposes and stamps the same turn.
3. **[this seat]** on the D4 ratify: formalize the L5 draft in the tree, then L6 -- gated on the
   sign-offs, which LIMB 6 enforces.
