# Self-drive dell2-box, ticks 195-196 (1.0.0_SA_CTO~DELL2)

Arming record: org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261015_020xZ_SELF_DRIVE_DELL2_BOX_KEEP_DRIVING_ON.md
Window: 00:26Z to 01:27Z 2026-10-21.

## Acts and rulings
- **Watcher fix 9fe08639a3** landed on box/dell2 (MSTR msg 11666; census of 42 bases: only CloudOps affected).
- **r34p: SIGNED** @d421313363 (blob b945271a46). LIVE at 00:49Z (IB2 msg 11689): V2S OK; cure hashes equal r34n's.
- **Audit managed-policy pair: RE-SIGNED** @d421313363 (blob 9f065fb2a5). New row irpt-anlreq-audit-x10-v1; ARNs unchanged.
- **Retention census** (IB2 msg 11673): 0 rows on a moved hash.
- **Y2 msg 11691:** tickets_table becomes an optional binding, not a unit env. r34q bundles the binding and the ACTIVE audit row.
- **Y2 msg 11710 (A):** the builder carries opal-tickets, pinned by a test against ticket-center/main.tf.
- **TV2 msg 11694:** DL1 stopped at 0 of 46 (cottonwood DenyForeignFirmPrincipals). RULED split:
  - irpt 42 under a re-cut pair, RE-SIGNED @773a895c2c (blob ff354d5036);
  - cottonwood 4 recorded as residue, act row 3ffe for Andrew;
  - the Deny is never edited.
- **TV2 msg 11704:** told 7f was in flight. V2 held DL1 (AMENDMENT 7), then released it on IB2's 7f report (AMENDMENT 8, msg 11722). Release accepted.
- **Run 7f RUN-DONE PASS** (IB2 msg 11724):
  - Andrew's Overview saved at C:/dev/andrew_samples/Opal_Overview_sample_post_r34p.pdf: 262121 bytes, sha256 74d8b3e803c2, 42 pages.
  - Read here: %PDF-1.4, 42 page objects, ends with %%EOF.
  - Packager outcome ATTACHED.
  - DLQ 2 -> 3 routed to Y2.
- **Andrew told** the sample is ready.

## Next
- DL1, 42 irpt objects (TV2).
- G2 Multi-Comp filing (FWD-10).
- AUDITPOLICY after DL1's terminal report.
- Row flip, then r34q.

## Acts only Andrew can do (cited)
- 65a1, 544d, a392: recursive deletion / destructive git (CLAUDE.md Agent Autonomy).
- a331: internal all-firm entitlement for an outside-domain user (entitlement beyond his grants).
- 3ffe: admin-user delete of 4 synthetic cottonwood objects. The bucket Deny blocks every agent principal and is never edited (CLAUDE.md: no weakening of security gates).
- FWD-13..15 DONE WHEN confirmation (Andrew confirms DONE WHEN at L2).

Completion test: NOT DONE.
state: ARMED

## Compiler Tools
open-calls.py list/add; inbox read/; git diff -w; PDF header/page read; safe-commit.sh.
