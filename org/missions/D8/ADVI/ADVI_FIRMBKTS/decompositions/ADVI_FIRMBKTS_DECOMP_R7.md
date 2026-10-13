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

## Amendment 2 (2.0.0_SA_COO~B1, 2026-10-13 ~10:0xZ): cells `FB-j-9` and `FB-j-10` added by the CTO's orders (ROUND_ANALYSIS.round3.md ADDENDA 14 and 15, msgs 4733 and 4735)

`FB-j-8` (complete): all 158 advisors fire a slot offline; every one of the 81 fired slots in two dry runs was DROPPED in `_build_slot`. The cause,
reproduced offline by the issuer and confirmed by FB1 against the deployed layer (`anthropic-sdk-deps:1`, SDK 0.45.0): `_call_llm` passes
`betas=[...]` to `client.messages.create`, which has no such parameter; the `TypeError` is raised before any request and swallowed by
`except Exception`. The summaries have never held text. The CTO ruled: fix it HERE (not a CRO brief, not "trigger first"): remove the `betas`
argument (`cache_control` already does the caching) and log every drop's exception class; the reproducing test must pass and a `betas` mutant
must fail; deploy under `FB-j-6`'s shape; dry-run TEN pre-screened advisors; the bullets must be non-empty; the CTO reads the text against the
figures for wording, PII and accuracy; ONLY THEN `FB-j-7` (citing that sample) and `FB-j-4`. Cells are now 10, chains 4 and 1 join.

| cell | item | serves | owned files | depends on | slot, class | risk | at the cut |
|---|---|---|---|---|---|---|---|
| `FB-j-9` the model call stops passing `betas`; every slot drop logs its exception class (reproducing test, `betas` mutant) | 2 | FWD-5 | `infra/aws/lambda/exec-summary-generator/{lambda_function.py,tests/test_slot_drop_log.py}` | `FB-j-5` (same file, merged) | ~73 worker | WORLD (path floor) | pending |
| `FB-j-10` deploy it (a second apply, under the pair's addendum 1); ONE dry run of TEN pre-screened advisors; read the drop classes and the bullets | 2 | FWD-5 | `deliverables/0.7.0_AE_CloudOps~FB1/SLOT_DROP_CAUSE.json`, `DRYRUN10_ARTIFACTS.json` | `FB-j-9`, the addendum | `0.7.0_AE_CloudOps~FB1` seat order | WORLD | parked |

**Ordering (the CTO's):** `FB-j-7` (the regeneration pair and the first-chain read) and `FB-j-4` (the trigger) do not move until `FB-j-10`'s
bullets are non-empty and read by the CTO; `FB-j-7`'s pair cites that sample. `FB-j-7`'s un-park condition "`FB-j-6`'s record read" is
superseded by "`FB-j-10`'s record read and its sample read by the CTO against the figures".

## Amendment 3 (2.0.0_SA_COO~B1, 2026-10-13 ~10:5xZ): cells `FB-j-11`, `FB-j-12`, `FB-j-13` added by the CTO's sample read (`ledger/CTO_SAMPLE_READ_FB_J_10_EXEC_SUMMARIES_20261013.md`)

`FB-j-10` (complete): the second apply works, 39 bullets for ten advisors, 0 drops, listing identical. The CTO read the sample: four slots read
well; `top_nna_mover` is broken (one placeholder `rel_id "0"` pools $9.6M under two advisors, raw relationship ids are printed, a client display name
leaked past the PII guard); one bullet (IQLT -69.2 percent) is implausible. His rulings for the regeneration pair: (a) `top_nna_mover` disabled by
config, the product fix to the CRO's exec-summary brief; (b) the guard learns client display names; (c) IQLT traced to its cost basis and price
before serve; (d) Andrew is offered the sample before `FB-j-4`. Cells are now 13, chains 5 and 1 join.

| cell | item | serves | owned files | depends on | slot, class | risk | at the cut |
|---|---|---|---|---|---|---|---|
| `FB-j-11` the slot switch (`top_nna_mover` OFF by config), the client-name guard, and the Terraform carrier `disabled_slots` | 2 | FWD-5 | `infra/aws/lambda/exec-summary-generator/{lambda_function.py,tests/test_slot_switch_guard.py}`, `infra/aws/terraform/exec-summary/{variables.tf,main.tf}` | `FB-j-9` (same file, merged) | ~74 worker | WORLD (path floor) | pending |
| `FB-j-12` the IQLT -69.2 percent traced to its cost basis and price (read-only) | 2 | FWD-5 | `deliverables/0.9.0_WK_ADVI_FIRMBKTS~75/` | -- | ~75 worker | LOCAL | pending |
| `FB-j-13` the third apply (code plus ONE environment key, switch ON) and a second ten-advisor dry run, texts beside figures | 2 | FWD-5 | `deliverables/0.7.0_AE_CloudOps~FB1/SLOT_SWITCH_SAMPLE.json` and the artifact and figure files | `FB-j-11`, the addendum 2 | `0.7.0_AE_CloudOps~FB1` seat order | WORLD | parked |

`FB-j-7` (the join) now also waits on: `FB-j-11` merged and deployed (via `FB-j-13`), `FB-j-12`'s classification read by the CTO (a data defect holds the
affected bullets), the second sample read by the CTO and offered to Andrew, and the regeneration pair signed citing it. `FB-j-4` waits on `FB-j-7`'s pair.

## Amendment 4 (2.0.0_SA_COO~B1, 2026-10-13 ~11:0xZ): cell `FB-j-14` added by the CTO's order (msg 4747, ADDENDA 4-5 of his FB-j-6 half)

The `FB-j-10` sample files (`DRYRUN10_ARTIFACTS.json`, `DRYRUN10_FIGURES.json`) hold raw relationship ids and are already on `origin/box/dell1`. The CTO
ruled: scrub forward, hash relationship ids at write time from now on, no history rewrite (Andrew's word; he recommends against it). Cells are now 14.

| cell | item | serves | owned files | depends on | slot, class | risk | at the cut |
|---|---|---|---|---|---|---|---|
| `FB-j-14` the ten-advisor sample files hold no raw relationship id (hashed forward) | 2 | (privacy hygiene of the sample) | `deliverables/0.7.0_AE_CloudOps~FB1/DRYRUN10_ARTIFACTS.json`, `DRYRUN10_FIGURES.json` | -- | `0.7.0_AE_CloudOps~FB1` seat order | LOCAL | pending |

## Amendment 5 (2.0.0_SA_COO~B1, 2026-10-13 ~10:3xZ): the first regeneration lands EMPTY-FOR-EMPTY (the CTO's ruling on `FB-j-12`, msg 4753)

`FB-j-12` (complete): the IQLT -69.22 percent is B_01's silver-noncash cap (market value scaled to 22.9 percent of units times price while cost is left
whole), on 64,629 of 492,998 open lots; price and cost are consistent. A data defect the product owner fixes (the CRO's pricing brief; served holdings
values too). The CTO: hold all position slots; `FB-j-7` and `FB-j-4` land the trigger empty-for-empty; the first chain grades act 4b's put; text waits.
`FB-j-7`'s face now has two acts (the slot switch to all six slots, then the dispatcher) and its criterion `nonempty_bullets` 0. No new cell; the chain
count is unchanged. The sample of `FB-j-13` remains the CTO's and Andrew's evidence of the model path, the name guard and the four position slots
BEFORE the cap is fixed; it is not served.

## Amendment 6 (2.0.0_SA_COO~B1, 2026-10-13 ~20:4xZ): cell `FB-j-15` added -- the organization trail records object writes on the three legacy buckets (DEC-12)

Andrew ruled DEC-12 YES (~20:0xZ, the CTO's msg 5128); the laptop CTO's infra-lane ruling (bus 671c3981, dell1 msg 5135) assigns the act to this project because it
serves FWD-6's write instrument, and to a laptop seat because CloudTrail write is a kept deny for the Dell users. Cells are now 15. Independent of the `FB-j-3/-4/-7` chain.

| cell | item | serves | owned files | depends on | slot, class | risk | at the cut |
|---|---|---|---|---|---|---|---|
| `FB-j-15` the trail's third (WriteOnly) selector on bd, inf and cot | 2 | FWD-6 | `infra/aws/terraform/shared-infra/cloudtrail-organization-trail.tf`; ledger entry | -- | `0.7.0_AE_CloudOps~FBL` seat order (crossbox) | WORLD | pending |
