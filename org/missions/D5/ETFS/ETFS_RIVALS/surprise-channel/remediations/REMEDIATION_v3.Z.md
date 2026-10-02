# ETFS_RIVALS -- round 3 remediations (site-Z fabric): the L10 slug

<sweep_watermark>2026-10-01T11:25Z</sweep_watermark>

Author: 3.0.0_SA_CVO~RV, 2026-10-01. Graduated at round 3's L9 (`adjudications/ADJUDICATION_v3.Z.md`). Seven items. One is ARMED by this seat's reading (W1-S27: the served daily trade schedule drops windows on every day a fund misses the global prior date). The slug goes to 1.0.0_SA_CTO~Z for the round-3 analysis.

```json
[
  {
    "id": "ETFS_RIVALS-Z-W1-S27",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "gold_trade_schedule.run_stage pairs a report date only with ordered[i-1], the previous date ANY fund has in G1. A fund with no G1 on that global prior date (a Bloomberg-lagging or periodic fund) gets no window for the date, so its trades are absent from the served G5. The replay pairs each fund's own consecutive dates and forms them.",
    "evidence": [
      "investigation row ETFS_RIVALS-Z-W1-S27 (0.9.0_WK_ETFS_RIVALS~1): TSEL window 2025-08-15..2025-10-09 (6 trades) absent from the served date=2025-10-09 object, 37 global dates between TSEL's two; WCMG window 2026-08-27..2026-08-31 absent, same cause",
      "d4_live.json gates.1: TSEL 0/6 and WCMG 0/1 in the served delta, inside the COO half's table as 'own-prior-date'",
      "DRAIN_END_READ_ROUND3.md:78: 'TSEL and WCMG windows go missing daily'",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R3_REVIEW_20261001.md (co-committed)"
    ],
    "remedy": "The served per-date build pairs each fund with its own prior report date, as the replay does, shipped to the live build-canonical-shape Lambda under a pair. Missing windows are counted per fund before and after as the positive control.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v3",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v3"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~RV",
      "at": "2026-10-01T21:54:46Z"
    },
    "closed": true
  },
  {
    "id": "ETFS_RIVALS-Z-W4-S5",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "G4's 'newest object at a partition' is the greatest object name, '<as_of date>-<sha12>', and as_of is the partition date. Recency is therefore decided by hash. At date=2026-09-29 the QA import (172 rows, no price) outranks the later live pull (434 rows, 430 GICS sectors, 430 PX_LAST), and G1 joins the import. G1's own revisions have the same tie (W1-S19, W1-S25).",
    "evidence": [
      "investigation row ETFS_RIVALS-Z-W4-S5 (0.9.0_WK_ETFS_RIVALS~4): market-20260929-afcd903ad844 beats market-20260929-53bc393958bd ('a' > '5')",
      "investigation rows ETFS_RIVALS-Z-W1-S19, W1-S25 (the G1 revision forms <ts16>-h... and -j<yyyymmdd>-)",
      "REMEDIATION_v2.Z.md ETFS_RIVALS-Z-W1-S11 (OPEN, round 4 per analysis ruling 7): the same contract question for G1",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R3_REVIEW_20261001.md (co-committed)"
    ],
    "remedy": "One revision contract for G1, G4 and trade_schedule whose name sorts by write recency or a generation counter, decided together with W1-S11. Until then, a G1 replay of 2026-09-29 after the import object is set aside (a human's word, per the row) would carry the live pull's prices and GICS.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v3",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v3"
    },
    "closed": true
  },
  {
    "id": "ETFS_RIVALS-Z-W4-S2",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "BASG resolves only through a same-day Bloomberg co-holding join, and the daily Bloomberg request excludes BASG (issuer_first), so every NEW BASG report date resolves 0 of 33. The home funds resolve 0.0 because the crosswalk holds none of their CUSIPs (W1-S20). The identity floor stays PROVISIONAL 0.0: the CTO refused d-4's key 4 because it was measured over 5 issuer funds while the guardrail grades every fund.",
    "evidence": [
      "investigation row ETFS_RIVALS-Z-W4-S2 (0.9.0_WK_ETFS_RIVALS~4): G1 date=2026-09-30 BASG 0 of 33 RESOLVED",
      "investigation row ETFS_RIVALS-Z-W1-S20: home rows 1465 UNRESOLVED on the 27-landing replay",
      "d4_live.json identity_fraction_per_fund at 2026-09-29: BASG 0.9394, IDVZ 0.0, the Bloomberg-sourced rivals 1.0",
      "DRAIN_END_READ_ROUND3.md:51-52, :70-74",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R3_REVIEW_20261001.md (co-committed)"
    ],
    "remedy": "Either an identity route for issuer-only days (a BASG line in the daily Bloomberg request, or crosswalk forms for issuer CUSIP/ISIN) or per-source identity floors measured over every fund the guardrail grades. Supersedes the floor half of v1 W1-S4.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v3",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v3"
    },
    "closed": true
  },
  {
    "id": "ETFS_RIVALS-Z-W3-S15",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "G4 px_close and total_return_index come from a BDP reference pull answered as of the pull moment, so a late, replayed or historical run writes today's PX_LAST under an older date partition.",
    "evidence": [
      "investigation row ETFS_RIVALS-Z-W3-S15 (0.9.0_WK_ETFS_RIVALS~3)",
      "W4-S5: the 2026-09-29 live pull ran 2026-10-01 ~11:07Z, two days after its partition date",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R3_REVIEW_20261001.md (co-committed)"
    ],
    "remedy": "The G4 producer refuses or labels a pull whose run date is not its partition date, or switches to a historical request for past dates. The answer depends on whether any reader uses G4 price for a past date (FWD-6's consumer).",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v3"
    },
    "closed": false
  },
  {
    "id": "ETFS_RIVALS-Z-S6",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "GQGU is the one not-updated fund on the served page because no reader covers it. It has a measured issuer route in BASG's SEI filepoint format with 305 archived days, while its Bloomberg coverage is unmeasured (the BQL request needs Andrew's vendor word, per the CTO).",
    "evidence": [
      "investigation rows ETFS_RIVALS-Z-S6 (correcting S5)",
      "this seat's get of platinum/page/date=2026-10-01/manifest.json: not-updated ['PFOE/GQGU'], funds_updated 12 of 13",
      "DRAIN_END_READ_ROUND3.md:24, :81-83",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R3_REVIEW_20261001.md (co-committed)"
    ],
    "remedy": "A second issuer adapter (the same SEI parser) plus an import of the 305 archived days puts GQGU on the page with history. The Bloomberg measurement waits for Andrew's word and is not needed for the issuer route.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v3",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v3"
    },
    "closed": true
  },
  {
    "id": "ETFS_RIVALS-Z-W4-S1",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "d-4's apply granted s3:ListBucket with prefix bbg/* to the canonical-shape and daily roles, beyond the COO never-widen half key 2's literal Get text. The reader lists the landing, so a Get alone would read AccessDenied. The act widened past its signed text by one read-only grant, with the disclosure filed after the fact.",
    "evidence": [
      "investigation row ETFS_RIVALS-Z-W4-S1 (0.9.0_WK_ETFS_RIVALS~4)",
      "d4_live.json gates.3: simulate-principal-policy, Put and Delete implicitDeny for both roles",
      "DRAIN_END_READ_ROUND3.md:84-85: 'read-only, and the CTO has a disclosure'",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R3_REVIEW_20261001.md (co-committed)"
    ],
    "remedy": "The CTO either ratifies the ListBucket grant against key 2 or narrows it to the landing prefix. Either way, a never-widen half's text names List alongside Get whenever the reader lists.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v3",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v3"
    },
    "closed": true
  },
  {
    "id": "ETFS_RIVALS-Z-S7",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The seating lint's resolver truncates a worker code at the first underscore, so 0.9.0_WK_ETFS_RIVALS~<n> reads as seat 0.9.0_WK_ETFS. Any projects sharing a prefix (ETFS_RIVALS, ETFS_GUARDRAIL, ETFS_INGEST) read as one multi-project seat. It prints REFUSED today without blocking.",
    "evidence": [
      "investigation row ETFS_RIVALS-Z-S7 (2.0.0_SA_COO~RV)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R3_REVIEW_20261001.md (co-committed)"
    ],
    "remedy": "Fix the resolver in to-decomp-ref-lint.py and to-check.py before the seating limb is switched to enforcing. Enforcing it as it stands would block every issuance of a prefix-sharing project.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v3"
    },
    "closed": false
  }
]
```
