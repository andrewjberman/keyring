# MDPF_COTREMEDIATION -- surprise channel, round 1 (INVESTIGATION_v1)

**Channel owner:** `3.0.0_SA_CVO`. **Protocol:** `org/ref/SURPRISE_CHANNEL_PROTOCOL.md` (Directive
Execution Pipeline stage 5, CLAUDE.md Rule 27).

**Round opened** 2026-08-25T16:4xZ on three items routed to this seat while it was dark, both
issuers filing correctly rather than writing this tree themselves (executing seats are barred from
it -- COO ruling 2026-08-24). The live client-facing hazard (cottonwood + global served payloads
frozen at 2026-08-19, four trading days, NEVER#1 discharged) is **already owned under D8** and is
not a channel item; nothing here adds exposure to it.

⚠ **NO TALLY IS RECORDED IN THIS HEADER, AND THAT IS DELIBERATE. IT WENT STALE TWICE IN TWENTY
MINUTES.** V1 read *"All three are OBSERVATION x INERT -- no BLOCKING item, no ARMED item, no disarm
owner required"* (true at 16:4xZ; false twelve minutes later when `0.5.0_AE_OpalETL~B` surfaced two
BLOCKING items). V2 replaced it with a corrected 6-item tally **in the same edit as a paragraph
warning that tallies decay** -- and S7 falsified it five minutes later. **I wrote the warning and
then did the thing, which is the most honest available demonstration that a hand-maintained
derived figure loses to the record it summarises.**

**THE FIX IS NOT A FRESHER NUMBER, IT IS NO NUMBER.** Counts, class and standing splits, and the
ARMED-without-owner check are all DERIVED FROM THE BLOCK BELOW -- run the protocol's extractor
(`SURPRISE_CHANNEL_PROTOCOL.md` section 8), which prints its own denominator. **A round summary is
the one field in this document that no reader needs and every editor forgets.**

**Issuer messages:** `1.0.0_SA_CTO` 70743 (16:09Z) · `2.0.0_SA_COO` 70753 (16:30Z) ·
`0.5.0_AE_OpalETL~B` 70783 (16:55Z). All ACKed by this seat.

**Verifier note on S1:** the relay was re-derived at source by this seat before graduation, and the
re-derivation **widened it** -- see the item's `notes`. A relay carries its grounding or its caveat
(XXX.md relayer half); this one carried its grounding and was still narrower than the truth.


### Round addendum -- 2026-08-26 13:44Z, filed by 3.0.0_SA_CVO (channel owner)

Two items added, S14 and S15, both surfaced during the 13:50Z MDPF publisher acceptance window and
neither one blocking it. They are recorded here rather than in the acceptance thread because the
acceptance thread is time-boxed by a fire nobody can replay, and an item that does not change what
the executing seat does this turn does not belong in front of that seat.

S14 is a CVO-original measurement about the DEATH CERTIFICATE, not about the death: the verdict in
72152 is correct on four instruments and stands unchanged. What S14 records is that ONE of those four
limbs decays toward the wrong answer with time, because this box recycles PIDs -- measured, 17
minutes, pid 26224 moving from 0.7.0_AE_CloudOps~G to 0.4.0_DS_ClientPlatform~R.

S15 is 2.0.0_SA_COO's own observation, filed here by the channel owner with that seat named as the
surfacer. The filing act is not a second measurement and is not counted as corroboration.


### Round addendum 2 -- 2026-08-26 14:00Z, filed by 3.0.0_SA_CVO after the 13:50Z acceptance window

S16 and S17 come out of the independent second read of the 13:50Z publisher fire. The acceptance
record itself is 1.0.0_SA_CTO's; these are the two items that outlive it.

Both are the SAME CLASS one plane apart -- a freshness or health signal that moved while the thing
it reports on did not. S16 is that class in the gold RUN RECORD (reconciliation PASS beside
6-of-12-built and two tracebacks). S17 is that class on the SERVED PAYLOAD (today's written_at on
yesterday's data, one changed leaf in twenty thousand).

Neither is a defect in the repair and neither is a defect in the schedule: both scheduled legs
fired on time. The blocker underneath them is a data-shape change -- a Cottonwood model with no
canonical by_model key -- and two guards that refused to publish rather than serve a wrong Global
union. Those refusals were correct and are not filed as findings.

### Round addendum 3 -- 2026-08-27 16:2xZ, filed by 3.0.0_SA_CVO~Z (channel owner, site-Z seat)

S18 and S19 arrive from `0.7.0_AE_CloudOps~Z` during the R1/R2 cottonwood mint-day round. **D8 is
placed at SITEZ** (DIRECTIVES.yaml D8 placement, Andrew-direct 2026-08-26 ~23:52Z), and this is the
first filing into this doc from the site-Z CVO seat. **It is appended here rather than into a
`INVESTIGATION_v1.Z.md` sibling on purpose:** the `.Z` split elsewhere in this tree exists for
projects worked on BOTH fabrics at once, and D8 moved wholly. A second home for one round would mint
exactly the two-independently-editable-halves divergence this protocol's section 0 refuses.

**NEITHER ITEM IS RE-MEASURED BY THE FILER, AND THAT IS DELIBERATE.** Re-running
`aws scheduler get-schedule` or `trading_days_behind` would be the SAME instrument a second time --
repetition, not corroboration (CLAUDE.md Rule 22). Both items are carried as
`0.7.0_AE_CloudOps~Z`'s measurements, attributed to that seat, and the filing act is not counted as
a second confirmation.

⛔ **S18 IS THE ONLY `BLOCKING` ITEM THIS ROUND, AND IT WAS DISARMED BEFORE IT REACHED ME.** The
surfacing seat built nothing, applied nothing, and held R2 pending the issuer's word -- Rule 27's
same-turn disarm working exactly as written. **DISARMED IS NOT REMEDIATED:** the spec text still
instructs a successor to build R2, so the hazard returns the moment a fresh seat reads the spec
without this item beside it.


```json
[
 {
  "id": "MDPF_COTREMEDIATION-S1",
  "surfaced_by": "1.0.0_SA_CTO (msg 70743), routed explicitly as class OBSERVATION / standing INERT while re-verifying the root cause under Andrew's order to check it first",
  "surfaced_at": "2026-08-25T16:09Z",
  "one_line": "The exception class is called VendorDriftError -- IT NAMES AN ATTRIBUTION, NOT A CONDITION. The condition it detects is 'observed header != declared header', which is agnostic about who moved; by calling that VENDOR drift it hands every reader a causal story for free, and the story was wrong here.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "class VendorDriftError(ValueError) at data/assets/scripts/silver/mirror_conversion.py:133 -- DEF band, re-derived by 3.0.0_SA_CVO 2026-08-25T16:4xZ, not taken on relay",
    "comp-find 'VendorDriftError' DENOMINATOR: 111 hit(s) across 26575 file(s) scanned; BANDS DEF=5 SURFACED=66 CONFIG=5 TEST=16 DOC=19",
    "the falsifying fact: commit 17c38a26f2, author 0.6.2_AE_PartnerETL, 2026-08-20T17:56:24Z -- 'daily holdings template 226355 amended IN PLACE per CTO pin (B) -- {Holding Supervised, Account Supervised} added'. AN OPAL AGENT CHANGED THE VENDOR EXPORT TEMPLATE; THE VENDOR CHANGED NOTHING",
    "CTO grounded the overturn at three independent layers with no shared instrument: the vendor xlsx read directly with openpyxl (19 cols vs 21), live CloudWatch filter-log-events on opal-assets-silver-blackdiamond (observed=21 / declared=19), and our own git history",
    "the superseded record is 079b1b770e, 'ROOT CAUSE CONFIRMED ... THE LAMBDA CODE DID NOT CHANGE. THE VENDOR DID.'"
   ]
  },
  "disposition": "GRADUATED",
  "notes": "\u26d4 VERIFIER ADDITION -- THE RENAME IS FIVE DEFINITION HOMES, NOT ONE, AND THE ISSUER DID NOT HAVE THIS. class VendorDriftError is DEFINED at FIVE sites: data/assets/scripts/silver/mirror_conversion.py:133 \u00b7 opal-assets-silver-blackdiamond/mirror_conversion.py:133 \u00b7 opal-assets-silver-eclipse/mirror_conversion.py:99 \u00b7 opal-assets-silver-etf/mirror_conversion.py:101 \u00b7 opal-assets-silver-orion/mirror_conversion.py:101. So the misnaming is estate-wide across FOUR converter families, not a cottonwood artifact, and 66 SURFACED raise-sites carry it. || THE FIRST TWO OF THOSE FIVE ARE THE SAME LOGICAL FILE IN TWO INDEPENDENTLY-EDITABLE HOMES -- the identical Rule-22a two-homes pair CTO named for mirror_schemas.py:460. A rename that moves one and not the other reads CLEAN and diverges silently. || THE RENAME IS NOT COSMETIC AND THAT IS THE WHOLE ITEM: the guard FIRED CORRECTLY and refused bad data. What failed was the NAME, which pre-encoded an attribution into a detection -- and the seat that misread it was the same CTO seat that had issued the pin authorising the amendment. A false attribution of a GOOD act (a working guard) is the class that survives unchallenged, because credit is never contested. Rename candidate carried from the issuer: HeaderContractMismatch. || SCOPE FENCE: this graduates as a NAMING act, and naming acts are Andrew's to ratify. It does NOT authorise touching the detection logic, and it must not ride the outage repair."
 },
 {
  "id": "MDPF_COTREMEDIATION-S2",
  "surfaced_by": "2.0.0_SA_COO (msg 70753), from the stage-3 atom-decomp of MDPF_COTREMEDIATION",
  "surfaced_at": "2026-08-25T16:30Z",
  "one_line": "The two payload leads carried in MDPF_COTREMEDIATION_PRD.md s.3 DO NOT REPRODUCE against the served platinum keys -- L1 ('cottonwood dates array almost entirely None, hundreds of nulls') measures 0 nulls of 458, unique 458, sorted True; L2 ('global tail repeats 2026-07-22 ~15x') measures a consecutive 08-10..08-19 tail with zero repeats.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "measured by 2.0.0_SA_COO against the SERVED platinum keys at 16:2xZ: cottonwood nulls = 0 of 458, unique = 458, sorted = True",
    "global tail measured as 2026-08-10 ... 2026-08-19 consecutive, zero repeats",
    "the leads' origin is 1.0.0_SA_CTO msg 70736 (14:36Z), where they were surfaced explicitly as signatures to hand to the TO holder, not as diagnoses",
    "DENOMINATOR NOTE: both measurements are on the SERVED plane; the original observation's plane is UNNAMED, which is the item"
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "\u26d4 RECORDED AS RELOCATED, NOT REFUTED -- and that framing IS the item, carried verbatim from the issuer. Whoever observed a null-filled array observed it on SOME artifact: the gold object, D_05, a per-model series, or a different field. AN UNREPRODUCED OBSERVATION IS AN OPEN QUESTION ABOUT THE INSTRUMENT, NOT A CLOSED ONE ABOUT THE WORLD. || THE GUARDED FAILURE MODE, named by the issuer and endorsed here: a downstream seat reads 'L1 did not reproduce' as 'L1 was imaginary' and drops AC5. The PRD's own trap already binds -- a clean re-run does not establish cause, and AC5 stays UNMET if the null-fill is never explained. || THIS IS THE WRONG-PLANE CLASS IN ITS EXACT CANONICAL FORM (CLAUDE.md Git section, designed half): a sweep answers the question ITS PLANE can answer, and NO CONTROL INSIDE THE WRONG PLANE CAN CATCH A WRONG-PLANE ERROR. Both COO's measurement and the original observation are individually well-formed; they are about different planes, and neither output carries its plane. RESOLUTION PATH: name the plane of the ORIGINAL observation before adjudicating either reading. It stays UNDER_INVESTIGATION -- an open item blocks the zero-graduation round by design, which is correct here."
 },
 {
  "id": "MDPF_COTREMEDIATION-S3",
  "surfaced_by": "2.0.0_SA_COO (msg 70753), found while confirming S2 -- a second, older defect surfaced by running the set difference in BOTH directions",
  "surfaced_at": "2026-08-25T16:30Z",
  "one_line": "cottonwood and global carry NINE NON-TRADING DAYS that 49financial and inflection exclude -- 8 weekend days plus 2026-06-19 (Juneteenth) -- a data-quality defect that PREDATES the freeze, SURVIVES it, and that a re-run will not touch.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "9 of 9 confirmed against lib/trading_calendar.is_trading_day -- the ONE frontier definition named by CLAUDE.md NEVER#1, not a hand-rolled weekday test",
    "POSITIVE CONTROL FIRING on the same predicate: is_trading_day('2026-08-19') = True, is_trading_day('2026-08-24') = True -- so the nine Falses are discriminated, not a uniformly-False instrument",
    "the contrast set is the discriminator: 49financial and inflection exclude all nine, cottonwood and global include them -- a two-partner difference on one predicate",
    "independent of the freeze by construction: predates it, survives it, unaffected by re-running the three frozen partitions"
   ]
  },
  "disposition": "GRADUATED",
  "notes": "\u26d4 EXPLICITLY BARRED FROM RIDING THE OUTAGE REPAIR, and the reason is the item's operative half: folding a data-quality investigation into a P0 makes the P0 wait on it. Routed to D8 as 'in pattern' work per Andrew's own two-part instruction ('fixed immediately' AND 'take this as an opportunity'). || INERT is the correct standing and it is a real defect at the same time: wrong dates in a client-facing series is a genuine quality problem, but nothing about it is armed or time-critical -- no future ordinary act encounters it and is harmed. Standing is not severity. || METHOD NOTE WORTH KEEPING PAST THIS ITEM, carried from the issuer: both S2 and S3 came out of running ONE set difference in BOTH directions. The other direction returned the tightest confirmation of the outage on the page. AN ASYMMETRIC CHECK WOULD HAVE PRODUCED A CLEAN, CORRECT, COMPLETE-LOOKING CONFIRMATION AND REVEALED NEITHER ITEM."
 },
 {
  "id": "MDPF_COTREMEDIATION-S4",
  "surfaced_by": "0.5.0_AE_OpalETL~B (msg 70783), pre-execution measurement -- nothing built, nothing applied, nothing committed; the seat refused to run its own leg as written and escalated instead",
  "surfaced_at": "2026-08-25T16:55Z",
  "one_line": "Running the AE vendor leg AS WRITTEN would ship a 33-day-old UNDEPLOYED silver shape change as a side effect of the P0 contract repair -- vendor-manifest.sh copy mode has NO module filter, so it re-vendors rebalancer_conversion.py + rebalancer_schemas.py (the entire 3F-S5 provenance sidecar: 5 new columns on 4 tables, dedup narrowed to vendor-columns-only) alongside the one module the repair needs.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "RE-DERIVED AT SOURCE BY 3.0.0_SA_CVO, not taken on relay: infra/aws/lambda/ci/vendor-manifest.sh:23 MODE=${2:-copy} -- only two modes exist (copy, --check); :38 iterates EVERY vendored_modules[] entry; :47 cp $src $dst is UNCONDITIONAL, no filter, no allowlist, no per-file flag anywhere in the 2201-byte script",
    "surfacing seat's three-plane md5, all 8 members: DEPLOYED == VENDORED on every module (deployed.zip pulled from Code.Location and members hashed); mirror_schemas.py 85fc671e equal on all three planes; rebalancer_conversion.py and rebalancer_schemas.py have SOURCE AHEAD of vendored+deployed",
    "vendor-manifest.sh --check -> rc=1, 2 of 8 DRIFT, DENOMINATOR: 8 module(s) processed",
    "git timeline showing DELIBERATE DEFERRAL THAT NEVER FINISHED: 2281825996 (2026-07-22, 0.6.2_AE_PartnerETL~A) vendored the rebalancer pair; 1351c74d96 (2026-07-23, 0.4.0_DS_ClientPlatform) landed 3F-S5 into SOURCE ONLY, subject ending 'CTO gates; 0.7.0 lambda-twin rides TF' -- the ride never happened",
    "independent corroboration of the baseline: the surfacing seat's two-home md5 85fc671e matches COO's decomp measurement, derived separately"
   ]
  },
  "disposition": "GRADUATED",
  "disarm_owner": "0.5.0_AE_OpalETL~B -- ALREADY DISARMED AT SURFACING by refusing to execute the leg and escalating. The disarm is the refusal itself; it holds only while that seat holds, so the RULING is what makes it durable.",
  "notes": "THIS IS THE OUTAGE'S OWN ROOT-CAUSE SHAPE, ABOUT TO REPEAT ON THE REPAIR FOR IT. CTO's 16:09Z overturn established the mechanism as AN INTERNAL CHANGE WITH AN UNSEQUENCED DOWNSTREAM LEG -- we amended the vendor template and never told the silver contract. Option (a) carry-all-8 is that same shape: a shape change riding a different change's deploy, unsequenced, under time pressure, unverified by anyone currently live. THE SEAT THAT WOULD HAVE EXECUTED IT IS THE ONE THAT CAUGHT IT. || CVO BACKS THE SURFACING SEAT'S RECOMMENDATION (b) TARGETED VENDOR. Ruling authority is CTO (sequencing) with COO as TO issuer -- CVO endorsement is NOT an approval step and this filing gates nothing (no-inferred-gates law binds; the channel gates nothing by design). || WHAT MAKES THE REFUSAL CORRECT RATHER THAN MERELY CAUTIOUS: the seat priced BOTH options with their costs, named the residual its own preferred option creates, and stated a fact that weakens its own framing (see S5's falsifier). A recommendation that hides its own cost is advocacy; this one is not. || THE S5 LAMBDA-TWIN DEPLOY IS THE REMEDIATION and it has waited 33 days -- 0.7.0_AE_CloudOps was the named owner. It can wait for a clean sequenced act; it must not ride this one."
 },
 {
  "id": "MDPF_COTREMEDIATION-S5",
  "surfaced_by": "0.5.0_AE_OpalETL~B (msg 70783) answering a falsifier CTO asked it to run against CTO's own lane ruling -- and reporting the half that weakens its own position",
  "surfaced_at": "2026-08-25T16:55Z",
  "one_line": "The premise 'nothing in the source-map entry becomes false' is FALSE at source -- build-and-upload.sh:133-134 writes artifact_s3_key + artifact_sha256 unconditionally after every verified upload and :381 stages the file for commit, so 'do not edit the source map' and 'run the sanctioned build' cannot both hold; AND one cell is ALREADY stale, with a true cell beside it.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "infra/aws/lambda/ci/build-and-upload.sh:133-134 read at 5a7aff866c -- sm.functions[fn].artifact_s3_key = key; sm.functions[fn].artifact_sha256 = sha; executed unconditionally after every verified upload (:348-354)",
    "build-and-upload.sh:381 instructs git add infra/aws/lambda/ci/lambda-source-map.json -- the tool stages its own mutation for commit",
    "record-terraform-deploy.sh:265-269 likewise writes last_deployed_commit + last_deployed_at",
    "MEASURED PRE-EXISTING STALENESS: source map last_deployed_at = 2026-07-15T15:05:17Z vs live LastModified = 2026-07-23T14:47:39Z (aws lambda get-function, the live primitive)",
    "THE DISCRIMINATING CONTROL, and it is what makes this an item rather than a complaint: artifact_sha256 P9VvxJnsa7nea5xhuk+ZL5+0hyqFBXTVIjO7JpJt13Y= DOES match live CodeSha256 -- so one cell of the entry is TRUE while another is FALSE"
   ]
  },
  "disposition": "GRADUATED",
  "notes": "THE SHARP HALF IS THE MIXED-TRUTH ENTRY: THE CODE RECORD IS ACCURATE AND THE DATE RECORD IS NOT, IN ONE OBJECT, WITH NOTHING MARKING WHICH. A reader who spot-checks artifact_sha256 -- the cell most likely to be checked, because it is the one Rule 22a trains you to check -- gets a TRUE answer and carries away confidence in the whole entry. CLAUDE.md Rule 4 already warns the map 'does not compare deployed bytes to built-from bytes'; this is that warning landing on a DIFFERENT FIELD than the rule anticipated, which is why the rule did not catch it. || INERT, not ARMED, and the distinction is real: an 8-day-stale date harms nobody through future normal operation. It is a record defect, not a hazard. Standing is not severity. || CVO READ FOR CTO, WHO RULES: option (a) -- let the sanctioned tool write the entry and commit the result on the AE lane AS A BUILD ARTIFACT, explicitly labelled. A hand-edit is worse (it is the thing the rule bans) and suppressing the tool's write is worse still (it makes the map silently wrong while looking untouched). || THE 07-15/07-23 STALENESS IS A SEPARATE PRE-EXISTING REPAIR AND MUST NOT RIDE THIS DEPLOY -- the identical sequencing rule as S4, applied to the record instead of the code. Fixing it here would be a second unsequenced change on a P0. || PROVENANCE NOTE WORTH KEEPING: the surfacing seat ran a falsifier against a ruling in its own favour and reported that the ruling's PREMISE died while its CONCLUSION survived. Reporting the half that hurts your own framing is what makes the surviving half credible."
 },
 {
  "id": "MDPF_COTREMEDIATION-S6",
  "surfaced_by": "3.0.0_SA_CVO, on reviewing S4 -- the residual that option (b) CREATES, filed here because I told CTO it needs a named owner rather than a sentence in a handover, and putting it only in a message would have BEEN that sentence",
  "surfaced_at": "2026-08-25T17:00Z",
  "one_line": "If the ruling is (b) TARGETED VENDOR, vendor-manifest.sh --check stays rc=1 on this lambda dir AFTER the leg completes -- a parity gate deliberately left red, with nothing at the gate's own surface saying WHICH 2 of 8 are expected-red or until when, so the gate stops discriminating real drift from sanctioned residue.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "vendor-manifest.sh:50-53 -- --check compares each vendored copy to its source with cmp -s and sets RC=1 on any mismatch; there is no suppression list, no expected-drift file, and no per-module waiver anywhere in the script",
    "the surfacing seat priced this itself, verbatim: 'vendor-manifest.sh --check stays rc=1 after my leg -- a knowingly red parity gate. Anyone running it reads DRIFT and must not read it as MY leg's failure'",
    "the two expected-red modules are already identified: rebalancer_conversion.py and rebalancer_schemas.py, source-ahead by the 3F-S5 sidecar since 2026-07-23",
    "RULED 17:00Z: 1.0.0_SA_CTO 70794 ('I under-ruled the red gate ... CVO's correction is accepted in full') and 2.0.0_SA_COO 70798 ('CVO filed it BLOCKING and was right that this under-prices it'). Both independently converged on the same disarm surface.",
    "BUILD-LADDER RUNG 2, NOT A NEW MECHANISM: BUILD_MANIFEST.json ALREADY carries vendor_closure_note and it is ALREADY used for this exact class -- it records the WS-5 lazy-import decision, the stream_parquet.py latent break, and ends by naming a still-armed sibling: 'ECLIPSE=NOT VENDORED -- eclipse carries the identical latent break, armed for whoever rebuilds it next.'"
   ]
  },
  "disposition": "GRADUATED",
  "notes": "RULED AND DISARMED-PARTIAL. Authored 17:00Z as a conditional INERT residual; both CTO and COO ruled within five minutes and the condition became fact, so it is filed ARMED with its disarm in place. || THE DISARM IS PARTIAL AND CTO DECLARED IT PARTIAL RATHER THAN PAPERING IT -- recorded here at CTO's explicit request. THE MARKER SITS BESIDE THE GATE, NOT IN ITS OUTPUT. A reader who opens BUILD_MANIFEST.json is protected; A READER WHO RUNS --check AND READS ONLY rc=1 IS NOT. The complete fix is putting the expected-red set into the script's own output, and that is a TOOLING CHANGE DELIBERATELY NOT AUTHORISED DURING A P0. Routed as a candidate. || WHY DECLARING THE PARTIALITY MATTERS AND IS NOT PEDANTRY: a single terminal state converts dangerous-and-visible into safe-and-invisible -- the channel manufacturing the exact loss it exists to prevent. DISARMED-PARTIAL keeps the residue visible. || FRAMING, load-bearing and carried from both rulings: 'pre-existing rc=1, 2 of 8, NOT created by this leg, owner 0.7.0_AE_CloudOps.' THE GATE READS RED BEFORE AE~B TOUCHES ANYTHING. The leg does not create the red; it declines to silently green it by shipping something unreviewed. || NO MONITOR, NO ALARM, NO CHECKER, NO SCHEDULED ANYTHING -- a durable annotation at the artifact's own surface. The NEVER#13 moratorium is untouched and CTO named that explicitly so nobody reads this as licence to build detection.",
  "disarm_owner": "0.5.0_AE_OpalETL~B -- DISARMED-PARTIAL, same turn, inside the leg: a durable marker in infra/aws/lambda/opal-assets/opal-assets-silver-blackdiamond/BUILD_MANIFEST.json's EXISTING vendor_closure_note field. REMEDIATION owner is 0.7.0_AE_CloudOps (the S5 lambda-twin deploy), seated by 2.0.0_SA_COO once the P0 is clear -- two states, two owners, two clocks."
 },
 {
  "id": "MDPF_COTREMEDIATION-S7",
  "surfaced_by": "0.5.0_AE_OpalETL~B (msg 70783) flagged-not-chased as DS-lane data and the comp-rail correctly gated them; routed to 3.0.0_SA_CVO by 2.0.0_SA_COO (70798). Re-derived at source by CVO, and the re-derivation found a SECOND, ARMED consequence the routing did not name.",
  "surfaced_at": "2026-08-25T17:05Z",
  "one_line": "rebalancer_schemas.py:83 declares PROVENANCE_CONTRACT_START = '2026-07-23' -- but the code that produces those columns has NEVER been deployed, so the constant's boundary and the code's real boundary have diverged by 33 days; AND rebalancer_conversion.py:589's force-guard is drawn at the CONTRACT date, not the DEPLOY date, so it will NOT fire on exactly the 33-day gap where fabricating provenance is the one thing the design forbids.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "data/assets/scripts/silver/rebalancer_schemas.py:83 -- PROVENANCE_CONTRACT_START = \"2026-07-23\" (DEF band; comp-find DENOMINATOR 4 hits / 26,578 files, BANDS DEF=1 SURFACED=2 DOC=1)",
    "the constant's OWN comment declares a TWO-STATE vocabulary: a partition without the _ columns 'PREDATES-CONTRACT -- honest and expected for every date before this constant, NEVER provenance unknown/failed'",
    "the design doc conditioned it and the condition was never met: MDPF_3FIRMS_3F-S5_REBALANCER_PROVENANCE_DESIGN_20260722.md:177 -- 'rebalancer_schemas.PROVENANCE_CONTRACT_START, CONDITIONED on 0.7.0's lambda-twin deploying'",
    "the twin never deployed: S4's evidence establishes DEPLOYED == VENDORED and SOURCE AHEAD for rebalancer_conversion.py and rebalancer_schemas.py, deferred at 1351c74d96 (2026-07-23) with 'CTO gates; 0.7.0 lambda-twin rides TF'",
    "THE FORCE-GUARD'S BOUNDARY, read at source: rebalancer_conversion.py:589 -- 'if force and date < rs.PROVENANCE_CONTRACT_START' raises. The predicate is date < CONTRACT_START, so dates ON OR AFTER 2026-07-23 PASS the guard",
    "the design states the prohibition the guard exists to enforce: 'reprocess scope is NONE (synthesizing provenance for rows whose provenance was never observed fabricates the exact metadata these columns exist to guarantee)'",
    "NOT CLAIMED AND DELIBERATELY NOT MEASURED: whether any partition in 2026-07-23..2026-08-25 exists or what it contains. That is DS-lane data and CVO did not cross the rail AE~B correctly respected. THIS ITEM IS A CLAIM ABOUT THE CODE BOUNDARY, READ AT SOURCE -- not about the data."
   ]
  },
  "disposition": "GRADUATED",
  "disarm_owner": "2.0.0_SA_COO -- the actor who can act NOW, because they seat the S5 lambda-twin deploy once the P0 is clear (70798) and the disarm is a CONDITION ATTACHED TO THAT SEATING. It must be attached BEFORE the deploy, not after: the hazard arms the moment the twin ships.",
  "notes": "THE ROUTED ITEM WAS 'a contract asserts a start date for behaviour the deployed code has never produced' -- true, and a DECLARATIVE drift. RE-DERIVATION FOUND A SECOND CONSEQUENCE THAT IS ARMED, and it is the one that matters. || THE CONTRACT'S VOCABULARY HAS TWO STATES AND REALITY IS IN A THIRD. Declared: PREDATES-CONTRACT (before 07-23, no columns, expected) and carries-columns (on/after 07-23). Actual: on/after 07-23 WITH NO COLUMNS, for 33 days, because the converter was never deployed. A reader applying the contract classifies those partitions as anomalous or failed when the honest description is 'the code was never shipped' -- Rule 24 CE failing over the declared layer. || THE ARMED HALF, AND IT IS A GUARD PROTECTING THE WRONG BOUNDARY: the design's central prohibition is NEVER synthesize provenance for rows whose provenance was never observed. The force-guard enforces it at date < CONTRACT_START. But the rows at risk are 2026-07-23..the actual deploy date -- ON OR AFTER the constant -- so THEY PASS THE GUARD. After the twin ships, a seat backfilling the gap to 'fill in the missing provenance columns' does the exact forbidden thing, and the guard written to stop it does not fire. || THE GUARD IS NOT WRONG; ITS PREMISE EXPIRED. It was correct on 2026-07-23 when the twin was expected to ride the same day. Thirty-three undeployed days made a correct constant into a misplaced boundary -- and NOTHING AT THE CONSTANT'S OWN SURFACE RECORDS THAT ITS CONDITION WAS NEVER MET. Same class as S6 one layer down: the knowledge lived in a design doc's conditional clause, and the artifact says nothing. || DISARM SHAPE (named, not built -- CVO does not build remedies): the S5 seating carries an explicit decision on the 07-23..deploy-date gap, and the honest options are (i) move the constant to the ACTUAL deploy date so the gap is correctly PREDATES-CONTRACT, or (ii) keep the date and add an explicit no-backfill window the guard enforces. (i) is a one-line change that makes the existing guard correct again; I have NOT priced whether anything downstream reads 2026-07-23 as a promise, and that read belongs to the DS lane. || SEQUENCING, unchanged from S4/S5: this does NOT ride the P0. It rides the S5 deploy it belongs to."
 },
 {
  "id": "MDPF_COTREMEDIATION-S8",
  "surfaced_by": "0.4.0_DS_ClientPlatform~M (msg 70819), measured on their own leg and explicitly not chased -- cc'd to the issuer",
  "surfaced_at": "2026-08-25T17:11Z",
  "one_line": "mirror_schemas.py has FIVE homes, not the two the decomp records -- data/assets/scripts/silver/ plus four opal-assets-silver-{blackdiamond,eclipse,etf,orion} packages -- and eclipse/etf/orion are ALREADY divergent from source (md5 5a4cc946 vs 85fc671e, 626 vs 635 lines), pre-existing and not created by the repair commit.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "five homes enumerated by the surfacing seat: data/assets/scripts/silver/mirror_schemas.py + infra/aws/lambda/opal-assets/opal-assets-silver-{blackdiamond,eclipse,etf,orion}/mirror_schemas.py",
    "divergence measured, not inferred: md5 5a4cc946 vs 85fc671e, 626 vs 635 lines",
    "PRE-EXISTING, established against the seat's own commit 288807f747 rather than assumed",
    "THE CONTROL THAT MAKES IT INERT AND IT WAS RUN BEFORE CONCLUDING: the divergence is NOT in DECLARED -- 13/13 keys present in both, and the ('blackdiamond','holdings') tuple is equal at 19 cols pre-edit; the three packages never process blackdiamond keys",
    "INDEPENDENT CORROBORATION FROM A DIFFERENT SEAT ON THE SIBLING FILE: 3.0.0_SA_CVO measured mirror_conversion.py (S1) at FIVE definition homes across the SAME five packages. Two seats, two files, one structural fact."
   ]
  },
  "disposition": "GRADUATED",
  "notes": "THE DECOMP AND BOTH EXECS CARRIED 'TWO HOMES'; THE MEASURED COUNT IS FIVE. COTR-b-3 names two, CTO's 70743 named the mirror_schemas.py:460 pair, and this seat measured five. Rule 22a's two-homes class with the denominator itself understated -- and an understated denominator is the more dangerous half, because a fix scoped to 'both homes' reads COMPLETE while three packages keep their own copy. || CONVERGENCE WORTH RECORDING: S1 (mirror_conversion.py, CVO) and S8 (mirror_schemas.py, DS~M) found the SAME five packages independently, from different questions. The converter family vendors as a unit; any file in it should be assumed five-homed until counted. || INERT IS CORRECT AND IT IS EARNED BY A CONTROL, NOT BY OPTIMISM: the seat checked WHERE the divergence sits (not in DECLARED) and WHETHER those packages touch blackdiamond keys (they do not) BEFORE calling it inert. An uncontrolled 'probably fine' on the same facts would have been a guess wearing a verdict's clothes. || SCOPE: this does NOT widen the P0 repair, which is blackdiamond-only. It widens any FUTURE contract edit to this family -- including S1's rename."
 },
 {
  "id": "MDPF_COTREMEDIATION-S9",
  "surfaced_by": "0.4.0_DS_ClientPlatform~M (msg 70819) -- EXERCISED, not predicted: they ran the 2026-08-19 file against their own new declaration and watched it refuse",
  "surfaced_at": "2026-08-25T17:11Z",
  "one_line": "After the contract edit, DECLARED[('blackdiamond','holdings')] expresses exactly ONE shape (21 cols), so replaying ANY pre-2026-08-20 partition now REFUSES with VendorDriftError -- and a backfill is the reflex remedy the MDPF_COTREMEDIATION PRD itself names, so someone will meet this.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "EXERCISED BY THE SURFACING SEAT: the 2026-08-19 file REFUSED with VendorDriftError under the new declaration -- the test that fails if the claim is false, not a config read",
    "mechanism is inherent to a single-declaration exact-tuple contract: one shape per (vendor,table) key, no version axis",
    "the seat established they did not introduce it -- it follows from the contract's existing shape, not from their edit",
    "the PRD names backfill as a remedy, which is what guarantees a future seat meets this"
   ]
  },
  "disposition": "GRADUATED",
  "notes": "STANDING: I CONSIDERED ARMED AND RULED INERT, AND THE REASONING BELONGS IN THE RECORD BECAUSE IT IS A CLOSE CALL. The case for ARMED: the PRD names backfill as the remedy, so a future ordinary act meets this. The case for INERT, which wins: IT FAILS LOUD. VendorDriftError raises, the seat sees it immediately, and nothing wrong lands. Compare S7, where the guard silently PASSES and lets fabrication through -- THAT is armed. Here the cost is time and a wrong expectation, not a corrupted artifact. Standing measures harm-through-normal-operation, not inconvenience. || THE ACTIONABLE HALF IS A DOCUMENT, NOT THE CODE: the PRD names a remedy that will refuse. Whoever owns the PRD should correct the remedy text before a seat burns a cycle discovering it. That is the cheap fix and it is why this was worth filing while cheap rather than when it fires. || NOTE THE SEAT'S OWN FRAMING, which is the right instinct: 'naming it while it is cheap rather than when it fires.' A trap named before anyone walks into it costs one line."
 },
 {
  "id": "MDPF_COTREMEDIATION-S10",
  "surfaced_by": "0.4.0_DS_ClientPlatform~M (msg 70819), handed over explicitly as 'not a claim, a pointer' -- found while discharging AC5, with the seat stating they have NOT read L4",
  "surfaced_at": "2026-08-25T17:11Z",
  "one_line": "A SECOND mdpf_revamp/ artifact exists beside the PRD's unread L4 lead -- global.meta.cottonwood_composed_backfill.source_key = 'gold/mdpf_revamp/cottonwood/aggregate_aua_timeseries_interpolated.json' -- suggesting mdpf_revamp/ is where cottonwood's COMPOSED artifacts live, which may be the whole of L4's 'real special case'.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "global.meta.cottonwood_composed_backfill.source_key = gold/mdpf_revamp/cottonwood/aggregate_aua_timeseries_interpolated.json, read from the artifact",
    "carries its own provenance: Andrew-direct 2026-07-28 sanctioned interpolated backfill, n_backfilled 44, first_measured_date 2026-07-20",
    "the L4 lead it sits beside: dim_mdpf_account_distribution.py:328 COTTONWOOD_UNITS_KEY = gold/mdpf_revamp/cottonwood/account_units.json, plus a _cottonwood_sidecar()",
    "EXPLICITLY NOT CLAIMED: the surfacing seat states they have NOT read L4 and are not asserting the connection -- and CTO's 70736 said the same of the original lead ('It is a LEAD, not a diagnosis. I have not read it.')"
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "TWO SEATS HAVE NOW DECLINED TO DIAGNOSE THIS AND BOTH SAID SO EXPLICITLY. CTO surfaced COTTONWOOD_UNITS_KEY as 'a LEAD, not a diagnosis -- I have not read it'; DS~M adds a second artifact under the same prefix and says 'I have NOT read L4 and am NOT claiming it.' The pointer is now stronger than either seat's claim, WHICH IS THE CORRECT STATE -- evidence accumulating without anyone inflating it into a conclusion. || WHAT IT IS WORTH: whoever reads L4 starts one step in, with two artifacts and a prefix hypothesis rather than one filename. That is the entire value of a pointer filed honestly. || UNDER_INVESTIGATION, not graduated: there is no mechanism here yet, only a location. Graduating it would put a remediation row on a hypothesis, which is what the grounding bar exists to prevent."
 },
 {
  "id": "MDPF_COTREMEDIATION-S11",
  "surfaced_by": "3.0.0_SA_CVO, answering 1.0.0_SA_CTO's discriminating question (pre-existing vs introduced-today) -- filed here because the finding it recovers was RECORDED in a deliverable and invisible to everyone working the P0 today",
  "surfaced_at": "2026-08-25T17:46Z",
  "one_line": "Global's coherence-gate refusal was diagnosed, named, quantified and lane-assigned in a CTO deliverable on 2026-08-24 -- same gate, same ~469-account round-trip, same 08-19/08-20 dates, explicitly called a correct refusal -- and the fabric rediscovered it from scratch during a live P0 the next afternoon, at the cost of a superseded dispatch and two withdrawn mechanisms.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260824_FABRIC_CLOSEOUT_LOG_THEN_PRDS.md @eb2be76858, committed 2026-08-24T13:41:45Z, heading 'OPEN FINDING CARRIED INTO THE PRD ROUND (not chased now)', VERBATIM: 'the CROSS-AXIS COHERENCE GATE refuses to emit (foreign-day roster signature: a ~469-account round-trip excursion on 08-19/08-20 exceeding net drift -- a roster imported from a different day than its values). Correct refusal; global stays down pending that data question (DS/CTO lane).'",
    "THE GATE IS NOT NEWLY ARMED: git -S over the gate text -> @f5c094434a, 2026-07-22, 0.4.0_DS_ClientPlatform, subject 'account_count from the SAME snapshot as the value -- drop the legacy served date-join that imported a foreign-day roster onto 2026-07-06'. Over a month old, and built for THIS EXACT CLASS on an earlier date",
    "THE 08-19 PARTITION IS ANOMALOUS AND PREDATES TODAY: gold/mdpf_revamp/_aggregate_aua/2026-08-19.json has 1 version, written 2026-08-19T23:33:16Z. CONTROLS on the same prefix: 2026-08-18 -> 2 versions newest 13:31:07Z; 2026-08-20 -> 2 versions newest 13:31:07Z. 08-19 is the only one of the three with a single version and the only one written outside the ~13:31Z producer window",
    "1.0.0_SA_CTO's run-log day-by-day (their measurement, cited with its invocation rather than re-run at this seat): mdpf-gold-lambda Invocations 08-17..08-25 = 1,1,1,1,1,1,1,1,3 -- no run missing, so every failure is a MEASURED outcome; global emitted 08-18/19/20, then SCOPE FAILED 08-21/22/23 as a CASCADE ('global fold SKIPPED: contributing leg(s) [cottonwood] failed'), then CROSS-AXIS COHERENCE GATE FAILED 08-24 and 08-25"
   ]
  },
  "disposition": "GRADUATED",
  "notes": "\u26d4 THE FILING WAS NOT THE FAILURE AND I WANT THAT ON THE RECORD FIRST. The 08-24 deliverable recorded the defect THE SAME DAY it first appeared (CTO's run logs show 08-24 is the first gate failure; the deliverable committed 13:41:45Z, minutes after that day's 13:31Z run), quantified it, called the refusal correct, and named a lane. That is prompt, accurate, complete filing. THE GAP IS THAT A DELIVERABLE IS NOT A QUEUE -- it was RECORDED and INVISIBLE, which is one worse than the state comp-surprise was built this hour to fix ('an item could be FILED AND INVISIBLE AT THE SAME TIME'). This one was never filed INTO the channel at all, so no aggregate view could ever have surfaced it. || WHAT IT COST, measured on today's traffic: a COO dispatch to re-run global gold, issued and superseded 35 seconds later; a CTO mechanism ('its own gold producer has not run') withdrawn by its author; my own mechanism ('still the 13:31Z scheduled write') withdrawn after MSTR caught the date I had formatted away. Three seats reasoning from artifacts about a condition whose diagnosis was twenty-eight hours old. || \u26a0 ONE CHARACTERISATION IN THAT DELIVERABLE IS NOW ITSELF UNDER QUESTION, AND I AM NOT CARRYING IT FORWARD AS SETTLED. It calls this 'an independent global defect', and COO's ruling today independently reached the same wording. CTO's run-log evidence points the other way: the mechanism CHANGED on 08-24 (cascade-skip 08-21/22/23 -> coherence gate 08-24/25), the gate's complaint names 2026-08-19 which is exactly the date cottonwood was frozen at, and folding cottonwood's frozen 08-19 slice against partners carrying current values IS a roster-from-a-different-day condition. If that holds, THE GATE IS A DOWNSTREAM DETECTOR OF THE SAME ROOT CAUSE AND NOT A SECOND DEFECT -- and it would be the ONLY instrument in the whole chain that noticed the freeze, while every freshness instrument read healthy for four days. CTO states it as a hypothesis and has NOT read the gate implementation; I am recording it the same way. THE SOURCE READ IS OWED AND IT IS DS~M's. || WHY THIS IS INERT: nothing is armed. The gate is refusing correctly, no bad data is emitting, and the finding is now visible. The harm already happened and is not recurring. || WHAT IT ARGUES FOR, and it is the channel's own thesis: a finding parked as 'not chased now' needs a HOME THAT SOMETHING READS. This one had a correct diagnosis, a quantification and a lane, and none of that reached the four seats who needed it the next day."
 },
 {
  "id": "MDPF_COTREMEDIATION-S12",
  "surfaced_by": "0.0.0_AB_MSTR (70865) as a P0 finding, consequence withdrawn by its author (70871); the reachability question then passed through 2.0.0_SA_COO, 0.5.0_AE_OpalETL~B (70945), MSTR again (70978) and 3.0.0_SA_CVO -- five seats, and it was never once filed into this channel until now",
  "surfaced_at": "2026-08-25T17:26Z",
  "one_line": "The silver contract fix is COMMITTED BUT NOT DEPLOYED to s3://opal-data-mdpf/code/scripts/silver/mirror_schemas.py -- a shared-home first-mint the safe-deploy membership guard correctly SKIPPED (404 = SKIP-NOT-MEMBER, loud) -- and the question that took five seats to settle is whether that absence is reachable by anything that runs.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "the 404 is real: s3://opal-data-mdpf/code/scripts/silver/ holds exactly 2 objects (rebalancer_schemas.py 12,553 B, build_fact_taxsma_report.py 30,788 B); mirror_schemas.py absent. Prefix populated + negative control 404s, so the absence is measured",
    "mechanism at source, safe_deploy_core.py:60-61: SHARED-HOME layers deploy under the S3-MEMBERSHIP GUARD -- key-exists = update (enforced); 404 = SKIP-NOT-MEMBER, loud. THE GATE DID ITS JOB",
    "THE PREFIX IS CONSUMED (0.5.0_AE_OpalETL~B, proven at source, correcting CVO): mdpf-daily-dispatch.sh:29 CODE_PREFIX=\"code\"; :125 aws s3 sync s3://${MDPF_BUCKET}/${CODE_PREFIX}/scripts/ $SCRIPTS_DIR/ --delete; :546 COT_PYPATH includes ${SCRIPTS_DIR}/silver",
    "BUT THE ABSENT FILE IS NOT REACHABLE (CVO trace): of 17 python invocations in the dispatch, EXACTLY THREE carry PYTHONPATH=${COT_PYPATH} (:554/:555/:556). Their full transitive closure is 8 modules. mirror_schemas occurrences across the closure: 0 in seven; 1 in rebalancer_schemas.py -- AT LINE 3, IN THE MODULE DOCSTRING ('Sibling of etf_schemas.py / mirror_schemas.py'), PROSE NOT AN IMPORT. Positive control mirror_conversion.py = 7 occurrences, so the census discriminates",
    "the one silver module the runner DOES execute is rebalancer_schemas -- PRESENT, current (12,553 B repo == S3), and its only import line is 'from __future__ import annotations'. The chain terminates there",
    "DYNAMIC-IMPORT AND SHELL-OUT GAPS CLOSED (0.5.0_AE_OpalETL~B 70999): AST scan over all 8 closure modules for __import__/importlib/exec/eval and os.system|popen/subprocess.* -> dynamic=0, shell=0, 8 parsed, 0 parse failures. Detector proven to FIRE on three controls (.tools/commit_gate_runner.py dynamic=4 shell=1; audit-archive-invoker.py; deploy-import-lint.py) and stay silent on a negative control"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "NOT A HAZARD, MEASURED ON BOTH PLANES. Every mirror_schemas importer is silver-layer and executes inside Lambdas from VENDORED packages that never read S3 at runtime; the EC2 runner that DOES consume the prefix reaches the absent file through no static, dynamic, or shell path across its full 8-module closure. The membership guard's skip is therefore correct AND permanent for this file. No remediation is owed; the deploy behaved as designed.",
  "notes": "\u26d4 THE REASON THIS IS FILED AT ALL, GIVEN IT DISMISSES: FIVE SEATS SPENT THIS QUESTION IN MESSAGES AND IT WAS NEVER FILED. It generated a P0-severity claim that was withdrawn by its author, a wrong 'no consumer' answer from me, a correction from AE~B, a narrowing from MSTR, and two rounds of limit-closing. All of it lived in a thread. S11 says a deliverable is not a queue; THIS ONE DID NOT EVEN REACH A DELIVERABLE. Dismissed items are still the record that stops the next seat re-deriving. || \u26a0 THE LATENT CONDITION IS THE HALF WORTH CARRYING, AND IT IS MSTR'S: THE RUNNER SYNCS WITH --delete. Today's verdict is a claim about TODAY'S SOURCE, not a permanent property. THE MOMENT ANY GOLD LEG IMPORTS A SILVER CONVERSION MODULE THAT IMPORTS mirror_schemas, THIS FLIPS TO A LIVE FAILURE -- and it flips silently, because the deploy guard will keep correctly skipping a first-mint nobody has minted. RE-OPEN TRIGGER, stated so it is testable: any new import of a silver conversion module (mirror_conversion, etf_conversion, etf_schemas, mirror_schemas) from anything under data/*/scripts/gold/. || THREE INSTRUMENT LESSONS, one per seat, all self-reported: (1) MINE -- comp-find over 'code/scripts/silver' was correctly executed and STRUCTURALLY BLIND, because the path is assembled at runtime from ${CODE_PREFIX} and never exists as a literal; my 'no consumer' conclusion was a DELETION WARRANT resting on a search that could not have hit. (2) MINE -- I corroborated that blind spot with a July DAG-coverage finding and read the agreement as confirmation, when both were silent for unrelated reasons. (3) AE~B's -- their first dynamic-import sweep returned the same 8 CLEAN rows with a POSITIVE CONTROL THAT DID NOT FIRE, and they re-ran rather than send it. A clean sweep from a detector that has never fired is indistinguishable from the real result."
 },
 {
  "id": "MDPF_COTREMEDIATION-S13",
  "surfaced_by": "0.4.0_DS_ClientPlatform~N (71095) as OBSERVATION/INERT, explicitly declining to trace whether a served key publishes the total; adjudicated to ARMED by 3.0.0_SA_CVO on that trace; one limb INVERTED by 1.0.0_SA_CTO (71115) who re-measured all four partners before ruling",
  "surfaced_at": "2026-08-25T18:25Z",
  "one_line": "ONE SERVED FIELD NAME, THREE DIFFERENT DERIVATIONS, ONE LABEL: account_count_total is NOT the by_model sum for cottonwood (317 vs 472), IS exactly the sum for 49financial and inflection, and is the sum on 410 of 458 dates for global -- and all four carry count_basis 'measured', so a client comparing account counts across partners is comparing three different quantities under one name.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "the producer's own meta.count_axis_note, quoted by the surfacing seat: 'account_count is per-model and fans out +1 per underlying model on a blend; summing it across models double-counts (447 vs 296 on 2026-07-22). NEVER TOTAL THIS COLUMN.'",
    "CVO identity test, per date, served vs sum-over-by_model: 49financial 413 of 413 comparable dates IDENTICAL (100%); global 410 of 449 (91%); cottonwood 0 of 18",
    "CTO re-measurement of all four served payloads at latest date -- total / raw / sum_by_model / models: 49financial 7,144 / 7,144 / 7,144 / 5; inflection 548 / 548 / 548 / 7; global 8,242 / 8,242 / 8,242 / 9; cottonwood 317 / 317 / 472 / 5",
    "SERVED SURFACE CONFIRMED: account_count appears in 12 of 14 served mdpf keys (manifests + archive excluded), all four partners; negative control token appears in 0 of 14",
    "SECOND INDEPENDENT TELL (CTO): account_count_total and account_count_total_raw are BYTE-IDENTICAL on 49financial, inflection and cottonwood (0 differing dates each) and differ on 48 dates for global only"
   ]
  },
  "disposition": "GRADUATED",
  "disarm_owner": "2.0.0_SA_COO -- the seat who can act now; the disarm is a decision about a served field's label/derivation, NOT a code change, and per the sequencing rule applied five times today it must NOT ride the global repair. CTO may rule on architecture grounds.",
  "notes": "\u26d4 THE ATTRIBUTION INVERTED UNDER MEASUREMENT AND THE CORRECTED SHAPE IS STRONGER. I reported 49financial's 413/413 identity as the exposure and dismissed cottonwood's 0-of-18 as 'a different composition path'. CTO read the DIRECTION I did not: cottonwood's served total is 317 against a by_model sum of 472 -- 155 LOWER, exactly the direction the producer's note predicts for NOT fanning out, same magnitude class as its own 447-vs-296 sample. SO COTTONWOOD IS THE PARTNER THAT HEEDS 'NEVER TOTAL THIS COLUMN'; 49financial AND INFLECTION ARE THE ONES THAT DO NOT. THE ARTIFACT CARRYING THE WARNING IS THE ONE OBEYING IT. || MY MISS, NAMED BECAUSE IT IS THE SAME CLASS TWICE IN ONE SESSION: I HAD THE DISCRIMINATING NUMBER AND DID NOT OPEN IT. '0 of 18' told me cottonwood differed; whether it was HIGHER or LOWER was the whole finding, and I labelled it instead of reading it. Identical to the rebalancer_schemas docstring hit earlier today, where the count was 1 and the meaning was in the line. A count you did not read is a count of the pattern's accidents. || WHY THE INVERTED VERSION IS THE ONE TO CARRY: a single wrong number on one partner is a bug. THREE DERIVATIONS UNDER ONE FIELD NAME WITH ONE LABEL DEFEATS THE OBVIOUS SANITY CHECK -- cross-partner comparison is exactly what a reader would do to catch a bad account count, and here it is the thing that hides it. Invisible at the point of use. || THE _raw TELL IS A SEPARATE FINDING RIDING ALONG: a declared raw-vs-derived distinction that never materialises on three of four partners is either a dead code path or a silently skipped step. It is capable of differing (global does, on 48 dates) and does not. || ARMED because the platinum publisher runs daily and re-emits every one of these fields to a client-facing surface; that is harm through future NORMAL operation. Class stays OBSERVATION -- it stops nobody's current work. || \u26a0 NOT CLAIMED BY ANY SEAT: the MAGNITUDE of the overstatement. The ~1.5x fan-out is the ARTIFACT'S OWN figure on one sampled date, quoted and re-derived by nobody. NOT CLAIMED: what the portal RENDERS -- a served key is not a rendered number, and that is a different plane. NOT CLAIMED: whether the fan-out note applies to the 49F/INF legs; only cottonwood's meta was read. || ROUTES TO D8 (Model Portfolios Pipeline Fortification) as 'in pattern' work, NOT to the outage repair, whose scope COO discharged at 17:5xZ."
 },
 {
  "id": "MDPF_COTREMEDIATION-S14",
  "surfaced_by": "3.0.0_SA_CVO, on its own get_live_agents + ps reads at 13:30:54Z and 13:43Z, while adjudicating the seat-death evidence in 2.0.0_SA_COO's 72152",
  "surfaced_at": "2026-08-26T13:44Z",
  "one_line": "A PID IS A LIVENESS ORACLE ONLY AT THE INSTANT IT IS READ, AND THIS BOX REUSES PIDS INSIDE 17 MINUTES: 2.0.0_SA_COO correctly certified 0.7.0_AE_CloudOps~G dead at 13:26Z partly on 'pid 26224 absent from ps', and at 13:43Z pid 26224 is LIVE and belongs to 0.4.0_DS_ClientPlatform~R -- so re-running that same limb now returns PRESENT and would read as ~G resurrected.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "3.0.0_SA_CVO -- disarmed same-turn by stating the rule wherever the death certificate is cited: a PID limb carries its READ TIME or it is not evidence, and a PID that reappears must be re-resolved to its CURRENT serial before it is read as the old one.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "2.0.0_SA_COO 72152 section 1, verbatim: 'pid 26224 (~B's 13:01:55Z LIVE reading) -> absent from ps'. Correct at 13:26Z; that is not disputed here.",
    "3.0.0_SA_CVO own get_live_agents at 2026-08-26T13:43Z: '0.4.0_DS_ClientPlatform~R [LIVE] (PID 26224, 5s ago)'. Same integer, different serial, 17 minutes later.",
    "3.0.0_SA_CVO own ps -ef read at 2026-08-26T13:30:54Z: inbox-watch.sh streams present for 2.0.0_SA_COO, 1.0.0_SA_CTO, 1.0.0_SA_CTO~X only -- no ~G, no ~B, no CVO. That limb is time-stamped and does not decay the same way, because it matches on the SERIAL, not on an integer the OS recycles.",
    "The correct four-instrument verdict of 72152 STANDS. This item does not dispute it and no re-adjudication follows from it."
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "THE SHAPE, and it is why this is filed rather than mentioned: the PID limb is ANTI-CORRELATED WITH TIME. Every other limb of a death certificate gets no weaker as the corpse cools -- a missing watcher stays missing, a broker roster stays empty. The PID limb gets ACTIVELY WRONG, and it flips to the answer that says the dead seat is ALIVE, which is the direction that stops an investigation rather than starting one. A seat re-deriving ~G's death tomorrow from 72152's four limbs would find three agreeing and one contradicting, and the contradicting one is the concrete-looking one. Same family as the orphan watcher already recorded in the /watcher doctrine (a process-table fact standing in for an agent-liveness fact); this is that family's TIME axis rather than its CONSUMER axis. Cost of the rule: one clause per PID citation. Does not apply when the PID and the read are in the same turn."
 },
 {
  "id": "MDPF_COTREMEDIATION-S15",
  "surfaced_by": "2.0.0_SA_COO (72152 section 1, its own line and its own framing); FILED by 3.0.0_SA_CVO as channel owner, which is a filing act and not a re-derivation",
  "surfaced_at": "2026-08-26T13:44Z",
  "one_line": "THE WAVE AWARDED THE SAME ACCEPTANCE READ TWICE TO A SEAT THAT WAS ALREADY GONE: three seats (0.7.0_AE_CloudOps~G, 0.5.0_AE_OpalETL~B, and 2.0.0_SA_COO's predecessor) died inside roughly 30 minutes, and a liveness check that was CORRECT when taken did not survive 25 minutes to the dispatch it justified.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "2.0.0_SA_COO 72152 section 1, verbatim: 'This is the SECOND instance today of an acceptance addressed to a seat that is not there'.",
    "2.0.0_SA_COO 72152 section 1, verbatim: '0.5.0_AE_OpalETL~B checked at 13:01:55Z and found it structurally present. That check was correct and it did not survive 25 minutes.'",
    "2.0.0_SA_COO 72152 opening, verbatim: 'My predecessor died ~13:10Z.'",
    "3.0.0_SA_CVO own ps -ef at 13:30:54Z independently confirms the ABSENCE half for ~G and ~B: no inbox-watch.sh stream for either serial.",
    "RELAY DISCIPLINE: the ~G and predecessor death TIMES reach this item only through 72152 and are carried as that seat's measurement, not re-derived by the filer."
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "2.0.0_SA_COO's own sentence is the finding and it is quoted rather than paraphrased: a liveness check is a reading of a MOMENT, not a property of the wave. INERT because the wave self-corrected inside one dispatch cycle -- the re-seat to 1.0.0_SA_CTO landed with 24 minutes of margin, the perishable pre-state turned out to live in the MESSAGE RECORD rather than only on the dead seat's disk, and the recovery cost the wave nothing. Filed because the RATE is what is unmeasured: three deaths in thirty minutes is either a bad half hour or a condition, and those are byte-identical from one sample. No action requested and nothing is held on this."
 },
 {
  "id": "MDPF_COTREMEDIATION-S16",
  "surfaced_by": "3.0.0_SA_CVO, from its own read of the gold run manifest during the 13:50Z independent acceptance read",
  "surfaced_at": "2026-08-26T14:00Z",
  "one_line": "THE GOLD RUN MANIFEST RECORDS reconciliation PASS ON A RUN THAT BUILT 6 OF 12 OBJECTS AND LOST 2 OF 4 SCOPES: the failures are fully and honestly recorded in errors{}, and scopes{} -- the field shaped like a status -- does not know about them, so a consumer branching on reconciliation gets GREEN off the same document that carries the traceback.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "0.6.2_AE_PartnerETL~A as the D8/MDPF_COTREMEDIATION P0 owner, routed by 2.0.0_SA_COO. DISARM IS NOT REMEDIATION here: the disarm is that no automated consumer is known to branch on scopes.reconciliation today, so the wrong-green is currently read only by humans who also see errors{}. Remediation is a per-scope reconciliation record and is NOT authorized by this item.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "s3://opal-data-assets/portal/gold/mdpf/_manifests/2026-08-25/20260826T133106Z.json, read by 3.0.0_SA_CVO at 2026-08-26T13:55Z",
    "run.a4_objects_built = 6 beside run.a4_expected = 12, in the same object",
    "scopes = one record only, _aggregate_aua with reconciliation PASS -- no per-scope entry for either scope that failed",
    "errors keys = cottonwood and global -- both carry full tracebacks in the SAME document",
    "run.code.commit = 1daf1913dd38a97186df3b6d9fb9d44057f6221a, module mdpf_gold_consolidator"
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "THIS IS THE VALUE-MUST-CARRY-ITS-CLAIM SHAPE AT THE RUN LEVEL, and it is the honest-producer variant, which is the harder one. Nothing here is hidden: the run wrote its own partial count and its own tracebacks. The defect is that ONE field in the document answers a narrower question than its name suggests, and it is the field a consumer would reach for. a4_objects_built 6 beside a4_expected 12 IS the sound pair, and nothing downstream reads it. AND THE ORDER MATTERS: a consumer that reads reconciliation is not being careless, it is reading the field named for the question it is asking. The producer must make the wrong answer inexpressible rather than rely on the consumer reading a different field. Sibling of S17, which is the same class one plane downstream, on the served payload rather than the run record."
 },
 {
  "id": "MDPF_COTREMEDIATION-S17",
  "surfaced_by": "3.0.0_SA_CVO, measured leaf-field diff of its own pre (13:35Z) and post (13:52Z) captures of the four served payloads",
  "surfaced_at": "2026-08-26T14:00Z",
  "one_line": "THE 13:50Z PUBLISHER STAMPED TODAY'S written_at ONTO YESTERDAY'S DATA FOR global AND cottonwood: the ONLY changed leaf in each is _provenance.written_at (1 of 20,345 and 1 of 11,960), as_of_last stayed 2026-08-24 and source_keys still names the 2026-08-24 gold input -- so every freshness signal on the served plane now reads CURRENT on two stale payloads.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "3.0.0_SA_CVO -- disarmed same-turn by publishing the discriminating rule to every seat that reads this surface (72183/72184/72185): on this key, freshness is as_of_last AND _provenance.source_keys, NEVER written_at and NEVER object mtime. Remediation is the cottonwood by_model canonical key (D8, 0.6.2_AE_PartnerETL~A) -- a different owner and a different clock.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "3.0.0_SA_CVO own s3api GET of all four served payloads at 13:35-13:36Z (pre) and 13:51-13:52Z (post), s3://opal-data-portal-v2/platinum/mdpf/{scope}/aggregate-aua-timeseries.json",
    "global: 1 changed leaf of 20,345 -- _provenance.written_at 2026-08-25T19:46:02Z to 2026-08-26T13:50:49Z; as_of_last 2026-08-24 UNCHANGED; n_dates 461 UNCHANGED; source_keys still names 2026-08-24.json",
    "cottonwood: 1 changed leaf of 11,960 -- identical shape, written_at to 2026-08-26T13:50:49Z, as_of_last 2026-08-24 UNCHANGED",
    "CONTROL, both arms, on the differ itself before it was trusted: identical input gives 0 deltas and UNMOVED; a planted as_of_last plus written_at advance gives PASS. The two arms are reachable from different truths.",
    "POSITIVE CONTROL on the same instrument in the same run: 49financial and inflection DID advance (as_of_last to 2026-08-25, source_keys to 2026-08-25.json, 55 and 47 changed leaves), so the UNMOVED verdict is not an instrument-wide null."
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "PRE-REGISTERED AND THEN OBSERVED. 2.0.0_SA_COO's 72152 s.4 named this exact case in advance as the one that looks most like success -- and the estate's own prior CVO record (72147) put it the other way round, as_of_last advancing while written_at does not. TODAY IT CAME OUT THE OPPOSITE WAY: written_at advanced and as_of_last did not. Both halves of the pair are now observed, which is why the bar has to be BOTH-AND and never either-or. NOTE WHAT THE REPUBLISH COST: before 13:50Z global and cottonwood carried a written_at of 2026-08-25T19:46Z, visibly a day old, which would have made a reader ask. After it they carry today's timestamp on the same bytes. The republish did not corrupt the data and it did not fix it -- it removed the only surface signal that anything was wrong. That is the estate's own recorded principle in a new place: a missing marker makes a reader ask, a false one makes them stop asking. Two of four partner surfaces are in that state now and stay there until the D8 cottonwood key lands."
 },
 {
 "id": "MDPF_COTREMEDIATION-S18",
 "surfaced_by": "0.7.0_AE_CloudOps~Z, msg 9174, routed SAME-TURN to the spec issuer 1.0.0_SA_CTO~Z with this seat cc'd as channel owner (Rule 27 BLOCKING routing, correctly executed)",
 "surfaced_at": "2026-08-27T15:08Z",
 "one_line": "R2 IS ALREADY BUILT -- on the EventBridge SCHEDULER plane, which `aws events list-rules` structurally cannot enumerate: `cot-bd-session-daily-et` is ENABLED, `cron(30 7 * * ? *)` pinned to America/New_York, targeting `cot-bd-session-trigger` with `{\"mode\":\"session-refresh\"}`, so building R2 as specified would land a DUAL TRIGGER and re-introduce the exact DST drift the Scheduler was chosen to prevent.",
 "class": "BLOCKING",
 "hazard_standing": "ARMED",
 "disarm_owner": "1.0.0_SA_CTO~Z as the spec issuer. DISARMED SAME-TURN by the surfacing seat itself -- 0.7.0_AE_CloudOps~Z built nothing, applied nothing, and held R2 pending amendment, while proceeding on R1 which the spec authorises independently. ⛔ DISARM IS NOT REMEDIATION: the spec's line 'the COT chain currently has no schedule of its own' is still on the page, and it is TRUE within the Rules plane, so a successor re-reading it re-arms the hazard with a correct-looking citation. Remediation is the spec amendment (recommendation on the table: 'already satisfied by cot-bd-session-daily-et; verify + document, build nothing'), and it is NOT authorized by this item.",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "0.7.0_AE_CloudOps~Z, live primitive `aws scheduler get-schedule --name cot-bd-session-daily-et` (not a config read, not Terraform): State ENABLED, ScheduleExpression cron(30 7 * * ? *), ScheduleExpressionTimezone America/New_York, Target.Arn arn:aws:lambda:us-east-1:313476888478:function:cot-bd-session-trigger, Target.Input {\"mode\":\"session-refresh\"}",
   "DENOMINATOR PRINTED BY THE SURFACING SEAT: 18 schedules materialised account-wide; cot-bd-session-daily-et is one of them",
   "NEGATIVE CONTROL ON THE OTHER PLANE, re-run by the surfacing seat and reproducing the issuer's census EXACTLY: 137 rules total, 17 matching cot/49f, `cot-bd-session-daily` and `bd-cot-session-daily` both genuinely ABSENT. The issuer's census was correct and complete ON ITS OWN PLANE.",
   "infra/aws/terraform/cot-pipeline/eventbridge.tf records the old cron(0 2)Z Rule deleted IN THE SAME CHANGE as the Scheduler was created, explicitly so there is 'no dual-trigger window'",
   "Andrew-direct 2026-07-29 chose Scheduler over a Rule because a Rule is UTC-only and a hardcoded UTC cron drifts an hour at DST, firing BEFORE market close come November",
   "FILER DID NOT RE-DERIVE. Re-running get-schedule would be the same instrument twice; this item carries 0.7.0_AE_CloudOps~Z's measurement as that seat's, per the Rule 22 repetition-is-not-corroboration clause."
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "notes": "THIS IS THE WRONG-PLANE CLASS, AND IT IS THE HIGH-QUALITY VARIANT: a clean, confident, well-formed ZERO about the plane the answer does not live on. EventBridge exposes two non-overlapping APIs -- `events list-rules` enumerates RULES, `scheduler list-schedules` enumerates SCHEDULES -- and a census over either is silent about the other while printing a denominator that LOOKS total. The issuer's 137-rule sweep was not careless; it was correct, complete, and unable to contain the answer. ⛔ THE CONTROL THAT WOULD HAVE CAUGHT IT IS NAMING THE QUESTION'S PLANE BEFORE THE SWEEP'S -- no control placed inside the wrong plane catches a wrong-plane error, which is CLAUDE.md's own retrieval law. WHAT MAKES IT WORTH A ROW RATHER THAN A CORRECTION: the caution the spec attached to R2 (preserve the ~11:30Z landing because ET-boundary timing is a DATA-CORRECTNESS parameter) is SATISFIED BY THE LIVE SCHEDULER AND WOULD HAVE BEEN VIOLATED BY THE BUILD -- a UTC cron(30 11) meets it today and breaks it on 2026-11-01. The spec's own protective clause was the thing the spec's own remedy would have broken, and only a read on the other plane can see that."
 },
 {
 "id": "MDPF_COTREMEDIATION-S19",
 "surfaced_by": "0.7.0_AE_CloudOps~Z, msg 9242, explicitly SURFACED-NOT-CHASED with this seat named as channel filer and 1.0.0_SA_CTO~Z as D8 owner",
 "surfaced_at": "2026-08-27T16:09Z",
 "one_line": "TWO CARRIES ON THE SERVED `global` AGGREGATE THAT NO HYPOTHESIS ON THE BOARD EXPLAINS: `2026-07-29 <- 2026-07-27` (2 trading days) and `2026-07-30 <- 2026-07-27` (3 trading days), both PREDATING the 2026-08-14 kill and neither landing on a mint day, so the mint-day chain break cannot be their cause -- and a 3-trading-day carry on a client-facing aggregate is a shape a T+1 cadence cannot produce.",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "disarm_owner": "1.0.0_SA_CTO~Z as D8 owner. ⛔ NOT DISARMED AT FILING, and the filer is stating the BASIS of the ARMED call rather than leaving it to read as measured: ARMED rests on the mechanism being UNKNOWN, not on a demonstrated live one. INERT would assert that normal operation is safe, which nothing here establishes either. THE MEASUREMENT THAT MOVES IT: re-run `lib.trading_calendar.trading_days_behind` over the ~20 trading days since 2026-07-30 -- a clean run with no further anomaly makes the condition expired-or-historical and the item INERT; a recurrence makes it live and re-classes it. That measurement is the channel's, not the D8 owner's, and this seat holds it.",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "0.7.0_AE_CloudOps~Z resolved the gaps with `lib.trading_calendar.trading_days_behind` rather than a weekday count -- calling a gap anomalous without resolving the trading calendar is NEVER#1's own error, and the trading-calendar resolution is what turned two ordinary-looking rows into anomalies",
   "MEASURED SPLIT WITH ITS DENOMINATOR: of 9 carries examined, 3 are anomalous (07-29<-07-27 = 2 td; 07-30<-07-27 = 3 td; 08-21<-08-19 = 2 td) and the other 6 are ordinary T+1",
   "DISCRIMINATING CONTROL, supplied by 0.0.0_AB_MSTR~Z and accepted by the surfacing seat: ['08-04','08-03'] and ['08-12','08-11'] carry from PRE-KILL mint days where bronze provably RAN (SSM Success, both) -- the same pattern appears where there was no failure, which killed the original 4-for-4 corroboration claim outright",
   "2026-07-27 IS NOT A MINT DAY (mints: 08-03, 08-11, 08-19, 08-27) and both carries PREDATE the 2026-08-14 kill, so the R1 mechanism is excluded by construction rather than by argument",
   "NEGATIVE SPACE NAMED BY THE SURFACING SEAT: 07-29 and 07-30 appear in the list 0.0.0_AB_MSTR~Z printed in msg 9234 and were classified there as ORDINARY -- they were in front of two seats and read as unremarkable until the calendar was resolved",
   "FILER DID NOT RE-DERIVE. Carried as 0.7.0_AE_CloudOps~Z's measurement; the filing is not a second instrument."
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "notes": "⛔ THE OBSERVATION IS GROUNDED AND THE MECHANISM IS ABSENT, AND PROTOCOL SECTION 2 KEEPS THOSE APART: the anomaly graduates nothing until a mechanism is attributed at source, so this row CANNOT seed a remediation and is not a backlog item anyone works. WHY IT IS FILED RATHER THAN DROPPED: it survives the only two explanations on the board. It is not R1 (predates the kill, not a mint day) and it is not the ordinary cadence (2 and 3 trading days). An anomaly that outlives every live hypothesis is the one worth a durable row, because the next seat to meet it will otherwise meet it as a first observation. WHAT IT INHERITS FROM S16/S17: the reporting gap is the same one this round keeps finding -- a PASS verdict is about `as_of_last` and write freshness and is SILENT on whether a contribution is REAL or CARRIED, and no instrument in the chain reports the difference; you have to open the payload and read `cohort_provenance`. So a carry of any length is invisible to every automated surface, which is precisely why two of them sat unnoticed for a month in a list two seats had already read. ⚠ PROVENANCE OF THE ROUND ITSELF, recorded because it bears on how much weight this row can take: the surfacing seat reached this by RE-MEASURING after a challenge falsified its previous corroboration, and it named its own error mechanism -- looking for a second instrument only AFTER being convinced, and never asking what that instrument says on days the conclusion is false. The retraction and this finding arrived in the same message; the retraction does not weaken the finding, and the finding does not rehabilitate the retraction. || \u26d4 MEASUREMENT RUN 2026-08-27 ~17:2xZ BY 3.0.0_SA_CVO~Z, THE CHANNEL SEAT THAT HELD IT. RESULT: NO NEW ANOMALY. Recommend INERT; the DISARM ACT remains 1.0.0_SA_CTO~Z's as D8 owner -- this seat ran the measurement the item names and does not self-disarm. || WINDOW: exactly 20 trading days 2026-07-30..2026-08-26 (the item's '~20'), measured on the SERVED object portal/gold/mdpf/global/aggregate-aua-timeseries/2026-08-26.json. IN-WINDOW: 5 carries, 1 anomalous (2026-08-21 <- 2026-08-19 = 2 td) -- AND THAT ROW WAS ALREADY IN THIS ITEM'S OWN RECORDED EVIDENCE AT FILING. ZERO anomalies newer than the filing. || POSITIVE CONTROL: the same instrument reproduced the two known anomalies exactly (07-29 <- 07-27 = 2 td; 07-30 <- 07-27 = 3 td), so the clean window is a MEASURED NEGATIVE, not a dead instrument -- a run that found nothing anywhere would have been indistinguishable from a broken one. || TWO DISCRIMINATORS AGREE on the carry set: (a) as_of_by_partner < row date, (b) the claim string starting 'carried'. Both return the SAME 8 rows, so neither a silent None nor a mislabelled row is hiding a carry. Claim vocabulary censused: cottonwood {absent 391, interpolated_estimate 44, measured 20, carried_at_declared_cadence 8}. || \u26d4 THE 9-vs-8 APPARENT DISCREPANCY WITH 0.7.0_AE_CloudOps~Z IS RESOLVED AND IS NOT A CONFLICT -- IT IS TWO VINTAGES OF ONE KEY, AND NEITHER SEAT WAS WRONG. The served key carries TWO versions: 13:31:13Z (311519 B) and 16:27:52Z (311363 B). The surfacing seat observed at 16:09Z, i.e. THE 13:31 BYTES; this run first read the 16:27 bytes. Re-measured on THEIR version: 9 carries / 3 anomalous -- EXACTLY their figures. The single delta is 2026-08-26 cottonwood as_of=2026-08-25, an ORDINARY T+1 carry on the HEAD row that healed when the day's real data landed. NO ANOMALY WAS HEALED; all three persist in both versions. Their count was right for their vintage and this one is right for its own. THE TRANSFERABLE HALF: a served key is not a plane until you name its VERSION -- an 18-minute gap between two seats' reads turned two correct counts into a clean-looking numeric contradiction. || \u26d4 AND THE DISARM CRITERION AS WORDED CANNOT PASS ON A LITERAL READING. The window 'since 2026-07-30' CONTAINS 08-21, which this item's OWN evidence already classifies anomalous. Read literally ('no anomaly in the window') the criterion could never return clean no matter what the world did; read as written ('no FURTHER anomaly') it passes. The intended reading is the second -- the filer knew of 08-21 and chose the window anyway -- and it is recorded here so a successor does not re-run this measurement forever against a criterion that structurally cannot discharge. || ONE SUBSTANTIVE DISTINCTION THE ITEM DID NOT DRAW, AND IT IS WHY THE IN-WINDOW ANOMALY IS NOT A RECURRENCE: 2026-08-19 IS A MINT DAY (mints 08-03, 08-11, 08-19, 08-27) while 2026-07-27 IS NOT. So 08-21 <- 08-19 carries FROM a mint day and HAS a live candidate mechanism in the mint-day chain break; the 07-27 pair has none, which is precisely what made them the unexplained ones. The in-window anomaly is therefore a DIFFERENT SHAPE, not a repeat of the shape this item was opened for. || INSTRUMENT: lib.trading_calendar.trading_days_behind, calendar source NYSE/hardcoded-fallback-2024-2027. DENOMINATOR: 463 cohort_provenance rows x 3 partners = 1389 (row,partner) cells."
 },
 {
   "id": "MDPF_COTREMEDIATION-S20",
   "project": "MDPF_COTREMEDIATION",
   "fabric": "laptop",
   "surfaced_by": "0.7.0_AE_CloudOps~V",
   "surfaced_at": "2026-09-22T14:40:00Z",
   "one_line": "The 2026-09-22 12:53Z qa_local crash of the 74d7efe144 build (rollback recommended on it, executed 13:25Z on Andrew's Go) was a DRY-RUN VINTAGE-PIN ARTIFACT, not a production hazard: run_cottonwood_family's dry_run branch pins the slice/pair to the newest LANDED gold dim partition (09-18) while the axis runs to 09-21, and two LATENT readers then failed on the trailing None -- (1) _shape_category_views's float(v[-1]) (Andrew's 09-11 guard 1465fd3f7d, on CLOUD but NOT in the running 48b8671569 pin nor the 74d7efe144 pin), (2) _cot_roll_forward_map skipping a covered-but-valueless date so the global fold's coherence gate (v) refused. Custom (Opal*) model processing is NOT a cause.",
   "class": "OBSERVATION",
   "hazard_standing": "ARMED",
   "disarm_owner": "0.7.0_AE_CloudOps~V",
   "disposition": "UNDER_INVESTIGATION",
   "grounding": {
     "status": "GROUNDED",
     "evidence": [
       "mdpf_gold_consolidator.py run_cottonwood_family (@74d7efe144 :1113-1160): the dry_run branch reads back the newest LANDED gold dim partition instead of staging today's, so a qa_local run at 12:53Z saw cottonwood values ending 2026-09-18 under an axis ending 2026-09-21; the production branch builds today's partition first (bdmp.main --date <adate> --upload) and does not carry that gap. Reproduced offline on the deployed bytes (.scratch/mdpf_qa/full_log.txt) and on the Phase A+B bytes at today's vintage: 15 of 16 A4 objects (.scratch/mdpf_qa/offline_build_all.txt), the 16th absent on the COTTONWOOD SIDECAR STALE gate (account_units.json value_date 09-15, itself a dry_run artifact: the pair writes the sidecar only under --upload).",
       "Reader (1): CLOUD 1465fd3f7d (2026-09-11) `_last` returns None on a null latest cell and _shape_category_views WITHHOLDS the scope; git merge-base --is-ancestor 1465fd3f7d 48b8671569 -> NOT an ancestor, so the Lambda running since the 09-15 pin has lacked the guard; the 09-21 hotfix pin 74d7efe144 (minimal over 48b8671569) inherited the gap. Carried into the fix-forward pin @3756c846a4 (cherry-pick, conflict resolved to the 09-11 text); tests/test_category_views_null_tail_guard.py 6 of 6 on the pin.",
       "Reader (2): dim_mdpf_aggregate_aua_timeseries.py _cot_roll_forward_map skipped every `d in cot_covered` date unconditionally; a date with a count partition and no value partition (the measured 09-21 shape) was left value=None beside a real count and the global fold's cross-axis coherence gate refused GLOBAL (.scratch/mdpf_qa/global_diag.txt). Fixed to skip only a covered date WITH a value: hotfix 47e00fa9ad, CLOUD @ebd2370ee9 merged @ac571ef0c7; tests/test_frontier_lag_trailing_none.py arm 2 (4 cases, old loop inline as negative control) 5 of 5.",
       "The rollback itself: ledger 20260922T1321Z_mdpf-cottonwood-autocustom-rollback-20260922 CLOSED @02a91c794d; the 13:30Z fire on the restored 48b8671569 wrote 8 of 16 (manifest 20260922T133114Z), i.e. the pre-deploy behaviour, not a recovery -- the rollback removed Phase A+B for nothing the production path would have hit. Owned to Andrew and to 1.0.0_SA_CTO / 2.0.0_SA_COO~B (msgs 99513/99514)."
     ]
   },
   "spec_asserts": "A qa_local run is the QA instrument for a pin (CTO ruling 015625Z): 'runs the FULL build with dry_run semantics' -- read as: what qa_local produces is what the scheduled production fire would produce, minus the S3 writes.",
   "world_is": "qa_local is NOT vintage-equivalent to production for cottonwood: its dry_run branch pins to the last LANDED gold dim partition and never refreshes the pair's sidecar, so a qa_local run on a day whose cottonwood partition has not landed reads a trailing-None frontier and a stale sidecar that the production branch would not. A qa_local crash on that shape is a LATENT-READER finding, not a production-fire prediction; this seat read it as the latter and recommended a rollback on it. The two readers were real defects (both fixed in the fix-forward pin), but the 13:30Z production fire on 74d7efe144 would have reached the same two readers only if the production cottonwood build had ALSO left a trailing None, which it does not by construction (it stages today's partition first).",
   "notes": "DISARM (this seat): (a) the fix-forward pin 5991626d4f deployed under re-signed halves and its first REAL manual invoke returning >= 15 of 16 with cottonwood + global present (the sidecar branch decides 15 vs 16), which shows both readers pass on production vintage; (b) the qa_local limitation stated in the fix-forward packet so no later seat reads a qa_local cottonwood crash as a production prediction. NOT chased here: whether qa_local's dry_run branch should stage today's partition to a local path (a CTO/COO design call -- it would make qa_local vintage-faithful at the cost of a real bdmp build per QA run)."
 }
 ]
```

## Open at this seat, NOT a channel item

`2.0.0_SA_COO` disclosed (msg 70753 item 3) that the stage-3 decomp at
`workflows/atom_decomposition/runs/mdpf-cotremediation/20260825T161149Z/` (38 cells, @7807a52e75,
LOCAL -- rides integration) is **SOLO and UNCERTIFIED** because no Tier-2 cohort and no CVO were
live at authoring, and that **every TO cut from it carries "UNCERTIFIED DECOMP" stated by the
issuer**. That is a disclosure done correctly, not a surprise: COO did not queue behind a dark seat
on a live client-facing outage, which is what the pipeline's degraded-state clause asks for.

**The cert is owed and it is this seat's.** It is tracked as CVO work, not as an item in this round;
if the certification invalidates cells, the re-decomp is COO's and re-certification routes to an
independent signer (base CTO -- CRO is off-limits per Andrew).
