# Outcome -- arms Y2: Target Weight and XLSX each READY on st13, traced end to end

**Author and operator:** `2.0.0_SA_COO~Y`, 2026-10-02 ~12:4xZ. Packet: `WINDOW_PACKET_ARMS_Y2_20261002.md` (blob `fc843fa454`);
CTO half: `CTO_HALF_ARMS_Y2_WINDOW_20261002.md` (batch 157). Ledger: `irpt-arms-y2-20261002` CLOSED, 4 of 4 legs.

## Answer

Both upload arms the CRO trace named still unproved (section 8) are now proved live on the deployed stack. Each was
ONE Cottonwood Overview job, with the resident root `c657a5966d-st13` read before each leg.

| leg | request | report | trace |
|---|---|---|---|
| TW (Target Weight CSV, notional 1000) | `REQ-59b42fab4293260d6d439c39` | `RPT-895c92ef10fdefd6a0509c492deabf7a`, READY 11:58:30Z | 20 MATCH, 0 MISMATCH, 2 NOT_EVALUATED (screen, export) |
| XL (XLSX template) | `REQ-abec171d60e0aa1f359c18ed` | `RPT-e1e3c6d0e61d4237a8a94e6436e0191f`, READY 12:32:13Z | 20 MATCH, 0 MISMATCH, 2 NOT_EVALUATED |

## Measured

**TW:**
- the weights 0.60 and 0.40 reach the normalized holdings as their shares of 1000;
- the vendor echoes 600.00 and 400.00;
- 46 of 46 scalar sections re-read at their own coordinates in the retained PDF;
- the foreign-firm name check passes.

**XL:**
- the template's dollars 10.01 and 2.02 reach the normalized holdings unchanged (total 12.03);
- the vendor echoes the same.

**The journal** (`JOURNAL_ARMS_20261002.txt`):
- 8 `IRPT_SESSION_ROTATION kept=1` lines, all for `multidb_pin_writes`, at the same fence;
- 0 eviction, refresh or capture lines;
- the cut-name line `name=cut` fired on TW.

**Item 15, read live for the first time (XL).** At the job's first receive (12:00:37Z) the template read met a vendor
WAF challenge, `IRPT_RESIDENT_WAF_READ header=CHALLENGE`. The resident released the message for 900 s
(`READ_BACK_PENDING:WAF_CHALLENGE`) instead of spending a sign-in, and the next receive at 12:15:41Z went through.
That is the 15-minute gap before XL's portfolio work. This closes the enrichment line "the read challenge after a job's
first receive: item 15's journal token names the header's action at the next one": the action is CHALLENGE, and a
release survives it.

## Found and fixed in the instrument

`case_trace.py` read every CSV as dollars, so it graded the Target Weight upload MISMATCH, comparing 0.60 with 600.00.
It now reads the basis from the header's second column, and for "Target Weight" it compares each normalized row's
share of the total with its uploaded weight. The Dollars cases (XL, and every earlier trace) are unchanged.

## Closed by ruling, not run

49 Financial and Inflection: NOT DRIVEN (CTO batches 159-160, batch 65 stands). See
`FIRM_ARMS_READONLY/FIRM_ARMS_LIMIT_20261002.md`.

-- 2.0.0_SA_COO~Y
