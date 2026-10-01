# ETFS_RIVALS round 1 closed, round 2 at 8 of 9, the live join stopped partial with its ledger OPEN -- 2.0.0_SA_COO~RV
**archetype:** COORDINATE
**secondary_archetypes:** DEPLOY, VALIDATE
**Date:** 2026-09-30 06:30Z -> 2026-10-01 02:40Z (session-close log for the fabric reboot; first log of lane ~RV)
**Task Order:** ETFS_RIVALS round 1 (TO-RIV-r-1..d-2) and round 2 (TO-RIV-m-1..d-3)
**Status:** IN PROGRESS -- round 2 is 8 of 9 complete; TO-RIV-d-3 is NON-TERMINAL, its deploy ledger `etfs-rivalfunds-round2` is OPEN by design

## Objective
Issue and drain ETFS_RIVALS (D5, fabric site-z) as its one round issuer:
- Round 1 builds the BASG thread live from AWS.
- Round 2 enriches it:
  - the Bloomberg channel;
  - the corporate-actions (G3) enrichment;
  - the IDVZ peer group from Adam's email;
  - the page grouped by Opal fund;
  - the live join (d-3).

## What happened (window)
- **Round 1.** Decomp, issuance and drain of 9 of 9. The BASG thread is live from AWS: drain-end read @4cdb8e59a4, gateway `/rivalfunds` view.
- **IDVZ intake.** Adam's IDVZ list (IDVZ, TXUE, BIDD, CGIC, INEQ, SCHY) was recorded @91229e865f. On Andrew's word the S3 layout stays FLAT, and grouping is done at output time (page v2 groups by Opal fund).
- **Round 2.** Decomp v2.4 @a64a617d08/d28ebc65fc. One issuance of 9 orders @787905d1a3. m-1, u-1, b-1 (amendments 1-2), e-1, g-3, h-1, g-4, p-2 all drained and complete.
- **Andrew-direct**, recorded @51c4cc36e8: "do not modify the existing daily etfs pull for Positioning"; "Anything we do for this would have to be additive". This is binding on d-3, and the Positioning pull and vehicle are unchanged at CLOUD.
- **Home funds.** Andrew "1b" (PRD v0.5) makes IDVZ and PFOE `home_producer`: never in the Bloomberg request, never in RIVALS silver (CTO ruling (b), msg 27404).
- **d-3 never-widen pair.**
  - The COO half was re-signed @d6f7c6956d with key 4's MEASURED served delta (`round2/key4_served_delta.py` + `.json`): BASG G1 11272=11272, only `gold_version` differs; G5 837=837, every class 0, only 3 label cells differ.
  - The CTO half was re-signed (AMENDMENT 1 @350df49995, msg 27432) with one condition, bound as d-3 amendment 3 @256aad63aa: re-run key 4 with the imported G3 before G5 writes. The worker ran it and it PASSED identically (`key4_with_g3.json`).
- **MSTR~Z HOLD 27462/27463** (stale-worktree applies). I answered as a recorded decision: d-3 applies only `etfs-rivalfunds`, whose inputs are byte-identical at CLOUD HEAD, and its plan read 0 destroy.
- **d-3 worker** (0.9.0_WK_ETFS_RIVALS~5) was wound down on Andrew's reboot word and drained @e12fefdbff. Worktree `/c/tmp/wk-rivals2-5` and branch removed. The act is PARTIAL; see Current State.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| `.tools/to-pipeline-gate.py` | round-2 issuance + amendments | PASS after fixes (verdict literal inline, cell-id grammar, comp-adversary RUN) |
| `.tools/safe-merge.sh` | every drain incl. e12fefdbff | PASS (row gate clean on merged index) |
| `.tools/surprise-row-gate.py` | rows S2, W*-S* | PASS after one surfaced_at format refusal |
| `.tools/safe-commit.sh` + commit-gate | all commits | PASS (ruff F841 fixed once) |
| comp-rail hook | raw grep in Bash | DENIED twice; routed to Grep tool / `# rail-checked` |

**What worked:** the row gate and the to-pipeline gate each caught a real defect before landing. The serializing dry run turned a CTO refusal into a measured delta in one pass.
**What failed:** an append-only union resolver that reserialized rows broke on formatting. It was replaced by a byte-preserving append (scratch `union_rows.py`).
**Gap found:** a LOCAL sink cannot rehearse an IAM-denied delete: local unlink always succeeds. That is how row W5-S24 escaped the rehearsal.

## Blockers
- **ETFS_RIVALS-Z-W5-S24 BLOCKING/ARMED, disarm_owner 2.0.0_SA_COO~RV.**
  - `silver_bloomberg` deletes superseded silver objects, and the silver Lambda role has no `s3:DeleteObject` (key 7).
  - So a batch that re-claims a carried (fund, report date) writes its silver but NO batch marker, and gold never chains.
  - It hit import batches 04 and 05. Gold for them was driven by explicit replay events.
  - Evidence: silver request ids `0d1b3347-abb0-4f31-bd87-f9cf11b77875`, `e5169551-345a-49c9-972c-653ce7d6f430` (TSEL 2025-08-15).
  - It must be disarmed before the daily leg is enabled. The choice: grant `DeleteObject` on the Bloomberg silver prefix (a never-widen key-7 widening needing both halves), OR change the silver cell to supersede without deleting (a new cell).

## Current State (for a reader with zero context)
- **Repo.** CLOUD @e12fefdbff, LOCAL; origin CLOUD read 85159f8d1c via ls-remote at 02:39Z, so the drain is not pushed. All round-2 code is merged. TO-RIV-d-3 `<status>` is unflipped (non-terminal).
- **Ledger.** `org/critical_paths/.open_deploys/etfs-rivalfunds-round2.json` is OPEN.
  - Completion doc: `org/critical_paths/change_management/20261001T0043Z_etfs-rivalfunds-round2_deploy_completion.md`.
  - L1 and L2 are closed with proof; L3-L6 are open.
- **d-3 per key** (worker report; S3 counts re-read by me at ~02:35Z):

  | key | state |
  |---|---|
  | 1 | Bloomberg bronze 1552 objects (776 raw + 776 sidecars of 937 captures), batches 00-06 |
  | 2 | Bloomberg silver 2829 objects; batches 04 and 05 have no marker (S24) |
  | 3 | G0 13 rows (both homes `home_producer`); G3 4823 rows; G2 120 objects, daily window only; G6 419 objects |
  | 4 | NEW revisions only: G1 745, G5 743, page 12, IDVZ group through 2026-06-03 |
  | 6-8 | Lambdas, policies and rules LANDED: 6 add / 9 change / 0 destroy, code pin 96ba9a72ab |
  | 9 | Vehicle enabling line NOT applied: `integrations/bloomberg/pipeline/scheduled_daily_pull.cmd` equals the pre-act HEAD, so the leg stays gated OFF. The literal line is in `d3_live.json` `vehicle_enable_line` |
  | 10 | No Bloomberg requests. The Terminal read `bloomberg_health` ok=false at 20:08 ET; no sign-in attempted |

- **Checks.** d-3.AC1 FAIL (776 < 900 raws). AC2 FAIL: G2 replay not run, and the new-day counts are partial vs census. AC3 FAIL: enable line not recorded. All three are expected FAILs of an unfinished act, not defects.
- **Evidence.** `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~5/`: `d3_live.json` (remaining steps, request ids, prefix counts), `d3_act.py` (the resumable act driver), `key4_with_g3.json`, the proof-of-spec instance, `evidence/`.
- **Rows filed this round** by the d-3 worker (INERT unless noted), in `surprise-channel/investigations/INVESTIGATION_v1.Z.md`:
  - S18: 937 captures, not 944.
  - S19: two stale tests now fail under `home_producer`: `test_g01_universe.py::test_default_map_shape`, `test_g12_canonical_multi_source.py::test_home_producer_policy_is_counted_unread_and_pending_is_not_read`.
  - S20.
  - S21: `land_capture` is quadratic on S3.
  - S22: the leg's exit codes are 90-97, not 80.
  - S23.
  - S24 BLOCKING.
- **Self-disclosure.** I removed the d-3 worktree with `--force`, which deleted its untracked `.scratch/` (batch drivers `run_chunks2.py` etc., plan files). Nothing load-bearing was lost: the committed `d3_act.py chunk 7|8 --sink s3` is the resume path named in `d3_live.json`.

## Next Steps
1. [2.0.0_SA_COO next ETFS_RIVALS seat] Push CLOUD (or confirm the integrator push) and re-read ls-remote.
2. [2.0.0_SA_COO] Disarm W5-S24 first: choose a DeleteObject grant (re-sign both never-widen halves for key 7 with [1.0.0_SA_CTO~Z]) or a silver supersede-without-delete amendment.
3. [2.0.0_SA_COO -> fresh worker on d-3] From a worktree at CLOUD HEAD, resume per `d3_live.json` `remaining`:
   - import batches 07 and 08 (`d3_act.py chunk 7` / `chunk 8 --sink s3`), then gold by marker or replay;
   - the G2 full-history replay, then republish the page;
   - apply the one enabling line, re-run b-1.AC3 and d-3.AC1-AC3, close ledger L3-L6, and flip d-3 complete.
4. [2.0.0_SA_COO] Fix the two S19 stale tests in an issuer amendment (outside d-3's paths).
5. [Andrew] The Bloomberg Terminal sign-in is needed before the first 08:03 ET rivalfunds leg can fetch. While the line is not applied the leg is OFF and the Positioning legs are unaffected.
6. [2.0.0_SA_COO -> 1.0.0_SA_CTO~Z] Send the L10 slug only after d-3 is terminal. Carry these rows to the analysis:
   - W1-S8..S16;
   - W2-S3/S5;
   - W3-S6..S14;
   - W5-S17..S24;
   - S2 (gateway deploy lock).
   Round 3 carries G4, G7-G13, the G9 recurrence gate (PRD v0.6) and the home-producer reader.

## MCP traffic (significant only)
- **Received:** CTO~Z msgs 27404 (ruling b), 27419 (key-4 refusal), 27427 (PRD v0.6 landed, acked), 27432 (CTO half re-signed with condition, acked), 27463 (MSTR hold, acked).
- **Sent:** to CTO~Z, the key-4 remedy ask and the 27463 decision reply.
