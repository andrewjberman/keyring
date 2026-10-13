# ADVI_FIRMBKTS -- DECOMPOSITION (L5) -- ROUND 5, THE CUTOVER'S OPEN READS AND THE ENRICHMENT (PRD v1.4)

```json
{
 "project": "ADVI_FIRMBKTS",
 "directive": "D8",
 "macro": "ADVI",
 "fabric": "dell1",
 "decomp_version": "v5",
 "step": 5,
 "prd_ref": "org/missions/D8/ADVI/ADVI_FIRMBKTS/prd/ADVI_FIRMBKTS_PRD.md (v1.4 @1e5dcef9cb)",
 "order_ref": "1.0.0_SA_CTO~DELL1 msg 4649 (ROUND_ANALYSIS.round4.md section 3, the ENRICHMENT LIST) and msg 4653 (item 7)",
 "author": "2.0.0_SA_COO~B1",
 "round": 5,
 "rectangle": "the round-4 analysis's enrichment list: FWD-1's 11 disagreements re-read under the stated table rule; the validator's ownership decisions replayed offline and read once live; the validator spec test-only; the exec-summary put-events diagnosis, read-only; the Black Diamond pricing findings S32-S34 quantified on served values, read-only; the fence instrument fixed (test-only). Item 6 (act 2's first scheduled chain read) is executed at the cut.",
 "cells": 8,
 "chains": 8,
 "join_cells": 0,
 "ground_truth": "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round5/L5_FACTS.md",
 "frozen": true
}
```

**Author:** `2.0.0_SA_COO~B1` (dell1), seated by `1.0.0_SA_CTO~DELL1` (round-4 analysis, msg 4649, and msg 4653). **Inputs:** the
round-4 analysis `ledger/ROUND_ANALYSIS.round4.md` sections 1-4; the CVO's `ADJUDICATION_v5.md` (`D1-C-S29`, `D1-C-S33`, `D1-C-S36`,
`D1-C-S37`); the round-4 packet `deliverables/2.0.0_SA_COO~B1/round4/R4_CLOSE.md`; `round5/L5_FACTS.md`; `round5/RULING_FWD1_R5.md`.

## Round 5 -- the cells

| cell | item | serves | candidate | owned files | depends on | slot, class | risk |
|---|---|---|---|---|---|---|---|
| `FB-h-1` blind reader A, second round: the 11 that disagreed and 11 controls | 1 | FWD-1 | F3 | its worktree `C:/dev/wk-firmbkts-r5-reader-a` (the issuer ingests the answers) | -- | ~61 worker-light | LOCAL |
| `FB-h-2` blind reader B, second round | 1 | FWD-1 | F3 | its worktree `C:/dev/wk-firmbkts-r5-reader-b` | -- | ~62 worker-light | LOCAL |
| `FB-h-3` the validator's ownership decisions replayed offline on the legacy and the canonical map | 2 | FWD-4 | F6 | `deliverables/0.9.0_WK_ADVI_FIRMBKTS~63/` (harness, `REPLAY_RESULT.json`) | -- | ~63 worker | LOCAL |
| `FB-h-4` the validator's ownership-key spec follows the flip (`D1-C-S33`), test-only | 3 | FWD-4 | F6 | `infra/aws/lambda-edge/auth-validator-edge/tests/ownership_key.spec.mjs` | -- | ~64 worker | WORLD (path floor) |
| `FB-h-5` the validator's canonical ownership read exercised once by a non-admin request (live half) | 2 | FWD-4 | F6 | `deliverables/0.7.0_AE_CloudOps~FB1/round5/VALIDATOR_LIVE_READ.json` | -- | `0.7.0_AE_CloudOps~FB1` seat order | WORLD |
| `FB-h-6` the exec-summary put-events diagnosis (read-only) | 4 | FWD-5 | F10 | `deliverables/0.9.0_WK_ADVI_FIRMBKTS~65/` | -- | ~65 worker | LOCAL |
| `FB-h-7` the Black Diamond pricing findings S32-S34 quantified (read-only) | 5 | (rows D1-S32..S34) | -- | `deliverables/0.9.0_WK_ADVI_FIRMBKTS~66/` | -- | ~66 worker | LOCAL |
| `FB-h-8` the fence-scoped-rows instrument: explicit UTF-8 and the object-shape fixture (`D1-S28`), test-only | 7 | (row D1-S28) | -- | `infra/aws/terraform/shared-infra/tests/` | -- | `0.7.0_AE_CloudOps~FB1` seat order | WORLD (path floor) |

No two cells write one file. Shared reads only: `round4/READING_KEY.json`, `mapping_v4.json`, the validator source, the
dispatcher script, the registry and the generated `firm-config.mjs`.

**Chains** (cells joined by a real data dependency are one chain): `{FB-h-1}`, `{FB-h-2}`, `{FB-h-3}`, `{FB-h-4}`, `{FB-h-5}`,
`{FB-h-6}`, `{FB-h-7}`, `{FB-h-8}`. M = 8. `FB-h-3` and `FB-h-5` are two halves of one comparison (item 2) but share no data:
the replay needs no live line and the live read needs no replay.

## Done at the cut, not a cell

**Item 6 -- act 2's first scheduled chain read.** Executed by the issuer at 06:20Z (`L5_FACTS.md` fact 9): `r3_act2_reads.py new-home --since
2026-10-13T03:30:00Z` reads 11 of 11 served classes written; `old-home --since 2026-10-12T06:22:08Z` reads 0 keys modified of 11
classes. The CVO re-reads at L9. The "maps stayed byte-equal" half of the CTO's wording is measured by `FB-h-3` (`bytes_equal`).

## Issuer acts of the round (records, not cells)

- `D1-C-S34` (FB-f-9 AC2 and AC3 still typed `--since <MOVE_TS>`): the issuer amends those two criteria to the measured value
  `2026-10-12T06:22:08Z` in its own amendment commit, stating the gate limb that graded it (the order's `<placeholders>` read).
- `D1-W60-S3` (the naming gate exempts `/tests/` and not `test/`) is ROUTED to `LGIC_ENFORCE` by the CTO; `D1-S28` is `FB-h-8`.
- Portal `ROUTER_FIRM_SUFFIX` (`49financial` -> `bd`): not in the CTO's list; a client-facing module; PROD waits on Andrew.

## Not in round 5 (each with its owner and its un-park condition)

| item | owner | un-park |
|---|---|---|
| the exec-summary generator's FIX (a pair naming up to 158 summary keys, a sample read before serving, prior VersionIds) | this project, a later cell | `FB-h-6`'s verdict, then the CTO's ruling |
| the BD pricing rules' change (de-duplication, an explicit price precedence, trade-date keying) | `4.0.0_SA_CRO` (a brief under its own project) | `FB-h-7`'s recommendation `BRIEF_TO_CRO` |
| the PRD sequencing R3 (the `mdpf/{firm}/platinum/*` serving grant) and R4 (the joint reader census) | `1.0.0_SA_CTO~DELL1` | named into a later enrichment list |
| FWD-7 and FWD-8 (the prohibited key, B2; DEC-13) | Andrew | his word |
| c290: one real SEV1 publish delivered | Andrew | his word (asked by the CTO) |
| the performance adapter's PutObject simulate and its evidence run | `IRPT_PERFADPT`'s COO | the next server-issued selection |

## Fan-out

`fanout: 8 of 8 chains, cap 8, reason: six worker subagents (FB-h-1 to -4, -6 and -7) and two seat orders (FB-h-5 and FB-h-8 to
0.7.0_AE_CloudOps~FB1) are disjoint in write set; the two seat orders are one seat's queue and spawn nothing.` All eight orders are
`pending` at the cut.

## Lenses read at L5 (each order's preflight carries its disposition)

| lens | disposition |
|---|---|
| `comp-schedule` | every cell DECLARED-NOT-APPLICABLE (reads, tests and records; no cron, rule or cadence changes) |
| `comp-iam` | `FB-h-3`: two `get-object` reads; `FB-h-6`, `-7`, `-5`: read verbs only (CloudTrail, EventBridge, IAM, S3, CloudWatch); no grant is added or changed; `FB-h-8`: the instrument's own reads |
| `comp-adversary` | each criterion is dry-run at base (FAIL as expected) and each shape grader on a good and a mutant fixture (`L5_FACTS.md`) |
