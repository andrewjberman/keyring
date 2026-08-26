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
        "480,954 keys FULLY WALKED across four NAMED trees: opal-data-assets/blackdiamond/ 3,655 \u00b7 opal-data-assets/ 472,846 \u00b7 opal-data-49financial/ 4,441 \u00b7 (fourth tree named in the seat's record)",
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
    "notes": "\u26d4 THE SEAT NAMED WHY THIS IS AN OBSERVATION AND NOT A FINDING, AND THE DISTINCTION IS THE ITEM: AN UNTESTABLE PREMISE IS NOT A FALSE ONE. Nobody can measure the overlap today, so a claim in either direction would be unfounded -- and recording it as a defect would assert something the evidence cannot support. || \u26d4 AND THEY NAMED THE CHEAPEST DISARM BECAUSE THE MOMENT IS ABOUT TO PASS: INS-a-1's FIRST bulk export can answer it for ONE LINE OF ORACLE -- print how many exported bd_account_id appear in JD2 at is_current, WITH THE DENOMINATOR. That costs nothing while the export is being built and becomes a separate project afterwards. A PREMISE THAT IS FREE TO TEST DURING ONE ACT AND EXPENSIVE AFTERWARDS IS WORTH NAMING BEFORE THE ACT, WHICH IS WHY THIS WAS FILED RATHER THAN LEFT."
  },
  {
    "id": "ADVI_INSURE-S3",
    "surfaced_by": "0.6.0_AE_PartnerETL",
    "surfaced_at": "2026-08-25T22:45Z",
    "one_line": "proof-of-spec-check crashed with an uncaught AttributeError when decomp_ref was a STRING, exiting rc=1 -- byte-identical to a legitimate INVALID verdict, while every TO instructs callers to check the rc.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "0.6.0_AE_PartnerETL",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "proof-of-spec-check.py:245 called .get() on decomp_ref assuming the object form; a bare string raised AttributeError",
        "the uncaught exception fell through to Python default exit code 1 -- the SAME code the tool uses for a legitimate INVALID verdict",
        "reproduced by 0.6.0_AE_PartnerETL on a committed PEER instance, so not local to the reporter file",
        "reproduced independently at 3.0.0_SA_CVO seat before any edit: string form rc=1, and a genuinely INVALID control instance also rc=1",
        "TOOL FIXED @9c9b2fd96b by 3.0.0_SA_CVO -- any uncaught exception now routes to rc=2 with TOOL-ERROR + NOT-A-VERDICT; 4-arm regression: defect 1->2, INVALID stays 1, VALID stays 0, READ-ERROR stays 2",
        "TRIGGERING ARTIFACT FIXED @d07c89a023 by 0.7.0_AE_CloudOps~J after censusing the estate: 152 instances, decomp_ref dict 15 / absent 136 / STRING 1 -- the one was theirs"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "An instrument failing in the direction of its own normal-looking output, in the VERIFIER OWN TOOL, on the night this fabric catalogued that class repeatedly in other seats work. Disarmed same-turn by the reporter for their own file; the tool half and the artifact half were closed by two other seats within the hour. The trigger population was exactly ONE and it was authored by the seat who read the fix notice and asked whether their own work was in scope -- which closed the residual 3.0.0_SA_CVO had named as not-mine-to-edit."
  },
  {
    "id": "ADVI_INSURE-S4",
    "surfaced_by": "0.6.0_AE_PartnerETL",
    "surfaced_at": "2026-08-25T22:45Z",
    "one_line": "AC1 oracle is a SOURCE-layer claim and the bd49f vehicle already ships DRY-gated, so the BUILD half of AC1 appears reachable with ZERO vendor egress; only EXERCISING it needs the sovereign word.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "lambda_function.py:118-123 @7d97a8bed2 -- _request REFUSES to open a socket while DRY_RUN=1, and the default is 1",
        "AC1 oracle asks that the vehicle leg EXIST and be CITED at a named ref, which is satisfiable by source read"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Executing seat did NOT proceed on it -- the spec is frozen mid-round and lifting a hold is the ISSUER call. 2.0.0_SA_COO holds. Recorded because it makes AC1 CHEAPER than assumed, not harder, and a seat that quietly proceeded on that reasoning would have been widening its own scope on a correct-sounding argument."
  },
  {
    "id": "ADVI_INSURE-S5",
    "surfaced_by": "0.6.0_AE_PartnerETL",
    "surfaced_at": "2026-08-25T22:45Z",
    "one_line": "The certified decomp I3 evidence line is TRUE but its SCOPE is narrower than the conclusion it supports: the session/token surface IS implemented, outside the searched tree.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "decomp I3 cites comp-find -i over data/black_diamond/ = 0 hits -- the search itself is correct",
        "the conclusion it supports is that nothing of it exists in the 49F BD code yet",
        "the credential half EXISTS at infra/aws/lambda/opal-assets/opal-assets-bd49f-reporting-pull/lambda_function.py:144-152 @7d97a8bed2, OUTSIDE the searched tree"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "NOT decomp-invalidating: the narrow-tree read makes AC1 CHEAPER (the credential leg already exists) rather than falsifying a premise the round depends on. Filed so the same narrow-tree pattern is not read in the OTHER direction by a later reader -- a true search over the wrong tree supporting a claim about the whole estate is the wrong-plane class, and it is invisible from inside the search.",
    "notes": "Raised by the reporter explicitly as NOT decomp-invalidating, which is the correct call and the reason it is dismissed rather than graduated."
  },
  {
    "id": "ADVI_INSURE-S6",
    "surfaced_by": "0.6.0_AE_PartnerETL",
    "surfaced_at": "2026-08-25T22:45Z",
    "one_line": "PRD s.11 Ruling 2 joins the two source modes on account number -- but that key is MASKED on the surface already inside the egress envelope and unmasked only on a separately gated surface, so the egress grant is load-bearing for the v1 JOIN ITSELF.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "the portfolioreporting surface -- the one inside the vehicle egress envelope -- returns account number MASKED, last-4 only, no exact-number filter accepted",
        "the unmasked key exists only on the account-api surface, separately gated (taxsma_resolver.py:10-19 @0ac99a72cb)",
        "Andrew-authorized live probe 2026-07-21, positive-controlled on Chiles internalId 22596361",
        "the measurement predates Ruling 2 by roughly three weeks"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Relevant to how ANY egress ask is scoped: the grant is not field enrichment, it is the join key for v1, so a scoping conversation treating it as enrichment would size the ask wrong. 2.0.0_SA_COO / Andrew. The notable part is that the measurement existed BEFORE the ruling -- the evidence was in the estate and the ruling was written without it."
  },
  {
    "id": "ADVI_INSURE-S7",
    "surfaced_by": "0.6.0_AE_PartnerETL",
    "surfaced_at": "2026-08-25T22:45Z",
    "one_line": "A captured payload file is MIS-NAMED -- account_detail_search.json holds a RelationshipAccountDetailSearch response -- so resolving it BY FILENAME returns a clean, well-formed, 200-status answer to a question you did not ask.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/black_diamond/API/domains/insurance/endpoints/payloads/account_detail_search.json @70e4741e83 -- its captured url is RelationshipAccountDetailSearch, not accountdetailsearch",
        "0 of 3 payload files hold an account-api response, while endpoints/README.md calls that endpoint the insurance-relevant endpoint",
        "two of the three files are the same endpoint",
        "reached by PARSING the captured payload bytes and diffing two projections of the same account -- a different instrument from the decomp census, so corroboration rather than repetition"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Rule 22a NEVER-BY-FILENAME one layer up from code: there it is deployed bytes vs source, here it is a captured payload vs its filename. The failure is not an error -- it is a 200-status well-formed response to the wrong question, which passes every check a reader would think to run. First-to-claim as far as the reporter could tell."
  }
]
```
