# IRPT_BCKEND~M -- Holdings with the snapshot model overlay -- status (FROZEN for hand-back)

Seat `2.0.0_SA_COO~M`. Round 19 closed 2026-09-29 ~00:2xZ; frozen 2026-09-28 ~17:5xZ under act 3 of
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

## Round 19 result (closed 2026-09-29 ~00:2xZ)

- TO-IB-m19-1 (R1 read-backs, drained @a765ef4dc5): cot-other-admission PASS, ledger CLOSED; cot-cash-admission FAIL
  (z09308463 / z09308511 cash served as fixed_income FCASH; row W41-S1) and bd-securities-cot-new-p1 FAIL (COT: S173;
  BD: C_06's incremental watermark never reprocesses a sealed date; row W41-S2) -- both ledgers stay HELD.
- TO-IB-m19-2 (R4, drained @6ceb8c3e5a): packages re-minted (members-sha256 94f2e3433d9e, 41 members, closure
  +lib/silver_ids.py); two firm-principal read-version grants signed and APPLIED (ledgers
  irpt-holdings-principals-versionread-m-20260928 and -ownread-m-20260928 CLOSED); 49F build peak cut in code
  (c81280bd75, OOM-SINGLE on the t3.medium, output identical); QA fire SUCCESS at all three firms (49F f61bb631,
  INF 58cbeda0, COT 3f2dca9e, business_date 2026-09-25); ENABLE half SENT @8d601db072 (CTO 102498, CRO 102499).
- Rows this round: W41-S1/S2 (CTO), W42-S1/S2 resolved by the grants, W42-S3 (pytest lib.silver_ids shadowing,
  pre-existing at CLOUD, INERT), W42-S4 (proof-instance filename key, INERT).

## Next-list, priority order (round 20 cells)

1. **R4 enable**, on both signatures of @8d601db072: flip `irpt-holdings-snapshot` to ENABLED through safe-apply under
   its own ledger; read the first scheduled publication.
2. **Goal /verify** criterion 3 on that publication (COT `CASH -- CASH` reads `cash`); then disarm ~P's S152 (INF
   holdings as-of at or after 09-25).
3. **AD-01/02 Holdings shape** (CTO 102475): per account, L0 CATEGORY nodes Models / SMAs / Client, each with its own
   amount, plus the L-1 account total; COT's Rebalancer-strategy wrapper removed. Served-shape change under its own half;
   pin to 2.0.0_SA_COO~D (102469 amended).
4. **UIC-14** (CTO 102443): the Holdings builder writes each snapshot's source vendor keys into its output.
5. **Directory bundle** investor-reporting.tar.gz: CLOUD's members moved (cash rule, UIC-16, 49F memory cut); MSTR asked
   to skip it at push; its re-mint goes with ~P's next directory package or under its own half.
6. **S173 re-point** (COT gold, BD gold, Holdings -> DDB etf-classifications) as ONE act with halves (CTO 102323).
   Gate: the POSN owner's fill. Also carries W41-S1 (COT cash-admission) and W41-S2's COT half.
7. **BD C_06 sealed-date reprocess** (W41-S2's BD half): the P1 write never reaches BD's historical mix; needs a
   re-run or a ruling. Owner of BD gold via 1.0.0_SA_CTO.
8. COT cash-line act; COT-new Part 2; B1 drain; ETF B2; COT B_01b deploy; 6 stale D_03 files -- unchanged gates as in
   the round-19 list (S173, ~X B1, ~D C34, COT's chain adds B_01b, Andrew's confirmation).
10. **UIC-16 at 49F** (CTO 102567): load the Schwab acct_type (9) and acct_regis (34 of 35) code table from Andrew's
    source https://docs.bridgeft.com/docs/source-account-and-registration-types (read by the CTO 2026-09-29 ~04:1xZ) as
    DATA with its URL and read date on the file; 49F labels carry the full names; RI401 (1 account) and blank (2) print
    as unrecognised, never guessed. Same file family as IB-mr-202/203 (holdings_snapshot.py / directory_runner.py):
    cut after round 20 drains.
11. **S165 / S166** (CTO round-19 analysis @d797a87872 s.3): issue two orders to 0.6.2_AE_PartnerETL~S -- (a) commit the
    RUNNING cot login script (28dd27a0, 35,049 B) under infra/aws/ec2/bd-cot-auto-login/ as the build input, no
    behaviour change; (b) port the retry-capable script (BD_MAX_LOGIN_ATTEMPTS / BD_LOGIN_BACKOFF_MS) under a deploy
    ledger, the diff read by this seat before it lands. Round 21 (GATE (x): round 20 ~M is issued).
12. **W42-S3** (same analysis): the lib.silver_ids sys.path collision (a test inserting .tools/ ahead of the repo
    root) -- fixed by the issuer at the chain-B drain of round 20.
    RULE from round 20 (analysis s.2): an order that changes a served figure names EVERY reader of that figure in its
    criteria, each with its own check, and proves on the served page. S187: worker slot n = 1 + max(n) over every
    0.9.0_WK_IRPT_BCKEND~n author line at HEAD, printed in the issuance commit.
9. Standing: answer 0.4.0_DS_ClientPlatform~E's source-read questions (PRD v0.19, CTO 102487).

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
