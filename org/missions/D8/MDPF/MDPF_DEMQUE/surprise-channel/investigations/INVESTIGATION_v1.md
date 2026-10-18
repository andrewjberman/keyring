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
    "id": "MDPF_DEMQUE-D1-W22-S1",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~22",
    "surfaced_at": "2026-10-11T05:17:53Z",
    "one_line": "All 32 stale price files end on 2026-06-23, so a redraw request built from each file's own date window (the DQ-t-28 build) ends 2026-06-23, not at the current frontier.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/redraw_stale.py --list on the worktree at base ba3ee9bd48 (S3 read, 2026-10-11 ~05Z): total 141, stale 32; every stale row end 2026-06-23; start 2013-04-08 for 31 rows and 2015-10-28 for 1",
        "org/missions/D8/MDPF/MDPF_DEMQUE/task-orders/MDPF_DEMQUE.TO-DQ-t28.redraw-stale-price-files.md build steps 1 and 3: a stale row's start and end are the file's own date min and max; the request end is the latest of the rows' windows",
        "data/mdpf/scripts/demque/daily_draw.py@ba3ee9bd48 _windows and on_result: the request start and end are passed to lock.check as the lock range"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "the 32 files are re-drawn so the price tables carry seven columns; the redraw request's window is each stale file's own date min and max (TO DQ-t-28 build steps 1 and 3).",
    "world_is": "the 32 stale files end 2026-06-23 (their last draw's window), so the built request ends there and the draw's lock range would follow it. Whether the 32 then reach the current frontier is not settled. Not read: the end dates of the 109 seven-column files and the lock.json valid_to of the 32. The issuer should read this before running --apply."
  },
  {
    "id": "MDPF_DEMQUE-D1-W22-S2",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~22",
    "surfaced_at": "2026-10-11T05:17:53Z",
    "one_line": "demand_queue.upload_ledger derives its repo root four dirname levels up from the file, which lands on data/, not the repo root, so its lib.opal_naming import holds only under the PYTHONPATH that run_daily_draw.sh exports.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/demand_queue.py@ba3ee9bd48 upload_ledger: root = four os.path.dirname calls on abspath(__file__), then sys.path insert and 'from lib.opal_naming import address'",
        "python read on the worktree: four dirname calls on demand_queue.__file__ print C:\\dev\\wk-demque-22\\data; lib/opal_naming.py exists at C:\\dev\\wk-demque-22\\lib",
        "data/mdpf/scripts/demque/run_daily_draw.sh@ba3ee9bd48 line 13: export PYTHONPATH=$ROOT"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "demand_queue.upload_ledger resolves the builder address through lib.opal_naming from the repo root found by its own path.",
    "world_is": "the four-level path lands on data/, so the import holds only under the PYTHONPATH set by the daily draw script. redraw_stale.py takes the repo root four levels up from its own folder and inserts it itself. Not read: whether any scheduled task calls upload_ledger without that PYTHONPATH."
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
  },
  {
    "id": "MDPF_DEMQUE-D1-W21-S1",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~21",
    "surfaced_at": "2026-10-11T05:17:01Z",
    "one_line": "The demque folder run (pytest data/mdpf/scripts/demque with test_demque_land.py ignored, as the order names) has one failure outside this order's paths: test_demque_bbg_ledger_upload.py::test_reads_record_lines_and_converts_rows_to_cells_per_mode returns cells None for the fourth row where 14 is expected.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO-DQ-t25 Tests paragraph: every other test_demque_*.py must keep passing unedited; a failure outside this order's paths is a surprise row and is not edited.",
    "world_is": "At base ba3ee9bd48 plus this order's uncommitted diff (bbg_quote.py, test_demque_bbg.py, new test_demque_tier_quote.py): 93 passed, 1 failed. The failing test imports bbg_ledger_upload only; that module does not reference bbg_quote and is unchanged in this worktree. The None where 14 is expected reads like the Name-to-literal case row MDPF_DEMQUE-D1-S6 names for bbg_ledger_upload.py; that link is NOT verified here.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "timeout 400 python -m pytest data/mdpf/scripts/demque --ignore data/mdpf/scripts/demque/test_demque_land.py -q: 1 failed, 93 passed; assertion [48, 64, 5, None, 2] == [48, 64, 5, 14, 2] at test_demque_bbg_ledger_upload.py:49",
        "grep of data/mdpf/scripts/demque for bbg_quote: bbg_ledger_upload.py makes no reference to it",
        "git status in C:/dev/wk-demque-21: only bbg_quote.py, test_demque_bbg.py and test_demque_tier_quote.py changed; bbg_ledger_upload.py not touched"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W21-S2",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~21",
    "surfaced_at": "2026-10-11T05:17:01Z",
    "one_line": "TO-DQ-t25 names the tier-1 reserve claim as held or measured and the tier as an int 1-5, but states no rule for an inferred reserve claim or an int tier outside 1-5; the build carries an inferred reserve as its claim and reads any int other than 1 as a backfill.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO-DQ-t25 cell text: tier-1 room is the history reserve figure (claim held or measured); tier 2 or above, or no tier, is a backfill.",
    "world_is": "bbg_quote.py at this worktree quotes a tier-1 request whose reserve claim is inferred as a reserve figure, with finish_date_claim inferred (run: .scratch/edge_arms.py, uncommitted, t1_reserve_inferred). A tier that is an int other than 1 (for example 0 or 6) reads as a backfill by _is_tier1; those values were not run. The three named tests do not pin either arm.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/bbg_quote.py _is_tier1 and _history_tier1 at this worktree (uncommitted diff over ba3ee9bd48)",
        ".scratch/edge_arms.py run: t1_reserve_inferred finish_date 2026-10-12, allowance_today 125, finish_date_claim inferred"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W21-S3",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~21",
    "surfaced_at": "2026-10-11T05:26:28Z",
    "one_line": "TO-DQ-t26 does not place two details of refreeze.py: the re-frozen quote also carries allowance_gap, and the collision counter follows the date (<id>.quote.superseded-<date>-2.json).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO-DQ-t26 build item 3: <id>.quote.json carries request_id, channel, cells, finish_date, finish_date_claim, claim, basis, quoted_as_of, refrozen_at, frozen_by, supersedes; the superseded copy is <id>.quote.superseded-<YYYY-MM-DD>.json, and when that name exists it uses -2, -3.",
    "world_is": "refreeze.py writes those keys plus allowance_gap (None on the real TR request; a named gap when the finish is absent, so a null finish is never unexplained). On a name collision the counter sits after the date: <id>.quote.superseded-<YYYY-MM-DD>-2.json. Both are the builder's reading. The three named tests and dq_t26_real.py exercise neither a collision nor a null finish through refreeze.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/refreeze.py refreeze() new dict and _superseded_name() at this worktree (uncommitted diff over 16b6e889a8)",
        "dq_t26_real.py output at this worktree: new finish=2026-10-17, superseded 2026-10-13 kept with its reason, qva OPEN with cells_drawn 5858"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-S9",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~Q1",
    "surfaced_at": "2026-10-11T05:37:51Z",
    "one_line": "The D1-S8 re-draw wrote 18 of the 32 three-column price files to seven columns; the other 14 re-drew and were REJECTED:LOW_TRADE_AGREEMENT by the lock, so price_store.write left their three-column files in place and 127 of 141 are served with seven columns.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Round-7 analysis item 3 (ROUND_ANALYSIS.round7.md @f5553ca3d5): the 32 symbols are re-drawn through the pacer and the row closes on a served read of 141 of 141 files with seven columns.",
    "world_is": "2026-10-11T05:26Z-05:35Z, run_daily_draw.sh once on dell1 after redraw_stale.py --apply (32 pacer entries reset, one tier-2 request enqueued): stored 32 = LOCKED+written 18, REJECTED:LOW_TRADE_AGREEMENT+not written 14. redraw_stale.py --list afterwards reads total 141, stale 14 (LCEYX, FTHSX, HLMEX, IWS, IWP, IWN, IWO, VSEIX, PFORX, RPIFX, VSS, VWO, MISIX, PIMSX). Trade agreement of the 14: 116/141 to 613/748 (IWS 200/240). Each of these 14 had been written to three columns on 2026-10-09 under an earlier LOCK, so the same name now fails the lock it passed. The cause (lock floor or threshold change, or the transaction set) was not measured here. C-PRICES (total return on every price table) is not met for these 14.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "run log: scratchpad s8_redraw_run.log, daily_draw.py output line stored[] (18 LOCKED written, 14 REJECTED:LOW_TRADE_AGREEMENT not written)",
        "python data/mdpf/scripts/demque/redraw_stale.py --list at 2026-10-11 ~05:40Z: total 141, stale 14",
        "python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R8_CHECKS/dq_t28_stale.py: STALE-OK n=14 of 141"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-S10",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~R1",
    "surfaced_at": "2026-10-11T06:31:57Z",
    "one_line": "138 of the 1,038 rows in request AMGT_RESAPP-S14-CRNCY-SCANNER-US are names the identity pool already holds, whose trading currency the served function already states from their own model block.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "The request's reason (filed 2026-10-11 on CTO~DELL1 msg 3434): a peer member's price currency has no source in any store (the scanner carries no currency field; the model-block pool holds CRNCY only for held names), so CRNCY is requested for the 1,038 United States scanner rows.",
    "world_is": "crosswalk.resolve of each row's bloomberg form ('<T> US Equity') reads MEASURED for 138 of the 1,038, so each is a held name with its own model block; the live peers route already serves price_currency for such members (AMD and NFLX on ASML's peers, read 2026-10-11 ~05:3xZ). The request has no quote and no answer yet. The list is in AMGT_RESAPP deliverables 2.0.0_SA_COO~R1/round91_prep/DEMQUE_REQUEST_ROWS_ALREADY_HELD.txt (tab-separated, row and held security_key).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python crosswalk.resolve over org/missions/D8/MDPF/MDPF_DEMQUE/requests/AMGT_RESAPP-S14-CRNCY-SCANNER-US.json securities[].bloomberg, 2026-10-11 ~06:4xZ: 138 MEASURED of 1038",
        "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round90_prep/OO1_WHOLE_PAGE_READ_20261011.md: live ASML peers, members with a stored price_currency"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "A question for the queue's owner, not an instruction: keeping the 138 as a second source for currency is a reasonable use of the draw; dropping them narrows the quote. This seat takes no action on the request. The ask rides CTO~DELL1's round-90 analysis item 4."
  },
  {
    "id": "MDPF_DEMQUE-Z-S1",
    "one_line": "TO-DQ-t27's stated precondition oracle dq_t26_real.py can only ever pass ONCE: it re-runs refreeze on a COPY of the already-re-frozen real quote, refreeze correctly declines, and the check reads REFRZ-BAD -- so its BAD verdict is evidence DQ-t-26 SUCCEEDED, not that it is incomplete.",
    "spec_asserts": "TO-DQ-t27 THE CELL: 'Start only after DQ-t-26's commit is in your tree (python .../R8_CHECKS/dq_t26_real.py prints REFRZ-OK there; drawer_schedule.py exists).'",
    "world_is": "dq_t26_real.py prints 'REFRZ-BAD expected one superseded file, found 0'. Measured cause, not inferred: the check copies the REAL requests/DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS{.json,.quote.json} into a tempdir and runs refreeze.py there; refreeze.py:59-61 returns {\"status\": \"ALREADY_REFROZEN\"} and writes nothing when the frozen quote already carries `supersedes`. Run directly on a scratch copy it printed exactly that and wrote 0 new files (before/after listing identical). The real folder already holds the completed re-freeze that t26 performed at 01:42 local: quote.json finish_date 2026-10-17, finish_date_claim measured, supersedes -> DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS.quote.superseded-2026-10-11.json, and that superseded file carries finish_date 2026-10-13 with superseded_reason 'rule changed, round 6 R1' and superseded_by the live quote -- which is precisely what the check's four arms (new_finish, old_kept, graded_on_new, prints_both) describe. DQ-t-26's commit IS in this tree (277294a59c, 0.9.0_WK_MDPF_DEMQUE~21) and drawer_schedule.py exists, so the precondition's SUBSTANCE is met and only its stated oracle is stale-by-construction. The check is non-idempotent: it grades a state transition whose input state the real act has already consumed, so it is unpassable from now on. t27 proceeded on the substance; the check was NOT weakened and is outside this order's <paths> (R8_CHECKS is the issuer's). SECOND, SMALLER DISAGREEMENT OF THE SAME CLASS, recorded here rather than as its own row: this order's refusal clause prescribes the id `MDPF_DEMQUE-Z-W2-S<k>`, but .tools/surprise-row-gate.py REFUSES a W coordinate from a seat -- 'a seat's row on the main index carries no W (the coordinate names the allocator, and a seat allocates on the main index)'. The row was renamed to the next free seat id MDPF_DEMQUE-Z-S1 rather than taking the audited override, because the gate is right and the order text is wrong. The four pre-existing MDPF_DEMQUE-Z-W1-S* rows are not re-graded by the gate and were left untouched.",
    "project": "MDPF_DEMQUE",
    "fabric": "site-z",
    "surfaced_by": "0.7.0_AE_CloudOps~ZQ",
    "surfaced_at": "2026-10-11T07:55:00Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R8_CHECKS/dq_t26_real.py -> 'REFRZ-BAD expected one superseded file, found 0'",
        "data/mdpf/scripts/demque/refreeze.py:59-61 the `supersedes` guard returning ALREADY_REFROZEN; direct run on .scratch/rf printed {\"status\": \"ALREADY_REFROZEN\"} rc=0 and wrote no superseded file",
        "org/missions/D8/MDPF/MDPF_DEMQUE/requests/DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS.quote.json (finish 2026-10-17, supersedes set) and .quote.superseded-2026-10-11.json (finish 2026-10-13, reason 'rule changed, round 6 R1')",
        "git log -1 data/mdpf/scripts/demque/refreeze.py -> 277294a59c 0.9.0_WK_MDPF_DEMQUE~21 DQ-t-26"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-Z-S2",
    "one_line": "A MID-DRAW re-quote of a partially drawn request reads a finish date ONE FIRE DAY LATER than the frozen quote (2026-10-18 vs 2026-10-17) because quote() always prices the FULL request from today's fire days and never subtracts the cells already drawn -- a reader comparing the two would see a slip that is not a slip.",
    "spec_asserts": "CTO round-7 analysis R2 and the re-frozen quote: the TR request's finish_date is 2026-10-17 (Sat 10-10, Sun 10-11, Sat 10-17 at 5,858 a day), finish_date_claim measured, and quote_vs_actual grades the re-frozen quote.",
    "world_is": "Measured with the mechanism printed, not inferred. bbg_quote.quote(TR request, allowance, 0, as_of) returns finish 2026-10-17 for as_of 2026-10-09 and 2026-10-10, and finish 2026-10-18 for as_of 2026-10-11. Cause: the request is 15,720 cells and the ceiling is 5,858 a day, so pricing the FULL request needs 3 fire days, counted FORWARD from as_of. From 10-09 the first three fire days are 10-10, 10-11, 10-17 (finish 10-17); from 10-11 they are 10-11, 10-17, 10-18 (finish 10-18). quote() does not subtract the 5,858 cells t24 already drew on 10-10, so each fire day that passes slides a live re-quote one fire day later while nothing is actually late. The frozen quote on disk still reads 2026-10-17 and remains the authority (that is what freezing is for), and quote_vs_actual grades the frozen value. NO EFFECT ON THE DRAWER OR ON t27's CRITERIA: standing_drawer reads only allowance_today (5,858) from the live quote, stores no finish_date in its receipt, and passes the FROZEN quote to record_actual so cells_quoted is 15,720; AC1, AC2 and AC3 never read a finish date. Filed because the two dates sitting side by side is a false-alarm generator for a later reader or a freshness check, not because anything is wrong today.",
    "project": "MDPF_DEMQUE",
    "fabric": "site-z",
    "surfaced_by": "0.7.0_AE_CloudOps~ZQ",
    "surfaced_at": "2026-10-11T09:50:00Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "bbg_quote.quote(TR, allowance, 0, as_of) -> finish 2026-10-17 at as_of 2026-10-09 and 2026-10-10; 2026-10-18 at as_of 2026-10-11",
        "drawer_schedule.fire_days from each as_of: ['2026-10-10','2026-10-11','2026-10-17',...] vs ['2026-10-11','2026-10-17','2026-10-18']",
        "15720 cells / 5858 per day = 2.68 -> 3 fire days when pricing the full request",
        "org/missions/D8/MDPF/MDPF_DEMQUE/requests/DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS.quote.json finish_date 2026-10-17 (frozen, the authority)"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-Z-S3",
    "one_line": "The TR request can NEVER reach its quoted 15,720 cells: the quote prices 1,310 WEEKDAYS per security but the vendor returns 1,260 TRADING days, so full coverage is 15,120 cells and `drawn < quoted` leaves the request OPEN forever -- from 2026-10-18 every non-trading day will fire the standing drawer, draw 0 rows and append a DRAWN actuals line reading cells_drawn 0.",
    "spec_asserts": "TO-DQ-t27: an open request is one 'whose cells drawn so far ... are fewer than its quoted cells', and the drawer draws open backfill requests until they are no longer open. The frozen quote reads cells.bloomberg_history 15720 with claim measured.",
    "world_is": "Measured with the denominator printed. The frozen quote's own basis is weekdays: 1,310 weekdays over 2021-10-01..2026-10-08 x 6 securities x 2 fields = 15,720, which reproduces the frozen figure exactly. But the vendor returns 1,260 rows per security: FOUR securities (KO, JNJ, T, VZ) are now complete to the request's end date 2026-10-08 and each holds exactly 1,260 rows, so the 50-row-per-security difference is NYSE holidays that fall on weekdays, not an incomplete draw. Real full coverage is therefore 1,260 x 6 x 2 = 15,120 cells, leaving an UNREACHABLE REMAINDER of 600 cells against the quote. Consequence, traced through the code: open_requests tests `already >= quoted` (standing_drawer.py), so at 15,120 the request still reads open; _draw_request advances each security's window to the day after its latest stored date, so once every security is complete `start > end` and all are skipped, the run draws 0 rows with reason None, and run() records outcome DRAWN with cells_drawn 0. PREDICTED DATES, checkable: MO needs 442 more rows and XOM 1,260, i.e. 3,404 cells, which is under the 5,858 ceiling, so the 2026-10-17 fire completes coverage at 15,120; the 2026-10-18 fire is the FIRST no-op, and every non-trading day after it appends another zero-cell DRAWN line. NO EFFECT ON t27's CRITERIA, all three of which passed today: AC1 DRW-OK, AC2 DRSCH-OK, AC3 FIRE-OK. The remedy is a round decision, not a mid-round edit, and it is not weakened here: either the open test becomes coverage-based (every security's window exhausted) rather than cell-count-based, or the quote is priced on trading days rather than weekdays. Found while verifying this fire's resume, not by looking for it.",
    "project": "MDPF_DEMQUE",
    "fabric": "site-z",
    "surfaced_by": "0.7.0_AE_CloudOps~ZQ",
    "surfaced_at": "2026-10-11T14:20:00Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "weekday count 2021-10-01..2026-10-08 = 1310; 1310 x 6 x 2 = 15720, reproducing the frozen quote exactly",
        "KO, JNJ, T and VZ are each complete to the request end 2026-10-08 with exactly 1260 rows (t24 + t27 parquets)",
        "1260 x 6 x 2 = 15120 real full coverage; 15720 - 15120 = 600 unreachable cells",
        "standing_drawer.py open_requests `already >= quoted` test and _draw_request's per-security window advance",
        "receipt.2026-10-11.json cells_drawn 5858, 11716 of 15720 drawn, 4004 remaining by quote arithmetic vs 3404 by vendor rows"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-S11",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~Q1",
    "surfaced_at": "2026-10-11T15:34:07Z",
    "one_line": "The transactions store holds ONE partition, date=2026-06-23, with largest Trade_Date 2026-06-22: the round-8 ruling that the lock reads the latest partition and checks trades since June has no later trades to read, so a served window past 2026-06-22 cannot be proved by the client's trades.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "ROUND_ANALYSIS.round8.md R1 (b): the lock reads the LATEST transactions partition, resolved through opal_naming, not a pinned date; new trades since June are checked.",
    "world_is": "2026-10-11 ~16:2xZ, S3 read (boto3, this seat): s3://opal-data-assets/commonwealth/cottonwood/silver/transactions/ lists one date= partition, date=2026-06-23, five parquet parts, 1,416,497 rows, max Trade_Date 2026-06-22. commonwealth/cottonwood/ holds only bronze/ and silver/; bronze/ lists imaging, manifest, portfolio_accounting (not read). Resolving the latest partition returns the same June snapshot today. TO-DQ-t30 resolves it dynamically and TO-DQ-t31's extension claims `held` for any window past trades_through; the served apply of the extension is HELD for the CTO's word.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "boto3 list_objects_v2 Delimiter=/ on commonwealth/cottonwood/silver/transactions/ -> 1 partition (2026-10-11, this seat)",
        "pyarrow max(Trade_Date) over date=2026-06-23/*.parquet -> 2026-06-22, 1,416,497 rows"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W25-S1",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~25",
    "surfaced_at": "2026-10-11T15:46:45Z",
    "one_line": "For FTHSX, IWS and VWO the served file and the fresh draw agree with the trades to the same percentage (40.7, 83.3 and 87.2 on both sides), so the draw-column class does not hold for these three: the causes measure as wrong-symbol (FTHSX) and never-met-floor (IWS, VWO).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO-DQ-t32 (round 9, DQ-t-32): the cause of each lock rejection is measured first; the classed causes are wrong-symbol, draw-column (old agreement >= 90 and new < 90), never-met-floor and unclassified.",
    "world_is": "2026-10-11 ~15:4xZ, lock_cause.py --names FTHSX,IWS,VWO --json at worktree wk-MDPF_DEMQUE-25 (branch HEAD descends from 477921e3dc): FTHSX old 40.7 new 40.7 n_checked 627 cause wrong-symbol disagreeing 372; IWS old 83.3 new 83.3 n_checked 240 cause never-met-floor disagreeing 40; VWO old 87.2 new 87.2 n_checked 313 cause never-met-floor disagreeing 40. first_lock_predates_floor is true for all three.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t32_real.py -> LCAUSE-OK 3 of 3 names read (S3 read plus three paced Yahoo pulls under a scratch pacer; nothing written)",
        "data/mdpf/scripts/demque/lock_cause.py measure(): old side is the served prices.parquet as_traded_close, new side is yahoo_pull.pull as_traded_close, both against the same daily trade medians with lock.check's tolerance",
        "python data/mdpf/scripts/demque/hold_lock_records.py --dry-run -> 14 planned, 14 three-column names, the three names among them (no write)"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W26-S1",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~26",
    "surfaced_at": "2026-10-11T15:45:39Z",
    "one_line": "refreeze.py prices the full request from as_of with 0 drawn, so a re-freeze whose as_of is after draws began reads a finish the remaining cells do not support: the DQ9-t33 AC2 re-freeze (--as-of 2026-10-11) gives finish 2026-10-18 for 15120 cells with 11716 drawn, where the remaining-cells quote gives 2026-10-17.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "refreeze.py docstring: as_of is the day the original quote was frozen, and the re-frozen quote is bbg_quote.quote(request, allowance, 0, as_of). DQ-t-33 item 3 names no drawn_to_date for refreeze.",
    "world_is": "On scratch copies of the TR request folder (tier 4 history, 15120 cells, ceiling 5858 measured), refreeze.py --as-of 2026-10-11 wrote a second superseded file with supersedes set, and quote_vs_actual reads finish_date 2026-10-18 with cells_drawn 11716. The same request quoted with --today 2026-10-11 and --actuals reads finish 2026-10-17 and cells_remaining 3404.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "dq_t33_real.py run from the worktree: refreeze rc=0 superseded_files=2; qva finish_date 2026-10-18, cells_drawn 11716, cells_quoted 15120",
        "bbg_quote.py --quote on the real request file with --actuals scratch ledger: cells 15120, cells_remaining 3404, finish_date 2026-10-17",
        "data/mdpf/scripts/demque/refreeze.py@b3a1f43daa refreeze(): q = bbg_quote.quote(request, allowance, 0, as_of_day)"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W26-S2",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~26",
    "surfaced_at": "2026-10-11T15:45:39Z",
    "one_line": "bbg_quote.quote() refuses a model_block request whose drawn_to_date is above 0 (ValueError), because the order names no remaining-cells rule for model_block, whose components draw on two channels.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "DQ-t-33 item 1: quote(..., drawn_to_date) walks and dates cells - drawn_to_date. The order does not say how a model_block request with drawn cells is priced.",
    "world_is": "data/mdpf/scripts/demque/bbg_quote.py quote(): the model_block branch raises ValueError when drawn_to_date is non-zero; with drawn_to_date 0 it prices as before.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/bbg_quote.py quote(): if drawn_to_date: raise ValueError('model_block has no remaining-cells quote ...')",
        "no model_block case in data/mdpf/scripts/demque/test_demque_quote_remaining.py; the existing model_block test in test_demque_bbg.py passes unedited"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W26-S3",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~26",
    "surfaced_at": "2026-10-11T15:45:39Z",
    "one_line": "bbg_quote.py --quote --actuals takes drawn_today over ledger lines whose channel equals the REQUEST channel, not the literal history. The two readings agree for every history request, which is the only class the order sizes, but differ for a bql or reference request.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "DQ-t-33 CLI: drawn_today is the sum of cells_drawn of every channel history line dated today.",
    "world_is": "data/mdpf/scripts/demque/bbg_quote.py _actuals_drawn(path, request_id, channel, today) filters on the request channel; for the TR request (channel history) that is the literal reading.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/bbg_quote.py _actuals_drawn(): if r.get('channel') == channel and row_day == day",
        "org/missions/D8/MDPF/MDPF_DEMQUE/requests/DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS.json channel history, so the readings agree for the real request"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W26-S4",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~26",
    "surfaced_at": "2026-10-11T15:45:39Z",
    "one_line": "quote_vs_actual.read takes the EARLIER of a COMPLETE line's date and the coverage date as drawn_date. The literal reading (the COMPLETE date alone) would move a request covered on time to LATE when its COMPLETE line lands after the finish day.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "DQ-t-33 item 2: a line with outcome COMPLETE sets drawn_date to its date (even when the cells never reach the quoted figure); otherwise unchanged.",
    "world_is": "data/mdpf/scripts/demque/quote_vs_actual.py read(): drawn_date = min(first coverage date, first COMPLETE date). test_complete_row_closes_the_request_and_sets_the_drawn_date covers a COMPLETE line with no coverage, not coverage followed by a later COMPLETE line.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/quote_vs_actual.py read(): closed = sorted COMPLETE dates; if closed and (drawn_date is None or closed[0] < drawn_date)",
        "data/mdpf/scripts/demque/test_demque_quote_remaining.py test_complete_row_closes_the_request_and_sets_the_drawn_date (r-done ON_TIME on the finish day, r-late LATE)"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-S12",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~Q1",
    "surfaced_at": "2026-10-11T16:00:23Z",
    "one_line": "Three of the 14 rejected names (FTHSX 40.7 pct, PFORX 42.9, RPIFX 39.2) are classed wrong-symbol by the cause rule, and FTHSX and PFORX are held by 4 and 11 accounts in the positions snapshot -- a client page may value those holdings with a possibly wrong security's prices.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "spec_asserts": "ROUND_ANALYSIS.round8.md R2: the near-40 pct names are read for whether any client page values a holding with them; if one does, that is a BLOCKING row to the CTO BEFORE any page change (a PROD change to a client-facing page waits on Andrew's word).",
    "world_is": "2026-10-11 ~16:0xZ: lock_cause.py over the 14 (ROUND9_LOCK_CAUSE_14.md): agreement old == new for every name; RPIFX 39.2, FTHSX 40.7, PFORX 42.9 (all Mutual Fund, 513 to 651 trade dates) class wrong-symbol (both below 60). silver/positions/date=2026-06-23 (the only partition, AsOfDate 2026-06-23): FTHSX 4 accounts, PFORX 11 accounts, RPIFX 0, Account_Status 0 on every row. Whether a client page values those positions through these price files was NOT traced; the three names serve unchanged with claim held and this reason. No page was changed.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/2.0.0_SA_COO~Q1/ROUND9_LOCK_CAUSE_14.md",
        "boto3 + pyarrow read of silver/positions/date=2026-06-23/part-00000.parquet, Cusip in (14064D865, 693390882, 77958B402) (this seat, 2026-10-11)"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W24-S1",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~24",
    "surfaced_at": "2026-10-11T15:51:39Z",
    "one_line": "demand_queue.draw skips every request whose job id already has a DRAWN row in the ledger; the standing request id STANDING-T1-EXTEND is fixed, so after its first DRAWN day no later daily draw fetches or writes it. The standing extension would run once and then go silent.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~Q1",
    "spec_asserts": "TO-DQ-t31 and ROUND-8 R1 (a)/(c): a STANDING tier-1 request, rebuilt each trading day, carries every locked symbol to the T-1 frontier through the shared pacer; apply resets those symbols so the day's draw re-pulls each once. The request id is pinned as STANDING-T1-EXTEND.",
    "world_is": "data/mdpf/scripts/demque/demand_queue.py@477921e3dc draw(): already = {job of each ledger row with outcome DRAWN} and a request whose request_id is in already is skipped (lines 169-173). run_daily_draw.sh appends every day to one ledger.jsonl with no per-day key, so the DRAWN row of day 1 stays in the ledger. Worker scratch probe (uncommitted, .scratch/t31_ledger/probe_ledger_skip.py at e3739bada7 plus this commit): one standing request, one DRAWN row for STANDING-T1-EXTEND, day-2 draw: fetch calls on day 2: 0, ledger rows written: 0. The apply is HELD for the CTO's word and has not run; no served, pacer or queue state was touched.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/demand_queue.py@477921e3dc lines 169-173: already set from DRAWN ledger jobs; continue when request_id in already",
        "scratch probe run in the worktree: fetch calls on day 2: 0 | ledger rows written: 0 | rows: []",
        "data/mdpf/scripts/demque/run_daily_draw.sh@e3739bada7 appends to $STATE/ledger.jsonl on every run (no per-day ledger key)"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W28-S1",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~28",
    "surfaced_at": "2026-10-11T16:17:14Z",
    "one_line": "DQ-t-36 AC2 cannot be met as written: the criterion asks --plan --today 2026-06-30 to be refused, but 2026-06-30 is AFTER the live store's latest valid_to 2026-06-23, so the guard the build specifies (refuse a frontier before latest valid_to) correctly plans it. Refusing it would block every normal daily extension. The worker did not weaken AC1 or AC2; the order stays open.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "spec_asserts": "DQ-t-36 (TO-DQ-t36 build item 1 and AC2): plan() refuses a frontier before the store's latest valid_to, apply() writes nothing; AC2 on the REAL store: --plan --today 2026-06-30 exits non-zero with no JSON plan and names the latest valid_to (the arms early_refused and early_names_valid_to); --plan --today 2026-10-12 still plans 141 symbols. The order's premise: 2026-06-30 is a frontier 'before every file's end, 2026-06-22/23'.",
    "world_is": "Live read only (ps.index over ps.s3_root(), 141 rows): max valid_to 2026-06-23; 96 rows at 2026-06-22, 45 at 2026-06-23. So 2026-06-30 is after every file's end and extends them, it does not shorten them. Base and built code: data/mdpf/scripts/demque/extend_frontier.py@92de80e612 plan() exits 0 for 2026-06-30 with the guard (frontier < latest_end is false). dq_t36_real.py output: 'early: rc=0 ... end 2026-06-30 symbols 141' and 'GUARD-REAL-BAD arms=early_refused,early_names_valid_to'. The shortening hazard is real only for a manual --today before 2026-06-23 (e.g. 2026-06-22); the scheduled daily --apply runs on the real date, after the store's end. Hazard INERT: nothing applied, no served, pacer or queue state touched.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/price_store.py index(): valid_to read from each lock.json (read-only S3 via ps.s3_root(), 2026-10-11)",
        "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t36_real.py run in the worktree at 92de80e612: GUARD-REAL-BAD arms=early_refused,early_names_valid_to",
        "python data/mdpf/scripts/demque/extend_frontier.py --plan --today 2026-06-30 (worktree, guard built): rc=0, end 2026-06-30, symbols 141"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-Z-S4",
    "one_line": "TO-DQ-t34's precondition oracle dq_t33_real.py is once-only in the SAME way Z-S1 recorded for dq_t26_real.py: its arms[supersedes_new] demands the re-freeze TRANSITION, which DQ-t-33's real act already consumed, so it reads QR-REAL-BAD while three of its four arms confirm the end state it wanted.",
    "spec_asserts": "TO-DQ-t34 THE CELL: 'Start only after DQ-t-33's commit is in your tree (python .../R9_CHECKS/dq_t33_real.py prints QR-REAL-OK there; bbg_quote.record_actual accepts outcome=\"COMPLETE\").'",
    "world_is": "dq_t33_real.py prints 'QR-REAL-BAD arms=supersedes_new'. Measured cause: the REAL requests folder already holds BOTH superseded quotes -- DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS.quote.superseded-2026-10-11.json (t26's re-freeze) and ...-2026-10-11-2.json (t33's chained re-freeze) -- and the live quote's `supersedes` already names the -2 file. The check copies that finished folder to a tempdir and re-runs refreeze.py, which correctly returns {\"status\": \"ALREADY_REFROZEN\"} and writes nothing, so `added = set(after) - set(before)` is EMPTY and the arm's `len(added) == 1` is False. Reproduced in isolation with the file names printed before and after. THE ASYMMETRY IS THE TELL: arms[second_superseded] (rc == 0 and exactly 2 superseded files) PASSES on the same re-freeze, because it reads the END STATE, while arms[supersedes_new] fails because it reads the DELTA. The other three arms all pass and together confirm t33 landed: cells 15120 == want 15120 (history now priced on TRADING days, which is Z-S3's remedy), cells_remaining 3404, finish_date 2026-10-17, label a remaining-cells quote, and quote_vs_actual OPEN printing both superseded finishes. SUBSTANCE FOR THIS CELL IS MET AND WAS EXERCISED, NOT INFERRED: bbg_quote.record_actual(..., outcome='COMPLETE') is ACCEPTED (a DRAWN positive control ran first so the call shape was right), the CLI carries --outcome {DRAWN,STOPPED,COMPLETE} and --actuals, and bbg_quote.py is at 00ca5a6f1e (DQ-t-33, 0.9.0_WK_MDPF_DEMQUE~26) with t33's own order at status complete. t34 therefore proceeded on the substance; dq_t33_real.py was NOT weakened and is outside this order's <paths> (R9_CHECKS is the issuer's). SECONDARY, AND THE REASON AN EARLIER READ OF MINE WAS WRONG: at 2026-10-11T15:52Z this check failed differently, with 'unrecognized arguments: --actuals' and a usage line reading --outcome {DRAWN,STOPPED}, because t33 was NOT YET in this tree -- it arrived at box-sync 83722b5786 (12:23 local / 16:23Z). A precondition measured against a tree a scheduled integrate is still moving can read BAD for a reason that evaporates minutes later, so the arrival commit is worth naming whenever a dependency check is quoted.",
    "project": "MDPF_DEMQUE",
    "fabric": "site-z",
    "surfaced_by": "0.7.0_AE_CloudOps~ZQ",
    "surfaced_at": "2026-10-11T16:40:00Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python .../R9_CHECKS/dq_t33_real.py -> 'QR-REAL-BAD arms=supersedes_new' with cells=15120 want=15120 remaining=3404 finish=2026-10-17 label=remaining-cells and superseded_files=2",
        "isolated reproduction: BEFORE 2 superseded files, refreeze rc=0 {\"status\": \"ALREADY_REFROZEN\"}, AFTER 2, added=[] so len(added)==1 is False",
        "the live quote's supersedes already names DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS.quote.superseded-2026-10-11-2.json",
        "record_actual(..., outcome='COMPLETE') ACCEPTED under a DRAWN positive control; guard reads (\"DRAWN\", \"STOPPED\", \"COMPLETE\")",
        "git log: bbg_quote.py at 00ca5a6f1e (DQ-t-33); arrival here at box-sync 83722b5786, 2026-10-11 12:23 local",
        "dq_t33_real.py:60-68, the arms dict, where second_superseded reads the end state and supersedes_new reads the delta"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W29-S1",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~29",
    "surfaced_at": "2026-10-11T16:40:06Z",
    "one_line": "DQ-t-37 says test_demque_extend_frontier.py keeps passing UNEDITED, but two of its tests pass --today 2026-10-12, later than the local date 2026-10-11, so the new refusal raises SystemExit on them and the suite is red until those tests pin the local date.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "spec_asserts": "TO-DQ-t37 build item 2 and the ACCEPTANCE block: test_demque_extend_frontier.py and test_demque_extend_guard.py keep passing UNEDITED; if one passes a today later than the real date, that is a surprise row, not an edit (they should pin the local date by monkeypatch).",
    "world_is": "pytest over test_demque_extend_frontier.py, test_demque_extend_guard.py and test_demque_extend_future.py at the worktree (extend_frontier.py with the DQ-t-37 refusal, 2026-10-11): 2 failed, 7 passed. The failures are test_plan_window_ends_at_the_expected_last_trading_day_and_lists_every_locked_symbol (plan(root, today='2026-10-12')) and test_apply_resets_exactly_the_plan_symbols_and_replaces_the_standing_request_file (its second apply(today='2026-10-12')); both raise '--today 2026-10-12 is after the local date 2026-10-11'. They pass on or after 2026-10-12 and fail before it. The guard file passes 3 of 3; test_demque_extend_frontier.py is unedited. Hazard INERT: the refusal writes nothing and touches no served, pacer or queue state, and the daily run uses the real date, so it is not affected.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/test_demque_extend_frontier.py@d5f215229d: test_plan_window_ends_at_the_expected_last_trading_day_and_lists_every_locked_symbol calls xf.plan(root, today=\"2026-10-12\"); test_apply_resets_exactly_the_plan_symbols_and_replaces_the_standing_request_file calls xf.apply(root, ..., today=\"2026-10-12\")",
        "python -m pytest -q test_demque_extend_frontier.py test_demque_extend_guard.py test_demque_extend_future.py (cwd data/mdpf/scripts/demque, 2026-10-11): 2 failed, 7 passed; SystemExit: --today 2026-10-12 is after the local date 2026-10-11: the extension plans no future day"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W29-S2",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~29",
    "surfaced_at": "2026-10-11T16:40:06Z",
    "one_line": "The order says to pin the local date by monkeypatch 'the way test_demque_extend_frontier.py does for its dates', but that file has no monkeypatch at all; it passes literal today= strings. The new test file pins the local date its own way.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO-DQ-t37 build item 2: test_demque_extend_future.py monkeypatches date.today in the module 'the way test_demque_extend_frontier.py does for its dates'.",
    "world_is": "test_demque_extend_frontier.py@d5f215229d has no monkeypatch call and no fixture; its dates are today= arguments. test_demque_extend_future.py (new, uncommitted when this row was filed) pins the local date with a local_day fixture that sets xf.date to a date subclass whose today() returns 2026-10-11. No existing test file was edited. Hazard INERT: a test-only pinning choice; no served, pacer or queue state is involved.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "read of data/mdpf/scripts/demque/test_demque_extend_frontier.py@d5f215229d: imports are json, os, pandas, demand_queue, extend_frontier, price_store, yahoo_pull; no monkeypatch; every date is a today= literal",
        "data/mdpf/scripts/demque/test_demque_extend_future.py (new, uncommitted at row time): local_day fixture monkeypatches xf.date to _PinnedDate, today() = 2026-10-11"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W27-S1",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~27",
    "surfaced_at": "2026-10-11T16:29:26Z",
    "one_line": "The two Cottonwood Tier-2 inputs that land_cot.py writes and build_canonical_prices_v2.py reads are absent: silver/historical_prices.parquet and config/ticker_lookup.json return 404 in opal-data-cot.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "land_cot.py docstring L3-5 and build_canonical_prices_v2.py INPUT_ADDRESSES (L168-172) name s3://opal-data-cot/silver/historical_prices.parquet and s3://opal-data-cot/config/ticker_lookup.json as the Tier-2 inputs; the lander lands the locked as-traded closes into the first.",
    "world_is": "HeadObject opal-data-cot/silver/historical_prices.parquet: 404 Not Found. GetObject opal-data-cot/config/ticker_lookup.json: 404 NoSuchKey (this seat, 2026-10-11 ~16:2xZ). The consumer's _load_tier2 (build_canonical_prices_v2.py L539-563) prints WARN and skips Tier 2 (Yahoo), starting from YF_OVERRIDES only. silver/prices/canonical_prices.parquet is present (LastModified 2026-10-09T13:41:04Z). Not established whether Tier 2 ever contributed to that served file.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/land_cot.py@53842ab400 L3-5, L79 (HIST_KEY), L257-274 (apply_plan)",
        "data/cot/scripts/gold/build_canonical_prices_v2.py@53842ab400 L168-172, L539-563",
        "aws s3api head-object --bucket opal-data-cot --key silver/historical_prices.parquet: 404; get-object --key config/ticker_lookup.json: 404 NoSuchKey"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W27-S2",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~27",
    "surfaced_at": "2026-10-11T16:29:26Z",
    "one_line": "The 15 positions cannot be bridged to any served account or household artifact: the custodian AccountNumbers match no account_id in gold/dimensions/accounts_dimension_latest.parquet and the advisor positions.json is not served, so all 15 rows are read_by_a_page false.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "spec_asserts": "TO-DQ-t35 item 2: read_by_a_page is true only where the hop that puts the position's value on a page was read; the trace must reach each account's page.",
    "world_is": "silver/positions date=2026-06-23 carries FTHSX in 4 accounts and PFORX in 11 (Advisor_ID HKJ and S58; custodian numbers of the B3S, 0QF and RGY kind). An exact match of the 11 custodian numbers against accounts_dimension account_id (1000 rows read, ids of the z09 kind) returns 0 rows. platinum/advisors/cottonwood_capital_advisors/ holds nna_clients.json, summary.json and timeseries.json; positions.json is NoSuchKey. The custodian-number-to-account_id crosswalk was not read. The table reads 0 of 15 on a page; which page values these 15 positions is open at account grain.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "commonwealth/cottonwood/silver/positions/date=2026-06-23/part-00000.parquet read with pandas (this seat): 15 rows, FTHSX 4, PFORX 11",
        "gold/dimensions/accounts_dimension_latest.parquet (opal-data-cot): exact isin test on the 11 custodian numbers returns an empty frame (1000 rows)",
        "aws s3api get-object opal-data-cot platinum/advisors/cottonwood_capital_advisors/positions.json: NoSuchKey; prefix listing: nna_clients.json, summary.json, timeseries.json"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W27-S3",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~27",
    "surfaced_at": "2026-10-11T16:29:26Z",
    "one_line": "The lot-valuation prefix that D_04 reads, gold/timeseries/holdings_lots/ in opal-data-cot, has no objects; dated holdings_lots objects exist in opal-data-bd. Which bucket writer and reader bind to in the deployed run is not established.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "D_04 _find_latest_holdings_lots (HOLDINGS_LOTS_PREFIX, lib/s3_layout.py L49) reads the latest non-backfill holdings_lots snapshot from BUCKET = lib.config S3_BUCKET; B_01 writes the same prefix.",
    "world_is": "list-objects-v2 opal-data-cot prefix gold/timeseries/holdings_lots/: KeyCount null (no objects). list-objects-v2 opal-data-bd, same prefix, max-items 3: gold/timeseries/holdings_lots/2026-02-20.parquet, 2026-02-23.parquet, 2026-02-27.parquet (latest not read). lib/config.py defaults to opal-data-cot unless BD_S3_BUCKET is set on the runner; that setting is not in the repo.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/cot/scripts/gold/lib/config.py@53842ab400 L9, L16",
        "data/cot/scripts/gold/D_04.client_portal_summary.py@53842ab400 L83, L300-306",
        "data/cot/scripts/gold/lib/s3_layout.py@53842ab400 L49",
        "aws s3api list-objects-v2 on opal-data-cot and opal-data-bd, prefix gold/timeseries/holdings_lots/ (this seat, 2026-10-11)"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W27-S4",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~27",
    "surfaced_at": "2026-10-11T16:29:26Z",
    "one_line": "On the page side a lot is re-priced from the custodian RPS closing price for any account with RPS coverage, so the Yahoo-path price file need not be the price a page shows for the same security.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "B_01 market_value = current_units x current_price, where current_price is the latest canonical price by asset_name (B_01 L29-30, L316-380).",
    "world_is": "B_01 L636-661 builds rps_price_by_cusip and rps_price_by_ticker keyed by (bd_account_id, cusip) and (bd_account_id, ticker) and overrides the lot price where the account has RPS coverage (comment COO GO 2026-04-17). Whether any of the 15 accounts has RPS coverage for these CUSIPs was not read. The price-file path reaches a page only for lots without that override.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/cot/scripts/gold/B_01.holdings_lots.py@53842ab400 L29-30, L316-380, L636-661"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W27-S5",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~27",
    "surfaced_at": "2026-10-11T16:29:26Z",
    "one_line": "The existing name resolvers return no ticker for the FTHSX and PFORX names as the positions snapshot writes them, and no store names RPIFX; the PFORX share-class candidates came from a name-stem text match over two classification stores, not from a resolver output.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO-DQ-t35 item 3: the candidates are the tickers the EXISTING resolvers return for each CUSIP (C-IDENTITY: no second resolver).",
    "world_is": "resolve_tickers.py chains (canonical_name, bd_securities_exact, mutual_fund_pattern, etf alias dict) return nothing for 'Fullerthaler Behavioral Small-Cap Equity Fund Institutional Shares' and 'PIMCO International Bond Fund (U.S. Dollar-Hedged) Institutional Class' (this seat). The stores carry the family under other spellings: bd-securities 'PIMCO International Bond (U.S. Dollar-Hedged) Fund Class I-2' -> PFBPX; etf-classifications 'PIMCO International Bond Fund (U.S. Dollar-Hedged) Class I-3' -> PFONX. No row carries 77958B402 in a ticker or asset_name field. Pulled: PFBPX 42.9 (n 513), PFONX 42.5 (n 506), PFUIX 0.0 (n 513); none reaches 90. Not claimed: that any share class is the right one.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/black_diamond/scripts/classification/resolve_tickers.py@53842ab400 L193-268, L399 (resolver chains)",
        "this seat's uncommitted scratch runs .scratch/t35/resolve_step_a.py, resolve_step_a2.py, candidates_step_b.py; denominators bd-securities 11,007 items, etf-classifications 9,339 named items"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W27-S6",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~27",
    "surfaced_at": "2026-10-11T16:29:26Z",
    "one_line": "The TO's proof command names only DQ9-t35-AC1 as the expected criterion, but its expected_criteria lists AC1 and AC2; the validator with AC1 alone returns INVALID (AC2 an unexpected addition, rc 1) and with both ids VALID (rc 0).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO-DQ-t35 proof_of_spec: validate with proof-of-spec-check <instance> DQ9-t35-AC1, AC2 is judgment and carries no verdict; <expected_criteria>DQ9-t35-AC1,DQ9-t35-AC2; general rule: one acceptance row per id in expected_criteria.",
    "world_is": "proof-of-spec-check <instance> DQ9-t35-AC1 -> 'coverage: instance row DQ9-t35-AC2 is NOT in the TO's expected set', INVALID rc=1. proof-of-spec-check <instance> DQ9-t35-AC1,DQ9-t35-AC2 -> VALID rc=0 (this seat, 2026-10-11). The instance was validated with both ids, the set the TO's expected_criteria names; the flip rests on that run.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D8/MDPF/MDPF_DEMQUE/task-orders/MDPF_DEMQUE.TO-DQ-t35.valuation-trace-and-reresolve.md@53842ab400 (proof_of_spec section and <expected_criteria>)",
        "python .tools/proof-of-spec-check.py <instance> DQ9-t35-AC1 (rc 1) and <instance> DQ9-t35-AC1,DQ9-t35-AC2 (rc 0), this seat 2026-10-11"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W27-S7",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~27",
    "surfaced_at": "2026-10-11T16:48:09Z",
    "one_line": "The production bucket is opal-data-cot, not the provisioned firm bucket: the cottonwood gold SSM document exports BD_S3_BUCKET=opal-data-cot and its chain does not run B_01 holdings_lots, so gold/timeseries/holdings_lots/ is empty by design and D_04 skips its account and advisor-position steps.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO-DQ-t35 item 1: the production bucket is established before hops 2-6 are read; the trace expected the lot-valuation artifact gold/timeseries/holdings_lots/ to be produced by the production run.",
    "world_is": "infra/aws/terraform/cot-pipeline/ssm.tf (this seat, @53842ab400): SSM document opal-cot-gold-run exports BD_S3_BUCKET=opal-data-cot and FIRM_ID=cottonwood (L304-331); the COT silver merge document exports the same (L233); the COT v1 chain comment excludes B_01/B_01b/B_02/B_03 lots (L294), and run_gold does not list B_01 (L375-404). opal-data-cottonwood holds none of silver/historical_prices.parquet, config/ticker_lookup.json, silver/prices/canonical_prices.parquet (HeadObject 404) or gold/timeseries/holdings_lots/ (no objects). D_04 L1304-1307 prints WARN and skips when no holdings_lots object exists.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/terraform/cot-pipeline/ssm.tf@53842ab400 L233, L294, L304-331, L375-404",
        "data/cot/scripts/gold/D_04.client_portal_summary.py@53842ab400 L1304-1307",
        "aws s3api head-object and list-objects-v2 on opal-data-cottonwood and opal-data-cot (this seat, 2026-10-11)"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W27-S8",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~27",
    "surfaced_at": "2026-10-11T16:48:09Z",
    "one_line": "In production the page value of the FTHSX and PFORX holdings is the BD snapshot market value per unit, not a Yahoo or canonical close; the price-file path does not set those page values, and the canonical name-keyed prices for these names are interpolated and end 2026-06-09.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO-DQ-t35 item 1 hop 5: the value artifact prices the position from the price file (the chain as written in the order).",
    "world_is": "gold/canonical/holdings/2026-10-09.parquet (opal-data-cot, read this seat): FULLERTHALER BEHAVIORAL SM-CP EQ INST 188 accounts, price 57.57-57.67, source bd_snapshot; PFORX-family (USD-HDG) INSTL 334 accounts, price 9.45-9.46, bd_snapshot. B_00 L171-173 sets price = market_value / units and source bd_snapshot. silver/prices/canonical_prices.parquet (read this seat): for the five FTHSX/PFORX-family names the sources are linear_interpolation and transaction_observed only (no yahoo_finance row), last date 2026-06-09 for every row of the file (11,289,398 rows).",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/cot/scripts/gold/B_00.canonical_holdings.py@53842ab400 L163-175",
        "aws s3 cp opal-data-cot/gold/canonical/holdings/2026-10-09.parquet and silver/prices/canonical_prices.parquet; pandas read, source and price columns (this seat)"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W27-S9",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~27",
    "surfaced_at": "2026-10-11T16:48:09Z",
    "one_line": "The bridge at 2026-06-23 links none of the 15 custodian positions: the crosswalk and account_links carry no MATCHED or LINKED row for them; two AWAITING_PERSON near matches and three unapplied exact-units candidates exist, and their served compositions name none of the three CUSIPs.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO-DQ-t35 item 2: the custodian AccountNumber maps to the served account_id and household through the estate's crosswalk; a link is applied only where the estate marks it MATCHED.",
    "world_is": "commonwealth/cottonwood/silver/crosswalk/date=2026-06-23/crosswalk.parquet (1533 rows, 471 MATCHED): the 11 PFORX-holding numbers and the 4 FTHSX-holding numbers are all NOT_MATCHED; <account id removed> AWAITING_PERSON (near match 0.765 to <account id removed>) and <account id removed> AWAITING_PERSON (0.765 to <account id removed>); the others NO_CURRENT_ACCOUNT_HOLDS_POSITIONS or NO_SECURITY_POSITIONS. account_links date=2026-06-23 (1450 rows, 212 LINKED) has none of the 15 numbers. Unapplied exact-units matches on the 2026-10-09 production holdings: <account id removed> FTHSX 35.963 to <account id removed>, <account id removed> FTHSX 52.158 to <account id removed>, <account id removed> FTHSX 39.659 to <account id removed> (no exact match on 2026-06-23). The served platinum/clients composition.json of the four candidate households (z09305579, z09305700, z09305639, z09311697) names none of FTHSX, PFORX or RPIFX in its top 9; detail.json is NoSuchKey.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "aws s3 cp commonwealth/cottonwood/silver/crosswalk/date=2026-06-23/crosswalk.parquet and account_links/date=2026-06-23/account_links.parquet (this seat)",
        "aws s3 cp opal-data-cot/gold/canonical/holdings/2026-10-09.parquet; exact-units test at 0.001 tolerance (this seat)",
        "aws s3 cp opal-data-cot/platinum/clients/<rel>/composition.json for the four candidate households (this seat)"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-S13",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~Q1",
    "surfaced_at": "2026-10-11T16:58:12Z",
    "one_line": "The three funds the cause rule classed wrong-symbol (FTHSX, PFORX, RPIFX) have a median trade-price / daily-close ratio of 1.00 and a 10th-90th percentile spread of about plus or minus 2 to 4 percent, so their trade prices centre on the symbol's close but do not fall inside the 0.5 percent band; no date offset of up to two trading days improves agreement.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "CTO ADDENDUM 4 (msg 4020): the three funds stay unresolved, with a row on whether fund trade prices are comparable to a daily close. ROUND9_LOCK_CAUSE_14.md classed them `wrong-symbol` by the rule (both agreements below 60).",
    "world_is": "2026-10-11 ~17:2xZ, read-only probe (this seat; lock._load_transactions + lock.trade_prices, one paced yahoo_pull.pull per name, scratch pacer): per name, share of trade dates within 0.5 pct of the close shifted by -2..+2 trading days: FTHSX 19.5/23.3/40.7/25.0/18.2 (627 dates), PFORX 38.2/41.9/42.9/42.5/41.7 (513), RPIFX 37.9/39.0/39.2/39.5/38.7 (651); control LCEYX (87.2 pct at lag 0) 51.7/65.4/87.2/65.4/56.4 (211). Median of trade price / same-day close: FTHSX 1.0000, PFORX 1.0001, RPIFX 1.0000; 10th-90th percentile FTHSX 0.974-1.016, PFORX 0.966-1.019, RPIFX 0.960-1.019; LCEYX 0.994-1.000. So lag 0 is the best offset for FTHSX and a flat 38-43 pct for PFORX and RPIFX, and the trade prices centre on the close. What the spread is (fees in Amount, a Quantity or Amount convention, or per-lot NAV timing) was NOT measured, and neither was whether the symbol is the right share class. `wrong-symbol` is the rule's label, not a finding.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "scratchpad lag_probe.py output (this seat, 2026-10-11 ~17:2xZ): FTHSX/PFORX/RPIFX/LCEYX lag table and ratio quantiles",
        "org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/2.0.0_SA_COO~Q1/ROUND9_LOCK_CAUSE_14.md"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-Z-S5",
    "one_line": "TO-DQ-t34's build item 3 (the completing fire records COMPLETE) and its build item 4 (the three existing test_demque_standing_drawer.py tests keep passing UNEDITED) cannot both hold: that t27 test's own fixture completes BOTH its requests on day 2, and it asserts at line 111 that the run outcome is DRAWN and at line 135 that every actuals line is DRAWN. The file is NOT in t34's <paths>.",
    "spec_asserts": "TO-DQ-t34 build 3: 'that run records its ONE line for the request with outcome COMPLETE ... not DRAWN'. TO-DQ-t34 build 4: 'The three existing test_demque_standing_drawer.py tests keep passing unedited.'",
    "world_is": "Built and measured, not predicted. With items 1-3 implemented: AC1 dq_t34_tests.py reads CL-OK (3 of 3 named tests pass) and AC2 dq_t34_close.py reads the expected date-gated 'CLOSE-BAD no COMPLETE row yet (2 rows for the job, 11716 cells drawn)'. But test_demque_standing_drawer.py::test_drawer_draws_min_of_allowance_and_remaining_in_rank_order then FAILS at line 111, 'assert COMPLETE == DRAWN'. The collision is structural and two assertions deep, so no design choice inside the drawer avoids it: line 111 reads the RUN outcome and could in principle be dodged by leaving the run-level field DRAWN, but line 135 asserts {r['outcome'] for r in rows} == {'DRAWN'} over the ACTUALS LINES, which is exactly what item 3 changes. The cause is the fixture's calendar, measured: that test's AAA request ends 2026-01-31 (a Saturday) and its ZZZ request ends 2026-01-04 (a Sunday), so after day 2's draws NO trading day remains in either security's (latest stored, end] window and both requests are COMPLETE under item 1's predicate. The two other t27 tests pass. test_demque_standing_drawer.py is NOT in t34's <paths> (the block grants standing_drawer.py, the NEW test_demque_standing_drawer_close.py, the actuals ledger, the STANDING output folder, change_management, .open_deploys and this channel), so the assignee cannot edit it, and item 4 forbids it anyway. NOTHING WAS WEAKENED AND NOTHING WAS LANDED: the candidate is preserved as org/tier2_senior/0.7.0_AE_CloudOps/deliverables/MDPF_DEMQUE_ZQ_T34_CANDIDATE.patch (7440 B) plus MDPF_DEMQUE_ZQ_T34_test_close.py.candidate (7004 B), and standing_drawer.py was reverted to its HEAD blob d3be03d854a72d7b639a4ef677acb189dbdd9461 with the new test file removed from the collection path, so the shared tree is green (11 passed). THAT REVERT WAS NOT HYGIENE, IT WAS A HAZARD: the registered task mdpf-demque-drawer-daily runs data/mdpf/scripts/demque/standing_drawer.py from the repository root every day at 10:00 ET, so an uncommitted edit sitting on disk would have been executed by the next fire as UNSIGNED code, outside the t34 pair whose site-Z half has not even been requested yet. WHAT IS ASKED: an issuer amendment that either grants test_demque_standing_drawer.py so its two DRAWN assertions can be updated to the new semantics, or re-scopes item 3 (for instance to the per-request line only, which still leaves line 135), or states that the t27 test is superseded. Two incidental findings fixed inside the candidate and not landed: run() wrote its receipt BEFORE computing per-request outcomes, so a COMPLETE line could have disagreed with a DRAWN receipt, and _stored_latest unioned the REAL t24 output folder even for a tmp-dir test, reading production securities into a fixture.",
    "project": "MDPF_DEMQUE",
    "fabric": "site-z",
    "surfaced_by": "0.7.0_AE_CloudOps~ZQ",
    "surfaced_at": "2026-10-11T17:25:00Z",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "disarm_owner": "2.0.0_SA_COO~Q1",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "dq_t34_tests.py -> CL-OK, 3 passed, with items 1-3 implemented",
        "dq_t34_close.py -> CLOSE-BAD no COMPLETE row yet (2 rows, 11716 cells) -- the expected date-gated read",
        "pytest test_demque_standing_drawer.py -> 1 failed, 2 passed; 'assert COMPLETE == DRAWN' at line 111",
        "test_demque_standing_drawer.py:111 run-outcome assertion and :135 {r['outcome'] for r in rows} == {'DRAWN'}",
        "2026-01-31 is a Saturday and 2026-01-04 a Sunday, so both fixture requests reach their end on day 2",
        "t34 <paths> does not list test_demque_standing_drawer.py",
        "candidate preserved: MDPF_DEMQUE_ZQ_T34_CANDIDATE.patch and MDPF_DEMQUE_ZQ_T34_test_close.py.candidate; standing_drawer.py reverted to HEAD blob d3be03d854a72d7b639a4ef677acb189dbdd9461; 11 passed on the reverted tree"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W32-S1",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~32",
    "surfaced_at": "2026-10-12T03:27:24Z",
    "one_line": "The order's 130-request cap assumes one vendor HTTP request per symbol; measured with the counter, a nonexistent ticker costs 8 HTTP requests and each process pays one crumb request, so this order's all-HTTP total is 132 (chart-level 116) and the COO must rule which unit the cap counts.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "batch_equality.py run @ worktree HEAD e2e74649a2 + this commit: per-symbol arm 51 HTTP (50 chart, 1 auth, 0 other); batched arm 58 HTTP (52 chart of which 2 planted, 2 auth, 4 other, statuses 200 x54 and 404 x4), EQUALITY_REPORT.json http_requests and http_detail",
        "exploration (2 symbols AMLP + ZZNOSUCH9Q, default download): 10 HTTP; AMLP alone history(period=max): 2 HTTP = 1 auth (/v1/test/getcrumb) + 1 chart",
        "dq_t40_equal.py AC2 run: spot 5 of 5, http_per_symbol 6 (5 chart + 1 auth), http_batched 5 chart; order total 12 + 109 + 11 = 132 all-HTTP, 116 chart-level",
        "yfinance 1.7.0 data.py _make_request: a status >= 400 switches cookie strategy and re-requests (extra auth + chart), so a 404 costs about four requests"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO BOUNDS: at most 130 symbol-requests across the whole order; cell text: about 938 requests a day, one vendor request per enrolled symbol. The budget arithmetic (20 + 100 + 10) assumes one HTTP request per symbol-call.",
    "world_is": "One real symbol costs one chart request in steady state; the cookie/crumb pair is paid once per process; a nonexistent ticker costs about eight requests (404 retries, quoteSummary timezone lookups). Under the strict all-HTTP unit this order's runs total 132, above 130; under the one-chart-request-per-symbol unit they total 116."
  },
  {
    "id": "MDPF_DEMQUE-D1-W32-S2",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~32",
    "surfaced_at": "2026-10-12T03:27:24Z",
    "one_line": "yfinance download() does not return a symbol's error to its caller: it logs the error on the yfinance logger and returns an empty or NaN frame, so a batched fetch_many must capture errors from the logger to classify FAILED_EMPTY versus FAILED_REFUSED.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "yfinance 1.7.0 multi.py _download_impl: _download_one catches the exception into ctx.errors and sets ctx.dfs[sym] to an empty frame; errors are logged with logger.error('[syms]: err') and not raised",
        "live exploration 2026-10-12: download(['AMLP','ZZNOSUCH9Q'], start=2025-10-01) logged ERROR:yfinance:['ZZNOSUCH9Q']: possibly delisted; no timezone found; the planted symbol came back None, AMLP returned 258 rows",
        "batch_pull.py _ErrorTap (logging handler on 'yfinance') maps 'no data' / 'delist' / 'possibly' to FAILED_EMPTY and any other logged error to FAILED_REFUSED; test_a_symbol_the_vendor_refuses_is_a_failure_for_that_symbol_alone_never_a_price PASSED"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO build item 1: fetch_many is the library's multi-ticker download; a symbol the vendor errors on is a FAILED_REFUSED result for that symbol alone.",
    "world_is": "The library returns the error only through its log and through a missing or empty frame; the error text is not in the return value. The capture is a logging handler on the yfinance logger for the duration of one call, and a later wiring must keep it."
  },
  {
    "id": "MDPF_DEMQUE-D1-W32-S3",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~32",
    "surfaced_at": "2026-10-12T03:27:24Z",
    "one_line": "The 10-symbol measurement in build item 2 was not run as written: the separate 10-symbol download (ii) was dropped to fit the request budget, and the per-symbol count (i) was taken from the proof's first 10 real symbols; the 51-symbol multi-ticker call answers ONE-or-n.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "EQUALITY_REPORT.json http_probe_10: per_symbol_history_calls_first10 chart_requests 10 (ACTHX, LCEYX, VADDX, CNSDX, FFMMX, BISOX, MADVX, FFBOX, CDSIX, CVMIX); one_multi_ticker_call_of_51_symbols chart_requests_total 52, one_per_symbol true",
        "the report's note field: the separate 10-symbol download was not run (request budget)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO build item 2: record, for 10 symbols, the request count of (i) 10 per-symbol history() calls and (ii) ONE multi-ticker download; state whether the multi-ticker call is ONE request or n requests.",
    "world_is": "The multi-ticker call is n requests: one chart request per symbol (yfinance multi.py calls Ticker.history() per symbol), measured on 50 real symbols plus the planted ticker. The 10-symbol download is not in the report; the COO reads the 51-symbol measurement instead."
  },
  {
    "id": "MDPF_DEMQUE-D1-W33-S1",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~33",
    "surfaced_at": "2026-10-12T03:52:00Z",
    "one_line": "The cell's trading_day_ordinal(frontier) is not a function of lib/trading_calendar.py: the module has no ordinal, so extend_frontier.py defines one locally as the NYSE trading-day count from 2020-01-01.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "lib/trading_calendar.py@347c6585ca: the public functions are is_trading_day, prev_trading_day, expected_last_trading_day, trading_days_behind, trading_days_between, trading_days_mtd, trading_days_ytd, total_trading_days_in_window, calendar_source; no ordinal or index function (grep of 'def ' in the worktree file)",
        "data/mdpf/scripts/demque/extend_frontier.py@this order's commit: trading_day_ordinal(day) = len(tc.trading_days_between(ORDINAL_ANCHOR, day)); the block index is ordinal % cycle_trading_days"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "DQ-t-41 build item 3: the block for a day is trading_day_ordinal(frontier) mod cycle, an integer from the trading calendar, so the rotation is stateless.",
    "world_is": "No such function exists at HEAD. The local definition is pure and stateless; the anchor shifts which day each block lands on, not the rotation itself. A calendar-level ordinal would be a lib/ edit outside this order's grant. Owner of that call: 2.0.0_SA_COO~Q1."
  },
  {
    "id": "MDPF_DEMQUE-D1-W33-S2",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~33",
    "surfaced_at": "2026-10-12T03:52:30Z",
    "one_line": "The rolling rule 'not already in the index when enrolled' cannot be evaluated from the live index after the rolling names land, so the enrolment file carries an enrolment-time snapshot the cell's JSON does not name.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "price_store.index on s3://opal-data-assets/yahoo/global/silver/price_history at this order's build: 141 CUSIPs; IRPT_BCKEND-AS-TRADED-CLOSES-878 has 878 unique CUSIPs, 96 of them in the index, 782 not (python read, 2026-10-12)",
        "requests/ENROLMENT_TIERS.json@this order's commit: rolling[0].stored_at_enrolment = the 96 CUSIPs; plan() refuses (SystemExit) a stored CUSIP the request does not carry"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "DQ-t-41 build item 2: rolling = the rolling request's names NOT already in the index when enrolled; the 96 stored ones stay daily.",
    "world_is": "Once a rolling name lands it is in the index, so a rule that reads the live index alone moves all 782 into daily (878 requests a day, over the cap of 380). The fix is the snapshot key in the rolling entry. That key is not in the cell's enrolment JSON: it is a deliberate addition, stated here for the CTO and 2.0.0_SA_COO~Q1 to ratify or replace."
  },
  {
    "id": "MDPF_DEMQUE-D1-W33-S3",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~33",
    "surfaced_at": "2026-10-12T03:53:00Z",
    "one_line": "Build item 6 is stopped: no existing freshness config fits the Yahoo price_history store, which is cusip-partitioned parquet with its as-of per name inside the file, so no entry was added to the served config or the manifest generator.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".tools/comp-freshness _max_partition_date (lines 503-520): reads a YYYY-MM-DD date-key from object names under the prefix; the store has cusip=<CUSIP>/ prefixes with no date-key, so the partition-key check reports PARTITION-KEY UNCHECKED (lines 908-919)",
        ".tools/comp-freshness as_of_field and as_of_map_field (lines 1006, 965): content modes that read a JSON document; the store's files are parquet (lock.json and prices.parquet per CUSIP)",
        "data/served_freshness_config.yaml@347c6585ca: no entry for the Yahoo price store; the only freshness_basis entries are for mdpf, cot, bd and inf artifacts"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "DQ-t-41 build item 6: add ONE freshness entry for the Yahoo price_history store with freshness_basis trading-day-frontier and the lag per tier in its note; if no existing config fits, file a row and stop that item.",
    "world_is": "An entry written now would verdict UNCHECKED on this prefix, or an mtime verdict on a per-name rewrite, which is a false-clean risk. The per-name as-of the rolling tier needs is a schema question for 2.0.0_SA_COO~Q1 and the CTO. Nothing was invented."
  },
  {
    "id": "MDPF_DEMQUE-D1-W33-S4",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~33",
    "surfaced_at": "2026-10-12T03:53:30Z",
    "one_line": "Ten of ADVI_COTBKF's fifteen funds are also IRPT_BCKEND names, so the two tiers overlap; the build resolves it by daily precedence and the cell does not state which tier wins.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python read at this order's build: the ADVI_COTBKF request's 15 CUSIPs against the IRPT_BCKEND request's 878 CUSIPs share 10; 2 of the 15 are in the index",
        "extend_frontier.py _tiers(): a daily_extra CUSIP that has landed is daily even when it is also a rolling name; the day's request holds each CUSIP once; plan-week under --assume-landed IRPT_BCKEND-AS-TRADED-CLOSES-878 gives daily 149, daily_extra_not_landed 5, rolling_names 782"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "DQ-t-41 build item 2: daily = every other indexed name, including the daily_extra funds once landed; rolling = the 782 IRPT names not stored at enrolment.",
    "world_is": "The two rules overlap on the ten funds. The build takes daily precedence, so those funds are requested every day and still count in rolling_names; the ruling on that precedence is the issuer's to confirm."
  },
  {
    "id": "MDPF_DEMQUE-D1-W34-S1",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~34",
    "surfaced_at": "2026-10-12T04:15:45Z",
    "one_line": "The cell names the index row's valid_to as the stored max date and asks the report to print as_of beside it, but as_of is a different column: the max date of the prices rows, not the lock window end.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/price_store.py@1eedfa615e write(): lock.json carries valid_to as the lock window; prices are kept only where date <= valid_to (line 142)",
        "data/mdpf/scripts/demque/price_store.py@1eedfa615e index() lines 170-174: as_of = max(prices.parquet date); valid_to = lk.get('valid_to') from lock.json",
        "read-only ps.index(s3 root) at this order's build, 141 rows: valid_to == as_of on 141 of 141 (127 at 2026-10-09, 14 at 2026-06-23); zero nulls"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "DQ-t-42 build item 2: the stored max date is the index row's valid_to; as_of is printed beside it, and if as_of holds something else the report says so and files a row.",
    "world_is": "The lag is measured from valid_to as specified and the report prints both. The two columns agree on the served store today, so the lag is unaffected now. They differ when a vendor's last bar predates the window end: as_of is then the earlier date and the valid_to lag understates the staleness. The report's docstring states this. Whether the lag basis should be as_of is the issuer's ruling."
  },
  {
    "id": "MDPF_DEMQUE-D1-W34-S2",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~34",
    "surfaced_at": "2026-10-12T04:15:45Z",
    "one_line": "On the served store the rolling tier measures zero names: all 141 indexed names are daily, and the 782 not-stored IRPT names have not landed, so the declared rolling cycle of 5 is checked against no real name.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python extend_frontier.py --lag-report at 1eedfa615e (S3 read only), frontier 2026-10-12: indexed 141, daily names 141 (within 127, over 14), rolling names 0, rolling_not_landed 782",
        "lag_report in extend_frontier.py: each name in _tiers' daily list is daily; rolling = the landed names of the rolling request not stored at enrolment, and none has landed"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "DQ-t-42 AC2: the two tiers partition the indexed names, and the declared rolling cycle is read against the rolling names.",
    "world_is": "The partition holds (141 + 0 = 141), but the rolling tier is unmeasured on real data until the rolling names land. The rolling branch of the report is exercised only by the three tests and the stub store. Nothing was extended or drawn to change this."
  },
  {
    "id": "MDPF_DEMQUE-D1-S14",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~Q1",
    "surfaced_at": "2026-10-12T17:45:34Z",
    "one_line": "Yahoo spells the dotted share classes with a dash (BRK-B, BRK-A, BF-B); the dotted form returns no bar, and no request builder translates it, so a request passes the crosswalk spelling as given.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "IRPT_BCKEND-D2-W310-S3 (routed, msg 4516): seven of the 878 tickers had no bar and the dash spelling for BF-B, BRK-A and BRK-B was never tried. The vendor pull takes a request's `symbol` field as the Yahoo ticker with no translation (yahoo_pull.pull).",
    "world_is": "2026-10-12T17:45:34Z, read-only probe, one request per spelling, 8 to 12 s gaps, nothing stored: BRK-B OK 7,655 rows to 2026-10-12; BRK-A OK 11,738 rows to 2026-10-12; BF-B OK 11,738 rows to 2026-10-12; BRK.B, BRK.A, BF.B each FAILED_EMPTY (the library logs 'possibly delisted; no timezone found'). Scan of every request file and queue file: only IRPT_BCKEND-AS-TRADED-CLOSES-878 carries a dotted symbol (3 of 878). The id had 0 ledger rows, so the 3 symbols were re-spelled in the request file and its queue copy before the first draw (the two copies byte-equal, validate OK, 878 securities, quote counts unchanged: 878 requests, 113,262 cells). The other 4 of the 7 no-bar names are not share classes and are not changed by this row. The lock still decides identity: a spelling that returns another security's bars is rejected by the 90 pct trade-agreement floor.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "probe output in this seat's session 2026-10-12 ~17:5xZ (yahoo_pull.pull per spelling, no pacer state written)",
        "requests/IRPT_BCKEND-AS-TRADED-CLOSES-878.json at the commit that re-spells the three symbols; ~/.opal/demque/ledger.jsonl read: 0 rows for the id"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-S15",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~Q1",
    "surfaced_at": "2026-10-13T14:11:32Z",
    "one_line": "rank.py --probe reads PRICE_NEED_FOR_SECHIST.csv, which the CTO containment ruling moved out of the repo, so the probe cannot run; the daily draw does not depend on it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "PRD C-IDENTITY / FWD-9: the need file feeds the ranking; rank.py NEED_FILE and lock.py NEED_CSV name org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~27/PRICE_NEED_FOR_SECHIST.csv.",
    "world_is": "2026-10-13T14:11:32Z: the file is absent from the tree; ADVI_COTBKF~27's MOVED_ACCOUNT_DATA.md lists it (sha256 abbae517..., 256,054 bytes, byte-copied outside the repo, round 51 CB-ay-1, ruling @0e8209c33c) and only PRICE_NEED_FOR_SECHIST.json (a census summary) remains. In demque/, only rank.need_rows (the --probe path) reads it; lock.NEED_CSV is a constant with no reader. The scheduled draw, the extension and the lock do not read it. DQ-t-43 derives per-security windows from the silver transactions instead.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Glob of org/missions/D8/ADVI/ADVI_COTBKF/deliverables/**/PRICE_NEED_FOR_SECHIST*: only the .json at ~27",
        "grep of demque/*.py for NEED_FILE / NEED_CSV / need_rows: rank.py:42,155,171 and lock.py:32 only"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W35-S1",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~35",
    "surfaced_at": "2026-10-13T14:25:02Z",
    "one_line": "DQ-t-43 orders days_to_finish as 'the whole number of trading days from today to finish_date' without saying whether today counts; the built count excludes today and includes finish_date.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO MDPF_DEMQUE.TO-DQ-t43, --quote line: days_to_finish = the whole number of trading days from today to finish_date.",
    "world_is": "card_a_slice.quote_line counts len(trading_days_between(today + 1 day, finish_date)) at commit 748b73b3ca: the trading days after today up to and including finish_date. On the real P1 slice (2026-10-13 to 2028-02-06, a Sunday) this is 330. A count that includes today would read 331; the finish date is not a trading day, so including or excluding it does not move the figure.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D8/MDPF/MDPF_DEMQUE/task-orders/MDPF_DEMQUE.TO-DQ-t43.card-a-p1-slice-per-security-windows.md: 'days_to_finish = the whole number of trading days from today to finish_date' (no today-inclusion rule stated)",
        "data/mdpf/scripts/demque/card_a_slice.py@748b73b3ca quote_line: days = len(trading_days_between(today + timedelta(days=1), finish))",
        "dq_t43_real.py run 2026-10-13: days=330 finish=2028-02-06 (the --quote line, verbatim)"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W35-S2",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~35",
    "surfaced_at": "2026-10-13T14:25:02Z",
    "one_line": "The P1 living-client slice of the CARD-A need runs 330 trading days to finish under the history backfill, past the 30-day line the round-9 amendment names for a CTO number.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "DECOMP round 9 amendment 8 (DQ-t-43): a number brought to the CTO if P1 alone runs past 30 days; CTO msg 4875: no new spend, the P1 count, cells and days-to-finish printed before the first draw.",
    "world_is": "The P1 slice prices 607 names (609 P1, 2 FDIC placeholders unresolved) at 882,024 cells; finish 2028-02-06, 330 trading days, claim measured. The figure rests on the history backfill at the measured ceiling 5,858 per non-trading day (bbg_allowance.json) and is quoted tier 2. Nothing has been drawn. The 2026-10-09 CARD-A quote priced the full 1,319-name need at 2,317,534 cells (inferred, an upper bound).",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "dq_t43_real.py run 2026-10-13 (rc 0): SLICE-REAL-OK P1 607 names priced, 2 unresolved, 882024 cells, 330 days to finish; p1=609 priced=607 unresolved=2 finish=2028-02-06 claim=measured",
        "data/mdpf/scripts/demque/bbg_allowance.json history.ceiling value 5858 claim measured; history.reserve 7322 held"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W35-S3",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~35",
    "surfaced_at": "2026-10-13T14:25:02Z",
    "one_line": "On dell1 the commit-time client-data check cannot run: the hashed account-id list is absent, so commit 748b73b3ca was not checked for client account ids.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "0.0.0_AB_MSTR",
    "spec_asserts": "CLAUDE.md section 5 and the worker face: account ids never enter a committed file; the commit gate checks client account ids against the hashed list before a commit lands.",
    "world_is": "The gate prints WARN: client-data-check: hashed account-id list ABSENT at C:\\Users\\Test\\.opal\\account_id_hashes.txt, and states the commit was NOT checked (absent is not empty). OPAL_ACCOUNT_ID_HASHES is unset. Until the list is placed, every dell1 commit passes this check unexamined. The commit's own content carries stub account tokens only (A1-A4, B1-B2, G1 in the test file; no account number).",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "safe-commit output for 748b73b3ca (2026-10-13T14:2xZ): WARN: client-data-check: hashed account-id list ABSENT at C:\\Users\\Test\\.opal\\account_id_hashes.txt -- this commit was NOT checked for client account ids",
        "test -e on C:\\Users\\Test\\.opal\\account_id_hashes.txt at 2026-10-13T14:25:02Z: ABSENT (rc=1); OPAL_ACCOUNT_ID_HASHES unset; the directory C:\\Users\\Test\\.opal exists"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W36-S1",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~36",
    "surfaced_at": "2026-10-13T14:56:32Z",
    "one_line": "The ABNB model-block request declares window_start 2016-01-01 and need_date 2026-10-09; the 365-day non_client rule refuses it, so AC2 arm 1 cannot pass as written.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "spec_asserts": "TO DQ-t-44 step 4: AMGT_RESAPP-107a-ABNB-MODEL-BLOCK is declared non_client, need_date 2026-10-09, window_start = the producer's HIST_START. If the rule refuses it, do not weaken the rule: file a BLOCKING row and leave the file declared as read. AC2 arm 1 requires refused == [].",
    "world_is": "integrations/bloomberg/research/model_block_pull.py line 313 reads HIST_START = \"2016-01-01\". bbg_quote.py --check-declared on the requests folder returns checked 8, accepted 7, refused [AMGT_RESAPP-107a-ABNB-MODEL-BLOCK: non_client window_start 2016-01-01 is more than 365 days before need_date 2026-10-09]. The request is not drawn and the rule is unchanged. The window that the rule admits is 2025-10-09 onward; re-windowing or dropping the request is the owner's call.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "dq_t44_real.py run 2026-10-13 on dell1: arm1 checked=8 accepted=7 refused=['AMGT_RESAPP-107a-ABNB-MODEL-BLOCK']; CLASS-REAL-BAD arm1 (rc 1)",
        "integrations/bloomberg/research/model_block_pull.py line 313 HIST_START = \"2016-01-01\" (read at worktree base 47a0cf6d33)"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W36-S2",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~36",
    "surfaced_at": "2026-10-13T14:56:32Z",
    "one_line": "bbg_backfill.py draws the TR request from its request start to its end per security with no stored-row check, so a run outside its one-shot folder re-draws in-window rows; the identity remainder does not reach it.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~Q1",
    "spec_asserts": "TO DQ-t-44 step 5: the drawer prices and draws the remainder as the undrawn (security, date) rows inside the request window, never quoted cells minus drawn cells; a stored row is never re-drawn.",
    "world_is": "bbg_backfill.py run() (lines 106-108) loops every security from request['start'] to request['end'] in calendar windows and reads no stored parquet row. The TR request now starts 2025-10-09, and KO, JNJ, T and VZ are fully stored inside that window in MDPF_DEMQUE_ZQ_T24 and MDPF_DEMQUE_ZQ_STANDING. Its only guard is the one-shot marker run.started.json. Nothing was run in this cell: no Bloomberg call, no write.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/bbg_backfill.py lines 99-108 (base 47a0cf6d33): per-security loop from request start to request end, no parquet read",
        "standing_drawer.py --plan --request DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS on dell1 2026-10-13: remaining_cells 1004 for MO and XOM; KO, JNJ, T, VZ have 251 stored in-window days each"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W36-S3",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~36",
    "surfaced_at": "2026-10-13T14:56:32Z",
    "one_line": "Seventeen existing demque tests outside this order's seven-file grant build undeclared Bloomberg requests and now fail the need-class refusal; only the grant's files can take a stub declaration.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "spec_asserts": "TO DQ-t-44: existing demque test files keep passing; if one needs a stub request to carry the new declarations, change only that stub and nothing else in the file. The grant names test_demque_bbg, test_demque_card_a_slice, test_demque_standing_drawer and three others, not these.",
    "world_is": "Failing with 'request ... refused by the need-class rule: need_class None is missing' (bbg_quote._validate). Counts: test_demque_ceiling.py 1; test_demque_nontrading.py 2; test_demque_quote_remaining.py 3; test_demque_refreeze.py 3; test_demque_reserve.py 1; test_demque_reserve_ledger.py 1; test_demque_tier_quote.py 3; test_demque_standing_drawer_close.py 3. The refusal is the rule working as written; nothing was weakened. The stubs need need_class and window_start, which the COO must grant.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python -m pytest data/mdpf/scripts/demque -q on dell1 2026-10-13 (worktree 47a0cf6d33 plus this order's edits): 24 failed, 131 passed; baseline 151 passed",
        "failure lines: need_class None is missing o... at bbg_quote.py:235 for each listed file"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W36-S4",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~36",
    "surfaced_at": "2026-10-13T14:56:32Z",
    "one_line": "Four test_demque_bbg_backfill.py tests use the TR request as their fixture and pin its old 2021-10-01 window; the re-windowed request draws 4380 cells, not 5858, and the vendor-limit tests read no parquet.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "spec_asserts": "TO DQ-t-44 step 4: the TR request moves start to 2025-10-09 with window_trim. The existing demque tests keep passing.",
    "world_is": "test_backfill_stops_at_the_days_allowance[0] and [10]: assert 4380 == 5858; the stub returns one calendar row per day over 2025-10-09..2026-10-08 for 6 securities x 2 fields, which is 365 x 6 x 2 = 4380, so the window exhausts before the allowance binds. test_backfill_stops_on_a_vendor_limit_warning[field] and [response]: pyarrow NoneType, no parquet. The test file is outside the grant.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python -m pytest data/mdpf/scripts/demque -q on dell1 2026-10-13: test_demque_bbg_backfill.py 4 FAILED (assert 4380 == 5858; assert 4380 == 5848; pyarrow NoneType x2)",
        "data/mdpf/scripts/demque/bbg_backfill.py line 19 REQUEST = requests/DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS.json"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W36-S5",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~36",
    "surfaced_at": "2026-10-13T14:56:32Z",
    "one_line": "Two test_demque_card_a_slice.py tests assert the superseded P1 window (2013-04-03 floor, 2026-06-23 end, NOLATE001 unresolved); the order changes all three, so both fail until the grant updates their assertions.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "spec_asserts": "TO DQ-t-44 step 6: the P1 window starts at max(first Trade_Date, 2012-01-01) and ends at the frontier for a held name, its last Trade_Date for a sold one; the request declares need_class client.",
    "world_is": "test_the_p1_slice_lists_priced_names_in_rank_order...: assert '2012-01-05' == '2013-04-03' (the floor is now 2012-01-01). test_a_p1_name_with_no_trades_or_no_bloomberg_cusip...: NOLATE001 trades on 2026-07-01 and 2026-08-01 fall before the frontier 2026-10-13, so it is priced, not unresolved. The real P1 quote reads window_end 2026-10-13.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python -m pytest data/mdpf/scripts/demque/test_demque_card_a_slice.py -q on dell1 2026-10-13: 2 failed",
        "card_a_slice.py --priority P1 --out .scratch/card_a_p1.json --quote (dell1, read-only S3): window_end 2026-10-13, p1_names 609, priced_names 607, unresolved_names 2"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W36-S6",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~36",
    "surfaced_at": "2026-10-13T14:56:32Z",
    "one_line": "test_demque_standing_drawer.py test_drawer_draws_min_of_allowance_and_remaining_in_rank_order asserts quoted minus drawn (20 more cells for AAA); the identity rule draws 16 cells, so the test fails on its second-day assertion.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "spec_asserts": "TO DQ-t-44 step 5: the remainder is the undrawn in-window (security, date) rows, never quoted cells minus drawn cells. Existing tests keep passing, with stub changes only.",
    "world_is": "The stub returns one calendar row per day, and the 60-cell quote is a fixture figure, so no trading-day identity reproduces the asserted 20 (or 28 in total). The run reads DRAWN with cells_drawn 16. Changing the assertion is beyond a stub change. The COO or CTO decides whether the fixture or the test moves.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python -m pytest data/mdpf/scripts/demque/test_demque_standing_drawer.py -q on dell1 2026-10-13: AssertionError outcome DRAWN cells_drawn 16 (expected COMPLETE, cells 20 then 28)",
        "data/mdpf/scripts/demque/standing_drawer.py _draw_request and undrawn_runs (this order's edit)"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W36-S7",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~36",
    "surfaced_at": "2026-10-13T14:56:32Z",
    "one_line": "The P1 held rule reads only the by and sl codes: 420 of 607 priced names read as sold and end at their last trade, and 403 of those carry other position codes (lo, li, trfi, trfo) whose meaning is not verified.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO DQ-t-44 step 6: held is net quantity, buys minus sells over every account, positive at the last transaction; a transactions frame with no sign makes every name held and the claim inferred.",
    "world_is": "Read-only S3 on dell1, 2026-10-13: codes are lowercase; by has 178,889 rows and sl has 147,895, each with unsigned non-negative Quantity. Of the 607 priced P1 names, 187 read held (end = FRONTIER) and 420 read sold (end = last trade). Of the 420 sold, 403 carry another code: lo 30,977 rows, li 19,749, man 19,753, dv 9,186, trfi 1,355, trfo 1,346. The P1 cells fall from 882,024 (2013 floor, end 2026-06-23) to 500,314 (2012 floor, frontier or last trade); held_claim is measured per the rule. If lo, li, trfi or trfo move a position, the sold windows are cut short. Not decided here.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "card_a_slice.py --priority P1 --quote on dell1 2026-10-13: cells 500314, days_to_finish 184, finish_date 2027-07-10, held_claim measured",
        "read-only transaction code census via rank.load_transactions (S3), dell1 2026-10-13, scratch script only"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W36-S8",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~36",
    "surfaced_at": "2026-10-13T14:56:32Z",
    "one_line": "ADVI_COTBKF-TIER2-15-FUNDS-AS-TRADED-20261012.json carries a securities list but no vendor and no channel, so the Bloomberg check skips it and quote() cannot read it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO DQ-t-44 step 3: --check-declared runs over every request with a securities list and vendor bloomberg, or no vendor and a Bloomberg channel.",
    "world_is": "The file has no vendor and no channel key. The check reads it as not Bloomberg and skips it, and bbg_quote.quote would raise request missing 'channel'. It is not one of the TO's ten files and was not declared. The owner should confirm its vendor; the Yahoo side is outside this cell.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "requests/ADVI_COTBKF-TIER2-15-FUNDS-AS-TRADED-20261012.json read at base 47a0cf6d33: keys include securities (list of 15) and no vendor or channel",
        "bbg_quote.check_declared output on dell1 2026-10-13: checked 8 (this file not among them)"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W36-S9",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~36",
    "surfaced_at": "2026-10-13T14:56:32Z",
    "one_line": "The TR request's quote file still prices the superseded 2021 window at 15,720 cells; the drawer's open gate reads it, and the remainder no longer follows it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Andrew-direct 2026-10-13 ADDENDUM 2: current requests are re-priced on the new windows before their next draw.",
    "world_is": "DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS.quote.json carries cells 15720 for 2021-10-01..2026-10-08. standing_drawer --plan gives remaining_cells 1004 by identity for 2025-10-09..2026-10-08. The quote file is outside this grant and was not rewritten.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "requests/DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS.quote.json at base 47a0cf6d33: cells bloomberg_history 15720",
        "standing_drawer.py --plan --request DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS on dell1 2026-10-13: remaining_cells 1004, window_start 2025-10-09"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W36-S10",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~36",
    "surfaced_at": "2026-10-13T15:26:42Z",
    "one_line": "The drawer test's calendar-row stub leaves AAA's 29 and 30 January owed by identity after the second fire, so the test's COMPLETE pin reads DRAWN; the 16-cell figure holds.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO DQ-t-44 AMENDED S5: change test_drawer_draws_min_of_allowance_and_remaining_in_rank_order to the identity remainder (16 cells, not quoted minus drawn); every other assertion stays.",
    "world_is": "The test's Stub returns one row per CALENDAR day up to the cap. Day 1 stores AAA 2026-01-02..01-21; day 2 draws 14 cells (22, 23, 26, 27, 28 Jan) and stops at the cap, so 29 and 30 Jan are trading days still owed and AAA reads DRAWN, not COMPLETE. ZZZ reads COMPLETE with 2 cells; the run total is 16. The vendor returns trading days only, so on a trading-day vendor this fixture would close AAA on day 2; the difference is the stub, not the drawer. The test now pins AAA DRAWN and ZZZ COMPLETE.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "scratch probe on dell1 2026-10-13 (base c01f633404 plus this order's edits, removed after use): day 2 cells_drawn 16, outcome DRAWN, requests AAA-FIRST 14 DRAWN and ZZZ-SECOND 2 COMPLETE; stored AAA dates end 2026-01-28",
        "data/mdpf/scripts/demque/standing_drawer.py undrawn_runs and _draw_request at c01f633404 (identity over trading days)"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W36-S11",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~36",
    "surfaced_at": "2026-10-13T15:26:42Z",
    "one_line": "The standing-drawer close tests' calendar-row stub spent the drawer's cap on weekend rows, so the identity remainder closed nothing on the first fire; their Stub now returns trading days only, as the vendor does.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO DQ-t-44 step 4 and AMENDED S3 to S6: the named files take declarations on their stubs; change only what a failure requires, every other assertion stays.",
    "world_is": "test_demque_standing_drawer_close.py: with declarations added, three tests failed. The first fire drew 40 cells of 20 rows (2026-01-02..01-21 calendar rows) and left trading days 22 to 30 Jan owed, so the request read DRAWN, not COMPLETE. The Stub now yields the trading days inside the cap (sd.is_trading_day). The assertions are unchanged; one comment's figure was corrected from 60 calendar rows to 20 trading rows. All three pass.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python -m pytest data/mdpf/scripts/demque/test_demque_standing_drawer_close.py -q on dell1 2026-10-13: before the Stub change 3 failed (DRAWN for COMPLETE; 2 == 1 closes); after it 3 passed",
        "data/mdpf/scripts/demque/test_demque_standing_drawer_close.py Stub at c01f633404 (calendar rows) and after this order's edit (trading rows)"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W36-S12",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~36",
    "surfaced_at": "2026-10-13T15:26:42Z",
    "one_line": "card_a_slice reads its transaction sign table from data/assets/scripts/silver/commonwealth_signs.py, outside the grant and read only; the P1 held rule now reads lo, li, trfi and trfo, and the real P1 quote moves from 500314 to 471522 cells.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "AMENDED S7: classify each Transaction_Type as adds-to or removes-from a position from the source; a code that cannot be classified leaves the name HELD and the printed held_claim inferred.",
    "world_is": "commonwealth_signs.py (ADVI_COTBKF CB-m-1) is the one Commonwealth sign table: PLUS_TYPES (by, li, LISU, lica, trfi, TRFIR, trci, dvr, ci, cs, so, LOX, QA, CAF, CAE, 12b1) add; MINUS_TYPES (sl, lo, loca, trfo, trco, ss, si, BYX, LIX, pyd, leu, DVRX) remove; NO_SHARE_MOVEMENT (dv, man, int, ...) moves no shares. card_a_slice imports it and matches case-blind. On the real table no code is unclassified, so held_claim is measured. docs/data/transaction_type_canonical_reference.md is the Black Diamond taxonomy and names no Commonwealth code. P1 --quote on dell1 2026-10-13: cells 471522, days_to_finish 175, finish_date 2027-06-26, window_end 2026-10-13 (S7 measured 500314 with by and sl only).",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "card_a_slice.py --priority P1 --out .scratch/p1_slice_request.json --quote on dell1 2026-10-13 (read-only S3): held_claim measured, priced_names 607, unresolved_names 2",
        "data/assets/scripts/silver/commonwealth_signs.py SIGN, PLUS_TYPES, MINUS_TYPES and NO_SHARE_MOVEMENT at c01f633404"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W37-S1",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~37",
    "surfaced_at": "2026-10-13T15:29:12Z",
    "one_line": "The CARD-A P1 slice prices CFNCASH, a cash identifier and not a CUSIP; the placeholder rule (FDIC plus digits) does not catch it, so it adds 3,326 needed cells to the P1 draw.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~Q1",
    "spec_asserts": "data/mdpf/scripts/demque/card_a_slice.py@6293183101 lines 13-14 and 51: a name is unresolved only when it has no trade in the window or its CUSIP is a cash-sweep placeholder shaped FDIC plus digits; every other P1 name is priced over its window (worker face: 609 P1, 607 priced, the 2 FDIC placeholders unresolved).",
    "world_is": "CFNCASH is ranked 571 of 1,319 at P1 and pursued in MDPF_SECHIST-CARD-A-COT-BBG-HISTORY.quote.json, so card_a_slice.build prices it over 2013-04-03..2026-06-23: 3,326 trading days, inside the 882,024 window cells. It is a cash line, not a Bloomberg-priceable security. Nothing was drawn; the next P1 draw would quote it.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "p1_coverage.py run 2026-10-13 at 6293183101 (rc 0): per_cusip row cusip CFNCASH, yahoo_class no_symbol, needed_days 3326, uncovered_days 3326; window_cells 882024 equals the card_a_slice merge figure",
        "MDPF_SECHIST-CARD-A-COT-BBG-HISTORY.quote.json ranked: CFNCASH rank 571 priority P1 pursued true (python read, 2026-10-13)"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W37-S2",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~37",
    "surfaced_at": "2026-10-13T15:29:12Z",
    "one_line": "47 gold holdings daily files (2026-04-22..2026-06-05, source bd) carry no cusip column, so their Black Diamond rows cannot be priced per CUSIP and those days stay in the residual.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "DQ-t-46 input list: Black Diamond units and value per CUSIP and held date from s3://opal-data-cot/gold/canonical/holdings/YYYY-MM-DD.parquet, exact price = market value over units per CUSIP and day.",
    "world_is": "The daily files dated 2026-04-22 to 2026-06-07 (47 files, source bd) hold ten columns (date, one account column, asset_name, units, price, market_value, source, bd_units, schwab_units, ticker) and no cusip. The cusip column appears from 2026-06-08 (88 files, source bd_snapshot); all 120 trading days of 2026-04-22..2026-10-12 have a daily file. Only ticker and asset_name identify the early rows; a ticker-to-CUSIP map was not built because it would be an inference. The early days are uncovered in the residual.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "schema read of all 135 gold/canonical/holdings parquet files, 2026-10-13 (rc 0): 47 without cusip (source bd), 88 with cusip (source bd_snapshot), first cusip file 2026-06-08",
        "trading_days_between 2026-04-22..2026-10-12 = 120 days, missing gold daily files on trading days = 0"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W37-S3",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~37",
    "surfaced_at": "2026-10-13T15:35:38Z",
    "one_line": "The DQ-t-46 output key bd_units_value, which the AC2 check reads, is a refused naming token; the naming gate refuses it, so the module prints blackdiamond_units_value and AC2 reads COVER-REAL-BAD.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~Q1",
    "spec_asserts": "DQ-t-46 cell and AC2 (dq_t46_real.py): p1_coverage.py prints one JSON line carrying the key bd_units_value and per-CUSIP bd_held_days; the worker face names the block Black Diamond units and value.",
    "world_is": "org/standards/NAMING_SCHEMA.json refused_tokens: bd is refused in every slot (the vendor is blackdiamond; the firm is 49financial). The naming gate refused the first commit of the module (13 graded lines, every bd carrier and the bucket alias). The module as committed at aa3b2100ee prints blackdiamond_units_value and blackdiamond_held_days; dq_t46_real.py at aa3b2100ee returns COVER-REAL-BAD arms=ints,bd,residual. The check was not edited and the key was not kept.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "safe-commit naming limb, first attempt 2026-10-13: NAMING-GATE REFUSE 13 graded (bd carriers at p1_coverage.py lines 139-154 and test lines 45-72; bucket alias at line 54); second attempt after the rename: committed aa3b2100ee",
        "dq_t46_real.py run at aa3b2100ee 2026-10-13 (rc 1): COVER-REAL-BAD arms=ints,bd,residual; the check reads d.get bd_units_value",
        "org/standards/NAMING_SCHEMA.json refused_tokens.bd: refused in EVERY slot; the vendor is blackdiamond"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W37-S4",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~37",
    "surfaced_at": "2026-10-13T15:51:46Z",
    "one_line": "The amended cash-identifier rule refuses any identifier that is not 9 alphanumeric characters, so two existing card_a_slice test fixtures (LO00000001, OK00000009; 10 characters each) would be refused; they were renamed to the 9-character LO0000001 and OK0000009.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Order DQ-t-46 AMENDED 2026-10-13 (ruling on rows D1-W37-S1): a name whose identifier is not exactly 9 alphanumeric characters is UNRESOLVED with reason cash_identifier; change only what the rule requires in existing tests (only the placeholder reason assertion is named).",
    "world_is": "data/mdpf/scripts/demque/test_demque_card_a_slice.py at 010cb17a67 used the 10-character identifiers LO00000001 (test_the_p1_slice_lists_priced_names_in_rank_order) and OK00000009 (test_a_p1_name_with_no_trades_or_no_bloomberg_cusip_is_listed_unresolved_and_never_quoted). Under the rule both would be unresolved, so their P1 assertions could not pass as written. The fixtures were renamed to LO0000001 and OK0000009 (9 characters); no assertion other than the placeholder reason string changed.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python length check 2026-10-13: LO00000001 10, OK00000009 10, LO0000001 9, OK0000009 9",
        "python -m pytest data/mdpf/scripts/demque/test_demque_card_a_slice.py at the worktree after the rule: 4 passed (rc 0)"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W38-S1",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~38",
    "surfaced_at": "2026-10-13T15:49:02Z",
    "one_line": "The device queue copy of the standing extension request (STANDING-T1-EXTEND-2026-10-12) carries no need_class and no window_start, so AC2 arm 1 (--check-declared over the device queue) refuses it; the other six queue Yahoo requests are declared.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "spec_asserts": "TO DQ-t-45 THE CELL and Decomp round 9: the six Yahoo requests in the repo and the device queue are ALREADY declared by the issuer (need_class and window_start); the worker edits no requests/*.json; AC2 arm 1 requires refused == [] over the device queue.",
    "world_is": "~/.opal/demque/queue/Z-STANDING-T1-EXTEND.json (keys end, fields, page, reason, request_id, securities, start, tier; request_id STANDING-T1-EXTEND-2026-10-12; 141 securities) is undeclared: it was written by the previous day's extend_frontier --apply before the declaration existed. demand_queue.py --check-declared on that queue prints checked 7, accepted 6, refused [STANDING-T1-EXTEND-2026-10-12]. The file is outside the repo and the grant forbids writing the queue directory; the next scheduled run_daily_draw.sh runs extend_frontier --apply first, which rewrites this file declared (the apply path builds it through _request), so the refusal clears at that run and not before.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python data/mdpf/scripts/demque/demand_queue.py --check-declared ~/.opal/demque/queue on dell1 2026-10-13 (worktree 86abd8733d plus the DQ-t-45 edit): {checked 7, accepted 6, refused STANDING-T1-EXTEND-2026-10-12}",
        "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t45_real.py arm1 queue: refused or too few checked (YCLASS-REAL-BAD)",
        "data/mdpf/scripts/demque/run_daily_draw.sh@86abd8733d runs extend_frontier.py --apply before daily_draw.py --queue"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W38-S2",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~38",
    "surfaced_at": "2026-10-13T15:49:02Z",
    "one_line": "redraw_stale.enqueue builds a Yahoo request with no need_class or window_start and calls demand_queue.validate, so DQ-t-45's refusal breaks it; the file is outside the grant, so both of its tests fail and redraw_stale --apply would reset the pacer and then refuse to enqueue.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~Q1",
    "spec_asserts": "TO DQ-t-45 BOUNDS: the grant is demand_queue.py, extend_frontier.py, test_demque_yahoo_need_class.py, the test_demque_*.py stub declarations, and the investigation file; the folder runs with 0 failed (156 passed plus 3). Existing demque tests take a stub declaration and nothing else.",
    "world_is": "data/mdpf/scripts/demque/redraw_stale.py enqueue (line 98-102 at 86abd8733d) builds {request_id DEMQUE-S8-REDRAW-<day>, tier 2, reason, page, securities, fields close, start, end} with no need_class or window_start, then calls dq.validate(req). The refusal now raises before the file is written. test_demque_redraw_stale.py test_resets_exactly_those_symbols_in_the_pacer_and_enqueues_one_request and test_second_run_with_no_stale_files_enqueues_nothing fail on the production enqueue, not on a stub, so no stub declaration can clear them. In main() reset_pacer runs before enqueue, so a redraw_stale --apply after this change resets the pacer entries and then raises with no request queued. The folder runs 157 passed, 2 failed.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python -m pytest data/mdpf/scripts/demque -q on the worktree 86abd8733d plus the DQ-t-45 edit: 2 failed, 157 passed (both failures ValueError need-class rule at bbg_quote.py:235 raised from demand_queue.validate via redraw_stale.enqueue)",
        "data/mdpf/scripts/demque/redraw_stale.py@86abd8733d lines 98-108 (enqueue) and 132-133 (main: reset_pacer before enqueue)"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W38-S3",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~38",
    "surfaced_at": "2026-10-13T15:49:02Z",
    "one_line": "extend_frontier.apply returns early without writing when the plan names no securities, so a stale undeclared standing file can stay in the queue, and demand_queue.draw then refuses the whole queue on it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO DQ-t-45 BUILD 3: extend_frontier._request declares need_class client and window_start; the standing extension declares itself. The spec does not cover the empty-plan branch of apply.",
    "world_is": "extend_frontier.py apply (line 407-409 at 86abd8733d) returns {request: None} without rewriting Z-STANDING-T1-EXTEND.json when plan securities are empty. The old undeclared file then stays in the queue. demand_queue._load_requests calls validate on every queue file, so daily_draw's draw raises ValueError on that file and the run exits nonzero before any pull. Reachable only when no locked name has landed; not seen on dell1 2026-10-13, where the plan names 183 symbols.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "INFERRED",
      "evidence": [
        "data/mdpf/scripts/demque/extend_frontier.py@86abd8733d apply: if not p[\"securities\"]: return without a write",
        "data/mdpf/scripts/demque/demand_queue.py _load_requests calls validate on every queue *.json (DQ-t-45 worktree edit)"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W38-S4",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~38",
    "surfaced_at": "2026-10-13T16:07:55Z",
    "one_line": "DQ9-t45-AC2 arm 2 runs extend_frontier.py --plan under a 58-second subprocess budget, and the plan takes about 77 seconds on dell1, so arm 2 times out with no verdict line on the first run and on the one retry.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "spec_asserts": "TO DQ-t-45 DQ9-t45-AC2: python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t45_real.py -> YCLASS-REAL-OK; the standing extension's plan declares client from a window start on or after 2012-01-01.",
    "world_is": "At 82fc16c19d, the check's arm 2 (dq_t45_real.py line 42, _line(extend_frontier.py --plan, timeout=58)) raised subprocess.TimeoutExpired on the first run and on the single retry (rc=1, no YCLASS-REAL line). A direct timed run, timeout 120 python data/mdpf/scripts/demque/extend_frontier.py --plan, returned rc=0 in 77 seconds with need_class client, window_start 2013-04-08, start 2013-04-08, frontier 2026-10-13, symbols 183. Arm 1 passes on the same run (requests 2 of 2 accepted; queue 7 of 7 accepted). The plan's content meets the criterion; the check's 58-second budget is shorter than the plan's measured read time. The check was not edited and its budget was not raised: it is outside the grant and the bound forbids weakening a check.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t45_real.py:42 timeout=58 on the --plan arm",
        "timeout 120 python data/mdpf/scripts/demque/extend_frontier.py --plan at 82fc16c19d: rc=0, elapsed 77s, window_start 2013-04-08",
        "python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t45_real.py at 82fc16c19d, two runs: TimeoutExpired after 58 seconds"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W40-S1",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~40",
    "surfaced_at": "2026-10-13T16:46:29Z",
    "one_line": "The append path keeps the stored lock; a full re-lock on the same transactions differs on 2 of 50 names (LCEYX, FTHSX): the served record is LOCKED with claim held under a below-floor claim_reason, the re-lock is REJECTED:LOW_TRADE_AGREEMENT with claim measured.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO DQ-t-48 THE CELL item 1: on append the lock valid_to is extended to the frontier with claim and trades_through unchanged; the docstring must say why that equals a full re-lock on a no-split day, or name the difference in a surprise row.",
    "world_is": "incremental_equal.py --n 50 at frontier 2026-10-12 (report lock_record: compared 50, differences 6). LCEYX (cusip 00141B204) and FTHSX (cusip 14064D865) served lock.json: state LOCKED, claim held, claim_reason 'below the 90 pct floor (row MDPF_DEMQUE-D1-S9); cause under measurement', trades_through null, observations 211/184 and 627/255. lock.check over the full history on the same transactions: state REJECTED:LOW_TRADE_AGREEMENT, claim measured, trades_through 2020-02-24 and 2026-06-02. The other 48 names agree on every lock field. The daily draw re-locks each pulled name (daily_draw.py line 88), and a re-lock over the 5-day window would count only the trade dates its pulled prices cover (lock.py line 88 inner join), so the append path cannot re-prove the identity on five days. incremental_append keeps the stored lock by design and says so in its docstring.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~40/INCREMENTAL_EQUALITY_REPORT.json no_split_arm.lock_record (compared 50, differences 6)",
        "served lock.json of cusip 00141B204 and cusip 14064D865 in the price store (price_store.s3_root(), read 2026-10-13T16:4xZ)",
        "data/mdpf/scripts/demque/daily_draw.py@83c3920c82 line 88: lock.check on each pulled name",
        "data/mdpf/scripts/demque/lock.py@83c3920c82 line 88: trades inner-joined to prices"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W40-S2",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~40",
    "surfaced_at": "2026-10-13T16:46:29Z",
    "one_line": "The append path returns PRICE_COLS only; price_store.write stores TR_COLS (cash, total_return, tr_source, flags) beside them, and a new row's TR needs the stored max close as its prior close, so a wiring order must add the TR step before an append can be written to the served store.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO DQ-t-48 THE CELL item 1: apply_incremental returns the new price rows with close_served and as_traded_close computed as yahoo_pull.pull computes them; no TR column is named.",
    "world_is": "price_store.py@83c3920c82 line 25 defines TR_COLS; line 141 merges tr_column.build and keeps PRICE_COLS + TR_COLS; lines 150-156 write prices.parquet with those columns. tr_column.py@83c3920c82 line 66 build() computes daily_tr over the full close series with the dividends, so the first new row needs its prior close. incremental_append.py returns no TR column (named in its COLUMNS docstring). The compared cells (prices, dividends, splits) exclude TR, so AC3 is silent on it.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/price_store.py@83c3920c82 lines 25, 141, 150-156",
        "data/mdpf/scripts/demque/tr_column.py@83c3920c82 line 66 (build)",
        "data/mdpf/scripts/demque/incremental_append.py (this order's commit): append returns PRICE_COLS, dividends, splits, lock"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W40-S3",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~40",
    "surfaced_at": "2026-10-13T16:46:29Z",
    "one_line": "The order says to merge box/dell1 into the worker branch before appending rows; the worker standing rule forbids a merge, so the worker did not merge, appended its rows on its own branch, and leaves the merge to the drain.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO DQ-t-48 REFUSAL CLAUSE: 'first MERGE box/dell1 into your branch, never rebase, before you append rows'.",
    "world_is": "The worker standing rules say never push, merge, rebase, checkout or clean. HEAD 83c3920c82 is an ancestor of box/dell1 (3a14a2a55d), and INVESTIGATION_v1.md is identical between the two (git diff empty), so appending on this branch cannot conflict now. A merge would fast-forward the whole worker branch to the box's tree, so none was run. A later box/dell1 append at the same offset will conflict, which the drain resolves.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git merge-base --is-ancestor 83c3920c82 box/dell1 succeeded at 2026-10-13T16:46Z",
        "git diff 83c3920c82 box/dell1 -- org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md: empty"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W41-S1",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~41",
    "surfaced_at": "2026-10-13T17:22:57Z",
    "one_line": "The order says to merge box/dell1 into the worker branch before appending rows; the worker standing rule forbids a merge, so this worker did not merge (same finding as MDPF_DEMQUE-D1-W40-S3) and appended its row on its own branch.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO DQ-t-49 REFUSAL CLAUSE: 'Merge box/dell1 into your branch (a merge, never a rebase) before you append rows'.",
    "world_is": "The worker standing rules say never push, merge, rebase, checkout or clean. box/dell1 (05874c6522) is 17 commits ahead of the worker branch merge-base 932f896786, and the investigation file is identical between HEAD and box/dell1 (git diff --stat HEAD box/dell1 empty), so the append cannot conflict now. No merge was run; the drain reconciles the row against box/dell1.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git diff --stat 932f896786 box/dell1 -- investigations/INVESTIGATION_v1.md: empty at 2026-10-13T17:22Z",
        "git rev-list --count HEAD..box/dell1: 17"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W41-S2",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~41",
    "surfaced_at": "2026-10-13T17:22:57Z",
    "one_line": "A held window that starts before 2012-01-01 cannot be requested as written: bbg_quote._validate refuses a security start before the floor, so porting_test.py clamps the draw window start to 2012-01-01 (held_window). No current name is affected.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO DQ-t-49 BUILD step 1: draw the 5 intervals inside each security's held window [valid_from, valid_to]; the request validates under bbg_quote._validate.",
    "world_is": "bbg_quote._check_window refuses any security start before WINDOW_FLOOR 2012-01-01. The real index (index/index.parquet, 326 rows) has min valid_from 2013-04-08, so the clamp changes no draw today: the request has window_start 2013-05-10 and 2497 cells. The clamp is a worker choice the order did not state; the alternative (drop such names) was not taken.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/porting_test.py held_window() at worker HEAD (this commit)",
        "data/mdpf/scripts/demque/bbg_quote.py _check_window: WINDOW_FLOOR 2012-01-01 refusal",
        "real index read 2026-10-13: 326 rows, min valid_from 2013-04-08, max valid_to 2026-10-12"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W42-S1",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~42",
    "surfaced_at": "2026-10-13T17:32:49Z",
    "one_line": "The $1.00 money market skip matches no priced name: the rule (MONEY MARKET in the name AND cash_equivalent true) selects 0 of 606, so the two Fidelity money market CUSIPs are read and pulled.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO DQ-t-50 BUILD step 2, cash-equivalent rule: a name whose text contains MONEY MARKET (case blind) and whose cash_equivalent flag is true is SKIPPED; every other cash equivalent, including an UNREAD one, is pulled.",
    "world_is": "Of 227 priced Cash Equivalent names, 33 are in the held snapshot, all with cash_equivalent false, and 194 are absent (UNREAD, pulled). The snapshot rows with flag true are 973 over 2 CUSIPs (CASH and 316067107), neither priced, so 0 names are skipped. Two Fidelity money market CUSIPs are pulled as read-but-not-skipped: 316175108 (name FIDELITY COLCHESTER STR TR MNY MRKT FDS I, flag false, 21 rows) and 316175207 (FIDELITY COLCHESTER STR TR MONEY MKT CL I, flag false, 1 row). The rule as written does not reach its intent; the issuer decides the rule text. The request is built as written (skipped 0, unread pulled 194).",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "b1_request.py --build at 1dcdbbde7d (S3 read only): skipped_one_dollar 0, unread_pulled 194, priced_names 606, securities 614",
        "held snapshot silver/cot_holdings.parquet: CUSIP 316175108 and 316175207 rows carry cash_equivalent false; asset_name MNY MRKT and MONEY MKT",
        "explore over the snapshot: 0 of 227 priced Cash Equivalent CUSIPs have any row with cash_equivalent true and a MONEY MARKET name"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W42-S2",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~42",
    "surfaced_at": "2026-10-13T17:32:49Z",
    "one_line": "The R9 check dq_t50_real.py docstring states priced_names + skipped_one_dollar == 606 + 0, but its executable arms require priced_names == 606 and securities == priced_names - skipped_one_dollar + funds_joined.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "dq_t50_real.py docstring: 'priced_names + skipped_one_dollar == 606 + 0'.",
    "world_is": "The arms govern and were met: priced_names 606, securities 614 == 606 - 0 + 8. The docstring identity holds only while skipped_one_dollar is 0; with any skip the docstring and the arms disagree. The worker did not edit the issuer's check file; the arms were met as written.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t50_real.py docstring: priced_names + skipped_one_dollar == 606 + 0",
        "dq_t50_real.py arms: priced_names == 606 and securities == priced_names - skipped_one_dollar + funds_joined; AC2 printed B1-REAL-OK"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W42-S3",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~42",
    "surfaced_at": "2026-10-13T17:32:49Z",
    "one_line": "The held snapshot silver/cot_holdings.parquet has no row in the legacy address registry; the builder derives its bucket and name from the registry's silver transactions row and the firm short token, because the naming gate refused the typed filename.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO DQ-t-50 BUILD: read the held snapshot s3://opal-data-cot/silver/cot_holdings.parquet (columns cusip, asset_name, asset_display_name, cash_equivalent); CLAUDE.md rule 30: every S3 address is lib/opal_naming output.",
    "world_is": "infra/logic/registry/legacy_addresses.json has no row for the snapshot, and no lib file names it. The first commit attempt of the code paths was refused by the naming gate (NAMING REFUSE b1_request.py cot_holdings.parquet -> lookup('cottonwood')). b1_request.py now reads the object the order names: bucket from legacy_address of cottonwood-silver-transactions-prefix, name from lookup('cottonwood')['short'] plus _holdings.parquet; 341,985 bytes and 10,183 rows at read. A registry row for the snapshot would retire the derivation.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "safe-commit of the code paths, first attempt: NAMING REFUSE data/mdpf/scripts/demque/b1_request.py:74 cot_holdings.parquet -> lookup('cottonwood'); rc 1; files unstaged",
        "grep of infra/logic/registry/legacy_addresses.json for the snapshot name: no row (the Cottonwood rows are cottonwood-silver-canonical-prices, cottonwood-silver-transactions-prefix, cottonwood-silver-historical-prices)",
        "read of the snapshot on 2026-10-13: get_object returned 341985 bytes; pyarrow read 10183 rows"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W42-S4",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~42",
    "surfaced_at": "2026-10-13T17:32:49Z",
    "one_line": "The order's window start is max(first held date, 2012-01-01), but the P1 builder starts a name at its first Trade_Date (any type, any account); the request uses the builder's window, and no held-history table was read.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO DQ-t-50 BUILD step 2 and Worker face item 1: the floor is max(first held date, 2012-01-01); the window end is the merged P1 builder's.",
    "world_is": "card_a_slice.trade_windows sets start = max(first Trade_Date, 2012-01-01) and end = the frontier when held, else the last Trade_Date. No held-start is defined there, and the held snapshot is current-only. The worker used the builder's start for the P1 names; the end rule is the builder's, as the order also says. The earliest start in the request is 2013-04-09; cells 37514. A held-start rule would need a held-history source the order does not name.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/card_a_slice.py trade_windows at 1dcdbbde7d: start = max(first_day, FLOOR); end = frontier_day if held else min(last_day, frontier_day)",
        "b1_request.py --build at 1dcdbbde7d: window_start 2013-04-09, cells 37514, days_to_finish 18"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W42-S5",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~42",
    "surfaced_at": "2026-10-13T17:32:49Z",
    "one_line": "The order requires a merge of box/dell1 before the rows are appended; the worker standing rules forbid a merge. This worker merged box/dell1 into its own branch (ad0aa2bf3d) because the investigation file differs by 41 lines from its base.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO refusal clause: 'Merge box/dell1 into your branch (a merge, never a rebase) before you append rows'; the worker rules: never push, merge, rebase, checkout or clean.",
    "world_is": "git diff 932f896786 box/dell1 on this investigation file: 41 insertions (rows of other workers). The merge was a plain merge into wk-MDPF_DEMQUE-42 with no conflict (merge commit ad0aa2bf3d, rc 0). Nothing was pushed or rebased. This is the rule collision of MDPF_DEMQUE-D1-W41-S1; the drain should rule which governs.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git diff --stat 932f896786 box/dell1 on the investigation file: 1 file changed, 41 insertions",
        "git merge --no-edit box/dell1 in wk-MDPF_DEMQUE-42: rc 0, merge commit ad0aa2bf3d, no unmerged paths"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W43-S1",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~43",
    "surfaced_at": "2026-10-13T17:44:38Z",
    "one_line": "On the real store index the UNTESTABLE arm of DQ9-t51-AC2 is vacuous: no held window is under 10 trading days (the minimum is 125), so the real run lists 0 UNTESTABLE securities; the UNTESTABLE path is exercised only by the synthetic test.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO DQ-t-51 ACCEPTANCE DQ9-t51-AC2: 'the UNTESTABLE ones are listed with the reason'; the report asks for 'the count of UNTESTABLE securities'. The decomposition's DQ-t-51 amendment frames a window under 10 trading days as a case that occurs.",
    "world_is": "Read-only probe of index/index.parquet at the worker's HEAD: 326 rows, 326 distinct CUSIPs; minimum trading days in the draw window 125; 182 windows are under 252 trading days (the 1-year length is replaced there); 0 windows are under 10. The --build line reads testable 326, untestable 0, intervals_total 1630, cells 3195. The 182 short windows are short against one year, not against ten trading days.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "porting_test.py build_request at a8710f8b4a: a window with fewer than MIN_WINDOW_DAYS=10 trading days is listed untestable",
        "dq_t51_real.py run 2026-10-13 (rc=0): INT-REAL-OK 326 testable with exactly 5 intervals each, 0 UNTESTABLE, 3195 cells",
        "read-only probe .scratch/t51_index_probe2.py (uncommitted): denominator 326, min N 125, N<252 count 182, N<=60 count 0"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W43-S2",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~43",
    "surfaced_at": "2026-10-13T17:44:38Z",
    "one_line": "The order says a fixed length that does not fit is replaced by a sha256 draw from 'a salted second digest' and says 'does not fit inside the window (in trading days)' without a test; the worker chose the salt, the word order and the fit test, and the draw now depends on those choices.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO DQ-t-51 BUILD step 1: 'a length that does not fit inside the window (in trading days) is REPLACED by a length drawn from the digest between 5 and N - 1 trading days (a salted second digest if the first has been used, so the replacement is deterministic)'.",
    "world_is": "porting_test.py at a8710f8b4a: a fixed length fits for k 0..2 when its calendar length has room inside the window and both endpoints snap to trading days inside it with at least 5 trading days between them. A replacement uses sha256('<cusip>|<k>|r'): word 0 gives the length 5 + (w mod (N-5)), so 5 to N-1; word 1 gives the start index (w mod (N-L)). k 3 and 4 use the first digest: length 5 + (word 1 mod (min(250, N-1)-4)). The draw is deterministic, so a second implementer must reproduce these bytes or the request differs.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/porting_test.py _fixed, _replacement, _drawn at commit a8710f8b4a",
        "data/mdpf/scripts/demque/test_demque_porting_intervals.py test_a_fixed_length_that_does_not_fit_is_replaced_by_a_sha256_drawn_length_that_fits_so_every_testable_security_has_five_intervals recomputes the salted draw"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W45-S1",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~45",
    "surfaced_at": "2026-10-13T18:39:26Z",
    "one_line": "The order's fund-type filter for --coverage reads Asset_Type 'from lock.json's class where present', but no landed lock.json carries a class field, so the filter had to take Asset_Type from the Cottonwood transactions instead.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO DQ-t-53 BUILD step 2: '--coverage ... of the landed names whose Asset_Type is an ETF or fund type (from lock.json's class where present)'.",
    "world_is": "The live price store (s3://opal-data-assets/yahoo/global/silver/price_history, read 2026-10-13) holds 326 landed names; the lock.json of all 326 was read and none carries asset_class, class or Asset_Type (the sample key set is claim, cusip, locked_at, median_abs_error, method, observations_checked, observations_passed, run_id, state, supersedes, trades_through, valid_from, valid_to, yahoo_symbol). The coverage therefore takes Asset_Type from b1_request.read_transactions (first non-null per CUSIP, the daily_draw rule; 4,634 CUSIPs). Fund types taken: ETF, Mutual Fund, Mutual Fund (Closed End), Unit Investment Trust. Measured: checked 131, classified 108, missing_examples 5 CUSIPs; the classification gap is SECCLASS's path, not DEMQUE's.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/secclass_sync.py coverage() and _run_coverage() at this branch: lock_class() reads lock.json keys asset_class, class, Asset_Type; the stderr line 'lock.json carries a class for 0' printed by --coverage on 2026-10-13",
        "data/mdpf/scripts/demque/b1_request.py read_transactions() and _asset_types() at commit 41d134244e; the distinct Asset_Type values counted from 1,416,497 transaction rows",
        "--coverage run 2026-10-13 (rc=0): {\"checked\": 131, \"classified\": 108, \"missing_examples\": [\"001419688\", \"00141B204\", \"00888W700\", \"01883A107\", \"09251M504\"]}"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W44-S1",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~44",
    "surfaced_at": "2026-10-13T18:40:44Z",
    "one_line": "The order's premise that the request builders already leave out pursued: False does not hold: card_a_slice.py calls rank.rank and reads no pursued flag, and b1_request.py reads none either. Before this change nothing in the demque folder read pursued outside rank.py.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "DQ-t-52 BUILD item 2 (task order DQ-t52, WORKER FACE): 'The request builders already leave out pursued: False.'",
    "world_is": "The exclusion is enforced where the order also names it: demand_queue.draw skips an excluded security (daily_draw.run passes the gate's classes), and extend_frontier leaves excluded names out of every tier. The builders still write a P2 or P3 name into a request file (census: requests/ holds 1,093 such securities, see MDPF_DEMQUE-D1-W44-S5), and the draw skips them there. card_a_slice.py and b1_request.py are outside the grant and were not edited.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/card_a_slice.py@e7a7beca52 line 158: ranked = rank.rank([...]) and no read of pursued in the file (grep)",
        "data/mdpf/scripts/demque/b1_request.py@e7a7beca52: imports rank (line 54); no call to rank.rank and no read of pursued (grep)"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W44-S2",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~44",
    "surfaced_at": "2026-10-13T18:40:44Z",
    "one_line": "Five existing tests outside the grant fail on the new rule. Each plans or reports standing names with fake CUSIPs and no classification stub, so the priority gate reads the real crosswalk, classes the fake names P2 (no holder on record) and excludes them. The grant does not cover these four files, so they are left unedited.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "spec_asserts": "Order instruction: 'another existing test file that fails on the new rule is a surprise row asking for the grant, not an edit'; the whole folder reports 0 failed.",
    "world_is": "python -m pytest data/mdpf/scripts/demque -q at e7a7beca52 plus this branch's change: 5 failed, 178 passed (51.6 s). The failing tests, none in <paths>: test_demque_extend_future.py::test_today_equal_to_the_local_date_still_plans; test_demque_extend_guard.py::test_a_frontier_on_or_after_the_latest_valid_to_still_plans; test_demque_lag_report.py::test_the_lag_report_counts_every_indexed_name_in_one_tier_with_its_measured_lag and ::test_a_name_older_than_its_tier_cycle_is_listed_over_and_never_counted_within; test_demque_yahoo_need_class.py::test_the_standing_extension_request_declares_client_and_a_window_start_on_or_after_the_floor. The grant that clears them is the one-line xf._excluded_for stub the order allowed in test_demque_rolling_tiers.py and test_demque_extend_frontier.py, added to each of these four files. Production is unaffected: dq_t52_real.py returns GATE-REAL-OK on the real names.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "pytest run at the worktree, output in the worker's scratch: 5 failed, 178 passed in 51.55s; each failing assertion reads 0 symbols or 0 names where the test expects 2 or the daily tier",
        "test_demque_extend_guard.py:79 'assert day[\"symbols\"] == 2 and day[\"cells\"] > 0' fails with (0 == 2): the extension excluded both fake names as P2"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W44-S3",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~44",
    "surfaced_at": "2026-10-13T18:40:44Z",
    "one_line": "rank.py's two S3 loaders compute the repo root with four dirname calls, which lands in data/, so 'from lib.opal_naming import address' fails in a plain python run unless PYTHONPATH carries the repo root. run_daily_draw.sh sets PYTHONPATH, so the nightly path is unaffected.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "DQ-t-52 AC2 runs 'python .../dq_t52_real.py' from the worktree root with no PYTHONPATH and expects GATE-REAL-OK (the census must load the crosswalk and transactions).",
    "world_is": "rank.py@e7a7beca52 lines 136 and 147 take four dirnames of abspath(__file__), which is data/. The first AC2 run returned GATE-REAL-BAD 'crosswalk unreadable (ModuleNotFoundError)' in 0.6 s. priority_gate.py now inserts the repo root from its own four-up path when it is absent from sys.path; rank.py's root formula is unchanged, as it is outside the order's scope. Any other caller of rank.load_crosswalk or load_transactions outside PYTHONPATH hits the same error.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/rank.py@e7a7beca52 lines 136 and 147: root = os.path.dirname x4 of os.path.abspath(__file__)",
        "AC2 run before the gate-side fix: GATE-REAL-BAD rc=1 REFUSED: crosswalk unreadable (ModuleNotFoundError), 0.6 s; after it: GATE-REAL-OK, 60 s"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W44-S4",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~44",
    "surfaced_at": "2026-10-13T18:40:44Z",
    "one_line": "The device queue is not P1-only. Its IRPT copy is cut to P1 (630 of 630), but ADVI_COTBKF-TIER2-15 carries 3 match-open names and R2-SCHED-SLICE-1 carries 1. From the 22:30 ET draw after this merges, those four securities are skipped and counted, not drawn.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Order orientation: 'Your change must keep a P1-only queue valid and drawing as before'; DQ-t-52 AC2: the IRPT device queue copy carries no P2 or P3 name.",
    "world_is": "priority_gate.py --census at e7a7beca52 (S3 read, 2026-10-13): queue/IRPT_BCKEND-AS-TRADED-CLOSES-878.json securities 630, P1 630, P2 0, P3 0; queue/ADVI_COTBKF-TIER2-15-FUNDS-AS-TRADED-20261012.json securities 15, P1 12, P2 3; queue/R2-SCHED-SLICE-1.json securities 3, P1 2, P2 1; the other five queue files are P1 in full. No request file was edited (outside the grant).",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "priority_gate.py --census output line (captured to the worker's scratch, rc 0): files rows for queue/*.json",
        "census rule field names Andrew-direct 2026-10-13 and the former client and match-open classes"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W44-S5",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~44",
    "surfaced_at": "2026-10-13T18:40:44Z",
    "one_line": "1,093 securities in the repo request files carry no CUSIP (a cusip_reason field stands in). The order does not say how a name with no CUSIP is classed. The gate classes it P2 by rank's no-holder rule, so it is excluded; the census counts it P2.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "DQ-t-52 BUILD item 1: 'a name with no holder on record is P2 (the rank rule), so it is excluded too'; the census rows: every file row has securities == P1 + P2 + P3.",
    "world_is": "census over requests/ at e7a7beca52: AMGT_RESAPP-S14-CRNCY-SCANNER-US.json 1038 P2; AMGT_RESAPP-S14-CRNCY-SCANNER-US-SLICE1.json 50 P2; AMGT_RESAPP-493c-ICT-IDENTITY.json 1 P2; MDPF_SECHIST-SHT8-TR-FIELD-HISTORY-20261009.json 2 P2; MDPF_SECHIST-SHT8-TR-FIELD-CONFIRM-20261009.json 1 P2; SITEZ-SIGNIN-PREFLIGHT-REFDATA-20261009.json 1 P2, every one with an empty cusip. None is in the device queue. The class is a choice (None is ranked like any name with no holder) for the CTO to confirm.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "priority_gate.py --census (rc 0): the requests/ rows of AMGT_RESAPP-S14-CRNCY-SCANNER-US.json and the five other no-CUSIP files",
        "priority_gate._request_files: cusips list carries None for a security with no cusip (the rank rule classes it P2)"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W44-S6",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~44",
    "surfaced_at": "2026-10-13T19:06:02Z",
    "one_line": "The census gives each non_client row securities 0, its count in requested, and null classes: the AC2 check reads a null class as zero and a string n/a would make its sum raise, so this is the only form it passes unedited.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Amended order 2026-10-13, census ruling: a non-client row's classes are counted as n/a 'so the rows still add up'; 'set their securities accordingly'. AC2 file_rows arm: every file row has securities == P1 + P2 + P3.",
    "world_is": "dq_t52_real.py file_rows computes (f.get('P1') or 0) + (f.get('P2') or 0) + (f.get('P3') or 0); a string 'n/a' raises TypeError there, null sums to 0. The census on this branch prints 8 non_client rows: requested 1,100 in total, securities 0, classes null. The check is unedited.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t52_real.py@b3c92c8830 (file_rows arm, unedited)",
        "python data/mdpf/scripts/demque/priority_gate.py --census run from the worktree wk-MDPF_DEMQUE-44 (rc 0; 8 non_client rows, requested 1100)"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W44-S7",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~44",
    "surfaced_at": "2026-10-13T19:06:02Z",
    "one_line": "A non_client security with no CUSIP, once its request is queued, is drawn but cannot be stored: the store is keyed by CUSIP, so the pull is counted under unstored_no_cusip and its pacer request is spent.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Amended order 2026-10-13, ruling: 'a non-client request security with no CUSIP is NOT skipped' (one test); the draw stores prices keyed by CUSIP (daily_draw on_result).",
    "world_is": "No non_client request is in the device queue today: all 7 queue files are client-class (survey at b3c92c8830). The repo requests/ folder holds non_client securities with no CUSIP: AMGT_RESAPP-S14-CRNCY-SCANNER-US.json 1038, AMGT_RESAPP-S14-CRNCY-SCANNER-US-SLICE1.json 50, AMGT_RESAPP-493c-ICT-IDENTITY.json 1, MDPF_SECHIST-SHT8-TR-FIELD-HISTORY-20261009.json 2, MDPF_SECHIST-SHT8-TR-FIELD-CONFIRM-20261009.json 1, SITEZ-SIGNIN-PREFLIGHT-REFDATA-20261009.json 1. If one is copied to the queue, each such pull is spent and its prices are dropped.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/daily_draw.py on_result, the cusip None branch (this branch)",
        "survey of requests/ and ~/.opal/demque/queue at b3c92c8830 (7 queue files, all need_class client; the requests/ no-CUSIP counts above)"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W47-S1",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~47",
    "surfaced_at": "2026-10-13T20:26:48Z",
    "one_line": "The DQ-t-55 order names the surface E CLI key set as {day, history_allowance, cap, cells, verdict, message}; the built CLI line also carries claim and remaining_reserve.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO MDPF_DEMQUE.TO-DQ-t55 step 4: the CLI prints ONE JSON line {day, history_allowance, cap, cells, verdict, message}; step 1: a non-measured ceiling claim is carried by the result; step 2: an ACCEPT carries remaining_reserve.",
    "world_is": "surface_e_intake.py at b079e76bd6 prints {cap, cells, claim, day, history_allowance, message, remaining_reserve, verdict}. claim is carried because step 1 says the result carries it; remaining_reserve because step 2 and the test name print it. A consumer that matches the exact listed key set sees two extra keys. dq_t55_real.py reads keys by name and is unaffected. The order does not fix the ACCEPT message text; the builder wrote it. The REFUSE message is the order's exact text.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/surface_e_intake.py check() and main() at branch wk-MDPF_DEMQUE-47 commit b079e76bd6",
        "org/missions/D8/MDPF/MDPF_DEMQUE/task-orders/MDPF_DEMQUE.TO-DQ-t55.surface-e-intake-cap.md WORKER FACE step 4 (CLI key list) at commit 1cd9c6f1ab",
        "python data/mdpf/scripts/demque/surface_e_intake.py --cost --securities 1 --trading-days 252 --fields 2 --day 2026-10-14 printed the 8-key line, rc=0"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W46-S1",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~46",
    "surfaced_at": "2026-10-13T20:30:47Z",
    "one_line": "The AC2 arm 1 expectation in dq_t54_real.py, (ceiling - 1000) + 0 + ceiling + ceiling, is 16574 at ceiling 5858, which is three ceilings where the order's own formula over the five trading days gives four: Tuesday, Thursday and Friday each carry a whole ceiling, so the figure is 22432. The criterion cannot be met as written; the check is not edited and the figure is not bent to match it.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "spec_asserts": "dq_t54_real.py arm 1 (the R9 check, unedited): a synthetic week Mon 1000, Tue 0, Wed ceiling + 500, Thu 0, Fri 0 must read carried_over == (ceiling - 1000) + 0 + ceiling + ceiling. The order's Build item 1: carried_over = the sum over trading days of max(ceiling - spent[d], 0). The order's AC2 line: Monday 1,000, Wednesday ceiling + 500, the rest 0 carries (ceiling - 1000) + 0 + ceiling + ceiling.",
    "world_is": "The five trading days between the previous fire day Sun 2026-10-11 and the fire day Sat 2026-10-17 are Mon 10-12, Tue 10-13, Wed 10-14, Thu 10-15 and Fri 10-16 (lib/trading_calendar.py is_trading_day True for each). Under the formula: Mon ceiling-1000, Tue ceiling, Wed 0, Thu ceiling, Fri ceiling = 4 x ceiling - 1000 = 22432. Measured by the R9 check run from the worktree: 'arm2 empty dir: carried_over=0 claim=absent room=5858 ceiling=5858', then 'arm1 synthetic ledger: carried_over=22432 expected=16574 room=28290 claim=measured', then 'CARRY-REAL-BAD arm1 carried_over/room mismatch', rc=1. Arm 3 is not reached by the check; a direct probe of the real default directory (absent on dell1) reads carried_over 0, claim absent.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t54_real.py arm 1 expect line @1cd9c6f1ab (read, unedited)",
        "org/missions/D8/MDPF/MDPF_DEMQUE/task-orders/MDPF_DEMQUE.TO-DQ-t54.non-trading-day-carry-over.md Build item 1 and the AC2 arm line @1cd9c6f1ab",
        "python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t54_real.py, run from the worktree wk-MDPF_DEMQUE-46 with this branch's standing_drawer.py (rc=1, CARRY-REAL-BAD arm1)"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W46-S2",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~46",
    "surfaced_at": "2026-10-13T20:30:47Z",
    "one_line": "The order reads a missing or unreadable budget ledger as spending 0 and marking that day's figure absent, while carried_over sums max(ceiling - spent, 0) over every trading day. Read literally, a day whose ledger is unreadable carries a whole ceiling even when production spent on it. The implementation follows the literal reading and lists such days in absent_days; the conservative reading (an absent day carries 0) is the CTO's to rule.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Order Build item 1: a missing or unreadable file reads 0 and marks the figure absent; carried_over = the sum over trading days of max(ceiling - spent[d], 0); claim is measured when at least one trading day's ledger was read, else absent with carried_over 0.",
    "world_is": "carry_over implements the literal reading: a partially readable week carries a whole ceiling for each missing day, lists it in absent_days, and claims measured. An empty or absent budget directory is the no-ledger case and carries 0 with claim absent. The real default directory on dell1 does not exist, so no site Z figure is measured here. The question only arises at site Z, where the first non-trading fire after a partially readable week would carry those days in full.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/standing_drawer.py carry_over and _day_spent, this branch (committed with this row)",
        "org/missions/D8/MDPF/MDPF_DEMQUE/task-orders/MDPF_DEMQUE.TO-DQ-t54.non-trading-day-carry-over.md Build item 1 @1cd9c6f1ab",
        "python data/mdpf/scripts/demque/standing_drawer.py --carry-over --day 2026-10-17 (default directory, rc=0, claim absent, absent_days lists the five trading days)"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W46-S3",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~46",
    "surfaced_at": "2026-10-13T20:30:47Z",
    "one_line": "bbg_budget.record keys each spend line by the UTC date at the moment it is written, so a non-trading fire run in the evening Eastern time writes its own draws into the next UTC date. When that date is a trading day inside the carry window, the carry reads the drawer's own draw as production spend. The error only lowers the carry, which is the conservative direction.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "The carry reads spent[d] from the budget ledger of UTC day d (order Build item 1, that UTC day's budget ledger). The drawer's draws are recorded through bbg_budget.record with mode demque-backfill.",
    "world_is": "bbg_budget.record writes to the file for dt.datetime.now(timezone.utc).date(). Observed in this worker's own test run: the run recorded its draw into the UTC-today ledger of the test budget directory, and that directory then read as a measured trading day. The test now uses a fresh directory for the CLI arm. A Sunday-evening or holiday-evening Eastern fire lands its draws on Monday or Tuesday UTC. No production change was made.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/etfs/scripts/rivalfunds/bbg_budget.py record() and _ledger_file() @1cd9c6f1ab (read)",
        "data/mdpf/scripts/demque/test_demque_carry_over.py CLI arm, this branch (the fresh directory after the failing run)"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W48-S1",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~48",
    "surfaced_at": "2026-10-13T21:12:32Z",
    "one_line": "Under the drawability rule the order states (a reference request with a list of securities is drawable), the two AMGT_RESAPP S14 CRNCY requests become open at the standing drawer. The full request's own securities_note says it is drawn only if the slice reads a non-USD currency; the drawer cannot read that condition, so the first fire on 2026-10-17 would draw the 50-cell slice and then the 1,038-security request up to the reference room.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~Q1",
    "spec_asserts": "DQ-t-56 Build item 4: a request with channel reference and a list of securities is drawable (one reference_data call per chunk). The R9 check arm 1 expects the open list to name B1, the porting test, the fund-type check and the TR comparison.",
    "world_is": "python data/mdpf/scripts/demque/standing_drawer.py --open (this branch, rc=0) lists MDPF_SECHIST-CARD-A-B1-FUND-TYPE, MDPF_SECHIST-CARD-A-B1-OPTION-C, MDPF_SECHIST-CARD-A-PORTING-TEST, AMGT_RESAPP-S14-CRNCY-SCANNER-US-SLICE1, AMGT_RESAPP-S14-CRNCY-SCANNER-US and DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS. Both AMGT files are tier 4, non_client, reference, with a quote on file. The slice's securities_note says the full request is drawn only if the slice reads a non-USD currency. The filer is 2.0.0_SA_COO~R1 (filed_by). The reference room is the held reference ceiling of 52 cells per fire day, and the slice is first in file order. Disarm: the issuer holds the full request, or marks the slice result, before the 2026-10-17 fire.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/standing_drawer.py _undrawable_reason, _draw_reference and survey (this branch)",
        "org/missions/D8/MDPF/MDPF_DEMQUE/requests/AMGT_RESAPP-S14-CRNCY-SCANNER-US-SLICE1.json securities_note @8b7c76ad35",
        "python data/mdpf/scripts/demque/standing_drawer.py --open (this branch, rc=0)"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W48-S2",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~48",
    "surfaced_at": "2026-10-13T21:12:32Z",
    "one_line": "Once client requests pass the priority gate, the three existing drawer test files reach the real crosswalk read (S3) and their fake cusips are excluded as P2. Their site fixtures now stub the gate; no assertion changed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "DQ-t-56 Bounds: the existing drawer tests keep passing; the three named files change only where an assertion pins the old behaviour.",
    "world_is": "With the gate applied, python -m pytest on test_demque_standing_drawer.py, test_demque_standing_drawer_close.py and test_demque_carry_over.py failed six tests with stop_reason GATED, and the run read S3. Each file's site fixture now monkeypatches priority_gate.load_inputs and priority_gate.excluded (two lines, plus an import). No assertion in those files was changed. The new test file stubs the gate in its own fixture.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/test_demque_standing_drawer.py, test_demque_standing_drawer_close.py, test_demque_carry_over.py site fixtures (this branch)",
        "data/mdpf/scripts/demque/priority_gate.py excluded and load_inputs @8b7c76ad35"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W48-S3",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~48",
    "surfaced_at": "2026-10-13T21:12:32Z",
    "one_line": "The order does not name a room for the reference channel. The drawer uses the held reference ceiling less the reference cells drawn today; history keeps its own room.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "DQ-t-56 Build item 4: cells = securities x fields, one call per chunk of CHUNK_ROWS securities. No room is stated for the reference channel.",
    "world_is": "run() gives reference requests their own room: allowance reference ceiling (held, 52 cells) less the reference cells in today's actuals lines. Reference rows are budget-recorded under mode demque-backfill-reference, which bbg_ledger_upload maps to channel None, so they never enter the history figure. The ceiling is a ledger floor (its own basis text says so). The issuer owns the reference figure.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/bbg_allowance.json reference.ceiling @8b7c76ad35",
        "data/mdpf/scripts/demque/bbg_ledger_upload.py _conversion (unknown mode -> channel None) @8b7c76ad35",
        "data/mdpf/scripts/demque/standing_drawer.py _reference_room and run (this branch)"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W48-S4",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~48",
    "surfaced_at": "2026-10-13T21:12:32Z",
    "one_line": "The --plan line must print securities as a count with identifier_forms summing to it, but test_demque_need_class.py (outside this order's grant) pins the plan() dictionary with securities as a list of identifiers. Both shapes are kept: plan() is unchanged and plan_detail() is the CLI line.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "DQ-t-56 Build item 6 and AC2 arm 2: the --plan line carries remaining_cells, securities (an integer of at least 600 for B1) and identifier_forms (a dict whose values sum to securities).",
    "world_is": "test_a_request_whose_start_moves_later_draws_only_the_undrawn_in_window_rows_by_identity asserts plan() == {request_id, window_start, remaining_cells, securities: [identifiers]}. plan() keeps that shape. plan_detail() returns the DQ-t-56 shape and is what python standing_drawer.py --plan --request ID prints. The need-class test file was not edited.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/test_demque_need_class.py lines 154-178 @8b7c76ad35",
        "data/mdpf/scripts/demque/standing_drawer.py plan and plan_detail (this branch)"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W48-S5",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~48",
    "surfaced_at": "2026-10-13T21:12:32Z",
    "one_line": "The one-row probe's row is discarded and its day is drawn again by the normal draw. The probe costs one extra cell, counted on the request and in its actuals line.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "DQ-t-56 Build item 1: the first draw of a /cusip/ entry is a one-row probe; if it returns the row the draw continues.",
    "world_is": "A probe returns one field for one day, while a stored history row must carry every field of the request, so the probe row is not stored. The day is drawn again in full, which costs one cell. The probe's cell is charged against the room as well as the owed cap. The receipt prints the probe under probes, and the request prints identifier_form.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/standing_drawer.py _probe_history, _identifier_form and _draw_history (this branch)",
        "data/mdpf/scripts/demque/test_demque_drawer_cusip_entries.py test 1 (this branch)"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W49-S1",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~49",
    "surfaced_at": "2026-10-13T22:00:25Z",
    "one_line": "AC2 arm2 requires securities 613 in the B1 line; the rule as written yields 612. One in-set CUSIP (9128334Y3) has an active window that opens 2026-09-22, after all of its B1 history, so its cells are clipped away and the name is emptied and dropped (Build item 3). 613 is the pre-clip count less the held-back fund. The emptied rule and the 613 cannot both hold; 613 was not forced.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "spec_asserts": "AC2 (dq_t57_real.py arm2): the B1 line shows securities 613, clipped about 99 CUSIPs, 33,000 to 35,500 cells. Build item 3: an entry left with no cells is dropped; a CUSIP left with none is counted in emptied_cusips; the --build securities key counts distinct CUSIPs in the request.",
    "world_is": "At be745e7fa2 the --build line reads securities 612, clipped_cusips 99 (98 narrowed plus the one emptied), emptied_cusips 1, unclipped_cusips 4, held_back 1, cells 34341. 612 = 614 (606 priced plus 8 funds) minus 1 held-back fund minus 1 emptied name. The emptied name 9128334Y3 has an active window from 2026-09-22, open; none of its B1 cells (2024-08-05 to 2026-05-27) falls inside it. A 613 would need a name with no entries in the request. CTO to rule: confirm an emptied name leaves the request (Build item 3 as written), and restate AC2 as 612.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D8/MDPF/MDPF_DEMQUE/task-orders/MDPF_DEMQUE.TO-DQ-t57.active-set-windows.md@be745e7fa2",
        "data/mdpf/scripts/demque/b1_request.py build_request and clip_entries@be745e7fa2",
        "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t57_real.py arm2, run at be745e7fa2: WIN-REAL-BAD arm2 (securities 612)"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W49-S2",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~49",
    "surfaced_at": "2026-10-13T22:00:25Z",
    "one_line": "AC2 and the order cite 37,439 filed cells for the unclipped B1 request. The unchanged base code measures 37,514 cells on this date, which matches the DQ-t-50 instance's measured 37514 at 1dcdbbde7d. The clip gives 34,341, which matches the issuer's figure exactly. The check's bound (under 37,439) holds either way.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Order AC2: 'the B1 line clipped ... 33,000 to 35,500 cells against 37,439 filed'; arm2: cells strictly below 37439.",
    "world_is": "The base b1_request.py, run once before any change on this branch (--build to a scratch path, S3 read only), printed cells 37514 and securities 614. The published set's clip gives 34341 cells. The figure 37439 does not reproduce on this date; no check was weakened.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D8/MDPF/MDPF_DEMQUE/task-orders/MDPF_DEMQUE.TO-DQ-t57.active-set-windows.md@be745e7fa2",
        "org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~42/MDPF_DEMQUE.TO-DQ-t50.b1-cottonwood-depth-option-c-request.proof_of_spec.json@6765fe5e2b (cells 37514 at 1dcdbbde7d)"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W49-S3",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~49",
    "surfaced_at": "2026-10-13T22:00:25Z",
    "one_line": "The unchanged --build ran about 51 s wall time and the first clipped build went over the real check's 55 s subprocess timeout (TimeoutExpired in arm2). Four speed-only changes (memoised NYSE calendar lookups; the P2/P3 gate reads the named CUSIPs' rows; fund windows read from the fund rows; output verified byte-identical) bring --build to about 45 s. The margin is thin: card_a_slice.build (about 24 s) is outside this order's paths and is the largest cost.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Order AC2 note: '55 seconds a run: read the CSV once; load the priority-gate classification lazily and cache it for the run'. dq_t57_real.py gives each --build subprocess a 55 s timeout.",
    "world_is": "Measured at be745e7fa2: one --build run took 55 s before the speed changes (arm2 TimeoutExpired) and 45 s after (rc 0, same bytes). Stage times after the changes: transactions read about 3 s, card_a build about 24 s, gate about 1 s, build_request about 5 s, quote about 6 s.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/b1_request.py _fund_windows, excluded_names, calendar memoisation@be745e7fa2",
        "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t57_real.py _line timeout=55@be745e7fa2"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W49-S4",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~49",
    "surfaced_at": "2026-10-13T22:00:25Z",
    "one_line": "AC2 expects accounts 769. Counting only the rows that are not skipped gives 639; 130 active accounts appear only on the 472 blank-cusip rows. active_set.census counts every row's account key (769): a skipped row still belongs to an active account. The definition is stated in active_set.py's docstring.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Order DQ-t-57 Build item 2: accounts = the distinct account keys COUNTED, not listed; Build item 1: a blank-cusip row is counted under skipped and ignored.",
    "world_is": "The published CSV holds 769 distinct account keys over all 42,319 rows, 639 over the 41,847 rows with a non-blank cusip, and 130 keys only on blank-cusip rows (window_basis not_established). Neither reading was printed by account key; the counts are the only output.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/active_set.py census and module docstring@be745e7fa2",
        "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t57_real.py arm1 (accounts 769)@be745e7fa2"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W49-S5",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~49",
    "surfaced_at": "2026-10-13T22:00:25Z",
    "one_line": "The P2/P3 hold-back calls priority_gate.excluded on the crosswalk and transactions that main() already read, not priority_gate.excluded_for(), which would read S3 a second time (crosswalk and transactions) per run. The rule, the fail-closed refusal and the classification are the same; the P1 build and the gate rank over the same frames, so they cannot disagree.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Order Build item 3: P2/P3 names are held back via priority_gate.excluded, the same fail-closed read; AC2 note: load the priority-gate classification lazily and cache it for the run.",
    "world_is": "b1_request.excluded_names calls priority_gate.excluded once per run on the frames main holds (narrowed to the named CUSIPs; rank's per-name statistics are unchanged by the narrowing). build_request holds nothing back when its excluded argument is None, so main() is the only caller that applies the gate.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/b1_request.py excluded_names and main@be745e7fa2",
        "data/mdpf/scripts/demque/priority_gate.py excluded_for and load_inputs (not used by the build)@be745e7fa2"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W49-S6",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~49",
    "surfaced_at": "2026-10-13T22:18:03Z",
    "one_line": "The order's premise for test_demque_b1_request.py (a stub active set of {} leaves every window unclipped, so that test takes {} and nothing else) does not hold under the 22:0xZ ruling: an empty or absent active set now holds every security back, and build_request then raises 'no name is priced'. The one build call in that test now passes an active set whose single entry (the priced name, open from 2012-01-01) clips nothing; no assertion in that test changed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Order DQ-t-57 AC1 note and 'Existing test_demque_b1_request.py tests keep passing; one that pins the unclipped cell count takes the stub's empty active set (a stub that returns {} leaves every window unclipped) and NOTHING else.' Ruling 22:0xZ: a security NOT in the active set is HELD BACK, never kept at its old window.",
    "world_is": "build_request(active=None or {}) holds every security back (OUTSIDE_REASON), so the test's call with no active argument would raise ValueError('no name is priced') rather than leave windows unclipped. The test now passes active={'CDX000003': window from 2012-01-01, open}, which clips nothing; the test's other assertions are unchanged.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/test_demque_b1_request.py test 3 build_request call (uncommitted at this row; committed in this commit)",
        "data/mdpf/scripts/demque/b1_request.py build_request and OUTSIDE_REASON (uncommitted at this row; committed in this commit)",
        "org/missions/D8/MDPF/MDPF_DEMQUE/task-orders/MDPF_DEMQUE.TO-DQ-t57.active-set-windows.md AMENDED 22:0xZ@e7655e1a1e"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W49-S7",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~49",
    "surfaced_at": "2026-10-13T22:18:03Z",
    "one_line": "AC2 arm3 'no_account_key' (dq_t57_real.py line 75) is the substring test \"account\" not in json.dumps(req).lower(). The ruled hold-back reason text (CTO msg 5227: 'not held by an active Cottonwood account under any identifier the files carry ...') contains that word in each of the four outside-set held_back entries, so the real request fails arm3 although it holds no account key and no account number. AC2 cannot pass as written with the ruled text; the check is the issuer's file and is not edited here.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "spec_asserts": "DQ9-t57-AC2 arm3: the request carries no account key (dq_t57_real.py: \"no_account_key\": \"account\" not in json.dumps(req).lower()); the amended order: each outside-set name is held back with the reason 'not held by an active Cottonwood account under any identifier the files carry (draws are limited to the active set, CTO msg 5227)'.",
    "world_is": "The real --build request (scratch copy .scratch/b1_check49.json, S3 read only) holds 5 held_back entries; the word 'account' occurs 4 times in the request text, all inside the 4 outside-set reasons, 0 times in any securities key, and no key names an account. arm1, arm2 (608 / 1 emptied / 5 held back / 34,223 cells) and the determinism and validity arms pass; only no_account_key fails. The test in test_demque_active_windows.py test 3 now reads keys, not text, for the same property.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t57_real.py line 75 (no_account_key) @e7655e1a1e",
        "data/mdpf/scripts/demque/b1_request.py OUTSIDE_REASON (uncommitted at this row; committed in this commit)",
        "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t57_real.py run at this commit's parent: arm3 no_account_key, WIN-REAL-BAD arm3 no_account_key"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W52-S1",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~52",
    "surfaced_at": "2026-10-14T00:31:45Z",
    "one_line": "The order's message-file instruction ends each commit with a Co-Authored-By line naming Claude Sonnet 5.5, but the agent executing this order is Claude Haiku 5.5; the commits of this order carry the Haiku 5.5 trailer.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Order MDPF_DEMQUE.TO-DQ-t60 REPORT section: the message file for each commit ends with 'Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>'.",
    "world_is": "The executing model is Claude Haiku 5.5 (claude-haiku-5-5). The session attribution instruction for commits this agent creates names Claude Haiku 5.5. The commits of this order end with 'Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>'; the --author identity is the one ordered (0.9.0_WK_MDPF_DEMQUE~52). No check or verdict depends on the trailer's model name.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D8/MDPF/MDPF_DEMQUE/task-orders/MDPF_DEMQUE.TO-DQ-t60.active-set-v2.md (Bounds and REPORT wording) @85b4503efb",
        "session attribution instruction for commits created by this agent (Claude Haiku 5.5) @85b4503efb"
      ]
    }
  }
]
```

## Row filed by 4.0.0_SA_CRO~DELL1 (YCharts coverage walk, CTO msg 5356)

```json
{
  "id": "MDPF_DEMQUE-D1-S16",
  "project": "MDPF_DEMQUE",
  "fabric": "dell1",
  "surfaced_by": "4.0.0_SA_CRO~DELL1",
  "surfaced_at": "2026-10-14T02:24:00Z",
  "one_line": "The YCharts coverage walk's stop rule (scratchpad walk.js, CTO msg 5218) halted only on a 403 sign-out body, so 39 consecutive 405 'Human Verification' WAF replies did not stop it; the gateway's shared-session freshness probe then read HTTP 202 from about 02:09Z and recovered to 200 by 02:23Z with no act.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "CTO msg 5218: if the session is dead or any step needs a sign-in that would evict the shared seat, STOP and report; one shared session, no bulk pulls.",
  "world_is": "walk.js STOP covered status 403 with 'concurrent sign in' or 'signed out' only. Its HAR records securities_info 200 (SPY), 200 (4424366D8), then 39 x 405 with title 'Human Verification' from 02:03:15Z to 02:05:49Z at 4 s spacing. Five gateway ycharts_search calls followed: 4 x 200, the 5th 202, then stop. ycharts_freshness read ok at 02:06Z, HTTP 202 at ~02:09Z, ok HTTP 200 at 02:23Z. infra/aws/ec2/investor-reporting-ycharts/ycharts_session.js lines 76-77 already record that data endpoints answer 405 with x-amzn-waf-action captcha for a signed-in session. Any future walk must treat 405 and 202 as STOP.",
  "disposition": "UNDER_INVESTIGATION",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "scratchpad ycwalk_2026-10-14T0203Z.har and .json (session cookies inside; not committed)",
      "org/tier1_exec/4.0.0_SA_CRO/deliverables/YCHARTS_COVERAGE_WHAT_EXISTS_20261013.md section 5",
      "infra/aws/ec2/investor-reporting-ycharts/ycharts_session.js:76-77",
      "1.0.0_SA_CTO~DELL1 msgs 5218 and 5356"
    ]
  }
}
```

## Rows filed by 0.9.0_WK_MDPF_DEMQUE~50 (DQ-t-58, merged by the issuer: union by id of the worker branch onto HEAD)

```json
[
  {
    "id": "MDPF_DEMQUE-D1-W50-S1",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~50",
    "surfaced_at": "2026-10-13T22:38:24Z",
    "one_line": "The order's proof call 'incremental_equal.py --n 10 --tr' cannot select 10 names: the stratified sampler is cut for n=50, so the 50-name proof ran as five --piece I/K chunks of one selection.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/batch_equality.py _select raises unless the QUOTA sums to n (QUOTA = 19+16+11+4 = 50) @502c991c40",
        "data/mdpf/scripts/demque/incremental_equal.py _piece_of and the --piece flag (this branch)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "DQ-t-58 build item 7: run incremental_equal.py --n 10 --tr --out <part> five times, distinct names per piece, and merge the parts.",
    "world_is": "--n 10 exits at _select with 'this proof is cut for n=50'. The worker selected the 50-name stratified sample once and ran --n 50 --tr --piece I/K for I = 1..5 (10 names each, distinct cusips, merged by a scratch script; 50 of 50 distinct). The split arm rides piece 1/5 only."
  },
  {
    "id": "MDPF_DEMQUE-D1-W50-S2",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~50",
    "surfaced_at": "2026-10-13T22:38:24Z",
    "one_line": "Two names whose served lock reads LOCKED (claim held) get REJECTED:LOW_TRADE_AGREEMENT from a fresh lock.check over today's trades; the append carries the served lock and extends its valid_to.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~Q1",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~50/INCREMENTAL_WIRED_EQUALITY_REPORT.json no_split_arm.lock_record (6 differences over 50 names, all on LCEYX and FTHSX)",
        "data/mdpf/scripts/demque/lock.py check (unchanged) run by incremental_equal.py _relock over the full history on the same trades"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "COO half, pair A: the append carries claim, trades_through, state, observations and run_id unchanged; whether a full re-lock would differ is measured by incremental_equal.py and reported (never assumed); a name with no trade in its appended window is appended without a re-lock and listed.",
    "world_is": "LCEYX and FTHSX: served lock state LOCKED, claim held, trades_through null. A fresh lock.check over the full history on the same trades gives REJECTED:LOW_TRADE_AGREEMENT, claim measured (LCEYX trades_through 2020-02-24; FTHSX trades_through 2026-06-02). Neither name has a trade in its appended window, so the wired draw appends both without a re-lock and extends their valid_to to the frontier. No full re-pull runs for a name without a split or restatement, so nothing in the wired path re-checks them."
  },
  {
    "id": "MDPF_DEMQUE-D1-W50-S3",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~50",
    "surfaced_at": "2026-10-13T22:38:24Z",
    "one_line": "At 22:21Z on 2026-10-13 Yahoo held no 2026-10-13 bar for the sampled mutual funds; 19 of 50 proof names appended 4 rows where the window has 5 trading days.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "yahoo_pull.pull('ACTSX') at 2026-10-13T22:2xZ (scratch check): status OK, last price date 2026-10-12",
        "INCREMENTAL_WIRED_EQUALITY_REPORT.json no_split_arm.names tr_rows (19 names at 4, 31 at 5)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "DQ-t-58 build item 1 and the COO half: the window is the last five trading days ending at the last closed session (lib/trading_calendar.py; before 21:00 UTC today's bar is not final).",
    "world_is": "The 2026-10-13 session counts as closed at 22:21Z, but Yahoo had published no 10-13 bar for ACTSX at that time. Both the full path and the incremental path see the same 4 rows, so the equality holds. The gap is one trading day; it is not measured to close on a later night (the next request starts at the stored max by construction)."
  },
  {
    "id": "MDPF_DEMQUE-D1-W50-S4",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~50",
    "surfaced_at": "2026-10-13T22:38:24Z",
    "one_line": "price_store.index read its 326 names one at a time (50.5 s measured), too slow for the 100-second subprocess limit on the live --spot run in dq_t58_equal.py; index() now reads them in a 16-thread pool with the same rows and order (4.0 s).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "scratch timing of price_store.index over the served store, sequential: 50.5 s, 326 rows; Bloomberg load tr_compare.load_bloomberg 2.8-3.3 s, 37 partitions",
        "data/mdpf/scripts/demque/price_store.py index and _index_row (this branch); test_demque_store.py index tests pass unchanged"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "DQ-t-58 AC2: the live spot check 'incremental_equal.py --spot 5 --tr' runs inside dq_t58_equal.py's 100-second subprocess timeout.",
    "world_is": "A sequential index read alone used half the timeout. The index is a read only; the parallel read changes its speed, not its rows or order. The nightly write_index call runs the same function."
  },
  {
    "id": "MDPF_DEMQUE-D1-W50-S5",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~50",
    "surfaced_at": "2026-10-13T23:01:33Z",
    "one_line": "The re-seating message asks for the commit trailer Co-Authored-By: Claude Sonnet 5.5; this worker runs as claude-haiku-5-5, so its commits carry the Haiku 5.5 trailer that the session attribution rule names.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "the worker's model identity in the session environment: claude-haiku-5-5 (Haiku 5.5)",
        "commit 9449d5f48e on wk-MDPF_DEMQUE-50 carries Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Re-seating instruction (launching agent, 2026-10-13): commits end with 'Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>'.",
    "world_is": "The worker runs as claude-haiku-5-5. Attribution must name the model that produced the work, so the commit carries Claude Haiku 5.5; the Sonnet trailer was not written."
  },
  {
    "id": "MDPF_DEMQUE-D1-W50-S6",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~50",
    "surfaced_at": "2026-10-13T23:17:25Z",
    "one_line": "The wired run checks identity over the COMBINED history only: the appended-window lock.check that the amended pair A condition 2 keeps was dropped at 9449d5f48e, so a trade that disagrees only inside the appended window can be written (measured: combined LOCKED 20 of 21; window-only REJECTED:PRICE_MISMATCH 0 of 1).",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~Q1",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/daily_draw.py on_incremental on branch wk-MDPF_DEMQUE-50 at aeb1c69990: the only pair A condition 2 term is combined_relock (line ~242); no lock.check runs on the appended days (data/mdpf/scripts/demque/incremental_append.py:45 says lock.check is not re-run there)",
        "data/mdpf/scripts/demque/daily_draw.py at 39c3a3e402 lines 227-235 carried 'relock: <state> on the appended window'; 9449d5f48e replaced it with the combined check only",
        "measured on synthetic data (scratch .scratch/window_gap_measure.py, not committed): 20 agreeing stored trades plus one window trade at 1.5x; lock.check over the combined history LOCKED (20 of 21), lock.check on the appended window REJECTED:PRICE_MISMATCH (0 of 1)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "AMENDED 2026-10-13 ~23:0xZ (ruling on S2), MDPF_DEMQUE.TO-DQ-t58 and build item 4 (pair A condition 2): 'After building the appended window, run lock.check on the appended days'; 'The appended-window check stays.' The combined history relock is added beside it, not in its place.",
    "world_is": "The tree runs one identity check, over the combined history. A name whose appended window carries a trade that disagrees with Yahoo, while its stored trades agree, is LOCKED by that check and its window is written; the appended-window check would hold it. No named test isolates a window-only mismatch (test 4 and test 5 each carry a mismatch that fails the combined check too). Nothing is written by this row; the fix is the issuer's decision."
  },
  {
    "id": "MDPF_DEMQUE-D1-W50-S7",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~50",
    "surfaced_at": "2026-10-13T23:32:34Z",
    "one_line": "The amended appended-window check names the trades and the appended rows but not lock.check's valid_from. With valid_from at the window's first day, lock.check's early-third rule rejects an agreeing trade that falls late in the window (measured 1 of 1 agreeing, REJECTED:PRICE_MISMATCH). The wired window_relock takes valid_from at the window's first in-window trade, as the full path starts a name's range at its first trade (measured 1 of 1 agreeing, LOCKED).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/lock.py check(): early_end = valid_from + (valid_to - valid_from) / 3; a passed trade must sit on or before early_end (lock.py lines 102-104, base 362d75e8fa)",
        "scratch measurement .scratch/vf_measure.py (not committed, this pass): one agreeing trade on the last window day 2026-10-13 against appended closes 2026-10-06..2026-10-13: valid_from 2026-10-06 gives REJECTED:PRICE_MISMATCH 1 of 1; valid_from 2026-10-13 gives LOCKED 1 of 1",
        "data/mdpf/scripts/demque/daily_draw.py window_relock (this pass, branch wk-MDPF_DEMQUE-50, base 362d75e8fa): valid_from = the first trade dated inside (stored max, frontier]; test_a_stored_name_takes_the_five_day_window... depends on the last-day trade reading LOCKED"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "AMENDED 2026-10-13 ~23:5xZ (ruling on S6), MDPF_DEMQUE.TO-DQ-t58 item (1): 'lock.check over the appended rows with the trades that fall inside the appended window'. No valid_from is named for that check.",
    "world_is": "lock.check's early-third rule makes the check's valid_from decide whether an agreeing late-window trade can pass. The wired check anchors valid_from at the window's first in-window trade, so the early-third rule applies to the window's own trades; the 90 pct floor and the three-trade minimum are unchanged. The issuer is asked to confirm this reading or name another valid_from. Nothing is written by this row."
  },
  {
    "id": "MDPF_DEMQUE-D1-W50-S8",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~50",
    "surfaced_at": "2026-10-14T04:05:05Z",
    "one_line": "AC2 (dq_t58_equal.py) was NOT re-run after the second applicability rule: its live --spot 5 --tr needs 5 Yahoo requests, the budget is spent (125 of 120) and no new spot is pre-approved. The 50-name report and its live spot are carried from commit 80a8479c2f; the issuer grades AC2 on the existing report.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D8/MDPF/MDPF_DEMQUE/task-orders/MDPF_DEMQUE.TO-DQ-t58.wire-yahoo-incremental.md at c11bc60ca9: AMENDED 2026-10-14 ~00:2xZ, 'AC2's live --spot 5 --tr is NOT pre-approved again'",
        "org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~50/INCREMENTAL_WIRED_EQUALITY_REPORT.json at 80a8479c2f (the 50-name report, unchanged by this pass)",
        "whole-store census of this pass (read only, no Yahoo): held names LCEYX and FTHSX are still REJECTED:LOW_TRADE_AGREEMENT with trades_before_window 0"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "AMENDED 2026-10-14 ~00:2xZ, MDPF_DEMQUE.TO-DQ-t58: 'The 50-name equality report and the Yahoo budget are unchanged ... run AC2 only if its report file and a spot result already on your branch satisfy it; if the check cannot pass without a new Yahoo request, say so in the report and file a row'.",
    "world_is": "AC2 was not run this pass. The second rule changes the relock step only for names with a trade before their stored window; the held list of the whole-store census is unchanged for the two sample names it holds (LCEYX, FTHSX). The report's relock_measured key was produced under the previous rule and may list names the new rule does not relock. Nothing is written by this row."
  },
  {
    "id": "MDPF_DEMQUE-D1-W50-S9",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~50",
    "surfaced_at": "2026-10-14T04:05:05Z",
    "one_line": "The ninth named test builds its stored window from the helper's DAYS range (the first trading day 90 calendar days before the frontier), not from 2026-04-14 as the order's synthetic description reads. The rule tested depends on the order of the dates, not on the start date.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/test_demque_incremental_wiring.py at c11bc60ca9: DAYS = tc.trading_days_between(F - timedelta(days=90), F); _store_name writes the stored window from DAYS[0]",
        "the ninth test, added this pass: test_a_name_with_some_trades_before_the_stored_window_is_not_held_by_the_combined_check_and_is_listed_without_relock, one trade on 2019-11-22 and two trades on DAYS[1] and DAYS[2]; WIRE-OK 9 of 9"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "AMENDED 2026-10-14 ~00:2xZ, item (3) of MDPF_DEMQUE.TO-DQ-t58: 'synthetic: one trade in 2019 and two inside the stored window from 2026-04-14, stored lock LOCKED with 3 observations'.",
    "world_is": "The synthetic helpers start the stored window at DAYS[0], so the stored window does not begin on 2026-04-14. The 2026-04-14 date appears in the order as the real-store probe's start and is not a helper input. The stored lock carries observations_checked 3 and observations_passed 3 as the order requires. Nothing is written by this row."
  },
  {
    "id": "MDPF_DEMQUE-D1-W50-S10",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~50",
    "surfaced_at": "2026-10-14T04:05:05Z",
    "one_line": "Under the second rule, 238 of the 483 stored names carry a trade before their stored window and are appended without the combined relock. Where their appended window also holds no trade, no identity check runs on their appended days at all; the receipt lists them under appended_without_relock.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~Q1",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "whole-store census of this pass (read only): not_applicable 238 of 483 names (before the change: 188); applicable 165; locked 151; held 14",
        "data/mdpf/scripts/demque/daily_draw.py window_relock at c11bc60ca9: returns None when no trade falls in (stored max, frontier], and combined_relock returns None under the second rule for a not_applicable name, so neither check runs on those appended days"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "MDPF_DEMQUE.TO-DQ-t58 item 4 (pair A condition 2): 'After building the appended window, run lock.check on the appended days.' The amended order's rule (AMENDED 2026-10-14 ~00:2xZ) lists such a name as appended_without_relock and proceeds after the appended-window check.",
    "world_is": "The census counts 238 names with a trade before the stored window. How many of them also have no trade in the appended window was not measured this pass; for each of those the appended days are written with no identity check. The first nightly run after the merge would write them unless the issuer decides otherwise. Nothing is written by this row."
  }
]
```

## Row filed by 2.0.0_SA_COO~Q1 (the stored-rows relock is not the full-history relock; measured on the real store)

```json
{
  "id": "MDPF_DEMQUE-D1-S17",
  "project": "MDPF_DEMQUE",
  "fabric": "dell1",
  "surfaced_by": "2.0.0_SA_COO~Q1",
  "surfaced_at": "2026-10-14T04:19:34Z",
  "one_line": "A relock over a name's STORED rows alone is not the full-history relock: the store keeps only the held window, so a name with any trade dated before that window reads REJECTED on the stored rows while its stored lock proved the identity on the full history.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "DQ-t-58 order amendment ~23:0xZ 2026-10-13 (issuer): the wired incremental path runs a no-network relock over stored as_traded_close plus the appended rows, which the issuer expected to reproduce the full-history lock.check.",
  "world_is": "Measured 2026-10-14 by a read-only census of the real store (S3 and the client transactions, no Yahoo): over 326 names the stored-rows relock read REJECTED for 121 of 265 names with trade rows while their stored locks read LOCKED (107 REJECTED:PRICE_MISMATCH with every trade before the stored window; 14 REJECTED:LOW_TRADE_AGREEMENT with every trade inside); over 483 names after the 22:30 ET run, 3 more PRICE_MISMATCH (FUEPX, FWMMX, ORCL) with trades both before and inside the window (stored observations passed 7 of 7, 13 of 13, 30 of 33; stored rows alone see 1, 1 and 3). The combined check now runs only where no trade predates the stored window and one lies inside it; the whole-store census then holds the 14 real names and 0 price-mismatch names. Left unfixed, the first wired night would have held about 110 healthy names and opened as many false REJECTED rows on the unresolved list.",
  "disposition": "UNDER_INVESTIGATION",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/MDPF/MDPF_DEMQUE/task-orders/MDPF_DEMQUE.TO-DQ-t58.wire-yahoo-incremental.md (amendments ~00:1xZ and ~00:2xZ 2026-10-14)",
      "incremental_equal.py --relock-census (merged @ea0dd99e4e), RELOCK_CENSUS_WHOLE_STORE.json under deliverables/0.9.0_WK_MDPF_DEMQUE~50/",
      "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/DISARM_EVIDENCE_D1_W50_S2_S6_S10_20261014.md"
    ]
  }
}
```

## Rows filed by 0.9.0_WK_MDPF_DEMQUE~53 (DQ-t-61, merged by the issuer: union by id of the worker branch onto HEAD)

```json
[
  {
    "id": "MDPF_DEMQUE-D1-W53-S1",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~53",
    "surfaced_at": "2026-10-14T04:17:40Z",
    "one_line": "The order's message-file instruction ends each commit with a Co-Authored-By line naming Claude Sonnet 5.5, but the agent executing this order is Claude Haiku 5.5; the commits of this order carry the Haiku 5.5 trailer.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Order MDPF_DEMQUE.TO-DQ-t61 (dispatch instruction): the commit message file ends with 'Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>'.",
    "world_is": "The executing model is Claude Haiku 5.5 (claude-haiku-5-5). The session attribution instruction for commits this agent creates names Claude Haiku 5.5. The commits of this order end with 'Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>'; the --author identity is the one ordered (0.9.0_WK_MDPF_DEMQUE~53). The same mismatch is recorded as MDPF_DEMQUE-D1-W52-S1. No check or verdict depends on the trailer's model name.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D8/MDPF/MDPF_DEMQUE/task-orders/MDPF_DEMQUE.TO-DQ-t61.yahoo-failed-14-bloomberg-request.md (Bounds and REPORT wording) @838bd5190c",
        "session attribution instruction for commits created by this agent (Claude Haiku 5.5) @838bd5190c",
        "org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md (row MDPF_DEMQUE-D1-W52-S1, the same mismatch) @838bd5190c"
      ]
    }
  }
]
```

## Rows filed by 0.9.0_WK_MDPF_DEMQUE~54 (DQ-t-62, workstream SYMBOLFORMS; the branch's copy, appended at its end)

```json
[
  {
    "id": "MDPF_DEMQUE-D1-W54-S1",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~54",
    "surfaced_at": "2026-10-14T04:35:14Z",
    "one_line": "The order's commit instruction ends each commit with a Co-Authored-By line naming Claude Sonnet 5.5, but the executing agent is Claude Haiku 5.5; this order's commits carry the Haiku 5.5 trailer, as MDPF_DEMQUE-D1-W53-S1 recorded for DQ-t-61.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Order MDPF_DEMQUE.TO-DQ-t62 (dispatch instruction): each commit message file ends with 'Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>'.",
    "world_is": "The executing model is Claude Haiku 5.5 (claude-haiku-5-5). The session attribution instruction for commits this agent creates names Claude Haiku 5.5. The commits of this order end with 'Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>'; the --author identity is the one ordered (0.9.0_WK_MDPF_DEMQUE~54). The same mismatch is recorded as MDPF_DEMQUE-D1-W52-S1 and MDPF_DEMQUE-D1-W53-S1. No check or verdict depends on the trailer's model name.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D8/MDPF/MDPF_DEMQUE/task-orders/MDPF_DEMQUE.TO-DQ-t62.share-class-symbol-forms.md (REPORT wording, dispatch Co-Authored-By instruction) @8a38f47d30",
        "session attribution instruction for commits created by this agent (Claude Haiku 5.5) @8a38f47d30",
        "org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md (row MDPF_DEMQUE-D1-W53-S1, the same mismatch) @8a38f47d30"
      ]
    }
  }
]
```

## Rows filed by 0.9.0_WK_MDPF_DEMQUE~51 (DQ-t-59, merged by the issuer: union by id of the worker branch onto HEAD)

```json
[
  {
    "id": "MDPF_DEMQUE-D1-W51-S1",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~51",
    "surfaced_at": "2026-10-14T04:34:48Z",
    "one_line": "The order's message-file instruction ends each commit with a Co-Authored-By line naming Claude Sonnet 5.5, but the agent executing this order is Claude Haiku 5.5; the commits of this order carry the Haiku 5.5 trailer.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Order MDPF_DEMQUE.TO-DQ-t59 (dispatch instruction): the commit message file ends with 'Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>'.",
    "world_is": "The executing model is Claude Haiku 5.5 (claude-haiku-5-5). The session attribution instruction names Claude Haiku 5.5 for commits this agent creates, so the commits of this order end with 'Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>'. The same mismatch is recorded as MDPF_DEMQUE-D1-W52-S1 and MDPF_DEMQUE-D1-W53-S1. No check or verdict depends on the trailer's model name.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D8/MDPF/MDPF_DEMQUE/task-orders/MDPF_DEMQUE.TO-DQ-t59.porting-verdict-column.md (Proof of spec and REPORT wording) @2de831ee1b",
        "session attribution instruction for commits created by this agent (Claude Haiku 5.5) @2de831ee1b",
        "org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md (row MDPF_DEMQUE-D1-W53-S1, the same mismatch) @2de831ee1b"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W51-S2",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~51",
    "surfaced_at": "2026-10-14T04:34:48Z",
    "one_line": "The signed never-widen pair and the check docstring name 326 CUSIPs in the store; the live index read by the real preview holds 483 rows, so the stated row count is stale. AC2 accepts 300 or more, so its verdict is unaffected.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Never-widen pair B COO half (ledger/NEVER_WIDEN_R9_YAHOO_B_COO_HALF.md: 'the porting-test request (326 CUSIPs, 3,195 cells)' and 'row count 326') and dq_t59_real.py docstring ('rows == the number of CUSIP directories in the store (326 today, read live)').",
    "world_is": "The real index read by price_store.py --index-preview (S3 read only, verdicts file absent) returned rows=483, the nine old columns plus porting_verdict, every row UNVERIFIED, in this worker's run on 2026-10-14 before this row was surfaced. The figure 326 is from an earlier read and does not describe the store today.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D8/MDPF/MDPF_DEMQUE/ledger/NEVER_WIDEN_R9_YAHOO_B_COO_HALF.md @2de831ee1b",
        "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t59_real.py (docstring, arm 1) @2de831ee1b",
        "live read: python data/mdpf/scripts/demque/price_store.py --index-preview (rc=0; rows 483; sample_cusips 00039J772, 00130H105, 001419423) in this worker's run on 2026-10-14"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W51-S3",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~51",
    "surfaced_at": "2026-10-14T04:34:48Z",
    "one_line": "A plain script run of price_store.py cannot resolve lib.opal_naming, so the default S3 root (s3_root) would fail; the worker added a repo-root sys.path guard at the top of price_store.py, the same pattern priority_gate.py uses.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Order MDPF_DEMQUE.TO-DQ-t59 (AC2 invocation, run from the worktree root): python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t59_real.py runs price_store.py --index-preview against the real S3 index, with no PYTHONPATH set.",
    "world_is": "With PYTHONPATH unset, a script run puts the script directory on sys.path, not the repo root; 'import lib' resolves to an unrelated site-packages namespace package (pywin32 win32 lib) that has no opal_naming. s3_root() therefore cannot import lib.opal_naming on a plain run. The worker added ROOT (four levels up from the script) to sys.path in price_store.py, with a guard, before the pandas import. After that change AC2 reads VERDICT-REAL-OK.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/price_store.py s3_root() (from lib.opal_naming import address) @2de831ee1b",
        "data/mdpf/scripts/demque/priority_gate.py lines 26-30 (the ROOT sys.path pattern) @2de831ee1b",
        "measured in this worker's run on 2026-10-14: PYTHONPATH unset; find_spec('lib') from a cwd outside the repo returns the site-packages win32 namespace package"
      ]
    }
  }
]
```

## Rows filed by 0.9.0_WK_MDPF_DEMQUE~55 (DQ-t-63, workstream ETFSINTAKE; the branch's copy, appended at its end)

```json
[
  {
    "id": "MDPF_DEMQUE-D1-W55-S1",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~55",
    "surfaced_at": "2026-10-14T19:21:27Z",
    "one_line": "The dividend request counts 70 reference cells, one per security, but DVD_HIST_ALL is a bulk field that returns several event rows per security; the reference rule cannot price those rows, so the cell count is an undercount of what the draw returns.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Order MDPF_DEMQUE.TO-DQ-t63 (Worker Face, request 3): ETFS_RIVALS-C1-DIVIDENDS is a channel reference request with one cell per security under bbg_quote's reference rule, 70 cells for the pinned names file.",
    "world_is": "bbg_quote's reference rule prices securities x fields, one row each. DVD_HIST_ALL returns several dividend event rows per security. BACKFILL_GAPS_FOR_DEMQUE.md Row 3 (the issuer's measurement, not re-measured by this worker) cites 9,354 event rows for 724 securities, about 13 each, so the rows drawn are about thirteen times the 70 cells. The build writes a cells_claim_note into the request saying so. No rule in bbg_quote prices a bulk field per row, so the queue's ledger carries 70 cells for this request.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/round30/BACKFILL_GAPS_FOR_DEMQUE.md @c9e98081a6 (Row 3: 9,354 event rows, 724 securities)",
        "data/mdpf/scripts/demque/bbg_quote.py reference channel, cells = securities x fields, @9b7d894bcb",
        "build of 2026-10-13 in this worker's run on 2026-10-14 (ETFS_RIVALS-C1-DIVIDENDS cells 70, securities 70; rc=0)"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W55-S2",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~55",
    "surfaced_at": "2026-10-14T19:21:27Z",
    "one_line": "Eleven securities held by the Rival Funds or shown in a page dialog have no row in the security universe, so the owed set carries no Bloomberg ticker for them; 2,711 units are left out of the requests, under the 2 percent refusal line.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Order MDPF_DEMQUE.TO-DQ-t63 (Worker Face): the owed set gives a Bloomberg ticker for each security; a security with none is counted as no_ticker and left out; more than 2 percent of the units with no ticker refuses the build and files a BLOCKING row.",
    "world_is": "Build of 2026-10-13: no_ticker 2,711 units of 216,361 (1.25 percent: TR union 123,933 plus close union 89,717 plus 2,711). The eleven securities are BCS_US_Equity, BDORY_US_Equity, BYDDY_US_Equity, MER_PM_Equity, NVS_US_Equity, PST_IM_Equity, SAN_US_Equity, SU_CN_Equity, VALE3_BZ_Equity and ZURVY_US_Equity (no universe row on 2026-10-13), and JD_US_Equity (its universe row has last_seen 2025-06-02, before the 365-day window, so the owed read drops it). The G1 holdings and the dialog keys carry them in key form (security_id BCS_US_Equity), so the universe read does not resolve them. The build does not derive a ticker from the key form; the units are counted and left out, as the order directs.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/etfs/scripts/rivalfunds/history_owed.py owed(): universe rows with a blank security_bloomberg or a last_seen before the window are dropped, @9b7d894bcb",
        "universe read on 2026-10-13 (history_owed._universe): 1,058 rows; the eleven security_id values have no row with a ticker, JD_US_Equity has last_seen 2025-06-02",
        "data/mdpf/scripts/demque/etfs_rivals_intake.py plan_units() no_ticker count (this order's branch, uncommitted when this row was filed)"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W55-S3",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~55",
    "surfaced_at": "2026-10-14T19:21:27Z",
    "one_line": "Every request carries window_start 2025-10-13, so the build is valid only for --day 2026-10-13: bbg_quote refuses the requests for any later page day, and the build exits 2 with the rule named.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Order MDPF_DEMQUE.TO-DQ-t63 (Worker Face): the stage floor and every request window_start are 2025-10-13, and --day is a required argument with no default.",
    "world_is": "Measured in-process by this worker: a D30 request for need_date 2026-10-14 with window_start 2025-10-13 is refused by bbg_quote._validate with 'non_client window_start 2025-10-13 is more than 365 days before need_date 2026-10-14'. The 365-day rule moves with the need date and the order's floor does not, so the next page day needs a window design from the issuer. The build refuses rather than trims, as bbg_quote does, and writes no request for a later day.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/bbg_quote.py _check_window (non_client window_start more than 365 days before need_date refused), @9b7d894bcb",
        "in-process bbg_quote._validate on a D30 request, need_date 2026-10-14, window_start 2025-10-13: refused (this worker's run on 2026-10-14)"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W55-S4",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~55",
    "surfaced_at": "2026-10-14T19:21:27Z",
    "one_line": "The AC2 check dq_t63_real.py fails at its own line 81 (from lib import trading_calendar) on a plain run, because the check does not put the repo root on sys.path; with PYTHONPATH set to the worktree root the same invocation reads INTAKE-REAL-OK.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Order MDPF_DEMQUE.TO-DQ-t63, DQ9-t63-AC2 invocation: python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t63_real.py, run from the worktree root, expects INTAKE-REAL-OK.",
    "world_is": "Plain run, PYTHONPATH unset: the two builds ran and the check then raised ImportError: cannot import name 'trading_calendar' from 'lib' (unknown location) at dq_t63_real.py line 81, so no arm was graded. The same trap is recorded as MDPF_DEMQUE-D1-W51-S3: a plain run puts the script directory on sys.path, and lib resolves to an unrelated site-packages namespace package. With PYTHONPATH set to the worktree root the run reads INTAKE-REAL-OK (3 min 46 s; account-id oracle 0 hits against 29,617 hashes). The check sits outside this order's write grant and was not edited.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t63_real.py line 81 (the import inside main, after the two builds) @9b7d894bcb",
        "plain-run traceback and PYTHONPATH run of dq_t63_real.py in this worker's run on 2026-10-14",
        "org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md (row MDPF_DEMQUE-D1-W51-S3, the same trap) @9b7d894bcb"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W56-S1",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~56",
    "surfaced_at": "2026-10-15T17:59:51Z",
    "one_line": "The worktree's sparse checkout omits data/assets/scripts/silver/ and data/etfs/ (both tracked at HEAD), so the census cannot import p1_coverage and the real AC2 run fails at import before any S3 read; BLOCKING, not repaired.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "spec_asserts": "Order MDPF_DEMQUE.TO-DQ-t64 (DQ-t-64 build step 2 and its premise): the worktree carries the paths the order names, and the real census runs on the real inputs with p1_coverage.request_symbols as the symbol overlay. Invocation: python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t64_real.py, run from the worktree root, expects INACTIVE-REAL-OK.",
    "world_is": "Branch wk-MDPF_DEMQUE-56 at 7fb4e17444 is a sparse checkout (core.sparseCheckout true; 11 folders in the cone, none of data/assets or data/etfs). Both folders are absent on disk and tracked at HEAD (data/assets/scripts/silver: 138 files, including commonwealth_signs.py; data/etfs: 233 files). p1_coverage imports card_a_slice, which inserts data/assets/scripts/silver and imports commonwealth_signs, so the census fails at import: dq_t64_real.py prints INACTIVE-REAL-BAD census rc=1 with ModuleNotFoundError: No module named 'commonwealth_signs' in 0.96 s, before any S3 read. The folder run python -m pytest data/mdpf/scripts/demque is interrupted at collection: 16 errors, the first-error lines naming commonwealth_signs (6) and data.etfs (9), plus one FileNotFoundError in test_demque_land.py. The order's refusal route applies: no importable symbol resolver for the requested CUSIPs. Not repaired: widening the sparse cone or putting another checkout on sys.path would rebuild the tree outside this order's grant, and no copy of the census or of request_symbols was made. AC1 passes (INACTIVE-OK).",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/card_a_slice.py lines 58-61 (the data/assets/scripts/silver path insert and the import of commonwealth_signs) @7fb4e17444",
        "data/mdpf/scripts/demque/p1_coverage.py line 50 (import card_a_slice) @7fb4e17444",
        "git ls-files data/assets/scripts/silver = 138 and git ls-files data/etfs = 233 at 7fb4e17444; git config core.sparseCheckout = true; git sparse-checkout list = 11 folders, neither data/assets nor data/etfs; both folders ABSENT on disk in C:/dev/wk-demque-56",
        "the real-check run: python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t64_real.py, rc=1, INACTIVE-REAL-BAD census rc=1 ... No module named 'commonwealth_signs' (worker run 2026-10-15)"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W56-S2",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~56",
    "surfaced_at": "2026-10-15T18:04:54Z",
    "one_line": "After the issuer's cone change (S1 ruled as provisioning), python -m pytest data/mdpf/scripts/demque -q gives 221 passed and 4 failed: 3 are FileNotFoundError on integrations/bloomberg paths that the sparse cone omits, and 1 is an assertion mismatch in test_demque_bbg_ledger_upload.py that this worker did not diagnose; none is in inactive_set.py.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Order MDPF_DEMQUE.TO-DQ-t64 step 4 (the folder count for data/mdpf/scripts/demque, once) and the coordinator's ruling that the worktree now collects with no error.",
    "world_is": "Collection is clean (225 tests), but the run reads 221 passed and 4 failed. Failing: test_demque_bbg_backfill.py::test_backfill_stops_on_a_vendor_limit_warning[field] and [response] and test_demque_bbg_ledger_upload.py::test_name_to_literal_assignment_is_resolved_before_literal_eval raise FileNotFoundError on C:/dev/wk-demque-56/integrations/bloomberg/pipeline/etf_daily_pull.py and integrations/bloomberg/mcp/blp_client.py; the folder integrations/ is absent from the sparse cone and from disk. test_demque_bbg_ledger_upload.py::test_reads_record_lines_and_converts_rows_to_cells_per_mode fails an assertion ([48, 64, 5, None, 2] == [48, 64, 5, 14, 2]) whose cause is not diagnosed here. The census (inactive_set.py) and its tests pass.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python -m pytest data/mdpf/scripts/demque -q, worktree C:/dev/wk-demque-56 at d89ade551a, rc=1: 4 failed, 221 passed in 14.43s",
        "git sparse-checkout list at d89ade551a: no integrations entry; ls -d integrations ABSENT in the worktree",
        "data/mdpf/scripts/demque/test_demque_bbg_backfill.py and test_demque_bbg_ledger_upload.py (the four failing tests) @d89ade551a"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W57-S1",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~57",
    "surfaced_at": "2026-10-15T18:21:17Z",
    "one_line": "DQ-t-65 asks census() to gain the key tx_symbol_only AND says the DQ-t-64 tests pass unedited, but the DQ-t-64 test test_the_census_adds_up_classes_symbols_and_stored_against_the_inactive_total compares the whole census dict for exact equality, so an always-present key fails it; the cell emits the key only when a transactions source (non-empty tx_only) is supplied.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Order MDPF_DEMQUE.TO-DQ-t65 build item 3: census(...) gains tx_only=() and the dict gains the integer key tx_symbol_only; every existing key, identity and call keeps its meaning (the DQ-t-64 tests pass unedited).",
    "world_is": "With the key always present, test_demque_inactive_set.py:59 fails (pytest: 'Left contains 1 more item: tx_symbol_only'; the left dict holds 15 keys, the DQ-t-64 expected dict 14). The cell therefore sets tx_symbol_only only when tx_only is non-empty: a call with the DQ-t-64 arguments returns the DQ-t-64 dict unchanged, and the real census (tx_only supplied) carries the key with the same value that AC2 checks. Both AC1 and AC2 pass under this reading; the DQ-t-64 test file is unedited (it is outside this order's grant).",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python -m pytest data/mdpf/scripts/demque -q, worktree C:/dev/wk-demque-57 with census key always present, rc=1: 'FAILED test_demque_inactive_set.py::test_the_census_adds_up_classes_symbols_and_stored_against_the_inactive_total', 'Left contains 1 more item: tx_symbol_only: 0', at data/mdpf/scripts/demque/test_demque_inactive_set.py:59 @270e1c6175",
        "after the conditional key: python -m pytest test_demque_inactive_set.py test_demque_inactive_symbols.py -> 6 passed, rc=0 (worktree C:/dev/wk-demque-57 on wk-MDPF_DEMQUE-57, base 270e1c6175)"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W58-S1",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~58",
    "surfaced_at": "2026-10-15T18:51:05Z",
    "one_line": "DQ-t-66 criterion AC2 cannot be met as written: the check reads a securities list from the extend_frontier.py --plan JSON line, and the CLI pops that list before printing (unchanged by this cell), so the check fails at its securities clause.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "spec_asserts": "Order MDPF_DEMQUE.TO-DQ-t66 criterion DQ9-t66-AC2 (dq_t66_real.py): extend_frontier.py --plan shows excluded_active above 0, no V2 CUSIP in the day's securities, 1 to 380 symbols, excluded_p2 and excluded_p3 both 0; the check requires the securities list on that line to be 1..380 entries equal to symbols.",
    "world_is": "extend_frontier.py main() runs p.pop(\"securities\") before it prints the --plan line, so the line carries no securities list. The check's first clause passes on the real line (excluded_active 528, excluded_p2 0, excluded_p3 0, symbols 6) and then prints GATE-REAL-BAD 'the securities list is not 1..380 entries equal to symbols' (rc=1). Read only, in-process plan(): securities 6, V2 CUSIPs in securities 0, V2 set 3368. The CLI print is not changed by this order, so the criterion stays unmet as written; the order is left open.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "extend_frontier.py@5e62883899 line 483: p.pop(\"securities\") before print(json.dumps(p)) in main() under --plan",
        "python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t66_real.py in worktree C:/dev/wk-demque-58 (with the DQ-t-66 change): stdout 'plan symbols=6 excluded_active=528 excluded_p2=0 excluded_p3=0' then 'GATE-REAL-BAD the securities list is not 1..380 entries equal to symbols', rc=1",
        "scratch .scratch/v2_securities_check.py (in-process plan(), counts only): symbols=6 securities=6 v2_cusips_in_securities=0 excluded_active=528 excluded_p2=0 excluded_p3=0; v2_set_size=3368"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W58-S2",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~58",
    "surfaced_at": "2026-10-15T18:51:05Z",
    "one_line": "The Yahoo gate reaches only client-class requests, so an active (V2) CUSIP in a non_client request still draws on Yahoo, against the cell's 'never drawn or extended on Yahoo'.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Order MDPF_DEMQUE.TO-DQ-t66 cell: 'a name in V2 is never drawn or extended on Yahoo'; build item 2: the daily draw's default gate becomes pg.yahoo_excluded_for and everything else in run is unchanged.",
    "world_is": "demand_queue.gated() returns every security of a request for which is_gated() is false, and is_gated() is false for need_class non_client, so the gate passed to draw() never reaches a non_client request. A V2 CUSIP in a non_client request (research scanner, TR comparison, positioning, pre-flight) is therefore drawn on Yahoo. The order's test name pins the client-request scope ('of a client request'), so the code follows the order; the scope question is for the issuer.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "demand_queue.py@5e62883899 lines 51-55: is_gated returns req.get(\"need_class\") != NON_CLIENT",
        "demand_queue.py@5e62883899 lines 63-69: gated() returns list(req[\"securities\"]), [] when not excl or not is_gated(req)"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W58-S3",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~58",
    "surfaced_at": "2026-10-15T18:51:05Z",
    "one_line": "Once a name is active (V2) its Yahoo rows stop extending at the next standing apply, and nothing in this order places it on the Bloomberg leg, so lag_report omits it and its served history can go stale without a report.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Order cell: 'Active accounts should get BBG pricing exclusively' (Andrew-direct 2026-10-15); the Yahoo leg excludes V2 names from every tier.",
    "world_is": "The standing extension (extend_frontier._tiers) leaves each V2 name in no tier, so apply() no longer requests it on Yahoo; the existing Yahoo rows for those names keep their last valid_to. lag_report skips excluded names (excluded_active is counted, not their lag). This order does not verify that the Bloomberg leg holds a served price for every V2 name, so the staleness, if any, is unmeasured here.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "extend_frontier.py in worktree C:/dev/wk-demque-58 (uncommitted, DQ-t-66): _tiers leaves a name in excl out of known, so out of daily and rolling; lag_report continues past excl names",
        "real plan at 2026-10-15: excluded_active 528 of the landed names, rolling_not_landed 387, symbols 6"
      ]
    }
  }
  ,
  {
    "id": "MDPF_DEMQUE-D1-W60-S1",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~60",
    "surfaced_at": "2026-10-15T18:43:13Z",
    "one_line": "DQ-t-68 says old_columns_digest is the sha256 of the ten OLD columns and equals the DQ-t-59 value; the DQ-t-59 digest is over the nine old columns, the same order's step 1 counts the ten as INDEX_COLS including porting_verdict, and a digest over the live rows cannot equal the DQ-t-59 hash because the store grew from 483 to 538 rows; the build keeps the nine-column digest unchanged.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Order MDPF_DEMQUE.TO-DQ-t68 build item 4: old_columns_digest is still the sha256 of the ten OLD columns as CSV text (so it equals the DQ-t-59 value).",
    "world_is": "price_store.py at base 5e62883899 computes the digest over OLD_INDEX_COLS, which holds nine columns; the DQ-t-59 proof records the nine-column definition and its preview digest 5fe689fd2a76d2bb4ad5b65191ed4afb855056a408092f32952bacb3d2fdf2e9 at 483 rows. This build's real preview reads 538 rows and prints old_columns_digest 7621374ba954b05357cfa07b18722de024fc3f1afd873eb95c38400bd78a01f6, equal across two real reads. The digest is unchanged in code, so the spec's equality with the DQ-t-59 value holds only as a definition, not as a hash comparison on the live store.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/price_store.py@5e62883899 line 35: OLD_INDEX_COLS is nine columns; _index_preview digests df[OLD_INDEX_COLS]",
        "org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~51/MDPF_DEMQUE.TO-DQ-t59.porting-verdict-column.proof_of_spec.json controls.determinism: old_columns_digest 5fe689fd2a76d2bb4ad5b65191ed4afb855056a408092f32952bacb3d2fdf2e9 at 483 rows; the TO-DQ-t59 order defines the digest as sha256 of the nine old columns as CSV text",
        "python data/mdpf/scripts/demque/price_store.py --index-preview in worktree C:/dev/wk-demque-60 (branch wk-MDPF_DEMQUE-60): rows 538, old_columns_digest 7621374ba954b05357cfa07b18722de024fc3f1afd873eb95c38400bd78a01f6, read twice (rc=0 both)"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W60-S2",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~60",
    "surfaced_at": "2026-10-15T18:43:13Z",
    "one_line": "DQ-t-68 names org/surprise_channel/schemas/investigation_item.schema.json as the row schema; that path is absent from this worktree and no investigation_item.schema.json exists under org/, so the row is written in the form of the existing rows of this file.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Order MDPF_DEMQUE.TO-DQ-t68 Surprise clause: a surprise row conforms to org/surprise_channel/schemas/investigation_item.schema.json.",
    "world_is": "The schema path does not exist at worktree HEAD 5e62883899 (org/surprise_channel is not present) and a Glob of org/ for investigation_item.schema.json returns no file. The surprise-row gate .tools/surprise-row-gate.py is the commit-time check; its verdict is recorded in this worker's proof instance.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Glob pattern **/investigation_item.schema.json under C:/dev/wk-demque-60/org: No files found (read at 2026-10-15T18:43Z)",
        "ls org/surprise_channel and ls org/surprise_channel/schemas in worktree C:/dev/wk-demque-60 at HEAD 5e62883899: No such file or directory"
      ]
    }
  }
  ,
  {
    "id": "MDPF_DEMQUE-D1-W61-S1",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~61",
    "surfaced_at": "2026-10-16T01:18:29Z",
    "one_line": "inactive_request.py keeps NIGHTLY_CAP = 380, a fourth value of the shared pacer's daily request count, used by the nights arithmetic; the order names three places (the Pacer default, extend_frontier.DAILY_CAP, inactive_request.DAILY_CAP) and the build leaves NIGHTLY_CAP unchanged, so the nights figure now divides by 380 while the shared pacer admits 600 a day.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Order MDPF_DEMQUE.TO-DQ-t71 Build: the cap is a default in three places and they must agree; inactive_request.py changes DAILY_CAP only.",
    "world_is": "data/mdpf/scripts/demque/inactive_request.py at the worktree line 42 reads NIGHTLY_CAP = 380 with the comment 'the shared pacer's vendor requests a day for the draw', and line 127 computes nights = ceil(kept / NIGHTLY_CAP). After this order yahoo_pull.Pacer admits 600 requests a day, so the nights figure reads high by the ratio 600/380. Not changed: it is not one of the three named defaults.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/inactive_request.py@worktree branch wk-MDPF_DEMQUE-61 line 42: NIGHTLY_CAP = 380; line 127: nights = -(-len(kept) // NIGHTLY_CAP)",
        "data/mdpf/scripts/demque/yahoo_pull.py@worktree branch wk-MDPF_DEMQUE-61 line 155: Pacer daily_cap default 600 after this order"
      ]
    }
  }
  ,
  {
    "id": "MDPF_DEMQUE-D1-W61-S2",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~61",
    "surfaced_at": "2026-10-16T01:18:29Z",
    "one_line": "demand_queue.py's quote CLI keeps --daily-cap default=400, outside this order's grant; the pacer path quotes with the Pacer's own daily_cap (600 after this order), so a bare CLI quote and a Pacer-driven quote now disagree on the finish date.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Order MDPF_DEMQUE.TO-DQ-t71 Build: the cap is a default in three places and they must agree; the Pacer's default is the cap the quote counts.",
    "world_is": "data/mdpf/scripts/demque/demand_queue.py line 346 reads ap.add_argument('--daily-cap', type=int, default=400); line 285 quotes with pacer.daily_cap. demand_queue.py is not in this order's <paths>, so it is not edited.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/demand_queue.py@worktree branch wk-MDPF_DEMQUE-61 line 346: --daily-cap default=400; line 285: quote(req, 0, pacer.daily_cap, today_s)",
        "data/mdpf/scripts/demque/yahoo_pull.py@worktree branch wk-MDPF_DEMQUE-61 line 155: Pacer daily_cap default 600 after this order"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W63-S1",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~63",
    "surfaced_at": "2026-10-16T16:16:11Z",
    "one_line": "The whole demque test folder does not pass at HEAD in worktree wk-MDPF_DEMQUE-63: 5 tests fail before any edit (5 of 243) and after this order's edits (5 of 249), because the worktree is a sparse checkout whose list omits integrations/.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Order MDPF_DEMQUE.TO-DQ-t73 Build 5: run the whole folder once, no failure; the test files in the folder are read against the tree the order names.",
    "world_is": "git sparse-checkout list in the worktree has 13 entries (data/mdpf/scripts/demque and org/missions/D8/MDPF/MDPF_DEMQUE among them, no integrations/); integrations/bloomberg/pipeline/etf_daily_pull.py is tracked at HEAD (git ls-files) but absent on disk. Failing at HEAD: test_demque_active_windows.py::test_the_pinned_active_set_is_the_v2_file_and_a_v1_hash_is_refused; test_demque_bbg_backfill.py::test_backfill_stops_on_a_vendor_limit_warning [field] and [response]; test_demque_bbg_ledger_upload.py::test_reads_record_lines_and_converts_rows_to_cells_per_mode and ::test_name_to_literal_assignment_is_resolved_before_literal_eval. Result after edits: 5 failed, 244 passed (238 at HEAD plus the 6 new tests in test_demque_budget.py).",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git -C C:/dev/wk-MDPF_DEMQUE-63 sparse-checkout list: 13 entries, no integrations/ entry",
        "data/mdpf/scripts/demque/test_demque_active_windows.py@worktree branch wk-MDPF_DEMQUE-63: FileNotFoundError on integrations/bloomberg/pipeline/etf_daily_pull.py (pytest run, 5 failed 238 passed before edits; 5 failed 244 passed after)",
        "git ls-files integrations/bloomberg/pipeline/etf_daily_pull.py@worktree branch wk-MDPF_DEMQUE-63: tracked (positive control), ls integrations/bloomberg/pipeline/ on disk: No such file or directory"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W64-S1",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~64",
    "surfaced_at": "2026-10-17T04:28:49Z",
    "one_line": "bbg_backfill.run draws up to the quote's allowance_today and passes no drawn_surface_today, so a surface-tagged request it runs (the D-tagged DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS) reads the full budgets.surfaces.D room even on a day the drawer already drew surface D.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~Q1",
    "spec_asserts": "DQ-t-69 THE RULE (CTO ruling 1.0.0_SA_CTO~DELL1, 2026-10-17): a surface-tagged request draws against its surface room less the surface cells drawn today. bbg_backfill.py is not in the order's <paths>, so its quote call was not edited.",
    "world_is": "data/mdpf/scripts/demque/bbg_backfill.py line 111 calls bbg_quote.quote(request, allowance, _spent(today, actuals), today) with no drawn_surface_today; line 112 takes room = quote['allowance_today'] and lines 141-142 cap every draw at room. The quote of a surface-D request is now budgets.surfaces.D (100000) less drawn_surface_today, which this call leaves at 0. test_demque_bbg_backfill.py::test_backfill_stops_at_the_days_allowance asserted the old 5858 ceiling for this request and was edited to 100000 (named in the worker report).",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/bbg_backfill.py@626c692706 lines 110-112 (quote and room), lines 141-142 (room caps every draw)",
        "org/missions/D8/MDPF/MDPF_DEMQUE/requests/DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS.json@626c692706 line 2 (\"surface\": \"D\")",
        "data/mdpf/scripts/demque/test_demque_bbg_backfill.py@wk-MDPF_DEMQUE-64 lines 59-63 (the edited assertion; worktree, uncommitted at filing)"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W64-S2",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~64",
    "surfaced_at": "2026-10-17T04:28:49Z",
    "one_line": "The untagged history figure also adds the production budget ledger for the day, which holds the drawer's own draws (surface draws included) under their UTC date, so a surface draw can reduce the untagged room on a day whose UTC date it was recorded under; the rule 'a surface draw never shrinks the untagged ceiling' is not met across a UTC-midnight run.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~Q1",
    "spec_asserts": "DQ-t-69 Room in the drawer: leave out of the untagged figure the actuals-ledger cells of surface-tagged jobs, so a surface draw never shrinks the untagged ceiling; keep production's cells as they are.",
    "world_is": "bbg_budget.record writes each draw to bbg_budget_<UTC date of the draw>.jsonl. bbg_ledger_upload.rows_for_day(D) reads that file and converts mode demque-backfill to channel history (CELLS_PER_ROW). standing_drawer._drawn_history_today(D) adds those rows to the untagged figure, and the spec leaves them in. A drawer run on a local evening can write its draws under the next UTC day, so the next day's untagged room (and day_room --room) is reduced by surface draws. The same budget-ledger rows also repeat the drawer's own untagged draws already counted from the actuals ledger (a double count that was already in the base code and is unchanged). test_demque_surface_room.py makes bbg_budget.record a no-op, so no test figure depends on the wall clock.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/bbg_ledger_upload.py@626c692706 lines 112-131 (rows_for_day reads bbg_budget_<day>.jsonl; demque-backfill maps to history)",
        "data/etfs/scripts/rivalfunds/bbg_budget.py@626c692706 line 30 (ENV_DIR) and the record path (UTC day file)",
        "data/mdpf/scripts/demque/standing_drawer.py@wk-MDPF_DEMQUE-64 _drawn_history_today (budget ledger term kept as spec'd; worktree, uncommitted at filing)"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W64-S3",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~64",
    "surfaced_at": "2026-10-17T04:28:49Z",
    "one_line": "The order names the drawn_surface_today keyword of quote only; the --quote --actuals CLI path was also made surface-aware, which the order did not ask for.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "DQ-t-69 Build 1: bbg_quote.py gains surface_budget, the drawn_surface_today keyword, the tagged walk and record_actual(surface=None). The CLI quote path is not named.",
    "world_is": "bbg_quote.main --quote with --actuals now passes REQUESTS_DIR and the allowance to _actuals_drawn (surface rows are left out of drawn_today for history) and, for a surface-tagged request, passes drawn_surface_today from surface_drawn_today. Without this the CLI quote of a tagged request would ignore the surface's draws today. The order's AC2 (no --actuals) is unaffected.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/bbg_quote.py@wk-MDPF_DEMQUE-64 main() --quote branch and _actuals_drawn (worktree, uncommitted at filing)",
        "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R10_CHECKS/dq_t69_real.py@626c692706 (AC2 invocation without --actuals)"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-Z-S6",
    "project": "MDPF_DEMQUE",
    "fabric": "site-z",
    "surfaced_by": "0.7.0_AE_CloudOps~MDPF1",
    "surfaced_at": "2026-10-17T14:10:15Z",
    "one_line": "The 2026-10-17 14:00Z fire read the new surface budgets but drew no surface-C cell: the run STOPPED on an empty vendor response in a surface-B request ahead of C, so DQ9-t70-AC2 reads FIRE-BAD.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "spec_asserts": "TO-DQ-t70: after the 2026-10-17 14:00Z fire, surface C drew more than 5,858 and at most 400,000 cells, and no row stopped on a vendor limit (AC2 dq_t70_fire.py FIRE-OK).",
    "world_is": "MEASURED: run.2026-10-17.started.json shows surface_rooms C 400000 and daily_total_left 2500000, so the DQ-t-69 code ran. The receipt reads outcome STOPPED, stop_reason EMPTY_OR_INCOMPLETE_RESPONSE, cells_drawn 5618 (surface D 1004 for DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS, surface B 4614 for ADVI_COTBKF-COTTONWOOD-HIST-T1-01), 55 attempts; the last attempt, /cusip/78658RKQ3 2022-11-22..2023-05-26, returned 0 rows (standing_drawer.py:861 turns that into a run-level stop). No request tagged surface C was reached: dq_t70_fire.py prints 'FIRE-BAD surface-tagged cells 5618 are not past the 5858 history ceiling' (surface cells B 4614, D 1004; C none), dq_t69_room.py still SURF-OK. The task result is 2. INFERRED, not measured: a security that stored no rows keeps the same cursor, so the 2026-10-18 fire may ask the same window of the same security first and stop there again, leaving surface C undrawn; the 5,858 ceiling and the C room are not the limiting factor. No draw was run by hand (order step 5).",
    "disposition": "UNDER_INVESTIGATION",
    "disarm_owner": "2.0.0_SA_COO~Q1",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier2_senior/0.7.0_AE_CloudOps/deliverables/MDPF_DEMQUE_ZQ_STANDING/receipt.2026-10-17.json (attempts[-1], stop_reason, requests)",
        "org/missions/D8/MDPF/MDPF_DEMQUE/ledger/BBG_ACTUALS.jsonl (2 rows dated 2026-10-17, both STOPPED)",
        "data/mdpf/scripts/demque/standing_drawer.py@08e393fd01 line 861"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-Z-S7",
    "project": "MDPF_DEMQUE",
    "fabric": "site-z",
    "surfaced_by": "0.7.0_AE_CloudOps~MDPF1",
    "surfaced_at": "2026-10-17T14:10:15Z",
    "one_line": "TO-DQ-t34 AC2 cannot now read CLOSE-OK: the TR request drew its last 1004 cells on 2026-10-17 but was recorded STOPPED, so no COMPLETE row will be written.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "spec_asserts": "TO-DQ-t34 build item 3: the run whose draws leave every security of a request at its end records that request's ONE line as COMPLETE; AC2 dq_t34_close.py reads exactly one COMPLETE row for the TR request with cells_drawn > 0 (CLOSE-OK).",
    "world_is": "MEASURED: the 2026-10-17 actuals row for DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS reads cells_drawn 1004, outcome STOPPED, stop_reason EMPTY_OR_INCOMPLETE_RESPONSE; standing_drawer.py --plan --request DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS now prints remaining_cells 0, and --open no longer lists it, so the request is complete. standing_drawer.py:1066 sets every attempted request's outcome to STOPPED whenever the run carries a stop reason (it checks 'reason' before request_complete), and the stop came from the surface-B request (see MDPF_DEMQUE-Z-S6), not from TR. dq_t34_close.py prints 'CLOSE-BAD no COMPLETE row yet (3 rows for the job, 12720 cells drawn)'. A complete request is skipped at the start of a run with no actuals line (:1058-1060), so the 2026-10-18 fire will write none: the one COMPLETE row t34 expects has no way to appear. The deploy-ledger entry mdpf-demque-zq-t34-close L3 expires 2026-10-17T18:53Z. Not changed: the drawer, the task, and the three files.",
    "disposition": "UNDER_INVESTIGATION",
    "disarm_owner": "2.0.0_SA_COO~Q1",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D8/MDPF/MDPF_DEMQUE/ledger/BBG_ACTUALS.jsonl (TR row 2026-10-17)",
        "data/mdpf/scripts/demque/standing_drawer.py@08e393fd01 lines 1058-1070 and 485-488",
        "org/critical_paths/.open_deploys/mdpf-demque-zq-t34-close.json (L3 open)"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W65-S1",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~65",
    "surfaced_at": "2026-10-17T14:36:37Z",
    "one_line": "A run stopped by a bookkeeping exception has no stopping request, so DQ-t-74's per-request rule reads every attempted request DRAWN or COMPLETE under a STOPPED run.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "DQ-t-74: a request reads STOPPED when the run's stop reason came from THIS request, i.e. got['stop'] is set on this entry; the draw loop breaks on the first stop, so at most one attempted request carries it.",
    "world_is": "run() wraps the draw loop in a try whose except Exception sets the run's reason with no got['stop'] on any entry (standing_drawer.py@836e16bafd lines 1042-1043). A fault raised inside _draw_history also loses that request's got, since it is never appended to attempted. The edit implements the stated rule literally: such a run reads its attempted requests COMPLETE or DRAWN, and the run result reads STOPPED with the exception as its reason. The order does not name this path.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/standing_drawer.py@836e16bafd lines 1042-1043 (except Exception sets reason; no got stop)",
        "data/mdpf/scripts/demque/standing_drawer.py@wk-MDPF_DEMQUE-65 run() outcome loop (worktree, uncommitted at filing)"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W65-S2",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~65",
    "surfaced_at": "2026-10-17T14:36:37Z",
    "one_line": "Every actuals line of a stopped run carries the run's stop_reason, so after DQ-t-74 a DRAWN line can name a stop that another request caused.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "DQ-t-74: the RUN-level result is unchanged, the receipt's stop_reason is unchanged, and nothing else changes.",
    "world_is": "run() passes line_reason = reason to bbg_quote.record_actual on every line that is not REFUSED or GATED (standing_drawer.py@836e16bafd lines 1106-1111 region), and record_actual writes stop_reason whenever it is not None (bbg_quote.py@836e16bafd lines 852-853). A COMPLETE line of a stopped run already carried the run's reason before the edit; the edit adds the same to DRAWN lines of a stopped run. No reader in data/mdpf/scripts/demque that was grepped tests stop_reason on a DRAWN line. The line-level reason was left as the order says.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/standing_drawer.py@836e16bafd lines 1101-1111 (line_reason = reason for every non-GATED line)",
        "data/mdpf/scripts/demque/bbg_quote.py@836e16bafd lines 838-853 (record_actual writes stop_reason when not None)"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W65-S3",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~65",
    "surfaced_at": "2026-10-17T14:36:37Z",
    "one_line": "The surprise-channel schema the system names is absent from this worktree: the worktree is sparse-checked-out and org/surprise_channel is outside its materialized set, though tracked at HEAD.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Investigation rows conform to org/surprise_channel/schemas/investigation_item.schema.json.",
    "world_is": "core.sparseCheckout is true in the worktree. org/surprise_channel does not exist on disk (ls fails) while git ls-files lists its files at HEAD; the schema file is not under org/ (Glob, zero matches). The org tree holds 23 materialized entries against 76840 tracked files. This row follows the shape of the rows already in INVESTIGATION_v1.md instead of the schema.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git config core.sparseCheckout in the worktree wk-MDPF_DEMQUE-65 (true); git ls-files org/surprise_channel at 836e16bafd (lists tracked rows)",
        "org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md@836e16bafd (row shape reference)"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W65-S4",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~65",
    "surfaced_at": "2026-10-17T14:59:06Z",
    "one_line": "An INCOMPLETE vendor return (rows missing a requested field) is stored into the history identity before the check that stops the run, so the stored row is never asked again.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "DQ-t-75: an INCOMPLETE return (rows present but a requested field missing) still stops the run, exactly as today.",
    "world_is": "The run stops on an incomplete return, but _draw_history first extends res rows, cells and the stored identity with the returned dates (standing_drawer.py@69b52bb6cf lines 848-852), and only then tests the fields (line 860). The stored dates make undrawn_runs skip those days on every later fire, so the field-less row is never re-requested. The t75 edit leaves this order as it was; the t74 stop tests now cite its two counted cells. Fires on an incomplete vendor return only; no such return is in the records this worker read.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/standing_drawer.py@69b52bb6cf lines 848-852 (rows, cells and stored identity written before the check)",
        "data/mdpf/scripts/demque/standing_drawer.py@69b52bb6cf line 860 (the incomplete-row stop)",
        "data/mdpf/scripts/demque/standing_drawer.py@wk-MDPF_DEMQUE-65 _draw_history (worktree, uncommitted at filing)"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W65-S5",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~65",
    "surfaced_at": "2026-10-17T14:59:06Z",
    "one_line": "A request whose only owed windows are cooled reads DRAWN with 0 cells and writes a 0-cell actuals line on each fire of its cooldown.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "DQ-t-75: an empty window draws zero cells, writes no rows and adds no actuals cells; the request_complete rule is unchanged. The order does not state the actuals line for such a request.",
    "world_is": "run() outcome rules are unchanged, so an attempted request with no stop, no refusal and no cells reads DRAWN (standing_drawer.py@wk-MDPF_DEMQUE-65 outcome loop), and record_actual writes one line for every such request (the actuals loop skips only GATED and REFUSED-without-cells). A cooled window therefore produces one 0-cell DRAWN line per fire until its seventh day. Before this order the same window stopped the run and wrote a STOPPED line, so a line per fire is not new; the 0-cell DRAWN form is. Tests assert the 0-cell line is absent only after completion.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/standing_drawer.py@wk-MDPF_DEMQUE-65 run() outcome loop and the ONE actuals line per request loop (worktree, uncommitted at filing)",
        "data/mdpf/scripts/demque/test_demque_standing_drawer_close.py@836e16bafd test_no_zero_cell_drawn_line_after_completion (the completion-only assertion)"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W65-S6",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~65",
    "surfaced_at": "2026-10-17T14:59:06Z",
    "one_line": "The empty-window record is keyed by the owed run's first and last day, not by the attempted chunk's window, because the chunk's stop moves with the room.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "DQ-t-75: the cooldown key is (request_id, security identifier, window start, window stop).",
    "world_is": "The attempted chunk runs from its start for cap = min(128, room // 2) rows, so the same undrawn window gets a different stop on a fire with a different room. A key on the chunk would not match the next fire. The key used (standing_drawer.py _window_key) takes the owed run's first and last undrawn trading day; nothing stores rows inside an empty run, so both ends hold until a later fire draws it. A second request that stores rows inside the same security splits the run and changes the key, so that window is asked again once; not tested.",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/standing_drawer.py@wk-MDPF_DEMQUE-65 _window_key, _empty_window and _cooldown_gate (worktree, uncommitted at filing)",
        "data/mdpf/scripts/demque/standing_drawer.py@69b52bb6cf _draw_history chunk cap = min(CHUNK_ROWS, avail // per_row)"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-Z-S8",
    "project": "MDPF_DEMQUE",
    "fabric": "site-z",
    "surfaced_by": "0.7.0_AE_CloudOps~MDPF1",
    "surfaced_at": "2026-10-18T14:08:08Z",
    "one_line": "The 2026-10-18 14:00Z fire drew 0 history cells (every history request REFUSED on an empty probe), and DQ9-t70-AC2 is hard-dated to 2026-10-17 so no later fire can turn it to FIRE-OK.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "spec_asserts": "TO-DQ-t70: AC2 dq_t70_fire.py reads FIRE-OK from the rows of the 2026-10-17 14:00Z fire (surface-tagged cells more than 5858, within each surface budget and the daily total, no vendor-limit stop); the order stays open until it reads FIRE-OK. Rows Z-S6 and Z-S7 stay open until the 2026-10-18 fire.",
    "world_is": "MEASURED: dq_t70_fire.py carries DAY = '2026-10-17' as a constant and prints 'FIRE-BAD surface-tagged cells 5618 are not past the 5858 history ceiling' (B 4614, D 1004; the 10-17 fire stopped on an empty window, Z-S6); that fire cannot recur, so AC2 as written cannot read FIRE-OK. The 2026-10-18 fire (receipt.2026-10-18.json, task result 0) recorded outcome DRAWN, cells_drawn 51 (reference only: MDPF_SECHIST-CARD-A-B1-FUND-TYPE 1 cell REFUSED, AMGT_RESAPP-S14-CRNCY-SCANNER-US-SLICE1 50 cells COMPLETE), history rows 0; every history request in the queue was REFUSED with 'identifier form /cusip/ UNVERIFIED (probe response empty)': the one-row probe of /cusip/662858FV6 returned 0 rows, where the 2026-10-17 fire's probe of the same identifier read VERIFIED with 1 row. empty_windows is empty, so the DQ-t-75 cooldown was not exercised; the AMGT COMPLETE line shows DQ-t-74's per-request outcome recorded while other requests were refused. CAUSE NOT MEASURED: whether the empty probe is a vendor or Terminal state or a probe-window effect is unread. TR (remaining_cells 0) was correctly skipped, and TO-DQ-t34's CLOSE-OK still holds. Surface C has no open request (draw_hold), as the AC2 amendment states. The next draw-capable fire is Saturday 2026-10-24 14:00Z: 10-19 to 10-23 are trading days and draw nothing. ASK: the issuer amends AC2's date (or accepts the 10-17 reading as final and cuts a follow-up), and rules whether the empty history probe on 10-18 needs a cause read. Nothing was changed at site Z and no draw was run by hand.",
    "disposition": "UNDER_INVESTIGATION",
    "disarm_owner": "2.0.0_SA_COO~Q1",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier2_senior/0.7.0_AE_CloudOps/deliverables/MDPF_DEMQUE_ZQ_STANDING/receipt.2026-10-18.json (probes[0] verdict UNVERIFIED, requests[*] outcome REFUSED)",
        "org/missions/D8/MDPF/MDPF_DEMQUE/ledger/BBG_ACTUALS.jsonl (2 rows dated 2026-10-18, channel reference)",
        "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R10_CHECKS/dq_t70_fire.py line 21 (DAY constant)",
        "data/mdpf/scripts/demque/standing_drawer.py@eb9921cf9a lines 696-721 (_probe_history)"
      ]
    }
  },
  {
    "id": "MDPF_DEMQUE-D1-W66-S1",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~66",
    "surfaced_at": "2026-10-18T14:48:46Z",
    "one_line": "DQ-t-76 records an INCONCLUSIVE probe security as an empty window by the DQ-t-75 mechanism, but the reference channel has no day-keyed window record, so a skipped reference security is recorded nowhere and is probed again on the next fire (at most three probes per channel per run).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/standing_drawer.py@6c71bea6bc lines 813-847 (DQ-t-75 record: _window_key and _empty_window are day-keyed; _empty_window is called from the history channel only)",
        "data/mdpf/scripts/demque/standing_drawer.py@6c71bea6bc lines 965-995 (_draw_reference and its reference probe: no window or cooldown record on the reference channel)",
        "worktree data/mdpf/scripts/demque/standing_drawer.py _draw_reference while loop (TO-DQ-t76): an INCONCLUSIVE reference security is removed from this fire's todo and writes no record",
        "scratch check .scratch/ref_probe_check.py (uncommitted): one EMPTY reference probe is skipped, the next probe VERIFIED, two securities drawn, 4 cells, outcome DRAWN"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-DQ-t76 item 2: the probed security is skipped for this fire and recorded as an empty window by the DQ-t-75 mechanism (COOLED_NEW, seven days, listed in empty_windows).",
    "world_is": "The DQ-t-75 record is keyed by (request_id, identifier, first owed day, last owed day) of a history run; the reference channel has no days and so no record. Built as: a reference INCONCLUSIVE probe skips its security for the fire and writes nothing, so the same reference security is probed again on each later fire until its probe verifies or the three-probe cap caches UNVERIFIED for that fire. Each such fire spends one reference probe cell (the cap bounds it at three per run)."
  },
  {
    "id": "MDPF_DEMQUE-D1-W66-S2",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~66",
    "surfaced_at": "2026-10-18T14:48:46Z",
    "one_line": "The order makes the probe the FIRST /cusip/ security; the pre-existing probe site asked a COOLED window (DQ-t-75: no call, no cell), so the probe now asks the first undrawn run that is not cooled, the reading the no-second-call criterion requires.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/mdpf/scripts/demque/standing_drawer.py@6c71bea6bc lines 884-890 (the probe ran before the cooldown gate of the run loop, on runs[0][0] whatever its gate)",
        "data/mdpf/scripts/demque/standing_drawer.py@6c71bea6bc lines 891-896 (the DQ-t-75 gate: a COOLED window is not asked, no call and no cell)",
        "worktree data/mdpf/scripts/demque/standing_drawer.py _probe_run (TO-DQ-t76): the probe asks the first run whose gate is '' or RETRY; a security whose every run is cooled is not probed",
        "worktree data/mdpf/scripts/demque/test_demque_probe_empty.py test_the_skipped_probe_security_is_listed_in_the_receipt_and_cooled_for_seven_days (a second fire makes no vendor call for the skipped security)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-DQ-t76 criterion 4: a second fire inside seven days makes no vendor call for the skipped security; DQ-t-75: a window cooled by an earlier EMPTY return is not asked (no call, no cell).",
    "world_is": "At base the probe ran before the cooldown gate, so a cooled first /cusip/ security was probed on every fire and each probe was a call on a window already known empty. Built: the probe skips a security whose runs are all cooled and asks the first run that is not. The probe's cell count and the verdict rule are unchanged; only which security the probe asks differs, and only when the first /cusip/ security is cooled."
  },
  {
    "id": "MDPF_DEMQUE-D1-W66-S3",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_DEMQUE~66",
    "surfaced_at": "2026-10-18T14:48:46Z",
    "one_line": "The probe asks one day, but an INCONCLUSIVE answer cools the WHOLE undrawn run of that security for seven days, and the third INCONCLUSIVE security is recorded as an empty window as well; the order states neither reading.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "worktree data/mdpf/scripts/demque/standing_drawer.py _skip_empty_probe (TO-DQ-t76): _empty_window receives the probed run, the whole undrawn run from its first to its last owed day",
        "worktree data/mdpf/scripts/demque/standing_drawer.py _identifier_form (TO-DQ-t76): on_empty runs for every INCONCLUSIVE probe, including the PROBE_EMPTY_MAX-th, before the form caches UNVERIFIED",
        "data/mdpf/scripts/demque/standing_drawer.py@6c71bea6bc lines 696-727 (_probe_history asks max_data_points=1 on one day: start = end = the first owed day)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-DQ-t76 item 2: the probed security is recorded as an empty window (COOLED_NEW, seven days); item 3: the third distinct empty caches UNVERIFIED and the request is refused as today.",
    "world_is": "A one-day empty answer cools every owed day of that security's run for seven days (the run is the window the DQ-t-75 record keys), so the skip is wider than the day it asked. The third empty security is listed and counted toward the more-than-five stop like the first two, because the order does not say otherwise. Both readings are the ones built; neither is asserted by the order."
  }
]
```
