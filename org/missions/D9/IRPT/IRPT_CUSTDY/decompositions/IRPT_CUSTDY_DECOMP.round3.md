# IRPT_CUSTDY decomposition -- ROUND 3, gated items (issuer 2.0.0_SA_COO~K2; drafted 2026-10-07 ~09:5xZ, dell2)

**Status: DRAFT -> ISSUED per gate.** The round-2 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_CUSTDY_ROUND_2_20261007.md`
@10e64fe9df (msg 280) pre-cuts three items, each issued the tick its gate opens, with no new analysis. This file is the cut of whichever
items have opened; each later opening appends its cell here in its own issuance commit.

| gate | item | state at 09:5xZ |
|---|---|---|
| IRPT_BCKEND E-P8 drained (`~P2`) | E1: the 482 re-read | CLOSED: E-P8 is an item of IRPT_BCKEND's round-61 analysis @aae1ed7781; no order cut |
| S4 FILE lands | E2: hop 3 on the real returns | **OPEN**: `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_CUSTDY/IRPT_CUSTDY_returns_gold_20260930.json` @ef5ea44568 (msg 286) |
| the portal kit lands on dell2 | E3: the 49 Financial template | CLOSED: `portal/node_modules` absent |

## E2 -- measured constraints

1. **The FILE carries presence, not figures** (row S6): the 2026-09-30 `account_return_daily` partition exists (data.parquet, 6854 rows,
   19 columns, 6854 distinct `account_id`; error null). The figures must be computed where the firm bucket is readable. **Issuer
   ruling:** E2 is cut as a read-only wrapper that the laptop runs under the standing fenced-read rule (msg 213), writing the chosen
   advisor's client-report documents to a FILE; that FILE is what grades E2's criteria. On dell2 the wrapper records the fence in its own
   output file (the same shape as `read_returns_gold_partition.py`).
2. **The ownership map is read through `opal_naming.legacy_address('blackdiamond-platinum-49financial-ownership-map')`** (registry row
   @58532d19fd, in HEAD) -> `s3://opal-data-bd/platinum/49financial/ownership_map.json`; no key is typed. This also discharges the
   round-3 carry noted in the round-2 packet.
3. **The advisor** is round 2's recorded pick (`DECOMP.round2.md`, "Recorded at the drain"): slug `matthew_gooch`, 10 households,
   as-of 2026-09-30. An account the projection refuses is reported as uncovered, never computed.
4. **HOLD A** binds the wrapper exactly as `client_report_figures.py` already enforces it (SI `HELD_CALENDAR_FIX` before 2024; the calendar
   never called for a pre-2024 date). No `--apply`: nothing is written to S3 by the wrapper or by the laptop run.

## The cells

| cell | what | serves | status | placement | risk | chain / slot |
|---|---|---|---|---|---|---|
| `CU-c-1` (E2) | the hop-3 real-run wrapper: for one advisor and as-of, resolve the advisor's accounts from the ownership map (legacy_address), build the client-report documents through `client_report_figures.py` (no `--apply`), and write them, with every account masked to the last 4, to one JSON FILE plus a summary line; read-only; the fence is recorded, never worked around | FWD-1 | NOT-EVALUATED | dell2 (built), laptop (run) | LOCAL | A, `0.9.0_WK_IRPT_CUSTDY~7` |

## Write sets

- **CU-c-1:** `data/assets/scripts/gold/irpt_custody/hop3_real_run.py` (new), `data/assets/scripts/gold/irpt_custody/tests/test_hop3_real_run.py` (new).

**Ordering and fan-out:** `fanout: 1 of 1 open chain (E1, E3 gated closed), cap 8`.

## The issuer's acts after the drain

1. Commit nothing new to the laptop path: send `0.0.0_AB_MSTR~DELL2`, for bus relay to laptop `3.0.0_SA_CVO` (copy `1.0.0_SA_CTO~DELL2`),
   the drain commit, the exact command and the recipient lane (msg-213 rule).
2. When the FILE returns: grade E2's three criteria from it (QTD/YTD/1Y at 2026-09-30 present per account and household; SI held where
   inception is before 2024; every figure's `source` names its rows) and file the result as a row closing S4/S6.
