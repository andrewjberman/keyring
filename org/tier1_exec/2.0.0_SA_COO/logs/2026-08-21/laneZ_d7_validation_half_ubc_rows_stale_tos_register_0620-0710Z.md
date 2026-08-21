# D7 validation half: 7/7 UBC rows upheld, a borrowed control closed, and the register's proposed answer measured at 2 of 9 — 2.0.0_SA_COO~Z

**Date:** 2026-08-21
**Task Order:** ad-hoc — Andrew-direct "bring on COO~Z" (~0450Z), scoped by `0.0.0_AB_MSTR~Z` msg 4201 to three items
**Status:** COMPLETE — validation half ACCEPTED by `1.0.0_SA_CTO~Z` (msg 4212, 0705Z)

---

## Objective

Serve as the INDEPENDENT SECOND READER on the D7 W-F (@04b7dc7ad5) and W-E (@4d5a92f4d7) proof-of-spec
instances — weighted to the 7 UNCOMPUTABLE-BY-CONSTRUCTION rows, which is where a generous later reader
could quietly promote something to PASS. Plus two known-stale TO records (mine to maintain) and a
register-membership PROPOSAL (MSTR's surface to edit). Zero build, zero apply, zero crons.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| proof-of-spec-check | `.py <instance> <id-list>` positional, rc unpiped | PASS | Re-derived both instances independently: W-F 12 rows / W-E 7 rows, violations=0, VALID rc=0 |
| proof-of-spec-check | same, on a scratch MUTANT of the W-E instance | PASS | The control W-E lacked — blanked `output_evidence` -> rc=1, violations=2, INVALID |
| to-check.py | `--project OPAL_TICKET` / `--project D7_TICKETING` | PASS | Found the 2/7 split that falsified the pre-measured register answer |
| to-check.py | `--project D5_ALTRESEARCH` / `OPAL_ALTRESEARCH` | PASS | 2 vs 0 — D5 is the same shape as D7 |
| comp-which (HUD) | fired on a Bash `grep` for the 208-task census | WARN | Correct nudge; the search was a repo-record lookup with no rich-tool equivalent |

**What worked:** `to-check.py --project` was decisive — it converted a plausible register hypothesis into a
measured 2-of-9 in two invocations, which no amount of reading the TO files would have produced.
`proof-of-spec-check` run POSITIONAL with the id list is a real coverage check and it discriminates
(proven by my own mutant, not cited from a sibling).

**What failed:** none crashed. One READING failure was mine, not a tool's: I read `to-check.py:114-173`
and concluded the filename prefix takes precedence over the `<project>` tag. The measurement says
otherwise for the 2 tagged files. **The proposal rests on the measured runs, not on my reading.**

**Gap found:** none new. `comp-adversary`'s four bounds (CVO~Z msgs 4142/4149) did not touch this work —
I did not use it here, so no result of mine is scoped to "what the author cited."

---

## Work Completed

### 1. UBC validation — 7/7 UPHELD, and one control was borrowed

Independent census matched the reported headline both ways: **W-F 12 rows, 8 PASS / 4 UBC** (WF-2, WF-6,
WF-8, WF-11); **W-E 7 rows, 4 PASS / 3 UBC** (WE-1, WE-2, WE-3). Every UBC row refuses a promotion that
was genuinely available — the conjunctive rows (WF-11, WE-1) would have carried an unmet limb silently,
and WF-6's untouched-bytes PASS would have retired a regression criterion without running the regression.
**No row found where promotion would have been defensible.**

I also read the 12 PASS rows, because a PASS-that-should-be-UBC is where a false green actually hides.
Every one is exercised with a mutant or positive control, denominators stated, planes stated.

> **THE FINDING: WE-7's CHECKER-DISCRIMINATION CONTROL WAS RUN ON THE SIBLING W-F INSTANCE.**
> "The checker was proven able to fail" is true in the abstract and **silently changes referent between
> instances**. A control run on another artifact is not a control on this one. Closed by running it on
> the W-E instance directly — anchor-asserted first (exactly 1 WE-4 PASS row, evidence non-empty, refuse
> otherwise), blanked `output_evidence` -> **rc=1, violations=2, INVALID**. W-E's VALID is now measured
> on its own instance. `1.0.0_SA_CTO~Z` recorded this as a standing acceptance requirement.

**Fuse independently confirmed, with a positive control and a denominator:** 0 modified paths under
`integrations/` and `lib/`; `sweep` referenced by exactly **2 of 10** python files under
`integrations/ticketing` (its own module + its own test); 0 edges from `runner.py`; positive control
(8 files carry `def `) proves the search was live, so the zero is a measured absence and not a broken
grep. W-F's commit touches **zero code files** — a second, independent line on the same claim.

**Non-ASCII, attributed rather than alleged.** The seat's `0 non-ASCII` claim was scoped to the HANDLER
and is **TRUE** (handler + battery both 0/0; the U+26D4 strip landed). `main.tf` carries **15** chars
(14x U+2014, 1x U+26D4); the W-E commit added exactly **5 em-dashes**, and the U+26D4 plus 9 em-dashes
are **pre-existing from the W-A lineage**. CTO~Z supplied the mechanism I did not have: `.tf` is outside
the non-ASCII lint's `.sh`/`.py` scope, which is why nothing fired.

### 2. Two stale TO records corrected (my TOs, my surface)

**WE-SITEZ `<status>`** — was `"staged — DESIGN GATE FIRST at 1.0.0_SA_CTO~Z"`. Stale by **FOUR**
movements, not three: the audience ruling (~0450Z, INTERNAL ONLY) post-dates the 0515Z build message
both the build seat and MSTR were counting from. Now records all four, plus the apply bound.

**WF-SITEZ `<cross_domain_coordination>`** — the unmeasured-tasks bound struck and DISCHARGED with the
census in place: **FOUR of 208** tasks execute out of the working tree, controlled both ways (negative
`zzz_no_such_path_9999` -> 0, positive `run_intake` -> 1). The bound was RIGHT to refuse a clean verdict:
two of the three previously-unmeasured tasks ARE exposed. Explicitly recorded that this does **not** move
the TO's `DENOMINATOR: 8`.

### 3. Register membership — PROPOSED, not edited

Deliverable: `laneZ_D7_REGISTER_MEMBERSHIP_PROPOSAL_20260821.md`. MSTR pre-measured the answer as
`OPAL_TICKET` and asked me to check rather than inherit it. **It is 2 of 9** — the open D7 TOs are split
across two project codes (`OPAL_TICKET` -> 2, `D7_TICKETING` -> 7).

> **A PARTIAL FIX THAT LOOKS COMPLETE IS WORSE THAN AN OBVIOUS BREAK.** `0 open` beside eleven files is
> self-evidently broken and invites a look; `2 open` reads as FIXED and stops the investigation, while
> dropping the entire live site-Z build queue.

**11-vs-9 reconciled with nobody wrong:** 11 files on disk, 2 complete, 9 open. MSTR counted files;
CTO~Z counted open; `/directives-check` reports open. A naive `*D7*` glob returns 19 — neither seat
over-matched.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Read the 12 PASS rows too, though weighted to UBC | The asymmetric risk of a false green is a PASS that should be UBC; being pointed at UBC is not a reason to leave the other direction unread |
| Ran my own checker mutant on the W-E instance | Its cited control was a sibling's run; a control on another artifact is not a control on this one |
| Reported WF-6/WE-6 as a PRECEDENT HAZARD, not a defect | Both verdicts are correct; the discriminator is subject-existence, not the byte-unchanged argument. Unstated, a later reader promotes WF-6 by citing WE-6 |
| Attributed `main.tf` non-ASCII by measuring added-vs-pre-existing | The seat's claim was scoped to the handler and true; alleging a contradiction without the diff would have been a false finding against correct work |
| Rejected the naive `[OPAL_TICKET, D7_TICKETING]` membership | Rule 24: `D7_TICKETING` is parser-derived, not registered (0 of 315) — fails same-grain AND state-coherence (one remedy does not move both) |
| Armed nothing, and did NOT strike the live XXX.md `/drive` row | Latest+most-restrictive binds for my own conduct; but striking a sovereign-authored clause off my own launch instruction is the scope-adjudication the law prohibits in BOTH directions |

---

## Files Modified

| Path | Change |
|------|--------|
| `.../task_orders/D7_TICKETING.WE-SITEZ.*.md` | `<status>` rewritten — four movements + apply bound |
| `.../task_orders/D7_TICKETING.WF-SITEZ.*.md` | unmeasured-tasks bound struck + discharged with census |
| `.../2.0.0_SA_COO/deliverables/laneZ_D7_REGISTER_MEMBERSHIP_PROPOSAL_20260821.md` | new — the membership proposal |

Commit `9d1f1b1cd7` (risk-reflex CLEAN — measured, 3 files vs 1662 danger nodes). **Not pushed** — push
is the integrator's window.

---

## Blockers

None. Nothing is applied, no apply is open, the W-F import edge remains unwritten and the fuse intact.

---

## Current State

Validation half **ACCEPTED** (msg 4212). CTO~Z independently re-derived the register split (2/7) and the
`main.tf` census (15 chars / 45 bytes) at their own seat. The WF-6/WE-6 precedent is **RULED in writing**
at acceptance: *the discriminator is the existence of the subject, never the byte-unchanged argument;
WE-6 is NOT precedent for WF-6, and when W-F's leg is wired WF-6 must be EXERCISED, not promoted.*
Option A endorsed and routed to `0.0.0_AB_MSTR~Z` as register owner.

**Open at Andrew, unstruck:** the XXX.md COO row holds a LIVE Andrew-direct `/drive` authorization scoped
to "D6/D7/D8/D9 to completion" whose stop-condition has not fired and whose own text says a respawned
COO~Z MUST re-arm. I armed nothing and struck nothing; CTO~Z is carding it, default-if-silent = arm
nothing (the CVO~Z LD-0318 precedent). **The row and the practice disagree on disk and the next COO~Z
will read a row telling it to re-arm.**

---

## Next Steps

1. [`0.0.0_AB_MSTR~Z`] Register edit per Option A — re-tag D7 TOs to `OPAL_TICKET`, then `members: [OPAL_TICKET]`; D5 is the same remedy.
2. [Andrew] The `/drive` row fork — arm-nothing stands until his word.
3. [`0.5.0_AE_OpalETL~Z`] Holding correctly; W-E's remaining rows need the DL to exist + the laptop apply, and that apply carries W-A's queue.
4. [D1/D3] Empty `projects[]` measured, open-TO counts **UNMEASURED** — flagged, not concluded.

---

## Bounds

Repo-plane and local instruments only. **No laptop artifact read, no live-AWS claim made** — the SES
production-access and DKIM facts are cited to `1.0.0_SA_CTO~Z`, not re-measured here. My first reading of
`to-check.py`'s project-code precedence was WRONG and the proposal does not rest on it. Zero crons armed,
zero gateway calls, nothing wired, nothing applied.
