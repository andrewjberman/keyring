# IRPT_BCKEND~M -- Holdings with the snapshot model overlay -- status (FROZEN for hand-back)

Seat `2.0.0_SA_COO~M`. Frozen 2026-09-28 ~17:5xZ under act 3 of
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_PLACEMENT_20260928_174xZ_RELAUNCH_CANONICAL_DRIVE_PMY_CLOSER_D.md`
(CTO msg 102386), per return brief section 3 A2
(`org/tier1_exec/4.0.0_SA_CRO/deliverables/IRPT_CLOSER_TO_CANONICAL_RETURN_BRIEF_20260924.md`).
Lease IRPT_BCKEND~M: FULL since 17:47Z (`drive-mode.py read`). The `/loop 20m` goal row is struck; the goal record
`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260923_224xZ_COO_M_GOAL_HOLDINGS_SNAPSHOT_MODEL_OVERLAY_LOOP_20M.md`
stays the done-criteria. Round 19 of the ~M workstream is cut from the next-list below. The pre-freeze long-form
status is this file's previous git version.

Claim column: `measured` = read at this freeze (17:4xZ-17:5xZ); `held` = cited from a receipt, not re-read.

## Pins

| What | Value | Claim |
|---|---|---|
| CLOUD (local) / origin/CLOUD | 229b3fd184 / d9e59dd372 (ls-remote read 17:4xZ) | measured |
| R4 Holdings code on CLOUD (cash rule + UIC-16) | bcf7a6adde (was dfb62b349d pre-purge); ancestor of origin/CLOUD | measured |
| R4 diff re-run / N1 ledger close | 565dd0abf5 / 26127abf10 (both on origin/CLOUD) | measured |
| Purge commit map | `org/tier0_exec/0.0.0_AB_MSTR/deliverables/S19_PURGE_COMMIT_MAP_20260928.txt` | measured |
| Served Holdings revisions | COT fc199c8e, INF ba9001d5, 49F 9ab377ce; rollback COT dec293d6, INF d32e50c6, 49F 5a25ae76 | held (receipts @7e57abcabd) |

Branches (all clean, no uncommitted work at the freeze; worktrees re-synced by MSTR 102372):

| Branch | Head | Worktree | Content |
|---|---|---|---|
| irpt-m-r4-holdings | 1379536ce3 | ../ajb_irpt_m_r4 | R4 + UIC-16; its content is on CLOUD @bcf7a6adde |
| irpt-m-cot-cash-line-act | 596453d184 | -- | the signed COT cash-line act (was 0deac23f1e) |
| irpt-m-s152-cloud | a94749d9d1 | ../ajb_irpt_m_s152c | S155 COT mix_views cash/other (was ff63895521) |
| irpt-m-cot-b1 / irpt-m-cot-cash-line | 0da4449e1f | ../ajb_irpt_m_cashline | B1 structured/commodities (was ccb9b38dd8) |
| irpt-m-comparison-consumer | dbe20f8022 | ../ajb_irpt_m_cmp | ~P's release carries it |
| irpt-m-b01b-skip | 89280b9d45 | -- | COT B_01b skip list + rule-2 prompt |
| irpt-m-s152 / irpt-m-s125-20260924 / irpt-m-s125-publish | 1c70dce6d4 / a7e5c59042 / 2e4c33738e | -- | superseded by the rows above; history only |

## Deployed artifact -> source commit, per served function

| Function | Deployed artifact | Source | Claim |
|---|---|---|---|
| `irpt-holdings-refresh-lambda` (Holdings dispatch; schedule DISABLED) | CodeSha256 SGwrvwLH8fhriLW03s/oXMPE1Whjhix8pwKJYHhWKwI=, LastModified 2026-09-26T19:13:41Z | 145c5e6494 (QA mode, `{"qa": true}` -> holdings_qa) | measured (sha); source held (ledger irpt-holdings-dispatch-qa-m-20260926) |
| Holdings packages `irpt_holdings_{49f,inf,cot}` at `s3://opal-data-<firm>/irpt/<firm>/code/gold/investor-reporting-holdings.tar.gz` | ETag 14d59119..., members-sha256 83f6a81aab34..., 40 members, 2026-09-25 18:1xZ | minted from CLOUD 4f58a95c84; does NOT carry bcf7a6adde (cash rule, UIC-16) | measured |
| `investor-reporting.tar.gz` at `s3://opal-data-mdpf/code/scripts/assets_gold/investor_reporting/` (directory chain) | ETag 4155283a, VersionId ceQmSBti..., 2026-09-26 18:00Z | holdings_snapshot.py blob = b9bae5f429's; directory_runner.py blob = de4e176cc3's; CLOUD HEAD differs on both (cash rule, UIC-16), skipped on the purge push (102369) | measured |
| `irpt-directory-refresh` | CodeSha256 DXuzx9jp..., LastModified 2026-09-24T20:59:50Z | refresh.py = a7e5c59042's (on CLOUD fecbf0dc43) | measured (sha); source held (ledger irpt-directory-refresh-s125-m-20260924) |
| COT gold C_06 / D_03 / D_04 | `comp-pipescript deployed --firm cot`: MATCH x3 | CLOUD; C_06 last change 7fd8149448 (S138 cash line) | measured |
| COT gold B_01b | STALE (S3 serves the no-op; auto-deploy disarmed, S141) | irpt-m-b01b-skip not merged | measured |

## Open ledger entries (~M)

All three are HELD with apply legs proven and only R1 open. COT's first scheduled gold run since the writes landed
today: `platinum/firm/mix_summary.json` LastModified 2026-09-28 11:36:20Z (measured). R1 is readable now.
- `cot-other-admission-m-20260925` R1: `other` passes through C_06's mix (value 0 today).
- `cot-cash-admission-m-20260925` R1: z09308463 cash slice, shares sum to 1; z09326138 or z09308511 100% cash.
- `bd-securities-cot-new-p1-m-20260926` R1: COT and BD classify the 941 Part 1 keys as written.
- Caveat: IRPT_BCKEND-S173 (ARMED) says the COT gold host cannot read bd-securities, so the R1 legs that depend on
  the table are expected to fail on served output. That is a prediction, not a read.

## Next-list, priority order (round 19 cells)

1. **R1 read-backs** on today's 11:36Z COT run for the three HELD ledgers (runbook A.1 + A.2). A fail is dispositioned
   by the rollback in its own entry or by S173's re-point, never by a merge.
2. **R4 D.0: re-mint the three Holdings packages** from CLOUD @bcf7a6adde under a new ledger. members-sha256 must
   change from 83f6a81aab34. Nothing scheduled runs them (dispatch schedule DISABLED).
3. **R4 D.2: one QA fire**, `aws lambda invoke --function-name irpt-holdings-refresh-lambda --payload '{"qa": true}'`,
   then read holdings_qa.
4. **R4 D.3: the ENABLE half.** Re-run the pinned diff (`account_mask_publication_diff.py dry --pin-served`) and the
   INF name census at the QA as_of; fill `IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_R4_ENABLE_DRAFT.md` (ETF Part A 16 keys incl.
   VNQ; own-mask labels; the cash rule; UIC-16 labels) and ADD the `investor-reporting.tar.gz` re-mint as a leg, since
   it moves served directory code. Send to 1.0.0_SA_CTO and 4.0.0_SA_CRO (the CRO's 18:00Z latest is missed; the CRO was
   told at 14:09Z it follows the reboot).
5. **Goal /verify** criterion (3) after the first enabled publication (COT `CASH -- CASH` reads `cash`); then disarm
   ~P's S152 (INF holdings as-of at or after 09-25).
6. **S173 re-point** (COT gold, BD gold, Holdings -> DDB etf-classifications) as ONE act with halves (CTO 102323).
   Gate: the POSN owner's etf-classifications fill. Coverage @9ab15461ca: COT 39.7%, BD 68.1%.
7. **COT cash-line act** (runbook B: irpt-m-cot-cash-line-act + irpt-m-s152-cloud, one ledger). Gate: item 1 passes
   and S173.
8. **COT-new Part 2** (26 `other` keys, runbook C). Gate: item 1, and d08/d06 admit `other` (~X's B1 commits).
9. **B1 drain**: irpt-m-cot-b1 + `ds-x-b1-cashline` + comp-constants 9135feae97 under B1's ledger; drop ~X's duplicate
   S150-S153 rows at that merge.
10. **ETF B2** (13 keys). Gate: B1 landed, ~D's C34 served, re-census at 0 RAISE / 0 drop.
11. **COT B_01b deploy** (irpt-m-b01b-skip). Gate: COT's chain adds B_01b; merge + safe-deploy as one ledgered act.
12. **6 stale COT D_03 composition files** (COT_SERVED_COMPOSITION_BASELINE_20260927.json): re-read after item 1; a
    delete needs Andrew's confirmation.

## Andrew acts in flight

- None pending at Andrew for ~M's acts.
- Conditional, not yet asked: the COT B_01b OpenAI run (per-use word); the 6-file delete (item 12).
- With the CTO for Andrew: the Schwab registration-code list for UIC-16 at 49F.

## Parked (owner, un-park condition)

| Item | Owner | Un-parks when |
|---|---|---|
| Law-lock budget refuses a CLOUD merge into a seat branch (canonical-flow and dispatch SKILL.md over 25,600 bytes) | 1.0.0_SA_CTO | the files shrink or the gate exempts it |
| NOT_READY vs NOT_FOUND for a selected account with no custody row (`_authz/errors.py:58`) | 1.0.0_SA_CTO | the CTO rules |
| `directory/tests` on CLOUD: 6 failures predating the refresh port | 2.0.0_SA_COO~P | the next change to directory/entry.py |
| d08 (runners_cot, QA emit) refuses its byte-schema once mix_summary carries `cash`; S151 same shape | runners_cot owner via 1.0.0_SA_CTO | an owner is seated or d08 blocks a served act |
| UIC-15 (name beside ticker) | 2.0.0_SA_COO~M | rides R4's INF name fill; re-measure at the enabled publication |
| UIC-16 at 49F | 2.0.0_SA_COO~M | the Schwab registration-code list arrives |
| IRPT_BCKEND-S124: the bundle mint reads working-tree bytes | owner of .tools/safe_deploy_core.py | next re-mint (item 2: mint from a clean tree) |
| Comparison consumer re-pinned @dbe20f8022 | 2.0.0_SA_COO~P | ~P's next release with its GRANT halves |

## Goal criteria (record: goal file above)

| Criterion | State | Evidence |
|---|---|---|
| (1) signed-in journey 49F / INF / COT | MET | ~D HARs w8 + w9 (09-27) |
| (2) every active 49F/INF account resolvable or refused explicitly | MET on the current directories | census @f247a922a5 |
| (3) COT soundness, window disclosed | BROKEN@SEMANTIC: COT `CASH -- CASH` served as equity | re-verify after next-list item 4's enabled publication |

Surprise channel: `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md`.
Runbook: `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/MONDAY_20260928_RUNBOOK.md`.
