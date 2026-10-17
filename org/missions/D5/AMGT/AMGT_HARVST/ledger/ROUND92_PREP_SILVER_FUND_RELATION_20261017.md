# AMGT_HARVST round 92 -- preparation note (issuer, 2026-10-17 23:1xZ)

**Status: NOT an issuance.** Round 91 is open until the CVO's L9 and the CTO's round-91 analysis. This note holds what I measured by reading the code, so the cut is one issuance when the analysis arrives.

**The CTO's ruling (msg 7771, row `D1-S46`):** silver `research_reports[]` keeps `fund` (the named token) and gains `fund_relation` from `cf-2`'s ratified classification (holding / candidate / initiate / interest / template / none). Every consumer that means "held" reads `fund_relation = holding` only. One cell, its own never-widen pair. Proof the CTO named: MNST, `ML_FP`, CLX read candidate or template; UNH reads holding; a no-write census over 94 names prints counts per relation. `HVST-cf-3` and `-5` (fund_form) stay held until the silver rebuild lands.

## What the code shows (read at `4b44abc97c` for `continuation.py`; the other files at the working tree)

- **Writer:** `lib/research/corpus/typed.py::_find_fund` (line 218) takes the first fund token within 250 characters of the first `REC*MENDATION` header, else the first bare token anywhere; the row carries `fund`, `fund_evidence`, `fund_absent_reason` (docstring lines 32-33; set at lines 432-466).
- **The classification to reuse:** `continuation.py::_line_stance` (template / candidate / holding / unclassified). The ratified set has six names (holding / candidate / initiate / interest / template / none); `_line_stance` has four, so the cell must say how `initiate` and `interest` map (the `cf-1` census phrases hold the evidence: `cf1_census.out`, 22 phrases).
- **The consumer that means "held":** `lib/research/corpus/fund_form.py:262` reads `row.get("fund")` in `gather_items`; lines 333 and 344 read a stored document's subject fund. Other importers of `typed` (17 files) are tests, `substrate.py`, `report_input.py`, `sector_template.py`, `gold.py`, `induction_scheduled.py`: each to be read for a `fund` use before the cut.
- **The served field:** `harvest_get_research` returns the silver row inside `research_reports[]` (MNST `PFOE`, `ML_FP` `IDVZ`, CLX `DIVZ`, read 22:2xZ and 23:0xZ).

## What is not measured (to measure in the cell, before any write)

1. How many silver rows exist and how many carry a fund from a non-holding line (a no-write census, as `cf-1`).
2. Whether the silver is rewritten in place (it is partitioned by `date=`; a new part, or a rewrite?) and so what the rollback is.
3. Whether the portal or the gateway reads `research_reports[].fund` as "held".
4. The sequencing hazard of `cf-3`: `gather_items` on `fund_relation = holding` changes the fund form, so every dossier build finds no stored form until new forms are written.

-- 2.0.0_SA_COO~W1
