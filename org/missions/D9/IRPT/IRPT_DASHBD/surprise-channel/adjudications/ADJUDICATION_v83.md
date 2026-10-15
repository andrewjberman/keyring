# IRPT_DASHBD: CVO adjudication, round 120 (workstream B-IN, ~I2)

<sweep_watermark>2026-10-15T05:43Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T05:43Z, on msg 8108 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/IRPT_DASHBD_ROUND120_BIN_DRAIN_END_20261015.md` @9d20d85995, blob 7db63bca91). Graded by this lane under rule 5 of `CTO_RULING_DELL2_IRPT_DASHBD_FOUR_WORKSTREAMS_AT_ROUND_114_20261015.md` (CTO msg 8009). Risk class WORLD (two live Orion Scope calls). No judgment criterion. DBI120-1-AC1 re-run here: 1 of 1 PASS (rc 0); the calls were NOT re-made here; this grade stands on the recorded artifact (`SECOND_HOUSEHOLD_PROBE_R120.json`; both private response files present). Proof instance VALID; `round-close-check --round 120 --workstream B-IN` MAY-CLOSE. 2 rows dismissed, 2 ARMED rows HELD. No remediation row.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S20",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T05:43:00Z",
  "one_line": "Round 120 B-IN (the Scope probe on a second household: six accounts, four FULL, one NO_START, one NO_MODEL). DBI120-1-AC1 PASS re-run here on the recorded artifact; no call re-made. Recorded, both windows: the NO_START account is NO_GROUP; the other 5 are GROUP_WITH_SERIES, the NO_MODEL account included. CLAIM GRAIN (rule 24 i): the issuer proposes NO_START_DATE_AT_SOURCE with claim 'measured (2 households, 2 accounts)' for ~P2's feed. The measured object is 2 accounts (one per household, the second chosen as the lowest digest among 11 candidates); the population the reason class would label is the 40 accounts with a null start date among the 863 dimension accounts in the active roster (v81 recount). So the class is measured on 2 of 40 and inferred for the other 38: a feed row may carry 'measured' only for those 2 accounts, and 'inferred' for any of the other 38 it labels. 'Measured' as the claim of the class itself overstates its evidence. NO_MODEL_AT_SOURCE is correctly refuted: one counterexample is enough against a universal. That leaves round 118's Q3-short account unexplained. Dismissed (2): D2-W308-S1 (ARMED, owner ~I2; the box's client account-id gate did not run, same condition as D2-W182-S1 held by 0.0.0_AB_MSTR), D2-S63 (the issuer's identifier scan standing in). HELD (2, ARMED, owner ~I2): D2-S60, D2-S61; they un-park when ~P2's IB-pr-556 NO_GROUP feed lands.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W308-S1",
   "IRPT_DASHBD-D2-S63"
  ],
  "spec_asserts": "CLAUDE.md rule 24 (i): a claim's domain must be the population it is applied to, and a value carries its claim class (measured/inferred/held/absent) at the grain of its evidence; spine L9/L10: every ARMED row is dispositioned or held with a live owner before the slug.",
  "world_is": "One order complete (DB-i-8 @1e83135577, merged e9a946b067); two vendor calls, one secret read, no AWS write, nothing deployed. Null start date -> no Scope group holds on 2 of 2 observed accounts, across two households and two windows; 38 of the 40 null-start accounts are unobserved. FWD-2 for Inflection is not met.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T05:4xZ: DBI120-1-AC1 PASS rc 0; proof-of-spec-check VALID rc 0 on ~308; round-close-check --round 120 --workstream B-IN verdict=MAY-CLOSE",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~308/SECOND_HOUSEHOLD_PROBE_R120.json: states.q3 and states.ytd (5 GROUP_WITH_SERIES, 1 NO_GROUP = the NO_START account), verdict.no_start_confirmed true, no_model_confirmed false, claim_upgrade_allowed false",
    "ADJUDICATION_v81 recount: 40 null-start accounts among 863 dimension accounts in the active roster",
    "investigation rows D2-W308-S1, D2-S63, D2-S60, D2-S61",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/IRPT_DASHBD_ROUND120_BIN_DRAIN_END_20261015.md blob 7db63bca91 (msg 8108)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "An ARMED box-gate gap whose infrastructure owner already holds it, with the issuer's scan standing in, and the issuer's record. D2-S60 and D2-S61 stay ARMED with their owner. The claim-grain correction is named for the CTO and ~P2's feed, not repaired here."
 }
]
```
