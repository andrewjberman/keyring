# drive log -- 2.0.0_SA_COO~D2 -- 2026-10-08 20Z -- desktop-n8rjv0a (dell2)

## ticks 166-178 -- round 29 executed, drained, MAY-CLOSE

| project | limb | round | TOs | act |
|---|---|---|---|---|
| IRPT_DASHBD | L7 -> L10 | 29 | 3/3 complete | three drains; round-close-check MAY-CLOSE; slug to 1.0.0_SA_CTO~DELL2 |

### Results (issuance @316736121d, analysis @e9b17e6e75)

- **DB-b-50 (E1), worker ~29, drained @8de470994a, proof VALID.**
  - S34's 440 accounts are classed: 437 `fee_or_basis_between_pulls` and 3 `other` (net over tolerance on near-zero opening values).
  - On all 437, BD's NET returns chain within 0.35 pp. The gross gap comes from round 18's fee add-back, `fees / ((bmv + emv) / 2)`, which
    is not additive across ranges. That is an artifact of Opal's tie-out method, not a BD inconsistency.
  - The 724.16 pp outlier is the add-back on a closing balance (ending value 0).
  - Overlap: 1,834 right-half misses, 306 inside the 440, 1,528 outside.
  - Row W29-S1.
- **DB-b-51 (E2), worker ~30, drained @1ee0fd9e99, proof VALID.**
  - Right-half signed gap over the 1,528: median +0.567 pp, p10 +0.374, p90 +0.764. Opal is above BD on 94.7% of them.
  - Correlation of the gap with the half's length: -0.145.
  - No Opal component explains the gap. The top driver is carried_days at r = -0.144; external_flow, income_received and market_value_eod
    are each about -0.009. fee_amount is 0 on every day, so its correlation is undefined (W30-S1).
  - Control over the 2,220 left-half ties: carried_days r = -0.042, so signature_absent is true.
  - Row W30-S2: round 18's read_gold column list omits four columns.
- **DB-b-52 (E3), worker ~31, drained @50a0ebae91, proof VALID.**
  - DEFAULT_BATCH_SIZE goes from 1000 to 2000.
  - The default run over 7,604 accounts: total 666.98 s; lots 442.04 s with a 1,526.3 MB peak.
  - 3 of 6 runs finished at or under 750 s. Batch 2,000 itself read 757.55, 692.81 and 666.98 s, so the 750 s bar sits inside this box's
    run-to-run spread (W31-S2).
  - Batch 0 ended without a record at 900 s and 2,733 MB (W31-S1).

### Drain mechanics

- Workers ~29 and ~30 appended to the investigation channel at the same offset.
- My first hand resolution in the shared tree broke a fence. The row gate refused it, the merge aborted, and nothing landed.
- The working method: resolve on the worker branch with safe-merge in its worktree, writing the channel as the target's file plus the
  branch's appended rows, then drain. That gave @5fa49047de for ~29 (107 blocks, 0 malformed) and @bf98f75e66 for ~31 (109 blocks).
- Drain hygiene on the producer: py_compile OK, ruff OK, 45 tests passed.
- Worktrees wk-29, wk-30 and wk-31 are removed with their branches (Andrew-direct @76e0e59d53).
- The shared tree moved to box/dell2 at 20:00:46Z (MSTR msg 1526). ~31 drained onto box/dell2.
