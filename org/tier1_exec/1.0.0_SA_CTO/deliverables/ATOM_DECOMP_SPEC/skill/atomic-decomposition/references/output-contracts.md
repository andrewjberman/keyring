# Output and Gate Contracts

## Required package

1. Decomposition charter and scope denominator.
2. Current-state system map derived from ledgers.
3. Script/function I/O catalogue with line locators.
4. Artifact and field lineage.
5. Deployed resource and recursive control graph.
6. Configured-versus-observed schedule/runtime reconciliation.
7. Consumer contract and compatibility boundary.
8. Contradiction, decision, and residual-unknown registers.
9. Target architecture and responsibility model.
10. Atomic migration wave plan with parity, cutover, rollback, and ownership.
11. Cleanup/replacement plan with drain and verified-absence tests.
12. Validation matrix and final assurance statement.

## Gate assertions

- G0 passes when identity, authority, mode, scope, environments, denominator, boundaries, and invariants are explicit.
- G1 passes when required inventories are populated and the dependency frontier has no unclassified item.
- G2 passes when evidence freshness is stated and decision-relevant contradictions are resolved or block progress.
- G3 passes when target ownership and preserved/changed consumer contracts are exact.
- G4 passes when every wave is atomic, sequenced, owned, testable, reversible, and replacement-aware.
- G5 passes after shadow and identity-level parity, operational controls, and serving-path proof.
- G6 passes after cutover stability, drain completion, replacement ledger closure, and approved removal probes.
- G7 passes after validation, predecessor absence, documentation/config cleanup, and residual-risk acceptance.

PASS requires linked evidence. WAIVED requires a named decision and approver. OPEN and BLOCKED are honest outcomes; they are not completion.

## Atomic work-package schema

Each package declares:

- one objective and one bounded ownership surface;
- prerequisite package IDs and external dependencies;
- exact reads, writes, resources, and contracts touched;
- implementation and test outputs;
- acceptance method and expected result;
- rollback action and rollback window;
- predecessor/successor relationship;
- owner, reviewer, and evidence IDs.

Split a package when it spans independently reversible cutovers, multiple unpinned contracts, or hidden owners. Do not split tightly coupled code and contract validation merely to make work appear smaller.

## Quality rules

- Every narrative claim links to a ledger claim.
- Every diagram can be regenerated from stable node/edge identities.
- Every exclusion has rationale and owner.
- Every volatile fact has a measurement time.
- Every cleanup action names what replaces it.
- Every unknown has impact and next probe.
- Completion language is forbidden while a required gate remains open.
