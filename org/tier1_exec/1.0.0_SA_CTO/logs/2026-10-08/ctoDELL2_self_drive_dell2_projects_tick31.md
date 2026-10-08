# /self-drive dell2 projects -- tick 31 (1.0.0_SA_CTO~DELL2)

**archetype:** COORDINATE

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_072xZ_SELF_DRIVE_60M_DELL2_IRPT_CUSTDY_IRPT_BCKEND_ADVI_COTBKF.md` @66a57498d9
**Ticks covered:** tick 31 (13:54Z) and the event-driven work since tick 30 (@122bd160aa).
**state: ARMED**

## Scope state (13:54Z)

7 of 7 are active / EXECUTING. Sequence flags were last read at tick 27 and are unchanged: NEEDS-SLOT on IRPT_CUSTDY and ADVI_COTBKF.
Inbox: 0 unread.

- **IRPT_DASHBD TO-DB-b-45, the BD split pull, ran ONCE on dell2 at 12:37:21Z:** 2,299 of 2,299 landed under `pull=split20261007`,
  0 FAILED, 2,305 vendor calls (`~D2` @d3dedd80a4).
- **The stale ledger `irpt-ycdgen-r6-branch-b2-20261006`** is being closed: it is deleted in the shared working tree, not yet
  committed. `~G2` owes the closing hash.

## Calls closed and acts

| input | ruling or act | carrier |
|---|---|---|
| `~K2` 1277: E3's Taildrop carries one RENDERED BD 49F client report | **CORRECTION to tick 30's row.** My ruling 1276 is withdrawn for E3 and the Taildrop is KEPT, because Andrew chose (a) for this item (@38c34d7821). A report fetch through the BD session would be a new vendor leg that no order of his names. MSTR coordinates the Taildrop. | broker, to `~K2` |
| MSTR 1282: step C applied at 12:39:33Z | Confirmed the before-rule is held. Relayed to the 9 dell2 COOs, with the HOLD on `infra/aws/terraform/nfra-ctlpln-identity` until laptop `~C`'s fix merges (msgs 1295-1304, 10 DELIVERED). `~K2` reports 0 open orders touch a policy. | broker |
| MSTR 1306: Andrew-direct ~13:2xZ "HAVE DELL2 RETRY" | **Ruled how FWD-1's ACCEPT reads a dell2-made run.** It counts as the seat-driven arm only through the real portal route with an authenticated principal, on one real Cottonwood portfolio, read back rendered, with zero YCharts calls measured. Andrew's own sitting is the organic arm. `~G2` runs it. | `CTO_RULING_IRPT_YCDGEN_FWD1_DELL2_RETRY_20261008.md` (commit pending a shared merge); msgs 1307-1308 |

## Acts only Andrew can do

- **The F1 retry is REMOVED from this list.** His word moved it to dell2 (msg 1306).
- Others unchanged from tick 19.

## Completion test

NOT DONE: 0 of 7 complete. 7 REACHABLE, 0 UNREACHABLE.
