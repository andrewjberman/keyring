# /self-drive dell2-box -- tick 161 (2026-10-20 ~07:56Z-08:26Z), 1.0.0_SA_CTO~DELL2, cadence 30m

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261015_020xZ_SELF_DRIVE_DELL2_BOX_KEEP_DRIVING_ON.md`.
**Covers:** tick 161, since the tick 160 log (@959989a9c4). state: ARMED.

## Run 6 (ADDENDUM 8: the unseeded staff filing; IB2 msg 11266, receipt `irpt_anlreq_commentary_e2e6/A_E2E6.txt`)

- **PROVEN on PROD:**
  - an unseeded, non-allow-listed staff user, with no advisor and no commentary flag, filed;
  - U was NORMALIZED (2 tries); T and S were ok (REQ-7206be96);
  - **P1 was READY in 30 s on the OPAL producer**, with no RecipeRefused, so the r37 v2 routing fix held;
  - P2 and P3 (commentary ref, draft) were green.
- **NOT PROVEN:**
  - P4 STOPPED with `IRPT_RESIDENT_PACKAGE retained_for_retry class=ClientError` at 08:04:18Z;
  - the READY hook ran at 08:02:53Z, but P7 saw no package member on the ticket at 08:03:02Z or 08:03:17Z (PARTIAL expected);
  - P5, the final P7, R and R2 were NOT RUN.
- **Leftovers:** rows S224 and S225. No rerun, as ordered.

## Rulings

| item | ruling |
|---|---|
| The packager ClientError | One READ (`~Y2` TO-READ-PACKAGER-CLIENTERROR, GO 08:10Z): the full packager journal lines, the ticket service `/package` log, and the resident role's grants by simulation. No writes, no rerun. Likely the same cause as "no ticket carries a package since 10-10". |
| The v0.24 portal PROD promote (supersedes this seat's run-6 PASS gate) | RELEASED to the DT now (msgs to `~Y2` 08:09Z and 08:10Z). Filing and the Opal report are proven, and the attachment failure is backend-only and no worse than today's PROD. Andrew can test the form. Approval row to follow. |

## Acts only Andrew can do

- **Row a331** (an entitlement): the outside-domain users row in TCKT_VNEXT-D2-S53, which carries the internal firm id.
- **Recursive deletions and discards of uncommitted files** (CLAUDE.md, Agent Autonomy: "Human confirmation ONLY for:
  recursive deletion, destructive git, ... S3 deletes"):
  - `C:\dev\wk-irpt-dashbd-503`;
  - row 544d;
  - row 65a1;
  - row a392.
- **S3 deletes:**
  - row 6e7c;
  - row 128f;
  - the synthetic leftovers of runs 5 to 6.

## Completion test

NOT DONE. The dell2-box scope is a keep-driving scope; it ends on Andrew's stand-down word.

state: ARMED
