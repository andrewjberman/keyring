# ADVI_INSURE -- surprise channel, round 1 (INVESTIGATION_v1)

**Channel owner:** `3.0.0_SA_CVO`. **Protocol:** `org/ref/SURPRISE_CHANNEL_PROTOCOL.md` (Directive Execution Pipeline stage 5, CLAUDE.md Rule 27).

**Round opened** 2026-08-25. Executing seats surface; the CVO files. Items are validated against `../schemas/investigation_item.schema.json`.


### Round addendum -- 2026-08-26 14:30Z, filed by 3.0.0_SA_CVO (channel owner)

Four items, S8 through S11, surfaced by 0.4.0_DS_ClientPlatform~R in 72195 off the landed gold table
`insurance_nav_current/date=2026-08-25/`. All four are OBSERVATION / INERT, none was chased, and the
surfacing seat kept working -- which is the channel behaving as designed.

DIVISION OF LABOUR ON THE EVIDENCE, stated so nobody reads this as two measurements: the CONTENT
figures are 0.4.0_DS_ClientPlatform~R's and are carried as that seat's. 3.0.0_SA_CVO independently
checked only GRAIN (the named object exists at the stated vintage -- 12,889 B, 2026-08-26T00:16:38Z)
and COVERAGE (that prefix holds exactly one object). A filing act is not corroboration.

The four are not one finding. S8 and S9 are VOCABULARY defects in fields a consumer groups on; S10
is an unadjudicated SIGN; S11 is a NAME that disagrees with its own data by design. S9 and S11 share
the property that makes them worth the disk: each returns a plausible value rather than an error,
so no downstream check fires.

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
 },
 {
  "id": "ADVI_INSURE-S8",
  "surfaced_by": "0.4.0_DS_ClientPlatform~R (72195), during its 72177 s.3 gate re-read; FILED by 3.0.0_SA_CVO as channel owner. The CONTENT measurements are that seat's and are carried as that seat's, not re-derived. 3.0.0_SA_CVO independently checked GRAIN and COVERAGE only.",
  "surfaced_at": "2026-08-26T14:30Z",
  "one_line": "THE `product` AXIS CARRIES TWO VOCABULARIES AT ONCE (Rule 24(i) exclusivity): an uppercase enum -- INSURANCE_OTHER 85, INSURANCE_LIFEINSURANCE 11, INSURANCE_ANNUITY 7 -- sitting beside free text 'Annuity - IRA' 2 and 'Insurance' 1, where 'Annuity - IRA' OVERLAPS INSURANCE_ANNUITY and 'Insurance' overlaps every value, so a consumer grouping on this field gets two buckets for one concept and cannot tell which.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "0.4.0_DS_ClientPlatform~R's own read of the landed gold table, denominator 106 rows x 15 cols stated on every count",
    "3.0.0_SA_CVO own s3api head-object at 2026-08-26T14:27Z: s3://opal-data-49financial/gold/advi/insurance/insurance_nav_current/date=2026-08-25/data.parquet EXISTS, 12,889 B, LastModified 2026-08-26T00:16:38Z -- matching the surfacing seat's stated vintage exactly. The object claimed about is the object that exists.",
    "3 of 106 rows carry the free-text form -- small in count and structural in kind, which is why it is filed rather than dismissed on size"
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "INERT: nothing degrades while this is unattended and no consumer is known to group on the field today. The reason it is not dismissed on 3-of-106: a MECE violation does not get less true at low count, it gets less VISIBLE -- a 3-row overlap is exactly the size that survives review and then silently splits a total. Producer-side remedy is one vocabulary or an explicit two-field split; that is not authorized by this item."
 },
 {
  "id": "ADVI_INSURE-S9",
  "surfaced_by": "0.4.0_DS_ClientPlatform~R (72195), during its 72177 s.3 gate re-read; FILED by 3.0.0_SA_CVO as channel owner. The CONTENT measurements are that seat's and are carried as that seat's, not re-derived. 3.0.0_SA_CVO independently checked GRAIN and COVERAGE only.",
  "surfaced_at": "2026-08-26T14:30Z",
  "one_line": "THE `carrier` FIELD CONTAINS CUSTODIANS AND PLATFORMS, NOT ONLY CARRIERS -- Charles Schwab 1, Vanguard 2, EquatePlus 1 sit beside Brighthouse Financial 85, Allianz Life 8, AXA Equitable 4 -- so custodian.name is not universally the carrier, and the field is right for about 96% and quietly wrong for the rest.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "0.4.0_DS_ClientPlatform~R's own value census over the landed table, denominator 106",
    "commit d7583e51b2 (0.6.0_AE_PartnerETL) explicitly flagged custodian.dataFormatName as the AGGREGATOR and custodian.name as the CARRIER, and chose the latter -- the AE lane named this exact near-miss when it made the choice",
    "3.0.0_SA_CVO own s3api head-object at 2026-08-26T14:27Z: s3://opal-data-49financial/gold/advi/insurance/insurance_nav_current/date=2026-08-25/data.parquet EXISTS, 12,889 B, LastModified 2026-08-26T00:16:38Z -- matching the surfacing seat's stated vintage exactly. The object claimed about is the object that exists."
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "THE SHAPE IS THE POINT AND THE SURFACING SEAT NAMED IT: a field that is right for 96% returns a PLAUSIBLE VALUE rather than an error for the other 4%. A wrong carrier does not fail a load, does not trip a schema and does not look odd in a spot check -- it looks like a carrier. Note also that the AE lane's choice was DELIBERATE and reasoned, so this is not a mistake being caught; it is the residual of a correctly-made choice between two imperfect fields, and that residual had not been written down anywhere a consumer could see it. Filed for that reason."
 },
 {
  "id": "ADVI_INSURE-S10",
  "surfaced_by": "0.4.0_DS_ClientPlatform~R (72195), during its 72177 s.3 gate re-read; FILED by 3.0.0_SA_CVO as channel owner. The CONTENT measurements are that seat's and are carried as that seat's, not re-derived. 3.0.0_SA_CVO independently checked GRAIN and COVERAGE only.",
  "surfaced_at": "2026-08-26T14:30Z",
  "one_line": "`current_emv` CARRIES 1 NEGATIVE (-309,502.70), 3 ZEROS AND 4 NULLS OVER 106 ROWS against a sum of 51,807,815.31 -- and whether a negative EMV on an insurance account is legitimate (a loan or surrender balance) is UNDETERMINED, so a sum over this column silently nets a value nobody has adjudicated.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "0.4.0_DS_ClientPlatform~R's own column census, denominator 106: 1 negative, 3 zero, 4 null, sum 51,807,815.31, max 3,703,469.55",
    "the surfacing seat explicitly did NOT determine legitimacy and explicitly did not investigate -- recorded as an open question, not as a defect",
    "3.0.0_SA_CVO own s3api head-object at 2026-08-26T14:27Z: s3://opal-data-49financial/gold/advi/insurance/insurance_nav_current/date=2026-08-25/data.parquet EXISTS, 12,889 B, LastModified 2026-08-26T00:16:38Z -- matching the surfacing seat's stated vintage exactly. The object claimed about is the object that exists."
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "The honest form of this item is that it is a QUESTION, not a finding, and it is filed as one. A negative EMV may be entirely correct on an insurance product. What is recorded is that the sign has never been adjudicated and a sum nets it either way -- so the number is decision-useful only once someone rules on the sign. 4 nulls over 106 additionally mean sum and mean are computed over 102 while reading as though over 106; that is the printed-denominator rule landing on a column."
 },
 {
  "id": "ADVI_INSURE-S11",
  "surfaced_by": "0.4.0_DS_ClientPlatform~R (72195), during its 72177 s.3 gate re-read; FILED by 3.0.0_SA_CVO as channel owner. The CONTENT measurements are that seat's and are carried as that seat's, not re-derived. 3.0.0_SA_CVO independently checked GRAIN and COVERAGE only.",
  "surfaced_at": "2026-08-26T14:30Z",
  "one_line": "`as_of_date` SPANS 2.4 YEARS INSIDE A PARTITION NAMED date=2026-08-25 -- four distinct values 2024-03-28, 2025-11-17, 2026-02-06, 2026-08-24 -- so a table called _nav_current carries rows whose value is over two years old, and a consumer reading 'current' without also reading as_of_date is wrong with no error.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "0.4.0_DS_ClientPlatform~R's own distinct-value read of as_of_date over the 106-row partition",
    "CONSISTENT BY DESIGN, not a defect: 0.4.0_DS_ClientPlatform~J recorded that this plane is explicitly NOT T-1 -- the partition is the RUN date and as_of_date is the vendor's per-account STATEMENT date",
    "3.0.0_SA_CVO own list-objects-v2, auto-paginated, counted client-side: the insurance_nav_current/ prefix holds exactly 1 object -- this is the ONLY partition ever written. Denominator 1. Noted because it bears on S11: a table named _nav_current with a single partition has no prior vintage to compare against.",
    "3.0.0_SA_CVO own s3api head-object at 2026-08-26T14:27Z: s3://opal-data-49financial/gold/advi/insurance/insurance_nav_current/date=2026-08-25/data.parquet EXISTS, 12,889 B, LastModified 2026-08-26T00:16:38Z -- matching the surfacing seat's stated vintage exactly. The object claimed about is the object that exists."
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "TWO CLOCKS IN ONE TABLE, AND BOTH ARE CORRECT. Judging a statement-cycle asset on a trading calendar would manufacture a false outage every day -- that is the NEVER#1 class pointed at the wrong subject, and the surfacing seat correctly declined to call this stale. What is filed is narrower and survives that: the NAME says current and the DATA does not, and the only thing standing between a consumer and a wrong read is that consumer knowing to read a second column. A name is not a field a consumer can branch on. Related to the denominator note in COVERAGE: with exactly one partition ever written, there is no prior vintage against which a reader could notice the spread by comparison."
 }
]
```


---

## D2 DRIVE-OPEN DECLARATION — 2026-08-27T15:1xZ, 3.0.0_SA_CVO (channel owner)

Appended at D2 drive open per Andrew-direct lock-in (record:
`org/tier1_exec/3.0.0_SA_CVO/deliverables/ANDREW_DIRECT_20260827_D2_TIGHTENING_LOCKIN_BEFORE_FLOOD.md`).
A LAUNCH HOLD is live at 0.0.0_AB_MSTR until the lock-in confirms. Binding for this project's D2 round:

1. **DURABILITY RULE:** any mid-round ruling that amends a spec, remedy, or acceptance for this
   project LANDS IN THIS DOCUMENT SAME-TURN, landed by 3.0.0_SA_CVO as channel owner. Executing
   seats rule on the wire at full speed; the landing is CVO's act, not theirs. (The class this
   kills: a wire ruling scrolls while the committed artifact keeps pointing at the rejected design.)
2. **ROUND-CLOSE MODE:** this round terminates through a REAL remediation cut — REMEDIATION_v1 is
   cut at round close and the round closes only when it graduates ZERO items; graduated rows
   re-enter at stage 3 as the next round's TO inputs. Completion is measured, never declared.
3. **Rule 27 standing:** 3.0.0_SA_CVO mans this channel for the whole D2 drive. Surprises: one
   line by MCP, class {OBSERVATION, BLOCKING} x standing {ARMED, INERT}; ARMED names its disarm
   owner at surfacing; OBSERVATION never interrupts.
