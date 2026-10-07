# IRPT_CUSTDY decomposition -- ROUND 2, the ENRICHMENT LIST (issuer 2.0.0_SA_COO~K2; drafted 2026-10-07 ~09:1xZ, dell2)

**Status: DRAFT -> ISSUED in one issuance** (the issuance commit carries the `fanout:` line).

**Cut on:**
- The round-1 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_CUSTDY_ROUND_1_20261007.md` @822468e309
  (`1.0.0_SA_CTO~DELL2`, msg 229), section 3: E1-E4. receiving-check: UNCHECKED (no checker exists for a round analysis; read by this seat).
- PRD v0.3 @1aa8fb7a0c, ADMITTED (`prd-signoff.py status`); `receiving-check.py` on the PRD -> ACCEPT.
- Round 1's code at HEAD: `data/assets/scripts/gold/irpt_custody/` (drains 737839f762, 06a44e56bd, 9dd85cec00, 36c37ef88d).

**Rule 24.** Domain: the analysis's four items E1-E4, nothing else (the served render a1-a4 is IRPT_BCKEND's `~P2`; hop 6 is Andrew's;
pre-2024 SI waits on the calendar fix). Each item is one cell; E2 consumes E1's output, so they are one chain. **E3 is HELD, not cut**
(below). Covered this round: E1, E2, E4.

## Measured constraints (read at the base, dell2 CLOUD, 2026-10-07 ~09:0xZ-09:1xZ)

1. **The `'None'` key (E1).** `infra/aws/lambda/investor-reporting/_ids/ids.py:387` -- `mapped = idx.get(str(raw).strip())`, then
   `base("account", mapped)` -- the seam index maps a raw account to the literal string `'None'` for 482 of 7022 distinct granted
   accounts (row S3; the CVO's compile @648dd308a6 names the literal). The index is loaded by `load_seam_index` (same file); where its
   values are made is UNMEASURED and is E1's first act. **ISSUER RULING on "fixed there":** if the source is under this project's
   paths, E1 fixes it there; if it is another project's file (`_ids/` and its producers are IRPT_BCKEND's; PRD section 4), E1 names
   it at file:line and files a row, and the issuer routes the fix to that owner -- this project never writes another's paths.
   Either way CU-a-1 counts a refused account as uncovered with its reason and never raises (the analysis's criterion 2).
2. **The ownership map (E1, E2)** is readable from dell2: `s3://opal-data-bd/platinum/49financial/ownership_map.json`,
   LastModified 2026-10-07T05:27:37Z, 472562 bytes, 190 advisors, 24082 grant entries (read ~08:5xZ). It refreshes daily
   (~05:27Z), so counts are quoted with their read time, never as constants.
3. **The firm bucket is FENCED from dell2** (row S4): `opal-data-49financial` -- the returns gold hop 3 reads, the `client_report`
   gold and `report_template` state this project writes -- is an explicit deny for `cloudops-dell2-agent-user`. E4 builds and is
   checked on fixtures; its real read goes to the laptop as the committed script
   `deliverables/2.0.0_SA_COO~K2/read_returns_gold_partition.py` @b97c663aa9 (standing rule, msg 213). No cell widens the fence.
4. **HOLD A** (laptop CTO 08:5xZ, msgs 179/192): nothing dated before 2024-01-01 through `lib/trading_calendar.py` on dell2 until fix
   B. E4 reports SI as held for any account whose inception is before 2024, and never calls the calendar for such a date.
5. **E3 HELD** (row S5): the `ClientReportDocument` lives in `portal/src/pages/InvestorReporting/render/` (CRO research
   @14fe71e545: a template is a React document chosen by `reportKind`); portal HEAD 8ddfe409 = origin/DEV; `portal/node_modules` is
   ABSENT on dell2 and installing it is npm egress. Its build and both its checks need that toolchain. Cut when the bring-up kit carries
   it, or on the CTO's placement of the cell on the laptop.
6. **Dependency graph:** `comp-blast` is unavailable on dell2 (row NFRA_CTLPLN-S7). Every cell's write set is round 1's own files in
   `data/assets/scripts/gold/irpt_custody/`; no producer, Lambda or route of another project is modified.

## The cells

| cell | what | serves | status | placement | risk | chain / slot |
|---|---|---|---|---|---|---|
| `CU-b-1` (E1) | the advisor pick runs on live data: name where the `'None'` value is made (file:line) and fix it there or route it (constraint 1); every account the projection refuses is counted as uncovered with its reason; the denominator printed beside the refused count | FWD-1 | NOT-EVALUATED | dell2 | LOCAL | A, `0.9.0_WK_IRPT_CUSTDY~5` |
| `CU-b-2` (E2) | the chosen advisor, by census: the real pick on the live map writes its census (advisors scanned, households each, accounts covered) and the pick to a deliverable file | FWD-1 | NOT-EVALUATED | dell2 | LOCAL | A (after CU-b-1), `~5` |
| `CU-b-3` (E4) | hop 3 on 2024 onward: QTD, YTD and 1Y computed for 2026-09-30; SI reported as held (`HELD_CALENDAR_FIX`) for an account whose inception is before 2024, never computed; each figure names its source rows | FWD-1 | NOT-EVALUATED | dell2 | LOCAL | B, `0.9.0_WK_IRPT_CUSTDY~6` |
| E3 | the 49 Financial `ClientReportDocument` (a5) | FWD-1, FWD-3 | HELD (constraint 5) | -- | -- | -- |

## Write sets (disjoint)

- **CU-b-1 (slot ~5):** `data/assets/scripts/gold/irpt_custody/advisor_client_list.py`, `.../tests/test_advisor_client_list.py`,
  `.../tests/test_advisor_projection_refused.py` (new), `.../none_source.py` (new).
- **CU-b-2 (slot ~5, after CU-b-1):** `data/assets/scripts/gold/irpt_custody/advisor_census.py` (new; imports the pick) and its census file
  under its deliverables folder.
- **CU-b-3:** `data/assets/scripts/gold/irpt_custody/client_report_figures.py`, `data/assets/scripts/gold/irpt_custody/tests/test_client_report_figures.py`.
- Each: its own deliverables folder and the investigation file.

**Ordering and fan-out:** `fanout: 2 of 2 chains cut (3 in the analysis; E3 held), cap 8` -- A (CU-b-1 then CU-b-2, one worker queue:
CU-b-2 reads CU-b-1's code) and B (CU-b-3) are independent.

## The issuer's acts after the drain

1. Record CU-b-2's census and pick in this file's constraint 2 (the analysis's E2 criterion 3).
2. Route any E1 source fix that sits in another project's paths to its owner, with the row.
3. Receive the laptop's file for the fenced returns-gold read (constraint 3) and run CU-b-3 on it locally if it carries the rows.
4. The served render (hop 5) and the advisor's read (hop 6) are not this round's: IRPT_BCKEND a1-a4, then Andrew.

## Recorded at the drain (2026-10-07 ~09:3xZ, the issuer's act 1)

- **The pick (E2):** `ADVISOR-PICK scanned=190 eligible=16 pick=matthew_gooch households=10 classes=4 projection_refused=482 of=7022`, on
  `s3://opal-data-bd/platinum/49financial/ownership_map.json` LastModified 2026-10-07T05:27:37Z, as-of 2026-09-30. Census, one row per
  advisor: `deliverables/0.9.0_WK_IRPT_CUSTDY~5/ADVISOR_CENSUS_20260930.md` (drain 1c925383a4). The same pick came out of CU-b-1's run.
- **The `'None'` source (E1):** `infra/aws/lambda/investor-reporting/_ids/data/custodian_key_seam.json:48` (IRPT_BCKEND's bundled
  artifact; 826 of its 6202 values are the string `'None'`, from null `schwab_account_id` in `dim_account_xref` 2026-09-16), passed by
  the guard at `ids.py:387-388` (`mapped is not None`). Not this project's path: routed (act 2), row W5-S1.
- **Drains:** 19ff3664fc (chain B, CU-b-3), 1c925383a4 (chain A, CU-b-1 + CU-b-2). Drain checks: py_compile 6/6, ruff clean, pytest 53
  passed, four self-tests all True.
