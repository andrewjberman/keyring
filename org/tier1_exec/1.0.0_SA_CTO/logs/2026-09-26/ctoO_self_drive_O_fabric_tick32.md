# /self-drive ~O fabric -- ticks 31-32 (2026-09-26 19:19Z - 20:35Z)

- Driver `1.0.0_SA_CTO~O`; arming record `ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_O_FABRIC.md` @56050d290d; cron 8abcafba.
- state: ARMED.

## Calls and verdicts
No open calls in scope. No new verdicts.

## NFRA_OPALAI's gating items: 0 open
- The fold (`_latest_dispositions` / `_gating_item_ids` in `.tools/surprise-row-gate.py`, run on NFRA_OPALAI) read 17
  gating items, 5 terminal. A disarm row that carries disposition UNDER_INVESTIGATION leaves its target open in the fold.
- This seat's two (Z-S21, Z-S30): made terminal by row Z-S33 @be4f5e58e6.
- COO~O's twelve: made terminal by its row Z-S34 @18f9409711. Re-measured here: gating 17, open 0.
- W4-S1 is disarmed, not fixed: it became cutover precondition CP-1 in NFRA_OPALAI_DECOMP.md (the live D7 intake
  runner.py still imports teams-watch.py, so the cutover re-points it before the file goes).

## Shared-tool defects routed to this seat by COO~O (file 20260926T202700Z)
| row | tool | state |
|---|---|---|
| W1-S1 | `.tools/owned-paths-validate.py` ignores the worker grant for a path with no lane row | FIXED earlier by this seat @6bc980ad5d (2026-09-25 05:05Z; the row is 09-24 22:30Z) |
| W5-S1 | `.tools/git-hooks/install-owned-paths.sh --submodule` resolves REPO_ROOT from the ambient cwd | FIXED @aa2f79ef0d: resolved from the script's own location. Run from /tmp, the new form finds the workspace; the old form fails |
| W2-S4 | `safe-ec2-deploy.sh` Step 3 writes EC2_MANIFEST.json with CRLF via jq.exe | **PARKED.** Owner: this seat. Condition: after OA-g-2's deploy (GO 21:07Z) closes its ledger, because that deploy runs this script tonight. The in-cell workaround (record by hand on an LF copy) stands meanwhile |

## Fabric movement
- COO~O recorded Andrew's call 3 (the stale converter-snapshot sweep) as QUEUED, NOT ISSUED @4f257c9a58.
- OA-g-2: every GO guard met; GO 21:07Z.

## Completion test
NOT DONE: 0 of 4 `complete`. Reachable 4 of 4.

## Compiler Tools
`python -c` over `.tools/surprise-row-gate.py` (`_latest_dispositions`, `_gating_item_ids`).
