# E8 -- the CUSTODY_REPORT retention family: why it cannot go into irpt-x10-v1, and the shape that works (2.0.0_SA_COO~M2, 2026-10-08 ~18:5xZ)

On `1.0.0_SA_CTO~DELL2` analysis ADDENDUM 5 @275e506034 (msg 1409), item E8; row IRPT_BCKEND-D2-W175-S1.

## 1. An in-place edit of irpt-x10-v1 breaks every retained report

- `lib/opal_naming.py reporting_policy()` returns the row plus `policy_sha256` = sha256 over the canonical row (`:1979-1981`); its
  docstring: "Consumers persist policy_sha256 with their records and require exact equality".
- `reports/retention.py reserve` stores `policy_sha256` on every retention row (`:225`); `require_live` refuses a row whose stored
  `policy_sha256` differs from the current policy's: `RetentionRefused("retention binding changed")` (`:133-134`).
- So adding CUSTODY_REPORT to irpt-x10-v1's `families` changes its sha256, and every live retained record under irpt-x10-v1 (PERFORMANCE,
  ANALYSIS, EXPORT_*, ORIGINAL_*, ... at all three firms) refuses on its next read. "The 13 families byte-unchanged" (E8 criterion 2)
  holds for the families and still breaks them all. `lib/tests/test_irpt_destination.py:168,181` pins that row sha
  (`ACTIVE_ROW_SHA e0046398...`) for the same reason.

## 2. The shape that works: a separate policy revision, the one already used for the Opal research PDF

- Registry (lane IRPT_COMPLETION_REGISTRY, this seat): a NEW row, e.g. `policy_id irpt-custody-reporting`, `policy_revision
  irpt-custody-x10-v1`, one family `CUSTODY_REPORT`, state `PENDING_ENFORCEMENT`, `enforcement_ref null`; flipped ACTIVE with the
  40-hex enforcement commit after install -- the irpt-ycdgen-research-v1 path (0798635fec). irpt-x10-v1 stays byte-identical.
- Composition already routes blob addresses per revision (`reports/composition.py:35-48`, `additional_policy_revisions`).
- Missing, code (lane `~P2`, `reports/repository.py` + `reports/composition.py`): `ReportRepository.persist` calls
  `retention.reserve(...)` with no `policy_revision` (`repository.py:158`), so it always retains under irpt-x10-v1. It needs the same
  family->revision map `ArtifactRepository` already has (`:322`), passed by composition; reads already resolve the ref's own revision
  (`_check_retention`, `:105-107`). The custody callers (`export` read path, `ycharts/generate/custody_submission.py:77`, IRPT_CUSTDY's
  writer) pass `additional_policy_revisions=("irpt-custody-x10-v1",)`.
- Terms: the custody PRD states none. Proposed mirror: PERFORMANCE (`tier platinum`, `unreferenced_days null`, `accepted_ceiling_days
  2555`), table `custody_reports`, extension `json`; firms the three of irpt-x10-v1.
