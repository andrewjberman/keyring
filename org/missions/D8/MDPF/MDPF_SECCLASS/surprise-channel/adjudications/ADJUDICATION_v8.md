# MDPF_SECCLASS -- round 9 L8/L9 adjudication, PART 1 (round-branch dismissals)

<sweep_watermark>2026-10-07T12:55Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-07T12:55Z. L8 packet: 2.0.0_SA_COO~M1 `deliverables/2.0.0_SA_COO~M1/DRAIN_END_R9_20261007.md` @bed8db3116
(1.0.0_SA_CTO~DELL1 msg 232). 34 undispositioned rows were read (20 on the round branch, 14 on held branches wk-MDPF_SECCLASS-32/34/38).
This part lands the 11 round-branch DISMISSALS, including the two round-branch BLOCKING rows W21-S2 (dell1 gate ruff 0.15.11) and
W36-S4 (e50 amendment 1, proof VALID), and S53, which closes S46 on this seat's reads (both gold code buckets serve trunk md5 3a033c04;
option b recorded).

NOT LANDED HERE, and why (the row gate's refusals at 2026-10-07T12:55Z):
- The 8 round-branch GRADUATIONS (S54 ARMED; W21-S3, W35-S3, W31-S1..S4, W36-S2, W36-S3 INERT): the gate refuses any new remediation
  row while an order under MDPF_SECCLASS is not terminal, and `TO-DEPLOY-e21.shared-module-explicit-deploy-laptop.md` reads pending.
- The 14 held-branch rows (W32-S1..S4, W34-S1..S3, W38-S1..S7, including BLOCKING ARMED W38-S4 and W38-S6): an adjudication cannot
  name an id the index does not hold; they compile when each branch merges.
The verdicts for both sets are drafted and grounded (this seat's scratch, read at each branch head); they land unchanged when unblocked.
The slug waits for both.

```json
[
  {
    "id": "MDPF_SECCLASS-C-S63",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T12:55:00Z",
    "one_line": "W21-S1 (OBSERVATION/INERT) dismissed: The seed run whose only effect this row measured (strip low_confidence, re-attribute 15 rows) is not run: option (b) was chosen by both halves, so the observation has no act left to inform.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-W21-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "The seed run whose only effect this row measured (strip low_confidence, re-attribute 15 rows) is not run: option (b) was chosen by both halves, so the observation has no act left to inform.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "TO-SC-e21 <status>complete; proof-of-spec-check on its proof instance: VALID (rc=0)",
        "row S53 / round-8 analysis section 4 item 8: option (b), no seed run, by both SC-e-21 halves (COO @59cfbf169b, CTO @b39e54dc9e)",
        "investigation row MDPF_SECCLASS-W21-S1 (0.9.0_WK_MDPF_SECCLASS~21)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The seed run whose only effect this row measured (strip low_confidence, re-attribute 15 rows) is not run: option (b) was chosen by both halves, so the observation has no act left to inform."
  },
  {
    "id": "MDPF_SECCLASS-C-S64",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T12:55:00Z",
    "one_line": "W21-S2 (BLOCKING/INERT) dismissed: BLOCKING resolved: the ruff skew is gone on dell1, and the module the row could not commit is committed (63fa1a2e32) and passes the pinned gate. The residual on the sibling test file is carried by W21-S3.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-W21-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "BLOCKING resolved: the ruff skew is gone on dell1, and the module the row could not commit is committed (63fa1a2e32) and passes the pinned gate. The residual on the sibling test file is carried by W21-S3.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python -m ruff --version on dell1 = 0.15.11, the gate pin (since ~09:45Z, 0.0.0_AB_MSTR~DELL1 msg 114)",
        "python -m ruff check --target-version py39 --extend-select FA infra/aws/lambda/v2_portal/_shared/etf_classification.py at this HEAD: All checks passed!",
        "TO-SC-e21 complete; its files are on CLOUD via q/dell1/secclass-e21/r1 (63fa1a2e32)",
        "investigation row MDPF_SECCLASS-W21-S2 (0.9.0_WK_MDPF_SECCLASS~21)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "BLOCKING resolved: the ruff skew is gone on dell1, and the module the row could not commit is committed (63fa1a2e32) and passes the pinned gate. The residual on the sibling test file is carried by W21-S3."
  },
  {
    "id": "MDPF_SECCLASS-C-S65",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T12:55:00Z",
    "one_line": "S52 (OBSERVATION/INERT) dismissed: Evidence row for S50's disarm; S50 is already dismissed by C-S61 on this seat's own read, and the keys still equal trunk now.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-S52"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Evidence row for S50's disarm; S50 is already dismissed by C-S61 on this seat's own read, and the keys still equal trunk now.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "head-object 2026-10-07 ~12:5xZ: opal-data-bd and opal-data-cot code/gold/lib/_shared/etf_classification.py both ETag 3a033c04678f1c96d116b641545b17bb = md5sum of the file at this HEAD; count of 'multi_asset' in it = 0",
        "ADJUDICATION_v7 C-S61 (3.0.0_SA_CVO, head-object 11:13Z, same ETag, 404 control)",
        "investigation row MDPF_SECCLASS-S52 (2.0.0_SA_COO~M1)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Evidence row for S50's disarm; S50 is already dismissed by C-S61 on this seat's own read, and the keys still equal trunk now."
  },
  {
    "id": "MDPF_SECCLASS-C-S66",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T12:55:00Z",
    "one_line": "S53 (OBSERVATION/INERT) dismissed: S46 closes on its own condition, verified here: the six-class module is on trunk with 0 multi_asset and both firm buckets serve exactly those bytes; option (b) means no seed run strips low_confidence. REMEDIATION_v6's S46 row is CLOSED by this adjudication. S46 (REMEDIATION_v6, ARMED) is closed by this row: its close condition is met on this seat's reads.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-S53"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "S46 closes on its own condition, verified here: the six-class module is on trunk with 0 multi_asset and both firm buckets serve exactly those bytes; option (b) means no seed run strips low_confidence. REMEDIATION_v6's S46 row is CLOSED by this adjudication.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "head-object 2026-10-07 ~12:5xZ: opal-data-bd and opal-data-cot code/gold/lib/_shared/etf_classification.py both ETag 3a033c04678f1c96d116b641545b17bb = md5sum of the file at this HEAD; count of 'multi_asset' in it = 0",
        "TO-SC-e21 proof VALID (proof-of-spec-check rc=0); halves COO @59cfbf169b and CTO @b39e54dc9e choose option (b), no seed run (round-8 analysis @1ca9e97fc9 section 4 item 8)",
        "investigation row MDPF_SECCLASS-S53 (2.0.0_SA_COO~M1)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "S46 closes on its own condition, verified here: the six-class module is on trunk with 0 multi_asset and both firm buckets serve exactly those bytes; option (b) means no seed run strips low_confidence. REMEDIATION_v6's S46 row is CLOSED by this adjudication."
  },
  {
    "id": "MDPF_SECCLASS-C-S67",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T12:55:00Z",
    "one_line": "W33-S1 (OBSERVATION/INERT) dismissed: The three pre-existing findings were cleared annotation/comment-only as TO-SC-e43's bound allows; the file passes the pinned gate at HEAD. Disclosure row, nothing open.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-W33-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "The three pre-existing findings were cleared annotation/comment-only as TO-SC-e43's bound allows; the file passes the pinned gate at HEAD. Disclosure row, nothing open.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python -m ruff check --target-version py39 --extend-select FA data/black_diamond/scripts/classification/resolve_tickers.py at this HEAD (a84955405a): All checks passed!",
        "investigation row MDPF_SECCLASS-W33-S1 (0.9.0_WK_MDPF_SECCLASS~33)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The three pre-existing findings were cleared annotation/comment-only as TO-SC-e43's bound allows; the file passes the pinned gate at HEAD. Disclosure row, nothing open."
  },
  {
    "id": "MDPF_SECCLASS-C-S68",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T12:55:00Z",
    "one_line": "W35-S1 (OBSERVATION/INERT) dismissed: Resolved by e47 amendment 1: the rule now drops vendor suffixes repeatedly, so the function is idempotent again and the round-8 idempotence input is restored.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-W35-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Resolved by e47 amendment 1: the rule now drops vendor suffixes repeatedly, so the function is idempotent again and the round-8 idempotence input is restored.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "TO-SC-e47 <status>complete; amendment 1 (W35-S1: trailing vendor suffixes drop repeatedly, idempotent), per the R9 packet",
        "infra/aws/lambda/v2_portal/_shared/tests/test_security_name.py:144-145 assert clean_name('ETF SHS COM') == 'ETF' and its second pass == 'ETF'; 'ETF SHS COM' is back in the idempotent INPUTS (line 157); pytest on the file: 82 passed",
        "investigation row MDPF_SECCLASS-W35-S1 (0.9.0_WK_MDPF_SECCLASS~35)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Resolved by e47 amendment 1: the rule now drops vendor suffixes repeatedly, so the function is idempotent again and the round-8 idempotence input is restored."
  },
  {
    "id": "MDPF_SECCLASS-C-S69",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T12:55:00Z",
    "one_line": "W35-S2 (OBSERVATION/INERT) dismissed: A disclosure of reusing an identical local producer build (no new fetch) and of inflection's 2026-10-02 data date; both are the inferred-held-set condition already carried open by W25-S1 until the fence join applies.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-W35-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "A disclosure of reusing an identical local producer build (no new fetch) and of inflection's 2026-10-02 data date; both are the inferred-held-set condition already carried open by W25-S1 until the fence join applies.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "FWD15_AI_PLAN_*_20261007.json and the held-set builds record claim 'inferred'; the sibling scratch builds (wk-secclass-r9-33/35) are removed from this box, so their bytes are not re-readable",
        "graduated row W25-S1 (REMEDIATION_v6, OPEN): firm buckets deny dell1; held sets are local producer builds, inferred",
        "investigation row MDPF_SECCLASS-W35-S2 (0.9.0_WK_MDPF_SECCLASS~35)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A disclosure of reusing an identical local producer build (no new fetch) and of inflection's 2026-10-02 data date; both are the inferred-held-set condition already carried open by W25-S1 until the fence join applies."
  },
  {
    "id": "MDPF_SECCLASS-C-S70",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T12:55:00Z",
    "one_line": "W36-S1 (OBSERVATION/INERT) dismissed: The round-8 issuer check for contract 0.5.0 fails 0.6.0 by construction because e54's rulings changed the contract; it is a superseded check, not a defect, and is retired rather than run at future drains.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-W36-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "The round-8 issuer check for contract 0.5.0 fails 0.6.0 by construction because e54's rulings changed the contract; it is a superseded check, not a defect, and is retired rather than run at future drains.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "TO-SC-e54 <status>complete; proof-of-spec-check on its proof instance: VALID (rc=0); its acceptance is issuer_check_sc_e54.py, not the round-8 check",
        "investigation row MDPF_SECCLASS-W36-S1 (0.9.0_WK_MDPF_SECCLASS~36)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The round-8 issuer check for contract 0.5.0 fails 0.6.0 by construction because e54's rulings changed the contract; it is a superseded check, not a defect, and is retired rather than run at future drains."
  },
  {
    "id": "MDPF_SECCLASS-C-S71",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T12:55:00Z",
    "one_line": "W36-S4 (BLOCKING/INERT) dismissed: BLOCKING resolved by e50 amendment 1 (the defect was the check's): the re-run here reads ok=True and the order closed with a VALID proof. The bound on AI verdicts is graded on the AI run's own output under its half.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-W36-S4"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "BLOCKING resolved by e50 amendment 1 (the defect was the check's): the re-run here reads ok=True and the order closed with a VALID proof. The bound on AI verdicts is graded on the AI run's own output under its half.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "TO-SC-e50 AMENDMENT 1 (~12:4xZ) amends the issuer check: DIRECT rows graded against the bound, AI rows must be BLANK",
        "python R11_CHECKS/old_list_held_census_check.py set at this HEAD: OLD-LIST-SET-V2 ok=True rows=10965 live=10965 direct=5811 ai=2770 cash_planned=15 problems=[]",
        "TO-SC-e50 <status>complete; proof-of-spec-check: VALID (rc=0)",
        "investigation row MDPF_SECCLASS-W36-S4 (0.9.0_WK_MDPF_SECCLASS~36)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "BLOCKING resolved by e50 amendment 1 (the defect was the check's): the re-run here reads ok=True and the order closed with a VALID proof. The bound on AI verdicts is graded on the AI run's own output under its half."
  },
  {
    "id": "MDPF_SECCLASS-C-S72",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T12:55:00Z",
    "one_line": "W36-S5 (OBSERVATION/INERT) dismissed: The non-ASCII is in old_key values that are the existing DynamoDB keys of the old list; the set must carry them byte-exact to address those rows, and the reader opens it as utf-8. Nothing new is written as non-ASCII by this file; the name-value case is carried by W35-S3.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-W36-S5"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "The non-ASCII is in old_key values that are the existing DynamoDB keys of the old list; the set must carry them byte-exact to address those rows, and the reader opens it as utf-8. Nothing new is written as non-ASCII by this file; the name-value case is carried by W35-S3.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python byte scan of OLD_LIST_RECLASSIFY_SET_V2_20261007.tsv at this HEAD: 101 bytes > 127, 49 characters > 127, the same 101 bytes as round 8's set",
        "investigation row MDPF_SECCLASS-W36-S5 (0.9.0_WK_MDPF_SECCLASS~36)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The non-ASCII is in old_key values that are the existing DynamoDB keys of the old list; the set must carry them byte-exact to address those rows, and the reader opens it as utf-8. Nothing new is written as non-ASCII by this file; the name-value case is carried by W35-S3."
  },
  {
    "id": "MDPF_SECCLASS-C-S73",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T12:55:00Z",
    "one_line": "W36-S6 (OBSERVATION/INERT) dismissed: Same disclosure as W35-S2 (identical local builds reused, inflection at 2026-10-02); carried by W25-S1's inferred-held-set condition.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-W36-S6"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Same disclosure as W35-S2 (identical local builds reused, inflection at 2026-10-02); carried by W25-S1's inferred-held-set condition.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "held-set builds record claim 'inferred' (FWD15_AI_PLAN files, census JSON); the sibling scratch is removed from this box",
        "graduated row W25-S1 (REMEDIATION_v6, OPEN)",
        "investigation row MDPF_SECCLASS-W36-S6 (0.9.0_WK_MDPF_SECCLASS~36)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Same disclosure as W35-S2 (identical local builds reused, inflection at 2026-10-02); carried by W25-S1's inferred-held-set condition."
  }
]
```
