# org/critical_paths/ — the critical-surfaces ledger (NFRA_GRAPHS §10.6)

Andrew-direct 2026-06-12 (via CVO 175050Z): the git-versioned, human-readable RECORD of everything that
happens to the critical-surface dependency chains registered in `org/modules/graph/critical-surfaces.yaml`.
Alarms (SNS/EventBridge) notify; THIS ledger records.

| Subfolder | What lands here |
|---|---|
| `change_management/` | SEV1 block-with-ack approvals (who/what/justification/commit/F6-marker-hash), baseline re-signs, scheduled-scan change findings |
| `stale_warning/` | staleness alerts scoped to critical-surface chains (F1 26h age-warn / BEHIND-by-N / UNKNOWN-VINTAGE, comp-freshness results) |

Entry naming: `{YYYYMMDD}T{HHMM}Z_{surface}_{firm}_{class}.md`, class ∈ {approval, resign, scan-finding, staleness}.

Writers are STRUCTURAL (the mechanism writes its own entry — an ack that doesn't write is not an ack):
- `SURFACE_ACK` bypass (comp-surface-check) → approval entry
- `comp-xref --save` re-sign → resign entry
- scheduled scan (§10.3(C)) + marker-keyed watcher (§10.6 L3) → scan-finding entries
- critical-chain staleness signals → stale_warning entries

Design: `docs/architecture/NFRA_GRAPHS.md` §10.6. Registry: `org/modules/graph/critical-surfaces.yaml` (v0.3+).
