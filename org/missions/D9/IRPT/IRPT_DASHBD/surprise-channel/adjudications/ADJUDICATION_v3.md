# IRPT_DASHBD -- rounds 5 to 9 (workstream B) L8/L9 adjudication

<sweep_watermark>2026-10-03T01:40Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-10-03 ~02:4xZ. L8 input: the issuer's drain-end records deliverables/2.0.0_SA_COO~P/IRPT_DASHBD_ROUND8_B_DRAIN_END_20261003.md @4e62b37990 and IRPT_DASHBD_ROUND9_B_DRAIN_END_20261003.md @f033774b5a; CTO RULINGS batches 193, 195 and 197; this seat's FWD-8 round-8 grade @a108c6bd93. 15 of 15 orders are complete. 14 rows surfaced after the previous watermark 2026-10-02T18:45Z (W1-S12 to W1-S20, W2-S1 to W2-S3, W3-S1, W4-S1, W4-S2); 46 rows are in the channel, 32 of them compiled at v1 and v2. 5 are dismissed by the 4 rows below (W1-S15, W1-S16, W1-S20, W2-S1, W2-S2). 9 graduate in remediations/REMEDIATION_v3.md (W1-S19 and W2-S3 share one remedy): 1 REMEDIATED and closed (W3-S1) and 8 OPEN, all in the issuer's P-2 packet except W1-S17. 0 rows ARMED: W1-S18 was disarmed by batch 193. Reads this seat made at ~02:3xZ: code at HEAD, the summary contract, the publish source map and Terraform text, reporting/tests run, and Schwab silver for one tie-out pair.

```json
[
  {
    "id": "IRPT_DASHBD-C-S11",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-03T02:45:00Z",
    "one_line": "W1-S15 and W1-S16 are decided and adopted: the summary contract 0.1.0 names the opaque key space (cli_ client ids, no custodian number) and carries window_status MEASURED / NOT_SPANNED / BREAK and unpublished_account_ids as required keys.",
    "class": "OBSERVATION",
    "adjudicates": [
      "IRPT_DASHBD-W1-S15",
      "IRPT_DASHBD-W1-S16"
    ],
    "spec_asserts": "Spine L9 (CLAUDE.md rule 27): every investigation item is dispositioned on grounded evidence; an issuer's 'answered by ruling X' is checked against each finding the row holds.",
    "world_is": "The worker's two open points became contract text the next round landed under CTO batch 197: the document is keyed by the issued opaque client id, never a name or custodian number; a window across a null-return day answers BREAK, never bridged or zero-filled; a partial client lists its unpublished accounts. The deployed path's raw-to-opaque mint is W4-S1's packaging, graduated below.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/standards/IRPT_DASHBD_CLIENT_SUMMARY_CONTRACT.json at HEAD (DB-b-16 @00145f3a27): client_id 'the ISSUED opaque client id (cli_ + 24 hex) of a directory entry; never a name and never a custodian number'; required keys include unpublished_account_ids; window_status block present (this seat's read 2026-10-03 ~02:3xZ)",
        "1.0.0_SA_CTO RULINGS batch 197 @7563d60e68: the summary has its own versioned contract and is served only on full per-account coverage"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Adopted by the contract: both rows asked for a decision the order left open, and the contract that landed records it."
  },
  {
    "id": "IRPT_DASHBD-C-S12",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-03T02:45:00Z",
    "one_line": "W1-S20 is ruled: a MARGIN INT ADJ credit is RETURN (batch 195), the same side as the margin interest it adjusts (round-2 analysis); the margin interest debit is a cost inside the return, not income and not a flow, by the same ruling.",
    "class": "OBSERVATION",
    "adjudicates": [
      "IRPT_DASHBD-W1-S20"
    ],
    "spec_asserts": "Spine L9 (CLAUDE.md rule 27): every investigation item is dispositioned on grounded evidence; an issuer's 'answered by ruling X' is checked against each finding the row holds.",
    "world_is": "Both of the row's facts are true and both are the ratified method: the 4,429.53 credit stays inside the return, and the 3,106.83 INTR debit moves value, not the income term. The pair it touches carries this as its stated non-defect reason in the round-8 tie-out.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "1.0.0_SA_CTO RULINGS batch 195 @8dcb24b212: 'RULED: RETURN, not an external flow ... W1-S20 is DISARMED by this ruling'",
        "deliverables/0.9.0_WK_IRPT_DASHBD~2/TIEOUT_49F_BLACKDIAMOND_R8.json s22 block: disposition RESTATED, residual 0.4738 pp, counterfactual 0.0044 pp"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Ruled by batch 195; no producer change follows from it."
  },
  {
    "id": "IRPT_DASHBD-C-S13",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-03T02:45:00Z",
    "one_line": "W2-S1 is answered by the standing rulings: under batch 181 a pair beyond 0.35 pp with a stated non-defect reason is explained, batch 193 keeps Black Diamond's accrual outside Opal's figure and stated per pair, and C-FEERAIL keeps Opal gross of fee; this seat re-derived all four reasons from Black Diamond's raw responses.",
    "class": "OBSERVATION",
    "adjudicates": [
      "IRPT_DASHBD-W2-S1"
    ],
    "spec_asserts": "Spine L9 (CLAUDE.md rule 27): every investigation item is dispositioned on grounded evidence; an issuer's 'answered by ruling X' is checked against each finding the row holds.",
    "world_is": "The four pairs beyond 0.35 pp at method_version 2 carry reasons that hold: accrual +6,022.40 (0.4999 pp, residual 0.0001) and -5,766.11 (0.4501 pp, residual 0.0107) on acct#6b914f88; a 3,020.96 fee inside Black Diamond's return (0.3961 pp, residual 0.0084) on acct#ffa615d2; the margin interest adjustment on acct#89d0916a (equity ratio 0.027544 from Schwab silver against 0.022806). No further ruling is needed to grade FWD-8; the CTO may still revisit the bar at the round analysis.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_DASHBD_FWD8_L9_GRADE_20261002.md section 'Round 8 re-grade' @a108c6bd93",
        "1.0.0_SA_CTO RULINGS batch 181 item 3 and batch 193 item 3 (RULINGS.md, IRPT_MVP_COMPLETION_20260922)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Explained under batches 181 and 193 and C-FEERAIL; each reason re-derived by this seat. Not a defect."
  },
  {
    "id": "IRPT_DASHBD-C-S14",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-03T02:45:00Z",
    "one_line": "W2-S2 is a definition and a census, not a finding against the spec: 'margin 0' means zero on the day and the prior trading day, 6,788 such accounts are unchanged apart from method_version, and 0 of 3,230,967 history rows carry a null margin_balance.",
    "class": "OBSERVATION",
    "adjudicates": [
      "IRPT_DASHBD-W2-S2"
    ],
    "spec_asserts": "Spine L9 (CLAUDE.md rule 27): every investigation item is dispositioned on grounded evidence; an issuer's 'answered by ruling X' is checked against each finding the row holds.",
    "world_is": "The producer treats a null component as an absent value and prints it; none exists today. The 28 accounts whose margin moved to zero change correctly because the day's base is the prior day's equity.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/0.9.0_WK_IRPT_DASHBD~2/POPULATION_EQUITY_R8.json and scan_balance_history_r8.py",
        "data/assets/scripts/gold/irpt_reporting/sources.json at HEAD: account_value_columns_comment 'A NULL in any listed column makes that account-day's value ABSENT (never a zero)'"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Measured, recorded in the declaration, no defect."
  }
]
```
