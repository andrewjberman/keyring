# MDPF_DEMQUE -- surprise channel, INVESTIGATION v1 (round 1)

Append-only. Worker rows `MDPF_DEMQUE-W<n>-S<k>`; seat rows `MDPF_DEMQUE-S<k>`.

```json
[
  {
    "id": "MDPF_DEMQUE-S1",
    "project": "MDPF_DEMQUE",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~Q1",
    "surfaced_at": "2026-10-08T23:23:39Z",
    "one_line": "The Andrew ~23:0xZ record that places the Rival Funds Bloomberg price asks in this queue is cited as on CLOUD @0573ceb0c3, but neither the record nor its commit @86d85ab4a5 is readable on dell1 after a fetch.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "0.0.0_AB_MSTR~DELL1 msgs 1232 and 1235: record org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_230xZ_SITEZ_AND_DELL2_OPEN_CALLS_ANSWERED.md @86d85ab4a5, 'reaches CLOUD via the laptop's integrate (CLOUD 0573ceb0c3)'",
        "2026-10-08T23:23:39Z: git fetch origin CLOUD -> origin/CLOUD = 0573ceb0c3; git cat-file -t 86d85ab4a5 -> 'Not a valid object name'; git ls-tree -r --name-only origin/CLOUD has no path matching 230xZ_SITEZ (positive control: the same ls-tree lists the MDPF_DEMQUE project.json)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "msg 1235: the record is an input to the first MDPF_DEMQUE decomposition and reaches dell1 with the next box-sync at CLOUD 0573ceb0c3.",
    "world_is": "CLOUD is at 0573ceb0c3 on origin and carries neither the record nor @86d85ab4a5. Round 1 is FWD-1 only, so the cut does not depend on it; the round-2 cut (tier 3, Rival Funds on Bloomberg) reads it first. Likely still on a box branch awaiting the laptop's next integrate."
  },
  {
    "id": "MDPF_DEMQUE-D1-W3-S1",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~3",
    "surfaced_at": "2026-10-08T23:37:57Z",
    "one_line": "The order's face names Cottonwood's live bucket and three keys as literals, but the commit-time naming gate (ENFORCE) refuses a new literal of them in data/mdpf, so land_cot.py derives them instead of typing them.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "safe-commit of data/mdpf/scripts/demque/land_cot.py + test_demque_land.py (first attempt, base 6dc65d8cba): 'NAMING REFUSE land_cot.py:22 opal-data-cot -> opal-data-cottonwood' and 'NAMING REFUSE :23/:24 silver/transactions/, silver/historical_prices.parquet -> {source}/{scope}/silver/...' (NEW and OUT-OF-PATTERN as S3Key), naming-gate DENOMINATOR 2 path(s); a second attempt then refused the path component 'cot' -> lookup('cottonwood')",
        "lib/opal_naming.lookup('cottonwood') at 6dc65d8cba: bucket opal-data-cottonwood, but alias opal-data-cot carries planes ['bucket'], routed True, lookup False: the live data sits in the routed legacy bucket, which is what the consumer reads",
        "Landed at 9ca032bff5: BUCKET = the single routed bucket alias from lookup('cottonwood'); the three keys are read out of the consumer's own source (build_canonical_prices_v2.py, tree from lookup pipeline_trees), a miss is a loud SystemExit; both checks still pass (LAND-OK; LSEAM-OK ... join_key=cusip)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The order's THE CELL text states the bucket, the two Tier-2 keys and the transactions prefix as plain addresses to read and write.",
    "world_is": "The gate refuses a hand-typed form of each (Rule 30, R20), and the legacy layout has no address() form. Derivation from the consumer's source is the workaround used: it ties the lander to what the price build reads, but breaks if the consumer's key expressions are rewritten to non-literal forms. If the lander is migrated to the LGIC layout (R19) the keys change with it. Owner of that call: 2.0.0_SA_COO~Q1 / 1.0.0_SA_CTO."
  },
  {
    "id": "MDPF_DEMQUE-D1-W4-S1",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~4",
    "surfaced_at": "2026-10-08T23:45:30Z",
    "one_line": "The cell premise that Cottonwood's gold run goes through gold_dispatch.sh (silver-prep S_00 only on --chain full) is false: the scheduled opal-cot-gold-run SSM document runs a fixed script list with no S_00 and never calls gold_dispatch.sh.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "2026-10-08T23:37Z: aws ssm get-document --name opal-cot-gold-run -> runCommand list A_00..D_04, no S_00, no gold_dispatch.sh; infra/aws/terraform/cot-pipeline/ssm.tf:375-404 (grep S_00 = 0 hits)",
        "144 gold-run logs under s3://opal-data-cot/logs/cot-exporter/gold-run/ synced: 0 lines 'BUILD CANONICAL PRICES', 0 '=== S_00'; positive control: the same logs carry '=== A_00' 125 times",
        "trace: org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~4/FWD1_HOP6_PRICES_TO_PAGE_TRACE.md Q1, Q2"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Worker face DQ-t-5: gold_dispatch.sh:1069-1071 runs S_00 only when invoked --chain full, and Q1 asks which gold_dispatch.sh arguments the Cottonwood schedule passes.",
    "world_is": "No Cottonwood schedule passes any gold_dispatch.sh arguments; the only gold_dispatch.sh run ever logged on Cottonwood is a manual partial chain on 2026-06-26. Adding S_00 to hop 6 means editing the opal-cot-gold-run SSM document in Terraform, not choosing a dispatch flag."
  },
  {
    "id": "MDPF_DEMQUE-D1-W4-S2",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~4",
    "surfaced_at": "2026-10-08T23:45:31Z",
    "one_line": "Cottonwood's live nightly run does not read canonical_prices.parquet on any page-feeding path: B_00 builds canonical holdings from BD-reported market value in silver/holdings and returns before load_canonical_prices(), and A_03's canonical_prices read is skipped.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/cot/scripts/gold/B_00.canonical_holdings.py:1095-1099 returns after _build_canonical_from_snapshot; load_canonical_prices() is at :1124",
        "s3://opal-data-cot/logs/cot-exporter/gold-run/cot-gold-run-20261008-113337.log: 'Holdings snapshot present (85 date(s)) -- canonical holdings from silver/holdings (BD-reported MV ...)' and A_03 'No unrealized data ... skipping buy injection' (silver/unrealized/unrealized_gain_loss.parquet is 404 live)",
        "portal/src has 0 hits for canonical_prices"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Decomp hop 6 and the DQ-t-5 cell: a new Yahoo row in silver/historical_prices.parquet reaches a Cottonwood client's page through canonical_prices.parquet.",
    "world_is": "Even with S_00 scheduled and the Tier-2 objects landed, no Cottonwood page value changes: pages are fed from gold/canonical/holdings built from silver/holdings market_value. Hop 6 needs a consumer decision (which holdings are Yahoo-priced), not only a schedule."
  },
  {
    "id": "MDPF_DEMQUE-D1-W7-S1",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~7",
    "surfaced_at": "2026-10-09T01:23:44Z",
    "one_line": "build_canonical_prices_v2.py accepts only --dry-run (no --upload; it always writes), so the S_00 ssm.tf step cannot pass \"$UPLOAD_FLAG\" ('--upload' would exit 2 on argparse); the step passes --dry-run under DRY_RUN and no flag otherwise.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/cot/scripts/gold/build_canonical_prices_v2.py main(): add_argument('--dry-run') is the only argument; Step 6 uploads unconditionally",
        "infra/aws/terraform/cot-pipeline/ssm.tf run_gold: UPLOAD_FLAG='--upload' (or '--dry-run' when DRY_RUN=true)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Worker face DQ-t-8 item 3: the S_00 line is run_gold S_00 build_canonical_prices_v2.py \"$UPLOAD_FLAG\" optional, if the script honours that form.",
    "world_is": "The script does not honour --upload; the step uses an inline conditional emitting --dry-run only when DRY_RUN=true (still matches AC2's regex). Issuer to confirm at apply."
  },
  {
    "id": "MDPF_DEMQUE-D1-W7-S2",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~7",
    "surfaced_at": "2026-10-09T01:29:04Z",
    "one_line": "Naming gate refuses the unchanged original literal silver/historical_prices.parquet at build_canonical_prices_v2.py:318 and the test's same literal; no compliant form exists without splitting, so the order is BLOCKED.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "safe-commit.sh on the repair: [naming-gate] NAMING REFUSE data/cot/scripts/gold/build_canonical_prices_v2.py:318 silver/historical_prices.parquet -> {source}/{scope}/silver/historical_prices.parquet; why: EXISTING and OUT-OF-PATTERN as S3Key in a surface remediations.json assigns to the live remediation ADVI_FIRMBKTS: REFUSE unless the diff removes it",
        "safe-commit.sh on the repair: [naming-gate] NAMING REFUSE data/cot/scripts/gold/test_s00_missing_tier2.py:46 silver/historical_prices.parquet; why: NEW and OUT-OF-PATTERN as S3Key: REFUSE",
        "line 318 is in load_historical_prices(), byte-identical to base 9c66868b3a (diff shows no change there); the file now touched trips the gate on a pre-existing literal"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Issuer ruling: restore both loaders byte-identical to base and handle the absent key at a _load_tier2() call site, commit passes the naming gate.",
    "world_is": "Edits are complete in the worktree (uncommitted): both checks pass (S00-OK, SCHED-OK), proof VALID rc=0. The commit is refused by the naming gate for the original literal (a line not changed) and the test's literal. Not re-split. Needs an issuer decision (gate exemption for the existing literal, or an ADVI_FIRMBKTS-conformant key for the test)."
  },
  {
    "id": "MDPF_DEMQUE-D1-S1",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~Q1",
    "surfaced_at": "2026-10-09T02:45:00Z",
    "one_line": "The lock rule locks a mapping as `measured` on any min(3, available) agreeing trade dates with no agreement-rate floor: PONPX (72201M719) locks at 51 of 83 dates agreeing (61%).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/lock.py check() @8abd95ad3b (DQ-t-1, per dell2 research s.1): LOCKED when >= min(3, available) dates pass and one falls in the earliest third",
        "QA re-lock 2026-10-09T02:4xZ with the per-security lock range: 131649774 CVMIX 255/255 LOCKED, 316066752 FSSZX 85/85 LOCKED, 72201M719 PONPX 51/83 LOCKED measured",
        "scheduled draw 2026-10-09T02:30:01Z (.git/demque-daily-draw.log): 32 LOCKED, 17 REJECTED, of which 15 had passed >= 98% of their dates and were rejected only by the request-wide lock range (fixed in daily_draw.py)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD C-IDENTITY: a client security's mapping is LOCKED, per date range, only when its prices agree with the client's own trade prices.",
    "world_is": "The rule as built accepts a 61% agreement as measured. A pass-rate floor (e.g. >= 90% of checked dates, by asset type) is a round-3 pilot-readout candidate; the rule is DQ-t-1's spec (dell2 research s.1) and is not changed mid-round."
  },
  {
    "id": "MDPF_DEMQUE-D1-W9-S1",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~9",
    "surfaced_at": "2026-10-09T03:40:00Z",
    "one_line": "DQ4-t10-AC1 cannot pass as written: bbg_quote.quote() does not expose the reserve claim, so the fourth named test must be xfail, and the AC1 checker requires every named test PASSED.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/bbg_quote.py quote(): the result keys are request_id, page, breakdown, cells, finish_date, allowance_gap; _figure() reads only value and claim-absent, and no claim is carried out (printed result for a held reserve: {'request_id': 'r1', 'cells': {'bloomberg_bql': 5}, 'finish_date': '2026-10-05', 'allowance_gap': None})",
        "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R2_CHECKS/_pytest_dir.py run(): a required test counts only when its pytest -v line contains PASSED; an XFAIL line does not",
        "2026-10-09T03:39Z dq_t10_tests.py: RESERVE-BAD not-passed=test_quote_finish_date_carries_held_when_reserve_is_held; three tests PASSED, the fourth XFAIL (strict, reason cites this row); dq_t10_seam.py: RSEAM-OK bql.reserve=1875"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Worker face DQ-t-10 item 5: the fourth test asserts quote() exposes the held claim; if it does not, file a row and mark the test xfail, never editing bbg_quote.py. AC1 expects RESERVE-OK.",
    "world_is": "quote() does not expose the claim, so the xfail branch applies and AC1 prints RESERVE-BAD for that one test. Needs an issuer decision: add the claim to quote()'s result (a bbg_quote.py edit in another order, after which the strict xfail flips to a pass and its marker comes off), or amend AC1 to accept an XFAIL citing this row."
  },
  {
    "id": "MDPF_DEMQUE-D1-S2",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~Q1",
    "surfaced_at": "2026-10-09T04:38:00Z",
    "one_line": "The Yahoo-backfill split ruling says DEMQUE builds no price writer and SECHIST is the one writer of stored series, but DEMQUE's price store is already live (32 securities) and is the file contract dell2's ADVI_COTBKF reads; SECHIST has no Yahoo writer yet.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_YAHOO_BACKFILL_OWNER_DEMQUE_VS_SECHIST_20261009.md (msg 1707): 'DEMQUE builds no price writer'; SECHIST owns the stored series; 'a second writer of the same rows would be a shadow pipeline'",
        "data/mdpf/scripts/demque/price_store.py (DQ-t-6, @8abd95ad3b) cut under the CTO's msg 1337 ruling (consumer (a)) and PRICE_STORE_CONTRACT.md; dell2 C2's AMLP consumer read @14d4fc7049 reads it",
        "s3://opal-data-assets/yahoo/global/silver/price_history/: objects present (cusip=00141B204/* LastModified 2026-10-09T02:38Z); index 32 rows after the 02:30Z fire",
        "comp-find '(?i)yfinance|yahoo' over org/missions/D8/MDPF/MDPF_SECHIST + data/mdpf/scripts, 2026-10-09 ~04:3xZ: 116 files scanned; every Yahoo-writing file is under data/mdpf/scripts/demque/; SECHIST holds only DOC mentions"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "msg 1707: a backfill run executes through SECHIST's Yahoo writer, which reads DEMQUE's ticker map; DEMQUE builds no price writer.",
    "world_is": "The only Yahoo price writer that exists is DEMQUE's price_store, live with 32 securities and a dell2 consumer; the next scheduled draw (02:30Z) would add up to 150 more. Not two writers today (SECHIST has none), but the ruling's end state needs a port: SECHIST's writer takes over the same rows and the consumer re-points, same-window rollback, never run side by side."
  },
  {
    "id": "MDPF_DEMQUE-Z-W1-S1",
    "one_line": "Budget mode backfill is shared by BQL holdings and ETF history; market-range and amgt-model-block also combine request shapes.",
    "spec_asserts": "TO-DQ-t14 asks for rows times a per-mode cells table and a channel per mode.",
    "world_is": "etf_daily_pull.py records backfill with etf_history_backfill_* batch ids and two RET fields; collector_bloomberg.py records backfill holdings with 16 returned columns. A mode-only multiplier misprices the latest 2929 history rows as 46864 rather than 5858 cells. Candidate 492cb5a2f1 uses the recorded batch identity for these two known cases and retains absent cells/channel for unresolvable mixed modes. No producer changed.",
    "project": "MDPF_DEMQUE",
    "fabric": "site-z",
    "surfaced_by": "0.7.0_AE_CloudOps~ZQ",
    "surfaced_at": "2026-10-09T08:06:45Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "integrations/bloomberg/pipeline/etf_daily_pull.py:472,609",
        "data/etfs/scripts/rivalfunds/collector_bloomberg.py:630",
        "data/etfs/scripts/rivalfunds/enrichment_bloomberg.py:835-862",
        "integrations/bloomberg/research/model_block_pull.py:2201-2224",
        "bbg_budget_2026-10-08.jsonl: backfill rows=2929 batch_id=etf_history_backfill_2026-10-07"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-Z-W1-S2",
    "one_line": "OPAL_BBGTML notebook draws have no budget record calls in the scheduled runner or its two notebook sources.",
    "spec_asserts": "TO-DQ-t14 step 5 requires reporting notebook record coverage as a held gap; editing the notebooks is outside this order.",
    "world_is": "The live OPAL_BBGTML_daily_pull task runs scheduled_daily_pull.cmd, which executes tplus1/tools/run_daily_pull.py. That runner executes market_indices_data_pull.ipynb and model_portfolio_regression_analysis.ipynb. A text search of all three sources finds no bbg_budget or .record( calls. Their notebook draw coverage is held, not measured complete. No notebook was run or edited.",
    "project": "MDPF_DEMQUE",
    "fabric": "site-z",
    "surfaced_by": "0.7.0_AE_CloudOps~ZQ",
    "surfaced_at": "2026-10-09T08:06:45Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Get-ScheduledTask OPAL_BBGTML_daily_pull: enabled daily 07:00 local Eastern Standard Time",
        "integrations/bloomberg/pipeline/scheduled_daily_pull.cmd RUNNER",
        "integrations/bloomberg/pipeline/tplus1/tools/run_daily_pull.py:235-238",
        "rg bbg_budget|\\.record\\( over tplus1/tools/run_daily_pull.py and both tplus1/src/*.ipynb: zero matches"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-Z-W1-S3",
    "project": "MDPF_DEMQUE",
    "fabric": "site-z",
    "surfaced_by": "0.7.0_AE_CloudOps~ZQ",
    "surfaced_at": "2026-10-09T09:39:47Z",
    "one_line": "DQ-t-18 requires an unmetered sentinel row while preserving uneditable tests that assert exact row counts without it.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "TO-DQ-t18 @73cae9cfe6 Build 2: day without bbgtml lines gets one bbgtml-unmetered row; Build 3: keep t14 tests passing; paths omit t14 tests",
        "data/mdpf/scripts/demque/test_demque_bbg_ledger_upload.py:47 exact cells list; :63 exact four rows; :99 exact two lines",
        "Memory-only sentinel probe with original five tests: 3 failed, 2 passed, exit 1; deciding failures extra None, 5 != 4, 3 != 2; S3 stubbed",
        "Unmodified baseline afterward: five passed, UPL-OK, exit 0",
        "org/tier2_senior/0.7.0_AE_CloudOps/deliverables/MDPF_DEMQUE_ZQ_T18_REFUSAL.md"
      ]
    },
    "spec_asserts": "TO-DQ-t18 requires both the added sentinel row and unchanged t14 tests passing; existing test file is outside write grant.",
    "world_is": "The fixtures have no bbgtml lines, so the mandatory row contradicts three exact cardinality assertions. No production file changed. Issuer must amend the test grant/expectations or the sentinel interface before implementation; order remains pending under its refusal clause."
  },
  {
    "id": "MDPF_DEMQUE-D1-W13-S1",
    "one_line": "The history reserve (40 cells) is the static producer names only; the ledger's one day draws 5858 history cells, so the quoted allowance per day is the ceiling less a reserve well under the real production draw.",
    "spec_asserts": "TO-DQ-t15 step 2: history.reserve = the tier-1 producers' daily history legs read as text (names x fields x rows per name), margin stated, gaps named.",
    "world_is": "Only etf_daily_pull.py states its history names in code: (FUNDS 4 + EXTRA_SECURITIES 2) x RET 2 fields + FUNDS 4 x FUND_D 5 fields, one top-up row each = 32 cells, x1.25 = 40. The run-time universe constituents (derive_universe reads S3), the depth backfill (BACKFILL_CAP 50), price_axis_pull (covered universe) and enrichment_bloomberg are named gaps, so they are not in the 40. The served ledger's largest history day (dt=2026-10-08) is 5858 cells, which includes those legs. The history ceiling is that same 5858 floor, so the history allowance per day (ceiling - reserve = 5818) treats the reserve as 40 although production drew far more that day; the finish days quoted from it (history 2026-10-13, model_block 2026-10-13) are HELD and may be early by that margin. Nothing was guessed; a measured production draw on the ledger (separating tier-1 from demand rows) would replace the reserve.",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~13",
    "surfaced_at": "2026-10-09T09:34:00Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/reserve_estimate.py --print: history producers {etf_daily_pull: 32}, value 40, 8 gaps named",
        "integrations/bloomberg/pipeline/etf_daily_pull.py:46,52,397,472,473",
        "demand_ledger dt=2026-10-08 history cells 5858 (s3://opal-data-assets/bloomberg/global/bronze/demand_ledger/dt=2026-10-08/ledger.jsonl)"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-S3",
    "one_line": "Yahoo's dividend list misses some cash Bloomberg's total return carries (LNVGY, DIVZ, IDVZ), and Yahoo shows money-market funds at a 0 total return where Bloomberg accrues interest daily.",
    "spec_asserts": "PRD ADDENDUM v0.5 / C-PRICES: every stored Yahoo row carries the as-traded price, the dividend/interest cash on its ex-date and a total-return value; the TR column is built by the method DQ-t-17 fixes.",
    "world_is": "DQ-t-17 (TR_COMPARISON.md @0aa91a7a96): on 36 comparable ex-dates Yahoo cash matches Bloomberg to 0.075 bp, but Bloomberg's TR carries payments Yahoo does not list -- LNVGY 2025-12-11 (85.8 bp), DIVZ 2026-09-29 (12.5 bp), IDVZ 2026-09-29 (21.8 bp) -- and FXFXX/SALXX accrue about 1 bp a day (3-4 bp over a weekend) in Bloomberg while Yahoo shows a $1.00 close and no dividend (TR 0). A Yahoo-only TR column would understate those names; interest-accruing funds need Bloomberg or an explicit accrual.",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~Q1",
    "surfaced_at": "2026-10-09T09:41:06Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~15/TR_COMPARISON.md",
        "org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~15/TR_COMPARISON.json",
        "dq_t17_run.py re-run at dell1 base @0aa91a7a96: TRCMP-OK 3 names"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W17-S1",
    "one_line": "With the history reserve seeded from the ledger (7322), the history allowance per day is not positive: the ceiling is the same 5858 floor the reserve is measured from.",
    "spec_asserts": "TO-DQ-t20 / CTO round-5 R1: the history reserve is the ledger's measured daily draw plus a margin, and if the allowance (ceiling - reserve) cannot hold it the quote says so.",
    "world_is": "history.ceiling = 5858 (largest ledger day dt=2026-10-08, a held floor); history.reserve = round(5858 x 1.25) = 7322. Allowance per day = 5858 - 7322 = -1464. bbg_quote.py --quote DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS.json now returns finish_date null and allowance_gap 'history allowance per day not positive (ceiling 5858, reserve 7322)' for 15720 history cells. The ceiling is a floor, not a capacity; a reserve measured from the same day can never leave room under it. A history ceiling above the measured draw (vendor meter or a refusal-bounded figure) is needed before any backfill is scheduled.",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~17",
    "surfaced_at": "2026-10-09T12:53:00Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/bbg_allowance.json history.ceiling/reserve",
        "bbg_quote.py --quote DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS.json output"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-S4",
    "one_line": "quote_vs_actual.py --all raises KeyError 'finish_date' on a frozen quote file of an older shape (MDPF_SECHIST-CARD-A-COT-BBG-HISTORY.quote.json), so the all-requests read stops at the first such file.",
    "spec_asserts": "TO-DQ-t19 build item 1: --all prints one line per frozen quote; a missing quote file is a ValueError, never a default.",
    "world_is": "requests/ holds 4 .quote.json files; the SECHIST card's quote (filed by 2.0.0_SA_COO~H1 before round 6) has no finish_date key. read() indexes quote['finish_date'] and --all crashes there. --request on the three round-5 quotes works (FWD4-OK ON_TIME at base @112f2f2b12). Remedy for the repair batch: a quote without finish_date reads verdict UNQUOTED with the gap named, never a crash and never a default date.",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~Q1",
    "surfaced_at": "2026-10-09T13:04:34Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python data/mdpf/scripts/demque/quote_vs_actual.py --all at dell1 base @112f2f2b12: KeyError 'finish_date' (line 24)",
        "org/missions/D8/MDPF/MDPF_DEMQUE/requests/MDPF_SECHIST-CARD-A-COT-BBG-HISTORY.quote.json"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W18-S1",
    "one_line": "DQ-t-21 appends four columns to prices.parquet as ordered, which fails the existing test_demque_store.py::test_only_the_locked_range_is_written (asserts exactly the three old columns); that file is outside the order's write grant.",
    "spec_asserts": "TO-DQ-t21 step 2: prices.parquet gains cash, total_return, tr_source, flags AFTER the existing columns; and 'keep the existing test_demque_*.py passing'.",
    "world_is": "data/mdpf/scripts/demque/test_demque_store.py line 32 asserts list(px.columns) == ['date','close_served','as_traded_close']; with the four columns appended it fails (1 failed, 76 passed across the demque test directory). Both instructions cannot hold. The new columns were built as ordered; the one-line fix to that assertion (compare the first three columns) belongs to the issuer, the file not being in <paths>. Also: daily_draw.py (not in <paths>) must pass bbg= to price_store.write for guard (a) to fire in the scheduled draw, and money_market.csv carries empty cusip cells (no CUSIP in the order).",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~18",
    "surfaced_at": "2026-10-09T12:55:30Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/test_demque_store.py:32",
        "data/mdpf/scripts/demque/price_store.py",
        "pytest -q data/mdpf/scripts/demque -> 1 failed, 76 passed"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W19-S1",
    "one_line": "DQ-t-22 as written (history always walks non-trading days) fails the existing test_demque_bbg.py::test_allowance_known_gives_finish_date_above_the_reserve; the quote applies the new rule only when the history ceiling is measured and the reserve is not.",
    "spec_asserts": "TO-DQ-t22 step 2: for channel history the finish date walks calendar days adding the ceiling on each non-trading day; and 'keep every existing test_demque_*.py passing'.",
    "world_is": "test_demque_bbg.py::test_allowance_known_gives_finish_date_above_the_reserve quotes history with ceiling 15 / reserve 5, both claim measured, and expects the weekday rule (finish 2026-10-09; 'not positive' gap at ceiling 5 reserve 5); an unconditional non-trading rule gave 2026-10-11 (1 failed, 85 passed). That file is outside <paths>. Worker choice, not in the order: bbg_quote.py applies the non-trading-day rule when history ceiling claim is measured AND history reserve claim is not measured (the real file: ceiling measured, reserve held), else the old weekday rule. Full suite 86 passed. The model_block history component still uses the weekday rule (the order names channel history only). The issuer may prefer to amend that older test and drop the reserve condition.",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~19",
    "surfaced_at": "2026-10-09T13:36:00Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/test_demque_bbg.py:77-88",
        "data/mdpf/scripts/demque/bbg_quote.py history branch of quote()",
        "pytest -q data/mdpf/scripts/demque -> 86 passed"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W19-S2",
    "one_line": "The worktree's org/standards/PROOF_OF_SPEC.schema.json is the broken e7c10e5b4b version, so proof-of-spec-check.py returns rc=2 here; validated against the 6b65ca5a52 schema content with the worktree file restored after.",
    "spec_asserts": "TO-DQ-t22 proof_of_spec: validate with python .tools/proof-of-spec-check.py <instance> DQ7-t22-AC1,DQ7-t22-AC2 before the flip; only the exit code is the verdict.",
    "world_is": "This worktree (branched before 6b65ca5a52 landed on box/dell1) carries schema e7c10e5b4b whose commit_or_etag type is an invalid jsonschema type: the worktree's own checker exits rc=2 (UnknownType), and the base checker run on the worktree instance exits rc=1 CHECKER-SCOPE. The schema is outside <paths>. Worker act: wrote git show 6b65ca5a52:org/standards/PROOF_OF_SPEC.schema.json over the worktree file, ran the worktree checker (VALID rc=0), then restored the original bytes (git status clean on that path). The schema file is not in any commit of this branch.",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~19",
    "surfaced_at": "2026-10-09T13:42:00Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/standards/PROOF_OF_SPEC.schema.json at e7c10e5b4b vs 6b65ca5a52",
        "proof-of-spec-check rc=2 UnknownType in the worktree before the temporary swap"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-S5",
    "one_line": "bbg_quote.py's non-trading-day rule (DQ-t-22) quotes every history request as a backfill, so a TIER-1 production history request gets allowance_today 0 on a trading day.",
    "spec_asserts": "C-RESERVE: production pulls (tier 1) never draw against the backfill allowance; they draw against the reserve. CTO round-6 R1 governs a history BACKFILL.",
    "world_is": "MDPF_SECHIST-SHT8-TR-FIELD-CONFIRM-20261009 (tier 1, 1 history cell, SALXX TOT_RETURN_INDEX_GROSS_DVDS) quotes allowance_today 0 and finish_date 2026-10-10 on 2026-10-09. Here the delay is harmless (needed before Monday 11:00Z), but a tier-1 history request on a weekday would be held a day for no reason. Remedy for the next round: the non-trading-day walk applies to tier >= 2 requests; tier 1 draws against the reserve on any day.",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~Q1",
    "surfaced_at": "2026-10-09T14:30:31Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python data/mdpf/scripts/demque/bbg_quote.py --quote requests/MDPF_SECHIST-SHT8-TR-FIELD-CONFIRM-20261009.json --today 2026-10-09 at @4c6a16ded6: allowance_today 0, finish_date 2026-10-10",
        "prd/MDPF_DEMQUE_PRD.md C-RESERVE"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-Z-W1-S4",
    "one_line": "TO-DQ-t24 requires vendor-warning stop and a named stop outcome through bbg_quote --record, but historical_data drops fieldExceptions and the recorder always emits DRAWN; dependency files outside write grant.",
    "spec_asserts": "TO-DQ-t24 build1: stop on the first vendor limit warning/refusal, recording the stop; append ONE actuals line with bbg_quote.py --record, outcome DRAWN or the stop named.",
    "world_is": "After local NTDQ-OK, offline stub session against real blp_client.historical_data with on_response_error=raise returns one data row and drops supplied fieldExceptions; responseError positive control raises. Real record_actual to temporary ledger emits DRAWN for zero cells and rejects outcome keyword; CLI --help has no outcome argument. Neither blp_client.py nor bbg_quote.py is granted. No real draw/task/auth/actuals act. Issuer amendment requested for opt-in diagnostics and stop-aware recording, or approved adapter/interface.",
    "project": "MDPF_DEMQUE",
    "fabric": "site-z",
    "surfaced_by": "0.7.0_AE_CloudOps~ZQ",
    "surfaced_at": "2026-10-09T14:49:55Z",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier2_senior/0.7.0_AE_CloudOps/deliverables/MDPF_DEMQUE_ZQ_T24_REVIEW.md",
        "integrations/bloomberg/mcp/blp_client.py historical_data handle: responseError opt-in; fieldExceptions not read",
        "data/mdpf/scripts/demque/bbg_quote.py record_actual and CLI outcome interface",
        "python .scratch/t24-interface-probe.py: rc0; lost field exception, positive responseError control, DRAWN zero, unsupported outcome keyword"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-S6",
    "one_line": "The live DQ-t-14 uploader writes ETF-history ledger rows with cells null / claim absent since SECHIST's SH-t-4: it reads etf_daily_pull.py's RET by ast.literal_eval, and RET is now list(HISTORY_FIELDS), not a literal.",
    "spec_asserts": "TO-DQ-t14 / FWD-2: the demand ledger carries each producer's drawn cells with a claim; the ETF history backfill converts rows x RET fields (2) to cells.",
    "world_is": "bbg_ledger_upload.py line 33 maps etf_history_backfill to (etf_daily_pull.py, 'RET') and line 50 evaluates the assignment with ast.literal_eval; etf_daily_pull.py now declares HISTORY_FIELDS = ['PX_LAST', 'DAY_TO_DAY_TOT_RETURN_GROSS_DVDS'] (line 67) and RET = list(HISTORY_FIELDS), so the read returns no literal and the row is written cells null, claim absent (reported by 1.0.0_SA_CTO~Z msg 32871, relayed in 0.0.0_AB_MSTR~DELL1 msg 2857). Honest (absent, never invented) but the ledger under-measures ETF history daily, and ceiling_from_ledger skips null rows. Remedy for the next round: resolve a Name-to-literal assignment (RET -> HISTORY_FIELDS) before literal_eval, with a test on the current producer source.",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~Q1",
    "surfaced_at": "2026-10-09T16:55:51Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/bbg_ledger_upload.py:33,50",
        "integrations/bloomberg/pipeline/etf_daily_pull.py:67 (HISTORY_FIELDS)",
        "1.0.0_SA_CTO~Z msg 32871 via 0.0.0_AB_MSTR~DELL1 msg 2857"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-S7",
    "one_line": "land_cot.py cannot read its consumer's key literals since ADVI_COTBKF moved them onto legacy_addresses, so test_demque_land.py raises SystemExit at collection and aborts the whole demque pytest run.",
    "spec_asserts": "DQ-t-4 / land_cot.py header: the lander's three keys are read out of build_canonical_prices_v2.py's own source; an extraction that finds nothing is a loud error, never a default.",
    "world_is": "build_canonical_prices_v2.py line 170 now reads {'bucket': S3_BUCKET, 'key': _legacy_key('silver-historical-prices')} (ADVI_COTBKF CB-av-1 @9cfa6f9584, CB-ax-1 @19b3550e8a, 2026-10-09), so land_cot.py's _consumer_literal(r\"Key='([^']*historical_prices[^']*)'\") matches nothing and raises at import. `pytest data/mdpf/scripts/demque` at origin/CLOUD dcb15f35bb ends in INTERNALERROR with no test run; with test_demque_land.py ignored, 89 passed, 1 failed (the D1-S6 uploader test). The lander fails closed (no write), so the hazard is inert; no served path imports it today.",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~Q1",
    "surfaced_at": "2026-10-11T03:58:00Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/land_cot.py:25-36 (_consumer_literal, SystemExit)",
        "data/cot/scripts/gold/build_canonical_prices_v2.py:170 (_legacy_key)",
        "pytest data/mdpf/scripts/demque at origin/CLOUD dcb15f35bb, 2026-10-11T03:5xZ"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-S8",
    "one_line": "32 of 141 served price files still carry the original 3 columns after the first served total-return write; all 32 are the symbols whose last Yahoo attempt is 2026-10-09, before that write.",
    "spec_asserts": "DQ-t-21 / C-PRICES: price_store.write serves the four new columns (cash, total_return, tr_source, flags) after the original three for every written name.",
    "world_is": "served_tr_read.py at origin/CLOUD dcb15f35bb, index written 2026-10-11T02:34:22Z: 109 prices.parquet carry the 7 columns, 32 carry the original 3, 0 other. The 32 symbols equal, by set intersection, the 32 pacer.json entries with last_attempt 2026-10-09 (outcome OK, http 200); the 147 attempted on 2026-10-10 carry 7 columns. Not read: whether the pacer's incremental window ever re-draws those 32, so whether they stay 3-column is open.",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~Q1",
    "surfaced_at": "2026-10-11T03:58:00Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R7_CHECKS/served_tr_read.py output: 109 / 32 / 0",
        "~/.opal/demque/pacer.json symbols[*].last_attempt (device-local, dell1), join in the real-run record",
        "data/mdpf/scripts/demque/price_store.py write path"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W23-S1",
    "one_line": "DQ-t-29 D1-S7 (land_cot.py) cannot be committed as the face specifies: the naming gate refuses the two registry row keys passed to legacy_address(), because legacy_address is not a permitted call context.",
    "spec_asserts": "Worker face DQ-t-29 section 2: HIST_KEY and TX_PREFIX are read through lib/opal_naming legacy_address(key) on the rows cottonwood-silver-historical-prices and cottonwood-silver-transactions-prefix, and the repaired land_cot.py is committed.",
    "world_is": ".tools/naming-gate.py@698312232c (lines 22-24) permits a firm token only inside the arguments of key(), address(), name() or lookup(); legacy_address() is not listed. Committing the repaired land_cot.py (safe-commit, before 2026-10-11T05:19:28Z) printed 'NAMING-GATE: REFUSE 3 graded' for data/mdpf/scripts/demque/land_cot.py:71 and :72 (cottonwood-silver-historical-prices, cottonwood-silver-transactions-prefix, NEW hand-kept carrier) and a WARN at :46. Nothing was committed for the lander half; the D1-S6 half committed alone at 27e8ae878a. lib/opal_naming.lookup('cottonwood') returns no legacy key rows, so no permitted builder route reads a legacy row by key. The alternative of composing the key from the firm token was not taken: it routes around the gate.",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~23",
    "surfaced_at": "2026-10-11T05:19:28Z",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".tools/naming-gate.py@698312232c lines 22-24 (CONTEXT RULE) and 1994-2026 (hand-kept carrier REFUSE)",
        "lib/opal_naming.py@698312232c line 1941 (legacy_address, not a key/address/name/lookup builder)",
        "infra/logic/registry/legacy_addresses.json@698312232c rows cottonwood-silver-historical-prices and cottonwood-silver-transactions-prefix",
        "data/mdpf/scripts/demque/land_cot.py lines 71-72 in the worktree (uncommitted): the two literal row keys"
      ]
    }
  }
]
```
