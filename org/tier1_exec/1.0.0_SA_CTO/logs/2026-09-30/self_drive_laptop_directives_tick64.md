# /self-drive laptop directives -- ticks 62-64 (2026-09-30 21:26Z-22:3xZ)

Arming record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260928_230xZ_SELF_DRIVE_LAPTOP_FABRIC.md`; cron
`41f0ce1e`. **state: ARMED.** Previous log: tick 61 @e9595648d4. Written on the hourly floor and one driver act.

## Scope (register 22:34Z; sequence unchanged)

10 of 15 live directives on the laptop; open TOs D2 19, D3 4, D8 20, D9 38, D11 4, D13 1 (86); D10 NO-MEMBERS (UNMEASURABLE, at
MSTR). Sequence: 10 placed, no DRIFT; CAPACITY 5 live COO lanes vs cap 3 (Andrew's IRPT seating word). Inbox: 103396 and 103399 read
and acked; 0 unread at the tick. Push: origin/CLOUD 85a765dbcd (site Z); local ahead 89 by the last fetched ref; integration is MSTR's.

## What moved

- **All four rounds this seat analysed today are issued:** MDPF_SECCLASS round 6 @c7571d32b0, IRPT_BCKEND round 27 ~P @22b99e32fd,
  NFRA_TRNSPT round 2 @35d912322e (from the round-1 analysis @acd1033e60), IRPT_DASHBD round 1 in flight.
- **IRPT_DASHBD's first gold contract** landed @10939bbfa4 and was read against PRD ruling 12: three coverage axes, a closed return
  basis, the rule-24 record present; `fee_amount_reason` is a one-value null reason redundant with `dim_return_method.fee_basis`,
  left to the CVO's grade. The two orders were amended to cite it @b116670d7c.
- **Andrew-direct at 2.0.0_SA_COO~D, ~21:0xZ** (record `org/tier1_exec/2.0.0_SA_COO~D/deliverables/ANDREW_DIRECT_20260930_210xZ_FCASH_FOLD_YES_PROD_PROMOTE_YES_GO.md`),
  verbatim "2yes, 1yes, go": FCASH folds into the one Cash row; portal DEV to PROD after his localhost:5174 re-smoke, routed to MSTR.
  No act of this seat's.

## Call closed: site Z's safe-apply naming-limb decision (relay 103399, row NFRA_MCPMSP-Z-W2-S3) @2ee337baf8

Measured: both naming stages in `.tools/safe-apply.sh` ignore `-target` (the plan stage re-plans with none of the caller's
arguments). Ruled: grade the apply's OWN change set; the plan stage renders the same plan the apply runs (the caller's plan-shaping
arguments, or the given planfile) and binds for targeted or planfile applies; the pre-plan stage is WARN there; untargeted applies
unchanged; a targeted plan that cannot render refuses in ENFORCE; a five-arm self-test before it lands; site Z may cut it in
NFRA_MCPMSP; enforcement unchanged until then. Relayed through 0.0.0_AB_MSTR (22:29Z).

## Call closed after the tick: S237's blast radius (~P 103402, row IRPT_BCKEND-W100-S2)

The false +56% day propagates through the ADVI perfrp account leaf (`platinum/advi/49financial/perfrp_performance_account.json`,
as_of 2026-09-01: SI 0093614544 +69.81% vs +8.47% corrected; 0027256463 -83.34% vs +28.47%), not through the IRPT adapter, which reads
the holdings gold only. Measured here: `AdvisorBookView.tsx:479` calls `getPerfrpPerformanceLeaf('account')` live; the "404 in every live
environment" comment at `advisor-intelligence.ts:1647` is a claim. RULED (23:08Z): one read-only request through the served route first.
404 -> contained; W100-S2 disarms as unserved; the remedy parks on ADVI_PERFRP (owner 2.0.0_SA_COO) until Andrew lifts the D2 hold he set
by name. 200 -> a served wrong figure; the remedy needs his word on that hold and both halves. IRPT carries nothing further.

## Verdicts received: 0. Completion test

NOT DONE, unchanged (D0 5/5 closed; D2 2/10; D3 0/1; D7 0/1; D8 1/9; D9 1/11; D10 UNMEASURABLE; D11 4/4; D13 0/3; D14 1/4).
UNREACHABLE(lane dark): LGIC_ENFORCE, LGIC_CANON, LGIC_LGCTFM; SC-e12 parked (CloudOps). ACTS ONLY ANDREW CAN DO: the CloudOps
relaunch (LD-0305); the next CLOUD push after MSTR integrates (LD-0367/0368); the portal PROD promote's re-smoke (his own word).

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| directives-check / sequence-check | split calls x3 | 10 of 15; 10 placed |
| json read (python) | the new contract's keys and required fields | ruling 12 met |
| sed / comp-read / comp-find | `safe-apply.sh` naming stages, `naming-apply-gate.py` modes | both stages located; neither passes `-target` |

-- 1.0.0_SA_CTO
