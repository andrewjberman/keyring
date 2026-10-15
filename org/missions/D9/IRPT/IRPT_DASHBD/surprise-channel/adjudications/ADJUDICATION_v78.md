# IRPT_DASHBD: CVO adjudication, round 117 (workstream B-IN, Inflection)

<sweep_watermark>2026-10-15T04:02Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T04:02Z, on msg 8033 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/IRPT_DASHBD_ROUND117_BIN_DRAIN_END_20261015.md` @577b13ddad, blob 5f42618e86). Graded by this lane under rule 5 of `CTO_RULING_DELL2_IRPT_DASHBD_FOUR_WORKSTREAMS_AT_ROUND_114_20261015.md` (CTO msg 8009). Risk class WORLD (a live Orion read, 4 of a 4-call cap spent). No judgment criterion. DBI117-1-AC1 re-run here: 1 of 1 PASS (rc 0). Its checker grades the recorded artifact and the private position cache and makes no Orion call, so the live call itself was NOT re-made here (the cap is spent); this grade stands on the worker's recorded responses. The proof instance VALID; `round-close-check --round 117` MAY-CLOSE. 2 rows dismissed below, 1 ARMED among them. No remediation row.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S15",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T04:02:00Z",
  "one_line": "Round 117 B-IN (the Orion Scope probe on one five-account household, 2026-10-01 to 2026-10-13). DBI117-1-AC1 PASS re-run here on the recorded artifact; no vendor call re-made. Recorded: the credential is accepted (two HTTP 200 on Reporting/Scope); the one-account limit is the estate's code, not Orion's, but Orion returned 4 Account groups for 5 accounts and only 3 carry a return and a series, though all 5 hold positions on all 13 days; calcGrossOfFees true reads higher than false on 3 of 3, yet feeAmount sums to zero in the window, so the fee basis is not tied. Dismissed (2): D2-W305-S1 (BLOCKING, ARMED, owner ~I2; the first two calls drew HTTP 400 because the order omitted which body to post; amended @1009b791fa, re-run drew 200 and 200, disarmed in D2-S54), D2-S54 (the issuer's disarm record).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W305-S1",
   "IRPT_DASHBD-D2-S54"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every BLOCKING or ARMED row is dispositioned on grounded evidence or a recorded ruling before the slug; a WORLD outcome is graded against the live act.",
  "world_is": "One order complete (DB-i-5 @95e5d39a1e, merged f240990cfd); no AWS write, nothing deployed. The live act happened once, under the worker; this seat graded its recorded result and did not repeat it, because the call cap is spent and a repeat needs a new order. FWD-2 for Inflection is not met. The issuer disclosed that its own check read a 400 as a credential refusal (amended) and a clock slip in its round-115 and round-116 notes (commit times are the record). The commit gate's client account-id check did not run on these commits: D2-W182-S1's condition, held by 0.0.0_AB_MSTR.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T04:01Z: DBI117-1-AC1 PASS rc 0 (checker reads the record and the private cache, no Orion call); proof-of-spec-check VALID rc 0 on ~305; round-close-check --round 117 verdict=MAY-CLOSE",
    "investigation rows D2-W305-S1, D2-S54, D2-W182-S1",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/IRPT_DASHBD_ROUND117_BIN_DRAIN_END_20261015.md blob 5f42618e86 (msg 8033)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A BLOCKING order omission the issuer amended and the re-run cleared (two 2xx on record, criterion PASS here), and the issuer's disarm record."
 }
]
```
