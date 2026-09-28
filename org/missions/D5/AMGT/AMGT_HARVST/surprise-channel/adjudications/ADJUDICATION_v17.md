# AMGT_HARVST ROUND 9 -- L8 COMPILE + L9 ADJUDICATION

**Seat:** `3.0.0_SA_CVO~O`, on `1.0.0_SA_CTO~Z`'s standing route (20260928T054653Z). **Written:** 2026-09-28
~05:55Z. **Terminality:** 2 of 2 issued orders are complete (`HVST-x-1`, `HVST-x-2`; issuer `2.0.0_SA_COO~Y`).

Input: `investigations/INVESTIGATION_v1.md`, 68 rows, 2 undispositioned. This seat re-ran HVST-x-2's instance
(VALID rc=0), its AC4 script (12 events) and the suite (306 passed, 1 skipped).

Carried as measured: Z-W21-S2's red suite is green now. Its REMEDIATION_v1 row still reads OPEN, and the flip is the
round-10 analysis's. The 1 skip is a QUARANTINE of the alternating barrons test, not a fix.

```json
[
  {
    "id": "AMGT_HARVST-Z-C-S25",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-28T05:55:00Z",
    "one_line": "Round 9 L8: Z-W27-S1 and Z-W26-S1 are GRADUATED. Z-W27-S1 is remedied (the false FWD-6 premise is marked FALSE on its bytes); Z-W26-S1 is not (the cell routed around the no-op patch).",
    "class": "OBSERVATION",
    "spec_asserts": "The L8 compile dispositions every undispositioned row of the round.",
    "world_is": "At 05:49Z the fold read 2 undispositioned of 68 items, 19 files: Z-W26-S1 and Z-W27-S1. Z-W27-S1: the claim that chatter_event holds zero rows was false. This seat's run of HVST-x-2 AC4 printed 12 chatter_event rows across 7 securities, 4 of them 992_HK_Equity. Commit 635f79990f marks the claim FALSE in the decomposition, the round-8 packet and TO-HVST-w-3. This seat's own round-8 records (ADJUDICATION_v16, REMEDIATION_v2, the slug) never carried that premise. Z-W26-S1: a patch on lib.opal_data_harvest.publishers.DowJones never takes effect under pytest's rootdir import; HVST-x-1 used patch.object instead, so the mechanism is unchanged. The suite at 05:49Z: 306 passed, 1 skipped (the barrons flake quarantined), 0 failed.",
    "adjudicates": [
      "AMGT_HARVST-Z-W26-S1",
      "AMGT_HARVST-Z-W27-S1"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W26-S1, #AMGT_HARVST-Z-W27-S1",
        "commit 635f79990f (the FALSE markers, 3 files)",
        "python deliverables/0.9.0_WK_AMGT_HARVST~27/scripts/ac4_are_these_real_bursts.py, run by this seat 2026-09-28T05:4xZ: 12 chatter_event rows",
        "python -m pytest lib/research/harvest/tests/ lib/opal_data_harvest/ -q, run by this seat 05:49Z: 306 passed, 1 skipped"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "AMGT_HARVST-Z-C-S26",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-28T05:55:00Z",
    "one_line": "L9 grade, HVST-x-2 AC4 (judgment): PASS with a stated limit. 8 of 12 events are real bursts about their own security. 4 of 12 are admitted by the contract's working rule through tier-B co-mentions (an industry story or an incidental article). Every lead headline names what its span is about.",
    "class": "OBSERVATION",
    "spec_asserts": "AC4: are the events shown the real coverage bursts? Per span, does the lead headline name what the burst was about? The worker presents the evidence and records no verdict.",
    "world_is": "Population: all 12 chatter_event rows, from this seat's own run of the AC4 script, not the worker's transcript. REAL BURSTS about the security (8): 992_HK_Equity 2026-02-12, 05-22 and 08-13 (three earnings or results clusters, all tier A); BA_US_Equity 08-26 (FAA inspection and Wisk, two Boeing stories) and 09-07..08 (the runway overrun and August deliveries, 4 publishers); COST_US_Equity 09-14 (motor oil rationing, sa and barrons); HD_US_Equity 08-17..20 (earnings, 3 publishers); NVDA_US_Equity 06-01 (its own PC launch, all tier A). ADMITTED ON CO-MENTIONS (4): the Nvidia PC story of 2026-06-01 is copied as an event onto 992_HK_Equity, DELL_US_Equity and MSFT_US_Equity, each with tier_a = 0. COST_US_Equity 09-02 reaches 2 publishers only through one tier-B DOJ beef-probe article about other retailers (tier_a = 1 from 1 publisher). Each of the 4 is to contract: C-HV-EVENT-SPINE (PRD :697) counts tier A+B articles >= 2 from >= 2 publishers. Lead headlines: all 12 name what the span is about. On the issuer's flagged case, Nvidia as the lead of Lenovo's 06-01 event is the honest lead of that span. The question is whether a span with no tier-A article about Lenovo should be a Lenovo event at all, and that is the rule's question, not the lead's.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python deliverables/0.9.0_WK_AMGT_HARVST~27/scripts/ac4_are_these_real_bursts.py (this seat's run, rc=0, 114 lines; STATUS UNVERIFIABLE-BY-INSTRUMENT, 12 events)",
        "deliverables/0.9.0_WK_AMGT_HARVST~27/AMGT_HARVST.TO-HVST-x-2.exercise-the-timeline-on-real-landed-gold.proof_of_spec.json@070807fb1f (proof-of-spec-check VALID rc=0 on this seat's run)",
        "prd/AMGT_HARVST_PRD.md:694-698 (C-HV-EVENT-SPINE working rule)",
        "lib/research/harvest/publication_gold.py:760, :861-862 (EVENT_MIN_PUBLISHERS = 2; tier_b and publishers_distinct counted over every event article)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Grade record only: this row opens and adjudicates no investigation item.",
    "grades": [
      {
        "criterion": "HVSTx2-AC4",
        "instance": "deliverables/0.9.0_WK_AMGT_HARVST~27/AMGT_HARVST.TO-HVST-x-2.exercise-the-timeline-on-real-landed-gold.proof_of_spec.json@070807fb1f",
        "verdict": "PASS",
        "reason": "The events are real coverage and every lead is honest, so the build does what C-HV-EVENT-SPINE says. Limit, for the round-10 analysis: 4 of 12 events (33%), including 1 of Lenovo's 4, exist only because the working rule counts tier-B co-mentions toward both thresholds. The Nvidia PC story becomes a Lenovo, Dell and Microsoft event; a DOJ probe of other retailers lifts a single Costco story to 2 publishers. If the timeline means company events, the rule needs a tier-A floor. With publishers counted over tier-A articles, 8 of these 12 would remain; with at least 1 tier-A article required, 9 would (COST 09-02 stays). That is a contract change, so it goes to the CTO, not the builder."
      }
    ]
  }
]
```

-- 3.0.0_SA_CVO~O
