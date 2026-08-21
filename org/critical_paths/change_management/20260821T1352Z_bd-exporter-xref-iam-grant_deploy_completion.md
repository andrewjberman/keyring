# Deploy-completion ledger: bd-exporter xref IAM grant (bd-pipeline root)

**Status:** CLOSED 2026-08-21T13:57Z by 1.0.0_SA_CTO — all four legs green, nothing stranded
**Close evidence:** apply `1 added, 0 changed, 0 destroyed` (13:54Z); re-plan `No changes` (13:55Z);
live `get-role-policy` returns both Sids (`MonolithBd49fXrefGet`, `MonolithBd49fXrefList`);
simulate-principal-policy isolated triplet — GetObject on the xref partition **allowed**,
ListBucket with in-condition prefix context **allowed**, out-of-condition negative control
**implicitDeny** (instrument discriminates). Tag `bd-v2.55.0`. Push rides the MSTR integration
window (LD-0367 integrator-only); MSTR notified.
**Change:** `aws_iam_role_policy.bd_exporter_monolith_bd49f_xref_read` — pure-add inline policy on
`bd-exporter-ec2-role`: GetObject on `opal-data-assets/blackdiamond/49f/silver/dim_account_xref/*`
+ ListBucket (own Sid, prefix Condition). Closes the a01 WP4-4 AccessDenied surfaced by DS~B inside
the LD-0429 first-green read (custodial tail declared UNDETERMINED every run).
**Commit:** iam.tf @34e45b92c0 (audited lane override CLOUD_OPS_OR_ETL, Rule 14a; Rule 26
builder-applies at this seat).
**Plan:** 1 to add, 0 to change, 0 to destroy (13:52Z read).
**Legs:** (1) apply via safe-apply — pending; (2) 0-diff re-plan — pending; (3) live verify
`get-role-policy` + `simulate-principal-policy` (one resource per call, isolated positive control)
— pending; (4) tag — pending.
**Exercised confirmation point:** next scheduled 12:45Z chain fire — a01 prints
`BD xref date=… (tail basis)` instead of `WARN: BD xref unavailable`; tail flips
UNDETERMINED → MEASURED. Not chased today (no ad-hoc production run).
**EXERCISED CONFIRMATION ARRIVED EARLY — 2026-08-21 ~15:17Z, on the RECORDED 08-19 backfill act
(not chased; it rode a commissioned production-host act):** SSM CommandId
`6b96ab4b-eeb1-4f1a-a0cb-23c156bf368c` on the production role — a01 ran the BD xref and printed
`BD xref date=2026-08-19: 5,376 distinct schwab accounts (tail basis)` → `CUSTODIAL tail=2023`,
matching the local-principal control run exactly (DS~B, 64808). The grant is verified at every
rung: DESIRED (plan 0-diff) + APPLIED (get-role-policy, simulate triplet) + **EXERCISED on the
granted principal**. Nothing further owed on this ledger.
