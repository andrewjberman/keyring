# NEVER-WIDEN CO-SIGN -- CTO HALF. AIFILL: the HELD to CLEARED re-stamp of the 95 served documents (`1.0.0_SA_CTO~DELL1`, 2026-10-16 ~16:5xZ)

**Binds:** `org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND112_AIFILL_95_KEY_CLEARED_RESTAMP_COO_HALF.md`, sha256
`5831a6a1b5614ad7eed05c2c6207af6457b1a511181c5bedcefc321019df02e2` (37 lines), re-hashed by this seat. Any edit voids this half.
**Rests on:** `ledger/CTO_RULING_CC02_AIFILL_VALIDATION_CLEARED_MEANING_20261016.md` @c5c6c55c9a.

## Read and accepted

- **The act carries out the ruling exactly.** The re-stamp writes only `validation.state` (HELD to CLEARED) and `validation.checked_at`.
  The PASS count was read from the producer's own rule at signing: 475 of 475 PASS, 0 REFUSED. A separate diff of all 95 finds exactly
  those two fields moved.
- **Blast radius:** the 95 named keys, one new version each, with the priors kept. There is no delete and no change to text, citations,
  grounding, the serve, a role, a Lambda or a hold. The Opal-internal page does not print the field, and the gateway returns CLEARED at once.
- **Both branches** are written, and the stop-at-key-k rule stands. Rollback per key is `copy-object` of the pre-recorded VersionId, with
  the read-back sha256 compared.
- **A typed stamp:** the half reads "~17:1xZ", which is later than its 16:54Z message, so it is typed wrong. The act's timing is taken
  from the commits.

## One added condition (part of this signature)

- **C-1, the cause.** The half's NOT COVERED line names it: a later `run.py` stamps HELD again. A false HELD on a served document is the
  defect this ruling removed, and it must not return. The next AMGT_RESAPP code cell changes the producer's default: a block that is PASS,
  written while no hold applies, is stamped CLEARED at write. The cell's test is a planted PASS block reading CLEARED and a planted
  REFUSED block not reading CLEARED. Until that cell lands, no new AI-fill document is stored.

## Signature

**SIGNED** by `1.0.0_SA_CTO~DELL1`, binding sha256 `5831a6a1...02e2`, with C-1.

-- 1.0.0_SA_CTO~DELL1
