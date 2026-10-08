# IRPT_BCKEND round 69 -- workstream ~Y decomposition (E11: Performance client statement submissions compose with the custody revision)

Issuer `2.0.0_SA_COO~Y2`, 2026-10-08 ~22:3xZ. Input: `1.0.0_SA_CTO~DELL2` ADDENDUM 10 (sweep 21, msg 1512), item E11, on row
`IRPT_BCKEND-D2-W177-S2`. Naming: Andrew-direct ~21:2xZ (CTO msg 1655): records and messages say "Performance client statement";
code ids (`CUSTODY_REPORT`, `irpt-custody-x10-v1`, `custody_submission.py`) are unchanged. ONE issuance, one cell, no edges.

**Dependencies, met at issuance:**
- E9 live: `PbyqmHBQ`, 64 of 64, ADJUDICATION_v40 @8d06a3d200; CTO ADDENDUM 12.
- E6 released: X-1 release 3 live at 21:26:18Z, drained @84916b911a.
- E11 rides the release AFTER E6, never E6 itself.

| item | cell | cut? |
|---|---|---|
| E11: `ycharts/generate/custody_submission.py` builds its retained repositories with the custody revision, through the SAME registry probe E9 used in `export/submit_installed.py` `retained_reports`. The custody revision is requested only when `reporting_policy(CUSTODY_POLICY_REVISION)` resolves; otherwise the build is as before. | `IB-yr-691` | **CUT** |

| criterion | invocation | base reading |
|---|---|---|
| Y69-1-AC1 (statement submissions carry the custody revision; PERFORMANCE and ANALYSIS unchanged; an unregistered revision composes as before) | `python -m pytest -q -p no:cacheprovider infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_custody_submission_revision.py` | FAIL: the file does not exist at base |
| Y69-1-AC2 (regression: the custody suites) | `python -m pytest -q -p no:cacheprovider infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_custody_composition.py infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_custody_entry.py infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_custody_retained.py` | recorded by the worker at base before the edit; must not regress |

Risk WORLD by the L6 gate floor on infra/aws paths (ADDENDUM 10 names LOCAL; no deploy here). Per ADDENDUM 10 the change rides `~Y2`'s next release pair. It is packaged from `source_dir`, so the next
`irpt-ycharts-generate` build carries it.

## Four-postulate record

(i) Domain: the one composition call in `custody_submission.py`. (ii) One call site. (iii) One intent: statement submissions retain
under the custody revision. (iv) PERFORMANCE and ANALYSIS families, the export function (E9/E10) and every deployed byte do not move.

fanout: 1 of 1 chains, cap 8, reason: one item. Worker slot `~220`: the Y block 150-159 is used up; Y extends to 220-229, beside P
160-199 and M 200-219.
