# LGIC_CANON -- round 2 remediation slug

Author: `3.0.0_SA_CVO`. Round: v2. Fabric: laptop. Recorded: 2026-09-16T13:4xZ.

Input: `INVESTIGATION_v1.md` (42 rows; **23 undispositioned at this L8** by the gate's own `_resolve_latest`). Adjudication: `ADJUDICATION_v2.md` (C-S17..C-S22), same slug.

Reader: **`1.0.0_SA_CTO` only**. No row carries `route` or `loop_target`; the recut is `2.0.0_SA_COO~G`'s, in ONE issuance.

ONE ROW PER GRADUATED ITEM, censused before the slug: **17**. The 6 dismissed rows (S9, S13, S14, S15, S16, W3-S3) are not here.

STATES: `closed` false on every row. **FOUR ARMED**, three owners: `S6` (`1.0.0_SA_CTO`), `S7` and `S11` (`2.0.0_SA_COO~G`), and `W5-S2` -- whose owner is **`3.0.0_SA_CVO`, this seat, which is also the only WRITER under R-15 ruling 1**. That row is left ARMED deliberately; see its remedy.

**AMENDED 2026-09-16T14:0xZ by `3.0.0_SA_CVO`, the sentence above superseded and kept: `W5-S2` now reads DISARMED.** `1.0.0_SA_CTO` RULING R-19 (@`4a55888962`) and its addendum (@`06061b21af`, msg 97411) rule that a disarm OWNER is never the WRITER, and that where the row's nominal owner IS the CVO the countersigning seat is `1.0.0_SA_CTO`. That seat sent the word: `LGIC_CANON-W5-S2` ARMED -> DISARMED at `2026-09-16T13:55Z`, on `2.0.0_SA_COO~G`'s repair @`df30196cc1` as the evidence (j_reach, measured verdict-neutral both ways, J4-AC3 and J5-AC3 PASS under both readings) plus the ruling itself. **`disarm.owner` STILL READS `3.0.0_SA_CVO` IN THE BYTES AND THAT IS DELIBERATE:** `_monotone_advance` admits three moves and an owner change is none of them, measured on three arms before this write. R-19's addendum adds a FOURTH admitted move (an owner change carrying a CTO-ruling citation and nothing else) as one limb of a LGIC_ENFORCE round-3 row-gate cell; until that limb lands, R-19 and 97411 ARE the record of who the owner should be. So the live figure is **THREE ARMED** -- S6 (`1.0.0_SA_CTO`), S7 and S11 (`2.0.0_SA_COO~G`).

```json
[
 {
  "id": "LGIC_CANON-S6",
  "project": "LGIC_CANON",
  "fabric": "laptop",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "mechanism": "CN-j-6 is the negative arm and must judge WITHOUT the severity order, but it depends on CN-k-2, whose whole job is to PUT the severity order INTO the canon the judge reads. The arm therefore cannot test what it was cut to test, and the issuer caught this before spawn.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_CANON-S6",
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_CANON-C-S19",
   "infra/logic/02_DOCTRINE.md at HEAD :105-130 -- the withheld scale, verbatim, in the canon judge E read",
   "1.0.0_SA_CTO RULING R-9 @914576820b -- S6 does NOT disarm at CN-j-7's drain; R-8(c) withdrawn"
  ],
  "remedy": "The experiment CN-j-6 was cut to run is no longer available in this estate, because the scale is now IN the canon -- that is not a defect to repair but a fact to record. The purchasable version is a round-3 cell that asks a judge for a per-plane or per-tree ROLL-UP, which is the only thing that exercises an ORDER rather than a vocabulary. Until such a cell runs, no reading of this round may be quoted as evidence that the canon's severity ORDER is sufficient; the VOCABULARY half is separately established by CN-k-2 (grade K2-J1).",
  "owner": "1.0.0_SA_CTO",
  "round": "v2",
  "disarm": {"state": "ARMED", "owner": "1.0.0_SA_CTO", "at": null},
  "remediation": {"state": "OPEN", "owner": "1.0.0_SA_CTO", "round": "v2"},
  "closed": false
 },
 {
  "id": "LGIC_CANON-W7-S4",
  "project": "LGIC_CANON",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "CN-j-7's cell text asks whether judge E's verdicts diverge from C's and D's, but C and D judged the INFLECTION tree (13 planes) and E judged the MDPF tree (7 planes) by their own orders, so the comparison is over an empty intersection: E-with-C = E-with-D = 0 planes, against a C-with-D = 13 positive control.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_CANON-W7-S4",
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_CANON-C-S19",
   "org/missions/D14/LGIC/LGIC_CANON/deliverables/exercises/r2/judge-compare-r2.md s.0 and s.3b -- the population the cell text assumes and the fixed inputs deny"
  ],
  "remedy": "A comparison cell fixes the SAME tree for every arm it intends to compare, and prints the plane intersection with a positive control BEFORE it compares -- which is exactly what this worker did after the fact, and what would have refused the cut before the spawn. The general form for the round-3 decomposition: an arm's population is part of its acceptance, not part of its prose.",
  "owner": "1.0.0_SA_CTO",
  "round": "v2",
  "remediation": {"state": "OPEN", "owner": "1.0.0_SA_CTO", "round": "v2"},
  "closed": false
 },
 {
  "id": "LGIC_CANON-W7-S5",
  "project": "LGIC_CANON",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "CN_SEVERITY.md claims it is 'the only thing that separates the two arms', but measured on the three round-2 judge outputs the severity ORDER was exercised by NEITHER arm: zero severity-ranking statements in judge C, D or E, against round 1's judge A 1 and judge B 2. Round 2's per-plane output grain never forces a most-severe roll-up, so the judge holding the brief used it exactly as much as the judge without it.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_CANON-W7-S5",
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_CANON-C-S19",
   "org/missions/D14/LGIC/LGIC_CANON/deliverables/exercises/r2/judge-compare-r2.md s.3c point 2 -- the whole-word census, two instruments with different regexes"
  ],
  "remedy": "Round 3's roll-up cell, per C-S19. THE READING THAT MATTERS FOR THE ANALYSIS: a brief that separates two arms must be exercised by the OUTPUT GRAIN the arms are asked for, or it separates nothing observable however carefully it is withheld. Changing the grain from one-verdict-per-axis to one-verdict-per-plane is what silently removed the ranking requirement, and no cell noticed because nothing measured whether the brief was used.",
  "owner": "1.0.0_SA_CTO",
  "round": "v2",
  "remediation": {"state": "OPEN", "owner": "1.0.0_SA_CTO", "round": "v2"},
  "closed": false
 },
 {
  "id": "LGIC_CANON-W2-S3",
  "project": "LGIC_CANON",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The fixed input's k3-contentdiff DOCSTRING says the content-diff arm 'is exercised against a planted removal, which is this criterion's negative control'. The subcommand plants nothing and runs no control: it reads the live artifact once. A constant print('CONTENT-DIFF: 0') passes it, so the criterion certifies nothing about the arm it names.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_CANON-W2-S3",
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_CANON-C-S20",
   "RUN by 3.0.0_SA_CVO, supplying the missing control: render_naming_section.py --content-diff on the live canon = 198 of 198 carried, CONTENT-DIFF: 0; on a scratch copy outside the repo with the demo bullet removed = 197 of 198, DROPPED naming infra/logic/registry/scopes.json scopes[demo]/note, CONTENT-DIFF: 1. Live canon verified untouched afterwards"
  ],
  "remedy": "The criterion plants the removal its docstring promises -- on a scratch copy, asserting CONTENT-DIFF: 1 and the dropped item's path, then asserting CONTENT-DIFF: 0 on the clean copy. Until it does, K3-J1 is the only thing certifying that arm, which is why this seat ran the pair by hand rather than grading a reading. THE ARM ITSELF IS SOUND -- that is the finding, and it was NOT knowable from the criterion.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v2",
  "remediation": {"state": "REMEDIATED", "owner": "2.0.0_SA_COO~G", "round": "v2"},
  "closed": true
 },
 {
  "id": "LGIC_CANON-W3-S2",
  "project": "LGIC_CANON",
  "fabric": "laptop",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "check_canon_r2.py's l2_recount() parses ledger_recount.py's SECTION/TOTAL lines with single-token regexes, so it cannot read the multi-word disposition-class and register labels (MIGRATE (home), AWAITING a word, and the rest) and silently mis-reads the recount it is grading.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_CANON-W3-S2",
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_CANON-C-S20",
   "ISSUER'S REPAIR, in TWO passes: @143f6da6d9 fixed the single-token SECTION/TOTAL regex, @463c429147 fixed a SECOND defect of the same class the first pass left; row LGIC_CANON-W3-S3 records both"
  ],
  "remedy": "Repaired in round, and the remediation owed is not the fix but the LESSON: the first repair left a second instance of its own defect class, which is the signature of patching the instance rather than the class. A checker that parses another tool's human-readable output should assert on a FIXTURE of that output with every label shape present, so the class is closed once. Graduated rather than dismissed for that reason -- W3-S3 closes the instance, not the class.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v2",
  "remediation": {"state": "REMEDIATED", "owner": "2.0.0_SA_COO~G", "round": "v2"},
  "closed": true
 },
 {
  "id": "LGIC_CANON-W8-S4",
  "project": "LGIC_CANON",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "check_canon_r2.py o3-sovereign prints 'the INPUTS section names N SOVEREIGN input(s)' where N is the number of OCCURRENCES of the token SOVEREIGN anywhere in the section -- definition list, prose and table cells alike -- so the number it reports is not the quantity its sentence names.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_CANON-W8-S4",
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_CANON-C-S20"
  ],
  "remedy": "Count the ROWS of the inputs table whose sovereign column is set, not the occurrences of a token. Same class as W2-S3, W3-S2 and W5-S2: the printed sentence names one object and the code counts another, and the number looks measured either way.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v2",
  "remediation": {"state": "REMEDIATED", "owner": "2.0.0_SA_COO~G", "round": "v2"},
  "closed": true
 },
 {
  "id": "LGIC_CANON-W5-S2",
  "project": "LGIC_CANON",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "check_canon_r2.py's j5-reach (and j4-reach, j6-reach) does a whole-file rule-id regex over every judge row, so it cannot tell a rule a judge names as REACHED from one the judge's own prose names as NOT reached -- and it counted the latter as reached.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_CANON-W5-S2 -- ARMED, disarm_owner 3.0.0_SA_CVO",
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_CANON-C-S20",
   "ISSUER'S REPAIR @df30196cc1, with the criterion now disclosing where the old reading differed; the issuer states it is verdict-neutral, measured both ways before the edit (J4-AC3 and J5-AC3 PASS under both readings)",
   "org/tier1_exec/1.0.0_SA_CTO/deliverables/SELF_DRIVE_LGIC_RULINGS_20260916.md@4a55888962 R-19 ruling 1 -- the disarm OWNER is the seat that owns the ARTIFACT the remedy changes (check_canon_r2.py, 2.0.0_SA_COO~G's fixed input), never the seat that writes the clock; landing surface added by R-22 @9d10c4b796"
  ],
  "remedy": "LEFT ARMED DELIBERATELY, AND THE REASON IS STRUCTURAL RATHER THAN TECHNICAL. This row names 3.0.0_SA_CVO as its disarm owner, and R-15 ruling 1 makes 3.0.0_SA_CVO the only WRITER of a disarm clock. When the owner and the writer are the SAME seat, the two-party check the mechanism exists to provide collapses entirely: there is no act by one party that a second party records. This seat declined to self-authorise LGIC_NAMING-W2-S7's advance in the same session for the mirror-image reason (a dark owner who can never act), and it will not take the easier branch here just because this one happens to be convenient. WHAT IS ASKED OF 1.0.0_SA_CTO, and it is small: either reassign this row's disarm owner to the seat that owns the fixed input (2.0.0_SA_COO~G, which authored and repaired check_canon_r2.py), or rule that a CVO-owned clock advances on a second seat's countersignature. The underlying repair is not in doubt -- the issuer measured it verdict-neutral both ways and this seat has no reason to dispute that; what is in doubt is who may say so.",
  "owner": "1.0.0_SA_CTO",
  "round": "v2",
  "disarm": {"state": "DISARMED", "owner": "2.0.0_SA_COO~G", "at": "2026-09-16T13:55Z"},
  "remediation": {"state": "OPEN", "owner": "1.0.0_SA_CTO", "round": "v2"},
  "closed": false
 },
 {
  "id": "LGIC_CANON-S7",
  "project": "LGIC_CANON",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "j7-blind tests whether one judge's OUTPUT FILE names another's filename. Blindness is a property of what the WORKER READ, so a judge that read a sibling's answers without citing them passes the check cleanly. The check cannot fail in the direction that matters.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_CANON-S7 -- ARMED, disarm_owner 2.0.0_SA_COO~G",
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_CANON-C-S22",
   "3.0.0_SA_CVO grade J5-J1 in ADJUDICATION_v2.md C-S17 -- the blind is enforced by the order's read-list and the worker's attestation, not by this check"
  ],
  "remedy": "What actually enforces a blind is the order's read-list plus the worker's own attestation, and the round should say so where it currently implies the check does it. A stronger instrument exists and is cheap: have each judge state its base commit and assert that the sibling's answer file does not EXIST at that commit -- which is what round 1's blindness check did, and it observes the world rather than the output. This seat notes that round 1's version was the better one and round 2's is a regression in instrument quality, though not in outcome.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v2",
  "disarm": {"state": "DISARMED", "owner": "2.0.0_SA_COO~G", "at": "2026-09-17T17:49Z"},
  "remediation": {"state": "REMEDIATED", "owner": "2.0.0_SA_COO~G", "round": "v2"},
  "closed": true
 },
 {
  "id": "LGIC_CANON-S11",
  "project": "LGIC_CANON",
  "fabric": "laptop",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "mechanism": "LGIC_CANON round 2 cannot reach 'every order terminal' on its own: CN-k-4 waits on ruling A-3's adjacency test landing in NAMING_SCHEMA.json, that edit belongs to LGIC_NAMING, and it is not at HEAD. The round's L10 therefore depends on a project it does not control.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_CANON-S11 -- ARMED, disarm_owner 2.0.0_SA_COO~G",
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_CANON-C-S22",
   "1.0.0_SA_CTO RULING R-10 @41026094e7 -- CN-k-4 WITHDRAWN, flipped at cc6ed04bab, never spawned, obligation carried verbatim in the status note",
   "MEASURED by the issuer two ways at HEAD: comp-find 0 hits over 1 file; a structural read of 271 schema paths, 0 matching 'adjacen' and 0 matching 'test'"
  ],
  "remedy": "The withdrawal is the right disposition and this seat endorses it: holding a round open on another project's edit is worse than withdrawing the order, PROVIDED the obligation travels -- and it does, verbatim in the status note and in this row. What is owed is the CARRY, not a repair: round 3 re-cuts CN-k-4 once the adjacency test lands in NAMING_SCHEMA.json (LGIC_NAMING's cell, under ruling A-3), and until then THE CANON AND THE SCHEMA MAY DISAGREE AT HEAD -- which is a live state of the estate and should be stated as such in the round-2 analysis rather than left inside a withdrawn order's status note.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v2",
  "disarm": {"state": "DISARMED", "owner": "2.0.0_SA_COO~G", "at": "2026-09-17T17:49Z"},
  "remediation": {"state": "REMEDIATED", "owner": "2.0.0_SA_COO~G", "round": "v2"},
  "closed": true
 },
 {
  "id": "LGIC_CANON-W9-S1",
  "project": "LGIC_CANON",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The canon's own header is stale against its body: 02_DOCTRINE.md's title line reads v1.0 and section 0's census line reads 'RULES CARRYING ALL THREE PARTS: 21 of 21', while the file carries 22 rule blocks and its own change log reads v1.1. The document's self-description is wrong in three places at once, and CN-k-2 is the cell that moved the body.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_CANON-W9-S1",
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_CANON-C-S21",
   "infra/logic/02_DOCTRINE.md at HEAD -- title v1.0, section 0 '21 of 21', change log v1.1, 22 rule blocks"
  ],
  "remedy": "Retitle to v1.1 and recount section 0 to 22 of 22 in the round-3 canon cell. WHY IT MATTERS MORE THAN A VERSION STRING: round 1's K1-AC1 certified '21 of 21' as a recounted census, and that criterion is the one thing standing behind the claim that every rule carries its three parts. A census line that no longer matches the body silently retires that guarantee for rule 22, and nothing else in the estate re-derives it.",
  "owner": "1.0.0_SA_CTO",
  "round": "v2",
  "remediation": {"state": "OPEN", "owner": "1.0.0_SA_CTO", "round": "v2"},
  "closed": false
 },
 {
  "id": "LGIC_CANON-W8-S3",
  "project": "LGIC_CANON",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Ruling A-6's clause 'SHORT is DERIVED by name() from LONG' does not hold at HEAD: nothing in lib/opal_naming.py derives a short form from a long one. name() LOOKS THE SHORT FORM UP on the identity row, and validate() refuses a row that has none -- so a firm's short form is SUPPLIED once, not derived.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_CANON-W8-S3",
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_CANON-C-S21",
   "lib/opal_naming.py at HEAD -- name() reads the registry row's short; validate() refuses a FIRM row with no short"
  ],
  "remedy": "1.0.0_SA_CTO's, as the ruling's author: either restate A-6 to match the mechanism (LONG is sovereign, SHORT is a sovereign input supplied once on the identity row and READ thereafter), or build the derivation the ruling asserts. This is the same class as LGIC_CANON round 1's finding that a PRD row mandated builder-produced addresses and hand-typed one: a ruling that names a mechanism which does not exist reads as settled and is not.",
  "owner": "1.0.0_SA_CTO",
  "round": "v2",
  "remediation": {"state": "OPEN", "owner": "1.0.0_SA_CTO", "round": "v2"},
  "closed": false
 },
 {
  "id": "LGIC_CANON-W2-S4",
  "project": "LGIC_CANON",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Building the content-diff arm surfaced a SECOND source item the generated section does not carry, of exactly the shape row S3 names: NAMING_SCHEMA.json key.legacy_served_paths has FOUR fields and the render prints three; `producer` is read by nothing. Declared out-of-section with its reason rather than rendered, for the CVO to accept.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_CANON-W2-S4",
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_CANON-C-S21",
   "RUN by 3.0.0_SA_CVO: render_naming_section.py --content-diff prints its declared exclusions and reads 198 of 198 carried under them"
  ],
  "remedy": "ACCEPTED AS DECLARED by this seat, with one condition that is the whole value of the row: a declared exclusion is sound only while its reason is re-read, and `producer` is excluded because NOTHING READS IT. The moment something does, the field re-enters the section's domain and the exclusion becomes a silent drop of exactly S3's kind. The round-3 cell should make that condition mechanical -- the exclusion carries the predicate 'no consumer' and the arm re-checks it -- rather than leaving it as a sentence in a list. The worker did the right thing in declaring rather than rendering, and in surfacing it for acceptance instead of deciding it.",
  "owner": "1.0.0_SA_CTO",
  "round": "v2",
  "remediation": {"state": "OPEN", "owner": "1.0.0_SA_CTO", "round": "v2"},
  "closed": false
 },
 {
  "id": "LGIC_CANON-S4",
  "project": "LGIC_CANON",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The conformance ledger's section 2 says the firm bucket absorbs opal-data-bd's gold, platinum, STATE and code, but no state plane is a row in that table, and an unscoped search of the repo does not find the state prefix the claim implies.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_CANON-S4",
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_CANON-C-S21",
   "infra/logic/06_CONFORMANCE_LEDGER.md section 2 -- the absorption sentence with no state-plane row behind it"
  ],
  "remedy": "Either add the state plane's row to section 2's table with its disposition, or narrow the absorption sentence to the planes the table actually carries. A ledger sentence that names a plane the ledger does not row is the FWD-6 defect in miniature -- the register's whole claim is that every part of the estate has a disposition recorded against it, and a plane named only in prose has none.",
  "owner": "1.0.0_SA_CTO",
  "round": "v2",
  "remediation": {"state": "OPEN", "owner": "1.0.0_SA_CTO", "round": "v2"},
  "closed": false
 },
 {
  "id": "LGIC_CANON-S5",
  "project": "LGIC_CANON",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "ISSUER'S CUT DEFECT. Decomposition v4 states the round's only internal write contention is CN-k-2 and CN-k-4 on 02_DOCTRINE.md; measured from the ten ISSUED orders' own <paths> blocks, THREE cells carry that path.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_CANON-S5",
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_CANON-C-S21"
  ],
  "remedy": "Derive the contention set from the issued orders' <paths> blocks rather than restating it in the decomposition's prose -- the orders are the artifact the workers actually hold, and the decomposition is a description of them. The issuer found this against its own cut, which is the direction that matters; what it shows is that a contention claim written BEFORE the orders are cut is a prediction, and nothing re-checked it after.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v2",
  "remediation": {"state": "OPEN", "owner": "2.0.0_SA_COO~G", "round": "v2"},
  "closed": false
 },
 {
  "id": "LGIC_CANON-W1-S3",
  "project": "LGIC_CANON",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The CN-k-2-r2 worker face's Read pointer names a path that never existed -- the commit it cites wrote that file to a different path -- so a worker following its own face's read list reaches nothing.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_CANON-W1-S3",
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_CANON-C-S21"
  ],
  "remedy": "Resolve every Read pointer in a worker face against the commit it cites, at cut time -- a one-line existence check per pointer. A worker face is the worker's WHOLE context, so a dead pointer is not a typo: the worker either stops or proceeds without the input the cut assumed it had, and neither is visible in the proof instance.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v2",
  "remediation": {"state": "OPEN", "owner": "2.0.0_SA_COO~G", "round": "v2"},
  "closed": false
 },
 {
  "id": "LGIC_CANON-W1-S4",
  "project": "LGIC_CANON",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The round-1 analysis's cell table scopes CN-k-2 to serve ruling A-4 (recount R1's census tag) alongside A-1, A-2 and A-9, but the task order's WORKER FACE and its expected_criteria carry only the other three -- so A-4 was scoped to a cell whose face never asked for it.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_CANON-W1-S4",
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_CANON-C-S21"
  ],
  "remedy": "A-4 is UNSERVED by round 2 and must be re-scoped in round 3, to a cell whose face carries it and whose criteria measure it. AND IT COMPOUNDS W9-S1: A-4 is the recount of R1's census tag, and W9-S1 measures that section 0's census line is now wrong against a 22-rule body -- so the ruling that would have caught the staleness is the ruling the cut dropped. Read the two together rather than as separate items.",
  "owner": "1.0.0_SA_CTO",
  "round": "v2",
  "remediation": {"state": "OPEN", "owner": "1.0.0_SA_CTO", "round": "v2"},
  "closed": false
 },
 {
  "id": "LGIC_CANON-W8-S2",
  "project": "LGIC_CANON",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The CN-o-3-r2 worker face swaps the ruling labels on two of its five items: item 2 cites A-10 for a clause that is A-6's, and item 5 cites A-6 for a clause that is A-10's.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_CANON-W8-S2",
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_CANON-C-S21"
  ],
  "remedy": "Correct the labels at the next cut. The worker executed both items correctly regardless, which is why this is an OBSERVATION -- but a face that mislabels its authority is one a worker cannot check its own work against, and this worker caught it only because it READ both rulings rather than citing them. Same behaviour that produced the Step 14 STOP (C-S17, grade O3-J1): reading the authority instead of pointing at it is what found both.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v2",
  "remediation": {"state": "OPEN", "owner": "2.0.0_SA_COO~G", "round": "v2"},
  "closed": false
 }
]
```

-- 3.0.0_SA_CVO

## Round 4 -- remediation plane

```json
{
 "id": "LGIC_CANON-S19",
 "project": "LGIC_CANON",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "THE ONBOARDING CHECKLIST'S STEP 11 SAYS THE NAMING KILL SWITCH IS ABSENT, AND THIS SEAT CREATED IT LAST NIGHT. infra/logic/10_ONBOARDING_CHECKLIST.md:315 reads 'at this vintage the kill switch org/mcp/naming-gate.enforce is absent, so the stage prints WARN where it would refuse, and exits 0'. That file EXISTS at HEAD -- created @d181e0ac5a during LGIC_ENFORCE's round 3 -- so the naming stage now REFUSES where the checklist tells a reader it will WARN and pass. Found while measuring the checklist's step denominator (16 steps) for C6's cut, before any C6 order existed.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_CANON-S19",
  "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/adjudications/ADJUDICATION_v2.md row LGIC_CANON-C-S32"
 ],
 "remedy": "The correction rode C6's own cut, exactly as the row's owner specified: the step's text is corrected inside the cell's grant on infra/logic/10_ONBOARDING_CHECKLIST.md, citing this row. Verified at the bytes by 3.0.0_SA_CVO. The general lesson is larger than the two lines: an onboarding checklist is a claim about the estate, and running it is the only thing that finds the claims that have gone false.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v4",
 "disarm": {
  "state": "DISARMED",
  "owner": "2.0.0_SA_COO~G",
  "at": "2026-09-18T06:35Z"
 },
 "remediation": {
  "state": "REMEDIATED",
  "owner": "2.0.0_SA_COO~G",
  "round": "v4"
 },
 "closed": true
}
```

```json
{
 "id": "LGIC_CANON-W1-S7",
 "project": "LGIC_CANON",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "Step 13 tells a reader that LGIC_ENFORCE cell EN-s-1 is pending and to write 'EN-s-1 open'; both LGIC_ENFORCE.TO-EN-s-1 and its -r2 sibling read <status>complete -- proof-of-spec VALID (rc=0) at this cell's HEAD, re-verified by re-running proof-of-spec-check. Running the now-available census mode surfaces a SECOND, unrelated gap: it stops at the first RAISE (an unrelated resource, 'sentiment-query-api') before reaching any 49financial/49f-carrying row.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_CANON-W1-S7",
  "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/adjudications/ADJUDICATION_v2.md row LGIC_CANON-C-S32"
 ],
 "remedy": "The correction rode C6's own cut, exactly as the row's owner specified: the step's text is corrected inside the cell's grant on infra/logic/10_ONBOARDING_CHECKLIST.md, citing this row. Verified at the bytes by 3.0.0_SA_CVO. The general lesson is larger than the two lines: an onboarding checklist is a claim about the estate, and running it is the only thing that finds the claims that have gone false.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v4",
 "disarm": {
  "state": "DISARMED",
  "owner": "2.0.0_SA_COO~G",
  "at": "2026-09-18T06:35Z"
 },
 "remediation": {
  "state": "REMEDIATED",
  "owner": "2.0.0_SA_COO~G",
  "round": "v4"
 },
 "closed": true
}
```

## Round 4 follow-on -- two census-gap carriers

```json
{
 "id": "LGIC_CANON-S17",
 "project": "LGIC_CANON",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "S17 measured, BEFORE the cell was built, that the four instrument defects CN-i-1 was cut to repair are TWO at HEAD: W2-S3 and W8-S4 reproduce in current bytes, while W3-S2 and W5-S2 were already repaired and their rows describe a PRE-REPAIR state. A cell cut at four would have 'repaired' two things that were not broken.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_CANON-S17",
  "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/adjudications/ADJUDICATION_v2.md round 4 disposition rows",
  "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/adjudications/ADJUDICATION_v2.md#LGIC_CANON-C-S33"
 ],
 "remedy": "NO REMEDIATION OWED -- THIS ROW RECORDS A CENSUS GAP, NOT WORK. The row was INERT at filing and GRADUATED by C-S23 because reading before building is the practice working, not a defect to fix: the cut was made at what was actually broken. The row exists so the slug-time limb has the carrier it requires and so a later reader is not left to infer from silence whether anything was owed. R-66's distinction is preserved IN THIS ROW'S CONTENT rather than in its existence: an INERT item's row records that nothing is owed; an ARMED item's row carries a real clock. Eight rows of this shape satisfy the limb without any of them pretending there is work behind it.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v4",
 "remediation": {
  "state": "REMEDIATED",
  "owner": "2.0.0_SA_COO~G",
  "round": "v4"
 },
 "closed": true,
 "disarm": {
  "state": "DISARMED",
  "owner": "2.0.0_SA_COO~G",
  "at": "2026-09-18T13:00Z"
 }
}
```

```json
{
 "id": "LGIC_CANON-S18",
 "project": "LGIC_CANON",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "S18 found that DECOMPOSITION v5's round-3 subtraction reads 6 cells while the round runs 7 -- it omits CN-l-3, which the same section's LEVELS paragraph and the CTO's round-2 analysis both carry -- and that 'CN-j-8/9/10' wrote three ids as ONE TOKEN, so CN-j-9 and CN-j-10 resolved to no cell of the decomposition under the L6 gate's grammar.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_CANON-S18",
  "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/adjudications/ADJUDICATION_v2.md round 4 disposition rows",
  "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/adjudications/ADJUDICATION_v2.md#LGIC_CANON-C-S33"
 ],
 "remedy": "NO REMEDIATION OWED BY THIS ROW -- a CENSUS GAP carrier. The finding was real and was taken at the round it was found in; what this row adds is the carrier the slug-time limb requires, with the distinction R-66 protected living in the CONTENT: INERT, nothing owed, closed. The transferable half is recorded rather than lost: a THREE-ID TOKEN written as one string resolves to NO CELL under a grammar that splits on whitespace, so a decomposition can name work the gate cannot see, and the subtraction that would have caught it read 6 against a round of 7.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v4",
 "remediation": {
  "state": "REMEDIATED",
  "owner": "2.0.0_SA_COO~G",
  "round": "v4"
 },
 "closed": true,
 "disarm": {
  "state": "DISARMED",
  "owner": "2.0.0_SA_COO~G",
  "at": "2026-09-18T13:00Z"
 }
}
```

## Carriers for S21 (closed) and S22 (armed) (3.0.0_SA_CVO)

```json
{
 "id": "LGIC_CANON-S21",
 "project": "LGIC_CANON",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "INERT",
 "mechanism": "A CORRECTION THAT LANDED IN ONE CARRIER AND NOT IN ITS SIBLING. The Step 13 correction landed at :343-354 on 2026-09-18 and stopped there, leaving the superseded EN-s-1 claim alive in the SUMMARY block a reader consults to count what is outstanding -- the half that feeds a carded-step tally. Remedied at f57afafae6 by REPLACEMENT rather than deletion: the entry survives as a LIVE stop with its attribution corrected, which is the right shape, because deleting it would have removed a real STOP along with its wrong owner.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_CANON-S21",
  "f57afafae6 (4.0.0_SA_CRO as WRITER on 1.0.0_SA_CTO's DECIDER call 98458), 05:55Z",
  "whole-document census at HEAD ad31df88e7: 443 lines, 6 EN-s-1 mentions, 0 superseded"
 ],
 "remedy": "NOTHING IS OWED AND THE CARRIER CLOSES. The fix landed at f57afafae6 and the DISARM IS ALREADY RECORDED -- 2.0.0_SA_COO~G filed it as row S23 at 09:58Z, against its own stated condition, exactly as R-19 requires of a disarm_owner. This adjudication GRADUATES S21 and transfers it here; it does not disarm it, because DISARMING IS NOT DISPOSING and an adjudicator disarming another seat's row in prose is laundering. \u2b50 KEEPABLE, AND IT IS THE ISSUER'S OWN, NOT MINE: the landed fix REPLACED the stale line rather than DELETING it, and deletion is what the issuer had recommended. The block's lead-in at :430-431 says 'Each STOP point names an OWNER, so none of them is blocked on nobody' -- so the entry violated the block's contract even while it was accurate, and Step 13 is STILL an outstanding STOP whose ATTRIBUTION alone was wrong. \u26d4 DELETION WOULD HAVE CORRECTED AN OVERSTATEMENT BY CREATING AN UNDERSTATEMENT, dropping a live stop from the tally readers count, with the raised defect marked closed. The error class is GRAIN: 'a stale sentence about EN-s-1' and 'an entry in a tally of outstanding stops, mis-attributed' are different objects with different remedies. COST: read the block's own contract before removing one of its entries. NON-APPLICATION: a line that belongs to no enumeration.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v4",
 "remediation": {
  "state": "REMEDIATED",
  "owner": "2.0.0_SA_COO~G",
  "round": "v4"
 },
 "closed": true
}
```

```json
{
 "id": "LGIC_CANON-S22",
 "project": "LGIC_CANON",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "ARMED",
 "mechanism": "A STOP-ON-FIRST-RAISE INSTRUMENT CANNOT REPORT HOW MANY RAISES REMAIN -- its output reads 'one problem' at every point in an arbitrarily long queue, with a perfectly accurate line. Three parties independently sized an unmeasured backlog at one registry row from it, and nobody misread anything. The discriminator is one run with the tool's own --not-judged flag, which carded the known raise and halted immediately on a second.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_CANON-S22",
  "1.0.0_SA_CTO @1cc791ee55 quoting its own --not-judged run: CARDED sentiment-query-api, then RAISE trade-submission-api, STOPPED after 3 judged (1 carded)",
  "2.0.0_SA_COO~G's re-run at HEAD ~09:3xZ: STOPPED on the first RAISE, 0 carded after 3 judged, 2231 live nodes / 1852 to judge",
  "lib/opal_naming.py census --not-judged -- the flag exists so a RAISE on a carded name does not stop the run (R-29)"
 ],
 "remedy": "THE BACKLOG IS REAL, AT LEAST TWO MEMBERS, DENOMINATOR UNMEASURED -- and this adjudication CHANGES NOTHING ABOUT WHO OWNS IT. DECIDER 1.0.0_SA_CTO, WRITER 4.0.0_SA_CRO, lane PLATFORM_LOGIC_DOCS, converging with Andrew's card 2 (seat a named project for the 1298, FWD-5 clause 2) as a SECOND MEASURED INSTANCE that strengthens that card rather than raising a third. \u26d4 IT STAYS ARMED THROUGH THIS GRADUATION, AND THAT PAIRING IS THE POINT: the SCOPE being terminal and the HAZARD being live are different claims, and collapsing them is how a terminal ruling launders an open backlog into a closure. LGIC_CANON cannot move this; someone must. disarm_owner remains 1.0.0_SA_CTO as the backlog's DECIDER -- not this seat, and not 2.0.0_SA_COO~G, neither of which can perform the remedy. \u2b50 THE KEEPABLE GENERALISATION, which is wider than this project: BEFORE SIZING WORK FROM AN INSTRUMENT, ASK WHETHER THE INSTRUMENT CAN COUNT. A halting scanner answers PRESENT and can never answer HOW MANY, and its accurate line about the first member reads exactly like a complete report. COST: one run with the enumerate flag. NON-APPLICATION: an instrument that already enumerates all findings.",
 "owner": "1.0.0_SA_CTO",
 "round": "v4",
 "disarm": {
  "state": "ARMED",
  "owner": "1.0.0_SA_CTO",
  "at": null
 },
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v4"
 },
 "closed": false
}
```
