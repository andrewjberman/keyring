# IRPT_DASHBD: CVO dispositions on ~F2's disarm requests (msg 10333, 10335): W1901-S2 DISARMED; S103 and S107 stay ARMED

<sweep_watermark>2026-10-17T06:22Z</sweep_watermark>

**Basis.** Dispositions by `3.0.0_SA_CVO~IRPT`, 2026-10-17T06:22Z, on msgs 10333 and 10335 from `2.0.0_SA_COO~F2`, the disarm owner. Trunk HEAD is a44d6eb2de.

**(1) W1901-S2: DISARMED.**
- **The amendment fixes the hazard; it does not only re-word the criterion.** Amendment f7d784393c widened the grant to the test file. The worker's e9f665114a replaced line 86's literal pin (`== "0.4.1"`) with two assertions: the words file's version EQUALS the contract's (`test_account_transaction_cottonwood.py:86`), and the contract is at least 0.4.1 (`:87`).
- **Why that is a fix:** the old pin broke on every contract bump. The new check is stronger in kind: it binds the words file to the contract on every version.
- **Re-run:** `pytest data/assets/scripts/gold/irpt_reporting/tests/test_account_transaction_cottonwood.py` gives 56 passed.

**(2) S103 and (3) S107: stay ARMED.**
- **The disarm line** (S107, CTO msg 8841): the contract and the per-firm producers land with their L9. That needs an L9 PASS for each firm against a contract equivalent in the graded fields.
- **49 Financial and Inflection: met.** DBF136-1-J2 and DBF136-1-J1 PASS, 20 of 20 each (v146), graded against contract 0.5.1. Contract and producers are unchanged since (empty `git diff 6b6c16b492 HEAD` on the contract and the three producer files). Schema hash ac652e2f71b18427, 19 columns.
- **Cottonwood: NOT met.**
  - **Its only PASS:** DBF131-1-J1, 20 of 20, recorded by its full id in v141 (row C-S78). v140 had used "J1/J2" and the gate could not read it.
  - **Graded against contract 0.4.0**, 18 columns.
  - **The producer changed twice since then:**
    - f25618c0b4 (0.4.1): business_date re-implemented through the shared day function. The rule's words are unchanged: the first NYSE trading day on or after the Trade Date.
    - acffc76bee (0.5.0): a 19th column, `business_date_claim`, emitted on every row.
  - **The gap:** the sample never verified that column, and the current Cottonwood producer's output has no L9. The contract is not equivalent in what a sample must now verify.
- **Owed to disarm:** one Cottonwood 20-row J sample on contract 0.5.1, by natural key, including `business_date_claim`. Owner: 2.0.0_SA_COO~F2.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S88",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-17T06:22:00Z",
  "one_line": "DISARMS IRPT_DASHBD-D2-W1901-S2: amendment f7d784393c and fix e9f665114a replace the literal version pin with words-file == contract version plus a floor of 0.4.1 (test lines 86-87), a fix, not a re-wording; the Cottonwood test file passes 56 of 56 on trunk a44d6eb2de.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": ["IRPT_DASHBD-D2-W1901-S2", "IRPT_DASHBD-D2-W1901-S3"],
  "spec_asserts": "W1901-S2 (ARMED): line 86 pins contract_version == '0.4.1', so the 0.4.2 bump turns the regression red.",
  "world_is": "test_account_transaction_cottonwood.py:86 asserts WORDS contract_version == CONTRACT contract_version; :87 asserts the contract >= (0, 4, 1). pytest: 56 passed.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "git show f7d784393c (order amendment), e9f665114a (the test edit)",
    "python -I -m pytest -q data/assets/scripts/gold/irpt_reporting/tests/test_account_transaction_cottonwood.py -> 56 passed at a44d6eb2de"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "DISARMED: the brittle literal pin is gone and the file binds the words file to the contract at every version."
 },
 {
  "id": "IRPT_DASHBD-D2-C-S89",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-17T06:22:00Z",
  "one_line": "S103 stays ARMED: 49F and Inflection have an L9 PASS on contract 0.5.1 (v146: DBF136-1-J2, DBF136-1-J1), unchanged since. Cottonwood's only L9 PASS is DBF131-1-J1 (recorded by full id in v141) on contract 0.4.0; the Cottonwood producer since gained business_date_claim (acffc76bee, 0.5.0) and a re-implemented business_date (f25618c0b4, 0.4.1), never sampled.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": ["IRPT_DASHBD-D2-S103"],
  "spec_asserts": "S103's disarm line (CTO msg 8841, row S107): the transaction contract and the per-firm producers land with their L9.",
  "world_is": "Contract 0.5.1 at HEAD (schema_hash ac652e2f71b18427, 19 columns), no change since 6b6c16b492. L9 PASS per firm: 49F DBF136-1-J2 (0.5.1), Inflection DBF136-1-J1 (0.5.1), Cottonwood DBF131-1-J1 (0.4.0, 18 columns, v141). Cottonwood producer commits after the sample: f25618c0b4, acffc76bee.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/adjudications/ADJUDICATION_v141.md (DBF131-1-J1 PASS, Cottonwood, full id); ADJUDICATION_v140.md title 'contract 0.4.0'",
    "org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/adjudications/ADJUDICATION_v146.md (DBF136-1-J1, DBF136-1-J2 PASS, contract 0.5.1)",
    "git log -- data/assets/scripts/gold/irpt_reporting/account_transaction_cottonwood.py: f25618c0b4, acffc76bee after 99b3dfc5e1 (round 131)",
    "git diff --stat 6b6c16b492 HEAD on the contract and the three producers: empty"
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Stays ARMED (owner 2.0.0_SA_COO~F2). Disarms on one Cottonwood 20-row J sample graded PASS on contract 0.5.1, natural key, unique-key rows, business_date_claim included."
 },
 {
  "id": "IRPT_DASHBD-D2-C-S90",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-17T06:22:00Z",
  "one_line": "S107 (S103's disarm line) stays ARMED with S103: its condition, an L9 for each firm's landed producer, holds for 49F and Inflection on 0.5.1 and fails for Cottonwood (last L9 on 0.4.0, before business_date_claim).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": ["IRPT_DASHBD-D2-S107"],
  "spec_asserts": "S107 DISARMS WHEN: IRPT_DASHBD_ACCOUNT_TRANSACTION_CONTRACT.json and the per-firm producer are committed and the CVO has graded the cell that landed them (L9).",
  "world_is": "As C-S89: two of three firms graded on the current contract; Cottonwood's current producer output has no L9.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "row IRPT_DASHBD-D2-C-S89 in this file"
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Disarms with S103, on the same Cottonwood sample."
 }
]
```
