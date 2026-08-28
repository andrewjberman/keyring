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


### CHANNEL ITEM — 76164 (0.6.0_AE_PartnerETL): the D2 rc-evidence rider has no schema slot | OBSERVATION / INERT / RECORDED

3.0.0_SA_CVO, landed at merge-window close (queued 16:4xZ, cause: MSTR merge window 76151).
FINDING (accepted as filed, grounding complete on arrival): the D2 lock-in rider mandates the
validator invocation + TRUE rc recorded IN the proof-of-spec instance; `org/standards/
PROOF_OF_SPEC.schema.json` root and `controls` are both `additionalProperties:false`, so the only
landing spot is `compiler_tools[].result` — an unconstrained string no validator rejects on (the
unenforced-field-drifts shape, effect size 0/16 vs 5/39). The rider buys discipline, not
enforcement, until a slot exists. Surfacing seat complied meanwhile (92054db7b5: TRUE_RC=0 captured
bare, two-arm negative control, both arms fired on different axes).
INTERIM FORM RULED (76166): compiler_tools[] row whose result BEGINS `TRUE_RC=<n>` + bare
invocation; checked per-instance by CVO eye at cert/acceptance, stated as a CVO-eye check.
REMEDY RIDES THE ROUND: candidate remediation row at round close = a constrained `validator_run`
slot in the schema, arriving WITH its Rule-24 four-postulate record + token census; schema custody
= 3.0.0_SA_CVO unless the round rules otherwise. Nothing armed; DISARM n/a.


### CHANNEL ITEMS — 76222 (0.4.0_DS_ClientPlatform~R, S4, TO-R1-DS a-2 census @f05d754d43): FOUR OBSERVATION/INERT | RECORDED; item 1 ROUTED to the decomp owner

3.0.0_SA_CVO, 2026-08-27 ~17:1xZ. Filing quality noted for the record: both control arms fired
(NEG insuranceCharacteristics 106/106 MISSING matching the egress refusal; POS accountNumber
106/106), carrier-vs-instrument distinction applied (AE proof instance correctly NOT used as
corroboration — same 08-25 measurement, two carriers), per-use grant boundary honored (no vendor
call; would have routed BLOCKING), and a self-correction carried (MISSING vs NULL — different
consumer code implied).

**ITEM 1 — DECOMP FACE NAMES THE WRONG CALL. ROUTED to 2.0.0_SA_COO (decomp owner) same-turn.**
INS-a-2 face says `accountdetailsearch` supplies the v1 fields; measured in landed bytes, all 8
come from `relationshipaccountdetailsearch` (sanctioned), while the short-named surface is
EGRESS-REFUSED (insurance_leg.py:78-89, OPAL_TAXSMA gate) and supplies only the Ruling-6-deferred
characteristics. The face is the LIVE dispatch surface for INS-a-1..3 at 0.6.0_AE_PartnerETL (S5,
seated). CVO second read (asked for by the surfacing seat): the defect is real per the measurement;
INERT is the RIGHT standing because the mis-reach FAILS CLOSED — a literal reader hits a loud
egress refusal, so the exposure is wasted motion and confusion, never silently wrong data. NOT
decomp-invalidating (the cell's surface is enumerated; its NAME is wrong — a face correction, not a
stage-3 reopen). Correction is the ISSUER'S act; the surfacing seat correctly declined to edit or
to message S5 directly.

**ITEM 2 — DUPLICATE BRONZE CAPTURE** (page0 byte-deep duplicate of offset0, superseded by the
offset0/offset50 pair): a prefix-globbing consumer double-counts 50 of 77 relationships. Nothing
consumes it today. Remediation candidate at round close: supersede/dedupe the stale capture,
DS-lane owner named at the cut.

**ITEM 3 — FOUR LIVE ACCOUNTS, NULL currentEmv, asOfDate 2025-11-17** (2 Allianz, 2 Vanguard).
Cause UNESTABLISHED and correctly not chased (closedDate null on all 106 — does not discriminate;
two stale-dated accounts DO carry emv — no non-null check separates them). Stays UNDER
INVESTIGATION; not graduable until mechanism attributed.

**ITEM 4 — ONE NEGATIVE BALANCE** in the 102 valued (sum 51,807,815.31; min -309,502.70; 3 zero).
Recorded. Not served (AC4 shut behind arm-(a)).

**ITEM 1 ROUTED ACT DISCHARGED -- 76236 (2.0.0_SA_COO), same window @333906bb5e:** the INS-a-2 cell AND the TO-A1-AE face both corrected on BOTH carriers (prior text preserved inside the correction blocks); 0.6.0_AE_PartnerETL notified read-before-next-act; correction cites this doc entry as its measurement. Item 1 is CLOSED at the channel: defect corrected at the issuer, surfacing seat exonerated of edit-restraint by the loop itself.


### ACCEPTANCE READ — ADVI_INSURE.TO-A1-AE: PASS (CVO independent run); completion flip is COO+CVO ground per CTO 76280

3.0.0_SA_CVO, 2026-08-27 ~17:5xZ. Validator run at this seat on the declared instance: ids
INSA1AE-AC1..AC3 -> `VALID`, TRUE_RC=0 bare, rows=3, violations=0 — and this instance exercised the
FULL pipeline alignment (decomp_ref ENFORCE; forward 3/3 criteria->cells, 3/3 cells->decomp id
space of 22; backward 3/3), the first launch-set instance to do so. Gate half closed by 1.0.0_SA_CTO
(76280): every 76225 concern back WITH its falsifier, arms 4-6 seat-self-added (arm 6 firm-fence
explicitDeny = separation ENFORCING), running bytes proven built bytes via BUILD_MANIFEST both
normalisations. Evidence commit a06658a1ab. The seat correctly did NOT self-flip; the flip lands
with 2.0.0_SA_COO's RAVC on this read + the gate acceptance.

**TWO-CARRIER FINDING banked (CTO -> COO round item #4):** "the declared build input" is TWO
carriers — BUILD_MANIFEST.json `vendored_modules` (documentation) vs lambda-source-map.json
`files[]` (what the packager ZIPS, build-and-upload.sh:119) — so a seat told to amend "the manifest"
can amend the carrier that does not build, shipping a zip missing the module while every filename
check passes. Registered @60c5f2f327; corrective belongs to the D0 build-tooling family when cut.


### CERT STEP-ZERO — INS-a-4 amendment + ADVI_INSURE.TO-A2-AE: **PASS** (pair certified together)

3.0.0_SA_CVO, 2026-08-27 ~18:0xZ, on 2.0.0_SA_COO's @5a92078c11 (which also flipped TO-A1-AE
COMPLETE on the three-instrument chain — seat a06658a1ab + CTO gate + CVO read @6956c27796).

**CELL (INS-a-4):** issuer-authored with the full provenance chain cited on its face (measured
advisor-spine gap 76245 advisor_basis NOT-CAPTURED 106/106; route-2 ruling 76246 + CTO concur
76249; word-holder's surface-scoped egress reading 76291) — the wire chain now has a FACE, closing
the ruled-on-the-wire/runs-under-a-closed-face gap the flip would have opened. Re-cert authority
named on the cell (CVO or base CTO, never CRO — the PERFRP-subject restriction respected). First-
exercise law carried: a clean zero or entitlement refusal is a REAL outcome, per-surface, never a
generalised absence. **PASS.**

**FACE (TO-A2-AE):** decomp_ref present naming the cell + amendment date; ids INSA2AE-AC1..AC4 all
cell-traced (4/4 both directions, single-cell trivially complete); AC1 EXERCISED with denominator
either way; AC2 bronze RAW byte-for-byte (Rule 17a) at APPLIED; AC3 scope SHOWN not asserted (calls
enumerated, zero /account-api/*); AC4 carries the D2 rc discipline verbatim; instance_path single-
group in the assignee folder. **SEQUENCING DISCLOSED, not smoothed:** the capture legally predates
this cert (authorized through the ruling chain); the ACCEPTANCE waits on the cert; nothing
grandfathered — the honest form, certified as stated. **PASS.**

Acceptance ground when 0.6.0_AE_PartnerETL reports: INSA2AE-AC1..AC4 on this face, CVO read at
cadence.


### CHANNEL ITEMS — 76302 (DS~R, BLOCKING-class qualification) + 76304 (0.6.0_AE, AC1 UNCOMPUTABLE-BY-DEPENDENCY) | RECORDED + PRE-REGISTRATION RULED

3.0.0_SA_CVO, 2026-08-27 ~18:1xZ. The two arrived in one window and interlock: the capture 76302
wanted pre-registered against is BLOCKED by 76304's authority finding — so the pre-registration
lands BEFORE any byte is captured, the strongest possible form.

**76302 — THE ADVISOR-HOP EXPECTATION WAS CROSS-FIRM INFERENCE (0.4.0_DS_ClientPlatform~R,
self-qualified):** the evidence `financialTeam[]` populates is a COTTONWOOD payload; for 49F, S4 has
never been exercised by anyone. The 49F-specific evidence points the other way: `teams[]` (sibling
field, same object) is an EMPTY ARRAY on 77/77 — the vendor affirmatively answering zero, not a
projection gap. The firm, not the surface, is the difference. The seat also ran the firm-separation
check BOTH directions before sending (0 of 77 relationships contain "cottonwood"; firmID single
value 3281 across 106 accounts) — the map's "every insurance byte is Cottonwood's" sentence
describes the pre-08-25 estate. Capture remains the right act; only its EXPECTED OUTCOME was
inference.

**PRE-REGISTERED, RULED AT THIS SEAT (CVO acceptance-read semantics on the face I certified; COO
concurrence requested for the face rider):** an EMPTY `financialTeam[]` on the 49F principal is a
**COMPLETE ANSWER AND A REAL FINDING** — sibling to AC1's refusal-is-complete law: it closes the
question as a Black Diamond CONFIGURATION state (no team assigned), the advisor-basis stamp moves
to a vendor-config value, and the resulting ask routes to Andrew. It is NOT a failed capture; it is
not retried, not widened, not quietly absorbed. ADOPTED with it, DS~R's probe-first form: when the
mint recovers, capture ONE relationship id and read `financialTeam[]` before spending the cohort —
empty on one means the cohort adds nothing but egress. DS~R's AC1 prep correctly designs for BOTH
branches.

**76304 — AC1 UNCOMPUTABLE-BY-DEPENDENCY at the AUTHORITY MINT (0.6.0_AE_PartnerETL,
@03d43dc4a3):** relationshipdetail NEVER CALLED — zero evidence about that surface exists; the seat
explicitly declined the convenient "capture refused" framing. Measured, arm-as-control-of-arm on
ONE live cookie: clientview token mint 0/3 vs datamining 3/3 — an authority-specific signature. The
08-25 byte-identical-bearers measurement was true of a SESSION, not a contract; the authorities
have diverged. **The leg's own defensive design (per-surface authority declaration, taken against
its author's own measurement) paid out in 48 hours** — the divergence is legible at the mint
instead of a silent 401 inside a production pull. Near-miss recorded by its author: a guessed
function name in the probe's hasattr guard nearly put "the 49F cookie is dead" on the record.
BLAST RADIUS (named, not chased): the deployed bd49f reporting producer's main path mints the same
failing authority (lambda_function.py:290) — would 401 on invoke today, NOT invoked to confirm;
keepalive HEALTHY (remedy not aimed there); re-establishment component = bd-49f-auto-login;
S1/datamining unaffected, S3+S4 fail together for one reason. **Re-establishment ROUTING is
2.0.0_SA_COO's** (the seat correctly offered handover rather than reaching into another lane).

**OBSERVATION/INERT (76302 tail):** `comp-pipescript io --pipeline advi` reports
`bd49f_insurance_nav_current.py` OUT-OF-GRAPH — a live gold producer outside the curated DAG its
pipeline is named for; AST-derived manifest clean, corroborates firm separation independently.
Recorded; graph-membership is a round-close candidate for the graph owner.

**76312 ADOPTION LANDED (2.0.0_SA_COO): all three halves ruled** -- (1) the pre-registration EXTENDED to the full three-outcome set: EMPTY / REFUSED / POPULATED are THREE different findings, each pre-registered COMPLETE (empty = vendor-config state, BASIS-axis stamp moves to the declared-but-unused arm DS~R preserved for exactly this case, ask routes to Andrew); (2) probe-first binds TO-A2-AE execution; (3) capture HOLDS until the ClientView mint is restored -- re-establishment routed to 0.7.0_AE_CloudOps~L (76305, owning family, single bounded act, mint-verified both arms). CVO CALL ON THE FACE (76312 asked): the empty-semantics half GOES ON THE FACE -- the banked law is that a protection existing only as a description is not a protection, and the face is what the executing seat reads at pickup; COO amends, CVO delta-certs the rider on landing. OUT-OF-GRAPH observation = round keeper #8 at the graph owner.

**DELTA-CERT on the AC1 rider @34edfe3e53: PASS.** Read at the face: the three-outcome set is complete on the criterion itself (landing / per-surface refusal / EMPTY-as-vendor-config-finding, each COMPLETE), the pre-registration timing is stated on the face (BEFORE any byte captured), the stamp-movement + Andrew routing are named, probe-first BINDS execution, and the id set is unchanged (still AC1..AC4 -- a rider, not a widening, so no expected_criteria delta). The 76312/76307 concurrence chain is cited. The empty-semantics now lives on the artifact the executing seat reads at pickup; the wire and this doc carry its provenance. Nothing further open on the 76302/76304 pair at any seat -- awaiting mint-restoration -> probe -> per its result.

**MINT RESTORED -- 76343/76349: the ClientView authority block is CLOSED as a bounded act.** Validated by COO on every bound: one sanctioned-wrapper invocation; mint-only PROVEN by a MEASURED ZERO (zero chain-Lambda invocations over the window, the 24h scheduled fires as the positive control that makes the zero a measurement); both verify arms 3/3 with the guard run BEFORE any status interpretation (the manufactured-401 near-miss carried, not repeated); box at resting state. The 00:00 scheduled fire stays the end-to-end acceptance. The pre-registered probe chain now runs at 0.6.0_AE_PartnerETL.

**CHANNEL ITEM (routed via COO, keeper candidate #11) -- THE MINT SUCCEEDED ON ITS FALLBACK | OBSERVATION / INERT / RECORDED:** kimiVision timed out on BOTH attempts; the DOM fallback carried the run; rc=0. The component holds ONE working classifier where it was built to have TWO -- and a green rc is exactly what that degradation looks like from outside. The anti-correlation class: the cleaner the pass, the less visible the loss of redundancy (kin to the orphan-watcher REACHABLE and the A.3 forwarder 93-of-93). Evidence: CommandId 36a927c5, on-box classify lines in 76343. INERT, moratorium stands; the round decides whether the kimi-timeout gets an owner.

### CAPTURE COMPLETE -- 76383 (0.6.0_AE_PartnerETL, @113354aa60): THE PRE-REGISTERED EMPTY OUTCOME FIRED. VENDOR-CONFIG FINDING; THE ASK ROUTES TO ANDREW.

3.0.0_SA_CVO, ~18:4xZ. relationshipdetail on 49F z08117302 -> HTTP-200, financialTeam KEY PRESENT type=list len=0 -- AFFIRMATIVELY EMPTY, not absent, not null. THE DISTINCTION WAS MUTATED, NOT ASSERTED: sealed planted mutant, four states -> four distinct verdicts (unmutated/key-removed/populated/null); determinism 2/2. PROBE-FIRST HONOURED: 1 of 50 ids spent; the cohort is a DECLARED EXCLUSION (adds vendor egress, zero information, per the pre-registration). Denominator honesty: 1 of 77 measured DIRECTLY; corroborated at own hand on a DIFFERENT page (50/50 teams empty, reproducing the 77/77 prior); raising the direct denominator is a widening needing a word, correctly not taken. PER THE PRE-REGISTRATION: advisor_basis moves to the vendor-config value (DS~R's EMPTY branch executes); the remedy ask -- assign teams in Black Diamond, or accept the advisor hop as unavailable for 49F -- IS ANDREW'S with 49F/Mike, routed via the CVO terminal.

SCORING on the certified face: AC1 PASS (empty-rider closed as MEASURED) / AC2 PASS (bronze raw, 0 parquet of 8) / AC4 PASS (instance VALID TRUE_RC=0, interim form) / **AC3 FAIL, DELIBERATE -- A CLAUSE-WORDING DEFECT, NOT A BREACH:** the S3 id-source call is STRUCTURALLY NECESSARY (S4's path needs an id; S3 is the sanctioned source in the certified map); every breach-guarding clause holds (49F only, read-only, ZERO /account-api/*). The seat REFUSED to score PASS against a false clause -- the sibling of INSA1AE-AC1's honest FAIL. AMENDMENT REQUESTED at 2.0.0_SA_COO ("relationshipdetail plus its structurally-required id source and the authority mints, no other surface"); CVO delta-certs on landing; the complete flip waits on it.

ALSO DISCLOSED (surfaced, not chased): landed objects carry to=ADVI_INSURE.TO-A1-AE in S3 metadata -- hardcoded in the deployed leg, minted before this face existed. Bytes untouched; the provenance stamp names the wrong TO. Round-queue candidate (code change + redeploy, not authorized mid-round). Restoration held: no 401 recurred.

**DELTA-CERT -- AC3 amendment @1b3a7817e7: PASS.** The clause is now true to the certified map (S3 named as the sanctioned id source, mints included, no-other-surface + all breach guards retained); the amendment note credits the deliberate-FAIL form and states why the original was false; id set unchanged; alignment_denominators added on the element (4 criteria / 1 cell / 0 unmapped / 0 untraceable). The seat re-scores AC3 against the amended clause and the COMPLETE flip proceeds on the full chain (COO RAVC-4 76395 + this cert + the seat re-score).

**TO-A2-AE ACCEPTANCE READ (final, post-re-score): PASS -- CVO independent validator run on the 4/4 instance: VALID, TRUE_RC=0 bare, full decomp_ref alignment (1 cell, 4 criteria, both directions). The seat's re-score disclosure is on the record as the model form: the verdict moved because the CRITERION changed, not the evidence -- byte-identical enumeration @113354aa60, no vendor call re-run, no denominator moved. Flip is COO ground on the complete chain; nothing at the channel blocks it.**

**TO-A2-AE FLIPPED COMPLETE (@5b250bffae) -- acceptance record final:** flip cites the two CVO reads (@5681c08447 cert + @432218b939 final read); the preserved AC3 FAIL travels in the flip's status text as criterion-corrected-forward, so the record teaches the honest-FAIL form. Both 0.6.0_AE_PartnerETL TOs closed; seat disposition at Andrew.

**KEEPER #8 GAINS A SECOND LIMB (DS~R 76430):** the insurance gold producer sits outside the curated advi DAG AND `comp-pipescript postdeps` returns rc=2 on all four firm trees (data/assets/ is not among them) -- TWO of three DS gold gates STRUCTURALLY CANNOT SEE this producer, and the tool's own TOOL-02 guard names the rule: blindness is not cleanliness. Also banked with the c02 face fix (@5b250bffae): **a RESTRICTIVE stale face is the arm nobody notices** -- holding always looks like discipline; pairs with the dep-block finding as one class, two arms, at the round.

### BRANCH B COMPLETE -- 76483 (0.4.0_DS_ClientPlatform~R): the vendor-config finding is IN THE GOLD CONTRACT; keeper #8 now has THREE MEASURED LIMBS

3.0.0_SA_CVO, ~19:1xZ. RE-EMIT with negative control: EXACTLY ONE FIELD MOVED (advisor_basis NOT-CAPTURED-PENDING-SURFACE -> NOT-DERIVABLE-UPSTREAM), 13 columns byte-unchanged, invariants held, pre-write falsifiers fired clean. Producer @f4836ad706 ON ORIGIN; axis amendment @36e59823f4.

TWO CONTRACT-RECORD GAINS: (1) **THE BOUNDARY IS NOW STATED IN THE SPEC:** NOT-DERIVABLE-UPSTREAM vs UNOBSERVED-CONTAINER -- byte-identical payloads, different epistemic states (observation of absence vs absence of observation), different remedies; the whole advisor finding turned on exactly that difference, worked example carried. (2) A stale-carrier pointer fixed at s.1 -- the line moved twice today and ENDED ON THE SAME STRING, the most dangerous stale shape because the outcome flags nothing; prior text preserved, forward pointer added.

**KEEPER #8, THIRD LIMB MEASURED (was predicted):** ALL THREE DS gold gates are structurally blind to this producer, run BEFORE the emit -- (1) curated advi DAG: OUT-OF-GRAPH; (2) postdeps: rc=2 all four firm trees; (3) deployed-bytes sweep: **rc=0 with a clean 70-MATCH/0-STALE summary OVER A POPULATION THAT DOES NOT CONTAIN THE SUBJECT** -- not even a no-verdict line, just silence where the subject should be. >> A CLEAN SUMMARY THAT DOES NOT CONTAIN YOUR SUBJECT IS NOT A PASS << -- the clean-metrics shape with no failure line to sit above. Reported BLIND, never PASSED, per the tool's own TOOL-02 guard. For the graph owner at the cut: a live gold producer emitting to a firm bucket, invisible to all three gates simultaneously -- each gate individually reasonable, the intersection a producer nothing watches.

TO-R1-DS state as filed: AC1 DISTINGUISHED/APPLIED-GATED, AC2 DESIGN-COMPLETE (named exception CLOSED by the vendor-config resolution), AC3 clean, AC4 SHUT, AC5+AC6 SATISFIED. THE ANDREW ASK (assign financial teams to 49F relationships in Black Diamond) is ROUTED VIA THE CVO TERMINAL -- surfaced there 18:4xZ and standing; DS~R correctly wrote it nowhere it could read as already-asked.

**BANKED FOR THE ROUND (76487/76489) -- THE ACK-CLOCK IDENTIFIER TRAP, with corrective:** a guessed identifier poisons the READ clock as thoroughly as a forger would -- the clock's whole value is that no PROCESS can forge it, so its integrity rests entirely on writer discipline. THE TRAP: a message's SUBJECT carries the id being REPLIED TO while its Msg-ID field carries its own -- two plausible numbers in one neighbourhood. THE MECHANICAL CORRECTIVE: read Msg-ID FROM THE BODY, never infer an id from a filename or subject. The false entry (76486 acked-unread, nil exposure, positive-controlled before reporting) stands annotated -- the clock is append-only and the honest annotation IS the correction. Round note: the fabric-wide prompt-ack habit is what made one guessed id stand out to its own author. DS~R's day closed at seven defects found, SIX in their own instruments or entries -- the ratio is the discipline working, on the record.

### DELTA-CERT -- ADVI_INSURE.TO-R1-DS INSR1DS-AC1 = PASS on issuer 78349, instance @c833341bab: **PASS** (third instrument on the standing pattern)

3.0.0_SA_CVO, 2026-08-28 ~18:0xZ. Pattern: seat transcription (DS~R 78400) -> issuer direct-JSON read (COO) -> this read. GRAIN: instance at HEAD byte-identical to @c833341bab (git diff empty, worktree clean). INSTRUMENT: the validator at this seat, TRUE rc read bare -- bare form VALID rc=0 rows=6 violations=0 (coverage unchecked by its own banner), positional form with the six ids VALID rc=0; alignment 6/6 - 14/14 - 14/14 against DECOMP.md's 24-cell id space. TRANSCRIPTION: the ruling's quoted status_reason (678 chars, read from 78349's body in DS~R's inbox) == the instance's status_reason prefix, char-for-char; the transcription note follows the `||` separator as 78349 required. SCOPE OF THE COMMIT: exactly the AC1 row + one added artifact row (the silver-stage design, COMMITTED-NOT-DEPLOY-SCOPE) + the compiler_tools re-run note; AC2/AC3/AC4 UNCOMPUTABLE, AC5/AC6 PASS -- no other row's status moved. The evidence under the PASS is 3 TABLES, NOT 77 RELATIONSHIPS, carried on the row in the seat's own words -- the honest bound stays attached. **PASS.** The face's AC1 criterion text (grammar + Rule 17/17a) is unchanged by the ruling; the restated close condition lives in the instance and in 78349 -- the criterion did not move, its count did, so no face amendment is owed. Face `<status>` stays `pending` (78492 RELEASE is not a close), correctly.

### CERT STEP-ZERO -- INS-a-5 VEHICLE RE-RULED (@6a634f2f6f) + ADVI_INSURE.TO-A3-AE (amended) + ADVI_INSURE.TO-A4-AEC (new): **PASS, CONFIRMS on ONE widening** -- act (c') has no acceptance row; re-point INSA3AE-AC3 to (c')

3.0.0_SA_CVO, ~18:2xZ, on 2.0.0_SA_COO 78531. Pin @6a634f2f6f is an ancestor of HEAD. "Alt base CTO" refused by CTO (78482) -- this cert is this seat's alone; CTO ruled the cell (row 14), COO cut it, so the verifier is neither.

**CELL (INS-a-5, amended twice on its face):** Andrew's 17:40Z / 17:41Z words VERBATIM on the cell with the record path; CTO row 14 cited; acts (c)+(d) SUPERSEDED and kept as record; (c') chain wiring, (d') reporting-pull side, (e') ONE acceptance = the first chain fire with `runner=insurance` + the same-day `main` run as negative control. SOURCE CLAIMS RE-READ AT THIS SEAT (Read-class on named files + both live trigger planes): `_RUNNER_BY_TARGET` at session-trigger `:57` with main/fees only -- MATCH; `_fire_runner` `:205-212` invokes with NO Payload (`lam.invoke(FunctionName, InvocationType="Event")` `:211`) and is the SINGLE path for both the Lever-A skip leg (`:253`) and the runner-run leg (`:310`) -- so a payload map placed IN `_fire_runner` reaches both legs by construction, Lever-A binding condition 3 working for us; the marker vocabulary is the dict's keys (`:98`), so the third target extends it without a second edit; invoke policy `InvokeRunner` Resource = [runner, fees_runner] in `bd-49f-session-chain.tf` -- MATCH (ONE ARN to add); live EventBridge (139 rules, auto-paginated): `bd-49f-session-daily cron(0 0)` ENABLED, `bd-49f-fees-session-daily cron(20 22 MON-FRI)` ENABLED -- MATCH; `bd-49f-runner-daily cron(0 2)` DISABLED (the legacy direct fire, correctly off). The reporting-pull's live env reads `BD_SESSION_SECRET_ID=blackdiamond/49f/session` -- the SAME secret the chain mints, so an insurance-target refresh hands the leg a fresh identity by construction. Handler dispatch at HEAD `lambda_function.py:328-348`: `event.get("leg")=="insurance"` -> `insurance_leg.run_insurance_leg(pull_date)`; unknown leg refused by name; missing `q_start` refused by name -- act (a) as certified on the prior face. **PASS.**

**FACE (TO-A3-AE, amended):** decomp_ref names the cell + amendment; ids INSA3AE-AC1..AC5 == expected_criteria; instance_path in the assignee folder (instance exists @22d029d7c8: AC1 PASS, AC2 PASS, AC3 N/A-BY-CONSTRUCTION, AC4 UNCOMPUTABLE-BY-CONSTRUCTION, AC5 PASS). Both supersession paragraphs disclose rather than smooth; the 17:43:19Z QA invoke is recorded as evidence-not-acceptance with its RequestId and its legality at its time stated. **ONE WIDENING, CONFIRMS-CLASS (the SG-2b / CF-3b precedent at this seat):** act (c') -- `INSURANCE_EGRESS` ON in the deployed env, the `.tf` comment, the two provenance one-liners, the NEVER#6 ledger -- **has NO acceptance row**: AC1=(a), AC2=(b), AC3 RETIRED, AC4=(d), AC5=instance. An unconditional act with a consequence (the first fire REFUSES fail-closed if the flag is not live) always produces an evidence row the machine layer should require. RULED: **re-point INSA3AE-AC3 to (c')** -- the flag ON read back live (`get-function-configuration`); the DEPLOYED BYTES carry the consumer (`insurance_leg.py:89-101, :365, :606` at HEAD -- the LIVE bytes `JyQp8...` of 17:33Z were built BEFORE the flag landed in the tree: the live env has no `INSURANCE_EGRESS` and the 17:43Z QA invoke egressed with it absent, which is consistent only if the running handler has no consumer yet -- so (c') is a CODE+ENV deploy, source-map-compared, not an env-only apply); the `.tf` comment at HEAD; the ledger CLOSED. The id set stays five, the positional check is unchanged, and the enum gap below stops mattering for this instance. **PASS, CONFIRMS on that one-line face edit by the issuer.**

**FACE (TO-A4-AEC, new):** decomp_ref + decomp_context carry the ruling chain verbatim; ids INSA4AEC-AC1..AC5 == expected_criteria, 5/5 cell-traced (single cell, trivially complete); instance_path in ~K's folder (not yet minted -- correct pre-work); certification line names this seat; scope_guard names the surprise channel, the main/fees invariant, ONE ARN no wildcard, no monitor, Terraform + safe-apply on a SAVED -target'd plan, the CTO plan-gate on the IAM diff BEFORE apply, the deploy-order dependency on 0.6.0's flag (a first fire with the flag off is a negative control, not the acceptance -- stated), and the foreign un-applied opal-assets changes as STOP-and-surface. AC3's IAM acceptance is one `--resource-arns` per call with the controls as SEPARATE invocations -- the XXX.md trap honoured on the face. **PASS.** Two P2 notes for ~K, not gates: (i) the reporting-pull ARN crosses TF roots (opal-assets -> bd-pipeline) -- reference it by a `data.aws_lambda_function` lookup, never a literal ARN (a typed value beside a derived one); (ii) the stagger comment cites "cot 02:00Z" and it is STALE: on the EVENTS plane there is no cot cron at hour 2 (9 cot-named rules, none at 02:00Z); cot's session refresh is `cot-bd-session-daily-et` on the SCHEDULER plane (18 schedules), `cron(30 7 * * ? *)` America/New_York = 11:30Z today -- the `.tf:16-17` comment describes the 06-29 world. 04:35Z clears every fire visible on both planes (nearest: main 00:00Z, 4h35m before; the 10:45Z etf floor after); write the gap against the measured neighbours and name the plane.

**P1 ON THE A3-AE INSTANCE (0.6.0, before its next commit):** AC4 reads `UNCOMPUTABLE-BY-CONSTRUCTION` -- the wrong member: by-construction says no remedy moves it, and the first chain fire moves it. It is `UNCOMPUTABLE` pending the fire (Rule 24 iv, state coherence). With AC3 re-pointed to (c'), the N/A-BY-CONSTRUCTION workaround retires too.

**SCHEMA OBSERVATION (INERT, routed to the enum's four-postulate record owner via 1.0.0_SA_CTO):** `PROOF_OF_SPEC.schema.json` status enum {PASS, FAIL, UNCOMPUTABLE-BY-CONSTRUCTION, UNVERIFIABLE-BY-INSTRUMENT, N/A-BY-CONSTRUCTION, UNCOMPUTABLE} has NO terminal-by-supersession member; 0.6.0 wrote N/A-BY-CONSTRUCTION "because the schema has no 'superseded' value and FAIL would be false" -- a face state the machine layer cannot express, the uncovered member of Rule 24 (i), mirror of DE~D's declared-state-no-producer-can-emit. Not a fix here; the record's owner decides.

Acceptance ground when the seats report: TO-A3-AE (c') on the re-pointed AC3 + AC4 on the first fire; TO-A4-AEC AC1..AC5 on its face; the (e') fire read ONCE by this seat for both.

### CHANNEL ITEM -- 78480 (0.6.0_AE_PartnerETL): OBSERVATION / INERT / RECORDED + IDENTIFIED -- the 2 foreign un-applied opal-assets changes are the KNOWN X-ii-a items, gated on the post-campaign 0.7.0 base re-seat

3.0.0_SA_CVO, ~18:2xZ. Measured: the emitter `AGGREGATE_PREFIX` move (`gold/mdpf_revamp/_aggregate_aua/` -> `portal/gold/mdpf/_staging/aggregate_aua/`, a served-prefix move) has sat in `emitter.tf:241` since @2740e4de8f, 0.7.0_AE_CloudOps, 2026-08-11 -- DESIRED 17 days, APPLIED never. It is not stranded: Andrew's ~22:2xZ 08-27 word (record @64fe9ef4ce) places "X-ii-a apply + freshguard close + re-emit DECISION" at the post-campaign 0.7.0-base re-seat sitting (one brief at MSTR), and TO-A4-AEC's scope_guard already names them as "another seat's un-applied X-ii-a changes". So 78480's open question closes: mid-flight-and-gated; owner 0.7.0_AE_CloudOps base; sitting = campaign completion. The hazard 0.6.0 named is real and stays: any UNTARGETED apply in that root lands a NEVER-class move under the applier's name -- every seat in opal-assets applies on a SAVED, -target'd plan until that sitting (already the law; restated because the landmine is live). The `terraform fmt -check` 7-file residue is the same sitting's.
