# SELF-DRIVE laptop directives -- tick 24 (2026-09-27 ~00:28Z)

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_LAPTOP_DIRECTIVES_IRPT.md`
@`ce6aa15a17`. **Covers:** the ticks since tick 23 (@`e3b68ee408`, 23:18Z). **State: ARMED.**

## Scope

9 laptop directives of 15 live (register `directives-check.py --json`). IRPT first:
- IRPT_BCKEND: active / EXECUTING (~P, ~M, ~Y on /closer-drive);
- DSGN_IRPTV1: active / EXECUTING (~D on /canonical-drive), PRD v0.16 @`f3026103f0` ADMITTED (both halves).

Unread at the tick: 0 (every item in `.unread-deliveries` was answered; replies in `~D`/`~P` inboxes).

## Acts (1.0.0_SA_CTO lane)

1. **OA-g-2 positive control (promised to site Z, agentbus 3e0605d2):** after site Z's gateway release df724ef284
   (live 23:15:53Z, MSTR relay 101664), `read_chat_messages top=25` on the two chats that used to return Graph 500.
   Both returned 25 messages with `@odata.nextLink`, no 500; both responses carry `select_fallback: true`. PASS,
   reported on agentbus (MessageId 4de336c2; NOT DELIVERED until site Z acks).
2. **C25 PROD promote (Andrew pre-authorized on the CVO PASS, record @`74bb8f9494`; CVO grade @`e20d1773da`):**
   read, not performed (MSTR's act):
   - portal PROD = `a0314f22` (ls-remote read), equal to the graded c25-narrow-trial head;
   - Deploy to Production run 36282246114 on `a0314f22`: completed / success (00:26:06Z);
   - tag `portal-v2.1.189` peels to `a0314f22`;
   - PROD in DEV: NO at 00:27Z -- the PROD->DEV back-merge is still owed by MSTR (DEV `4e29386e`).
3. **IV-e-35 (~D 101650):** ruled (a) merge as a strict improvement, one harness cell with a deterministic runner
   (reply at 00:09Z); ~D drained wk-DSGN_IRPTV1-23 @`c1e4b26d78`.
4. **IV-e-46 (~D 101647):** GO with one change (reply 00:07Z).

## Verdicts / words received

- **Window 6 K4/K5:** Andrew said go at ~Y's terminal at 00:09Z (~Y to ~P, inbox file `20260927T000923Z_2.0.0_SA_COO_Y_Window_6__Andrew_said_go_at__Y_00_09Z_--.md`). The open call
  is CLOSED. K4 NORMALIZED 00:10:04Z; K5 QUEUED, finishing server-side under branch (e).
- **Window 6 close (~P @`56327aee4c`):** principal deleted 00:21:32Z against a 00:20Z deadline (92 s late, branch (e):
  the job was still SUBMITTING). K1 GetItem absent, login 401, K1-CRED ParameterNotFound. Both halves covered the
  branch; no row owed from this seat.
- **Andrew-direct via ~M:** "VNQ is alternatives, it's a REIT" -- confirms the signed ETF Part A direction.

## Open calls in scope

None at this seat. PRD-002 alarms stay HELD on Andrew's word ("alarms need further consideration").

## Completion test

NOT DONE: IRPT_BCKEND and DSGN_IRPTV1 both `active` / EXECUTING (0 of 2 IRPT projects complete). D10 has no members:
UNMEASURABLE (routed to 0.0.0_AB_MSTR at arm).

## Waiting on other seats

| seat | owes |
|---|---|
| 0.0.0_AB_MSTR | the PROD->DEV back-merge of `a0314f22` |
| ~P | window 6 K5 server-side completion read |
| ~D | IV-e-46 re-cut; the IV-e-35 harness cell; round 7 cells; the Global merge |
| ~M | Monday 09-28 runs; the R4 enable half (full pinned delta); ETF Part B census |
| 3.0.0_SA_CVO | the round-5 slug (then this seat's L10 analysis) |
| site Z | ack of agentbus 4de336c2 |

**Next at this seat:** re-arm FAST leases ~M/~P/~Y before 01:52Z.

## Compiler Tools

`gh -R Opal-Capital/portal run list` filtered by headSha (the `--branch PROD` filter returned a stale a580bbb4 run --
a sha filter is the sound read); `git ls-remote`; `git tag --points-at` + `rev-parse ^{commit}`; `directives-check.py`;
`active-commitments.py`; `prd-signoff.py status`.

state: ARMED
