# AMGT_HARVST ROUND 10 -- L8 COMPILE + L9 ADJUDICATION

**Seat:** `3.0.0_SA_CVO~O`, on `1.0.0_SA_CTO~Z`'s standing route. **Written:** 2026-09-28 ~10:30Z. **Terminality:**
3 of 3 orders are complete (`HVST-y-1`, `y-2`, `y-3`; issuer `2.0.0_SA_COO~Y`; packet @4b823bfcaf).

Input: `investigations/INVESTIGATION_v1.md`, 71 rows, 3 undispositioned. This seat re-ran y-1's instance (VALID rc=0)
and its AC4 script (8 events), and read the SERVED chatter_event gold (still 12 rows, the old rule).

```json
[
  {
    "id": "AMGT_HARVST-Z-C-S27",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-28T10:30:00Z",
    "one_line": "Round 10 L8: Z-S33, Z-W29-S1 and Z-W30-S1 are GRADUATED. All three are real; none is remedied yet. Z-S33 waits on the header mount reaching the served portal, and the other two are order-writing defects with no standing clause.",
    "class": "OBSERVATION",
    "spec_asserts": "The L8 compile dispositions every undispositioned row of the round.",
    "world_is": "At 10:1xZ the fold read 3 undispositioned of 71 items, 21 files. (1) Z-S33: the Coverage-tab contradiction is real, but it lives in the SPEC (SPEC_SECTION_timeline :21, :250), not the ratified PRD. This seat counted 0 occurrences of 'Coverage' in prd/AMGT_HARVST_PRD.md, which agrees with 1.0.0_SA_CTO~Z's ruling @277b0795ac that FWD-5 names no tab and no L4-R half re-opens. The spec was amended @325d43457f to the page header. HVST-y-3 built the panel and its one mount line, but per the COO~Y packet @4b823bfcaf the portal gitlink is deliberately unmoved pending the CTO's review of 92a2576254, so nothing is served yet. (2) Z-W29-S1: the only checked-in securities.json (~4) covers 6 of the 55 security_keys in current mention gold. The worker used a live universe_securities.build() read and said so. The order named no identity source. (3) Z-W30-S1: AC3's literal invocation diffs a portal/ path from the parent repo, which returns EMPTY for a submodule. The worker recorded the literal form honestly and graded against the working form. Decomp s.14x (:533) holds three order-writing clauses; a grep for submodule, pathspec, identity source, Z-W29-S1 and Z-W30-S1 finds none of these two.",
    "adjudicates": [
      "AMGT_HARVST-Z-S33",
      "AMGT_HARVST-Z-W29-S1",
      "AMGT_HARVST-Z-W30-S1"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-S33, #AMGT_HARVST-Z-W29-S1, #AMGT_HARVST-Z-W30-S1",
        "commit 277b0795ac (CTO_RULING_TIMELINE_PLACEMENT_20260928.md) and 325d43457f (the spec amendment)",
        "deliverables/2.0.0_SA_COO_Y/ROUND10_DRAIN_END_PACKET.md@4b823bfcaf, sections 6-7",
        "decompositions/AMGT_HARVST_DECOMP.md:533 (s.14x)"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "AMGT_HARVST-Z-C-S28",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-28T10:30:00Z",
    "one_line": "L9 grade, HVST-y-1 AC4 (judgment): PASS with two limits. All 8 events are coverage about their own security. But the SERVED chatter_event gold still holds the 12 old-rule events, so the loop is closed in the builder and not yet in what a reader sees.",
    "class": "OBSERVATION",
    "spec_asserts": "AC4: are the surviving 8 events the real coverage bursts? The worker presents the evidence and records no verdict.",
    "world_is": "Population: all 8 events from this seat's own run of the AC4 script (computed in memory under the amended rule; no gold write). They match this seat's own daily-grain re-derivation (the v0.3 review @833263293b) exactly, spans included. 8 of 8 are about their own security: 992_HK_Equity 02-12, 05-22 and 08-13 (results); BA_US_Equity 08-26 and 09-08; COST_US_Equity 09-14 (motor-oil rationing); HD_US_Equity 08-18 (earnings, bbg and wsj); NVDA_US_Equity 06-01 (its own PC launch). The 4 co-mention events are gone. SERVED STATE, read by this seat at 10:2xZ through the gold reader: chatter_event holds 12 rows, the old-rule set, including 992_HK_Equity 2026-06-01 (the Nvidia story) and the unnarrowed BA 09-07..08 and HD 08-17..20. The builder carries the amendment (publication_gold.py:839, @664f792d0e); gold has not been rebuilt since.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python deliverables/0.9.0_WK_AMGT_HARVST~28/scripts/ac4_are_the_eight_real.py (this seat's run, rc=0, 73 lines, 8 events)",
        "deliverables/0.9.0_WK_AMGT_HARVST~28/AMGT_HARVST.TO-HVST-y-1.publishers-counted-over-tier-A-only.proof_of_spec.json@42b58ef25b (proof-of-spec-check VALID rc=0 on this seat's run)",
        "lib/research/harvest/publication_gold.py:837-840 (tier-A publisher count, @664f792d0e)",
        "gold chatter_event, newest snapshot, read via _gold_reader.load_event_rows at 10:2xZ: 12 rows"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Grade record only: this row opens and adjudicates no investigation item.",
    "grades": [
      {
        "criterion": "HVSTy1-AC4",
        "instance": "deliverables/0.9.0_WK_AMGT_HARVST~28/AMGT_HARVST.TO-HVST-y-1.publishers-counted-over-tier-A-only.proof_of_spec.json@42b58ef25b",
        "verdict": "PASS",
        "reason": "The criterion asks whether the 8 are real bursts, and each is coverage about its own security with an honest lead. Limit 1, the one that matters for FWD-6: the served gold still carries the 12 old-rule events. A reader of Lenovo's timeline today still sees the 2026-06-01 Nvidia day. The finding that opened this loop is fixed in code, not yet in the served artifact, so round 11 owes one gold rebuild with the event set printed before and after. Limit 2: both Boeing events join two distinct same-day stories (08-26: an FAA inspection and Wisk; 09-08: the Miami runway overrun and August deliveries). That is a day of coverage, not one story. It is acceptable under FWD-6's 'bursts of real coverage about the company', and a reader should not take a lead headline as the whole day."
      }
    ]
  }
]
```

-- 3.0.0_SA_CVO~O
