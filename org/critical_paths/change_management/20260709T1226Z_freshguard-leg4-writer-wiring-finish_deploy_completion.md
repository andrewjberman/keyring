# Deploy Completion Record
**Date opened:** 2026-07-09T12:26:09.108694+00:00
**Status:** HELD-SOVEREIGN-GATED -- gate: external / GATE RESTATED 2026-07-09T23:20Z (0.7.0 finding 231918Z; source + applied + exercised). >>> DO NOT CLOSE L4 ON THE ~02:11Z READ. IT PASSES ON A TRANSIENT AND IS FALSE AN HOUR LATER. <<< MECHANISM: _provenance.stamp_marker rebuilds the marker WHOLESALE from its CALLERS table_names and discards existing.table_metadata (:203-212, :226-235). derive_runner + cse_store stamp 4 tables; incremental_updater stamps 3 (lambda_function.py:575-579) -- so EVERY incremental stamp DELETES cse. The reader (:255) iterates only the table names PRESENT in the marker, so an ABSENT table prints NOTHING AT ALL. The never-a-silent-fresh guarantee covers a present-key-with-null-value, NOT a missing key. APPLIED (live marker 16:13:18Z): writer_id=incremental_updater, 3 tables, no cse; bucket versioning is OFF so the derives 4-table marker is destructively gone. EXERCISED: the real reader against the live marker -> 3 lines out, cse mentioned False. CloudWatch shows incremental_updater firing every hour tonight. NEW GATE = the ARCH FIX (merge-not-replace in stamp_marker + reader NAMES absent tables). CTO arch-gated; unwritten. NOT CLAIMED: that cse is stale right now -- the mtime oracle at _provenance.py:141-145 is FORMALLY RETIRED and Nessie is VPC-internal/unreachable, so the true snapshot cannot be resolved. INFERRED, non-actionable, not asserted. Closing on the 02:11Z read is LD-0267(C): aiming an instrument at the wrong moment. (held since 2026-07-09T13:11:12.866381+00:00)
**Deploy:** FRESHGUARD leg-4 finish: wire all 3 writers (derive_runner/incremental_updater/cse_store) to the centralized _provenance.stamp_marker so per-table last_write_iso lands live. GROUNDED: leg-4 is SOURCE-INCOMPLETE (unwired), not merely undeployed -- the centralized stamp has ZERO call sites; all 3 writers stamp their own local marker with no last_write_iso field. HELD on CTO approach-gate (A centralize-import vs B 3-copy).
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD: wire 3 writers -> _provenance.stamp_marker + Dockerfile COPY _provenance.py + Lambda zip vendors _provenance.py | hash pushed | committed 86ab291f8 (6 files, +61/-133), pushed origin/CLOUD edc6790c4..86ab291f8. All 3 writers delegate to _provenance.stamp_marker; Dockerfile COPY _provenance.py; zip vendors _provenance.py (sha256 9dC0bal9...); source map updated. commit-gate clean; grep-proven zero residual local marker-write (only _provenance.py:227). | CLOSED 20260709T125750Z |
| L2 | activation | derive image CodeBuild rebuild+push (derive_runner+cse_store call shared stamp; image carries _provenance.py) | CodeBuild build-id + image digest | CodeBuild globgrph-derive-build:fb7b48b9 SUCCEEDED/COMPLETED. APPLIED-truth: ECR opal-globgrph-derive-runner:latest pushed 2026-07-09T13:06Z, tag 20260709-130548, digest sha256:2b7f5ec0bfdb329d25cef5adeaad9ba1abc23904ada56aefd68d87a4990e821a. Image carries _provenance.py + derive_runner/cse_store delegation (P3-FREE: motif reverted to fad55a83c^, signature-free per CTO sequencing). Task-def globgrph-derive-runner references :latest -> nightly auto-picks up (no revision needed). | CLOSED 20260709T130943Z |
| L3 | activation | incremental_updater Lambda: rebuild zip(+_provenance.py) + safe-apply TF (source_code_hash tracks) | get-function CodeSha256 + 0-diff plan | safe-apply complete 0-add/1-change/0-destroy (HALT-gate clean). APPLIED-truth (Rule22a): get-function-configuration opal-globgrph-incremental-updater CodeSha256=9dC0bal9JcpQ9D0CuBaeXOT1E9LY80btOGR6lsHmzTA= (== rebuilt zip w/ _provenance.py vendored), State=Active, LastUpdateStatus=Successful, LastModified 2026-07-09T13:07:33Z; targeted 0-diff plan = No changes. Lambda now delegates to _provenance.stamp_marker. | CLOSED 20260709T130834Z |
| L4 | verify | live marker last_write_iso POPULATED all 3 tables, EXERCISED (real incremental write + nightly derive), APPLIED-truth Rule22a | marker read per-table non-null + writer_id |  | OPEN |

## Log

- 20260709T122609Z OPENED by 0.7.0_AE_CloudOps with 4 leg(s)
- 20260709T125750Z LEG L1 closed: committed 86ab291f8 (6 files, +61/-133), pushed origin/CLOUD edc6790c4..86ab291f8. All 3 writers delegate to _provenance
- 20260709T130834Z LEG L3 closed: safe-apply complete 0-add/1-change/0-destroy (HALT-gate clean). APPLIED-truth (Rule22a): get-function-configuration opal
- 20260709T130943Z LEG L2 closed: CodeBuild globgrph-derive-build:fb7b48b9 SUCCEEDED/COMPLETED. APPLIED-truth: ECR opal-globgrph-derive-runner:latest push
- 20260709T131112Z HELD-SOVEREIGN-GATED gate=external/next nightly derive_runner ECS run ~02:10Z (last_write_iso all 4 tables) + next 
- 20260709T232036Z HELD-SOVEREIGN-GATED gate=external/GATE RESTATED 2026-07-09T23:20Z (0.7.0 finding 231918Z, source+applied+exercised
- 20260709T232058Z HELD-SOVEREIGN-GATED gate=external/GATE RESTATED 2026-07-09T23:20Z (0.7.0 finding 231918Z; source + applied + exerc
