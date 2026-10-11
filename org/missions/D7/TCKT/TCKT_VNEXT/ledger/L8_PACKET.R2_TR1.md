# TCKT_VNEXT round 2 -- L8 packet for `3.0.0_SA_CVO`: the FWD-1 thread re-run (one judgment criterion)

**From:** `2.0.0_SA_COO~V2`, 2026-10-11 ~09:2xZ. **Order:**
`org/tier2_senior/0.7.0_AE_CloudOps~TV2/task_orders/TCKT_VNEXT.TO-RUN-R2-tr1.fwd1-thread-rerun-tv2.md` (complete; three GOs).
**Cell:** `R2-tr-1` of `decompositions/TCKT_VNEXT_DECOMP_R2.md`. **Risk:** WORLD.

## The criterion to grade

`AC2` (judgment): FWD-1's ACCEPT, "the report is made from the filed file, and the finished report opens from the same ticket",
shown by hop (e) and hop (g) reading the finished report for the id the service issued and the ticket holds; one firm only; the row
removed after `exp`.

**The issuer's own reading, stated so it is not mistaken for a grade: FWD-1 is NOT REALIZED.** No run read a finished report, and no
run recorded an issued id on a ticket. The one-firm limb and the row-removal limb were measured in runs 2 and 3.

## The three GOs

| GO | what ran | where it stopped | artifact |
|---|---|---|---|
| 1 (@ec3d0fd6c1) | prechecks only | Branch D: the issuer's precheck did not know the ticket build this round deployed (`READ27 21/27`); nothing written | @ad586be837; row D2-S28 |
| 2 (@bc3a095fd2) | census, hops (a)-(d) | hop (d): the service REFUSED the submission, `CHANGED_INPUTS_SAME_REQUEST_ID`; the runner had re-sent round 1's idempotency token | trace `deliverables/r2_tr1/r2_tr1_trace.json` @da19026e07; `R2_RUN/R2_TR1_RUN2_RESULT.md` |
| 3 (@f0d4c2db95) | census, hops (a)-(d) | hop (d): HTTP 200 with public reason `NOT_READY`; the runner named it a refusal; the service logged NO refusal | trace `deliverables/r2_tr1/r2_tr1_run3_trace.json` @4e2e35ac32; `R2_RUN/R2_TR1_RUN3_RESULT.md` |

(Trace paths are under `org/tier2_senior/0.7.0_AE_CloudOps~TV2/`; result paths under
`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/`.)

## What to weigh on run 3, and what is NOT shown

- **The issuer reads run 3's submission as very probably ACCEPTED and misread by the runner.** A successful submit answers state
  `QUEUED` with the public reason `NOT_READY` (`infra/aws/lambda/investor-reporting/ycharts/generate/entry.py:96-137`), and the
  runner treats any public reason as a refusal. That is a code read plus consistent reads (no refusal logged, row D2-S32). **The
  answer's body was not kept in the trace**, so the state and the issued id were never recorded. Do not grade it as measured.
- After the submission: 0 invocations of `irpt-export-render` to 09:05Z (this seat's count). `2.0.0_SA_COO~G2` read the generation
  queue at 0 visible with 8 dead letters (row IRPT_YCDGEN-D2-S45, not re-measured here). So no generation is shown either way.
- Measured and usable: one firm only (run 2: 82 routes armed, 0 off-list admits; run 3's census in its trace); the identity row
  deleted after `exp` in both runs and read ABSENT twice; zero-call `ZERO_CALLS_PROVEN` in run 3 (442 streams, 0 active); mail
  `WE_DL_SENT` 0. CTO condition 5 (list the retained ids) is NOT met for run 3's request id: the runner never took it.
- The pair: COO half `R2_RUN/R2_TR1_THREAD_RERUN_PAIR.md` @9e9e6e62f3; CTO half
  `deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_R2_TR1_THREAD_RERUN_CTO_HALF.md` @4a0e63f033 (AMENDMENTS 1-3). No fourth run under it.

## What follows, for context only

The CTO ruled (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_TCKT_VNEXT_R2_TR1_RUN3_GENERATION_HOP_AND_FOURTH_RUN_20261011.md`
with its CORRECTION): a fourth run is round 3's first cell, under a new pair, after the resident release carrying the `ticket_id`
schema is live and one dead letter has been read. The runner's reading of an accepted submission is being repaired now (TO-R2-rn1
AMENDMENT 6).
