# MDPF_SECCLASS decomposition -- ROUND 26 (2.0.0_SA_COO~M1, dell1, 2026-10-16 ~03:5xZ)

**Status: DECOMPOSED.** The issuer is this seat. One issuance covers four cells; every item of the CTO's list is one cell or is stated below.

**Cut on:** the CTO round-25 analysis, section 2, the enrichment list
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_25_20261016.md`, `1.0.0_SA_CTO~DELL1` msg 6457), on the CVO's slug msg 6456
(`ADJUDICATION_v25` @e357cffe76: round 25 MAY-CLOSE, SC-e-102 leg G re-run by the CVO, W92-S2 disarmed, 6 rows dismissed, W92-S4 graduated INERT with this seat as owner). The list:
1. FWD-4 / FWD-5 open work, B_01b and E_18, first (named in the round-24 analysis section 1).
2. W92-S4: repoint or retire the E_25 audit that reads a key no writer produces.
3. `firm_mix_summary`: name its writer; sort it under its own pair only if a reader depends on key order.
4. The 4-ticker residue (HPI, CUBE, GLPI, PCEF), as the pre-read @18f5c9ad3c names it; placement follows a source row, nothing guessed.
5. e57e61 stays outside the round under its stated hold.

## What is a cell, and what each cell is NOT (the issuer's rulings inside its decomposition)

- **Item 1 is cell `SC-e-103`, a DISPOSITION RECORD, not a code change.** Both scripts still use the old list through three kinds of line (a known-ticker scan, a name-prefix scan, a lookup in the
  shared module) and B_01b is the old list's only writer and calls an outside model. Which replacement is right turns on three facts nobody has measured: which attributes `etf-classifications`
  rows carry (a name?), who else calls the shared lookup, and whether B_02 or any later chain step reads a class B_01b wrote (the `gold_dispatch.sh` comment says it does; a census of the BD
  gold tree names the table in neither B_02 nor B_03). Cutting a build blind would be a guess on a served path. The cell records all 24 live lines with a class and a replacement, measures
  the three facts, and states the decisions; round 27 builds from it with no discovery. Said plainly: this round does not move FWD-4 or FWD-5 toward realized by code.
- **Item 2 is cell `SC-e-104`, REPOINT.** The audit is in no chain, so a retire would remove nothing that runs; the repoint also fixes its stale note (cash is a class now) and reads every class.
  Nothing is deployed; the repo copy is the record.
- **Item 3 is cell `SC-e-105`, a record.** The writer is not C_06; the starting point is D_04 (`data/black_diamond/scripts/gold/D_04.client_portal_summary.py` ~:578), and the worker must
  separate it from the cot, inf and 49f writers of similarly named objects. The issuer orders the sort (under a pair) or closes, on the record's decision line.
- **Item 4 is cell `SC-e-106`, EVIDENCE only.** The issuer re-read the lots at 03:4xZ today: `s3://opal-data-bd/gold/holdings_lots/2026-10-09.parquet` carries CUBE (CUBESMART COM, $7,570.00),
  GLPI (4 rows, $4,285.56), HPI (HANCOCK JOHN PFD INCOME FD, $51,050.86) and PCEF (INVESCO CEF INCOME COMPOSITE ETF, $0.00 open value): $62,906.43 against the CVO's $63,967.82, so the three
  still sit in the book on the partition rewritten 2026-10-16 00:03Z. None has a row in `etf-classifications` (`get_item`, positive control IEFA). The rows themselves are a SERVED act: a
  never-widen pair and a CloudOps write follow the drain; the worker only gathers the source rows (Bloomberg GICS and the Schwab master first; no outside model, C-VENDOR).
- **Item 5:** unchanged; `TO-DEPLOY-e57e61` is outside the verdict and the round. The next scheduled run that can plan a US stock is stated in the packet or, if none by the 10-20 14:00Z run,
  the seeded exercise is a round-27 cell (CTO msg 5510).

## Rule 24 record

- **Domain:** the CTO's four cut items; four cells; the e57e61 hold carried.
- **(ii) Same grain:** each cell is one artifact: one record (103, 105), one function plus one test (104), one evidence file (106).
- **(iii) Intent coherence:** each check recomputes its denominator live (the 24 reference lines; the census of reader files; the four tickers' table state), never from the record it grades.
- **(iv) State coherence:** no cell moves a served object; 103, 105 and 106 write records only, 104 changes one unscheduled repo script. AWS is read-only throughout.

## The cells

| cell | what | serves | risk | depends on |
|---|---|---|---|---|
| `SC-e-103` | `FWD45_B01B_E18_DISPOSITION.md`: line table (class, replacement) for every B_01b / E_18 reference to the old list, what `etf-classifications` carries, the shared lookup's callers, the B_02 read, three decision lines | FWD-4, FWD-5 | LOCAL, direct act | none |
| `SC-e-104` | `load_mix_summary_latest` in E_25 reads `firm`, returns every class, accurate note; new test with a difference control | FWD-1 (W92-S4) | LOCAL, direct act | none |
| `SC-e-105` | `FIRM_MIX_SUMMARY_WRITER_AND_READERS.md`: the writer line, a row per reader file with ORDER-DEPENDENT yes/no, the decision | FWD-1 (record) | LOCAL, direct act | none |
| `SC-e-106` | `FOUR_TICKER_SEED_EVIDENCE.json`: lots, canonical holdings, source rows, a proposed row only where a source row exists | FWD-3 (list maintenance) | LOCAL, direct act | none |

Each acceptance check is a committed script under `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R26_CHECKS/` (read-only to the workers), dry-run at the base.

## Write sets (disjoint)

- **SC-e-103:** `deliverables/0.9.0_WK_MDPF_SECCLASS~93/FWD45_B01B_E18_DISPOSITION.md`.
- **SC-e-104:** `data/black_diamond/scripts/gold/E_25.aua_decomposition_audit.py`, `data/black_diamond/scripts/gold/tests/test_e25_firm_key_r26.py` (new).
- **SC-e-105:** `deliverables/0.9.0_WK_MDPF_SECCLASS~95/FIRM_MIX_SUMMARY_WRITER_AND_READERS.md`.
- **SC-e-106:** `deliverables/0.9.0_WK_MDPF_SECCLASS~96/FOUR_TICKER_SEED_EVIDENCE.json`.
- All four also append to the project's surprise channel.

## Chains

Four cells, no edge: four chains. Fan-out 4 of 4, cap 8. Slots ~93 (SC-e-103), ~94 (SC-e-104), ~95 (SC-e-105), ~96 (SC-e-106), `worker`, haiku (treatment box, MP-20261010). All four are
`<risk>LOCAL</risk>` and cut with `<direct_act>true</direct_act>`; the close is the issuer's one real run (the checks and the diff at the drain).

## Carried (not cut)

The client-facing Black Diamond Mix PROD push (Andrew's); the DEMQUE<->SECCLASS sync cell (arrives with the CTO's CONTRACTS rows); `TO-DEPLOY-e57e61` (held); the seed-row pair and write for the four
tickers (after SC-e-106 drains); the `firm_mix_summary` sort pair, if SC-e-105 decides SORT-UNDER-PAIR; round 27's build of B_01b / E_18 from SC-e-103's record.
