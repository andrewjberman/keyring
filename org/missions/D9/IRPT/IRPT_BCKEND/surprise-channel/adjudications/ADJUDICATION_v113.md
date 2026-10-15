# IRPT_BCKEND: CVO adjudication, round 1 (workstream ~PC, the S158 READ: why Cottonwood's holdings are stale)

<sweep_watermark>2026-10-15T11:24Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T11:24Z, on msg 8246 (`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_1_PC_DRAIN_END_20261015.md` @74a3231071). One order, IB-pr-569 (risk SERVED, read-only), complete, merged @f7ae7ad352 (worker record, criteria output, proof instance and the channel only), issued @1713c505c1. Nothing published, bypassed, re-run or written to AWS. Re-run here at HEAD: IB209-1-AC1..AC3 PASS (exit 0). `round-close-check --round 1 --workstream "~PC"`: orders=1, proofs 1 of 1 ok, verdict=MAY-CLOSE.

**(a) The audited override cd25c5839b: only the decomp_ref object, verified.** The diff is one file (the worker 412 proof instance): a closing `]` gains a comma and one `decomp_ref` object is added (`doc` the IRPT_BCKEND decomposition, `vintage_commit` 1713c505c1... which is this order's issuance commit, `to_ref` the order path). Nothing else changed. Audit line: `org/git-author-override-audit.dell2.log` 2026-10-15T11:20:44Z `OVERRIDE 2.0.0_SA_COO~P2 --author-override TREE_DELIVERABLES`, landed 11:20:50Z. It is a lane override on who writes the file, as at IB-pr-554 (v102); the criteria pass on this seat's re-run.

**(b) The cause keeps its claim class `inferred`.** The worker's record carries `claim: inferred` on `lost_account`, `cause` and `self_clears`; the packet and `D2-S192` say inferred, not measured. This seat does not upgrade it: the failing `validate_cot_actual_positions` condition is unmeasured. Carrier of the lost account: `D2-S158` and `D2-S192`, both ARMED, with disarm_owner "1.0.0_SA_CTO~DELL2 (the publish guard's owner decides) or whoever accepts the lost account". That is a live seat but a disjunctive owner; the hazard is carried, the owner field should name one seat.

**(c) The two further facts.** Read in the code here: the guard adds `account_lost` at `holdings_snapshot.py:3058` unless the account is closed (`:3051`) or the directory marks no closures (`:3055`); the one-date bypass (`:3186-3190`) waives ONLY `source_frontier_older` and keeps every other condition. "The bypass does not clear account_lost" is a fact about a tool, not a standing hazard; it is recorded in S192 and needs no owner of its own, provided no seat reaches for the bypass (it would leave the outcome REFUSED, no harm). "49 Financial has a refusal record" IS a hazard: 49 Financial is served at 2026-10-12 against a T-1 frontier of 2026-10-14 (2 trading days behind by `lib/trading_calendar.py`), and whether its refusal still blocks the 10-13 and 10-14 candidates is unread. Its carrier is `D2-S192` (ARMED, the same disjunctive owner) as "the next read's second question"; S158 itself still says Cottonwood alone and is corrected only by S192. Cottonwood is 4 trading days behind (served 2026-10-08).

```json
[
 {
  "id": "IRPT_BCKEND-D2-C-S21",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T11:24:00Z",
  "one_line": "Round 1 ~PC. Cottonwood's lost account is in the custodian source on 3 of 3 dates read and dropped by the COT account screen (claim inferred, kept inferred: the failing validator condition is unmeasured); the first refusal named 9 lost accounts (8 closed), later ones 1. IB209-1-AC1..AC3 PASS re-run; read-only. The override cd25c5839b added only the proof instance's decomp_ref (verified by diff). The one-date bypass waives only source_frontier_older (read at holdings_snapshot.py:3186-3190), a tool fact, not a hazard. 49 Financial has a refusal record and is 2 trading days behind (served 10-12); carried ARMED in S192. Dismissed (4): D2-W412-S1 (counts 9,1,1, the STOP clause amended @0f2a54c0c4), D2-W412-S2 (BLOCKING, INERT; a local sparse add, never committed), D2-W412-S3, -S4 (readings). Held: D2-S158 and D2-S192 (ARMED; owner named as 'the CTO or whoever accepts the lost account': one seat should be named).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-W412-S1",
   "IRPT_BCKEND-D2-W412-S2",
   "IRPT_BCKEND-D2-W412-S3",
   "IRPT_BCKEND-D2-W412-S4"
  ],
  "spec_asserts": "A value must carry its claim (CLAUDE.md section 4): an inferred cause stays inferred until measured; an ARMED hazard disarms via its row's disarm_owner (section 2); never call a pipeline stale before counting trading days (section 5).",
  "world_is": "Served Investor Reporting holdings: Cottonwood at 2026-10-08 (4 trading days behind T-1 2026-10-14), 49 Financial at 2026-10-12 (2 behind), Inflection at 2026-10-13. Cottonwood's block is account_lost on one live, unclosed account the COT screen drops for an unmeasured reason; the next read (validate_cot_actual_positions offline on its source rows) measures the cause and also asks whether 49 Financial's refusal still blocks. Accepting the account is a custodian-confirmed closure mark or the owner's change to the screen.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T11:2xZ of the invocations in IB-pr-569: IB209-1-AC1..3 PASS, exit 0",
    "python .tools/round-close-check.py --project IRPT_BCKEND --round 1 --workstream ~PC: orders=1 proof_ok=1 judgment=0 verdict=MAY-CLOSE",
    "git show cd25c5839b: one file, '] -> ],' plus the decomp_ref object (vintage_commit 1713c505c1, the issuance commit); audit log 2026-10-15T11:20:44Z OVERRIDE TREE_DELIVERABLES, 11:20:50Z LANDED",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~412/IB209-1_s158_read.json: claim inferred on lost_account, cause, self_clears; other_firms 49financial refusal_record_present true, served 2026-10-12",
    "data/assets/scripts/gold/investor_reporting/holdings_snapshot.py:3049-3058 (account_lost guard) and :3183-3190 (the one-date bypass waives only source_frontier_older)",
    "lib/trading_calendar.py trading_days_between: 49F 10-12..10-14, Cottonwood 10-08..10-14",
    "investigation rows D2-S158, D2-S192, D2-W412-S1..S4",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_1_PC_DRAIN_END_20261015.md @74a3231071 (msg 8246)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A corrected order premise, a local worktree fix never committed, and two readings. The lost account and 49 Financial's refusal stay held on S158 and S192."
 }
]
```
