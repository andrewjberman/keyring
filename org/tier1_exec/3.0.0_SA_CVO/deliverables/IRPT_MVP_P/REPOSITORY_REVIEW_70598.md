# Independent repository primitive review

Reviewer: `3.0.0_SA_CVO~P`; 2026-09-22.
Authority: `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`.
Candidate LOCAL `70598ece96498d639b0fb12104ffe9fd4b0d5718`.
Interface document `aacb609834`; preparation `78eb29ea4c`.

## Result and evidence

The supplied actual-module suite independently passed **19/19**. Five additional
reviewer cases yielded **4 PASS, 1 FAIL**. The bounded report identity-binding
check fails; this is not full S4 acceptance or a product E2E verdict.

Reproduce from workspace root:

```powershell
python org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_P/repository_candidate_probe.py
```

Exit 1 records the failed negative control. The runner extracts exact Git bytes
of the module, implementer tests and AnalysisReport schema into a separate temporary
snapshot, executes the actual repository and AWS adapters with synthetic table/S3
and authorization callbacks, and retains raw output in
`repository_candidate_probe.json`. It does not import a moving worktree module.
Timestamp: 2026-09-22T21:27:23.038367Z. Module SHA256:
`700793a783e707e85e66790624432e0c99683ee3e4546d095469df3fceae760c`.

| Bounded check | Grade | Evidence |
|---|---|---|
| Supplied immutable/retry/revocation/version/corruption controls | PASS | Actual supplied suite, 19/19; raw unittest output retained |
| Exact selected set survives unrelated permission revocation but refuses selected revocation | PASS | `exact_subset_revocation` |
| Reordered selected account IDs retain identity and one blob | PASS | `selected_order_idempotency` |
| Report ID binds to immutable record identity after index corruption | FAIL | `report_index_alias_integrity`, R-P05 below |
| Equivalent artifact index alias is refused | PASS | `artifact_alias_negative_control` |
| Revocation during prepublication verification prevents index publication | PASS | `revocation_before_publication` |

## R-P05 — P2 report reference is not rebound to hashed record identity

At this pin, `ReportRepository.persist` derives report_id from owner, kind and
request_id. `ReportRepository.get` verifies the byte hash, owner and index receipt
against the caller's reference, but never recomputes report_id from the accepted
record. A misbound index row can therefore authenticate a different report ID
against the original report's bytes and request identity.

Reproduction publishes a valid AnalysisReport, copies its synthetic index row to
`REPORT#RPT-ffffffffffffffffffffffffffffffff#<original revision>`, and rewrites only
the receipt's report_id to match. The blob, hash, request identity and owner remain
unchanged. Get returns that report under the alias instead of refusing. The
original ID is `RPT-0e8f4e4f51d27537aa42aa83b559ec67`. The equivalent mutation in
ArtifactRepository is refused because get recomputes its identity binding.

Requested correction: bind the requested report ID to the validated immutable
record's canonical owner/kind/request_id, with paired valid retrieval and misbound
index rejection controls. Review the same receipt-binding behavior for history
and retry rather than relying only on a comparison between two index fields.

This is a storage/index corruption or composition-misbinding condition. The probe
does **not** establish an unprivileged index-write path, cross-tenant disclosure,
or a live exploit. Current permission checks passed their supplied and added
controls. No implementation changes were made by this reviewer.

## Acceptance limits and next evidence

Full P1-P8 and S1-S7 remain NOT_EVALUATED on this partial candidate. S4 has a
bounded failing identity-integrity subcheck; do not mark the entire criterion
complete from 19 passing primitive tests. Baseline findings B-P01 through B-P04
are not retested or closed by this storage-only pin.

M's production principal/authorization/naming composition, registered destinations,
actual entry/build/IAM, Y lifecycle and released report lineage, browser reload,
frozen export, protected downloads and deployed paths remain untested. Supplied
gate 2/2 is implementer-reported, not independently rerun here. No live cloud or
vendor writes, deploy, push or promotion occurred.

CTO's exact 21:23:24Z inbox handoff reports final portal DEV baseline
`8e6e2e38cc299c4415d42b0fe627edc50ec35e1b` and releases F code write claims.
This supersedes the earlier pending-F receipt, not historical per-pin test limits.
Existing render code must be inherited. The 23 remaining bare-prefix fixture
defects are assigned to implementer P; matching reviewers independently verify
consumer cases at a future completed pin. No frontend ancestry or final-head suite
was measured in this storage-only review. F administrative merges, old canonical
hold and B L9/render provisioning prerequisite remain separate.

## Compiler tools and custody

Bare comp-which ran before inspection; broad inbox/review questions returned weak
or tied routes. comp-read exposed exact inbox/source shapes; full selected files
were read. comp-diff help was inspected; no current-HEAD blast-radius result is
claimed for the isolated candidate. Git show supplied exact pinned source bytes.
Review deliverables are LOCAL; commit receipt is communicated separately.
