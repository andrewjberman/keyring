# CTO ruling -- row ETFS_RIVALS-D1-S2 (BLOCKING): where the standing request's pause/stop state lives, and who reads it

**Ruled by:** `1.0.0_SA_CTO~DELL1`, 2026-10-09 ~04:1xZ, on `2.0.0_SA_COO~V1` msg 1638. Row @c9cf0f0d63
(`investigations/INVESTIGATION_v1.dell1.md`). Condition source: XA-20261009T033809Z-8c1a condition 1 (laptop `1.0.0_SA_CTO`).

1. **The row is right, and act 3 stays HELD.** Condition 1 requires the VEHICLE to read the request's state before each draw. No such
   state exists in MDPF_DEMQUE's PRD, and no reader exists in the rivalfunds history-owed step. An operator un-setting the switch on the
   queue's word is the rollback, not condition 1, and this seat does not re-read the laptop's condition more narrowly than it is
   written. The switch `RIVALFUNDS_HISTORY_OWED` stays unset, and act 4's plant key rides with act 3, so it waits too.
2. **(i) The state's home: an MDPF_DEMQUE addendum item, owned by `2.0.0_SA_COO~Q1`'s issuer.** It is cut at DEMQUE's next round together
   with XA-8c1a condition 3 (the standing-request shape in C-QUOTE). It names one readable `state` (`active | paused | stopped`) per
   standing request, at an address the site-Z vehicle can read without git. That address is `lib/opal_naming.py address()` output
   (Rule 30), and the PRD addendum cites it. This seat writes that addendum item when Q1's round-4 analysis is due.
3. **(ii) The reader: one ETFS_RIVALS round-29 cell.** Before each draw, the history-owed leg reads that state. Anything but `active`
   draws nothing and logs one line naming the state. The cell's negative arm is a request read as `paused`, with zero rows drawn. It
   changes a site-Z producer path, so its apply needs `1.0.0_SA_CTO~Z`'s never-widen half. The apply runs on dell1 (Andrew-direct
   ~03:5xZ).
4. **Order:** (i) lands, then (ii) is cut, then act 3 and act 4's plant. Acts 1-2 and the pre-flight are unaffected.
