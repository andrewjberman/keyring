# 1.0.0_SA_CTO (Claude) session log -- IRPT MVP completion, 2026-09-24 00:05Z-01:55Z

Continues logs/2026-09-23/claude_takeover_IRPT_2243-0005Z.md. Files over mail: RULINGS.md batches
11-13, CONTROL.md, DIRECT_REVIEW_2020_20260923/*.json under
org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/.

## Commits this window (all LOCAL; origin/CLOUD 69e36619ae by ls-remote at 01:3xZ)
- 69e36619ae  Andrew-direct "all recs approved" (seven cards) + two Y test rows (batch 11) -- PUSHED by MSTR.
- dda3b7ab42  Anna Holdings NOT_READY root cause + remedy routing + sink repackage GO (batch 12).
- 88fc8b8c7d  49F/INF publication GOs, ORIGINAL_HOLDINGS accepted, fence rows acknowledged, one Y test row (batch 13).
Peer commits consumed: 4.0.0_SA_CRO 8b4c15c6ba (exemptions.json, three irpt-holdings-role rows);
2.0.0_SA_COO~M 58ee5b36dd (ORIGINAL_HOLDINGS family row, M worktree); 2.0.0_SA_COO~P 9b6e6fa98e
(resident.tf + instance state, plan 04c77cbe), bc7281c50b (sink package, publish branch);
2.0.0_SA_COO~Y 7fec957269 (prospect_dates v2 binding).

## The Anna NOT_READY thread (Andrew's 00:53Z retest: Unavailable / No source age yet / NOT_READY)
Eliminated with evidence (record HOLDINGS_NOT_READY_ROOT_CAUSE_20260924.json): as_of, the deployed
reader path on the live publication, the selection store, the role's identity policy, the portal's
parse of a success body, encryption, the "No source age yet" text.
ROOT CAUSE: opal-data-cottonwood's DenyForeignFirmPrincipals denies every ARN not like role/*-cot-* and
not one of three exempted users; irpt-holdings-role matches neither. Discriminator: simulate-
principal-policy WITH the live bucket policy -> explicitDeny (ResourcePolicy); WITHOUT -> allowed. Every
offline replay ran as an exempted user (a replay certifies code and data, never the runtime principal).
Same fence on opal-data-49financial and opal-data-inflection.
REMEDY (registry-driven, three buckets): CRO rows LANDED 8b4c15c6ba -> P plans shared-infra from a tree
containing it (expected 0 add / 3 change / 0 destroy; ledger before the act; decoded diff to CTO + CRO)
-> CTO half + CRO half -> P safe-applies, readback x3, re-plan 0/0/0 -> CTO re-simulates expecting
allowed -> Andrew retests. Andrew told via MSTR (cross-firm-guard enumeration edit; veto possible).
Sink repackage (served.py 3ac9cbdc98, code-only) GO'd; P's BEFORE: artifact tndS2IuX / xd4mk5fx, one
member differs, plan 06880e79 0/1/0.

## Other rulings this window
- GO A 49F 7c0e7ce3 (160 writes) and GO B INF 1ebc7696 (35 writes) after CTO recount on the prepared
  bytes: sha256 == revision, gold sha == summary, _platinum_plan -> 156 / 31 parts, receipts 8 + 8,
  targets empty (404 + 0 keys, cottonwood index as positive control). Finding: superseded revisions sit
  beside the GO'd ones in the prepared dirs; the publish call names the bytes explicitly.
- ORIGINAL_HOLDINGS family row accepted (table original_holdings, extension csv; xlsx suffix = enrichment
  per Y's measurement); policy_sha256 cb9c4e6e -> 7a7ed8f6; P re-pins the X10 matrix (39 destinations).
- Resident cutover plan 04c77cbe GO (99936): decoded plan read (1 create / 1 update / 16 no-op); ONE
  apply; CTO half by message, Y's 99916 review the second; D1 sign-in once through the canonical
  wrapper; --once acceptance stops before any live provider calculation.
- Y test row ops/tests/test_prospect_dates.py -> IRPT_Y_ACCESS_INTEGRATION_P at 7fec957269.
- Y's second half for 04c77cbe STANDS (99938); bound (c) confirmed as Y read it: the first 12.03 job's
  YCharts calls run under the standing host-workflow authorization (CRO 6fc3f5f785 item 3), not CALL-3.
- Andrew-direct via MSTR 99940 (~01:4xZ, "recs approved" on MSTR's cards): NO VETO on the
  irpt-holdings-role fence exemption; CurrencyAuthorities.json (P 815dbc5507 bytes) whole-file added to
  CLOUD; ONE TRUNK (SITEZ retired) with a shared-tree MERGE WINDOW to come; portal DEV pushed c1ac41ec.

- GO A / GO B EXECUTED by M (99947, receipts @90c0bca189 in the M worktree): 49F 7c0e7ce3 index
  EvNOT_ocng2dG0yqDqpXUDFBCPO1ovwK 01:46:02Z; INF 1ebc7696 index J_FeUeEAd0jRBCN0lgMoixLY_m3o9QHM
  01:48:29Z. CTO readback 01:5xZ (own instrument): head-object returns exactly those VersionIds;
  list-objects-v2 under irpt/49financial/ = 160 objects (158 platinum date + 1 gold + 1 index) and
  under irpt/inflection/ = 35 (33 + 1 + 1), untruncated. All three firms now hold an accepted Holdings
  publication behind a CAS index; the function reads none of them until the fence apply.

## Open at the CTO (event-driven; inbox Monitor bmdrltu96, script pid 15308, armed 01:33Z)
1. P's shared-infra plan + ledger + decoded diff -> sign the CTO half; CRO signs; apply; re-simulate.
2. P's sink AFTER receipt (CodeSha == xd4mk5fx...).
3. DONE: M's GO A / GO B receipts (above).
4. P's re-pinned X10 matrix -> ACTIVE review (retention arms are the CTO's); then CALL-3 one-use plan.
5. P's cutover receipt (enrolled_user_id measured, HostCapture pins) -> Y's 12.03 runbook.
6. CurrencyAuthorities.json route to CLOUD (P drain vs whole-file add) -- Andrew stopped MSTR's add;
   still parked. Eclipse scheduled-pull change still needs its own card.
7. Instruments corrected this window: none new; the replay-under-exempted-user face was appended to the
   box-memory simulate-principal-policy entry.
