# MDPF_SECCLASS -- rounds 2 and 3 L8/L9 adjudication

<sweep_watermark>2026-09-30T06:25Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-09-30 ~07:2xZ. L8 packet: 2.0.0_SA_COO~M 103214 (DRAIN_END_R2_R3_20260930.md @6d22aa7388). Review: org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_SECCLASS_R2_R3_REVIEW_20260930.md (co-committed). 9 undispositioned rows: 5 dismissed by the 4 rows below, 4 graduated in remediations/REMEDIATION_v2.md. L9: no swept order carries a JUDGMENT criterion (0 of 9). The watermark is the order-set cut: SC-e10 (round 4, first added 06:29Z) is outside this compile.

```json
[
  {
    "id": "MDPF_SECCLASS-C-S4",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-30T07:20:00Z",
    "one_line": "W4-S2 (the contract still read v0.1.0 in one worktree) is resolved by the drain: the contract at HEAD is v0.2.0 with identifier_namespace and four classified_by values.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-W4-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "org/standards/MDPF_SECCLASS_CONTRACT.json at CLOUD HEAD: contract_version 0.2.0; fields instrument_kind, identifier_namespace {TICKER, CUSIP}, classified_by {seed, scheduled, constituents, legacy}.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "the contract file read by this seat at 07:1xZ (json.load, contract_version and both enums printed)",
        "investigation row MDPF_SECCLASS-W4-S2 (0.9.0_WK_MDPF_SECCLASS~4): a sibling cell's commit not yet in its worktree",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_SECCLASS_R2_R3_REVIEW_20260930.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The row described a worktree's view before the sibling cell drained; the shared tree now carries SC-e1's amendment, so nothing is open."
  },
  {
    "id": "MDPF_SECCLASS-C-S5",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-30T07:20:00Z",
    "one_line": "W5-S1 (a round-1 test encoded the superseded two-value C-WRITER) is fixed by SC-e2 amendment 1; W5-S4 is the worker's record of that fix.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-W5-S1",
      "MDPF_SECCLASS-W5-S4"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "test_seed_fields.py at HEAD carries test_constituent_seeder_sets_constituents_label_and_refuses_seed_or_scheduled (1 occurrence) and no longer the never-sets assertion; the worker read 19 passed after the edit.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/v2_portal/_shared/tests/test_seed_fields.py at HEAD, grep count 1 for the new test name",
        "investigation rows MDPF_SECCLASS-W5-S1 and MDPF_SECCLASS-W5-S4 (0.9.0_WK_MDPF_SECCLASS~5)",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_SECCLASS_R2_R3_REVIEW_20260930.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The stale assertion is replaced under the issuer's own amendment; the repo-wide regression it tracked is gone."
  },
  {
    "id": "MDPF_SECCLASS-C-S6",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-30T07:20:00Z",
    "one_line": "W6-S1 (BD's E_18 caller resolved the repo root one hop short) is fixed by SC-e7 amendment 1 in both firm files.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-W6-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "data/black_diamond/scripts/gold/E_18.detect_new_securities.py:54 and data/cot/scripts/gold/E_18.detect_new_securities.py:64 both read Path(__file__).resolve().parents[4] at HEAD.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "both files at CLOUD HEAD, the _REPO_ROOT lines printed by this seat",
        "investigation row MDPF_SECCLASS-W6-S1 (0.9.0_WK_MDPF_SECCLASS~6)",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_SECCLASS_R2_R3_REVIEW_20260930.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The one-line fix the row asked for is on HEAD in BD's file and in COT's copy. Whether FWD-7's BD caller has run live since is E18_IAM's release question, not this row's."
  },
  {
    "id": "MDPF_SECCLASS-C-S7",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-30T07:20:00Z",
    "one_line": "W4-S1 (round 2's thread census used its own population, not round 1's unrecoverable one) is a named substitution, not a regression.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-W4-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Round 1's resolution-stage generator lived in an uncommitted .scratch/ and cannot be re-run; round 2 measured 2,220 distinct held tickers with the production filters and said so in the census and the half.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row MDPF_SECCLASS-W4-S1 (0.9.0_WK_MDPF_SECCLASS~4)",
        "DRAIN_END_R2_R3_20260930.md: THREAD-CENSUS gold rows=524413 unclassified=1822 (round 1: 3565)",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_SECCLASS_R2_R3_REVIEW_20260930.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The like-for-like figure is the gold-row count (524,413 both rounds; unclassified 3,565 -> 1,822), which the review reads. The 3,992-vs-2,220 difference is two populations, as the row says."
  }
]
```
