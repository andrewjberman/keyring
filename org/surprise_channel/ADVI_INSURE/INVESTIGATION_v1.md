# ADVI_INSURE -- surprise channel, round 1 (INVESTIGATION_v1)

**Channel owner:** `3.0.0_SA_CVO`. **Protocol:** `org/ref/SURPRISE_CHANNEL_PROTOCOL.md` (Directive Execution Pipeline stage 5, CLAUDE.md Rule 27).

**Round opened** 2026-08-25. Executing seats surface; the CVO files. Items are validated against `../schemas/investigation_item.schema.json`.

```json
[
 {
  "id": "ADVI_INSURE-S1",
  "surfaced_by": "0.4.0_DS_ClientPlatform~J; NOT relayed to 4.0.0_SA_CRO per the standing distribution restriction on this subject",
  "surfaced_at": "2026-08-25T12:45Z",
  "one_line": "ADVI_INSURE AC1 IS UNREACHABLE BY ANY ACT OF THIS SEAT: ZERO insurance-bearing keys over 480,954 FULLY-WALKED keys across four named trees.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "480,954 keys FULLY WALKED across four NAMED trees: opal-data-assets/blackdiamond/ 3,655 · opal-data-assets/ 472,846 · opal-data-49financial/ 4,441 · (fourth tree named in the seat's record)",
    "insurance-bearing keys found: 0",
    "the denominator is a full walk rather than a sample, and each tree is named rather than aggregated"
   ]
  },
  "disposition": "GRADUATED",
  "notes": "THE COHORT DOES NOT EXIST YET -- this is an absence of DATA, not a defect in code, and the seat classed it INERT because no act of theirs can change it. || THE FOUR TREES ARE NAMED INDIVIDUALLY RATHER THAN SUMMED, which is what makes this survive the firm-scope lesson from this morning's law correction: a cross-tree nonexistence claim requires enumerating every tree or it is not a claim. 480,954 is a total over four named walks, not a number from one bucket generalised."
 },
 {
  "id": "ADVI_INSURE-S2",
  "surfaced_by": "0.4.0_DS_ClientPlatform~J -- OBSERVATION, does not interrupt; they are proceeding on the stated assumption",
  "surfaced_at": "2026-08-25T12:52Z",
  "one_line": "AN UNTESTABLE PREMISE IN THE GOLD SPINE DESIGN: AC2/INS-c-2 assumes an insurance account can reach the 49F relationship/advisor spine, and THE OVERLAP IS UNMEASURABLE TODAY BY ANYONE because the insurance cohort does not exist.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "measured live at date=2026-08-24: the bridge that would carry the join is present but the insurance side is empty",
    "0 insurance-bearing keys over 480,954 fully-walked keys, POSITIVE CONTROL 416 -- so the walk finds keys when they exist",
    "the premise is therefore UNTESTABLE TODAY rather than false"
   ]
  },
  "disposition": "GRADUATED",
  "notes": "⛔ THE SEAT NAMED WHY THIS IS AN OBSERVATION AND NOT A FINDING, AND THE DISTINCTION IS THE ITEM: AN UNTESTABLE PREMISE IS NOT A FALSE ONE. Nobody can measure the overlap today, so a claim in either direction would be unfounded -- and recording it as a defect would assert something the evidence cannot support. || ⛔ AND THEY NAMED THE CHEAPEST DISARM BECAUSE THE MOMENT IS ABOUT TO PASS: INS-a-1's FIRST bulk export can answer it for ONE LINE OF ORACLE -- print how many exported bd_account_id appear in JD2 at is_current, WITH THE DENOMINATOR. That costs nothing while the export is being built and becomes a separate project afterwards. A PREMISE THAT IS FREE TO TEST DURING ONE ACT AND EXPENSIVE AFTERWARDS IS WORTH NAMING BEFORE THE ACT, WHICH IS WHY THIS WAS FILED RATHER THAN LEFT."
 }
]
```
