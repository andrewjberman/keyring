# NEVER-WIDEN CO-SIGN -- COO HALF. Round 80, `AMGT-dd-1`'s merge: a SITE-Z DEPLOY of the filing cutter

**Signer:** `2.0.0_SA_COO~R1` (dell1), 2026-10-09 ~02:4xZ. **Counterpart owed:** `1.0.0_SA_CTO~Z`'s half, at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND80_DD1_SITEZ_CTO_HALF.md`, signed BEFORE the merge
(`1.0.0_SA_CTO~DELL1` msg 1267; ruled a producer path by msg 1394: a module an ACTIVE site-Z producer imports IS a producer path).

## THE ACT

`bash .tools/safe-merge.sh wk-AMGT_RESAPP-315` into `box/dell1`, which reaches `CLOUD` at the integrator's next run and site Z's
WORKING TREE at site Z's next `Opal box-sync` (the census @6a308cd424: the daily pull runs site Z's working tree). Branch head
`ae77bcc57f`, proof VALID (AC1-AC3 SERVED: YES; filings folder 192 passed; api folder 2 failed, both `pypdf` absent on dell1).

## BLAST RADIUS -- what the act MAY move, and nothing else

Four product files and three test files, exactly (`git diff --stat a0db38c8ae ae77bcc57f -- lib`):
- `lib/research/filings/document.py` -- a 20-F `business` key (Item 4.B Business Overview, cap 60000); the 10-K patterns and
  the three existing 20-F keys hash as before (AC3, 6 of 6).
- `lib/research/filings/fetch.py` -- one line: `EXCERPT_ITEMS["20-F"] = ["business", "risk", "mdna"]`.
- `lib/research/filings/section_coverage.py` -- one line: `_WANTED["20-F"]` equal to the producer's table.
- `lib/research/filings/section_census.py` -- NEW, read-only (it writes nothing).
- tests: `test_document.py`, `test_section_census.py`, `test_section_coverage.py`.
NO store write, NO schedule, NO Lambda (the function moves only at its own redeploy under its own pair), NO vendor call.

## WRITER CENSUS -- who RUNS the moved code on site Z (CORRECTED in place on 1.0.0_SA_CTO~Z's condition C3, @f1a7df146f: N = 6 importers under lib -- `battery.py`, `analyze.py`, `batch.py`, `drafting_build.py`, `fetch.py` itself and `lib/research/api/scoped_amgt.py`, plus tests. `analyze.py`, `batch.py` and `drafting_build.py` are libraries that run on site Z only inside a hand-run or a disabled task; no scheduled site-Z task runs any of them, so DELTA = 0 holds. The three entry points the act can reach are read below)

1. `lib/research/filings/battery.py` (census row 28, a HAND-RUN, `:507-519` its Terminal leg): imports `document` and `fetch`.
   Its next hand-run 20-F cut adds a `business` item to the excerpt; `_winning_edgar_extra` (`battery.py:832`) and the 20-F
   "no named item could be cut" reason now list `business`. No hand-run is scheduled; one runs only on a seat's ask.
2. `-FilingsAnalyzer` task (census row 29): DISABLED. While disabled it runs nothing.
3. `opal-amgt-scoped-api` (imports `section_coverage` at serve time): NOT moved by this act; at its next redeploy each 20-F
   name's `passage_coverage` lists Item 4.B as wanted (and, for the 5 stored 20-F names, not covered, which is true: 0 of 5
   hold one -- the census).

## EXPECTED OUTCOME -- both branches

- **No hand-run battery and the analyzer disabled (the case today):** nothing on site Z produces a different byte; DELTA = 0
  on every stored object until a seat runs a battery.
- **A hand-run battery cuts a 20-F:** its stored source object carries a `business` item when the filing has a Business
  overview heading, or the item `FAILED` with its reason when it has none; risk / mdna / officers cut exactly as before (AC3).

## PER-KEY ROLLBACK

`git revert -m 1 <merge>` on `box/dell1`, carried to `CLOUD` and site Z by the same integrate and box-sync. No stored object is
written by the act, so none is restored. A battery run between the merge and a revert is its own act with its own record.

## NOT COVERED

Re-cutting ASML NA (SEC fetch, silver write, re-analysis): Andrew's per-use word, its own pair. Any served change: the Lambda's
own redeploy under its own pair.

-- 2.0.0_SA_COO~R1
