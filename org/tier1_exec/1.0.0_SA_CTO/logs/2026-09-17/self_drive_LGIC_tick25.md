# /self-drive LGIC -- ticks 24-25 (2026-09-18 ~01:2xZ to ~01:5xZ)

**Scope:** `LGIC_NAMING, LGIC_ENFORCE, LGIC_CANON, LGIC_LGCTFM`. **Device:** laptop. **State:** ARMED.
Predecessor log: ticks 21-23 @`99038867f5`.

## SCOPE STATE

Zero flags across all four. `LGIC_NAMING` complete/CLOSED; `LGIC_ENFORCE` EXECUTING with **round 5 CUT AND DRAINING**
(`EN-g-30` drained @`921092060f`, `EN-h-29` executing, 2 queued); `LGIC_CANON` EXECUTING, PRD ADMITTED at v1.7;
`LGIC_LGCTFM` EXECUTING, round 1 one cell from terminal (`LT-x-1` re-handed with R-40 applied).

**COMPLETION TEST: NOT DONE -- 1 of 4 complete** (denominator 4). 4 REACHABLE, 0 UNREACHABLE.

## ACTS

| # | what | hash |
|---|---|---|
| 1 | `NFRA_MCPINDEX` v0.5 -- the two narrating sentences deleted from the ENDPOINT section | @`b7dc80e2cc` |
| 2 | **`NFRA_MCPINDEX` ADMITTED**; register row + compiled sequence moved with the gate | @`3ce018566e` |
| 3 | **R-43** -- the PRD is the authority over a decomposition on a gate; an amendment that LIFTS a gate names that gate's carriers | @`50e51bd8d3` |
| 4 | `3.0.0_SA_CVO` nudged out of an idle-at-prompt state holding three already-delivered items | (no commit) |

## THE TICK'S FINDING: A GATE PROPAGATED TO 22 CARRIERS AND ITS LIFT REACHED 2

`2.0.0_SA_COO~G` @`a0a63bcc1a` found that `LGIC_CANON_DECOMP.md` says in FOUR places that `C6` STAYS NOT CUT on
Andrew's `G-N` word and on `ADVI_FIRMBKTS`'s repoint -- **both LIFTED in the PRD, neither lift reaching the
decomposition**, which was last cut against v1.5 while the PRD is ADMITTED at v1.7. **The defect is this seat's:** when
this seat took the PRD to v1.6/v1.7 and issued R-34, it moved a GATE and censused nothing.

**Measured over 1087 files under three roots:** `G-N` in **22** files, `ADVI_FIRMBKTS` in **47**, and **`R-34` -- the
LIFT -- in SIX, only TWO inside the project** (the PRD and the project row).

⛔ **AND THE REMEDY IS ONE DOCUMENT, NOT A SWEEP.** Of the 22 carriers, **all twelve task orders mentioning `G-N` read
`complete`** -- frozen history, CORRECT at their vintage. A round-1 analysis SHOULD say what was true in round 1;
rewriting it would falsify a record rather than repair one. **Only a carrier read as CURRENT DIRECTION can be stale**,
and exactly one qualifies: the decomposition (`G-N` x11, `ADVI_FIRMBKTS` x6, **`R-34` x0, `CARDED` x0**). Correction
rides `LGIC_CANON`'s L5 re-cut at `2.0.0_SA_COO~G`, which that lane proposed before this ruling existed.

**The near-miss is that lane's to be credited with:** reading the DECOMPOSITION first, it drafted the OPPOSITE claim
into `org/XXX.md` -- that an unlifted Andrew gate held `C6` -- **which would have parked the project on a hold he had
already released, in the file every seat reads at startup.** Caught by verifying its own sentence at the bytes before
committing, not by re-reading it.

## SEAT WATCH -- and the refinement now cuts BOTH ways

Tick 24 found `3.0.0_SA_CVO` idle at an empty prompt, its closing line listing three items it believed it was owed --
**all three already delivered and unread in its inbox.** That is the expensive form: the seat believes it is waiting,
and the thing it waits for has already arrived. One nudge naming the three resumed it; the MCPINDEX half signed minutes
later.

**Tick 25 found the same seat IDLE and did NOT nudge it**, because nothing is owed to it: every PRD half is signed, and
round 5's and round 3's L8 hand-offs do not exist yet. ⛔ **IDLE IS NOT STALLED WHEN THE QUEUE IS GENUINELY EMPTY**, and
a nudge into a seat with no work is noise that trains the next reader to ignore nudges. The discriminator is not the
seat's state -- it is whether anything is OWED, which is read from the artifacts, not from the roster.

## OPEN

1. `2.0.0_SA_COO~G`: ENFORCE round 5 draining; LGCTFM `LT-x-1`; then LGIC_CANON's L5 re-cut (v6) carrying G-N's lift,
   R-34 and FWD-5's CARDED carve-out.
2. `2.0.0_SA_COO~O`: OG-q-5 half two, then the one C3 cell (R-OG-18).
3. `2.0.0_SA_COO~B`: IRPT_BCKEND round 3, cut @`e7b61b4936` off this seat's round-2 analysis.
4. **Andrew: gate G-A, and the LGCTFM ANDREW_CARD** (round 1 not terminal, so the fallback has not triggered).

## Compiler Tools

`sequence-check.py` (read + `--compile`), `prd-signoff.py status` x2, `missions-tree-index.py check`, a 1087-file token
census across three roots, per-order `<status>` parsing, `get_delivery_state`, `unstick.ps1 -Peek` x2 + one nudge,
`safe-commit.sh` x4.
