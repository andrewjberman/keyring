# AMGT_HARVST round 2: CVO adjudication

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-09-23T02:5xZ at HEAD after `533fec7afb`, LOCAL on SITEZ.
**Inputs:** `2.0.0_SA_COO~Y`'s packet @`533fec7afb` (11,126 bytes), the five orders, the channel's 26 rows, the
amended spec read in full, and `2.0.0_SA_COO~Z`'s evidence message on the two cited row ids (msg 24561, supplied
as evidence and explicitly not as a verdict).

## Round state

**5 of 5 terminal.** Sweep **PASS 21 / FAIL 0 / UNVERIFIABLE 1 of 22** over 5 orders; the one unverifiable is the
judgment criterion below. **ZERO vendor calls this round**, read from a counter rather than asserted.

## JUDGMENT -- `HVST-r-1` AC4: **PASS**, and the gap I failed it on is closed

**The question:** does the amended spec now draw every state, including the call's own failure, such that a build
cannot reproduce the `Z-S227` / `C-S400` defect on this surface?

**The amendment is +30 lines, nothing outside the spec file.** Read here:

- **§5, the error envelope.** Every route, on a non-200, a timeout or an exception, returns ONE shape:
  `{"error": true, "error_code": <stable token>, "message": <reason>}`. ⭐ **And the clause that matters most is the
  prohibition, not the shape:** a response carrying `error: true` is **never merged into `series`, `events` or
  `articles`, and never rendered as a zero-length version of them** — because an empty array means "the call
  succeeded and there is nothing in range," which is a different, honest state.
- **§6, the failed-call state.** "The timeline request itself failed" is now enumerated beside the other five, and
  it is decided **by the transport/envelope outcome, never by any row `chatter_daily` holds.** Never a blank chart,
  an empty series or a zero-height line, because each of those reads as "we hold nothing" while this state means
  **"we do not know what we hold."** It renders a distinct page-level state with a retry, and **a failed dissection
  call shows the state in its own panel without forcing the line into it.**

**`2.0.0_SA_COO~Z`'s distinction is the right test and I applied it:** `Z-S227` is an error DISCARDED at the call
site (omission); `C-S400` is a component that **cannot receive one** (assertion). A spec that merely draws the
failure prevents the first and not the second.

**Both are prevented here, and by different clauses:**
- `Z-S227`'s class: the state is enumerated, so a build that renders nothing on failure is off-spec.
- ⭐ **`C-S400`'s class: the spec forbids the ASSERTION FROM ABSENCE directly** — an empty array may not be rendered
  as a failure, and the failure may not be rendered as emptiness. That is exactly the overlay's sentence, outlawed
  at the spec level rather than left to the component's contract.
- The per-panel independence clause requires the dissection panel to show the state **on its own**, which a build
  cannot satisfy without the failure reaching that panel.

**CARRY, for the BUILD cell's own criteria rather than the spec:** the spec prescribes no `.tsx` by design, so the
TYPED CHANNEL is the one thing it cannot fix. **The build cell must prove the failure reaches each rendering
component through its own input, never inferred from an absent or empty value** — that is `C-S400`'s mechanism and
it is checkable only in the build. I state it here so the criterion exists before the cell is cut.

## The round's real finding: `Z-W15-S1`, and its consequence for the vendor hold

The harvest-mode listing persist sits **AFTER** the whole per-article loop, so a job that raises mid-loop discards
every listing page already held in memory. Seeking-alpha fetched multiple listing pages and then took an HTTP 502.

⛔ **That moves FWD-1's listing half from "the publishers refused" toward "our code discarded it."** At round 1 I
graded FWD-1 NOT REALIZED with listing pages at wsj 2 and every other publisher 0, and the reading then was
sessions. **A third cause now exists and it is ours.** **CONSEQUENCE, and the issuer states it rather than asking
for the act: a fourth vendor act would NOT reliably produce listing pages for any publisher whose job raises after
page 1.** GRADUATED, and it is a cheap round-3 candidate.

## `Z-S4`: the issuer's own defect, and the shape is worth more than the instance

Three of five worker rows have ONE root cause — the ten-path sparse cone every worktree was dispatched with, chosen
because a full checkout risks an out-of-memory failure on this device. The sharpest face is `Z-W14-S1`, which
recorded a suite reading "1 failed, 6 passed" as a **third pre-existing repository failure**. It is not: the same
suite reads 7 passed in the full shared tree, and the worktree failure is a `ModuleNotFoundError` on a directory
the cone never materialised.

⛔ **EACH FACE LOOKS LIKE A FINDING ABOUT THE CODE TO THE WORKER THAT MEETS IT, AND THAT WORKER CANNOT SEE THE FULL
TREE.** That is the same family as tonight's manufactured zeros, one level up: **the instrument is the worker's
whole environment, and a defect in it is indistinguishable from a defect in the repository from inside.** No
grade changes — every criterion was met against the population its own order named — and `Z-W14-S1`'s own framing
is corrected by the issuer, about the issuer's own dispatch.

## `Z-S3`: an EXPOSURE, and the wording bound is the right disarm

`r-2`'s verdict names PATHS ("paths_proven 2 of 5") while its evidence covers 14 objects of a 103-object bronze
population, and all 6 objects carrying no `received-form` label sit under the one path the cell grades PROVEN.
**Filed as an exposure because no consumer census exists** — nobody has measured whether anything reads that label.
**The cheapest disarm is the one the issuer names: no later artifact restates "paths_proven 2 of 5" as a claim
about those paths' whole history.** That is a wording bound, not a defect in `r-2`.

```json
[
  {
    "id": "AMGT_HARVST-Z-C-S4",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-23T02:55Z",
    "one_line": "L9 GRADE RECORD for round 2: 5 of 5 terminal, 21/0/1 of 22, zero vendor calls; r-1 AC4 PASSES -- the amended spec closes the gap it failed on, and prevents BOTH cited defects by different clauses (the state is enumerated, and the assertion-from-absence is forbidden outright).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "surprise-row-gate --acceptance AMGT_HARVST --round 2: PASS 21 / FAIL 0 / UNVERIFIABLE 1 of 22 over 5 orders; the one unverifiable is r-1 AC4, the judgment criterion.",
        "SPEC_SECTION_timeline.md read at HEAD: SS5's error envelope returns one shape and forbids merging error:true into series/events/articles or rendering it as a zero-length array; SS6 enumerates 'The timeline request itself failed', decided by the transport outcome and never by a stored row, with a per-panel independence clause and a retry.",
        "git diff of the spec: +30 insertions, one file, nothing under lib, portal or infra.",
        "2.0.0_SA_COO~Z msg 24561, evidence only: Z-S227 DISCARDS an error that exists (omission); C-S400 CANNOT RECEIVE one (assertion). A spec that merely draws the failure prevents the first, not the second."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Spine v3 L9: judgment criteria are graded here and never self-graded.",
    "world_is": "The amendment closes the failed-call gap at the spec level and forbids the assertion-from-absence directly; the typed channel remains the build cell's to prove.",
    "notes": "CARRY for the BUILD cell's criteria, not the spec: prove the failure reaches each rendering component through its own INPUT, never inferred from an absent or empty value. That is C-S400's mechanism and only a build can demonstrate it. The spec prescribes no .tsx by design, so this is not a defect in it.",
    "dismissal_reason": "Grade record: this row carries the round-2 L9 grade and dispositions no item; the enum has no record value."
  },
  {
    "id": "AMGT_HARVST-Z-C-S5",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-23T02:55Z",
    "one_line": "GRADUATED: Z-W15-S1 (the listing persist sits after the per-article loop, so a mid-loop raise discards every page already captured -- a THIRD cause for FWD-1's listing half, and it is ours not the publishers'), Z-S4 (the sparse-cone dispatch, whose three faces each read to a worker as a finding about the code), Z-W11-S1, Z-W13-S1, Z-W14-S2, and Z-S3 as an EXPOSURE with the issuer's wording bound as its disarm.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Z-W15-S1: _write_harvest_listings sits after the whole per-article loop, re-read at the source by the issuer; seeking-alpha fetched multiple listing pages then took an HTTP 502.",
        "Z-S4: the same suite reads 7 passed in the full shared tree and '1 failed, 6 passed' in a sparse-cone worktree, the failure a ModuleNotFoundError on a directory the cone never materialised.",
        "Z-S3: r-2's verdict names PATHS while its evidence covers 14 of 103 bronze objects, and all 6 objects lacking a received-form label sit under the one path graded PROVEN."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "A captured page is persisted; a worker's environment is the population its order names; a verdict's subject matches its evidence's scope.",
    "world_is": "One code defect discards real captures, one dispatch choice makes environment defects read as repository defects, and one verdict sentence is wider than its measurement.",
    "notes": "Z-W15-S1 is the round-3 candidate and it CHANGES THE VENDOR CALCULUS: a fourth act would not reliably produce listing pages for any publisher whose job raises after page 1. Z-S4's remedy is the issuer's own dispatch, not a cell. Z-S3's disarm is a wording bound: no later artifact restates paths_proven 2 of 5 as a claim about those paths' whole history. Remediation rows owed at L10.",
    "adjudicates": [
      "AMGT_HARVST-Z-W15-S1",
      "AMGT_HARVST-Z-S4",
      "AMGT_HARVST-Z-S3",
      "AMGT_HARVST-Z-W11-S1",
      "AMGT_HARVST-Z-W13-S1",
      "AMGT_HARVST-Z-W14-S2"
    ]
  },
  {
    "id": "AMGT_HARVST-Z-C-S6",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-23T02:55Z",
    "one_line": "DISMISSED: Z-W14-S1, whose own framing is measured WRONG -- it records a sparse-cone ModuleNotFoundError as a third PRE-EXISTING repository failure, and the issuer corrected it at Z-S4 about its own dispatch.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "The same suite reads 7 passed in the full shared tree; the worktree failure is a ModuleNotFoundError on integrations, which the ten-path cone never materialised.",
        "No cell's grade changes: every criterion was met against the population its own order named."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "A pre-existing repository failure is a property of the repository.",
    "world_is": "It was a property of the worktree the issuer dispatched, invisible to the worker that met it.",
    "notes": "Dismissed as a row whose finding is superseded by its own root cause; the class lives at Z-S4, which is graduated.",
    "adjudicates": [
      "AMGT_HARVST-Z-W14-S1"
    ],
    "dismissal_reason": "The row's finding is corrected by Z-S4; the environment defect it reports is real and graduated there, and no grade rests on the superseded framing."
  }
]
```
