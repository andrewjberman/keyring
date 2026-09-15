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

## 5. DECISION AND PROGRESS

**The decision, taken in this seat's own lane.**
- This seat took decision (b) itself, in lane `TREE_CVO`, on Andrew's `/open-calls` at ~02:5xZ 2026-09-15.
  Remediation rows are this seat's alone, so the scope of their backfill is not a sovereign call and is not listed as
  one.
- (b) means: backfill the projects still EXECUTING, one at a time, as `.tools/surprise-row-gate.py`'s L10 limb admits
  each one.
- Pre-issuance intake graduations are EXCLUDED.
- Closed projects are recorded only.

**IRPT_FNTEND is done: `remediations/REMEDIATION_v4.md` @18c2d2a8aa.**
- 42 rows, equal to the recomputed set. 0 jsonschema violations.
- Round split: v4 24, v5 18.
  - v4 is C-S56..C-S58 at the round-4 L9, plus C-S65..C-S72 in the round-4 backlog pass.
  - v5 is C-S81..C-S84.
- 0 pre-issuance exclusions: every carrier post-dates the first order @3ceb5201cb.
- 4 rows are REMEDIATED, each citing the later row that records the remedy as executed: S27 (C-S79), and S53, W4-S7
  and S56 (C-S85).
- 17 rows are ARMED:
  - 6 read DISARMED, each citing the row that records the disarm: S27 (C-S79), S42 (S57, the owner's disarm, with
    C-S85; C-S76 records this seat's disagreement), S53, W4-S7 and S56 (C-S85), and W2-S24 (S59, disarm by detection).
  - 11 read ARMED with `at` null, because no row records their disarm: S55, S61, W1-S39, W1-S46, W1-S51, W1-S52,
    W1-S56, W1-S57, W2-S11, W2-S21 and W5-S1.
- 14 rows are FLAGGED, written `per carrier <id>:` with the carrier's own text, because the carrier states no remedy in
  so many words.
- The gate admitted all 42: "45 task order(s) at HEAD on both roots, 0 open; 227 investigation item(s) ... 0
  undispositioned".

**Excluded.**
- LGIC_NAMING-S3: pre-issuance intake, graduated by C-S2 before the project's first order @777770e6aa.
- ADVI_FIRMBKTS, 5 ids: the project has no task order, so all 5 are intake graduations.
- NFRA_OPSEC202609, 2 ids: the project is CLOSED, so they are recorded here and not backfilled.

**Next candidates at this HEAD: none can be admitted now.**
- A project becomes a candidate at its next gap between rounds, once every order reads terminal and every item carries
  a disposition.
- Counts below are open orders by status word, then undispositioned items:
  - NFRA_CLDGRPH: 0 / 49
  - NFRA_COMPEFFICACY: 0 / 12
  - NFRA_OUTSET: 2 / 26
  - POSN_ASTTAX: 4 / 8
  - AMGT_RESAPP: 10 (status word unreadable) / 3
  - NFRA_REPORT: 2 / 6
  - ETFS_GUARDRAIL (ROUND_CLOSE): 1 / 46
- The undispositioned count reads carriers from both the investigation and adjudication files. A channel that uses
  another carrier convention may read higher than the gate does, and the gate's own run decides. Since @fa6521ea12 an
  order with a VALID bound proof also counts as terminal.

**Where the count stands.**
- Of the census's 291 (strict), IRPT_FNTEND's 42 are now carried, leaving 249.
- Of those, 8 are excluded or recorded only: LGIC_NAMING-S3, ADVI_FIRMBKTS's 5 and NFRA_OPSEC202609's 2.
- That leaves at most 241 round graduations still to backfill, as their projects reach a gap between rounds.

**Incident, this seat's.**
- The backfill commit @18c2d2a8aa ran in the background. Its post-commit hooks held the shared `.git/index.lock` from
  03:22:47Z until some time between 03:32Z and 03:33:55Z, about 10 minutes.
- For that time it blocked 1.0.0_SA_CTO~A's commit, which that seat reported at 03:32:13Z. This seat answered at
  03:43Z, and PID 32684 was gone by 03:42:17Z.
- A commit that holds the shared index runs in the foreground from now on.

**A de-duplication, disclosed.** This section was first committed in two copies. The parent's copy was appended on
disk while the fork was writing its own, and the fork's commit f2b9067e9f carried both. The parent's copy is removed
here, and its one unique item, the incident above, is kept. The fork's undispositioned counts supersede the parent's,
because they read carriers from BOTH the investigation and adjudication files.

Push state: LOCAL. This seat does not push.
