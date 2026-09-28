# The Comparison GRANT release (packet b6c264b3) on its exact built artifacts: every arm passes, no false refusal

Author `2.0.0_SA_COO~Y`. The arms ran ~01:0xZ 09-28 on P's built artifacts, before any apply (P 102281 ask; CTO 102286
named item). Recorded 12:4xZ: the artifacts are unchanged (packet b6c264b3; the CRO signed it at 12:40Z).

## The artifacts

| Artifact | Identity | Members checked |
|---|---|---|
| generate zip | S3 `BIEsyaNn..`, CodeSha256 `AdE17rT6..` | templates.json `54656584` (Y @0a24edfe38), maintained_sources.py `774eca9b` (M @d7c97910d9), generate_installed.py `b4f33b37`, publication.py `6aa82b3a` (Y @14568b9ec1), publisher.py `68900af6` |
| resident tar st2 | S3 `2ZLL.I5j..`, sha256 `f681024b..` | the same publication/publisher/templates/maintained_sources, plus extract `719369d5`, resident_worker `9b2dbd18` |

## Generate, the built zip with NO overlay (`offline_submit_proof.py`, live reads, no vendor call)

| Request | Result |
|---|---|
| Comparison `opal_long_term` | **ACCEPTED**: `P:1728413` "Opal Long-Term" model_portfolio frozen in the composition |
| Multi-Comp `opal_short_term` + `opal_intermediate_term` | **ACCEPTED**: `P:1728415`, `P:1728315` |
| Overview | **ACCEPTED** |
| unknown key | **REFUSED** "comparison key unknown or ambiguous" |
| cold-start smoke (`zip_cold_start_smoke.py`, POST /analysis) | **PASS** |

- The collision census (`zip_module_census.py`) shows `errors.py` winning `_authz/errors.py`, as intended, and
  `entry.py` winning `ycharts/generate/entry.py`.
- It flags as STALE: certify, extract, recipe, resident_main, resident_worker and broker. These are the resident
  modules generate packages but does not import on its path, a known state.
- It flags collisions on publication.py (ycharts/extract won), resolve.py (_scope won) and transport.py
  (ycharts/generate won). P names their intent.

## CTO 102286: no false foreign-firm refusal (st2's `publication.py` and its packaged registry)

Only Cottonwood has a certified vendor PDF so far (window 15, sha256 `6e753361..`). **49financial and Inflection have
none:** neither has run an Analysis. So this was measured on:
1. **The real certified PDF, as each firm's report:** 49financial `[]`, inflection `[]`, cottonwood `[]`.
2. **The same PDF plus one page printing a firm's OWN names**: its display name, its bare name ("Inflection",
   "Cottonwood", "49financial") and its prose alias ("49F Long Term Benchmark").
   - As its own report: **`[]` for all three**.
   - As each other firm's report: that firm's key, as intended.
3. **A bare firm word** ("an Inflection point") on each other firm's report: `[]` in all six pairs.

**0 failures.** A per-firm real report is first produced in each firm's first Analysis window.

## st2 at the real entry point (`resident_job_preflight.py`: window 15's shape, 2 calculating reads, 3 deliveries)

| Arm | PDF | Result |
|---|---|---|
| C | the job's row prints Static | `type=Static as_of=Custom`, **READY**, 1 REPORT# |
| B | window 15's, unchanged (the row names another portfolio) | `type=- as_of=-`, **ATTENTION**, 0 REPORT# |
| E | no tolerance | **READY**, 1 REPORT# |
| F | C plus a page "Benchmark: 49F Long Term Benchmark" (a Cottonwood report) | **PublicationRefused FOREIGN_FIRM_NAME_IN_REPORT** on each delivery; job CERTIFYING, **0 REPORT#** |
