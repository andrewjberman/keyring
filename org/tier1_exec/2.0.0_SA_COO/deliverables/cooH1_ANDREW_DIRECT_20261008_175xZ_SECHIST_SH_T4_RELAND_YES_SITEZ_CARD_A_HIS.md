# Andrew-direct 2026-10-08 ~17:5xZ, dell1 terminal of 2.0.0_SA_COO~H1 -- MDPF_SECHIST

**Recorded by:** `2.0.0_SA_COO~H1`, same turn. **Channel:** Andrew at this seat's terminal, answering the seat's three blocked items
(1. SH-t3 acceptance read waits on the 2026-10-09 scheduled pull; 2. re-land 5c4f55a2ea on his yes; 3. SH-t-5 waits on site Z card A).

## VERBATIM

> 1.) Does this have to block next steps? 2.) Yes. 3.) I will handle that with sitez.

## What each answer moves

1. A question, not an order. Answer given at the terminal: SH-t3 itself must read a `run_class: scheduled` manifest (ruling cb6fb2a52c;
   CLAUDE.md "ad-hoc artifacts are never production evidence"), and an ad-hoc pull spends the Bloomberg ledger, so SH-t3 still waits for the
   2026-10-09 07:00 ET pull. It does NOT block item 2: CTO msg 932 names the alternative "If Andrew prefers to keep it on the trunk now,
   site Z must hold its pull of that file until after 07:00 ET."
2. **Yes** to re-landing 5c4f55a2ea (the SH-t-4 run-record edit to `integrations/bloomberg/pipeline/etf_daily_pull.py` and its test).
   This lifts the 2026-10-06 no-modify order for that edit only. Taken on the CTO's msg-932 alternative: re-land on dell1 CLOUD now; site Z
   does not take that file until after the 2026-10-09 07:00 ET pull has run (the CTO half's condition 3).
3. Site Z card A (FWD-2, SH-t-5): Andrew handles it with site Z. This seat cuts SH-t-5 when the release reaches it; it sends nothing to
   site Z on card A.
