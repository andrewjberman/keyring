# /self-drive dell2 projects -- tick 10 (1.0.0_SA_CTO~DELL2)

**archetype:** COORDINATE

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_072xZ_SELF_DRIVE_60M_DELL2_IRPT_CUSTDY_IRPT_BCKEND_ADVI_COTBKF.md` @66a57498d9
**Ticks covered:** the event-driven work since tick 9 (@ba3de8941d), plus tick 10 (15:45Z). **state: ARMED**

## Scope state (15:45Z)

| project | status | dep_stage | sequence flag |
|---|---|---|---|
| IRPT_CUSTDY | active | EXECUTING | NEEDS-SLOT (known tracker gap; `~K2` live) |
| IRPT_BCKEND | active | EXECUTING | none |
| ADVI_COTBKF | active | EXECUTING | NEEDS-SLOT (known tracker gap; `~C2` live) |
| IRPT_YCDGEN | active | EXECUTING | none |
| IRPT_DASHBD | active | EXECUTING | none |
| NFRA_TRNSPT (placed on dell2; project.json now reads placement DELL2, lane `~T2`, round 4, from merge @508fa452bd) | active | EXECUTING | none |

Denominator: 6 projects, 6 active. Inbox: 0 unread after acks. dell2 CLOUD is 0 behind origin (msg 797).

## Calls closed and acts (driver ruled, REC)

| input | ruling or act | carrier |
|---|---|---|
| CVO slug 737 (ADVI_COTBKF round 12: cash in lieu unsigned) | Round 13 is E1 (a census of every transaction type, `leu` -1, rebuild) and E2 (crosswalk re-scored) | @9a9384d247 |
| CVO slug 744 (IRPT_DASHBD round 23: 39 of 91 identity gaps) | Round 24 is E1 (diagnose: the 1.1M account term by term, a type census, the gaps classed) and E2 (fix and re-grade on a window with a realized term) | @9f285400cf |
| CVO slug 747 (IRPT_CUSTDY round 6) | Hop 5's server half is live. Round 7 is E1 (mixed household refused), E2 (hop 5 served, after the DEV landing) and E3 (FWD-9 field map) | @881e552c2e |
| `~K2` 739 / 758 (portal e355d193, then 4c10b488) | CHANGES (a mixed document refused by name), then PASS. The DEV landing is Andrew's word | msgs 743, reply to 758 |
| CRO 748 / 752 (Product-Alyssa; the PRD-001 shape) | Design call ruled after research. The labelled corpus becomes C-CRITERION's precision ground truth; no store exists; C-GOLD-FIELDS stands | @7164750e30 |
| MSTR 755 (IB-pr-349 after-reads 4-5 blocked by the order's bound) | REC to `~P2`: grade the exposure on the controls; the new-export reads go to the first real Opal export. The ledger then CLOSED, 4 legs proven (msg 764) | msg to `~P2` 15:21Z |
| `~T2` 762 (NFRA_TRNSPT C3 packet) | CTO never-widen half SIGNED with 4 conditions (no landed-key delete without Andrew; APPLY 2 owned and timed; no content read from dell2; laptop applier on a permission refusal) | @d450f6664b |
| MSTR 731 (the dell2 CRO session ended) | Ruled: leave it down. Superseded by Andrew-direct: reseated as `4.0.0_SA_CRO~D2` for the Opal gateway MCP | record @039e62c520 |
| MSTR 764 (Andrew-direct: the download tiers bind EVERY box) | Relayed to 10 dell2 seats (msgs 775-784). This answers the tick-8 question to Andrew | -- |

## Acts only Andrew can do

1. The IRPT_YCDGEN F1 retry on DEV (his login).
2. The ADVI_COTBKF Bloomberg share: 1,319 securities / 2,317,534 security-days (his per-use vendor word).
3. The IRPT_DASHBD split BD pull, 2,299 calls (his per-use vendor word).
4. The IRPT_CUSTDY portal DEV landing of e355d193 + 4c10b488 (his word for portal landings).
5. Lifting his PROD advisor hold: "no advisor on PROD until the fail-closed release ships". The release shipped; the exposure is proven
   closed, ledger CLOSED.
6. Handing IRPT_CUSTDY reports to the advisor (egress), when hop 5 serves.
7. NFRA_TRNSPT:
   - the 14 flagged words (his named-reader read);
   - FWD-8's second reader (his naming);
   - Alyssa placing her labelled corpus into bronze (client PII moving between people).
8. Answers asked: R13 (a per-firm correction memory); confirming FWD-17 to FWD-23. The download-tier question is ANSWERED (msg 764).

## Completion test

NOT DONE: 0 of 6 complete. 6 REACHABLE, 0 UNREACHABLE.

## Compiler Tools

- `sequence-check.py --project` x6: unchanged from tick 9.
- Portal diff read by hash range (`git diff e355d193 4c10b488`): it caught the mixed-shape path before PASS.
