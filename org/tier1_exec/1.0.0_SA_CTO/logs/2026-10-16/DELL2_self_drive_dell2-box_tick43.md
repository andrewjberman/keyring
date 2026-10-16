# /self-drive dell2-box -- tick 43 (2026-10-16 ~10:27Z-10:56Z), 1.0.0_SA_CTO~DELL2, cadence 30m

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261015_020xZ_SELF_DRIVE_DELL2_BOX_KEEP_DRIVING_ON.md`.
**Covers:** since tick 42 (@411e4fb4ad). Substantive delta.

## Acts taken

| act | carrier |
|---|---|
| XB-bfaa (FWD-23): dell2 seats.json committed by this seat (21 seats; the MSTR is refused by the lane) and the crossbox answered: graded work is IRPT_DASHBD r147 PUBLISH, graded by CVO~IRPT v131 | @7464c5847c; answer record; to-side closed |
| `~Y2` msg 9281 (the run-3 probe: all 5 candidates TICKER_CHECK_FAILED): ruled HOLD, no B-only run. Diagnosis assigned to `~G2`; the re-probe needs AMENDMENT 3 | msgs 9282/9283 |
| `~Y2` msg 9287: the probe's correction answers DID store 5 synthetic CSVs (addendum 3's "stores nothing" was inferred and wrong). Registered with the R33 sitting's 8 as Andrew's delete act (row dc59: keep until run 3 is graded, then a listed-key delete) | row dc59 |
| `~G2` msg 9290 diagnosis: a checker bug. yfinance 1.2.0 RAISES YFTickerMissingError on an unknown symbol and `default_history` lets it escape. r34d accepted, with the condition: ONLY that class (and its subclasses) maps to NOT_KEPT, every other exception stays CHECK_FAILED, tests on both sides, V2 in the service's own environment | msg to `~G2` |

## Release chain (IRPT_ANLREQ)

r33, r35L and r34c are LIVE. Run 3 is HELD before its run window (unspent). Next: r34d (the checker fix), then AMENDMENT 3 re-probe, then the run.

## Open calls (dell2 list: 3 open, all Andrew's acts)

## ACTS ONLY ANDREW CAN DO

- **dc59 (new):** the delete of the synthetic test objects in the 49financial intake store (5 probe CSVs plus 8 from the R33 sitting),
  after run 3 is graded. It is an S3 delete (CLAUDE.md Agent Autonomy: "dropping tables/S3 deletes" need human confirmation).
- **c02c:** POSTPONED on his word, condition met.
- **e260:** the Opal_Terminal key, his.

Completion test: NOT DONE. state: ARMED

## Compiler Tools

open-calls.py, crossbox-call.py, agentbus-sqs.sh, safe-commit.sh.
