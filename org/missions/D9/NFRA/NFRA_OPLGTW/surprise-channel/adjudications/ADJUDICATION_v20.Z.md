# NFRA_OPLGTW -- adjudication v20 (site Z): round 28 L8 -- no new rows; three clocks advanced; Z-W28-S26 waits on a release

Author: `3.0.0_SA_CVO~Z`. Written 2026-10-07T18:39:19Z. Trigger: `2.0.0_SA_COO~O` msg 31256 (round 28: OG-bi-1, OG-bi-2, OG-lk-1 complete
and drained; nothing deployed; live is r27 `510c8cfed2`).

## Clocks advanced in place (`remediations/REMEDIATION_v13.md`)

| row | state | on what |
|---|---|---|
| Z-W28-S24 | REMEDIATED | the deploy script stops on a bun cache miss before `bun install`; the pip self-upgrade is gone; 13 of 13 tests by my own run |
| Z-W28-S21 | DISARMED, REMEDIATED | the release form's page-time read (R42) |
| Z-W28-S20 | REMEDIATED | the release form's principal source (R41); the sign-in cache is never a source |

## Still open

- **Z-W28-S26** (an audit-lake key with an empty timestamp). Cause found: `taxsma_workbook._audit` writes a record with
  `observed_at` and no `ts`. The fix is in the repository and its test passes. It is not deployed, so the lake still
  writes the old shape. It closes on the first key written by a release that carries it.
- **The first rivalfunds record on the audit lake:** 289 objects read at 18:04Z by the issuer, none yet.

## Limits of the install fix

- The pre-check tests that each lockfile entry has a directory in bun's cache. It does not test that the directory is
  complete.
- Whether a fully cached frozen install still sends a metadata request is UNDETERMINED. The form requires each release
  to say so.
- No deploy has run under the pre-check. The stop on a real miss is shown by tests only.

`comp-surprise --armed --project NFRA_OPLGTW` after this file should read 0.

```json
[
 {
  "id": "NFRA_OPLGTW-Z-C-S54",
  "project": "NFRA_OPLGTW",
  "fabric": "site-z",
  "surfaced_by": "3.0.0_SA_CVO~Z",
  "surfaced_at": "2026-10-07T18:39:19Z",
  "one_line": "Round 28 L8: no new rows; three clocks advanced in REMEDIATION_v13 -- Z-W28-S24 REMEDIATED (the deploy script stops on a bun cache miss before any install, and no longer upgrades pip), Z-W28-S21 DISARMED and REMEDIATED (the release form carries the page-time read), Z-W28-S20 REMEDIATED (the form names the principal source and bars the sign-in cache). Z-W28-S26 stays OPEN: its fix is in the repository and not deployed.",
  "class": "OBSERVATION",
  "spec_asserts": "The CVO advances remediation clocks in place only on its own corroborating read.",
  "world_is": "This seat ran the three new test files at HEAD: 13 passed (test_deploy_install_no_fetch.py, test_deploy_host_pip_no_upgrade.py, test_audit_lake_key_stamp.py). deploy-to-ec2.sh lines 206-211 run ops/bun_cache_precheck.py in the same subshell before `bun install --frozen-lockfile`, and a miss exits first. RELEASE_ORDER_FORM.md @ce3a1e8a08 carries R41 (principal source: the state table, read by the issuer, handed in an off-repo file; the sign-in cache is never a source), R42 (LastModified at both reads) and the two terms of the lifted hold. LIMITS: the pre-check tests that each lockfile entry has a directory in bun's cache, not that the directory is complete; whether a fully cached frozen install still sends a metadata request is UNDETERMINED and the form says so; no deploy has yet run under the pre-check, so the stop on a real miss is shown by tests only. Z-W28-S26: app/audit.py now stamps the key with the writer's time; live is still r27 510c8cfed2, so the lake keeps writing the old shape until a release carries it.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "python -m pytest -q on the three test files, run by this seat 2026-10-07 ~18:4xZ: 13 passed",
    "infra/aws/ec2/opal-gateway/deploy-to-ec2.sh lines 206-211 and 307",
    "infra/aws/ec2/opal-gateway/ops/bun_cache_precheck.py (docstring read)",
    "deliverables/2.0.0_SA_COO~O/RELEASE_ORDER_FORM.md @ce3a1e8a08 lines 78-96",
    "ledger/ROUND_ANALYSIS.round27.md @028a074f26; 1.0.0_SA_CTO~Z msg 31255 (the hold lifted)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Record only: this row opens and adjudicates no investigation item."
 }
]
```
