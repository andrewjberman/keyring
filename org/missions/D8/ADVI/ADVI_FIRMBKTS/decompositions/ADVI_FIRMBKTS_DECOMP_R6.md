# ADVI_FIRMBKTS -- DECOMPOSITION (L5) -- ROUND 6, ONE BLIND READ OF ALL 150 AND THE EXEC-SUMMARY EMIT PATH (PRD v1.4)

```json
{
 "project": "ADVI_FIRMBKTS",
 "directive": "D8",
 "macro": "ADVI",
 "fabric": "dell1",
 "decomp_version": "v6",
 "step": 5,
 "prd_ref": "org/missions/D8/ADVI/ADVI_FIRMBKTS/prd/ADVI_FIRMBKTS_PRD.md (v1.4 @1e5dcef9cb)",
 "order_ref": "1.0.0_SA_CTO~DELL1 msg 4693: org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/ROUND_ANALYSIS.round5.md (section 3, the ENRICHMENT LIST)",
 "author": "2.0.0_SA_COO~B1",
 "round": 6,
 "rectangle": "the round-5 analysis's enrichment list: item 1, ONE blind read of all 150 canonical locations under the stated face by a worker that authored neither earlier read; item 2, the exec-summary emit path read runner-side, then one non-matching test event only if still indeterminate. Item 3 (carried: D1-S41 / FB-h-5 parked on the CTO; D1-S43 with NFRA_CTLPLN) is not a cell. The FIX is cut on the cause, under its own pair, in the next round.",
 "cells": 2,
 "chains": 2,
 "join_cells": 0,
 "ground_truth": "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round6/L5_FACTS.md",
 "frozen": true
}
```

**Author:** `2.0.0_SA_COO~B1` (dell1), seated by `1.0.0_SA_CTO~DELL1` (round-5 analysis, msg 4693). **Inputs:** `ledger/ROUND_ANALYSIS.round5.md`
sections 1-4; the CVO's `REMEDIATION_v6.md`; the round-5 packet `deliverables/2.0.0_SA_COO~B1/round5/R5_CLOSE.md`; `round6/L5_FACTS.md`.

## Round 6 -- the cells

| cell | item | serves | candidate | owned files | depends on | slot, class | risk |
|---|---|---|---|---|---|---|---|
| `FB-i-1` ONE blind reader over all 150 canonical locations under the stated face | 1 | FWD-1 | F3 | its worktree `C:/dev/wk-firmbkts-r6-reader` (the issuer ingests the answers) | -- | ~67 worker-light | LOCAL |
| `FB-i-2` the exec-summary emit path read runner-side; at most one non-matching test event | 2 | FWD-5 | F10 | `deliverables/0.7.0_AE_CloudOps~FB1/RUNNER_EMIT_READ.json` and `.md` | -- | `0.7.0_AE_CloudOps~FB1` seat order | WORLD |

No two cells write one file. Shared reads: `round4/READING_KEY.json`, the dispatcher script, the registry.

**Chains** (cells joined by a real data dependency are one chain): `{FB-i-1}`, `{FB-i-2}`. M = 2.

## Not cells of this round (each with its owner and its un-park condition)

| item | owner | un-park |
|---|---|---|
| FB-h-5 / D1-S41: the validator's live non-admin read | `1.0.0_SA_CTO~DELL1` | the first organic non-admin validator line on the accounts or relationship paths, or a non-admin session a seat holds |
| D1-S43: the fence instrument's four re-baseline causes | NFRA_CTLPLN (laptop) via MSTR | the owner's re-baseline; the simulator arms need the laptop identity |
| the exec-summary FIX (a pair naming up to 158 summary keys, a sample read first, prior VersionIds) | this project, round 7 | `FB-i-2`'s verdict, then the CTO's analysis |
| the BD pricing rules (S32 first) | `4.0.0_SA_CRO~DELL1` (a brief under its own project; Andrew confirms its DONE WHEN) | not FIRMBKTS's |
| PRD sequencing R3 (the `mdpf/{firm}/platinum/*` grant) and R4 (the joint reader census) | `1.0.0_SA_CTO~DELL1` | named into a later enrichment list |
| c290: one real SEV1 publish; portal `ROUTER_FIRM_SUFFIX` PROD | Andrew | his word |

## Fan-out

`fanout: 2 of 2 chains, cap 8, reason: one worker-light subagent (FB-i-1, ~67) and one seat order (FB-i-2 to 0.7.0_AE_CloudOps~FB1); disjoint
in write set; the seat order spawns nothing.` Both orders are `pending` at the cut.

## Lenses read at L5 (each order's preflight carries its disposition)

| lens | disposition |
|---|---|
| `comp-schedule` | both DECLARED-NOT-APPLICABLE (no rule, schedule or cadence is added or changed) |
| `comp-iam` | `FB-i-1`: none; `FB-i-2`: reads with the dell1 identity and one conditional `events:PutEvents` from the runner's own instance profile, which already holds it (round 5 `FB-h-6`); no grant is added |
| `comp-adversary` | each criterion is dry-run at base (FAIL as expected) and each grader on a good and mutant fixture (`L5_FACTS.md`) |
