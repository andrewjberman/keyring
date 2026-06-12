# CVO standing queue — GLOBGRPH in-VPC AC exercise legs (on-record per CTO 163812Z / COO 163843Z)

**archetype:** SCRIBE

Rides the next in-VPC opportunity (unit-proven sufficient interim). Named legs:

1. **Concurrent-commit serialization** — simultaneous 2b + F3 commits: serialized lineage, 0 orphans, BOTH increments served post-refresh (TO-P1 AC-a).
2. **Synthetic-orphan-inject** — detector fires ERROR, marker stamp SKIPPED, non-zero rc (TO-P1 AC-b).
3. **REACHABLE-FROM-BRANCH-HEAD (named leg, CTO condition on the snapshot-lineage acceptance):** assert the landed snapshot is reachable from the Nessie branch head — the authoritative end-to-end check the served-state observation implies; asserted explicitly, not inferred.
4. **TO-F3 live demo** — ad-hoc `--commit-to-nessie` re-derive lands as a Nessie commit + marker stamp + next canonical rebuild serves it (deferred from 2026-06-12, same in-VPC constraint).

Separate timed item (NOT in-VPC-gated): 2026-06-13 AM one-pass nightly review — 2a MARKER_STAMPED on a real advancing commit (closes the AC10(d) pin-aging caveat) · marker monotonicity/content · zero CAS/orphan ERRORs on v0.1.12 first live run · canonical auto-refresh serves nightly state · GLDINC 6-stream verdicts same sitting.

— 3.0.0_SA_CVO
