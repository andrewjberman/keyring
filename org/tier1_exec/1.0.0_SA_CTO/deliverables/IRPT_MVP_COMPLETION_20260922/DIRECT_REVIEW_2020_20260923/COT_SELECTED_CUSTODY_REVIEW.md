# Selected Cottonwood custody - CTO direct review

Pin: 7033e234909d996ed122f1c198f7af89a7c68e18. Verdict: bounded source PASS.

Exported pinned files and dependencies to an isolated scratch; no moving M edits
used. Three affected selected-account/security-tree checks passed in 1.06 seconds
(75 deselected). A valid requested account survives an unrelated unknown-value
account; original physical row ordinal is preserved; selecting the unknown account
still refuses; an account missing from both sources refuses. Two additional CTO
probes selected two accounts with one absent from holdings or independent totals:
both refused with the census mismatch, rather than silently shrinking selection.

The implementation filters only on the explicitly requested canonical account set,
then independently validates the selected custody and totals. It records excluded
row counts; this is selected-account evidence, not whole-firm coverage. Positive
security-tree projection evidence is included in the three checks.

Limits: fixture source frames and local schema/reconciliation only. No live data,
authorization, accepted publication, API, UI, history or export proved here.
Currency provenance from Andrew's COT USD attestation and canonical directory-to-
source mapping are subsequent integration work, not proved by this source pin.
M's uncommitted mapping/producer edits were left untouched. Continue directly to
the first actual ready COT account, preserving full three-firm outcome scope.
