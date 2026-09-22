# AMGT_RESAPP round 30 -- never-widen pair, `AMGT-rk-118` (L-FIL) -- the COO half

**Author:** `2.0.0_SA_COO~Z`. **Status: DRAFT -- signed at the round-30 issuance.** The paired CTO half is written by
`1.0.0_SA_CTO~Z` at `ledger/NEVER_WIDEN_ROUND30_RK118_CTO_HALF.md` against live pre-act reads. The order does not act
on one half (its AC0).

**Sources:** PRD v0.23 s.12 stage 3; the CTO's stage-3 ruling msg 24257 (issuer site only, no hkexnews); msg 24328;
rk-105's SKIP-HELD / CHANGED-HELD rules; rk-98's bronze sink; the order
`task-orders/AMGT_RESAPP.TO-AMGT-rk-118.lenovo-filings-battery.md`.

**Measured by the issuer, read-only, 2026-09-22 ~18:5xZ.** Where the worker's AC1 re-read differs, the ROLLBACK
TARGET is the worker's value.

## THE ACT

ONE battery invocation for ONE security:
`python -m lib.research.filings.battery --security-key 992_HK_Equity --write-bronze --write-pool --cache-dir ... --out-dir ...`
- **Public sources only. No vendor word is spent**: SEC EDGAR and the issuer's own site are public. No Bloomberg, no
  Lusha, no Seeking Alpha, no model call.
- Ceiling: 1 SEC ticker-table fetch + at most 1 EDGAR index + at most 1 EDGAR document + **at most 40** issuer-site
  pages (`_step4_company_site`'s `max_pages` default, printed by AC0) + the documents the crawl accepts.

## BLAST RADIUS

What the act MAY touch, and nothing else:
- **(B1) `sec/harvest/bronze/company_tickers/<date>/company_tickers.json`** -- 0 -> 1 estate-wide if step 1 runs.
  Immutable; one fetch per UTC day by rk-98's own rule.
- **(B2) `sec/harvest/bronze/filing/...`** -- a document only if step 2 (EDGAR by CIK) fetches one. Immutable.
- **(B3) `issuer-site/harvest/bronze/document/...`** -- one object per step-4 CANDIDATE document the crawl checks
  (rk-98's ruled behaviour, not only the winner). Immutable. 0 objects estate-wide today.
- **(B4) SERVED: `amgt/harvest/state/filing_attempt/security_key=992_HK_Equity/UNRESOLVED-SOURCE.json`** -- Lenovo's
  existing object, subject to rk-105: an UNCHANGED outcome is SKIP-HELD and writes NOTHING; a CHANGED outcome is
  CHANGED-HELD, writes NOTHING, and the run exits non-zero. **The key is write-once and refuses an overwrite by
  contract, so this act can only ADD where nothing exists.**
- **(B5) SERVED: `filings/v1/992_HK_Equity/...`** and its `filing_source` silver -- only on a RESOLVED outcome.
- **(B6) The served Thesis tab for Lenovo** reads `filing_attempt`'s reason when there is no drafting document
  (`scoped_amgt.py:1954-1981`, used at `:2052-2055`). If this run RESOLVES, **the adapter will still serve the OLD
  UNRESOLVED reason** until the supersede reader cell lands (the CTO's carried item at round 27, Z-S225's sibling).
  That is expected, it is named here, and it is a trial finding rather than a defect of this cell.

**NOT moved** (asserted by AC3, AC4, AC5):
- any `filing_attempt` or `filings/v1` object for ANY security other than `992_HK_Equity` (AC3 prints `foreign 0`);
- any bronze under another security's partition;
- **`hkexnews.hk` or any regulator host** -- excluded by msg 24257, and the measurement shows nothing pulls one in by
  accident (HK has no `EXCHANGE_LISTING_PAGES` template, so no exchange seed exists);
- the crosswalk, `registrations.json`, identity bronze, the model block, DynamoDB, Lusha, Seeking Alpha,
  publications, social;
- every Lambda, IAM policy, layer and the portal.

## WRITER CENSUS

- **(B4) `filing_attempt`:** N = **1** function, `lib/research/harvest/filings.py::state_put_filing_attempt`, reached
  from **6** call sites; the one this act uses is `fetch.persist` via the battery CLI's `--write-pool`. The function
  is write-once (conditional put) and, since rk-105, answers an unchanged outcome with SKIP-HELD and a changed one
  with `FilingAttemptChangedError`.
- **(B5) `filings/v1` + `filing_source` silver:** N = **1** writer, `fetch.persist`'s RESOLVED branch.
- **(B1)-(B3) bronze:** N = **1** writer, rk-98's `fetch.BronzeSink`, threaded into battery steps 1, 2 and 4 only.
- **(B6) the served reason:** N = **1** reader, `scoped_amgt._read_filing_source_object`. This act writes no adapter
  code and deploys nothing.
- **The act's own write set, one call deeper:** the battery performs S3 puts only through the two writers above; 0
  IAM writes, 0 Lambda writes, 0 DynamoDB writes, **0 deletes**.

## EXPECTED OUTCOME -- read from the producers' own rules, every branch covered

Read from `run_battery`'s ordered steps and rk-105's rules, not predicted from the input's shape:
- **Branch RESOLVED (issuer site):** (B3) gains the candidate documents, (B5) gains Lenovo's source object, (B4) is
  untouched because the outcome is no longer UNRESOLVED. The Thesis tab keeps serving the old reason until the
  supersede cell lands (B6).
- **Branch RESOLVED (EDGAR by CIK, step 2):** possible for the first time, because rk-121 supplies CIK 932477 for a
  name the PRD calls "not an SEC filer". (B2) and (B5) gain objects. **This is a trial FINDING, recorded, not a
  violation:** EDGAR is public and is the producer's own ordered route.
- **Branch UNRESOLVED, outcome UNCHANGED:** rk-105 prints SKIP-HELD, **0 puts** for (B4). The stage ends UNRESOLVED
  with its reason, which msg 24257 admits as a trial finding.
- **Branch UNRESOLVED, outcome CHANGED:** rk-105 prints CHANGED-HELD with the differing field, **0 puts** for (B4),
  and the run exits 2. The served reason stays the OLD one. Also a finding, not a failure.

## PER-KEY ROLLBACK -- NEVER A DELETE

- **(B4) `filing_attempt`:** the key is write-once and refuses an overwrite, so there is nothing to undo; a wrong
  outcome is superseded only by the reader cell the CTO carried, never by a delete or an overwrite.
- **(B5) `filings/v1` / silver:** a wrong source object is LEFT and recorded; a corrected object is written only under
  an issuer-authorised re-run. The silver row is append-only.
- **(B1)-(B3) bronze:** immutable, and no production reader keys on a specific stamp. LEFT and recorded.
- **(B6) the served reason:** not written by this act; nothing to roll back.
- **A FOREIGN-SECURITY write is the one true rollback trigger**, and its remedy is a BLOCKING row plus an OPEN ledger
  entry naming the served state -- **not** a delete, which is Andrew's word.

## NOT COVERED

- any security other than `992_HK_Equity`;
- `hkexnews.hk` or any national-regulator route, and any registry row for one (that belongs to the registry lane on
  the other fabric, recorded as an OPEN ITEM for the trial report);
- ESEF (does not apply to HK);
- the analysis / drafting stage (stage 5), which waits on this cell landing a document;
- the adapter's supersede reader (the CTO's carried item), Lusha, Seeking Alpha, the model block, DynamoDB;
- any code change, schedule, alarm, IAM change or portal change;
- any S3 delete.

Each needs its own pair. The held branch `wk-amgt-14-50` is not read or named as a surface.

**Signature (COO):** to be signed `2.0.0_SA_COO~Z` at the round-30 issuance; the issuance commit's hash is the
signature's vintage.
