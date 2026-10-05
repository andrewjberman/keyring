# Never-widen half, MDPF_SECCLASS FWD-9 BRANCH 2 -- the resolved US bare-ticker rows (CTO batch 261 item 3, batch 263 condition 2)

**Author:** `2.0.0_SA_COO~M`, 2026-10-05 ~21:0xZ. **For:** `1.0.0_SA_CTO`, second half. Branch 1 (626 `BBG:` rows) is done; this file
carries Branch 2 only. **Status: COO half SIGNED; CTO half UNSIGNED. Nothing is written.**

## The act

`python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R7_CHECKS/r7_fwd9_write.py --write --namespace TICKER --resolved-only
--half org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_FWD9_BRANCH2_20261005.md`, under ledger
`secclass-fwd9-branch2-m-<date>` opened first. `--resolved-only` is new in this half (the writer had no filter for batch 263
condition 2); the dry run, 2026-10-05 ~21:0xZ, prints `FWD9-WRITE plan=8 (TICKER=8)`, (a) MET, (b) MET, (c) NOT MET (no half signed).

**The 8 rows (GICS-resolved sub-class, `input: gics`):** AUGO Materials; BAP Financials; ETOR Financials; GRFS Health Care; HDB Financials;
HTHT Consumer Discretionary; RYAAY Industrials; TCOM Consumer Discretionary. Each: `asset_class equity`, `classified_by scheduled`,
`updated_by rivalfunds-backfill`, put on absence.

**NOT written, named (batch 263 condition 2, a US key with no resolved sub-class):** the other 23 of the 31 -- AAGIY ADYEY ATI BG BKD BZ
CACI GENI GXYYY JAN KB NBIS RARE SPHR STLA STVN SUNB THC TISI VG XTSLA YMM ZIM.

## The held census (served nodes at the three firms, latest revision 2026-10-02, every part read: cottonwood 27 of 27, inflection 51 of 51, 49financial 188 of 188)

The 8 written keys:
- **HDB**: held at inflection (1 account). Today `equity | International | TABLE` (the fallback's own table). After: `Financials`, basis `TABLE`.
- **RYAAY**: held at inflection (1 account). Today `equity | International | TABLE`. After: `Industrials`, basis `TABLE`.
- AUGO, BAP, ETOR, GRFS, HTHT, TCOM: held at none of the three firms.
So the act moves two nodes' sub-class, both at inflection, within `equity`. Their dollar amounts were not read.

The 23 unwritten US keys that firms hold keep reading their fallback (no change): ATI (cottonwood 2 accounts, 49financial 10), BG (2, 1), JAN (2, 4),
VG (cottonwood 1), NBIS (49financial 1), SUNB (49financial 7), AAGIY and BKD (inflection 1 each).

## W14-S5's nine (batch 261 item 3): none is written, all stay OUT, named

BRK/B, CRWV, EPAM, FPS, MDLN, ORI, SLDE, HAL, VLO carry no GICS in the row set, so none has a resolved sub-class; batch 263 condition 2 bars a
US row without one. Held today (served nodes, symbol as served):
- VLO: Energy / TABLE; cottonwood 11 nodes, inflection 2, 49financial 11. HAL: Energy / TABLE; cottonwood 5, inflection 1, 49financial 10.
- BRK.B: US Large Cap / TABLE; cottonwood 9 nodes ($1,184,198.25). CRWV: US Mid Cap / TABLE; cottonwood 2, 49financial 10.
- FPS and MDLN: no sub-class / TICKER_SHAPE; 49financial 6 and 7. EPAM, ORI and SLDE: held at none.
A sub-class-less row for VLO, HAL, BRK.B or CRWV would replace a real sub-class with none, FWD-7's own failure. The positive held-table
signal (batch 261) was not sought, because it would add rows only for keys that cannot be written without a sub-class.

## Blast radius

`etf-classifications`, 8 new keys, each put on absence; no existing row changes. The table counts 3,493 (full scan, 2026-10-05) and
would count 3,501. Served effect: the 2 inflection nodes above, at the next inflection holdings build; no other firm holds any of the 8.

## Writers counted

N = 7 (the writers read in the FWD-10 half; this writer is the FWD-9 one, run for Branch 2). The FWD-10 producer (daily,
10:00 ET MON-FRI) also puts on absence and may meet one of these keys: both branches of the put are safe.
- **Branch A, a key is absent:** the put lands, 8 of 8 `written`.
- **Branch B, a key appeared since the plan:** `ConditionalCheckFailedException`, the row is left as it was, reported `refused`.

## Rollback per key

`delete-item` of `ticker = <key>`, on Andrew's word only.

## Acceptance

1. Each of the 8 keys reads back `classified_by scheduled`, `updated_by rivalfunds-backfill`, `asset_class equity` and the sub-class above;
   the table counts 3,501.
2. A second dry run with `--resolved-only` plans 8 (the writer plans from the set file, as for Branch 1); the read-back's 8 present keys stand in.
3. The next inflection holdings build reads HDB `Financials` and RYAAY `Industrials`, basis `TABLE`.

## COO half -- SIGNED for BRANCH 2 (TICKER, resolved-only)

`2.0.0_SA_COO~M`, 2026-10-05 ~21:0xZ, after reading the set file, the held census above and the dry run.
- **Blast radius:** 8 new `etf-classifications` keys, each put on absence; two inflection nodes (HDB, RYAAY) change sub-class within `equity`.
- **Writers counted:** N = 7; both put branches are above. **Rollback per key:** a `delete-item`, on Andrew's word only.
- **Not signed here:** the 23 unresolved keys and W14-S5's nine; they are not written.

## CTO half -- UNSIGNED

Awaiting `1.0.0_SA_CTO`.
