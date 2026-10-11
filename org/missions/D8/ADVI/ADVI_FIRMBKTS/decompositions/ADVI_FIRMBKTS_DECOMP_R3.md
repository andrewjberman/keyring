# ADVI_FIRMBKTS -- DECOMPOSITION (L5) -- ROUND 3, THE CUTOVER WINDOW AND THE ENRICHMENT (PRD v1.3)

```json
{
 "project": "ADVI_FIRMBKTS",
 "directive": "D8",
 "macro": "ADVI",
 "fabric": "dell1",
 "decomp_version": "v3",
 "step": 5,
 "prd_ref": "org/missions/D8/ADVI/ADVI_FIRMBKTS/prd/ADVI_FIRMBKTS_PRD.md (v1.3; the CTO's header-only fabric edit at d9822d7b2d re-opens no half)",
 "order_ref": "1.0.0_SA_CTO~DELL1 msg 3521: org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/ROUND_ANALYSIS.round2.md @ba27c8c055",
 "author": "2.0.0_SA_COO~B1",
 "round": 3,
 "rectangle": "the enrichment list (items 1-5) plus the remediations the CVO's REMEDIATION_v3 names to this seat: the cutover window's four acts (the advTenant remedy deployed, the platinum producers repointed, the delta copy, the list entry + map value + all-ASCII router + F6 deploy), the compare instrument (item 2), the table repair under the grain ruling (item 3), two project-free blind readers (item 4), F4's own-firm admit exercised (item 5); and the two measurement cells the window's blast radius needs: the producer census and the advTenant build with its Rule-24 record",
 "cells": 11,
 "chains": 8,
 "join_cells": 0,
 "ground_truth": "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round3/L5_FACTS.md (read-only measurement 2026-10-11 ~05:2xZ-06:0xZ)",
 "frozen": true
}
```

**Author:** `2.0.0_SA_COO~B1` (dell1), seated by `1.0.0_SA_CTO~DELL1`, round-2 analysis msg 3521. **Inputs:**
- PRD v1.3 (ENDPOINT, CONTRACTS, DEC-1..17, CELL CANDIDATES F1-F13);
- the CTO's round-2 analysis, sections 2 and 3, and `NEVER_WIDEN_ROUND2_F7_COPY_*` conditions 1-3;
- `surprise-channel/remediations/REMEDIATION_v3.md` (rows owed by this seat: `D1-W9-S2`, `D1-W9-S5`, `D1-W4-S7`, `D1-W7-S1`,
  `D1-C-S7`);
- `deliverables/2.0.0_SA_COO~B1/round3/L5_FACTS.md`.

## Round 3 -- the cells

| cell | item | serves (cell_refs) | candidate | owned files | depends on | slot, class | risk |
|---|---|---|---|---|---|---|---|
| `FB-f-1` the compare instrument | 2 | FWD-4 | F7 | `round3/checks/r3_f7.py` | -- | ~11 worker-light, direct act | LOCAL |
| `FB-f-2` table repair, grain ruling | 3 | FWD-2 | F2 | `deliverables/mapping_v3.json`, `MAPPING_TABLE_v3.md` | -- | ~12 worker | LOCAL |
| `FB-f-3` blind reader A, project-free | 4 | FWD-1 | F3 | `round3/blind/` (the issuer's ingest) | -- | ~13 worker-light | LOCAL |
| `FB-f-4` blind reader B, project-free | 4 | FWD-1 | F3 | `round3/blind/` (the issuer's ingest) | -- | ~14 worker-light | LOCAL |
| `FB-f-5` F4's own-firm admit | 5 | FWD-4, FWD-6 | F4 | `deliverables/0.9.0_WK_ADVI_FIRMBKTS~15/` | -- | ~15 worker | LOCAL |
| `FB-f-6` producer census | 1 (step 2) | FWD-5, FWD-4 | F10 | `deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/` | -- | ~16 worker | LOCAL |
| `FB-f-7` advTenant: record + dormant build | 1 (step 1) | FWD-3, FWD-4 | F6 | `shared-advisor-router/`, `shared-advisor-router-response/`, `_shared/firm-config.mjs`, `lib/opal_naming.py`, the registry row | -- | ~17 worker | WORLD (infra floor), built dormant |
| `FB-f-8` act 1: deploy the advTenant build | 1 (step 1) | FWD-3, FWD-4 | F6 | the Terraform apply of the two functions | `FB-f-7` | ~17 (queue) | WORLD, STAGED |
| `FB-f-9` act 2: producers repoint | 1 (step 2) | FWD-5, FWD-4 | F10 | the writers `FB-f-6` names | `FB-f-6` | ~16 (queue) | WORLD, STAGED |
| `FB-f-10` act 3: the delta copy | 1 (step 3) | FWD-4 | F7 | `deliverables/0.9.0_WK_ADVI_FIRMBKTS~11/` (second manifest), the destination keys | `FB-f-1` | ~11 (queue) | WORLD, STAGED |
| `FB-f-11` act 4: list entry, map value, all-ASCII router, F6 deploy | 1 (step 4) | FWD-4, FWD-3 | F6, F7 | `shared-advisor-router/index.mjs`, the registry map value, the Terraform apply | -- | ~18 worker | WORLD, STAGED |

No two cells write one file. The only shared reads are `mapping.json`, `census.json`, `mapping_v2.json` (never edited) and
the round-2 F7 manifest.

**Chains** (cells joined by a real data dependency are one chain): `{FB-f-1, FB-f-10}`, `{FB-f-6, FB-f-9}`,
`{FB-f-7, FB-f-8}`, `{FB-f-11}`, `{FB-f-2}`, `{FB-f-3}`, `{FB-f-4}`, `{FB-f-5}`. M = 8.

**The window's order is a sequence, not an edge.** Acts 1-4 run in the CTO's order (`FB-f-8`, `FB-f-9`, `FB-f-10`,
`FB-f-11`), each opened by its own never-widen pair and its change-management entry opened first; that order is
enforced by each order's un-park condition, not by a file one cell hands another.

**Fan-out:** 7 workers spawned now for 8 chains (the four staged acts ride three of the seven slots' queues, and
`FB-f-11` takes `~18` when its pair signs), cap 8. Seven orders spawn at the cut; the four staged acts do not.

## Not in round 3 (ruled here, each with its owner and its un-park condition)

| item | ruling | owner, un-park |
|---|---|---|
| Inflection's and Cottonwood's cutovers (F8, F9) | NOT cut. Every act on `opal-data-inf` waits on FWD-7 and FWD-8. | Andrew; then `1.0.0_SA_CTO~DELL1` |
| F11 bronze and silver home; F12 retirement proofs | later rounds, per the PRD's arc | CTO's round-3 analysis |
| deleting the old bucket's platinum keys | never in this window: the old bucket is untouched through the rollback window; a delete is Andrew's word, act by act (DEC-17) | Andrew |
| the PRD's F4 wording (row `D1-S1`) | the CTO lands it as an addendum AFTER this issuance, so a re-hash cannot refuse the issuance at LIMB 6 (analysis section 2 item 6) | `1.0.0_SA_CTO~DELL1` |
| the gate disagreement (row `D1-S10`) | filed to the gate owner as `NFRA_GATSCP-D1-S16`; until it lands, every order here names the stem | gate owner |

## Battery

| lens | disposition |
|---|---|
| `comp-schedule` | `FB-f-9` may change the trigger of a producer (the census names it); every other cell DECLARED-NOT-APPLICABLE. A schedule change is read by the amendment that un-parks `FB-f-9`. |
| `comp-iam` | RUN by the issuer's reading at L5: `FB-f-5` needs `ssm:SendCommand` on one instance (measured Success at the dry run) and `sts:AssumeRole` of the research role from the runner's profile (measured Success); `FB-f-10` needs `s3:PutObject` on `opal-data-49financial` (measured `allowed` in round 2); `FB-f-8` and `FB-f-11` need the Terraform deploy chain of `infra/aws/terraform/portal-auth/` and are read at their amendment. |
| `comp-adversary` | RUN by the issuer as the checks' controls (L5_FACTS section 6): every check at base, on a reference or fixture, and against at least one mutant. Blindness: the lens cannot see which files a reader opened (the reader's directory listing and its `OPENED:` line are the witnesses), and cannot see the producers' next write window. |

## Rule 24 record

New enumerated values: `kind: marker` and `rule` strings `3a`..`3d` on mapping rows, `partition_rule: per-date`, collision
`verdict: split`. (i) MECE: every census class is placed once or re-gridded into children that sum to its live
listing; a placeholder is RETIRE, a completion marker is `kind: marker` in a `state/` home. (ii) grain: one row per class
or child. (iii) one axis: where the class's bytes end up. (iv) state coherence: RETIRE moves and deletes nothing; FAULT
changes nothing; a `split` verdict changes no key. The advTenant record is itself a cell deliverable (`FB-f-7`).

## Placement

Every cell executes on dell1 (`fabric: dell1`).
