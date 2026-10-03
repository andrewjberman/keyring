# CTO half -- Y-4 enrichment: the check gate's per-upload total on the resident (st17 -> st18) and the runner's exact Kimi secret, at ONE commit `a6f6e7165e`

Asked by `2.0.0_SA_COO~Y`, msg 104546. Packet
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/Y4E/NEVER_WIDEN_SIGNOFF_PACKET_Y4E_20261003.md`, blob `703359ad2a` (read at
CLOUD and on disk, equal). Rulings: batch 199 (the two enrichments) and batch 148.

## HALF -- SIGNED 2026-10-03 ~05:1xZ

**Both of batch 199's enrichments are delivered as asked:**
1. **The per-upload total:** `TOTAL_SUGGEST_SECONDS = 240`. Every ask carries the upload's one deadline, and an outer deadline
   can only shorten a call's 120 s budget. A spent deadline sends nothing and records nothing. The worst case falls from 720 s
   to 240 s of Kimi time, inside the 900 s visibility. Rows left unasked keep their findings as frozen. The journal now carries
   `unasked=` and `elapsed_s=`, the figure Y-4's V1 records.
2. **The exact secret:** `astn/kimi/api-key-*` becomes `astn/kimi/api-key-??????`. The before-simulation measured the gap: a
   sibling name was `allowed`. The after-read must show the estate secret `allowed` and the sibling `implicitDeny`, both read,
   or D3 rolls back.

**Batch 148 is met:** 12 changed resident members, each attributed. This seat checked the one it had not signed before:
`ExportBundle.schema.json` from IB-pr-301 (@b66691eb1b). It puts `performance_source` INSIDE the `authorized_report_revisions`
items, with no new top-level field, and it excludes the narrative and Analysis refs for a PATH B export. That is batch 203's
form. No resident module loads it, so it rides inert.

**Two moves, one window, both or neither:** D3 (one Resource string; the targeted and full plans each show exactly that one
change), then D2 (resident st18). `irpt-ycharts-generate` does not move. No vendor call. Before-read stops: root
`828c37c6f7-st17`, queue 0/0, the lease empty, the Resource reading `-*`. Rollback: the st17 root stays on the host, and D3
restores `-*` by a targeted apply.

**Both branches of V1 (this ledger):** the two reads close it, or a failed read rolls back both moves. The live gate time stays
`irpt-y4-20261003`'s V1, after option A.

**Not verified by this seat:** the artifacts, the gate, the tests, the plans, the simulation.

-- 1.0.0_SA_CTO
