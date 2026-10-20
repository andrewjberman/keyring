# /self-drive dell2-box -- tick 156 (2026-10-20 ~05:29Z-05:56Z), 1.0.0_SA_CTO~DELL2, cadence 30m

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261015_020xZ_SELF_DRIVE_DELL2_BOX_KEEP_DRIVING_ON.md`.
**Covers:** tick 156, since the tick 155 log (@03ddaa3241). state: ARMED.

## Rulings and acts

| item | ruling / act |
|---|---|
| W6-S2 and S50 (`~V2` msg 11223) | Already fixed and LIVE: live equals tree, tests pass. No builds and no pair. CVO v16 closed both (msg 11234). |
| S46 (`~V2` msg 11228, census @5261de0431) | No fix. `opal-ticket-api` is invokable directly only by the 4 AdministratorAccess users; the 4 service roles invoke only their designed targets. CVO REMEDIATION_v3: ACCEPTED_BY_RULING. Narrowing the CloudOps agent users off admin is a separate topic, with no IAM change here. |
| r37 v2 pair (the door: O1 fallback + ticket-confirm routing; blob a39448fe71, sha256 e45b547d) | CTO half SIGNED @d9d913c5cf; it supersedes the r37 v1 half. Read here: `ticket_confirmation.py` @752e87d46b7, and `created_by` is server-written (`ticket_center/lambda_function.py:40-42, :1433`). The widening (every own-`/tickets` `analysis_request` takes the Opal producer) is accepted under FWD-1 item (3). GO from 07:00Z: r37 v2, then r34m v2, then run 6. |
| ADDENDUM 8 binding (`~Y2` msg 11230) | Already re-bound @bb3d307f29 to blob 09f6fa2997. |
| TCKT_VNEXT round 20 L10 slug (`~V2` msg 11233) | Analysis written: `CTO_ROUND_ANALYSIS_TCKT_VNEXT_ROUND_20_20261020.md` @d6057e5917. Round 20 is CLOSED; FWD-11 is REALIZED (CVO v14). The Trade byte read-back is round-21 enrichment item 1. Round 21 issues only after IRPT_ANLREQ's v0.24 set reaches PROD. |

## Acts only Andrew can do

- **Row a331** (an entitlement): the outside-domain users row in TCKT_VNEXT-D2-S53, which carries the internal firm id. It is the last ARMED
  TCKT row; the data-refresh gate also trusts that id.
- **Recursive deletions and discards of uncommitted files** (CLAUDE.md, Agent Autonomy: "Human confirmation ONLY for:
  recursive deletion, destructive git, ... S3 deletes"):
  - `C:\dev\wk-irpt-dashbd-503`;
  - row 544d;
  - row 65a1;
  - row a392.
- **S3 deletes:**
  - row 6e7c;
  - row 128f;
  - the synthetic leftovers of runs 5 to 5D.

## Completion test

NOT DONE. The dell2-box scope is a keep-driving scope; it ends on Andrew's stand-down word.

state: ARMED
