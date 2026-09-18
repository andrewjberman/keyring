# Andrew-direct ~16:xxZ 2026-09-18 -- run the EDGAR check; web-search egress for foreign filing-channel research

**Recorded by:** `4.0.0_SA_CRO~Z`, at this terminal, before the first call it authorizes.
**Context:** the THESIS panel review. Bloomberg's DAPI returns an SEC CIK (`CENTRAL_INDEX_KEY_NUMBER`) for all 22
covered names that carry no filing identity, and for NVIDIA, but no field says which of them file annual reports
with the SEC, and no field returns filing text. This seat asked for a per-use word before calling EDGAR.

## Verbatim

> go, run the EDGAR check,  you have egress for web search for additional foreign channel reserach

## Reading, narrow

1. **EDGAR:** one read-only lookup per name against the SEC submissions endpoint the estate's own
   `lib/research/filings/fetch.py` already uses (`https://data.sec.gov/submissions/CIK##########.json`), for the 23
   names above, to learn which file a current 20-F or 10-K. Dry run: nothing is fetched beyond the submissions index,
   nothing is written to the pool, no analyzer runs, no schedule changes.
2. **Web search:** egress for WEB SEARCH to research foreign filing channels (regulator repositories, exchanges,
   annual-report sources) for the covered names that have no SEC path. Research only -- it authorizes no scraper,
   producer, pull cadence or pool write, and no Bloomberg Terminal traffic interception.
3. Both are per-use words for this investigation, not standing egress.
