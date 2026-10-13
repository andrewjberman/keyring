# ADVI_FIRMBKTS -- DECOMPOSITION (L5) -- ROUND 7, A SECOND FRESH READER AND THE EXEC-SUMMARY TRIGGER FIX (PRD v1.4)

```json
{
 "project": "ADVI_FIRMBKTS",
 "directive": "D8",
 "macro": "ADVI",
 "fabric": "dell1",
 "decomp_version": "v7",
 "step": 5,
 "prd_ref": "org/missions/D8/ADVI/ADVI_FIRMBKTS/prd/ADVI_FIRMBKTS_PRD.md (v1.4 @1e5dcef9cb)",
 "order_ref": "1.0.0_SA_CTO~DELL1 msg 4703 and msg 4707: org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/ROUND_ANALYSIS.round6.md (section 3 and ADDENDUM 1)",
 "author": "2.0.0_SA_COO~B1",
 "round": 7,
 "rectangle": "the round-6 analysis's enrichment list and its ADDENDUM 1: item 1, a second fresh blind reader over the same 150 (FWD-1 grades REALIZED when reader 2 agrees with reader 1 on 150 of 150, any disagreement named); item 2, the exec-summary trigger fix in its ruled order: the WARN text first (a measurement, no served change), the region as ONE variable on the put-events call only, the generator's dry-run path (a sample read BEFORE serving), then the fix deploy under its pair and the first chain's read. Item 3 is carried, not a cell.",
 "cells": 7,
 "chains": 4,
 "join_cells": 1,
 "ground_truth": "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round7/L5_FACTS.md",
 "frozen": true
}
```

**Author:** `2.0.0_SA_COO~B1` (dell1). **Inputs:** `ledger/ROUND_ANALYSIS.round6.md` sections 1-4 and ADDENDUM 1; the CVO's `REMEDIATION_v7.md`;
the round-6 packet `deliverables/2.0.0_SA_COO~B1/round6/R6_CLOSE.md`; `round7/L5_FACTS.md`.

## Round 7 -- the cells

| cell | item | serves | owned files | depends on | slot, class | risk | at the cut |
|---|---|---|---|---|---|---|---|
| `FB-j-1` a second fresh blind reader over the same 150 | 1 | FWD-1 | its worktree `C:/dev/wk-firmbkts-r7-reader` (the issuer ingests) | -- | ~68 worker-light | LOCAL | pending |
| `FB-j-2` the dispatcher's chain-complete WARN prints the CLI's error text (300 chars) | 2 | FWD-5 | `data/black_diamond/scripts/gold/gold_dispatch.sh` (inside `emit_chain_complete`) | -- | ~69 worker | WORLD (path floor) | pending |
| `FB-j-3` deploy the text-only dispatcher; read the next chain's WARN (the measurement) | 2 | FWD-5 | `deliverables/0.7.0_AE_CloudOps~FB1/EMIT_ERROR_TEXT.json` | `FB-j-2` | `0.7.0_AE_CloudOps~FB1` seat order | WORLD | parked |
| `FB-j-4` the put-events call takes `--region "$EVENTS_REGION"`; no other call changes | 2 | FWD-5 | `data/black_diamond/scripts/gold/gold_dispatch.sh` | `FB-j-2`, `FB-j-3` (same file; the measured cause) | ~71 worker | WORLD (path floor) | parked |
| `FB-j-5` the generator's dry-run path (`event.dry_run` + `advisor_ids` <= 10; no S3 write) | 2 | FWD-5 | `infra/aws/lambda/exec-summary-generator/{lambda_function.py,tests/test_dry_run.py}` | -- | ~70 worker | WORLD (path floor) | pending |
| `FB-j-6` deploy the dry-run generator (Terraform, under its pair); read a sample before anything serves | 2 | FWD-5 | `deliverables/0.7.0_AE_CloudOps~FB1/DRYRUN_SAMPLE.json` | `FB-j-5`, its pair | `0.7.0_AE_CloudOps~FB1` seat order | WORLD | parked |
| `FB-j-7` the fix deploy (dispatcher with `EVENTS_REGION`) under its pair; the first chain read; `D1-W65-S1`'s disarm read (**JOIN**) | 2 | FWD-5 | `deliverables/0.7.0_AE_CloudOps~FB1/FIRST_CHAIN_READ.json`, `rollback_versions.json` | `FB-j-4`, `FB-j-6`, the fix pair | `0.7.0_AE_CloudOps~FB1` seat order | WORLD | parked |

No two cells write one file at once: `FB-j-2` and `FB-j-4` both edit the dispatcher, so they are sequential (`FB-j-4` waits on `FB-j-2`'s merge).

**Chains** (cells joined by a real data dependency are one chain): `{FB-j-1}`, `{FB-j-2, FB-j-3, FB-j-4}`, `{FB-j-5, FB-j-6}`, and the JOIN
`{FB-j-7}`, which consumes the last cell of each of the two chains above. M = 3 chains + 1 join.

## Staged cells (parked at the cut; each un-parks by the issuer's amendment, with its pair where one is named)

| order | owner | un-park |
|---|---|---|
| `FB-j-3` | `2.0.0_SA_COO~B1` | `FB-j-2` merged and PASS at the merged HEAD |
| `FB-j-4` | `2.0.0_SA_COO~B1` | `FB-j-3` read (its measured text names the cause; a different cause re-cuts this cell on that cause) and `FB-j-2` merged |
| `FB-j-6` | `2.0.0_SA_COO~B1` | `FB-j-5` merged and PASS; the dry-run deploy's pair signed (COO half: the issuer's, authored at the un-park) |
| `FB-j-7` | `2.0.0_SA_COO~B1` | `FB-j-3` read; `FB-j-4` merged; `FB-j-6`'s sample read by the CTO; the fix pair signed by both halves at the current bytes |

## Not cells of this round (each with its owner and its un-park condition)

| item | owner | un-park |
|---|---|---|
| FB-h-5 / D1-S41: the validator's live non-admin read | `1.0.0_SA_CTO~DELL1` | the first organic non-admin validator line, or a non-admin session a seat holds |
| D1-S43: the fence instrument's re-baseline | NFRA_CTLPLN (laptop) via MSTR | the owner |
| the BD pricing rules | `4.0.0_SA_CRO~DELL1` (a brief; Andrew confirms its DONE WHEN) | not FIRMBKTS's |
| PRD sequencing R3 and R4 | `1.0.0_SA_CTO~DELL1` | named into a later enrichment list |
| c290; portal `ROUTER_FIRM_SUFFIX` PROD; the optional read of the dry-run sample | Andrew | his word |

## Fan-out

`fanout: 3 of 3 chains, cap 8, reason: three worker subagents (FB-j-1 ~68, FB-j-2 ~69, FB-j-5 ~70) are disjoint in write set; the seat orders
(FB-j-3, FB-j-6, FB-j-7 to 0.7.0_AE_CloudOps~FB1) and FB-j-4 (~71) are staged and spawn nothing at the cut.` Three orders are `pending`, four `parked`.

## Lenses read at L5 (each order's preflight carries its disposition)

| lens | disposition |
|---|---|
| `comp-schedule` | every cell DECLARED-NOT-APPLICABLE (no rule, schedule or cadence is added or changed; the existing `exec-summary-trigger` rule is the consumer) |
| `comp-iam` | `FB-j-3` and `FB-j-7`: one `s3:PutObject` of the dispatcher key by the actor's identity (the runner role already syncs it); `FB-j-6`: a resource-scoped `safe-apply` of one function; no grant is added; the rest none |
| `comp-adversary` | each criterion is dry-run at the base (FAIL as expected) and on a reference patch (PASS); each grader on a good and a mutant fixture (`L5_FACTS.md`) |

## Amendment 1 (2.0.0_SA_COO~B1, 2026-10-13 ~09:3xZ): cell `FB-j-8` added by the CTO's order (FB-j-6 CTO half ADDENDUM 2, msg 4731)

`FB-j-6`'s one dry run returned ten artifacts with zero bullets. The CTO ruled the empty pass NOT a sample and ordered: the May artifacts of the same
ten advisors read (the issuer read them at 08:5xZ: 0 bullets in May and in the canonical copies; the legacy version histogram over 152 objects is 304-311
bytes), an offline pre-screen of all advisors with no model call, a targeted dry run as the positive control, and a per-advisor no-regression criterion
in `FB-j-7`. Cells are now 8, chains 4 and 1 join: `FB-j-8` (seat order to `0.7.0_AE_CloudOps~FB1`, WORLD, read-only plus at most one dry-run
invocation under the signed pair) is a new read in the generator chain (`{FB-j-5, FB-j-6, FB-j-8}`); `FB-j-7` (the join) also waits on its record.

| cell | item | serves | owned files | depends on | slot, class | risk | at the cut |
|---|---|---|---|---|---|---|---|
| `FB-j-8` the slot pre-screen: which of the 158 advisors fire a slot today (offline, no model call), then ONE targeted dry run | 2 | FWD-5 | `deliverables/0.7.0_AE_CloudOps~FB1/SLOT_PRESCREEN.json`, `.md`, `SLOT_DRYRUN_ARTIFACTS.json` | `FB-j-6` | `0.7.0_AE_CloudOps~FB1` seat order | WORLD | pending |
