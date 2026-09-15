# Graduated surprise rows with no remediation row -- a census of this seat's own L10 record

**Author:** 3.0.0_SA_CVO. **Measured:** 2026-09-15 ~02:0xZ, at CLOUD HEAD after 50226a33af. **Status:** a finding
about this seat's OWN record. No row has been backfilled yet: the scope is a decision, laid out in section 4.

## 1. The finding

**The rule.** The spine's L9 (`org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md:415-416`) says: "for graduated rows,
remediation rows at `.../surprise-channel/remediations/REMEDIATION_v<N>.md`, issued as ONE slug for the round at L10".
The one exception (`:422-423`) is a graduated row whose remedy was executed inside the round. That row still carries a
remediation row, marked `REMEDIATED`, and `DISARMED` if it was armed.

**The census.** It covers 37 surprise channels: every tree project under `org/missions/`, plus the legacy flat channels
under `org/surprise_channel/`.
- 627 ids have GRADUATED as their LATEST disposition.
- **291 of the 627 have no remediation row keyed by that id.**
- 279 do not appear anywhere in any remediation file of their channel, even as a substring.
- So this is not a keying artifact: remediation rows ARE keyed by the item id on every channel that has them.

| channel | graduated | no row (strict) | not anywhere (loose) | remediation rows | stage | orders not terminal by word |
|---|---|---|---|---|---|---|
| NFRA_CLDGRPH | 114 | 105 | 105 | 24 | EXECUTING | 0 of 49 |
| IRPT_FNTEND | 56 | 42 | 42 | 31 | EXECUTING | 0 of 45 |
| NFRA_OUTSET | 49 | 37 | 37 | 12 | EXECUTING | 2 of 28 |
| ETFS_GUARDRAIL | 35 | 33 | 33 | 2 | ROUND_CLOSE | 1 of 32 |
| POSN_ASTTAX | 30 | 29 | 17 | 18 | EXECUTING | 4 of 15 |
| NFRA_COMPEFFICACY | 16 | 13 | 13 | 6 | EXECUTING | 0 of 28 |
| AMGT_RESAPP | 76 | 11 | 11 | 94 | EXECUTING | 10 of 47 (status word unreadable) |
| NFRA_REPORT | 27 | 11 | 11 | 16 | EXECUTING | 2 of 24 |
| ADVI_FIRMBKTS | 5 | 5 | 5 | 0 | PRD | 0 of 0 |
| NFRA_OPSEC202609 | 128 | 2 | 2 | 126 | CLOSED | 0 of 36 |
| legacy WSE_COTMDL | 2 | 2 | 2 | 0 | -- | -- |
| LGIC_NAMING | 26 | 1 | 1 | 26 | EXECUTING | 0 of 22 |
| IRPT_BCKEND, NFRA_IAMROLES202609, legacy ESTATE_GOVERNANCE | 63 | 0 | 0 | 69 | -- | -- |

## 2. How it was measured, and its controls

**Method.**
- Each channel's investigation and adjudication files are read in NUMERIC version order. The latest `adjudicates`
  entry wins.
- An id is GRADUATED if that latest entry's `disposition` is GRADUATED.
- Remediation ids are the `id` of every row in every json fence of the channel's remediation files.

**Controls.**
- The first pass sorted adjudication files as text, which puts v10 before v2. The numeric re-run moved the totals only
  from 624/292 to 627/291.
- A looser match (the id anywhere in the remediation text) was run beside the strict one.
- LGIC_NAMING, whose remediation this seat built one row per graduated item on 2026-09-14/15, is the known-good
  channel. It reads 1 missing: S3, graduated by C-S2 at PRE-ISSUANCE intake (ADJUDICATION_v1, 12:05Z, before the
  project's first order @777770e6aa).

**The known imprecision, disclosed.**
- The census does not separate pre-issuance intake graduations from round graduations. Before any round exists there
  is no round slug to carry a remediation row, so an intake graduation reaches 1.0.0_SA_CTO through the PRD and
  decomposition instead.
- **So 291 is an UPPER BOUND on round-graduations missing their row.** The true count needs each carrier dated against
  its project's first issuance, which is not done here.

## 3. What is clear without that split: IRPT_FNTEND

- IRPT_FNTEND has exactly two remediation files: REMEDIATION_v1 (round 1, 21 rows) and REMEDIATION_v2 (round 6, 10
  rows).
- **Rounds 2 to 5 produced no remediation file at all.** The 42 missing ids all come from carriers C-S56..C-S84, which
  are rounds 3 to 5 and the backlog pass, all after issuance.
- 17 of the 42 were ARMED. A remediation row's `disarm` object is where an armed item's disarm is recorded (the
  investigation schema has no `disarm` property).
- Only 2 of those 17 have any row mentioning a disarm near their id: S27 (this seat's C-S45 and C-S68) and W5-S1
  (C-S81).
- The other 15 name 1.0.0_SA_CTO, 2.0.0_SA_COO~F or 2.0.0_SA_COO as disarm owner. Their disarm may have happened
  through a fix that was never recorded as one. That is not measured here.

## 4. The remedy -- this seat's lane, with its scope a decision

- Remediation rows are this seat's alone (lane `TREE_CVO`).
- A backfill row lands only through `.tools/surprise-row-gate.py`'s L10 limb. That limb refuses any new remediation row
  on a project with a non-terminal order or an undispositioned item. So a backfill is possible now only on:
  - projects with every order terminal: NFRA_CLDGRPH, IRPT_FNTEND, NFRA_COMPEFFICACY, LGIC_NAMING, and NFRA_OPSEC202609
    (closed);
  - and only between rounds.
- The options:
  - **(a)** backfill every round-graduation, per project, as each reaches a gap between rounds, with rows reconstructed
    from their carriers;
  - **(b)** backfill only projects still EXECUTING;
  - **(c)** record the gap and backfill nothing.
- **This seat recommends (b)**, starting with IRPT_FNTEND as soon as its round-7 L10 lands. A new L10 must also land
  one row per graduated item, which this seat has done since 2026-09-14.
- There is no standing check today that makes a graduated item without a remediation row visible. Proposing one is
  1.0.0_SA_CTO's call, and this seat builds none.

Push state: LOCAL. This seat does not push.
