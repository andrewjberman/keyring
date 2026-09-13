# 1.0.0_SA_CTO~Z -- /self-drive AMGT_RESAPP & POSN_ASTTAX, tick 14

**state:** `ARMED` · **cadence:** 30m, cron `254949d7` · **covers:** tick 14 and everything after the
tick-13 log @`cbcadad9a4`

```
SELF-DRIVE AMGT_RESAPP & POSN_ASTTAX -- tick 14 (2026-09-11T16:47Z)   state: ARMED   job: 254949d7
SCOPE: 2 project(s) -> AMGT_RESAPP (D5), POSN_ASTTAX (D4)   device: sitez
OPEN CALLS IN SCOPE: 0 adjudicable, 0 RESERVED -- no pitch sent
VERDICTS SINCE LAST TICK: 2 brief-half L4-R stamps (26f942429c6a, then c90934a3d620)
COMPLETION TEST: NOT DONE -- 0 of 2 projects status:complete
LOG: written (substantive delta)
```

## 1. AMGT_RESAPP: ADMITTED, and the S6 row now says INTEGRATE

`@6c52a4e380`: folded round-4 row `AMGT_RESAPP-Z-S8` into the PRD. **The material change is the S6
manifest row, not the prose.**

```
WAS:  | S6 | FWD-6 | THE VERSION STORE | absent                       | ... | build   |
NOW:  | S6 | FWD-6 | THE VERSION STORE | STORE EXISTS; surface absent | ... | INTEGRATE -- no create cell |
```

⛔ **A ROUND-5 CUT AGAINST THE OLD ROW WOULD HAVE CUT A CREATE CELL FOR A BUCKET THIS PROJECT CREATED
YESTERDAY** -- and it would have PASSED while doing exactly the wrong thing. `opal-data-research` was
created by this project's own `AMGT-s-6` at 2026-09-10T20:59Z under a CLOSED deploy-completion entry,
declared at `infra/aws/terraform/research/s3.tf:11`. Verified at the record by this seat before it
went into the spec, then **independently re-derived on `4.0.0_SA_CRO~Z`'s own instruments** before it
signed -- six facts, all six confirming.

⭐ **THE HISTORY QUESTION IS ANSWERED, AND THE WITHDRAWAL WAS STILL CORRECT.** S8 establishes the very
phrase withdrawn at `b9723b43e5`: the bucket was measured ABSENT twice, the second time by
`AMGT-s-6`'s own AC1 **three minutes before that cell created it**. It was unsupported when asserted
and is supported now -- different facts about different moments. **A claim is not made true
retroactively by later evidence arriving**, so withdraw-then-re-add-ON-EVIDENCE is the right sequence,
not a reversal. `4.0.0_SA_CRO~Z` endorsed that and sharpened it against itself: its own 5b error was
endorsing an UNMEASURED claim AS MEASURED, and **that error is identical whether or not the claim
later turned out true -- a lucky guess is exactly where this failure mode is hardest to see.**

Evidence the CRO added that this seat did not have: `BABA_US_Equity` carries **two distinct
timestamped snapshots**, neither overwritten -- so FWD-6's accumulate-never-overwrite bar is
demonstrated **in the data**, not only by the `Enabled` flag. Still NOT claimed, carried forward:
**write access was never exercised.**

**Gate now: ADMITTED** -- ratified `4eb997ed71ee`, brief `c90934a3d620`. Round 5 unblocked, and it is
`2.0.0_SA_COO~ZZZ`'s to cut against the CORRECTED row.

## 2. POSN_ASTTAX: step (2) is DONE-AND-FAILED. The retag is NO-GO, and this seat got it wrong first

**2 of 8 terminal -> 5 of 8.** Staged: `S1-1`, `S2-1` (the retag), `S3-1`.

⛔ **THIS SECTION REPLACES A CONCLUSION THIS SEAT BROADCAST AND WITHDREW** (msgs 21476/21477/21478,
withdrawn by 21480). The withdrawn claim was that C-RETAG-SAFETY's sequence was SEQUENCE-CLEAR
because steps (0)(1)(2) were `complete` with proof instances VALID at HEAD. Corrected by
`2.0.0_SA_COO~Z` (msg 21479), which is right.

| step | cell | state | what it actually means |
|---|---|---|---|
| (0) HARDEN | `TO-S6-1` | complete, VALID | DONE |
| (1) `management_style` | `TO-S5-1` | complete, VALID | DONE |
| (2) verify the chain | `TO-S7-1` | complete, VALID | **DONE AND FAILED -- verdict NO-GO** |
| (3) retag | `TO-S2-1` | STAGED | **NOT REACHED** |

Step (2) is not "run a verification cell." Verbatim, it is "verify the asset_class allocation chain
**CARRIES** the ratified FIVE-class vocabulary." The cell ran it and **the answer was NO**:
`S7-AC3` -- **HOPS TESTED 17 | SURVIVES 3 | SILENTLY DROPPED 14 | RAISES 0**, accounting COMPLETE
(79 of 79 AC2 hits assigned). `S7-AC5`'s GO threshold was 17 of 17. It read 3.

⛔ **THE SHAPE OF THIS SEAT'S ERROR, which is worth more than the correction. A COMPLETED
VERIFICATION CELL IS NOT A PASSED ONE.** I substituted a proxy -- terminal status plus a well-formed
instance -- for the thing itself, the cell's verdict. **And the caveats made it look rigorous while
missing it:** four limits were attached to that claim and every one was about the CHECKER's coverage
(COVERAGE UNCHECKED, the CVO cert judgment, round 2 undrained, what CONTENT-resolution proves). Not
one asked what the cell CONCLUDED. That is a GRAIN error -- **the wrong object, read carefully** --
and the density of the caveats is what made the conclusion persuasive, including to its author.
Third instance today of dressing an unmeasured thing in measured vocabulary; recorded as a standing
weakness of this seat, not three incidents.

⭐ **THE PREMISE INVERTED, AND THIS IS THE PART TO CARRY FORWARD: 0 of 17 hops RAISE.** The KeyError
premise the whole constraint was built on is **DEAD** -- `AT2-s-6` killed it. A retag today would NOT
blank the page. It would render `Commodities`/`Structured` as the literal string `'Unknown'` through
the four-key `.get(asset_class_raw, 'Unknown')` display map, and silently zero the weight through an
if/elif chain at `:389-407` with **no else**. **THE HAZARD GOT QUIETER, NOT SAFER** -- strictly worse
for detection than the blanking it replaced.

⛔ **AND `TO-S2-1` CANNOT SEE ITS OWN FAILURE.** `S2-AC5` is "confirm the page still renders", which
post-`s-6` returns the SAME observation in the healthy world and the broken one -- a criterion that
cannot discriminate. Cutting S2-1 as written would have produced a **PASS over a live regression**.

VXX is the **only** held member of the retag set (LT 0.0150 / ULT 0.0200; corroborated on the served
plane; controls AGG 3 rows, ZZZZNOPE 0) -- the entire live blast radius; the commodity half is
latent. A SECOND defect stands alongside: `seed-etf-classifications.py`'s unconditional full-item put
would revert both `AT2-s-5`'s writes and any retag (LATENT, no automatic trigger, measured unscoped).

`2.0.0_SA_COO~Z` is NOT cutting S2-1/S3-1 this round and leaves them `staged` rather than
cancelled -- *"a terminal status without a real pointer is rot with a tidier label."* It declined to
amend `S2-AC5` mid-round under Rule 27's freeze. All three decisions are that seat's and all three
are right; this seat asked for none of them.

## 3. THE PATTERN THIS TICK CONFIRMS

Three brief-half edits inside one hour, each a real improvement, **each found by a reviewer rather
than by the author** -- and both overclaims found by the reviewer of the OTHER half. That is evidence
against any future argument that a half's reviewer need only read its own half. Both `4.0.0_SA_CRO~Z`
and this seat reached it independently from opposite sides.

Also worth keeping: the gate has now correctly reported STALE on **four consecutive** brief-half
edits, every one of them this seat's own. Before the content-bound re-sign it would have printed
"SIGNED current" and moved the half invisibly. Row `S7`'s disarm of `S6` is EXERCISED, not argued --
and its three non-claims are unchanged: the library is untouched, the old-format carrier is still
present and merely shadowed, the estate class is uncounted.

## 3b. WHAT THIS SEAT NOW OWES AT L10 -- round 2's read is mine and carries more than a grade

Taking `2.0.0_SA_COO~Z`'s recommendation: these belong in the round-2 analysis or a PRD addendum,
**never a mid-round edit** (Rule 27's freeze, and that seat was right to decline).
1. **`C-RETAG-SAFETY` needs RE-FOUNDING, not re-sequencing.** Its stated mechanism -- "a fixed-key
   allocation dict KeyErrors and blanks the page" -- is FALSIFIED by measurement (0 of 17 RAISE).
   The constraint is still right that the retag is unsafe, and right for a **different reason than
   it states**. ⛔ A constraint whose stated mechanism is dead will be mis-applied by the next cell
   that reads it -- and "the page still renders" is exactly the check that mechanism invites.
2. **Step (2) must name its own BAR, not an ACT.** It reads "verify the chain", which is a task; it
   must read as a CONDITION with a threshold. **Written as an act, it invited precisely the error
   this seat made** -- treating the act's completion as the condition's satisfaction.
3. **A criterion that cannot discriminate must not be re-cut as written.** `S2-AC5` needs to fail in
   the broken world: the served value and the weight, not "the page renders".
4. The re-seed revert, and `TO-S7-1`'s two disclosed gaps (the FRONTEND hop unmeasured -- `portal/`
   outside the worker's cone, census printed 29577 UNREADABLE -- and two enumerated-but-untested
   sibling consumers). Both can only STRENGTHEN a NO-GO, neither is measured, and neither is being
   treated as though it were.

## 4. COMPLETION TEST

**NOT DONE -- 0 of 2 `status: complete`** (denominator 2, read from the register). `AMGT_RESAPP`
active/EXECUTING, round 5 uncut, gate ADMITTED. `POSN_ASTTAX` active/EXECUTING, L7, 5 of 8 terminal.
Both REACHABLE; no HELD-AT-STOP. **Open calls at Andrew: 0.**

Carried, unfixed, all three surfaced-and-routed under Andrew's ~15:4xZ scope word: `spawn-agent.ps1`
has no codex branch; `prd_signoff_lib`'s legacy `prd_version` fallback (row `S6`); and the L4
notifier's delivery row, measured `UNSENT attempts=0` and **mis-routed to `2.0.0_SA_COO~Z`** because
`RECIPIENT` is homed on the COMMITTER's lane rather than the project's COO -- with `coo_lane` unset on
both projects and undeclared in `PROJECT_TREE.contract.json`, which also leaves `route_half`'s Rule 27
exclusion filter DESIRED-NOT-APPLIED. The L4->L5 handoff was delivered BY HAND instead.

## Compiler Tools

`prd-signoff.py status` · `prd_signoff_lib.half_hashes` (before/after on BOTH halves, every edit,
checked BEFORE writing) · `proof-of-spec-check.py` on three instances with its own COVERAGE-UNCHECKED
limit quoted · `comp-read --enumerate` (the constraint body; a case-sensitive miss on `THIS`/`This`
cost one retry) · `comp-find --name` with printed denominators · `.tools/aws s3api
get-bucket-versioning` · `git log`/`ls-remote`/`merge-base --is-ancestor` with negative controls ·
`safe-commit.sh -F` (non-ASCII gate hit a SECOND time -- `⭐` after `⚠`) · `ack_messages` 21466, 21475.

**Push state:** LOCAL at write time -- `959ba3e947`, `cbcadad9a4`, `f0ff95cfac`, `6c52a4e380`.
`0.0.0_AB_MSTR~Z` pushes origin/SITEZ; this seat does not push.
