# ETFS_RIVALS task order -- `RIV-q-1` -- ROUND 4 (ENRICHMENT): GQGU THROUGH ITS MEASURED ISSUER ROUTE -- COLLECTOR AND SILVER (Z-S5/Z-S6)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-q-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~1</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (2026-10-01 ~12:xxZ, --drift) -- no armed gate names rivalfunds/, issuer-site/etfs/, bloomberg/etfs/ or this cell's files; the notifier moratorium binds.
comp-iam: RUN at L5 -- no IAM change in this cell.
comp-adversary: RUN at L5 on the round-4 decomposition; declared on RIV-v-2, not this cell.
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: daily holdings of rival active ETFs in two peer groups (IDVZ, PFOE), each fund's trade schedule, and a served page grouped by Opal fund. Rounds 1-3 built the live pipeline (package `data/etfs/scripts/rivalfunds/`, five AWS stage Lambdas, a terminal-machine Bloomberg leg); the 2026-10-01 page serves 12 of 13 funds. **Round 4** fixes the daily trade pairing, unifies 'newest', grades identity per source and adds GQGU. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-q-1` -- GQGU's issuer collector and silver (rows Z-S5/Z-S6; ruling 4)

- `adapters/gqgu.py`: the SEI filepoint URL, and a fetch identical in shape to BASG's.
- `collector_issuer.land_bronze(..., fund="BASG")`: bronze stem `<source>-<requested_date>-<ts>-<sha12>` per fund. The daily mode
  fetches every issuer-route fund of the map.
- `silver_issuer`: per fund. Objects are `<source>-<capture_id>.parquet`, rows typed from that fund's file. BASG is unchanged.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base 48ec92238a)

- `collector_issuer.py` is BASG-shaped (`from .adapters import basg`; stem `basg.SOURCE-...`; `_classify` reads BASG rows).
  `adapters/basg.py`: `FUND_TICKER`, `SOURCE`, `URL_TEMPLATE` (SEI filepoint), `fetch`, `basg_internal_dates`.
- GQGU's route (row Z-S6): `https://gqg.filepoint.live/assets/data/SEI_GQG_Tradedate_Holdings_<MMDDYYYY>.txt`, the same
  pipe-delimited column set (`date|fund_id|...|fund_ticker|...|percent_of_net_assets`), fund_ticker `GQGU`; 305 archived days in
  `.runtime/amgt-reconn-daily-census-20260929/gqgu/` (`<D>.txt` + `<D>.json` {requested_date, url, at, http_status, rows}),
  39 GQGU rows on 2026-09-28. No vendor word is needed (CTO ruling 4); no Bloomberg request for GQGU.
- `silver_issuer.py` names objects `basg-<capture_id>.parquet` and keeps every row of the file; make it per fund
  (`<source>-<capture_id>`), BASG unchanged. G1's per-fund read is RIV-v-2's (do not edit gold_canonical_shape.py).

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (the Positioning pull is under an Andrew-direct no-modify order), the package's other modules, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round{1,2,3,4}/checks/`, the device-local captures under `C:\Users\Opal Bloomberg\Desktop\ajb_workspace\.runtime\`, and live S3 READ-ONLY where a check mirrors it.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~1/`; the reopen is slot ~1's). NEVER: any S3 write, any deploy, any Bloomberg or OpenAI call, the vehicle, any file another round-4 cell owns. Tests go beside the code as `tests/test_q1_*.py`, run with `python -m pytest <file> -q` from `data/etfs/scripts/`; the issuer runs the whole suite at the drain.

<paths>
data/etfs/scripts/rivalfunds/collector_issuer.py
data/etfs/scripts/rivalfunds/adapters/
data/etfs/scripts/rivalfunds/silver_issuer.py
data/etfs/scripts/rivalfunds/tests/test_q1_*.py
data/etfs/scripts/rivalfunds/tests/test_c1_core_and_collector.py
data/etfs/scripts/rivalfunds/tests/test_s1_silver_issuer.py
data/etfs/scripts/rivalfunds/gold_holdings_coverage.py
data/etfs/scripts/rivalfunds/tests/test_hp1_home_producer.py
data/etfs/scripts/rivalfunds/tests/test_g2_*.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

**AMENDMENT 1 -- REOPEN (issuer ruling on rows ETFS_RIVALS-Z-W4-S12 and Z-W4-S13, S13 ARMED, 2026-10-01), reissued to slot ~1.** `gold_holdings_coverage.py` `_issuer_obs` stamps EVERY issuer-site sidecar `fund: BASG` (and returns nothing unless BASG is in the funds), `_Evidence.issuer_rows` reads the silver object under BASG's source name, and `_latest` keeps the latest capture per (fund, source, day). The vehicle fetches BASG then GQGU each morning, so from the next 07:00 ET fetch BASG's coverage row reads GQGU's capture (0 BASG rows), and GQGU never gets a coverage row (its calendar reads unavailable). Measured by the issuer at CLOUD: `q-1.AC2.py` reads BASG's 2026-09-28 row on a gqgu-* capture with 0 rows, and no GQGU row. Fix: an issuer observation's fund is the sidecar's own `fund` (a legacy sidecar without one is BASG's), every issuer-route fund of the map is observed (the adapters registry), and its rows are read from that fund's own silver object (the sidecar's `source`). Nothing about BASG's served coverage may move except that it can no longer be displaced. NEVER touch S3. One criterion is added: AC2.

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- two REAL archived GQGU days land under gqgu- keys; issuer silver holds GQGU's 39 rows for 2026-09-28; BASG's object for that date is kept (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round4/checks/q-1.AC1.py`)
- **AC2** (amendment 1) -- with BASG's and a 5-second-later GQGU capture of 2026-09-28 replayed through silver, G1 and G2, BASG's coverage row reads a basg-* capture with its 35 rows, GQGU has its own gqgu-* row with its 39 rows, and no row crosses funds (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round4/checks/q-1.AC2.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-q-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round4/checks/q-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC2" cell_refs="RIV-q-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round4/checks/q-1.AC2.py</invocation><expect>AC2 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~1/ETFS_RIVALS.TO-RIV-q-1.gqgu-issuer-route.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-q-1.gqgu-issuer-route`. Report once: each criterion's verdict line with the output above it; files written; any test assertion changed and why; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** Round-3 analysis @d4a1e22801 (msg 27810), decomposition round 4 v1.0. Checks dry-run
at base 48ec92238a: q-1.AC1 FAIL -- each FAIL as expected.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<completion_note>2026-10-01 drain by 2.0.0_SA_COO~RV: worker 0.9.0_WK_ETFS_RIVALS~2 @8f0bec50e9 (build b4f1ee0e88); proof instance VALID; q-1.AC1 PASS (GQGU bronze gqgu-2026-09-28-*, silver 39 == 39 rows, BASG kept 35 == 35); suite 258 passed 2 skipped; row W2-S11 ARMED (a gqgu silver object beside basg would displace BASG in G1 until RIV-v-2's per-fund read) -- disarmed by construction: RIV-d-5 deploys only after RIV-v-2 merges, named in d-5's pair.</completion_note>
<round>4</round>
<slot>~2</slot>
<fabric>site-z</fabric>
