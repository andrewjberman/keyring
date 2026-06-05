# Work — FIND_DUALBIZ engagement kickoff: fingerprint, pipeline codification, broader-scan (2026-06-05)

**archetype:** IMPLEMENT
**secondary_archetypes:** EXPLORE, DESIGN

Andrew-direct live engagement. "Reformat the FIND_INSURE engine around a new target": discover
small/mid firms running insurance + a parallel AUM business (the Paraclete/49 profile), seeded by
3 exemplars (Paraclete, 49 Financial, FIG).

## Arc

1. **Seed profiling** — browser-UA fetch + SEC/FINRA public records of the 3 seeds. Finding: they are
   one insurance+AUM organism at 3 tiers (FIG aggregator → Alphastar affiliated-RIA/TAMP → Paraclete
   producing; 49 = integrated, own RIA). PRIMARY discriminator = the dual-entity **disclosure-footer
   boilerplate** ("advisory services offered through [RIA], a SEC-registered investment adviser …
   separate and independent entities"). The existing FIND_INSURE `am_prominence` scorer false-negatives
   Paraclete (insurance-front site, RIA only in the disclaimer) → re-tune, don't blindly reuse.
2. **Andrew rulings** — exclude the old 99-IMO giants (too big to be useful); size/practicality screen
   first-class; overfit on 49/Paraclete OK; scrape stack = browser-UA curl + Playwright escape-valve,
   NO Bright Data.
3. **Brief** (doc-of-record) — `docs/briefs/find-dualbiz-seed-fingerprint-and-pipeline-design-20260605.md`
   (b1a9aa6d7 + amendments).
4. **Engine B1 PoC** — disclosure-string reverse-search (`"offered through Alphastar Capital Management"`)
   returned Alphastar's producing-agency roster first-pass: Ramer + Refined confirmed small dual-business
   producers. Zero cost, browser-UA.
5. **Pipeline codified** — new `data/find/dualbiz/` tree (config fingerprint + tamp-seeds; `_util` browser-UA
   fetch; `fingerprint.py` scorer; `discover.py`; `pipeline.py` discover→bronze→silver→gold→serving).
   Validated: Paraclete producing/present, Ramer producing/present, 49 integrated/present. ds-gate clean.
6. **Broader-scan** — `broaden.py` + `provider-seeds-v1.json`: provider = IMO/FMO + affiliated RIA pair;
   `generate_disclosure_strings()` reverse-engineers the search strings. Discovered Advisors Excel/AE
   Wealth, AmeriLife/Brookstone, SMS/Sequent. Harvested 6 new producing candidates → roster 5→11.
   Adjacent firms with JS-rendered disclosure correctly flagged fetch-limited (Playwright = next).

## Files / commits (my author line)

| Artifact | Commit |
|---|---|
| Seed brief (doc-of-record) | b1a9aa6d7 |
| Brief amendments (rulings + Engine B1 PoC) | 69d3c93a5 |
| Pipeline codified (`data/find/dualbiz/` config + scripts + README) | (this session) |
| Broader-scan (broaden.py + provider-seeds + tamp-seeds expansion + brief §5.3) | (this commit) |

## Compiler Tools

| Tool | Result |
|------|--------|
| `.tools/ds-commit-gate.sh` (all dualbiz .py) | All checks passed (py_compile + ds-precommit-check + ruff) |
| `python fingerprint.py` | scorer smoke OK (synthetic producing disclosure → present) |
| `python pipeline.py [--deep]` | end-to-end run; serving table emitted |

Read-only S3/graph tools N/A — this is a new local discovery pipeline, no gold-script or S3 artifact yet.

## State / next

- Pipeline runnable + repeatable; broader-scan proven (providers → disclosure strings → producing rosters).
- **Next hardening (clear):** wire the Playwright escape-valve to fetch JS-rendered disclosure footers
  (converts known producing/adjacent → present at scale); run peer-provider discovery wider.
- FIND_DUALBIZ tracked provisionally by COO (b970bcdd6); full PRD/bucket/project formalization held for
  CTO+Andrew elevate-call. Lead = 0.1.0_DS_MI. Andrew-direct live.
