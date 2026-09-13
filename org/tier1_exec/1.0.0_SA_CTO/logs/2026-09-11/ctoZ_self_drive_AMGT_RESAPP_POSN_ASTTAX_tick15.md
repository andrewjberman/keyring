# 1.0.0_SA_CTO~Z -- /self-drive AMGT_RESAPP & POSN_ASTTAX, tick 15

**state:** `ARMED` · cron `254949d7` · covers tick 15 (the tick opened QUIET and did not stay that way)

```
SELF-DRIVE AMGT_RESAPP & POSN_ASTTAX -- tick 15 (2026-09-11T17:09Z)   state: ARMED
OPEN CALLS IN SCOPE: 1 RESERVED (raised to Andrew this tick, citation on the card) · 0 adjudicable
COMPLETION TEST: NOT DONE -- 0 of 2 projects status:complete
LOG: written -- two driver acts taken after the tick opened quiet
```

## 1. THE L10 PRECONDITION: I WAS WRONG, AND SO WAS THE COO. THE REFUSER EXISTS

Tick 15 opened with this seat and `2.0.0_SA_COO~Z` agreeing, from opposite ends, that no tool
mechanically refuses an L10 close on a non-terminal order -- so the question was interpretive.
**`3.0.0_SA_CVO~Z` falsified that, and this seat CONFIRMED IT AT SOURCE rather than on report.**

`.tools/surprise-row-gate.py`, `_route_precondition_violations` (:773-809) + `_open_tos_for_project`
(:744). Executed: `_open_tos_for_project('.','POSN_ASTTAX')` -> **2 open of 8**, exactly `TO-S2-1
[staged]` and `TO-S3-1 [staged]`. Its refusal text quotes the authority:

> "The slug waits until every task order is complete (Andrew-direct 2026-09-03, @`716a9bc7ce` call 3,
> LD-0521: **'We do not route until the job is over'**)."

⛔ **SO IT WAS NEVER INTERPRETIVE, AND THE GATE IS ANDREW'S WORD.** Everything 21490 built on "no
refuser exists" falls -- including its conclusion that nobody should add one. There is nothing to add.

⭐ **THE METHODOLOGICAL ERROR IS THE PART TO KEEP.** The census that missed it read `'L10'` across
56,221 files -- 4,117 hits -- and reasoned that only the DEF band could hold a refuser. **The
decisive implementation is named `_route_precondition_violations`: its identifier does not contain
"L10" anywhere.** A token census for a CONCEPT cannot find an IMPLEMENTATION that does not spell the
concept in its name, and **a four-thousand-hit denominator makes that blindness look like
thoroughness.** The CVO found it by going at the BEHAVIOUR (what refuses a remediation row) instead
of at the word, which is why a third tool neither operational seat had opened turned out to be the
carrier. I endorsed the wrong inference in 21490 and called the absence "deliberate" -- **third time
today I accepted a well-dressed proxy for the thing itself.**

**Measured by this seat and added:** `TERMINAL_TO_WORDS` includes `superseded` and `withdrawn`, so a
terminal vocabulary that could honestly fit DOES exist -- but only with a real successor to point at,
which is precisely the qualifier `2.0.0_SA_COO~Z` put on its refusal. And the same predicate returns
**8 open of 36 for AMGT_RESAPP** (the round-5 cells), so this gate will refuse AMGT's slug too when
round 5 ends -- correct there, that job is not over.

## 2. THE BIND, AND WHY IT LEFT THE FABRIC

1. The gate refuses the round-2 slug while S2-1/S3-1 are non-terminal.
2. Neither seat will flip them terminal -- the denominator-shrink, and **I would be the beneficiary**.
3. The cells MUST NOT run: `TO-S7-1`'s NO-GO is measured, and `S2-AC5` cannot discriminate.
4. ⛔ **The audited override is NOT OURS.** `# surprise-row-override:` exists, but this precondition
   is ANDREW'S WORD; using an override to step past his ruling is converting his word by agent
   judgment, which CLAUDE.md forbids. Refused, and recommended against for everyone.

**RESERVED CARD RAISED (msg 21495/21496/21497)** -- and it passes the citation test that most claimed
reservations fail: the verbatim standing hold is quoted and it names the decision class exactly.
**REC:** let round 2 route with both cells carried forward EXPLICITLY as un-run. **A round frozen at
L10 forever because it was RIGHT not to run two cells penalises the correct decision.** Pitched to
the CVO as a RESERVED CLAIM for classification review; `0.0.0_AB_MSTR~Z` copied as the route to
Andrew.

## 3. AT-RISK WORK PRESERVED -- producer UNTOUCHED

`2.0.0_SA_COO~Z` (21492) surfaced a substantive UNCOMMITTED edit to
`infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-constituents.py` -- 13 insertions, 6 deletions,
**survived the 14:10:36Z reboot**, dirty for ~17 days. Last committer on the file is `b3d830094c`,
**this seat**, 2026-08-25, and the edit quotes an Andrew-direct of the same date -- most likely this
seat's own WIP.

Preserved @`5c9e329a21` as a patch + README under `deliverables/at_risk_patches/`. **The working-tree
file was NOT touched and is still ` M`** -- verified after the commit, not assumed. Nothing applied,
nothing deployed. ⭐ **Copying rather than committing was the point:** it kills the loss risk at ZERO
production risk, and **this seat did NOT re-measure the diff's `ValidationException` claim -- an
in-comment "measured:" is the AUTHOR'S assertion, not this seat's measurement.** That is the same
distinction I got wrong three times today, and I was not going to repeat it on a production write
path.
`0.0.0_AB_MSTR~Z` independently preserved the same bytes @`880780f5a4`. **Two carriers, and that is
REDUNDANCY not drift** -- both are insurance copies of an ephemeral thing and both disclaim
authorship and review. Named here so a later reader does not mistake it for the two-carrier defect.

⚠ **For W8-S2, whose disarm this seat owns: MEASURE THE WORKTREE, NOT JUST HEAD.** Reading the
committed producer alone means reasoning about a version someone has already partly revised, and the
difference is invisible unless you look. The edit does NOT fix W8-S2 (it changes the empty-value
FILTER, not the create-only behaviour). The ~17-day coincidence between the uncommitted fix and the
stale blank values is **suggestive, NOT causal** -- an empty-string write should have RAISED under
the old filter -- and is recorded, not diagnosed.

## 4. AMGT_RESAPP -- round 5 issued and spawned

`@dcbebda22c`, 8 cells, fanout 2 of 2 chains, cap 8. Both TABLE cells are the only roots, which
encodes "tables first" STRUCTURALLY rather than by instruction. Gate ADMITTED @`6c52a4e380`.
**The S6 correction landed in time and 8 of 8 rows were verified by `2.0.0_SA_COO~ZZZ` to contain no
S6 create cell**; the decomposition's bounds state `opal-data-research` is an EXISTING DECLARED
RESOURCE that a cell must INTEGRATE with. Stated precisely: the corrected bytes were an ANCESTOR of
the cut (12:44:38 vs 13:06:05), which proves AVAILABILITY, not that the cutter read them -- `rd-1`'s
own "NOT `opal-data-research`" text is the direct evidence.
⭐ **The hand-delivered L4->L5 handoff is what carried it.** The notifier row still reads UNSENT at
attempts=0, lane-homed to the wrong COO. Had both seats trusted the mechanism, round 5 would have cut
a create cell for a bucket this project built yesterday -- **and that cell would have PASSED every
mechanical criterion while doing exactly the wrong thing.**

## 4b. VINTAGE BOUND ADDED AFTER THIS LOG WAS COMMITTED (appended, nothing rewritten)

⚠ **The "17 hops / 3 survive / 14 silently drop" figures quoted above and in msgs 21480/21495 are
PINNED TO `TO-S7-1`'s VINTAGE and are NOT a current measurement.** `3.0.0_SA_CVO~Z` states: *"S1 later
repaired a benchmark hop, so S7 3/14/0 is historical, not a recount of current source."*
**THE VERDICT IS UNAFFECTED** -- the CVO re-confirms NO-GO against current controls: *"still display
Commodities/Structured as Unknown."* Only the RATIO is historical. Nobody should re-quote 3/14 as
today's state.
Appended rather than edited in place: the body was true at its vintage, and silently correcting a
number inside a committed record destroys the evidence of what was believed when.

## 5. COMPLETION TEST

**NOT DONE -- 0 of 2 `status: complete`.** AMGT_RESAPP active/EXECUTING, round 5 L7 in flight (8
staged). POSN_ASTTAX active/EXECUTING, round 2 at L8/L9 with the CVO, 6 of 8 terminal, slug BLOCKED
by the Andrew-word precondition. Both REACHABLE; no HELD-AT-STOP.
**Open at Andrew: 1 RESERVED card** (the L10 precondition vs a correctly-declined cell).

## Compiler Tools

`surprise-row-gate.py` `_open_tos_for_project` / `_route_precondition_violations` read at the function
AND executed · `TERMINAL_TO_WORDS` read at source · `git apply --check --reverse` (round-trip proof
the saved patch IS the current delta) · `git diff` / `git status --porcelain` before and AFTER the
preservation commit · `prd-signoff.py status` · `safe-commit.sh -F` · `ack_messages` 21485, 21488,
21492/21493.

**Push state:** `origin/SITEZ = 5c9e329a21` (this tick's preservation commit) per `0.0.0_AB_MSTR~Z`'s
ls-remote with a negative control. This seat does not push.
