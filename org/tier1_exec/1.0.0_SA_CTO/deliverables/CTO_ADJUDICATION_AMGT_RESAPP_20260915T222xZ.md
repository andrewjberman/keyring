# CTO ADJUDICATION -- AMGT_RESAPP, /self-drive tick 6 (2026-09-15 ~22:2xZ)

**Adjudicator:** `1.0.0_SA_CTO~W`, on Andrew-direct ~19:3xZ (@`2ac5611057`, "you adjudicate"). **Scope:** AMGT_RESAPP.
**New input:** `4.0.0_SA_CRO~Z`'s Seeking Alpha consensus crawl @`910dc1bb7e` (msg 23258, 22:02:40Z), run on Andrew's ~19:0xZ word and his
~19:30Z word to use the canonical harvest scrapers.

```
OPEN CALLS -- AMGT_RESAPP -- 1.0.0_SA_CTO~W, /self-drive tick 6 (1 new call, ADJUDICABLE; the 2 RESERVED cards of tick 1 stand at Andrew)

+-- CALL 16 ---------------------------------------------------------+
  **Does Seeking Alpha's consensus enter the Divergence score?**
  The crawl (deliverable lines 44-50): EPS and revenue mean/high/low/count/actual per fiscal year for 5 of 5; EBITDA mean and actual only;
  FCF and CFPS NOT_CARRIED (10 cash-flow item variants empty beside a firing EPS control). Source: a third-party aggregator by schema,
  vendor unnamed, programmatic reuse terms not verified (lines 86-91, labelled inferred).
  --------------------------------------------------------------------
  **REC --** Not as a score input. Bloomberg stays the source of every score number; Seeking Alpha's EPS range and analyst count are a
  recorded second instrument for the estimate-count guard and a dispersion cross-check.
  --------------------------------------------------------------------
  **RULING --** (REC adopted) Divergence reads Bloomberg only: F_cons `BEST_ESTIMATE_FCF`, the dispersion per tick-1 ruling 3 (CFPS relative
  scaling at 1FY, EPS in the same form where CFPS fails), which this crawl does not change -- Seeking Alpha adds no cash-flow dispersion and
  carries a high/low range, not a standard deviation. Seeking Alpha's EPS high, low and analyst count are kept as a SECOND INSTRUMENT: the
  score record may print the Seeking Alpha count beside Bloomberg's for the N_est guard and flag a disagreement, but never substitutes it.
  It becomes a score input only if its vendor and reuse terms are verified AND a later ruling names it. The house forecast (FWD-20) is not
  answered by any consensus feed and stays research.
+---------------------------------------------------------------------+
```

Ledger row appended to `org/tier1_exec/1.0.0_SA_CTO/drive_pairs/ctoW_AMGT_RESAPP/VERDICTS.jsonl` (tick 6). Push state: LOCAL.
