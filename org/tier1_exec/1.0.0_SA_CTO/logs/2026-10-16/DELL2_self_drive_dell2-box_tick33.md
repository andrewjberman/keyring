# /self-drive dell2-box -- tick 33 (2026-10-16 ~05:27Z-06:06Z), 1.0.0_SA_CTO~DELL2, cadence 30m

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261015_020xZ_SELF_DRIVE_DELL2_BOX_KEEP_DRIVING_ON.md`.
**Covers:** since tick 32 (@92c78aa4c0). Substantive delta.

## Acts taken

| act | carrier |
|---|---|
| F-SHIP r124: the FWD-5 words RATIFIED at `tran_srcde` grain (160 codes, 16 UNMAPPED); flow class per code, not per word (W1001-S2) | @c43f8fc13a |
| B-CW r147 (`~C2`, DB-c-25): four portal commits REVIEWED and PASS. The candidate was cut from PROD and approval row 92c0 registered, client-facing | review msg; row 92c0 |
| r35L (the irpt-status failure-code reader) CTO half SIGNED (blob 3092cf2a13). Applier AQ2. R0 lists the role's policies: any jobs-table write is a STOP | @2d5d62db42 |
| F-SHIP r125: UNMAPPED shows as "Unclassified" (amends r124's "Other"); absent and served-empty are told apart with reasons | @e9ea3fb815 |
| R34C (the resident re-apply with the hop_failure writers) NOT SIGNED: its pre-read requires the r34 root absent and D1 requires 404 keys, but the rollback kept both. Rebuild under r34c names. Deleting the kept objects is refused (an S3 delete is Andrew's) | msg to `~G2` |
| Run-3 ADDENDUM 3 AMENDMENT 1 (blob b778d4072e) NOT signed yet: its R0e pins the unsigned R34C. Re-pin once to the renamed packet | msg to `~Y2` |
| MSTR msg 9111 (the private sweeps config to dell1): not confirmed sight unseen. COTBKF_SWEEPS_CONFIG is not set in this seat or at User/Machine scope; asked for the path; read before confirm | msg to MSTR |

## Open calls (dell2 list: 3 open, all Andrew's)

## ACTS ONLY ANDREW CAN DO

- **92c0 (new):** approve for portal DEV the client-facing Performance-tab note "N trading days not reported by the source: <dates>."
  (CLAUDE.md Portal: "client-facing for Andrew"). CTO review passed. No live account shows it until the Cottonwood publish Act 4 lands.
- **c02c:** POSTPONED on his word, condition met.
- **e260:** the Opal_Terminal key, his.

Completion test: NOT DONE. state: ARMED

## Compiler Tools

open-calls.py, safe-commit.sh, git diff --no-index, portal git log and diff, Grep, PowerShell Get-FileHash.
