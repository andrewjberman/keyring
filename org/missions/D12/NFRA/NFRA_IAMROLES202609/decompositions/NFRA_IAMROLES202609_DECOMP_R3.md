# NFRA_IAMROLES202609 -- L5 DECOMPOSITION, ROUND 3 (the first delivery round)

**Cut by** `2.0.0_SA_COO~ZI` **at L5, 2026-09-10.**
**Consumes:** `1.0.0_SA_CTO~Z`'s round-2 analysis `ledger/ROUND_ANALYSIS.round2.md` @`3cadaf52ca`
(section 8 is the recut instruction), which routed `3.0.0_SA_CVO~Z`'s slug @`d076801ecf` and this
lane's `ledger/COMPLETION_REPORT.round2.json` @`baa5705269`.

> ⛔ **ROUND 3 IS THE FIRST ROUND THAT CAN DELIVER AN OUTCOME.** Rounds 1 and 2 built and repaired the
> instruments -- vocabulary, denominator, membership, schema. The analysis says to read this as the
> project's first delivery round, not its third repair, and the rectangle is cut to that frame.

Round 1's rectangle (`_DECOMP.md`, nine cells) and round 2's (`_DECOMP_R2.md`, six cells) stay in
place so their instances keep resolving. This is a third file, not an edit.

---

## 1. THE RECTANGLE -- THREE CELLS

| cell | outcome | the act |
|---|---|---|
| `IAM-t-1` | FWD-4 | **CLOSE FWD-4.** Nine `ADOPT` rows carry NO `owner=` field at all; `lambda-test-role` carries `RETIRE owner=UNASSIGNED`. Give each a named owner or an in-code declaration -- or record, as a FINDING, that the owner does not exist inside this fabric. |
| `IAM-t-2` | FWD-2 | **EXERCISE the permission-grain usage instrument** across a stated role population over a stated lookback, and NAME the unused permissions per role. |
| `IAM-t-3` | FWD-6 | **THE THREE PRIOR REMEDIATION PLANS**, each established landed-or-not ON THE ARTIFACT, never on the plan document's own say-so. |

### 1a. THE ANALYSIS'S LABELS ARE NOT LEGAL CELL IDS, AND THE MAPPING IS RECORDED RATHER THAN ASSUMED

Section 8 names the cells `R3-A`, `R3-B`, `R3-C`. **`R3-A` DOES NOT MATCH `CELL_ID_RE`** and cannot be
a cell id; a decomposition using it would fail the L6 gate's alignment limb. Measured against
`CELL_ID_RE` loaded as a MODULE OBJECT from `.tools/proof-of-spec-check.py`, with controls:

```
CANDIDATE   IAM-t-1 / IAM-t-2 / IAM-t-3      match=True   (all three)
POS CONTROL both prior rounds' real id shapes
            (round-1 `s`-series and round-2 `r`-series,
             2 of 2 tested)                   match=True
NEG CONTROL IAM-3-a, IAM-t-, iam-t-1,
            IAM_t_1, R3-A                     match=False
```

**MAPPING, binding for every later reader:** `R3-A` = `IAM-t-1`, `R3-B` = `IAM-t-2`, `R3-C` = `IAM-t-3`.

---

## 2. THE BATTERY, RE-RUN AT ROUND-3 VINTAGE -- AND THE INVOCATION FORM IS PART OF THE FIGURE

⛔ **THIS IS THE `Z-S9` REMEDY ACTUALLY APPLIED, AND IT NEEDED ONE MORE RUNG THAN `Z-S9` STATED.**
`Z-S9` said a battery is a measurement of a TREE and that the remedy is to measure from a clean
worktree. **Measuring from a clean worktree is NOT sufficient by itself:** the bare command name
resolves through a `~/bin` forwarder to the MAIN checkout, so `comp-iam` run *inside* a clean worktree
still reported the dirty main tree's number. **THE INVOCATION FORM DECIDES WHICH TREE IS MEASURED, NOT
THE `cwd`.** Measured, one variable apart, at the same commit:

| invocation | tree measured | IAM roles parsed |
|---|---|---|
| `comp-iam stats` (bare) from the clean worktree | MAIN checkout | **195** |
| `comp-iam stats` (bare) from the main tree | MAIN checkout | **195** |
| `bash .tools/comp-iam stats` from the main tree | main tree | **195** |
| **`bash .tools/comp-iam stats` from a CLEAN worktree @`f20bc65d71`** | **that worktree** | **191** |

**DISCRIMINATOR, so this is not an arithmetic coincidence.** Four `aws_iam_role` declarations exist
ONLY in five untracked files in the main checkout, confirmed absent from every commit (`git show`
rc=128) and absent from the worktree. The clean-tree role list does NOT contain them (census 0 for
`opal-globgrph-freshness-alarm` and `inf-gold-freshness-guard-lambda-role`), while a committed control
role IS present (census 1). 195 - 4 = 191.

**FIGURE OF RECORD FOR ROUND 3, and every cell inlines it with its invocation form:**

```
comp-iam           RUN, `bash .tools/comp-iam stats` from a CLEAN worktree at f20bc65d71:
                   191 TF roles / 188 services / 1084 operations / 304 permission gaps.
                   NOTEs stand: TF role labels `orchestrator` and `scheduler` were each reused across
                   three modules and SILENTLY MIS-LINKED their inline policies pre-fix -- a reason to
                   read SOURCE rather than a parse when deciding a role's state.
                   wafv2:UNMODELED and UNMAPPED-METHOD persist, so 304 is a FLOOR on the DESIRED plane.

comp-schedule      RUN to completion, 5 of 5 carriers, 13.5 s, WITHIN BUDGET.
                   GATES ARMED 25. Reached denominators C1=23 C2=6 C3=12 C4=20 C5=335.
                   C2 (deploy-ledger) = 6 OPEN entries, NONE of them this project's and none to close.
                   G-21 (no alert/alarm/monitor/schedule/notification) BINDS EVERY CELL BELOW.

comp-find          RUN, --corpus aws IAM_ROLE, vintage 2026-09-10 12:24:50 UTC (manifest aebbd9cef8c4):
--corpus aws       219 IAM_ROLE nodes scanned, DECLARED=203, LIVE-no-DECLARED=16.
                   STILL EXACTLY 16 AFTER ROUND 2 PROVED ONE MEMBER OF THAT CLASS IS A FALSE POSITIVE.
                   The live drift class does NOT learn from the repair, so it is NOT the membership
                   oracle; round 2's per-member SOURCE read is (population 15, measured).

comp-iam-usage     BUILT, TRACKED and SELF-TESTING at HEAD -- see 2a; this is IAM-t-2's instrument and
                   it is NOT to be rebuilt.

comp-blast         DISCHARGED at round 2 by the adoption cell and not owed again here: no cell in this round
                   changes Terraform custody.

comp-adversary     RUN on this rectangle before the cut; its declaration is that this lane took the
                   analysis's recut as GIVEN and re-derived only the ONE premise recorded in 2a.
```

### 2a. ONE PREMISE IN THE ANALYSIS IS ONE RUNG STALE, AND THE CELL IS CUT TO THE WORLD

Section 8 says of `R3-B`: *"`.tools/comp-iam-usage` is BUILT and answers the ROLE axis; the cell
EXTENDS it to the PERMISSION axis."* **The PERMISSION axis is already there.** Measured at HEAD:

- `comp-iam-usage` exposes `permission-cold` -- *"PERMISSION grain: which of a role's GRANTED
  permissions were never used over a stated lookback (IAM Access Advisor ACTION_LEVEL, NOT Access
  Analyzer)"*, with `--role` and `--lookback` (default 90).
- Its `self-test` passes and **names FWD-2 by name**: *"'unused over the stated lookback', FWD-2's own
  phrasing"*, and carries the discipline that **unobservable != never-used**.
- Round 1's instrument-build cell (`S1`) produced exactly two artifacts -- `org/modules/graph/comp_iam_usage.py`
  and `.tools/comp-iam-usage` -- and **NO usage RESULT**. The instrument was built and never exercised
  at population scale.

⭐ **SO THE GAP IS EXERCISE, NOT CONSTRUCTION, AND `IAM-t-2` IS CUT AS AN EXERCISE CELL.** This does
not contradict the ruling; it applies it one rung further. `C-EXTEND-NOT-BUILD`'s own ladder puts *"the
estate already has it"* above *"extend"*, and cutting a build-or-extend cell for a subcommand that
exists, self-tests, and already speaks the outcome's language would re-buy working code -- precisely
what section 8 forbids. FWD-2's bar is **EXERCISED**; an extension would still leave it unexercised.
Recorded as a surprise ROW (`spec_asserts` vs `world_is`) rather than settled here, and the row is
this lane's, not a dispute with the analysis.

---

## 3. BOUNDS -- what no cell in this round may cross

```
C-TWO-REMEDIES        GOVERNANCE and PERMISSIONS are two axes with two remedies that do not move
                      together. IAM-t-1 is governance ONLY; IAM-t-2 is permissions ONLY. Neither may
                      read the other's finding as its own answer, and neither may recommend the
                      other's remedy.
C-NO-ACCESSDENIED     no cell narrows, revokes or detaches any permission, and no cell applies
                      anything. IAM-t-2 REPORTS unused permissions; naming one is not removing it.
C-ANALYZER-PRICED-FIRST + G-25   NO AWS Access Analyzer. permission-cold uses IAM Access Advisor and
                      says so; pricing Access Analyzer is a VENDOR call reserved to Andrew and NO CELL
                      MAY TAKE IT.
G-21 (ARMED, 25 gates) no cell mints an alert, alarm, SNS, SES send, notification, freshness checker,
                      monitor or schedule.
NEVER-9               no bare `terraform apply`, no `aws lambda update-function-code`. No cell in this
                      round has any reason to touch either.
FROZEN SPEC           mid-round the PRD and this rectangle do not move. A cell that believes a bound
                      is wrong files a surprise ROW and keeps working.
OWNERSHIP IS NOT      IAM-t-1 MUST NOT write `owner=<seat>` for any seat that has not accepted it.
ASSIGNABLE BY A CELL  Three rows name 1.0.0_SA_CTO~Z because that seat ACCEPTED those three. Whether
                      the remaining owners exist inside this fabric AT ALL is the cell's FINDING.
```

---

## 4. DEPENDENCY EDGES -- there are none, and that is measured, not assumed

```
IAM-t-1  <- (none)
IAM-t-2  <- (none)
IAM-t-3  <- (none)
```

**DATA:** no cell consumes another's output. `IAM-t-1` disposes governance rows on a membership set
already settled at round 2 (population 15, measured). `IAM-t-2` exercises an instrument that exists
today. `IAM-t-3` reads three historical plans and their artifacts.

**WRITE SURFACE -- checked explicitly, because round 2's first edge set was WRONG on exactly this and
nothing downstream would have refused it until the drain:**

```
IAM-t-1   deliverables/0.9.0_WK_NFRA_IAMROLES202609~3/GOVERNANCE_DISPOSITION.md  + its own deliverable
IAM-t-2   its own deliverable only                        (.tools/ and AWS are READ surfaces)
IAM-t-3   its own deliverable only                        (org/critical_paths/ is a READ surface)
```

**No two cells write the same file.** The append-only surprise channel is shared by construction and
is NOT a chaining reason -- it conflicts on every concurrent drain and is resolved as a union by row id.

**Minimum chain partition = 3** (Dilworth: the maximum antichain is `{IAM-t-1, IAM-t-2, IAM-t-3}`,
size 3, and three chains of one cover it). So `fanout: 3 of 3 chains, cap 8` and each worker holds a
queue of exactly one.

---

## 5. RULE 24 -- THE FOUR-POSTULATE RECORD FOR THIS RECTANGLE

**(i) MECE over a DECLARED domain.** The domain is *the outcomes the analysis put in the recut*:
FWD-4, FWD-2, FWD-6. One cell each, no overlap, no gap. **The uncovered members are named rather than
hunted and lost:** FWD-5 and FWD-8 sit behind `IAM-t-2` and are DELIBERATELY NOT CUT -- cutting either
now would idle a lane against a dependency. FWD-1, FWD-3 and FWD-7 are downstream of FWD-2's exercise
and are likewise not cut. **This rectangle does NOT claim to cover the PRD's eight outcomes and the
round-3 completion report will say so on the same partition the round-2 report used.**

**(ii) SAME GRAIN.** Every cell is ONE ACT ON ONE AXIS producing ONE deliverable: a disposition pass, an
instrument exercise, a landed-or-not adjudication. No cell is a programme.

**(iii) INTENT COHERENCE.** One axis per cell, and the axis is named in the cell: `IAM-t-1` governance,
`IAM-t-2` permissions, `IAM-t-3` historical status. `C-TWO-REMEDIES` is the constraint that keeps (iii)
true across the round, and it is in BOUNDS rather than left implicit.

**(iv) STATE COHERENCE -- which values one remedy does NOT move.** `IAM-t-1` moves rows from *no owner*
or *UNASSIGNED* to *a named owner*, an in-code declaration, or **a recorded finding that no owner
exists**. ⛔ **It does NOT move a role into Terraform and does NOT change any permission** -- the same
row can be governance-closed and permission-open at once, and those are two clocks. `IAM-t-2` moves
FWD-2 from *instrument built* to *instrument exercised with a stated denominator and lookback*; it moves
NO row's disposition and NO permission. `IAM-t-3` moves three plans from UNKNOWN to landed-or-not; it
remediates nothing.

---

## 6. WHAT THE ROUND CANNOT CLAIM, STATED AT THE CUT

- **It cannot close the project.** Five of eight outcomes are not in this rectangle.
- **`IAM-t-1` may not be able to close FWD-4 either**, and that is an accepted outcome rather than a
  failure: if the owners for the nine `ADOPT` rows do not exist inside this fabric, the cell's honest
  product is that FINDING plus whatever rows it can legitimately close. The analysis says that
  escalation is the recut's finding and is raised then, NOT pre-emptively.
- **`IAM-t-2`'s coverage is bounded by what AWS tracks.** Access Advisor does not observe every action
  of every service; `unobservable != never-used` and the deliverable must keep them apart.
