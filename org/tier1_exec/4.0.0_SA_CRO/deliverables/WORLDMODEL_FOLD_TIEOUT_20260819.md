# WORLDMODEL FOLD TIE-OUT — the @6096e11d95 ingestion validated end-to-end (Andrew-ordered)

**Author:** 4.0.0_SA_CRO · **Date:** 2026-08-19 · **Method:** full sha256 tree-compare (satellite
repo, `.git` excluded → `infra/system/ontology/worldmodel/`), script-run this session; every count
below is measured, denominators in-line.

## VERDICT: THE FOLD TIES. Zero content loss, zero silent mutation, every delta explained.

| Check | Result |
|---|---|
| Content fidelity | **62 of 62 shared content files BYTE-IDENTICAL** (sha256) — the fold's own "62 files byte-faithful" claim ties exactly |
| The one intended difference | `README.md` deliberately REWRITTEN for the new home (5,226 → 2,748 B) — verified it carries: the fold authority verbatim, park semantics ("changes HOME, not state"), the canon relationship (SYSTEM_DEFINITIONS canonical; worldmodel defers per its own CANON_ALIGNMENT), the exclusion statement, the SYSPARITY WS-4 note |
| The exclusion | **513 files / 427,022,680 B under `20_rulings/archives/deleted_bucket_archives/`** — exactly the declared class; the six bucket dirs match the README's six by name (ajb-workflow, opal-analytics-dashboard, opal-ci-staging, opal-crawl-catalog, opal-data-aaii-v2, opal-market-data-v2). *Unit nit, not a defect: measured = 407.2 MiB / 427.0 decimal-MB; the "~409MB" prose figure sits between conventions — the count and names are what tie.* |
| Left behind (non-archive) | **ONLY `.gitignore` (126 B)** — correct to leave; nothing else in the satellite failed to fold |
| The 68-vs-62 delta (banked at fold-verify) | **FULLY EXPLAINED:** 62 content + 1 rewritten README = **63 tracked** (`git ls-files` = 63); + 5 `__pycache__` .pyc files that were DISK residue, never tracked (`infra/.gitignore:41` catches them) — removed this session (regenerable caches) |
| The 121-vs-118 ledger delta (banked at fold-verify) | **ADJUDICATED — vintage, not integrity:** source and target ledgers are byte-identical; the satellite's own ledger carries 121 rows, so the v0.1 PRD's "118" was true at its authoring and 3 rulings landed in the satellite afterward. No loss either side of the fold |
| Ties outward | PRD v1.1 §6 home pointer resolves; census seed declaration (`10_census/` = 07-31 vintage snapshot) matches the README's own statement; the archive-residue disposition (S3 bucket + manifest, CTO pending) is named identically in README, PRD §7, and JSON |

**Residual (pre-existing, unchanged by this validation):** the 427MB archive set still lives ONLY
in the retired satellite's local copy until CTO's S3 archive lands — that is the one remaining
single-disk item, and it is rollback insurance, not program evidence.

**Live-census fold (the A2/A3 re-derivation returned during this validation, comp-kuzu):**
portal 11,338 · ms 5,958 · aws 2,043 · pipeline 1,337 · semctl 23 · **codebase ABSENT** —
total 20,699. Confirms live: A2 FAILS-b (codebase universe declared, zero materialized) and the
S0 half-landing (retired `pipeline` value still on 1,337 nodes; dropped `semctl` still on 23).
Deltas vs the 08-12 build: ms +72, aws −12, portal/pipeline/semctl unchanged.
