# COT_CANON458 -- surprise channel, round 1 (INVESTIGATION_v1)

**Channel owner:** `3.0.0_SA_CVO`. **Protocol:** `org/ref/SURPRISE_CHANNEL_PROTOCOL.md` (Directive Execution Pipeline stage 5, CLAUDE.md Rule 27).

**Round opened** 2026-08-25 on five items surfaced from `COT_CANON458.TO-R1-DS`, a MEASUREMENT-ONLY round. **All five are OBSERVATION x INERT** -- no BLOCKING item, no ARMED item, no disarm owner required. Full grounding, denominators and controls for every line: `org/tier2_senior/0.4.0_DS_ClientPlatform~I/deliverables/COT_CANON458.TO-R1-DS_SERVED_CENSUS_AND_EXCLUSION_PREDICATE.md` s.8.

```json
[
 {
  "id": "COT_CANON458-S1",
  "surfaced_by": "0.4.0_DS_ClientPlatform~I, from a MEASUREMENT-ONLY round -- none of these interrupted the round and none was chased",
  "surfaced_at": "2026-08-25T11:05Z",
  "one_line": "TWO INDEPENDENTLY-EDITABLE WRITERS PUT THE SAME THREE SERVED KEYS: D_01.partner_analytics.py:2643 and D_04.client_portal_summary.py both put_object platinum/firm/partner_analytics_{annual,monthly,quarterly}.json WITH DIFFERENT CacheControl -- cacheable vs no-store -- and which header the live object carries is decided ONLY BY WRITE ORDERING.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "D_01.partner_analytics.py:2643 and D_04.client_portal_summary.py both put_object the same 3 keys",
    "the two CacheControl values are mutually contradictory: public max-age=300 s-maxage=3600 vs no-store no-cache must-revalidate",
    "D_04 wrote last; the live objects carry ITS header",
    "D_01's own comment: TEMPORARY direct-write, the fast-follow wires the standard gold/artifacts to platinum publish -- THE FAST-FOLLOW HAS NOT LANDED"
   ]
  },
  "disposition": "GRADUATED",
  "notes": "⛔ ONE-PRODUCER-PER-SERVED-KEY (Rule 17b's amendment: the publisher is the estate's ONLY JSON producer, so the property holds BY CONSTRUCTION) IS VIOLATED HERE IN THE LEAST VISIBLE WAY. Nothing is broken today because write ordering happens to favour one writer. THE DEFECT IS THAT CORRECTNESS RESTS ON ORDERING, and ordering is not a control -- it is a fact about today's schedule. || THE CACHE HEADERS ARE THE TELL AND THEY ARE OPPOSITE: one says cache an hour at the edge, the other says never cache. A reader cannot tell from the served object which producer authored it, so THE HEADER IS THE ONLY PROVENANCE EVIDENCE AND IT FLIPS SILENTLY WITH THE SCHEDULE. || A TEMPORARY MARKED IN A COMMENT WITH ITS FAST-FOLLOW UNLANDED IS THE DESCRIPTION-NOT-MECHANISM CLASS: the comment records an intention no artifact enforces."
 },
 {
  "id": "COT_CANON458-S2",
  "surfaced_by": "0.4.0_DS_ClientPlatform~I, from a MEASUREMENT-ONLY round -- none of these interrupted the round and none was chased",
  "surfaced_at": "2026-08-25T11:05Z",
  "one_line": "FIVE WRITE TARGETS DECLARED IN D_04 PRODUCE NOTHING IN THE SERVED SET -- fee_efficiency.json, leaderboard.prior_week.json, advisors/{aid}/positions.json, advisors/{aid}/mix.json, accounts/{acct}/summary.json -- and the platinum/accounts/ prefix DOES NOT EXIST AT ALL.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "DENOMINATOR: 1,125 keys MATERIALISED 2026-08-25T10:06:31Z, prefix named",
    "POSITIVE CONTROL on the same probe shape returns 1 hit, so the zeros are measured rather than an empty read",
    "3 of the 5 re-checked LIVE and return 404",
    "no platinum/accounts/ prefix exists in the served set at all"
   ]
  },
  "disposition": "GRADUATED",
  "notes": "GATED-OFF vs DEAD CODE IS EXPLICITLY UNDETERMINED AND THE SURFACING SEAT REFUSED TO DIAGNOSE IT -- not in their cells, and the two possibilities take OPPOSITE remedies (a gated writer waits for a switch; dead code is debt to delete). NAMING THE FORK RATHER THAN PICKING IT is the correct act, and it is the same discipline that kept an absent cot partition undiagnosed this morning. || THE CONTROLS ARE WHAT MAKE THIS FILEABLE: a materialised listing rather than --query length(), a named prefix, a positive control on the probe shape, and a live 404 re-check on 3 of 5. A five-way absence claim without those is a guess."
 },
 {
  "id": "COT_CANON458-S3",
  "surfaced_by": "0.4.0_DS_ClientPlatform~I, from a MEASUREMENT-ONLY round -- none of these interrupted the round and none was chased",
  "surfaced_at": "2026-08-25T11:05Z",
  "one_line": "⛔ SERVED_KEY IS A CONSTANT WHOSE NAME READS LIKE PROVENANCE AND IS NOT: runners_cot/d01_cot_firm_header_metrics.py:46 and d02_cot_value_overlay.py:33 BOTH declare SERVED_KEY = platinum/firm/header_metrics.json and NEITHER WRITES S3 -- a put_object/upload_file/boto3 scan returns ZERO hits in both files.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "d01_cot_firm_header_metrics.py:46 and d02_cot_value_overlay.py:33 both declare the identical SERVED_KEY constant",
    "a put_object / upload_file / boto3 scan returns 0 hits in BOTH files, so neither is a producer of that key",
    "the constant is therefore not evidence of authorship by either module"
   ]
  },
  "disposition": "GRADUATED",
  "notes": "⛔ THIS IS THE ONE THAT WOULD HAVE BITTEN A CERTIFIER, AND THE SURFACING SEAT SAYS SO IN THE RIGHT WORDS: ANY FUTURE PRODUCER-RESOLUTION KEYED ON SERVED_KEY IN THIS TREE NAMES THE WRONG FILE, AND IT WOULD READ AS A CLEAN ANSWER. A wrong answer that arrives clean is the hazard class this fabric spent the night on -- and here it is PRE-LOADED INTO A CONSTANT, waiting for the first seat who resolves a producer by grepping for it. || IT IS A NAME THAT ASSERTS A RELATIONSHIP THE CODE DOES NOT IMPLEMENT: SERVED_KEY reads as the key this module serves; it means a key this module knows about. Same family as comp-estate emitting a served name it does not warrant, and as an audit row's serial field reading as the actor rather than the subject."
 },
 {
  "id": "COT_CANON458-S4",
  "surfaced_by": "0.4.0_DS_ClientPlatform~I, from a MEASUREMENT-ONLY round -- none of these interrupted the round and none was chased",
  "surfaced_at": "2026-08-25T11:05Z",
  "one_line": "A SAMPLED platinum/clients/{id}/views.json carries generated_at 2026-08-22T11:33:55Z while its OBJECT was written 2026-08-24T11:35:28Z -- the content stamp is roughly two days behind the write.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "one sampled client object: generated_at 2026-08-22T11:33:55Z vs object LastModified 2026-08-24T11:35:28Z",
    "SAMPLED ON ONE CLIENT AND DELIBERATELY NOT GENERALISED to the other 221"
   ]
  },
  "disposition": "GRADUATED",
  "notes": "THE SURFACING SEAT'S OWN CAVEAT IS WHY THIS IS FILEABLE: ONE OBJECT IS NOT A POPULATION. They measured one, said so, and refused to extend it to 221 -- the exact restraint that failed at THIS seat twice tonight, when a sample of three was read as a population and a tally of corrections was read as a distribution of errors. || WHY IT WOULD MATTER IF IT GENERALISES: a content stamp behind its write time means A CONSUMER READING generated_at GETS A DIFFERENT ANSWER THAN ONE READING LastModified, so freshness verdicts differ by which plane the instrument happens to read. That is the two-planes hazard inside a single object. NOT GENERALISED, NOT CHASED."
 },
 {
  "id": "COT_CANON458-S5",
  "surfaced_by": "0.4.0_DS_ClientPlatform~I, from a MEASUREMENT-ONLY round -- none of these interrupted the round and none was chased",
  "surfaced_at": "2026-08-25T11:05Z",
  "one_line": "One client dir (z09305728) carries 4 leaves where all 221 others carry 5 -- composition.json absent -- and this single directory IS THE ENTIRE 221-vs-222 ASYMMETRY in the census.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "z09305728 has 4 leaves; all 221 other client dirs have 5",
    "the missing leaf is composition.json",
    "this one directory FULLY ACCOUNTS for the 221-vs-222 discrepancy -- the residual is explained, not merely noted"
   ]
  },
  "disposition": "GRADUATED",
  "notes": "THE VALUE IS THAT A DISCREPANCY WAS RUN TO GROUND RATHER THAN CARRIED AS A ROUNDING NOTE. 221 vs 222 in a census reads as noise; ONE NAMED DIRECTORY MISSING ONE NAMED LEAF is a fact someone can act on or dismiss deliberately. || AN UNEXPLAINED RESIDUAL IS AN OPEN QUESTION WEARING THE COSTUME OF A ROUNDING ERROR -- and it survives indefinitely precisely because it is small enough to ignore and large enough to be real."
 }
]
```
