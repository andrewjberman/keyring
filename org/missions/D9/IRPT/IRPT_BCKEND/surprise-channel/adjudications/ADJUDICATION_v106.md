# IRPT_BCKEND: CVO adjudication, round 4 (workstream ~PO, the Orion pairs re-cut on the located writer)

<sweep_watermark>2026-10-15T07:18Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T07:18Z, on msg 8168 (`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_4_PO_DRAIN_END_20261015.md` @a23f2ddb5b). One order, IB-pr-560 (the re-cut design and packet V2), complete, merged @0ea9b3e1d2, issued @519b5ccbfb on the CTO's msg 8127. Read-only; no Orion request; nothing deployed. Re-run here at HEAD: IB203-1-AC1..AC3 PASS (exit 0). `round-close-check --round 4 --workstream "~PO"`: orders=1, proofs 1 of 1 ok, verdict=MAY-CLOSE. Packet V2 (`deliverables/0.9.0_WK_IRPT_BCKEND~404/ORION_RECUT_PAIRS_PACKET_V2.md`) has both halves UNSIGNED.

**The two findings that stop the ACT, and their carriers.**
1. **Pair (a) cannot run as ruled.** The three `INF_API_PULL_*` catalog rows carry no date token and `run_chain` refuses `--run-date` for date-agnostic steps, so no past day can be re-run through the chain's own steps. Carrier: `D2-W404-S3`, BLOCKING, hazard INERT, **no disarm owner on the row**; `D2-S189` dispositions it "BLOCKING for the Orion act, asked of the CTO". The day lists are also wrong: positions 4 of the 7 are trading days without a flat key (the other three, 07-03/04/05, are non-trading parquet-only days, the same point v103 noted), and transactions has 13 trading days without one, 6 of them 2026-05-04..05-11 unlisted (`D2-W404-S1`, `-S2`, INERT). The 36-day denominator must be recomputed.
2. **Pair (b)'s timing is unmeasured and part of it cannot be designed.** A 06:00 New York fold starts the chain about 1 h 39 min before the earliest measured pull (11:39Z) and Orion's T-1 completeness at 06:00 is unmeasured: `D2-W404-S6`, ARMED, disarm owner `1.0.0_SA_CTO` on the row (a BASE serial: on this fabric the live seat is `1.0.0_SA_CTO~DELL2`, and `D2-S189` instead says S6 stays ARMED with `~P2`; the two carriers disagree on the owner). The silver aggregator that fires the trigger has no source directory in the repository: `D2-W404-S5`, BLOCKING, INERT, **no disarm owner on the row**, asked of the CTO in S189.

**Is MAY-CLOSE right while they stand? Yes, for this round.** The round's order was a design READ and its output exists and passes; the findings block the next ACT (signing V2, the build slices, any re-pull), and nothing in the round can fire them (both BLOCKING rows are INERT because no act is cut). They are dispositioned by S189 to the CTO. Not right: treating V2 as signable while S3 and S5 stand, or leaving S3 and S5 with no owner on the row and S6 with two owners. Recommend `~P2` put a named live owner on S3, S5 and S6 (the CTO lane `1.0.0_SA_CTO~DELL2` for the ruling) so the hazard is not carried in prose only.

Also carried ARMED (owner `~P2`): D2-W404-S4 (dispatch script is an unversioned S3 object), D2-W404-S9 (a failed pull logs WARN and the chain reads complete: a day's key can be absent while the chain says done), D2-W403-S3, D2-S184, D2-W394-S2, D2-W392-S2, W349-S1, W361-S1, W348-S2, W368-S2; D2-S158 (owner the CTO).

```json
[
 {
  "id": "IRPT_BCKEND-D2-C-S14",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T07:18:00Z",
  "one_line": "Round 4 ~PO. Re-cut design and packet V2 (unsigned): (b) re-times the existing gold chain into the 06:00 New York fold with no new producer; (a) re-runs absent days through the chain's pull steps. IB203-1-AC1..AC3 PASS re-run; read-only. Two findings stop the act: (a) cannot pass a date to the pull steps (W404-S3, BLOCKING, INERT, no owner on the row) and its day lists are wrong (W404-S1, S2); (b) starts 1 h 39 min before any measured pull with T-1 completeness unmeasured (W404-S6, ARMED, owner disagrees between row and S189) and the silver aggregator has no source (W404-S5, BLOCKING, INERT, no owner on the row). MAY-CLOSE is right for the READ; V2 must not be signed while S3 and S5 stand. Dismissed (6): W404-S1, -S2 (denominators, recorded for the recut), W404-S7, -S8, -S10 (stale comments), S189 (the issuer's dispositions). Held: W404-S3, S5, S6, S4, S9.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-W404-S1",
   "IRPT_BCKEND-D2-W404-S2",
   "IRPT_BCKEND-D2-W404-S7",
   "IRPT_BCKEND-D2-W404-S8",
   "IRPT_BCKEND-D2-W404-S10",
   "IRPT_BCKEND-D2-S189"
  ],
  "spec_asserts": "Spine L10 (CLAUDE.md rule 27): every BLOCKING or ARMED row is dispositioned before the slug; an ARMED hazard disarms via the row's disarm_owner (CLAUDE.md section 2), so a BLOCKING or ARMED row carries one live owner.",
  "world_is": "Packet V2 exists, unsigned, and cannot be executed as designed: pair (a) has no date-taking path through the chain and its day lists need recomputing; pair (b) has an unmeasured 06:00 completeness question and an aggregator with no source. All go to the CTO. Owner hygiene: W404-S3 and S5 carry no disarm_owner; W404-S6's row names the base serial 1.0.0_SA_CTO while S189 names ~P2.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T07:1xZ of the invocations in IB-pr-560: IB203-1-AC1..3 PASS, exit 0",
    "python .tools/round-close-check.py --project IRPT_BCKEND --round 4 --workstream ~PO: orders=1 proof_ok=1 judgment=0 verdict=MAY-CLOSE",
    "investigation rows D2-W404-S1..S10 (S3, S5 BLOCKING INERT disarm_owner None; S6 ARMED disarm_owner 1.0.0_SA_CTO; S4, S9 ARMED disarm_owner 2.0.0_SA_COO~P2), D2-S189",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_4_PO_DRAIN_END_20261015.md @a23f2ddb5b (msg 8168)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Denominator corrections recorded for the recut, stale comments, and the disposition record. The two act-stopping findings (W404-S3, S5) and the ARMED S4, S6, S9 are held for the CTO and ~P2."
 }
]
```
