# 2.0.0_SA_COO~C1 -- handoff, ADVI_COTBKF waiting state (written 2026-10-16 ~10:05Z, dell1)

Resume from this file, the ledger and branch `box/dell1` only. Nothing is uncommitted; no worker or worktree is live; origin and local read the same head (a28c3c33be) at writing.

## State (all measured this session)

- **Project:** `ADVI_COTBKF`, `dep_stage` EXECUTING, lease FULL. Rounds 96 to 103 are closed by the CTO (`ledger/ROUND_ANALYSIS.round96-98.md`, `.round99.md` to `.round103.md`). The CTO's last word (msg 6640): no round 104 now.
- **Outcomes:** 5 of 9 REALIZED (FWD-1, 3, 5, 6, 8). FWD-2, FWD-4 and FWD-7 wait on Andrew landing the CRM archive in the store (and, for FWD-7, naming who can read the restricted places). FWD-9 waits on his sending the match packet. No contact with Cottonwood.
- **FWD-3 as graded:** REALIZED on ACCEPT's terms (0 blanks lack a reason); beside it the stated facts: 93.7% of days blank, 98.3% of those UNPRICED (15,973,399 holding-days over 4,371 securities); UNGRADABLE months 78,622, at most 72,184 of them gradable after a full UNPRICED fill (`deliverables/0.9.0_WK_ADVI_COTBKF~193/MONTH_PARTITION_RECORD.json`).
- **Served tables:** the relabelled FWD-3 tables, applied in round 98 (apply commit a593268704), VersionIds `lNzQMjfx6uX2zdFdWKsDANboShtDUz2N` (daily_returns), `ObKZXku7Am.QGjO.oSAsIScy8IcJxN5a` (account_day_value), `nkTE.F82uFSboXr9PEamIENCwFL9cwcC` (month_grades). `deliverables/2.0.0_SA_COO~C1/cu1_ac3_served_unchanged_check.py` reads them unchanged; rollback VersionIds are in the COO half.
- **Bloomberg history:** nothing in the store reaches before 2025-08-28; the CUSIP-keyed store covers 0 and the ticker-keyed stores 1,960 of 15,973,399 unpriced holding-days (row D1-S19). The CTO routed the 4,371-security history pull to `2.0.0_SA_COO~Q1`'s queue, priced first.

## What I owe, and when

1. **When Q1's queue reports covered holding-days that move the fill rate:** cut the rebuild under a never-widen pair (CTO's word, msg 6640). The pair's template is `ledger/NEVER_WIDEN_R97_FWD3_LABELS_COO_HALF.md` and its CTO half; the order template is `task-orders/ADVI_COTBKF.TO-CB-ct-1.fwd3-labels-apply.md`; the regrade command and pins are in `deliverables/0.9.0_WK_ADVI_COTBKF~129/RETURN_CHANGE.md` and the round-97 order `TO-CB-cs-1`. The private sweeps config is at `C:/Users/Test/.opal/commonwealth_sweeps.json` (sha256 `b1d93408f64a996b2a9659bbed9ca0863fbf0d0db348e1397e1a7e184910a89d`, never committed). The dell2 run data is at `.scratch/advi_cotbkf/` (20,563 files, 4,478,568,892 bytes; off git).
2. **Otherwise:** dispatch nothing. Tick with `python .tools/unblock.py tick --serial 2.0.0_SA_COO~C1 --project ADVI_COTBKF --result work --owed-call <id>` (a dated wait on a live owner is not an empty tick); do not count it.
3. **If Andrew acts** (CRM archive landed, or the packet sent): the CTO's next analysis cuts the cells; FWD-4 will need a CRM silver builder, which does not exist in `data/assets/scripts/silver/` (only `cotbkf_crm_match_job.py`).

## Update 16:2xZ: the Bloomberg budget changed the timing of the history pull

Andrew-direct ~15:5xZ (CTO ruling `org/missions/D8/MDPF/MDPF_DEMQUE/ledger/CTO_RULING_BBG_DAILY_BUDGET_2_5M_IMPLEMENTATION_20261016.md` @67b7eee51c): a 2.5M-cell daily Bloomberg budget is the TARGET; the ceiling climbs by measured steps (the standing 11,716, 23,432, 29,290, then 100,000, 300,000, 1,000,000, 2,500,000), each step after one clean drawing day. B's Cottonwood share still waits on the first tranche's resolve rate clearing 50%. The "about 372 days" in the 12Z drive log was the old 5,858-cell ceiling; with the ramp the whole 1,857,629-cell ask could take days to a couple of weeks. Q1 issued DQ-t-73 (the allowance file). The first measurable result is still the tranche's resolve rate (slice T1-01 first), not the whole fill.

## Rule 34 (CLAUDE.md, Andrew-direct 2026-10-16 ~15:4xZ, CTO msg 6814)

CloudOps is seated one lane per macro per box, never one per task. The next CloudOps order for ADVI_COTBKF (the apply of a rebuild under a pair) goes to the ADVI lane `0.7.0_AE_CloudOps~<MACRO><n>` that `0.0.0_AB_MSTR` names, shared with ADVI_FIRMBKTS, not to a fresh lane. `0.7.0_AE_CloudOps~CB1` closes as idle; do not address new orders to it. Ask MSTR~DELL1 for the lane name when the rebuild is cut.

## Lessons to carry (all happened, all recorded)

- A check script and its order must define the same thing: two of mine disagreed (rows D1-S17, the round-103 partition script). Run every issuer script against a matching and an altered record before the cut.
- An order's `<paths>` must name its own file, or the worker cannot flip it (D1-S16).
- The investigation channel holds CRLF lines: append with `open(path, 'ab')`; never read and rewrite it.
- A proof instance's `output_evidence` must equal its `expect` pattern exactly, and an artifact row for a file an earlier commit carried is pinned to that commit's FULL hash.
- A worker's instance lives in its lane's deliverables folder; correcting it needs `GIT_COMMIT_AUTHOR_OVERRIDE` (audited; used twice, say so in the message).
- The comp rail denies `find`, blind recursive grep and a pipe after a census; use native Grep and Glob.

## Loop and watcher

Cron `b6082e41` (`11,41 * * * *`, `/canonical-drive ADVI_COTBKF once`) dies with the session; re-arm only per Andrew's relayed word (MSTR msg 6412, record `org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20261016_024xZ_KEEP_DRIVING_ON_30M_SELF_DRIVE_CANONICAL_DRIVE.md`) after `CronList`. The inbox watcher expires every 30 minutes and is re-armed on the expiry notice.

## Compiler Tools

- Written from the ledger, the round analyses, the drive logs and the broker mail of this session; checked with `git status` and `git log` only; no tool was run to produce this note beyond reading origin and local heads.

## OWED NEXT ROUND (added 2026-10-16 ~17:40Z)

1. **Round 104 (CB-da-1, worker 0.9.0_WK_ADVI_COTBKF~194, branch wk-ADVI_COTBKF-194, worktree C:/dev/wk-cotbkf-194):** the account-match review workbook, desktop only (`Cottonwood_Account_Match_Review_20261016.xlsx`). Amendment 1 (`ledger/CB_DA_1_AMENDMENT_1_20261016.md` @3be9c112f0) sent to the worker: old account value on the last day it held a security; shared-account rows adjacent. On its report: run `cz1_review_sheet_check.py` (AC2 and AC3), check the strengths split, merge the branch with `.tools/safe-merge.sh`, close the round. Report to the CTO: 95 of 107 read weak because the packet's own fingerprint band is under 0.5 for 82 of 107; the strength rule is the issuer's and unchanged unless the CTO or Andrew redefines it.
2. **CTO msg 6923 (FIRMBKTS row S59, `org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md` line 8389):** cut ONE cell in the next round: Cottonwood silver `account_attributes` stopped at 2026-08-20 because the SSM document `opal-cot-silver-run` never runs `--table account_attributes` (writer `data/cot/scripts/silver/cot_silver_merge.py` TABLE_CONFIG; document at the cot-pipeline `ssm.tf` lines 236-251). Close on a silver partition newer than 2026-08-20 (the row expects the next partition to carry 2026-10-13's 1,119 rows). It is a Terraform and live-document change on served data: a never-widen pair (COO half and CTO half) before the apply; apply by the CloudOps lane MSTR names for this macro (rule 34); bare `terraform apply` is forbidden (`safe-apply`).

## ROUND 106 STATE (added 2026-10-16 ~19:00Z)

Round 105 closed MAY-CLOSE, merged @90831503eb. Round 106 issued @5b64371c0c: `TO-CB-dc-1` (WORLD apply of the one-line ssm.tf change) to `0.7.0_AE_CloudOps~FB1` (re-seated by MSTR 18:43:55Z, msg 6974). Pair signed: COO half @7a14b821b4, CTO half SIGNED with C-1 (msg 6968): NO early dispatch; read the organic silver fire about 2026-10-17 midday.

**On the lane's report:** run `dc1_apply_check.py doc` (AC1) and `state` (AC2) in `deliverables/2.0.0_SA_COO~C1/`, then `.tools/safe-merge.sh <its branch>`, then `round-close-check --round 106`.

**The close read (COO and CVO; the CloudOps lane does none of it).** Baseline is already taken (`.scratch/cotbkf_r106/dim_baseline.parquet`, dimension VersionId begins QyyWrPzI, 1,005 rows, 942 with attributes). After the first scheduled silver fire (about 2026-10-17 midday) and the gold run that follows: `python -I deliverables/2.0.0_SA_COO~C1/dc1_fire_read.py fire` (expect silver_partitions about 46, added_filled 62/62, changed_agree 171/171), then `snapshot` after EACH gold build; after the second build `compare` prints the C-1 count (how many of the 122 multi-book accounts change portfolio_group between two consecutive builds). Nonzero, or a consumer appearing first, means the next round cuts an `A_00` cell making the choice deterministic (CTO half). Branch B (the gold build refuses on disagreeing flags) is reported to the CTO; removing a partition is an S3 delete and Andrew's. Record the dated wait with `unblock.py tick --wait-until <UTC> --owner schedule:cot-silver-run`.

## CRM ARCHIVE (added 2026-10-16 ~21:45Z)

Andrew-direct ~21:40Z (`ANDREW_DIRECT_20261016_2140Z_CRM_ARCHIVE_UPLOAD_FROM_LAPTOP.md`, LOCAL @2bc556fe20): the CRM archive is in Downloads on the laptop; the laptop CTO works out the upload. Relayed through `0.0.0_AB_MSTR~DELL1`; waiting for the landed key. CTO msg 7011 confirmed the routing and added (build ladder rung 2): before FWD-4/7 cut a new CRM silver builder, the laptop CTO is asked whether its existing Cottonwood account-to-household mapping (a README plus 11 scripts, revision 2, 76 of 83 accounts HIGH or MEDIUM) is, or contains, that builder; reuse if so; the mapping files stay off git. FWD-7's reader naming stays Andrew's. On the landed key: cut FWD-2/4/7 next round (the reuse answer decides whether FWD-4/7 need a builder cell).

## CRM ARCHIVE -- LAPTOP CTO ANSWERS (added 2026-10-16 ~21:55Z, MSTR msg 7014 relaying laptop msg 109761)

Upload: the key is `s3://opal-data-cottonwood/commonwealth/cottonwood/bronze/crm/date=2026-06-23/CRM_CottonwoodCapitalAdvisors.zip`. Only `cloudops-cot-restricted-breakglass-role` may write it and that role trusts only Andrew's console identity, so no agent can land it: the laptop CTO extracted the zip to the laptop's Downloads (26,485,027 bytes) and is walking Andrew through the one upload; the landed key follows to MSTR or this seat. The live policy keeps all three DenyRestricted statements; the prefix is empty until then.

Reuse: PARTLY. Only `matcher.py`'s `pipe()` table reader and its Crmhouseholds HHID-to-HouseholdID map are reusable. No silver writer, no schema, no X14 field exclusion exist, so FWD-4/7 still need a builder cell that reuses those two pieces (build ladder rung 2). An agent identity cannot read the restricted prefix: a builder that reads the archive needs the round-88 pattern (one named role, one key, a CloudOps grant under a never-widen pair, withdrawn afterwards), and FWD-7's reader naming stays Andrew's.

## OWED NEXT ROUND (added 2026-10-17 ~01:55Z)

1. **CTO msg 7121 (MDPF_CANON PRD v2.25 @8889e98304):** the next ADVI_COTBKF round cuts ONE cell that widens Cottonwood's DataMining account set (or its holdings, allocations and attributes templates) to return the 96 carrier-feed accounts. Close: the 10/15-equivalent supervised total ties to 530,421,988.14. Round 106 is mid-round (spec frozen), so this is the next issuance, not an amendment. Read the PRD section before cutting; a change to what Cottonwood's pipeline serves is a never-widen pair (COO half, CTO half) and a CloudOps lane per rule 34.
2. **CTO msg 7116 / CRO `~DELL1` brief:** if Andrew's read makes `portfolio_group` the unit of the Cottonwood book, the `A_00` cell (one stated rule for a multi-book account's group) is cut BEFORE any page cell. Record `ANDREW_DIRECT_20261017_0145Z_CRO_PORTFOLIO_GROUP_KEY_AND_COTTONWOOD_ADVISOR_INTELLIGENCE.md` @8816c4fe6c.

## WIDEN COLLISION (added 2026-10-17 ~02:00Z, CTO msg 7127, v2.26 @72ef0a649f)
`4.0.0_SA_CRO~DDD` (not this seat) executes the 96-account DataMining widen on Andrew's word (supersedes the round placement in msg 7121; do not cut that cell). Its rule: no Cottonwood silver write before the R106 close read unless this seat agrees in writing. My reply (msgs 7129, 7130): NOT agreed now; I agree after `dc1_fire_read.py fire` and the first `snapshot` if CRO~DDD first sends the write time, partitions touched and whether any of the 122 multi-book accounts gain rows. OWED: post "fire read done" to `4.0.0_SA_CRO~DDD` (CTO copied) when the fire read and first snapshot are taken, and answer its write plan in writing.

## WIDEN WRITE AGREED (added 2026-10-17 ~02:50Z, msgs 7162/7163 answering CRO~DDD 7157/7161)
Agreed in writing to CRO~DDD's silver write (fact_holdings + fact_allocations date=2026-10-16 only, earliest ~15:00Z, after BD posts carrier values) on four conditions: (1) not before my "fire read done"; (2) it sends the overlap count of the ~94-96 new allocation rows against my 122 multi-book accounts first; (3) no silver/account_attributes partition and no A_00 code; (4) it sends the write and gold-chain run times so I `snapshot` after each build. CTO 7159: `dc1_fire_read.py compare` now prints `dropped_between_builds` apart from the flip count (control passes: dropped_same=0, dropped_removed>0). FWD-10 ADVI CTO half signed @6df622c7c5. STILL OWED: "fire read done" to CRO~DDD after ~13:00Z.

## WIDEN RUNS NOW (added 2026-10-17 ~03:25Z, CRO~DDD msg 7197, Andrew-direct "do the run now, we dont need to wait until the morning")
My condition 1 (not before "fire read done") is superseded by Andrew's word; conditions 3 (no account_attributes partition, no A_00 code) and 4 (send me each run time; I `snapshot` after every build) stand. Pre-write state taken 03:2xZ: dimension QyyWrPzI, silver account_attributes 1 partition (2026-08-19), attr_filled 942 of 1,005, multibook 1 in that partition. The "fire read done" post is no longer a gate for CRO~DDD; the round-106 close read after the ~13:00Z fire is unchanged and still mine.
