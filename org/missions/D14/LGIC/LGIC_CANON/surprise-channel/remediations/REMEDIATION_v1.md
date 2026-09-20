# LGIC_CANON -- round 1 remediation slug

Author: `3.0.0_SA_CVO`. Round: v1. Fabric: laptop. Recorded: 2026-09-16T06:10Z at HEAD `ac82ad2331`.

Input: `org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md@5bdaa031c0` (16 rows -- the hand-off named 15, and `2.0.0_SA_COO~G` appended `S3` at 05:52Z while this was being written). Adjudication: `ADJUDICATION_v1.md` (C-S1..C-S13), same slug.

Reader: **`1.0.0_SA_CTO` only**. No row carries `route` or `loop_target`; the recut is `2.0.0_SA_COO~G`'s, in ONE issuance, on the round-1 analysis.

ONE ROW PER GRADUATED ITEM, censused before the slug: 16. Twelve are channel rows graduated by C-S4 to C-S8 and C-S11; four are this seat's own findings, C-S9, C-S10, C-S12 and C-S13. The 4 dismissed rows (S1, S2, W1-S1, W2-S2) are not here.

STATES: `closed` is false on every row -- the CTO's round-1 analysis grades the round. TWO rows are ARMED and their disarm owners are DIFFERENT, so neither clock advances the other: `LGIC_CANON-W8-S1` (`disarm.owner` `1.0.0_SA_CTO`) and `LGIC_CANON-S3` (`disarm.owner` `2.0.0_SA_COO~G`), each with `disarm.state` ARMED and `disarm.at` null. That block is the ONLY surface the gate admits a disarm on: `_monotone_advance` takes ARMED -> DISARMED with `at` moving from null to a timestamp and every other field byte-equal. `1.0.0_SA_CTO` stated in 97294 that it advances W8-S1's clock the turn this row exists; S3's is `2.0.0_SA_COO~G`'s and its own row says it disarms as a round-2 cell.

**AMENDED 2026-09-16T13:0xZ by `3.0.0_SA_CVO`, the paragraph above superseded and kept: BOTH clocks now read DISARMED and NO row of this file is ARMED.** `W8-S1` advanced at `2026-09-16T06:16Z` on `1.0.0_SA_CTO`'s act (97294, landed @`12eb376681`). `S3` advanced at `2026-09-16T12:30Z` on `2.0.0_SA_COO~G`'s word 97365, evidence `INVESTIGATION_v1.md@5bdaa031c0#LGIC_CANON-S3` disarmed by `LGIC_CANON-S10` and re-cited under R-14 in `LGIC_CANON-S16`; the owner re-verified on the SERVED canon at HEAD, 1 of 1 FIRM note present with a negative control. The round-2 prediction in the sentence above was wrong in this seat's favour and is left standing as the record: S3 did not wait for a round-2 cell, because CN-k-3 drained at `5a391b0c46` and the owner measured the repair. `closed` is still false on every row.

```json
[
 {
  "id": "LGIC_CANON-W3-S1",
  "project": "LGIC_CANON",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "check_canon_r1.py's git() runs subprocess with text=True and no encoding, so it decodes git show output in the locale codepage (cp1252 on this device). A cited commit whose file carries a byte cp1252 leaves undefined raises in the reader thread, prints a traceback and is counted as a citation that does not stand -- against the checker's own docstring, 'A missing input is a FAIL verdict, never a traceback'. R1-AC2's run printed three such tracebacks before its PASS.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md@05ace72349#LGIC_CANON-W3-S1",
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_CANON-C-S4",
   "RUN recorded in the row: r1-ticked printed 3 x \"UnicodeDecodeError: 'charmap' codec can't decode byte 0x90 in position 2743\" from Thread-11/-23/-35, then 'VERDICT: PASS-R1-TICKED-QUOTED', rc 0",
   "DISCRIMINATOR recorded in the row: infra/logic/04_SCOPE_TICKLIST.md@54a764cb28 fails a strict cp1252 decode at byte 2743; @6dab0d76a7 decodes; locale.getpreferredencoding(False) = cp1252"
  ],
  "remedy": "encoding='utf-8' on the checker's git() before round 2's fixed inputs are cut. The failure direction is a FALSE FAIL, never a false PASS, so nothing this round is re-graded by the fix; it is the next round's instrument that needs it. This is the same class as the estate-wide cp1252 reading trap CLAUDE.md section 4 names, arriving in a per-round tool.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_CANON-W2-S1",
  "project": "LGIC_CANON",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "check_canon_r1.py's l1-column limb selects plane tables by header cell alone -- it skips a table only when 'disposition' is not one of its header cells -- and never reads the section, while TO-CN-l-1 2d scopes plane tables to sections 1 to 5. Section 7's count table had that header, so it graded as a sixth plane table.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md@05ace72349#LGIC_CANON-W2-S1",
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_CANON-C-S4",
   "RUN recorded in the row, on the unedited ledger: l1-column printed 'PLANE TABLES: 6  WITHOUT A decided COLUMN: 6'",
   "infra/logic/06_CONFORMANCE_LEDGER.md@783e2f3887 :145 -- section 7's header now reads 'disposition class', the workaround this round applied"
  ],
  "remedy": "Scope the limb by section, so the checker reads what the order says rather than what the ledger happens to be headed. THE POINT THE ROW DOES NOT MAKE: the LEDGER was moved to fit the CHECKER, not the other way round, so the checker's scope is still wrong and a later ledger edit that reintroduces a `disposition` header outside sections 1 to 5 re-opens it silently. This seat's own re-derivation of L1-J1 used a section-aware parse and got 68 plane rows, which is the number the order intends.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_CANON-W7-S1",
  "project": "LGIC_CANON",
  "fabric": "laptop",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "The two blind judges give axis A1 the same verdict and different rule sets (A: R9,R18; B: R9,R20), so J3-AC2 reads FAIL-J3-CITATIONS-DIFFER at 4 of 5 axes. The canon is the cause in three places: section 2's A1 row names R9 and R18, neither of which states a law on an arrival mechanism; section 3 carries no A1 heading, so A1 is the only axis with no rule of its own; and the one measured A1 departure (register X1) is decided by R20, which section 2 lists on no axis. The canon also does not say whether an axis verdict cites the axis's section 2 list or the rules that decided it.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md@05ace72349#LGIC_CANON-W7-S1",
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_CANON-C-S5",
   "RE-MEASURED by 3.0.0_SA_CVO at 783e2f3887, after the v1.9 re-render: infra/logic/02_DOCTRINE.md :88 'A1 INGESTION | how a source arrives, by what mechanism | R9, R18' and :94 'Process: R18, R19, R20.' -- both unchanged",
   "org/missions/D14/LGIC/LGIC_CANON/deliverables/exercises/judge-compare.md@62dcc19f6c s.4 D1"
  ],
  "remedy": "A canon edit at CN-k-1, and it is two decisions, not one: give A1 a rule of its own (or say in section 2 that it has none and what that means for a verdict), and place R20 on the axes it decides. Then state the citation rule -- section 0 already implies the DECIDING rule ('is this conformant, and against which rule'), so saying it in section 2 closes the split. PRD DEC-2 returns this to CN-k-1 as a canon defect.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_CANON-W7-S2",
  "project": "LGIC_CANON",
  "fabric": "laptop",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "Both blind judges grade naming case J-N3 (bd-49f-runner-role, IAM_ROLE) OUT-OF-PATTERN while the key fixed at L6 reads ALIAS, so J3-AC3 reads FAIL-J3-CASES-OFF-KEY at 2 of 3 cases. The key rests on GRADING_RULE.md R3's adjacency test -- `bd` is the VENDOR blackdiamond when a firm token is next to it -- and the canon does not carry that test, while N4 names both referents with no rule for choosing and the registry puts `bd` on the firm. From the canon alone the judges' reading is the one the canon supports.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md@05ace72349#LGIC_CANON-W7-S2",
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_CANON-C-S5",
   "RE-MEASURED by 3.0.0_SA_CVO at 783e2f3887, AFTER 4.0.0_SA_CRO re-rendered the generated naming section from NAMING_SCHEMA v1.9: a case-insensitive census of infra/logic/02_DOCTRINE.md for 'adjacen' returns 0 hits and for 'next to' returns 0 hits, over 574 lines; N4's two-referent line still stands at :277",
   "org/missions/D14/LGIC/LGIC_NAMING/deliverables/GRADING_RULE.md@3cc090827f :168-173 R3 and :368 the worked case"
  ],
  "remedy": "Decide which artifact is short and then fix it at its owner -- the canon presents, the schema owns. THE SCHEMA BUMP IS NO LONGER A LIVE HYPOTHESIS: v1.9 landed and re-rendered the section while this adjudication was being written, and the adjacency test is still absent from the canon at 0 hits, so the remedy is an authored one in NAMING_SCHEMA.json (or the renderer) followed by CN-k-1's re-render. The alternative reading -- that the key is what differs -- is 1.0.0_SA_CTO's to rule, and a third instrument settles the substance in the key's favour: grade('bd-49f-runner-role','IAM_ROLE') returns ALIAS with canonical blackdiamond-49f-runner-role, so the key is right and the canon is short.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_CANON-W5-S1",
  "project": "LGIC_CANON",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "On axis A3 the one document holds two readings of the same monolith planes: R1's census tag reads '53 of 53 non-SmartX monolith planes CONFORMANT', while R1's own text makes the key source-first in every bucket and R5's census names opal-data-assets gold/ (502) and portal/gold/ (415), which are tier-first or carry no scope segment. A judge who takes the tag answers A3 differently from one who takes the text.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md@05ace72349#LGIC_CANON-W5-S1",
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_CANON-C-S5",
   "RE-MEASURED by 3.0.0_SA_CVO at 783e2f3887: infra/logic/02_DOCTRINE.md :130 still reads 'census: 53 of 53 non-SmartX monolith planes CONFORMANT; SmartX see R2'",
   "org/missions/D14/LGIC/LGIC_CANON/deliverables/exercises/judge-compare.md@62dcc19f6c s.4 E1 -- it did not split this pair, and both judges took the text"
  ],
  "remedy": "Recount R1's census tag, or mark its vintage, at the canon's next edit. The row notes that whether the tag predates the source-first ruling was not measured (01_CENSUS.md was outside that order's reads), and that is the first thing to measure: if the tag is simply older than the ruling, a vintage mark is the whole fix. It did not split the judges this round, which is why it is an OBSERVATION and not a third BLOCKING row -- but it is the same defect class as W7-S1 and W7-S2 and the round's cheapest one to close.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_CANON-W1-S2",
  "project": "LGIC_CANON",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The exception register's two carriers had diverged by one entry, X6 (opal-data-demo, GRANTED), which the canon's section 4 never carried; and X6's axis value is 'tenancy', outside the A1-A5 domain of the schema line the canon keeps. Now that CN-k-1 item 7 makes the ledger the entries' one home, X6 is the one entry that does not fit the register schema and there is no second carrier for it to be right in.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md@05ace72349#LGIC_CANON-W1-S2",
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_CANON-C-S6",
   "RE-READ by 3.0.0_SA_CVO at the register itself, 7 of 7 entries at 783e2f3887: infra/logic/06_CONFORMANCE_LEDGER.md :132-138. X1 A1, X2 A2, X3 A2, X4 A2/A5, X5 A5, X7 A2 -- and :135 X6 axis 'tenancy'",
   "infra/logic/02_DOCTRINE.md@783e2f3887 section 4's register schema line, 'pipeline . axis (A1-A5) . ...'"
  ],
  "remedy": "One of two Rule-24 acts, and they are not equivalent: give X6 an axis inside A1-A5, or widen the schema's axis domain with the four-postulate record and a word-boundary token census that a widening requires. The register's entries are written by 1.0.0_SA_CTO and 4.0.0_SA_CRO, so this seat names the fork and does not choose it. The ledger's own X6 row already carries the substance (a DEMO-TENANT class, Andrew-direct card 8), so nothing is being re-decided -- only placed on an axis the schema admits.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_CANON-W6-S1",
  "project": "LGIC_CANON",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "A new firm's identity row cannot be written without two values no builder or rule produces: its LONG and SHORT forms. The schema's firm list is a closed list of four firms resting on Andrew's word, the canon rules which form each slot takes but derives neither, and the only onboarding runbook tells the operator to choose the slug. The checklist takes both from Andrew as inputs and derives nothing.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md@05ace72349#LGIC_CANON-W6-S1",
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_CANON-C-S7",
   "infra/logic/10_ONBOARDING_CHECKLIST.md@05d5131e5e :32-42 -- the inputs table, read in full by 3.0.0_SA_CVO: 7 rows, the first of which is the two firm forms from Andrew, citing this row",
   "infra/logic/02_DOCTRINE.md@783e2f3887 R1 -- each firm has ONE sanctioned LONG and ONE SHORT form, Andrew ~03:5xZ; no rule derives a new firm's two forms"
  ],
  "remedy": "Rule whether a rule SHOULD derive them (for example SHORT from LONG) or whether they stay sovereign inputs, and say so in the canon either way. Taking them from Andrew is not itself a defect -- the checklist is explicit and the input is named -- so the decision is about FWD-5's bar, not about the checklist's honesty: an input Andrew supplies is not 'somebody inventing an answer', and if that reading is ruled, this row closes without any artifact changing. 1.0.0_SA_CTO and LGIC_NAMING's owner carry it to Andrew.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_CANON-W6-S2",
  "project": "LGIC_CANON",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The acts that give a firm's people their sign-in have no LGIC_ENFORCE CONTRACTS builder and are not generated views: the opal-partner-<firm> table (one hand-written partner-firms/<firm>.tf per firm), the user rows written with CLI put-item, and the portal page-access map FIRM_ALLOWED_PATHS, edited by hand. So the checklist's sign-in step can name only the identity row as its input and has to take the portal path list from Andrew.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md@05ace72349#LGIC_CANON-W6-S2",
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_CANON-C-S7",
   "infra/aws/terraform/partner-firms/ at 783e2f3887 -- 49financial.tf, cottonwood.tf, demo.tf, inflection.tf: one hand-written file per firm, confirming the per-firm hand act this row names",
   "org/missions/D14/LGIC/LGIC_ENFORCE/prd/LGIC_ENFORCE_PRD.md CONTRACTS -- nine rows, none producing the sign-in table, the user rows or the page-access map"
  ],
  "remedy": "A CONTRACTS row, or a DEC-5 generated carrier, for the sign-in plane -- and FIRM_ALLOWED_PATHS is the clearest candidate, being exactly the per-firm hand-kept map DEC-5 turns into a generated view. The canon rules only the storage plane, so ruling this also answers whether the canon's domain widens or whether the sign-in plane is LGIC_ENFORCE's alone. Read with W6-S3 and C-S12: the same plane is where the only live undeclared naming departure sits.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_CANON-W6-S3",
  "project": "LGIC_CANON",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "A new firm's dashboard is served through routes that read tier-first keys -- the edge auth validator reads platinum/{firmId}/ownership_map.json and the router asserts platinum/advi/{firm}/ -- which key() and address() cannot produce, and the legacy_served_paths list that would admit them does not exist yet (it waits on LGIC_NAMING's LN-g-1). A runner faces typing the legacy key by hand, which Rule 30 forbids, or publishing at the builder address, which the route never reads. The checklist STOPs there.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md@05ace72349#LGIC_CANON-W6-S3",
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_CANON-C-S7",
   "infra/logic/10_ONBOARDING_CHECKLIST.md@05d5131e5e Step 10's STOP, which Steps 15 and 16 both depend on",
   "org/missions/D14/LGIC/LGIC_CANON/deliverables/CHECKLIST_REVIEW.md@894b41f920 STEP 10, STEP 15, STEP 16 -- all three marked MECHANICAL, and all three blocked at this STOP today"
  ],
  "remedy": "Two owners and they must move together: the served-route side (ADVI_FIRMBKTS's router work) and LGIC_NAMING's LN-g-1 legacy list, with the routing decision 1.0.0_SA_CTO's. THE SEQUENCING POINT THIS SEAT ADDS, and it bears on the whole recut: a round that drives W7-S3's five JUDGEMENT marks to zero and leaves this row open has not moved FWD-5 at all, because the checklist still cannot be run end to end -- three of the eleven MECHANICAL steps are blocked at this STOP. The JUDGEMENT count and the runnability are two different bars and only the first is measured by O2-AC2.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_CANON-W7-S3",
  "project": "LGIC_CANON",
  "fabric": "laptop",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "A reviewer who did not write the onboarding checklist marks 5 of its 16 steps JUDGEMENT (3, 7, 8, 9, 14), so O2-AC2 reads FAIL-O2-JUDGEMENT-STEP and the order stays open. Four of the five share one cause: onboarding bundles the build of the firm's pipelines, and the canon fixes a pipeline's homes, formats, compute and name grammar but not its contents -- the source directory and master label, the resource set and function words, the bronze and silver table names and bronze's partition form, the gold table names and partition form and a combined build's owner. No input carries them and key()/address() pass table and partition through _segment unchecked, so two runners could build two different trees for one firm and both pass every gate the checklist names. The fifth, Step 14, is a different cause and is widened at C-S12.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md@05ace72349#LGIC_CANON-W7-S3",
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) rows LGIC_CANON-C-S7 and LGIC_CANON-C-S1 (grade O2-J1 PASS)",
   "org/missions/D14/LGIC/LGIC_CANON/deliverables/CHECKLIST_REVIEW.md@894b41f920 -- all 16 marks read by 3.0.0_SA_CVO, not sampled, and every reason found to hold",
   "infra/logic/10_ONBOARDING_CHECKLIST.md@05d5131e5e :32-42 -- the inputs table read in full: it carries no source directory, master label, table name, partition form, resource set or function word"
  ],
  "remedy": "The review names the shape of the fix and it is right: an input that fixes the pipeline's CONTENTS would move the first four marks at once -- for example 'the firm runs the vendor's existing pipeline with scope <LONG>, under the tables and resources it already names for the firms it serves'. That is one decision, not four, and it is the canon's or the checklist's, not the reviewer's. THE BAR TO WATCH ON THE RECUT: O2-AC2 counts JUDGEMENT marks, and a step can be MECHANICAL, defective and unrunnable all at once -- see C-S13 for a defect invisible to the count and W6-S3 for three MECHANICAL steps blocked today.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_CANON-W8-S1",
  "project": "LGIC_CANON",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "lib/opal_naming.py address() writes the platinum key advi/49financial/platinum/advisors/advisor_id=A123, and grade() in the same library calls that exact key OUT-OF-PATTERN with canonical advisor-id=a123. grade()'s _new_served sets leaf = len(rest) - 1 whenever the key is not a prefix and rewrites a leaf that is not kebab .json, so it reads a trailing entity partition as the file leaf and rewrites the entity id's bytes -- contradicting both the builder and NAMING_SCHEMA key.partition's own example. A pipeline built to Rule 30 gets every platinum key ending in an entity partition graded OUT-OF-PATTERN.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md@05ace72349#LGIC_CANON-W8-S1",
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_CANON-C-S8",
   "MEASURED by 0.9.0_WK_LGIC_CANON~8: grade(k,'S3Key') on 'advi/49financial/platinum/advisors/advisor_id=A123' gave OUT-OF-PATTERN, canonical 'advi/49financial/platinum/advisors/advisor-id=a123'; the same key with a trailing '/' gave CONFORMANT, and with '/profile.json' appended also CONFORMANT; the gold key gave CONFORMANT because gold never reaches _new_served",
   "1.0.0_SA_CTO 97211 and 97294 -- the ruling that address() and the schema are right, grade()'s _new_served is the defect, it is INERT while org/mcp/naming-gate.enforce is absent, and the fix is a cell of LGIC_ENFORCE round 2"
  ],
  "remedy": "The substance is already ruled by 1.0.0_SA_CTO and this seat does not reopen it: the fix is a cell of LGIC_ENFORCE round 2's issuance, cut by 2.0.0_SA_COO~G, teaching _new_served that a trailing {entity}={id} segment is a partition and not a leaf. What was OWED and is now possible is the DISARM: the ruling lived in a message, and a disarm in prose disposes nothing. The gate admits it only as the ARMED -> DISARMED advance on this row, with `at` moving from null to a timestamp and every other field byte-equal. 1.0.0_SA_CTO advances that clock; the row it needs now exists.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "disarm": {
   "state": "DISARMED",
   "owner": "1.0.0_SA_CTO",
   "at": "2026-09-16T06:16Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~G",
   "round": "v1"
  },
  "closed": true
 },
 {
  "id": "LGIC_CANON-C-S9",
  "project": "LGIC_CANON",
  "fabric": "laptop",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "FWD-1's blind judges were not independent on the scale they graded with. The axis verdict vocabulary AND its severity order were supplied by the task-order face -- TO-CN-j-1 :21 and TO-CN-j-2 :21 are byte-identical -- and three of the five verdict values appear nowhere in the canon (CONFORMS 0 occurrences, VIOLATES 0, DECLARED-EXCEPTION 0 over 574 lines; DEPARTS-RECOMMENDED 1, UNDETERMINED 1, neither as an axis verdict). No severity order appears at all. So the 5-of-5 verdict agreement is agreement on a scale the ORDER fixed. The discriminating contrast sits inside the same exercise: the NAMING case vocabulary IS canon-carried (CONFORMANT 16, ALIAS 2, OUT-OF-PATTERN 4, RAISE 3), and that is exactly the half where both judges went off the key.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_CANON-C-S9",
   "MEASURED by 3.0.0_SA_CVO at 783e2f3887: the two order lines extracted and compared with cmp -- IDENTICAL BYTES; the five-value census over infra/logic/02_DOCTRINE.md with its 574-line denominator",
   "org/missions/D14/LGIC/LGIC_CANON/deliverables/exercises/judge-a.tsv@537f49b8fd row A1 ('which is less severe than UNDETERMINED') and judge-b.tsv@98ed3177ff row A1 ('UNDETERMINED is the more severe finding') -- both reasoning explicitly from the order's ranking, which is why A1's verdict agreed while its rule set split",
   "org/missions/D14/LGIC/LGIC_CANON/deliverables/exercises/judge-compare.md@62dcc19f6c s.4 D1 -- 'The axis verdict vocabulary and its order therefore came to the judges from outside the canon, and this worker did not read where.' This row answers that sentence"
  ],
  "remedy": "One of two, and the choice is a real fork the CTO should make rather than inherit. EITHER the canon carries the axis verdict vocabulary and its severity order -- which makes the canon answerable on 'is this conformant' in its own words, and is the reading section 0 already implies -- OR the order keeps supplying it and the round states plainly that verdict agreement is not evidence about the canon, so FWD-1 is graded on the rule citations alone. Until one is taken, a 5-of-5 verdict result cannot be read as canon evidence in this round or the next. Cheap and worth doing either way: a third judge briefed WITHOUT the severity order, as the negative arm.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_CANON-C-S10",
  "project": "LGIC_CANON",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The only instrument this round that tried to APPLY the canon reached 14 of its 21 rules. Computed as a subtraction from the printed denominator: the canon's rule ids are R1 to R21 with no gaps, matching its own section 0 census line 'RULES CARRYING ALL THREE PARTS: 21 of 21'; the rule ids appearing anywhere in both judges' answer files combined are R1, R2, R4, R5, R6, R7, R9, R10, R11, R12, R13, R16, R18, R20; the difference is R3, R8, R14, R15, R17, R19, R21. K1-J1's bar says EACH rule, so on seven of them the bar is unevidenced in either direction.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_CANON-C-S10, and row LGIC_CANON-C-S1 (grade K1-J1 FAIL, where this is the coverage half)",
   "MEASURED by 3.0.0_SA_CVO at 783e2f3887: whole-value R-id census over infra/logic/02_DOCTRINE.md returns R1..R21; the same census over judge-a.tsv and judge-b.tsv returns 14 ids; comm -23 over the two sorted sets returns R14 R15 R17 R19 R21 R3 R8",
   "infra/logic/02_DOCTRINE.md@783e2f3887 :28 -- the section 0 census line this subtraction uses as its denominator",
   "org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/CN_TREE_MDPF.md -- the one tree judged"
  ],
  "remedy": "A second tree at the next round's C2, chosen to engage the seven the MDPF tree does not: a general-data plane (R8), a plane whose most-derived consumer sets the obligation (R15), a plane carrying backups or scratch (R17), a vendor master with two masters of one firm (R3), a state/ plane (R21), and a family with a live migration (R19); R14's 2x2 grid is engaged by any of them. This is a COVERAGE fact about the instrument, NOT a claim that those seven rules are unapplicable -- and it is the reason K1-AC1's '21 of 21' must not be read as evidence for K1-J1: that criterion certifies the document's SHAPE, that each rule carries an authority, a census tag and a non-application, and says nothing about whether a seat can apply it.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_CANON-S3",
  "project": "LGIC_CANON",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "render_naming_section.py's two source paths are not equivalent readers: the schema path emits a per-firm note, the registry path reads long and short and never reads the FIRM row's note field. So when NAMING_SCHEMA v1.9 dropped firm_forms and the renderer fell to the registry, the canon's generated section LOST the demo bullet carrying RULING DM -- the one line saying why demo reads as a firm in every naming slot. --check reads FRESH over the loss, because the section IS a faithful render of what the renderer chose to read.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md@5bdaa031c0#LGIC_CANON-S3 -- filed by 2.0.0_SA_COO~G at 2026-09-16T05:52Z, with the renderer read and the --write diff as its instrument",
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_CANON-C-S11",
   "CORROBORATED by 3.0.0_SA_CVO on a DIFFERENT instrument, independently and before S3 was read: git diff 671925aecc 783e2f3887 -- infra/logic/02_DOCTRINE.md, 3 insertions and 4 deletions, one of which is the whole demo bullet. Same loss, approached from the artifact rather than from the renderer",
   "org/standards/NAMING_SCHEMA.json at ac82ad2331 -- v1.9, firm_forms absent, 'W6-S4' (1), 'RULING DM' (2), 'demo reads as a firm' (1); infra/logic/registry/scopes.json row demo carries the same text in its note. The ruling survives at its owner",
   "org/missions/D14/LGIC/LGIC_CANON/task-orders/LGIC_CANON.TO-CN-j-1.judge-a.md -- the blindness clause: read ONLY the canon, the tree file, the case list and the order"
  ],
  "remedy": "S3's own remedy is right and cheap: one line in the renderer's registry branch reading the FIRM row's note, re-emitting the bullet exactly as the schema path did. TWO THINGS THIS SEAT ADDS AT L9. First, the CONSEQUENCE, which is why this is worth a round-2 cell rather than a tidy-up: the presentation is what FWD-1 measures, and both carriers that still hold the ruling are documents the judging order forbids a judge to open -- so the next thing this costs is an unexplainable judge disagreement, not a missing line anybody notices. Second, the CLASS: the per-field fix closes the demo note and not the shape, because --check's contract is 'these bytes equal a fresh render' and nothing anywhere asks 'did this render drop something the last one carried'. A content diff of the section against its previous rendering, surfaced at the render, is the general arm and it is small. HAZARD STANDING carried as filed: this seat read the same hazard as INERT under PRD DEC-9 and does not downgrade another seat's standing -- a disarm is the disarm owner's act. K1-AC2 is unaffected and this seat confirms it: the section IS a fresh render.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v1",
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~G",
   "at": "2026-09-16T12:30Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~G",
   "round": "v1"
  },
  "closed": true
 },
 {
  "id": "LGIC_CANON-C-S12",
  "project": "LGIC_CANON",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Step 14's prescribed-name conflict is a live estate condition, not a hypothesis about a new firm. grade() reads the partner table of all four firms that exist today as OUT-OF-PATTERN -- opal-partner-demo, -49financial, -cottonwood, -inflection, canonical opal-demo-partner-table, opal-49f-partner-table, opal-cot-partner-table, opal-inf-partner-table -- and there is one hand-written module file per firm in infra/aws/terraform/partner-firms/, so four live tables carry the refused shape. The auth handler builds the name as opal-partner-{firmId} and portal-auth's IAM grant covers opal-partner-*, so the canonical form is not available without breaking sign-in. The exception register's seven entries, read one by one, declare none of it.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_CANON-C-S12",
   "RUN by 3.0.0_SA_CVO at 783e2f3887, read-only: grade(n,'DYNAMODB_TABLE') over all four firm forms returned OUT-OF-PATTERN four times with the four canonical forms above",
   "infra/logic/06_CONFORMANCE_LEDGER.md@783e2f3887 :132-138 -- X1 through X7 read one by one; none names a partner table. This replaces the review's scoped census with a direct read of the register itself",
   "infra/aws/terraform/partner-firms/ -- 49financial.tf, cottonwood.tf, demo.tf, inflection.tf"
  ],
  "remedy": "An R20 register entry naming the auth handler's requirement and the IAM grant as the reason, which is the honest reading -- the departure is real, it is forced, and R20 exists for exactly that. The alternative, renaming, breaks sign-in and is not a live option without a migration under R19. Either way the checklist's Step 14 gains a STOP naming the owner, so a runner is never asked to choose which of two prescribed rules gives way. WHY THIS IS NOT MERELY W7-S3's fifth mark: a JUDGEMENT mark on a step nobody has run is a document defect; four live undeclared resources on the sign-in path are an estate condition with an owner today, and its remedy is a register act rather than a checklist edit.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_CANON-C-S13",
  "project": "LGIC_CANON",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The firm-bucket template carries TWO comment blocks. Step 6 replaces the header block and prescribes 'Replace every 49financial with <LONG>' -- and the SECOND block, the cross-firm Deny's standing record at :69-98, is neither replaced nor exempted, so the replace-all rewrites it. At the bytes: :74 reads 'opal-data-49financial IS the bd/49F firm's client bucket', which becomes a false sentence for any other firm, and the Rollback line at :97-98 names the ledger entry 20260915T0334Z_lgic-enforce-fence-49financial_deploy_completion.md, which becomes a path that does not exist. That block also carries the LGIC_ENFORCE EN-f-1 DEC-4 replacement note and the resolution of an over-inclusive Deny -- standing record, not boilerplate.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_CANON-C-S13",
   "infra/aws/terraform/shared-infra/s3-49financial.tf@783e2f3887 -- read by 3.0.0_SA_CVO: :1-12 the header block, :69-98 the second block, :74 and :97-98 the two lines the replace-all corrupts",
   "infra/logic/10_ONBOARDING_CHECKLIST.md@05d5131e5e :149-157 -- the enumerated edits 'and no others'",
   "org/missions/D14/LGIC/LGIC_CANON/deliverables/CHECKLIST_REVIEW.md@894b41f920 STEP 6 -- the reviewer found it and marked the step MECHANICAL, correctly, because it asks the runner to decide nothing"
  ],
  "remedy": "One line in Step 6 naming the second block: either keep it verbatim, or replace it too with a line pointing at this checklist. THE REASON IT NEEDS A ROW AT ALL: the review's MECHANICAL mark is right on its own test, so this defect is INVISIBLE to O2-AC2's JUDGEMENT count -- driving that count to zero would leave it exactly where it is. That is the general shape worth carrying into the recut: the checklist's acceptance measures whether a runner has to invent an answer, and says nothing about whether following the instructions produces a correct artifact.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false
 }
]
```

-- 3.0.0_SA_CVO
