# /self-drive ~O fabric -- ticks 110-111 (1.0.0_SA_CTO~O, 2026-09-28 09:48Z-10:46Z)

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_O_FABRIC.md` @56050d290d.

- **MX-s-11 COMPLETE** (COO~O @557fa728c7). The 09:15:49Z opal-data-bd code writes were attributed to the pre-push
  safe-deploy hook on the push of 19dcfa26d4 (@728a2a576e); the bytes equal HEAD, so no row was filed.
- **MX-s-10 step 2:** AE~I made two ad-hoc runs (@73ca905836). Neither reached the vendor, so there were zero vendor
  calls.
  - Run 1: the document's as-of line called `prev_trading_day()` with no date. Fixed by A3 (@9b5e3c3fd9).
  - Run 2: AccessDenied at `load_bd_cookie`. `bd-exporter-ec2-role` cannot read `blackdiamond/49f/session`, and the
    preflight had asserted it could.
  - COO~O ruled row Z-S44 in A4 (@1853736322): one `aws_iam_role_policy` statement, `GetSecretValue` on the one 49F
    secret, in the `ReadSessionForCheck` form. Terraform + safe-apply + its own NEVER-2 ledger; the plan must read
    1/0/0.
  - This seat's read: the role is bd's own (`news-pipeline/cross-firm-secret-deny.tf:71`), and the grant names only the
    49F secret, so the firm line holds. No served output moves.
- Owed by this seat next: the MX-s-10 CTO never-widen half, once a run reaches the vendor and matches the current dim.

**Inbox:** 1 message (COO~O 095547Z, attribution), closed. 0 unread at 10:46Z.

**Open calls in scope:** 0. **Cards at Andrew:**
- (1) URGENT: rotate the BD password.
- (2) The history-scrub scope.
- (3) The census as a commit gate.
- (4) The switchover sitting.

**Completion test:** NOT DONE. 0 of 4 projects are complete.

state: ARMED
