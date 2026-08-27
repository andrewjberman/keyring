# D3_MODELOVERLAY -- surprise channel, round 1 (INVESTIGATION_v1)

**Channel owner:** `3.0.0_SA_CVO`. **Protocol:** `org/ref/SURPRISE_CHANNEL_PROTOCOL.md` (Directive Execution Pipeline stage 5, CLAUDE.md Rule 27).

**Round opened** 2026-08-25. Executing seats surface; the CVO files. Items are validated against `../schemas/investigation_item.schema.json`.

```json
[
 {
  "id": "D3_MODELOVERLAY-S1",
  "surfaced_by": "0.4.0_DS_ClientPlatform~K -- surfaced WITHOUT holding; they kept executing surfaces (a) and (b), which are unambiguously theirs",
  "surfaced_at": "2026-08-25T12:38Z",
  "one_line": "SURFACE (c), THE PLATINUM PROJECTION (D3-c-1/D3-c-2, AC6), HAS FOUR RECORDS NAMING FOUR DIFFERENT OWNERS -- including the Andrew-approved PRD s4c ruling 9 (0.7.0_AE_CloudOps, publisher key) and the decomp's own sequencing line at :90 ((c)+(d) DE-class).",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "PRD s4c ruling 9 -> 0.7.0_AE_CloudOps (publisher key) -- THE ANDREW-APPROVED ROW (all recs approved, ~19:1xZ)",
    "DECOMP.md:90 -> (a)+(b) DS-class; (c)+(d) DE-class -- the decomp's own sequencing line puts (c) in the DE lane",
    "four records, four owners, ALL READ AT SOURCE IN ONE TURN by the surfacing seat",
    "DISARMED by 2.0.0_SA_COO within four minutes: PRD s4c ruling 9 BINDS"
   ]
  },
  "disposition": "GRADUATED",
  "notes": "⛔ NOTHING IS WRONG WITH ANY SINGLE RECORD, AND THAT IS THE HAZARD. Four correct-looking records disagreeing is worse than one wrong one: EACH READER FINDS A CLEAN ANSWER AND NO READER FINDS THE CONFLICT. It surfaces only when someone reads all four in one turn, which is what the surfacing seat did. || THE SEAT DID NOT ADJUDICATE AND DID NOT HOLD -- they routed to the issuer for a spec amendment and kept executing the surfaces that were unambiguously theirs. Rule 27's shape exactly: surface without stopping. || DISARMED SAME DAY by the issuer ruling that the ANDREW-APPROVED row binds, which is the only tiebreak that needs no adjudication -- a sovereign-approved record outranks a lane-sequencing note by provenance rather than by argument."
 },
 {
  "id": "D3_MODELOVERLAY-S2",
  "surfaced_by": "0.4.0_DS_ClientPlatform~K, found on the way into surface (b) and routed same-turn; NOT blocked overall -- building the three levels that work",
  "surfaced_at": "2026-08-25T12:55Z",
  "one_line": "THE ADVISOR LEVEL OF THE FOUR-LEVEL CONTRACT IS NOT BUILDABLE: PRD s4c ruling 4 (Andrew-approved) names Primary Portfolio Group as the 49F advisor rollup key, and `is_primary` IS 100% NULL UPSTREAM -- None for 29,907 of 29,907 rows, zero non-null.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "gold/advi/dimensions/bridge_group_account, date=2026-08-18 -- THE ONLY PARTITION, DENOMINATOR 1, stated",
    "is_primary: None for 29,907 of 29,907 rows = 100.00%; non-null 0",
    "is_primary_status: 'ABSENT-UPSTREAM: BD dim 436 not selected by template 390224' -- all 29,907 rows, ONE distinct value",
    "dim_portfolio_group.partition_key_status independently agrees: 'MEMBERSHIP-ONLY: is_primary absent upstream (BD dim 436)'",
    "AC6/D3-e-3 requires s4b's four-level contract honoured AT ALL FOUR LEVELS"
   ]
  },
  "disposition": "GRADUATED",
  "disarm_owner": "THE ISSUER of D3_MODELOVERLAY (2.0.0_SA_COO to cut the spec amendment, 1.0.0_SA_CTO on the PRD ruling) -- the advisor level cannot be built until BD dim 436 is selected upstream, and that is neither the surfacing seat's act nor this channel's.",
  "notes": "⛔ AN ANDREW-APPROVED RULING NAMES A KEY THAT DOES NOT EXIST IN THE DATA. The ruling is sound; the data cannot satisfy it. Same shape as the a06 finding earlier today -- not a defect in our code, but A CONTRACT ASSUMING AN UPSTREAM PROPERTY NOBODY VERIFIED EXISTS. || ⛔ THE PRODUCER RECORDED THE REASON FOR ITS OWN ABSENCE, AND THAT IS WHY THIS IS DIAGNOSABLE IN ONE TURN RATHER THAN A MYSTERY: `is_primary_status` carries 'ABSENT-UPSTREAM: BD dim 436 not selected by template 390224' on every row. A bare NULL column would have been indistinguishable from a load failure, a schema drift, or a genuine all-false. THE NULL PLUS ITS REASON IS A FACT; THE NULL ALONE WOULD HAVE BEEN A QUESTION. || THREE OF FOUR LEVELS REMAIN DELIVERABLE and the seat is building them. ARMED because AC6 as written cannot be met and the round will reach it."
 }
]
```
