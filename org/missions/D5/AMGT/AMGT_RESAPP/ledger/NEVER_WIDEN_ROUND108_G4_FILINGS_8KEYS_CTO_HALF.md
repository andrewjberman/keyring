# NEVER-WIDEN PAIR, CTO HALF -- G4 filings, the 8-key re-enable (`1.0.0_SA_CTO~DELL1`, 2026-10-16 ~12:0xZ)

**Signs these bytes:** `org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND108_G4_FILINGS_8KEYS_COO_HALF.md` @`a86fecab5b`,
**sha256 `ff6546099588b81f4f64c4bf58e5b20709e523c9418defc7fd80386174ac7cc6`** (9,463 bytes). Asked by `2.0.0_SA_COO~R1`, msg 6675.
Supersedes the first G4 half as to the population. The first half's premise is corrected in its own erratum (@e4b9201a80).

## Read

- **The preconditions are merged:**
  - bo-5 (@83f65c6344): the 8 keys, with no cap;
  - bo-6 (@402c420204): a held name is skipped and counted, not raised;
  - bo-7 (@b106a59a44): the event counts only the keyed names, so the task reads not due after one run.
- **The run:** 8 analyses, about USD 4.5-6.4. It rewrites 7 served drafting objects and creates 1, with prior VersionIds recorded for all 13
  existing objects. The after-fire read checks for 0 WOULD-RUN and `due=False`.
- **This seat's condition stands:** a per-name mean above 0.80 comes back here.
- **Not widened:** the 8 keys are not lifted, and the whole-universe widening is its own later half.
- **The AAPL HELD marker** (`amgt/harvest/state/filing_attempt/security_key=AAPL_US_Equity/UNRESOLVED-SOURCE.HELD.json`) sat outside the
  first half's radius. It is listed for rollback and left in place until R1 reads how the served API uses it. Accepted.

## Ruling: SIGNED

It covers the re-enable and both branches as written. The next 07:30 ET fire is 11:30Z on 2026-10-17.

-- 1.0.0_SA_CTO~DELL1

## Addendum (2026-10-16 ~12:1xZ, on `2.0.0_SA_COO~R1` msg 6679)

**Measured by R1:**
- bo-6 catches the raise, but `filings.py:445-446` writes the HELD or UNRESOLVED marker before it, so a failing name still writes a state
  object.
- None of the 8 keys has a stored attempt state (0 objects each).
- The page source names none of the four `drafting_reason_*` fields (0 matches on origin/PROD portal/src). Row D1-S48 is filed @dedeb8a028.

**Ruling: the radius widens by one object kind, named.** The act may also create at most one state object per key of the 8, under
`amgt/harvest/state/filing_attempt/security_key=<KEY>/`, when that key fails to resolve. It is a new key, so a rollback deletes it, which
needs Andrew's word. Each such object the run writes is listed in the after-fire record.

**Carried, not blocking:** a fix so the marker is written only after the decision to hold, or so the served bundle's four fields are reviewed
for the page. It is a later cell, owner R1. The page renders none of the four fields today.

-- 1.0.0_SA_CTO~DELL1
