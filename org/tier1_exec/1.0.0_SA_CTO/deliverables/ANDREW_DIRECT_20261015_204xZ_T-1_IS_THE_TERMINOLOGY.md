# ANDREW_DIRECT 2026-10-15 ~20:4xZ -- "T-1" is the term for the price as-of

**Channel:** Claude Code terminal, dell2, to `1.0.0_SA_CTO~DELL2`, mid-turn while PRD v0.16 was being written. **Recorded by:**
`1.0.0_SA_CTO~DELL2`. The record is late by the same session: the sentence went into PRD v0.16 (@a4af0e5bba) first. That gap is the
provenance point `3.0.0_SA_CVO~DELL2` raised (review @6e93eb4238), and this record closes it.

Andrew's words, verbatim:

> "T-1 is the correct terminology, let's just stick to that"

**Context:** the no-price-date-selection word earlier the same minute (`4.0.0_SA_CRO~DELL2`'s record
`ANDREW_DIRECT_20261015_204xZ_NO_PRICE_DATE_SELECTION_LATEST_CLOSE.md`, which also carries his "You are correct" on the CRO's reading).

**What it binds:** every price the Analysis Request uses is the T-1 close, the frontier of `lib/trading_calendar.py`, stated as the as-of.
No record, field or label uses "T+1" (IRPT_ANLREQ PRD v0.16, C-PRICES).
