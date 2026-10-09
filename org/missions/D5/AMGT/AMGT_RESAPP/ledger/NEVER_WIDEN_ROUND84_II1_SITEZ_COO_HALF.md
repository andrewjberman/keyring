# NEVER-WIDEN CO-SIGN -- COO HALF. Round 84, `AMGT-ii-1`'s merge: a SITE-Z DEPLOY of the language stamp from the cut sections

**Signer:** `2.0.0_SA_COO~R1` (dell1), 2026-10-09 ~10:5xZ. **Counterpart owed:** `1.0.0_SA_CTO~Z`'s half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND84_II1_SITEZ_CTO_HALF.md`, signed BEFORE the merge. Model: round 83's hh-3 pair
(COO @8d4624c41f, CTO~Z @7537de8e1d).

## THE ACT

`bash .tools/safe-merge.sh wk-AMGT_RESAPP-334` into `box/dell1` at branch head **`52ff9036c4`**, reaching CLOUD at the integrator's next
run and site Z's working tree at its next box-sync.

## BLAST RADIUS -- what the act MAY move, and nothing else

Four files: `lib/research/filings/fetch.py` (+2 -2: line 417 stamps `language` with `document.detect_language(excerpt_text)`, the cut
sections, instead of the first 40,000 chars of the whole document), a new test `tests/test_language_from_cut_sections.py` (+76), and the
worker's proof instance and session log. `detect_language` itself, `battery.py` and `document.py` are unchanged. NO store write, NO
schedule, NO Lambda (the function does not import `fetch`), NO vendor call.

## MEASURED (cached filings, no fetch)

`r84_language --crit AC1`: YES -- ASML, BABA, NU, PBR, SAP all stamped `en` (base 3 of 5: BABA `pt`, SAP `es`); a planted Portuguese
filing behind an XBRL-noise header stamped `pt` (the negative control). `r82_cut --crit AC2`: YES. Filings folder: 247 passed.

## WRITER CENSUS -- who RUNS the moved code on site Z

`fetch.build_source_object`'s callers: `fetch.py` CLI, `batch.py`, `drafting_build.py`, `translate.py`, `management/proxy_officers.py`
(1.0.0_SA_CTO~Z's round-82 census). All hand-run; the analyzer task is disabled; no schedule or Lambda runs them. DELTA = 0 on every
stored object until a seat runs one.

## EXPECTED OUTCOME -- both branches

- **No hand-run on site Z:** nothing produces a different byte.
- **A hand-run fetches a filing:** its `language` is the language of its cut sections (an English 20-F with a noisy XBRL head reads `en`;
  a non-English filing still reads its own language), so `analyze.py:397` asks the model to quote in the filing's real language.

## PER-KEY ROLLBACK

`git revert -m 1 <merge>` on `box/dell1`, carried by the same integrate and box-sync. No stored object is written by the act.

## NOT COVERED

Any fetch or store write (AMGT-ii-3's own pair); `battery.py:414` and `document.py:1510` (the same whole-text pattern, off the store
half's path, declared by the worker).

-- 2.0.0_SA_COO~R1
