# 4.0.0_SA_CRO~Z -- Seeking Alpha consensus crawl for AMGT_RESAPP, 19:11-22:03Z 2026-09-15

**archetype:** MIXED (EXPLORE, VALIDATE, SCRIBE)

## What was asked

Andrew-direct ~19:0xZ at the 1.0.0_SA_CTO~W terminal (record @a026de4004), routed to this seat by serial and
relayed twice (1.0.0_SA_CTO~W msg 23221, 0.0.0_AB_MSTR~Z msg 23227): *"Ask CRO~Z to explore Seeking Alpha with an
authenticated crawl, they should have consensus figures."* For BA, COST, HD, SAP, BABA: whether SA serves consensus
per fiscal year for FCF, CFPS, EPS and revenue (mean/median, high, low, analyst count, revisions), every absence
classed NOT_CARRIED vs NOT_REACHED, and whether the figures are SA's own or a relay.

## The correction that shaped the method

Mid-turn at ~19:30Z, at this terminal, VERBATIM: *"do not reinvent the wheel with seeking alpha scraping, we have
the harvest scrapers for this reason to get cookies and they are canonical."* Recorded and committed @1a2a676265.
This seat had started a bespoke Playwright route-discovery script; ABANDONED it. Its one run had already failed on a
Git Bash path-mangling defect (the `/symbol/...` args rewrote to Windows paths) and recorded 0 calls, so nothing was
lost. The crawl then ran entirely through the canonical rider.

## Method, canonical only

`sa_rest_fetch.build_session` imported as a library: the parked `seeking-alpha/session` cookies, the residential
proxy, Chrome TLS impersonation, the proxy-CA `verify=False`. GETs to SA's JSON estimates API with the documented
per-page `Referer`. No browser, no new scraper. Secrets read through `comp-secrets get --reveal` into a locked
session-scratch dir; comp-secrets wraps the value in a `value:` line envelope, so the extraction takes that line and
JSON-parses it. Parked session confirmed authorized before any estimate call (`check` -> Annual, active, via proxy).

## Findings

- **The consensus route:** `GET /api/v3/symbol_data/estimates?period_type=annual&relative_periods=-1,0,1,2,3&ticker_ids={id}&estimates_data_items={items}`. ids BA 769, COST 58, HD 799, SAP 1320, BABA 137271.
- **EPS and revenue: CARRIED 5 of 5** -- mean, high, low, num_of_estimates, actual, FY-1..FY+3, each dated.
- **EBITDA: CARRIED 5 of 5, mean + actual only** (no dispersion).
- **FCF and CFPS: NOT_CARRIED**, discriminated on BA: 10 documented cash-flow item-name variants empty while an EPS
  control returned on all 11 calls and an EBITDA positive control returned in the same call. The positive control is
  what makes it NOT_CARRIED rather than a route we failed to reach.
- **Source:** a licensed third-party consensus aggregator by payload schema, not SA's own contributor content;
  aggregator name and reuse terms NOT verified (inferred from shape).
- **Bounded, named, not chased:** explicit up/down revision counts (empty `revisions` sibling needs revision items;
  timing is on every effectivedate) and quarterly periods.

Bears on the Model tab Divergence: neither Bloomberg nor SA carries FCF dispersion; SA carries EPS dispersion for all
five, so Andrew's item-2 CFPS-or-EPS choice resolves toward EPS on coverage. The house forecast F_model is not
answerable from a consensus feed and stays research for 4.0.0_SA_CRO~W.

## Acts, each read back after it landed

| act | artifact | read-back |
|---|---|---|
| record of the ~19:30Z word | `.../ANDREW_DIRECT_20260915_193xZ_...md` @1a2a676265 | in HEAD, pure ASCII |
| deliverable | `.../AMGT_RESAPP_SEEKING_ALPHA_CONSENSUS_CRAWL_20260915_Z.md` @910dc1bb7e | in HEAD, blob matches worktree, pure ASCII |
| carrier to the asker | 1.0.0_SA_CTO~W inbox 20260915T220240Z | delivered |
| record + classed-absent to the carrier | 0.0.0_AB_MSTR~Z inbox 20260915T220252Z | delivered |

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `comp-secrets list` / `get --reveal --json` / `get --reveal` | secrets located and read | The value is on a `value:` line in the output envelope; `--json` did not return bare JSON. Parse the `value:` line. |
| `sa_rest_fetch.py check` (canonical) | authorized, Annual, active | The authorization oracle before any estimate call. |
| canonical `build_session` ridden by three scratch probes | estimates route 200; matrix; FCF discrimination | Reused the canonical session builder; no new scraper. |
| `.tools/aws s3 ls raw/seekingalpha/*` | HD_US and SAP_GY have no stored harvest objects; BA/BABA/COST do | Coverage of the existing pool, not this crawl. |
| `.tools/safe-commit.sh` x2 | @1a2a676265, @910dc1bb7e, msg-verify MATCH | -- |

## Parked / not chased

- The bespoke discovery script's failure (Git Bash rewriting `/symbol/...` to a Windows path) is a device instrument
  trap, not a Seeking Alpha finding. Memory-worthy but not this crawl's subject.
- Raw estimate JSON per ticker sits in this session's scratch only, not committed: raw vendor bytes belong in the
  harvest pool's `raw/seekingalpha/{key}/{stamp}/` shape under the harvest owner's cadence, which Andrew reserves.

## Current State

The Seeking Alpha consensus crawl is DONE and committed (@910dc1bb7e, LOCAL). The asker (1.0.0_SA_CTO~W) and the
carrier (0.0.0_AB_MSTR~Z) have it. POSN_AGGFIX PRD v0.2 remains ADMITTED with both L4-R halves SIGNED; nothing owed
there. This lane holds 0 open task orders. Push state: LOCAL, origin/SITEZ 6f09a06dc9.

## Blockers

None. The house-forecast follow-up and the wider tab-score research are 4.0.0_SA_CRO~W's brief, not this seat's.

## Next Steps

1. **[4.0.0_SA_CRO~W]** Cite this crawl in its five-point findings brief (per the CTO's research brief @a026de4004).
2. **[1.0.0_SA_CTO~W]** Rule CFPS-vs-EPS for Divergence on the coverage above (its call, not this seat's).
3. **[4.0.0_SA_CRO~Z]** Event-driven: L4-R re-read only on a POSN_AGGFIX brief-half bump; SA follow-ups (revision
   counts, quarterly) only if asked. Re-arm the inbox Monitor on each expiry.
