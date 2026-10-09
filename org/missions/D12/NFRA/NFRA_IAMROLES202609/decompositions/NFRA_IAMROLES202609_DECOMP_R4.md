# NFRA_IAMROLES202609 -- L5 DECOMPOSITION, ROUND 4 (the enrichment round on FWD-2's substrate)

**Cut by** `2.0.0_SA_COO~ZI` **at L5, 2026-10-09.**
**Consumes:** `1.0.0_SA_CTO~Z`'s round-3 analysis `ledger/ROUND_ANALYSIS.round3.md` @`f8571787db`, section 7
(the recut instruction) and section 8 (what is owed, by whom).

> The analysis was written 2026-09-10. This recut lands 2026-10-09, twenty-nine days later, because the
> issuing lane was not seated between those dates. Nothing in the analysis depends on the date except the
> round-3 census's vintage, and every cell below carries that vintage explicitly.

Rounds 1-3 (`_DECOMP.md`, `_DECOMP_R2.md`, `_DECOMP_R3.md`) stay in place so their instances keep resolving.
This is a fourth file, not an edit.

---

## 1. THE RECTANGLE -- THREE CELLS

| cell | analysis label | outcome | the act |
|---|---|---|---|
| `IAM-u-1` | R4-A | FWD-1 | **THE POSTURE NUMBER.** A rollup of round 3's committed 219-role census, recomputable with no cloud call, carrying its denominator, its vintage and the population qualifier (219 = every live role at Path "/", i.e. 229 total minus 10 service-linked). |
| `IAM-u-2` | R4-B | FWD-8 | **THE SECOND RUN PLUS THE COMPARISON.** Re-run the permission-grain assessment over the same population rule and lookback, by a composed harness someone else can invoke, and put the answer beside round 3's. |
| `IAM-u-3` | R4-C | FWD-3 | **EXERCISE THE CONDITION AXIS.** Round 1 surfaced the exhibit from POLICY TEXT (DESIRED). Move it to EXERCISED with a live read plus a read-only `simulate-principal-policy` battery, with a scoping control. |

**Mapping, binding for every later reader:** `R4-A` = `IAM-u-1`, `R4-B` = `IAM-u-2`, `R4-C` = `IAM-u-3`.
`CELL_ID_RE` loaded as a module object from `.tools/proof-of-spec-check.py`: `IAM-u-1/2/3` match=True;
positive control `IAM-t-2`, `IAM-s-4` match=True; negative control `R4-A`, `IAM-u-` match=False.

**NOT IN THE RECUT, per analysis section 7:** `FWD-4` (blocked on an ASK, not work -- a cell would idle);
`FWD-7` (REALIZED at round 3 -- do not cut); `FWD-5` (follows `FWD-1`, does not race it).

---

## 2. THE BATTERY, AT ROUND-4 VINTAGE (2026-10-09, base `54c2fd91b6`)

```
comp-iam           RUN, `bash .tools/comp-iam stats` from the MAIN checkout (not a clean worktree; the
                   form is part of the figure): 214 TF roles / 196 services / 1154 operations / 338 gaps.
                   Round 3 read 191/188/1084/304 from a clean worktree. No cell in this round reads it.

comp-find          RUN, `comp-find '.' --corpus aws IAM_ROLE`, graph vintage 2026-10-09 03:31:25 UTC
--corpus aws       (manifest 1c41f4caa29b): 283 IAM_ROLE nodes, DECLARED=262, LIVE-no-DECLARED=18,
                   MULTI_STATE_MANAGED=3. Round 3's population was 219 at Path "/" by a list-roles read
                   (229 total). The graph count and the list-roles count are DIFFERENT INSTRUMENTS, but
                   the gap (283 vs 229) says the population MOVED in 29 days. IAM-u-2 must measure that
                   with its own list-roles read, and IAM-u-1 must state that its figure predates it.

comp-iam-usage     INSTRUMENT PINS UNCHANGED SINCE ROUND 3, measured at the base:
                   .tools/comp-iam-usage                   5c7f03ba3702d5de5c0edf7a955a72dd20e596f5
                   org/modules/graph/comp_iam_usage.py     8670fc5025694c942f8a7c725a19e2317cf63c20
                   So a second run uses byte-identical instrument code, which is half of "comparable".

condition-axis     round-1 reader at deliverables/0.9.0_WK_NFRA_IAMROLES202609~2/condition-axis-reader.py,
reader             blob 62ff401ce8237a5a148e9873ce9e21e894bd256f.

AWS live read      `aws iam get-role-policy estate-report-runner-role / estate-report-runner-selfstop`:
                   live text matches the round-1 exhibit (one action ec2:StopInstances, one ARN-pinned
                   instance i-0584e17d283fa7ef4, NO Condition). `simulate-principal-policy` on it with no
                   context: ec2:StopInstances -> allowed, rc=0. The exercise path is reachable.

comp-schedule      RUN TWICE, `python .tools/comp-schedule` (the bare path is not a bash script): BUDGET
                   REACHED at 90 s and again at 220 s, 1 of 6 carriers, C1=23 (7 gates armed), C2=32
                   PARTIAL (0 of 32 ledger entries scanned). ANSWER-STATE PARTIAL_OR_BLIND -- not read as
                   clean. Round 3 completed 5 of 5 carriers in 13.5 s. G-21 (no alert/alarm/monitor/
                   schedule/notification) binds every cell regardless; it is CLAUDE.md law, not only a
                   C1 sentinel.

comp-adversary     this lane took the analysis's recut as GIVEN and re-derived two premises: the
                   instrument pins (unchanged) and the population (moved, see comp-find above).

comp-blast         DECLARED-NOT-APPLICABLE: no cell changes Terraform custody or applies anything.
```

---

## 3. BOUNDS -- what no cell in this round may cross

```
C-NO-ACCESSDENIED     no cell narrows, revokes, detaches or applies anything. simulate-principal-policy
                      is a READ (it evaluates, it does not change). Naming is not removing.
C-ANALYZER-PRICED-FIRST + G-25   NO AWS Access Analyzer. Access Advisor only, through comp-iam-usage.
G-21                  no alert, alarm, SNS, SES send, notification, freshness checker, monitor or schedule.
                      IAM-u-2's harness is invoked BY HAND, every time; it never wakes itself up.
C-TWO-REMEDIES        no cell assigns an owner or touches GOVERNANCE_DISPOSITION.md.
C-COVERAGE-OVER-COUNT a smaller figure that states what it cannot see beats a tidy one that hides it.
                      IAM-u-1's figure carries the unobservable share beside it, always.
PART VII ITEM 5       IAM-u-3 exercises ONE policy; it makes no population claim about the estate.
INSTRUMENTS ARE RUN   .tools/ is not in any write surface. Round-1 and round-3 deliverables are READ
NOT REWRITTEN         surfaces: no cell edits another worker's directory.
FROZEN SPEC           mid-round the PRD and this rectangle do not move; a cell that thinks a bound is
                      wrong files a surprise ROW and keeps working.
```

---

## 4. DEPENDENCY EDGES -- none

```
IAM-u-1  <- (none)   reads the committed round-3 bundle only
IAM-u-2  <- (none)   reads AWS and the committed round-3 bundle
IAM-u-3  <- (none)   reads AWS and the round-1 reader
```

`IAM-u-1` does NOT wait for `IAM-u-2`'s fresh run: the analysis cuts FWD-1 as "a rollup of the census
that exists", and a posture number that states its vintage is the bar. A refreshed posture figure off the
second run is an enrichment candidate for round 5, not a dependency now.

**WRITE SURFACE**

```
IAM-u-1   deliverables/0.9.0_WK_NFRA_IAMROLES202609~10/   only
IAM-u-2   deliverables/0.9.0_WK_NFRA_IAMROLES202609~11/   only
IAM-u-3   deliverables/0.9.0_WK_NFRA_IAMROLES202609~12/   only
```

No two cells write the same file. The append-only surprise channel is shared by construction and is
resolved as a union by row id at the drain. Minimum chain partition = 3, so `fanout: 3 of 3 chains, cap 8`.

---

## 5. RULE 24 -- THE FOUR-POSTULATE RECORD

**(i) MECE over a DECLARED domain.** Domain = the outcomes analysis section 7 put in the recut: FWD-1,
FWD-8, FWD-3. One cell each. The PRD's other five are named in section 1 with the analysis's reason.

**(ii) SAME GRAIN.** Each cell is one act producing one deliverable: a rollup, a re-run plus comparison,
a live exercise.

**(iii) INTENT COHERENCE.** One axis each: posture (permissions, aggregate), repeatability (permissions,
over time), condition (what a policy requires of its caller).

**(iv) STATE COHERENCE.** `IAM-u-1` moves FWD-1 from *no figure* to *a figure with denominator and
vintage*; it does NOT refresh the census. `IAM-u-2` moves FWD-8 from *harness composed, one role* to
*re-run at population scale and compared*; it does NOT recompute FWD-1. `IAM-u-3` moves FWD-3's exhibit
from DESIRED to EXERCISED; it changes no policy and claims nothing about any other policy.

---

## 6. WHAT THE ROUND CANNOT CLAIM, STATED AT THE CUT

- **It cannot close the project.** FWD-4 stays blocked on the seating ask; FWD-5 is not cut.
- **FWD-1's figure is as of 2026-09-10.** The population has moved since (section 2); the figure says so.
- **FWD-8's comparison may show differences.** A difference is not a failure of comparability; what
  makes the two runs comparable is the same rule, lookback and instrument bytes, stated, plus an
  intersection on which the two can be read side by side.
