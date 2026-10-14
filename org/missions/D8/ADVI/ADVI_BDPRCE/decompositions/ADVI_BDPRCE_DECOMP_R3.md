# ADVI_BDPRCE -- DECOMPOSITION (L5) -- ROUND 3, THE AMENDED RULE, THE LIST ANDREW READS, AND THE EXACT-LOT PRECONDITIONS (PRD v1.2)

```json
{
 "project": "ADVI_BDPRCE",
 "directive": "D8",
 "macro": "ADVI",
 "fabric": "dell1",
 "decomp_version": "v3",
 "step": 5,
 "prd_ref": "org/missions/D8/ADVI/ADVI_BDPRCE/prd/ADVI_BDPRCE_PRD.md (v1.2 @b8fe0dfd9e, both halves signed)",
 "order_ref": "1.0.0_SA_CTO~DELL1 msg 5337: org/missions/D8/ADVI/ADVI_BDPRCE/ledger/ROUND_ANALYSIS.round2.md (section 2) and ledger/CTO_RULING_R1_THE_PRICE_RULE_20261013.md AMENDMENT 1",
 "author": "2.0.0_SA_COO~K1",
 "round": 3,
 "rectangle": "the round-2 analysis's enrichment list: item 1 the amended rule into the module (BP-c-1) and the replay re-run on it (BP-c-2); item 2 the FWD-7 packet re-cut (BP-c-3, join); item 3 the 500,000-row check (BP-c-4) then the lot-key fixture proof (BP-c-5); item 4 the honest sentinel line, which a measurement made at the cut shows is already deployed, so it becomes a read-only verification joined to item 5's Monday/Tuesday cause (BP-c-6); item 5 the 1,859 off-canonical lots (BP-c-7). Item 6 (the writers import R1) is not this round. Nothing served moves.",
 "cells": 7,
 "chains": 4,
 "join_cells": 1,
 "ground_truth": "org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/2.0.0_SA_COO~K1/round3/L5_FACTS.md",
 "frozen": true
}
```

**Author:** `2.0.0_SA_COO~K1` (dell1). **Inputs:** the round-2 analysis, `R2_CLOSE.md`, the CVO's `ADJUDICATION_v2.md` and `REMEDIATION_v2.md` @0447f2df38, `round3/L5_FACTS.md`.

## Round 3 -- the cells

| cell | item | serves | owned files | depends on | slot, class | risk | at the cut |
|---|---|---|---|---|---|---|---|
| `BP-c-1` R1 Amendment 1 into the module and its tests, with a probe over real partitions | 1 | FWD-2, FWD-4, FWD-5 | `data/black_diamond/scripts/silver/bd_price_rule.py`, `.../silver/tests/test_bd_price_rule.py`, `deliverables/0.9.0_WK_ADVI_BDPRCE~13/` | -- | ~13 worker | LOCAL | pending |
| `BP-c-2` the replay re-run on the amended rule (determinism arm, the late-landed lookback, the fate of every interpolated row) | 1 | FWD-7 | `deliverables/0.9.0_WK_ADVI_BDPRCE~14/` | `BP-c-1` | ~14 worker | LOCAL | staged |
| `BP-c-3` the FWD-7 packet Andrew reads (the BP-b-7 re-cut) (**JOIN**) | 2 | FWD-7 | `deliverables/0.9.0_WK_ADVI_BDPRCE~15/` | `BP-c-2` | ~15 worker | LOCAL | staged |
| `BP-c-4` is 500,000 an export cap? (read-only) | 3 | FWD-9 | `deliverables/0.9.0_WK_ADVI_BDPRCE~16/` | -- | ~16 worker | LOCAL | pending |
| `BP-c-5` the lot-key fixture proof re-run with `relationship_id` in the key | 3 | FWD-9 | `deliverables/0.9.0_WK_ADVI_BDPRCE~17/` | `BP-c-4` (the order is the CTO's: check, then proof, then apply) | ~17 worker | LOCAL | staged |
| `BP-c-6` the honest sentinel line (is it deployed and exercised) and the cause of the Monday/Tuesday header-only export (read-only) | 4, 5 | FWD-5, FWD-9 | `deliverables/0.9.0_WK_ADVI_BDPRCE~18/` | -- | ~18 worker | LOCAL | pending |
| `BP-c-7` the source of the 1,859 lots priced off no canonical row (read-only) | 5 | FWD-3, FWD-8 | `deliverables/0.9.0_WK_ADVI_BDPRCE~19/` | -- | ~19 worker | LOCAL | pending |

No two cells write one file. `BP-c-1` edits the two module files (round 2's `BP-b-1` created them; no writer imports them); every other cell writes its own deliverables folder. `BP-c-5` produces a patched copy under its folder and edits nothing under `data/`.

**Chains** (cells joined by a data dependency are one chain): `{BP-c-1, BP-c-2, BP-c-3}`, `{BP-c-4, BP-c-5}`, `{BP-c-6}`, `{BP-c-7}`. M = 4 chains, one of them ending in the join `BP-c-3`.

## Staged cells (parked at the cut)

| order | owner | un-park |
|---|---|---|
| `BP-c-2` | `2.0.0_SA_COO~K1` | `BP-c-1` merged and PASS at the merged HEAD (the amended module is in its worktree) |
| `BP-c-3` | `2.0.0_SA_COO~K1` | `BP-c-2` merged and PASS; the census extract's sha256 re-read equal |
| `BP-c-5` | `2.0.0_SA_COO~K1` | `BP-c-4` merged and PASS; its verdict (CAP, NOT_A_CAP, NOT_DETERMINED) read: on CAP the fixture proof runs on a paged complete export or states its limit |

## Not cells of this round (each with its owner and its un-park condition)

| item | owner | un-park |
|---|---|---|
| **APPLY the exact-lot export change** (Units and Cost Basis on in the S3 and repo qt4 template; the silver patch; the lot table at the builder address; the first export read back) -- WORLD, reversible | `2.0.0_SA_COO~K1`, executed by a dell1 CloudOps lane the CTO names (queued as a call) | `BP-c-4` and `BP-c-5` merged and PASS, then the never-widen pair signed by BOTH halves at the current bytes; the order is cut then by amendment |
| the honest sentinel LINE as a code change | -- | withdrawn: the runner already prints `OK: bronze sentinel emitted` only after a `head_object` read-back (`bd-49f-runner/lambda_function.py:156-198`, committed `3709ae40d6`, deployed 2026-10-07T00:50:44Z per the function's `LastModified`); `BP-c-6` verifies it ran |
| every writer imports R1, or is retired | `2.0.0_SA_COO~K1` under FWD-7 pairs | Andrew's review of `BP-c-3`'s list, per fix |
| the fix of the lots priced off no canonical row; the fix of the Monday/Tuesday export | same | `BP-c-7` and `BP-c-6` name their causes |

## ARMED rows (11, owner this seat) -- disarm map

Each disarms by a served move after Andrew's review (FWD-7), except `W10-S2`. Round 3 brings these within reach: `W6-S2` (the amended module reads par-quoted per unit, `BP-c-1`/`BP-c-2`), `W2-S2`, `W2-S4`, `W1-S3`, `W3-S3`, `W3-S4` (the amended R1 is final, the list is re-run), `W12-S1` (the fate of every interpolated row is listed, `BP-c-2`/`BP-c-3`), `W4-S2` (`BP-c-7` names the sources), `W10-S2` (`BP-c-5` is its disarming read: zero rows folded and zero colliding groups still differing).
`W4-S8` and `W7-S4` (market value off quantity x price) are brought no closer this round: their act is per-lot UNVERIFIED, after the exact-lot apply.

## Fan-out

`fanout: 4 of 4 chains, cap 8, reason: BP-c-1, BP-c-4, BP-c-6 and BP-c-7 are disjoint in write set and data; BP-c-2, BP-c-3 and BP-c-5 are staged on a data edge and spawn nothing at the cut.`

## Rule 24 record (the typed-result sets this decomposition introduces)

| set | classes | domain and denominator | state coherence |
|---|---|---|---|
| off-canonical lot source (BP-c-7) | `EQUALS_OLDER_CANONICAL_VERSION`, `EQUALS_DAILY_FILE_ROW`, `EQUALS_NAMED_OTHER_SOURCE`, `UNEXPLAINED` | one of the 1,859 `PRICED_OFF_NO_CANONICAL` lots; denominator `lots_total` printed | `UNEXPLAINED` names what could not be read and claims no cause; the first matching class in the listed order takes the lot |
| cap verdict (BP-c-4) | `CAP`, `NOT_A_CAP`, `NOT_DETERMINED` | the export's row count per day over at least 10 days | `NOT_DETERMINED` names what could not be read; the verdict is not inferred from one round number alone |
| sentinel cause (BP-c-6) | `EXPORT_WINDOW_RULE`, `VENDOR_EMPTY`, `RUNNER_DEFECT`, `NOT_DETERMINED` | the Monday/Tuesday header-only first exports | one cause per record, with evidence; `NOT_DETERMINED` is not a cause |
| replay result (BP-c-2) | `UNCHANGED`, `CHANGED`, `NOW_CARRY_FORWARD`, `NOT_RECOMPUTABLE` | unchanged from round 2 | unchanged from round 2; the par-quoted rows must all read `UNCHANGED` |

Same grain within each set (one row per element), one intent per set, and each grader enumerates its closed set and refuses another key (`checks/r3_checks.py`, 35 self-test arms).

## Lenses read at L5 (each order's preflight carries its disposition)

| lens | disposition |
|---|---|
| `comp-schedule` | every cell DECLARED-NOT-APPLICABLE: no rule, schedule or cadence is added or changed; BP-c-6 READS the producers' schedules |
| `comp-iam` | every cell DECLARED-NOT-APPLICABLE: reads only (`s3api get-object`/`list-objects-v2`/`list-object-versions`/`head-object`; `logs filter-log-events`; `lambda get-function-configuration`; `events describe-rule`). No grant is added; a denied read is a finding |
| `comp-adversary` | RUN by the issuer: each grader has a good fixture and mutants (`checks/r3_selftest.py`, 35 arms OK); each criterion fails at the base. Blindness: the graders prove shape and arithmetic, not that a measurement is right; the issuer re-reads cited objects at the drain |
