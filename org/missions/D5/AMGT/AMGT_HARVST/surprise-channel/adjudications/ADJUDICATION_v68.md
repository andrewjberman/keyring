# AMGT_HARVST -- round 76 L9 grade (dell1)

<sweep_watermark>2026-10-09T13:08Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-09T13:08:00Z. Asked by 2.0.0_SA_COO~W1 msg 2454. HVST-bt-1 AC4 MET: the samples support R31's retirement.

```json
[
  {
    "id": "AMGT_HARVST-D1-C-S1",
    "project": "AMGT_HARVST",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T13:08:00Z",
    "one_line": "HVST-bt-1 AC4 MET (graded by this seat): both census samples read, and the common-word list read. KEPT sample (20 pairs over 5 securities): 20 of 20 are about the company, each on a real second anchor (CDNS, ORANY, 'Booking Holdings', 'Visa Inc', 'Orange SA'). REMOVED samples: 24 of 26 sampled removals were TRUE mentions -- Booking 5 of 6 are Booking.com (the company's own brand; the sixth is 'Booking trends'), Cadence 9 of 10 are Cadence Design (the tenth is Cadence Bancorporation, a different company), Orange 10 of 10 are the telecom. So R31 removes far more true mentions than the false ones it fixes, which supports the CTO's ruling to retire it (ROUND_ANALYSIS.round74 ADDENDUM 7). The list (measured, LOWER/CAP_MID >= 0.2 over 20,908 articles) flags 5 of 413 aliases: Booking 1.0, Cadence 0.24, Orange 0.23 (x2), Visa 0.22. Wrongly caught: none as WORDS, but all five are brands whose capitalised use is overwhelmingly the company, so 'is a word' is the wrong test for removal. Missed: Monster (0.059) stays under the threshold, though its false pairs (a Godzilla review) were already removed by R30's lower-case rule; Apple 0.002, Meta 0.001, Intel 0.0007 are rightly not flagged.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9: JUDGMENT criteria are graded at L9 by a seat that did none of the work, never self-graded.",
    "world_is": "HVST-bt-1 AC4 MET (graded by this seat): both census samples read, and the common-word list read. KEPT sample (20 pairs over 5 securities): 20 of 20 are about the company, each on a real second anchor (CDNS, ORANY, 'Booking Holdings', 'Visa Inc', 'Orange SA'). REMOVED samples: 24 of 26 sampled removals were TRUE mentions -- Booking 5 of 6 are Booking.com (the company's own brand; the sixth is 'Booking trends'), Cadence 9 of 10 are Cadence Design (the tenth is Cadence Bancorporation, a different company), Orange 10 of 10 are the telecom. So R31 removes far more true mentions than the false ones it fixes, which supports the CTO's ruling to retire it (ROUND_ANALYSIS.round74 ADDENDUM 7). The list (measured, LOWER/CAP_MID >= 0.2 over 20,908 articles) flags 5 of 413 aliases: Booking 1.0, Cadence 0.24, Orange 0.23 (x2), Visa 0.22. Wrongly caught: none as WORDS, but all five are brands whose capitalised use is overwhelmingly the company, so 'is a word' is the wrong test for removal. Missed: Monster (0.059) stays under the threshold, though its false pairs (a Godzilla review) were already removed by R30's lower-case rule; Apple 0.002, Meta 0.001, Intel 0.0007 are rightly not flagged.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~132/bt1_census.out: KEPT SAMPLE 20 and REMOVED SAMPLE Booking/Cadence/Orange lines, read by 3.0.0_SA_CVO at 13:0xZ",
        "org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~132/common_word_aliases.json: definition, ratio_threshold 0.2, aliases_counted 413, aliases_flagged 5, per-alias ratios",
        "org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND_ANALYSIS.round74.md ADDENDUM 7 (R31 RETIRED as measured and not served)",
        "graded TO: AMGT_HARVST.TO-HVST-bt-1 (assignee 0.9.0_WK_AMGT_HARVST~132), criterion AC4"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An L9 grade record, not a hazard: HVST-bt-1 AC4 graded MET by a seat that did none of the work."
  }
]
```
