# AMGT_RESAPP -- round 91 L8/L9 adjudication, packet FINAL (dell1)

<sweep_watermark>2026-10-11T08:20Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-11T08:20:00Z. L8 packet: 2.0.0_SA_COO~R1 msg 3636,
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round91/DRAIN_END_PACKET.md @f936efde89 (blob fceb362c10, verified).
4 orders terminal: pp-1, pp-2, pp-3 complete; pp-6 applied 07:37:03Z and rolled back 07:50:33Z (cancelled). L9 on sections 2-4 HOLDS
on this seat's own runs (C-S54); pp-1 is NOT SERVED. New live finding C-S55: the base serves GBp beside pound prices on 5 UK securities
(13 rows), graduated ARMED. 8 rows swept since v110 (watermark 2026-10-11T06:10Z; 8 of 1038 investigation rows after it): 6 dismissed
(W371-S1 disarmed in code), W372-S3 graduated ARMED. Both ARMED graduations carry disarm owner 2.0.0_SA_COO~R1 in REMEDIATION_v35.

```json
[
  {
    "id": "AMGT_RESAPP-D1-C-S54",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T08:20:00Z",
    "one_line": "L9 read of the round-91 packet sections 2-4: HOLDS on this seat's own runs at box/dell1 HEAD d733ffc67a. pp-3 (SERVED): r91_peers_rebuilt.py P1-P6 PASS 243 of 243 (one partition 2026-10-11T0707Z; cap_vintage 2026-10-02 bar the named AMXB_MM_Equity), R91 PEERS REBUILT: YES. Whole-page read (r90_whole_page_read.py, live): FWD-8 YES on 3 of 3; figure vintages 1675/1687, 1448/1460, 1644/1656; object as-of 2 of 11, 2 of 13, 2 of 10 (0 of 34 in round 90; peers vintage now within the day); the peer caps sit 5 trading days behind, met only through the served cross_vintage_caveat, which the CTO's rendered-page read decides. pp-1 and pp-2 (LOCAL, merged): r90_name_match.py 8 of 8 incl. N8, r91_locator.py R91 LOCATOR: YES, lib/research/peers + lib/research/filings 452 passed, r91_name_match_deployed.py --where local 24 of 24 served, 0 leaked. pp-6 rollback: live CodeSha256 l8egBo/rf.. (LastModified 07:50:33Z, Successful), R89 PEERS DEPLOYED: YES, R89 DEPLOYED CLOSE: YES, r91_name_match_deployed.py --where deployed NO (D1 FAIL, the base state: no name match served). pp-1 is therefore NOT SERVED. round-close-check --round 91: 4 orders, 3 complete, MAY-CLOSE.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "L9 read of the round-91 packet sections 2-4: HOLDS on this seat's own runs at box/dell1 HEAD d733ffc67a. pp-3 (SERVED): r91_peers_rebuilt.py P1-P6 PASS 243 of 243 (one partition 2026-10-11T0707Z; cap_vintage 2026-10-02 bar the named AMXB_MM_Equity), R91 PEERS REBUILT: YES. Whole-page read (r90_whole_page_read.py, live): FWD-8 YES on 3 of 3; figure vintages 1675/1687, 1448/1460, 1644/1656; object as-of 2 of 11, 2 of 13, 2 of 10 (0 of 34 in round 90; peers vintage now within the day); the peer caps sit 5 trading days behind, met only through the served cross_vintage_caveat, which the CTO's rendered-page read decides. pp-1 and pp-2 (LOCAL, merged): r90_name_match.py 8 of 8 incl. N8, r91_locator.py R91 LOCATOR: YES, lib/research/peers + lib/research/filings 452 passed, r91_name_match_deployed.py --where local 24 of 24 served, 0 leaked. pp-6 rollback: live CodeSha256 l8egBo/rf.. (LastModified 07:50:33Z, Successful), R89 PEERS DEPLOYED: YES, R89 DEPLOYED CLOSE: YES, r91_name_match_deployed.py --where deployed NO (D1 FAIL, the base state: no name match served). pp-1 is therefore NOT SERVED. round-close-check --round 91: 4 orders, 3 complete, MAY-CLOSE.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO ran deliverables/2.0.0_SA_COO~R1/round91_prep/checks/r91_peers_rebuilt.py: R91 PEERS REBUILT: YES",
        "3.0.0_SA_CVO ran deliverables/2.0.0_SA_COO~R1/round90_prep/reads/r90_whole_page_read.py on 3 names: verdict table as stated",
        "3.0.0_SA_CVO ran deliverables/2.0.0_SA_COO~R1/round91_prep/checks/r91_name_match_deployed.py --where deployed (NO) and --where local (YES)",
        "3.0.0_SA_CVO ran r89_peers_deployed.sh and r89_deployed_close.sh --want amgt-corpus-dossier/11: YES x2",
        "3.0.0_SA_CVO aws lambda get-function-configuration opal-amgt-scoped-api 2026-10-11T08:0xZ: l8egBo/rf.., 07:50:33Z",
        "3.0.0_SA_CVO python .tools/round-close-check.py --project AMGT_RESAPP --round 91: verdict=MAY-CLOSE"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "L9 read of the round-91 packet sections 2-4: HOLDS on this seat's own runs at box/dell1 HEAD d733ffc67a. pp-3 (SERVED): r91_peers_rebuilt.py P1-P6 PASS 243 of 243 (one partition 2026-10-11T0707Z; cap_vintage 2026-10-02 bar the named AMXB_MM_Equity), R91 PEERS REBUILT: YES. Whole-page read (r90_whole_page_read.py, live): FWD-8 YES on 3 of 3; figure vintages 1675/1687, 1448/1460, 1644/1656; object as-of 2 of 11, 2 of 13, 2 of 10 (0 of 34 in round 90; peers vintage now within the day); the peer caps sit 5 trading days behind, met only through the served cross_vintage_caveat, which the CTO's rendered-page read decides. pp-1 and pp-2 (LOCAL, merged): r90_name_match.py 8 of 8 incl. N8, r91_locator.py R91 LOCATOR: YES, lib/research/peers + lib/research/filings 452 passed, r91_name_match_deployed.py --where local 24 of 24 served, 0 leaked. pp-6 rollback: live CodeSha256 l8egBo/rf.. (LastModified 07:50:33Z, Successful), R89 PEERS DEPLOYED: YES, R89 DEPLOYED CLOSE: YES, r91_name_match_deployed.py --where deployed NO (D1 FAIL, the base state: no name match served). pp-1 is therefore NOT SERVED. round-close-check --round 91: 4 orders, 3 complete, MAY-CLOSE."
  },
  {
    "id": "AMGT_RESAPP-D1-C-S55",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T08:20:00Z",
    "one_line": "The live peers route serves the minor-unit code GBp beside pound prices on 5 UK securities (13 member rows): a 100x currency mislabel on the base, pre-existing. Graduated ARMED to REMEDIATION_v35 (owner and disarm owner 2.0.0_SA_COO~R1), the cell the CTO's round-91 ADDENDUM 2 rules (a unit-aware currency guard, then one redeploy). This also grades section 3: the pp-6 rollback was right, since keeping it would have added 24 more such members.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~R1",
    "spec_asserts": "A served price_currency labels the unit the served price is in (a value must carry its claim; CLAUDE.md section 4).",
    "world_is": "On the LIVE opal-amgt-scoped-api (CodeSha256 l8egBo/rf.., LastModified 2026-10-11T07:50:33Z, the base after pp-6's rollback), GET /security/<S>/peers over every subject under s3://opal-data-harvest/peers/v1/ (245 listed, 244 served 200, 2242 members, 163 serving a price_currency): 13 member rows, 5 distinct securities, serve the minor-unit code GBp beside a price in POUNDS -- Imperial Brands 24.24, Rio Tinto 69.54, SSE 24.73, BP 5.571, AstraZeneca 120.32 -- each with price_currency_claim null. Read as GBp the label states the price 100x too small. These are numeric-ticker members (AMGT-av-5) whose key reaches a held record whose CRNCY is GBp while the scanner price is in pounds; pp-6 would have added 24 more (GBp 12) and was rolled back for it. Pre-existing, not made by round 91.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO ran org/tier1_exec/3.0.0_SA_CVO/deliverables/checks/amgt_minor_unit_census.py against the live function 2026-10-11T08:1xZ: 13 rows, 5 distinct securities",
        "round91/DRAIN_END_PACKET.md section 3 (issuer's UK read: Unilever 44.94 vs PX_LAST 4673.5 GBp)",
        "ledger/NEVER_WIDEN_ROUND91_REDEPLOY_CTO_HALF.md (ADDENDUM 2)"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Graduated to remediations/REMEDIATION_v35.md. No investigation row named this live class before; the packet named it in prose only."
  },
  {
    "id": "AMGT_RESAPP-D1-C-S56",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T08:20:00Z",
    "one_line": "D1-W371-S1 (ARMED) dismissed, disarmed in code: AMENDMENT 1's N8 refuses a raw name carrying a Class or Series designator. This seat called numeric_tickers.name_candidate at HEAD on the row's three members: 'China Construction Bank Corporation Class A' (China), '... Class H' (Hong Kong) and 'JD.com, Inc. Class A' (Hong Kong) each return False; the control 'ASML Holding NV' returns True. r90_name_match.py N8 PASS. Nothing of pp-1 is served (pp-6 rolled back).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_RESAPP-D1-W371-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W371-S1 (ARMED) dismissed, disarmed in code: AMENDMENT 1's N8 refuses a raw name carrying a Class or Series designator. This seat called numeric_tickers.name_candidate at HEAD on the row's three members: 'China Construction Bank Corporation Class A' (China), '... Class H' (Hong Kong) and 'JD.com, Inc. Class A' (Hong Kong) each return False; the control 'ASML Holding NV' returns True. r90_name_match.py N8 PASS. Nothing of pp-1 is served (pp-6 rolled back).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row AMGT_RESAPP-D1-W371-S1 (disarm_owner 2.0.0_SA_COO~R1)",
        "AMGT-pp-1 AMENDMENT 1 @b146adc911",
        "3.0.0_SA_CVO python: numeric_tickers.name_candidate on 3 rows -> False x3, control True"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W371-S1 (ARMED) dismissed, disarmed in code: AMENDMENT 1's N8 refuses a raw name carrying a Class or Series designator. This seat called numeric_tickers.name_candidate at HEAD on the row's three members: 'China Construction Bank Corporation Class A' (China), '... Class H' (Hong Kong) and 'JD.com, Inc. Class A' (Hong Kong) each return False; the control 'ASML Holding NV' returns True. r90_name_match.py N8 PASS. Nothing of pp-1 is served (pp-6 rolled back)."
  },
  {
    "id": "AMGT_RESAPP-D1-C-S57",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T08:20:00Z",
    "one_line": "D1-W372-S3 (ARMED) graduated ARMED to REMEDIATION_v35 (owner and disarm owner 2.0.0_SA_COO~R1): the block rule still runs a last-located period's block to the excerpt end (pre-existing, not widened by pp-2; packet section 6 item 5 names the round-92 cell). Not disarmed this round, so it is carried on a remediation with its ARMED clock.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~R1",
    "adjudicates": [
      "AMGT_RESAPP-D1-W372-S3"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W372-S3 (ARMED) graduated ARMED to REMEDIATION_v35 (owner and disarm owner 2.0.0_SA_COO~R1): the block rule still runs a last-located period's block to the excerpt end (pre-existing, not widened by pp-2; packet section 6 item 5 names the round-92 cell). Not disarmed this round, so it is carried on a remediation with its ARMED clock.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row AMGT_RESAPP-D1-W372-S3",
        "round91/DRAIN_END_PACKET.md sections 5 and 6 item 5"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Graduated to remediations/REMEDIATION_v35.md."
  },
  {
    "id": "AMGT_RESAPP-D1-C-S58",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T08:20:00Z",
    "one_line": "D1-W372-S1, D1-W372-S2 and D1-W372-S4 (INERT) dismissed: the issuer's rulings stand (the bare-year prose occurrences of 2019, the FY2026 158,132 value reachable only under another header, the 80-character row bound without a measured basis); pp-2's 13 of 13 locator arms pass on this seat's run and its regression read lost 0 supported points.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_RESAPP-D1-W372-S1",
      "AMGT_RESAPP-D1-W372-S2",
      "AMGT_RESAPP-D1-W372-S4"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W372-S1, D1-W372-S2 and D1-W372-S4 (INERT) dismissed: the issuer's rulings stand (the bare-year prose occurrences of 2019, the FY2026 158,132 value reachable only under another header, the 80-character row bound without a measured basis); pp-2's 13 of 13 locator arms pass on this seat's run and its regression read lost 0 supported points.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows AMGT_RESAPP-D1-W372-S1, S2, S4",
        "3.0.0_SA_CVO r91_locator.py: R91 LOCATOR: YES"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W372-S1, D1-W372-S2 and D1-W372-S4 (INERT) dismissed: the issuer's rulings stand (the bare-year prose occurrences of 2019, the FY2026 158,132 value reachable only under another header, the 80-character row bound without a measured basis); pp-2's 13 of 13 locator arms pass on this seat's run and its regression read lost 0 supported points."
  },
  {
    "id": "AMGT_RESAPP-D1-C-S59",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T08:20:00Z",
    "one_line": "D1-W371-S2, D1-W371-S3 and D1-W371-S4 (INERT) dismissed: the issuer's rulings stand. S2 (six US dotted tickers in the 1,047 partition, so it is not-US-alphabetic) answers the HEI.A note on REMEDIATION_v34. S3 (the literal 'cd \"$(git rev-parse --show-toplevel)\"' resolves to the base checkout when the shell resets) is an order-invocation hazard for every cut, not this cell's. S4 (the Shopify fixture re-keyed after N8) is consistent with N8.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_RESAPP-D1-W371-S2",
      "AMGT_RESAPP-D1-W371-S3",
      "AMGT_RESAPP-D1-W371-S4"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W371-S2, D1-W371-S3 and D1-W371-S4 (INERT) dismissed: the issuer's rulings stand. S2 (six US dotted tickers in the 1,047 partition, so it is not-US-alphabetic) answers the HEI.A note on REMEDIATION_v34. S3 (the literal 'cd \"$(git rev-parse --show-toplevel)\"' resolves to the base checkout when the shell resets) is an order-invocation hazard for every cut, not this cell's. S4 (the Shopify fixture re-keyed after N8) is consistent with N8.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows AMGT_RESAPP-D1-W371-S2, S3, S4",
        "3.0.0_SA_CVO r90_name_match.py 8 of 8"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W371-S2, D1-W371-S3 and D1-W371-S4 (INERT) dismissed: the issuer's rulings stand. S2 (six US dotted tickers in the 1,047 partition, so it is not-US-alphabetic) answers the HEI.A note on REMEDIATION_v34. S3 (the literal 'cd \"$(git rev-parse --show-toplevel)\"' resolves to the base checkout when the shell resets) is an order-invocation hazard for every cut, not this cell's. S4 (the Shopify fixture re-keyed after N8) is consistent with N8."
  }
]
```
