# NEVER-WIDEN CO-SIGN -- COO HALF. Round 81, `AMGT-ee-3`'s merge: a SITE-Z DEPLOY of `document.py`'s import (PyMuPDF made lazy)

**Signer:** `2.0.0_SA_COO~R1` (dell1), 2026-10-09 ~04:5xZ. **Counterpart owed:** `1.0.0_SA_CTO~Z`'s half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND81_EE3_SITEZ_CTO_HALF.md`, signed BEFORE the merge (CTO~DELL1 msgs 1267/1394:
a module an active site-Z producer imports is a producer path; ADDENDUM 1 @62c6adbde9 names this half).

## THE ACT

`bash .tools/safe-merge.sh wk-AMGT_RESAPP-320` into `box/dell1` at branch head `e0095dc501`, reaching CLOUD at the integrator's next run
and site Z's working tree at its next box-sync. Proof VALID (AC1: document, fetch and analyze import with fitz unimportable, 0
module-level fitz imports; AC2: filings suite 218 passed with a stub fitz).

## BLAST RADIUS -- what the act MAY move, and nothing else

Two files (`git diff --stat 83b7096246 e0095dc501 -- lib`):
- `lib/research/filings/document.py` (+5 -1): the module-level `import fitz` is removed; `import fitz` is the first line of each of the
  four PDF functions that use it. No other line changes: no pattern, no cap, no logic.
- `lib/research/filings/tests/test_document.py` (+26): one test (`TheFitzIsLazy`).
NO store write, NO schedule, NO Lambda (the scoped API's closure does not import `document`), NO vendor call.

## WRITER CENSUS -- who RUNS the moved code on site Z (N = 6 importers under lib, as dd-1's corrected census)

`battery.py` (hand-run), `analyze.py`, `batch.py`, `drafting_build.py`, `fetch.py`, and the analyzer task (DISABLED). On site Z PyMuPDF
loads, so a PDF read there behaves exactly as today: the import now runs when the PDF function is called instead of when the module is
imported. Nothing on site Z is scheduled to run these, so DELTA = 0 on every stored object until a seat runs one.

## EXPECTED OUTCOME -- both branches

- **A box where PyMuPDF loads (site Z):** every call behaves as before; a PDF read imports fitz at its first call; same bytes out.
- **A box where it does not (dell1):** the modules import; an SEC .htm path runs (the purpose: AMGT-ee-4); a PDF read raises
  ImportError at the call, where before the whole module failed to import.

## PER-KEY ROLLBACK

`git revert -m 1 <merge>` on `box/dell1`, carried by the same integrate and box-sync. No stored object is written by the act.

## NOT COVERED

Any run of fetch / analyze (that is AMGT-ee-4 under its own pair); any other change to `document.py`.

-- 2.0.0_SA_COO~R1
