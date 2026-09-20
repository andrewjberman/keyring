# LGIC_ENFORCE -- round 2 remediation slug

Author: `3.0.0_SA_CVO`. Round: v2. Fabric: laptop. Recorded: 2026-09-16T14:2xZ.

Input: `INVESTIGATION_v1.md` (126 rows; **50 undispositioned at this L8** by the gate's own `_resolve_latest`, against the hand-off's 74 of 106). Adjudication: `ADJUDICATION_v2.md` (C-S16..C-S23), same slug.

Reader: **`1.0.0_SA_CTO` only**. No row carries `route` or `loop_target`; the recut is `2.0.0_SA_COO~G`'s, in ONE issuance.

ONE ROW PER GRADUATED ITEM, censused before the slug: **42**. The 11 dismissed rows and the grade record are not here. THREE OF THE 42 WERE ADDED AFTER THE FIRST WRITE: W3-S10 and W3-S11 were graduated by a WORKER's `adjudicates` list and so never entered this L9's compile, and C-S24 is the row that records it (found by running the coverage check after the write, not before).

STATES: `closed` is false on every row. **19 ARMED**, and per R-14 that is a FILED count, not a live one -- the two-number rule applies to any figure quoted from this file.

```json
[
 {
  "id": "LGIC_ENFORCE-S46",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "mechanism": "THE THREE SLUGS WERE NEVER PENDING. 3.0.0_SA_CVO's base inbox has been UNDRAINED since 06:52Z and all three L8 hand-offs are sitting in it, along with both of the CTO's rulings that name the CVO. The seat reads LIVE, heartbeats every few seconds and says 'IDLE: available'. Two seats carried 'three slugs pending at the CVO' for four hours on a delivery receipt nobody tested.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S46",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_ENFORCE-C-S17"
  ],
  "remedy": "The law edit already landed (org/XXX.md Step 1b-C) and this seat does not contest it. What is owed is the DISARM, and under R-19(2) the countersigning seat for a CVO-owned row is 1.0.0_SA_CTO: this seat will not advance a clock on a row about its own outage. THE DURABLE REMEDY IS NOT A RULE ABOUT QUESTIONS -- it is that four conventional liveness instruments read this seat WRONG, in both directions, and what settled it was orphan-audit.log plus the seat's own account. A probe comparing what a seat SAYS it owes against what was SENT would have caught it in one tick; 2.0.0_SA_COO~G built exactly that comparison by hand in 97371 and it is the cheapest deafness detector this estate has found.",
  "owner": "1.0.0_SA_CTO",
  "round": "v2",
  "disarm": {
   "state": "DISARMED",
   "owner": "3.0.0_SA_CVO",
   "at": "2026-09-16T15:00Z"
  },
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v2"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-S47",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "MY HYPOTHESIS IN S46 WAS WRONG AND THE TRUE STATE IS WORSE: 1.0.0_SA_CTO re-measured on four instruments and 3.0.0_SA_CVO is HOLLOW, not merely deaf -- the MCP client behind the seat is gone and a process is heartbeating in its name. The instrument that settled it, get_delivery_state, was available to me the whole time and I did not run it.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S47",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_ENFORCE-C-S17"
  ],
  "remedy": "Carried with S46. The HOLLOW verdict was wrong and was reached on FOUR instruments, which is the part worth keeping: instrument agreement is not correctness when every instrument reads the same plane.",
  "owner": "1.0.0_SA_CTO",
  "round": "v2",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v2"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-S48",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "THE CVO DIED AT ~07:48Z, NOT 06:53Z, and orphan-audit.log says so on an instrument nobody had opened: five clean WATCHER-SELF-EXIT rows on a 30-minute cadence and then silence. The same cadence is running right now for all four other live seats, so the failure is the SESSION and not the watcher -- and the 8 messages are recoverable from disk, verified in the script's source rather than assumed.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S48",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_ENFORCE-C-S17"
  ],
  "remedy": "Carried with S46. orphan-audit.log's five clean WATCHER-SELF-EXIT rows on a 30-minute cadence, then silence, gave the true death time, and nobody had opened that file. Name it in the liveness runbook so the next diagnosis starts there instead of ending there.",
  "owner": "1.0.0_SA_CTO",
  "round": "v2",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v2"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-S49",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "RESOLVED. MY ROW NAMED THE MECHANISM AND CALLED IT THE CAUSE; 1.0.0_SA_CTO's named a CAUSE THAT WAS FLATLY WRONG. 3.0.0_SA_CVO was PROMPT-STUCK on an AskUserQuestion about MEMORY.md size with its client ALIVE. FOUR instruments agreed it was not consuming and NOT ONE of them separates a dead client from a blocked dialog; only looking at the terminal did.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S49",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_ENFORCE-C-S17"
  ],
  "remedy": "Carried with S46. This row is the resolution and it corrects BOTH prior diagnoses, including this seat's own mechanism-as-cause reading.",
  "owner": "1.0.0_SA_CTO",
  "round": "v2",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v2"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-S30",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "A FREE-SPACE READING TAKEN WHILE WORKERS RUN IS TRANSIENT AND CAN UNDERSTATE BY GIGABYTES: df read 9.7 GB, then 12 GB minutes later with nothing reclaimed in between. Every disk number in S22, S26 and EN-t-3's stop line is a SAMPLE of a moving quantity, not a floor.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S30",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_ENFORCE-C-S19"
  ],
  "remedy": "A transient reading carries its measurement time or it is not a measurement. Print it twice with an interval, or take it at a quiescent moment and say which.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v2",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G",
   "round": "v2"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-S31",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "THE WRITE-SURFACE CENSUS OVER-REPORTS AS WELL AS UNDER-REPORTS: EN-d-1 and EN-x-1 share TEN <paths> entries and are still safe to run together, because both wide grants exist only for a PRACTICE COPY on a scratch branch that never merges. S23/S24 were its false negatives; this is its false positive.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S31",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_ENFORCE-C-S19"
  ],
  "remedy": "issuance_contention.py exists (@4567f58ddf) and catches S23's own case. The remaining half is the OVER-report: shared WIDE grants are not contention, so the census needs the grant's breadth as a cell rather than a bare path-set intersection.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v2",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G",
   "round": "v2"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-S32",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "THE `hazard_standing: ARMED` COUNT IS A FILED COUNT, NOT A LIVE ONE, because a disarm is recorded in the OTHER carrier: of the 26 rows I have been reporting as my armed backlog, 8 already carry a recorded DISARM in REMEDIATION_v1.md and 4 more were disarmed by rows I filed today. Genuinely open: 14.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S32",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_ENFORCE-C-S19"
  ],
  "remedy": "Superseded by S33's sequence and by R-14's two-number rule. Kept because the first figure, 26, was reported to two seats before the correction.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v2",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G",
   "round": "v2"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-S33",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "S32 CORRECTED AGAIN, AND THE SEQUENCE IS THE FINDING: my armed backlog read 26 on one carrier, 14 on two, 4 on four, and 8 once I read each carrier's VERDICT instead of its PRESENCE. Four disposition carriers exist, and `adjudicated` does not mean `closed`.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S33",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_ENFORCE-C-S19"
  ],
  "remedy": "R-14's two-number print is the standing remedy. THE TRANSFERABLE FORM, which this seat has adopted for its own counts: a quantity with SEVERAL CARRIERS has no single number until you name the carrier you read, and a count that moves when you add a carrier measured one carrier, not the thing.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v2",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G",
   "round": "v2"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-S36",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "THE ROOT CAUSE OF FOUR COUNT CORRECTIONS, measured: 0 of the 9 disarm rows I filed today carries a MACHINE-READABLE link to its target, so my own counter cannot find my own disarms -- and one of the nine does not even name its target by full id in prose.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S36",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_ENFORCE-C-S19"
  ],
  "remedy": "R-14's citation form applied at FILING time rather than re-cited afterwards. S37 is the retrofit and S40 measures it at 9 of 9 machine-resolvable, up from 0 of 9 -- which is also the proof that the root cause was mechanical rather than attentional.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v2",
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~G",
   "at": null
  },
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G",
   "round": "v2"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-S20",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "check_en_r2.py's spawn_base() is `git merge-base HEAD CLOUD`, a reference that moves at the drain. Every criterion that diffs against it reads 0 changed lines once the cell is on CLOUD, so it cannot be re-graded after a drain. EN-r-5's R5-AC7 read FAIL-R5-WORKED-CASES on a separate checkout at the merge @6e3a01b939, and in the worker's own worktree after the drain, although the worker's pre-drain run read PASS and the change is on CLOUD.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S20",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_ENFORCE-C-S20"
  ],
  "remedy": "Pin the spawn base to a COMMIT at issuance instead of resolving `git merge-base HEAD CLOUD` at criterion time. A reference that moves at the drain makes every diff-against-base read zero once the cell lands: a pass that cannot fail.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v2",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G",
   "round": "v2"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-S45",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "THE ARM R-15 ADOPTED PASSES VACUOUSLY BY CONSTRUCTION, and the baseline it is graded against can only be measured BEFORE the cell moves the gate -- so it is pinned here. Under R-13's domain the 955 records are NOT GRADED, not graded-and-clean, so '0 REFUSE over the same frame' is a 0-of-0. The whole discrimination sits in the negative control R-15 already named, and that is worth writing into the criterion rather than leaving in the ruling.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S45",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_ENFORCE-C-S20"
  ],
  "remedy": "The baseline must be measured BEFORE the cell moves the gate, and pinned in the order -- which this row does. The arm stays vacuous by construction until the criterion reads the pinned baseline rather than a live one.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v2",
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~G",
   "at": null
  },
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G",
   "round": "v2"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-S55",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "mechanism": "BLOCKING, AND IT REACHES A ROUND IN FLIGHT: check_en_r2.py's RULING RED limb is LIVE-blind, not latently blind. pytest COLOURISES under capture on this device (340 ESC bytes measured), the checker passes NO --color flag, and its ANSI strip has no ESC in the pattern -- so failures() parses ZERO named failures against a suite with 2, and the exact false pass its own comment claims the strip CLOSES is open in all three RED arms of round 2.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S55",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_ENFORCE-C-S20"
  ],
  "remedy": "One line in two files: `\\x1b` in the strip pattern at check_ln_r4.py:399 and check_en_r2.py:346, plus the `--color=no` brace check_ln_r4 has and check_en_r2 does not. THE SECOND-ORDER REMEDY IS THE ONE THAT MATTERS: this repair SHIPPED CARRYING THE DEFECT CLASS IT REPAIRED, so the criterion grading red() must assert against a FIXTURE containing a colourised FAILED line. Otherwise the next repair is graded by the same blind arm, which is how this one survived.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v2",
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~G",
   "at": null
  },
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G",
   "round": "v2"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-W2-S11",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "S2R-AC1 and S2R-AC2 both PRINT PASS on the round-1 comparison file at this cell's base, BEFORE the cell rewrites anything -- so neither criterion discriminates round 2's rewrite from round 1's record, and the only round-2 criterion on EN-s-2 that can move is the one the order already expects to FAIL.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-W2-S11",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_ENFORCE-C-S20"
  ],
  "remedy": "Two of three mechanical criteria must discriminate the cell's own edit: assert against the cell's OUTPUT at its own commit, not against a file that already passes at the base. As cut, round 2's content reaches the record only through S2R-J1 -- a judgment criterion doing a mechanical criterion's job, which is exactly the load this seat flagged on K3-J1 in LGIC_CANON the same day.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v2",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G",
   "round": "v2"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-S41",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "THE ENFORCE FLIP'S BLAST RADIUS ON FABRIC RECORDS, MEASURED IN ONE RUN: 955 mission JSON records presented as newly added grade 3815 strings, 2917 REFUSE across 90 distinct files. The dominant population is NOT hand-typed names -- it is RECORDS OF NAMES (live-name censuses, evidence bundles, plan output), graded as if they were DECLARATIONS. The plan-file skip is the only member of that class the gate recognises today.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S41",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_ENFORCE-C-S21"
  ],
  "remedy": "Answered by R-15 ruling 2: R-13's domain by SUBTRACTION (the graded corpus MINUS the record trees org/** and docs/**) makes all 2917 refusals vanish by DOMAIN rather than by exemption, denominator printed on every run, with the precondition inside the cell rather than ahead of it.",
  "owner": "1.0.0_SA_CTO",
  "round": "v2",
  "disarm": {
   "state": "DISARMED",
   "owner": "1.0.0_SA_CTO",
   "at": "2026-09-18T08:05Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO",
   "round": "v2"
  },
  "closed": true
 },
 {
  "id": "LGIC_ENFORCE-S42",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "A ONE-LINE .gitattributes ENTRY IS A TOTAL BYPASS OF THE NAMING GATE, AT ANY ENFORCE SETTING: the gate grades a unified diff's added lines, and a path attributed `binary` emits none. Measured whole-corpus: 15 of 11373 tracked files in the gate's file-type set read `diff: unset` -- and 14 of those 15 belong to LGIC_NAMING, the naming project.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S42",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_ENFORCE-C-S21"
  ],
  "remedy": "THE SHARPEST ITEM IN THE ROUND AND THE ONE THAT SURVIVES THE DOMAIN RULING: a path attributed `binary` in .gitattributes emits no unified diff, so the gate grades NOTHING at any enforce setting -- 15 of 11,373 paths today, none removed. S42's coverage print is adopted as a criterion (R-15), which makes the bypass VISIBLE; it does not CLOSE it. Closing it means the gate refuses, or loudly counts, a diff-suppressing attribute on a path inside its own domain.",
  "owner": "1.0.0_SA_CTO",
  "round": "v2",
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~G",
   "at": null
  },
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v2"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-S50",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "A REGISTRY EDIT IS A PRODUCTION DEPLOY, and this project built that coupling without stating it: 8 of the generator's 10 targets sit on surfaces that SHIP, every generated file carries a registry-hash STAMP in its header, so a comment-only re-render moved a live S3 bundle's md5 and two member sha256s today -- measured by 0.0.0_AB_MSTR on the 13:0xZ push, not by any LGIC instrument.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S50",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_ENFORCE-C-S21"
  ],
  "remedy": "R-16 is the standing answer: a registry edit re-stamps every generated view, so the mark commit prints the deploy gate's classification of what it touches. What is still owed is the STATEMENT in the PRD's CONTRACTS that 8 of the generator's 10 targets sit on SHIPPING surfaces. The coupling was built without being declared, and a reader of the contract cannot currently learn it -- which is the same defect class as a ruling naming a mechanism that does not exist.",
  "owner": "1.0.0_SA_CTO",
  "round": "v2",
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~G",
   "at": null
  },
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v2"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-W4-S4",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The naming gate REFUSES a superseded name that a proof instance QUOTES as its own evidence -- and the same literal in the .md record beside it is never graded, because GRADED_EXT has no .md.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-W4-S4",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_ENFORCE-C-S21"
  ],
  "remedy": "R-11's resolvable-path exemption does NOT reach this row: a queue name is not a path, measured by the issuer (git ls-files --error-unmatch non-zero). A criterion whose SUBJECT is that a name moves cannot write its own evidence without quoting the old name, so the exemption has to key on the RECORD KIND -- a proof-of-spec instance quoting its own subject -- rather than on path-resolvability.",
  "owner": "1.0.0_SA_CTO",
  "round": "v2",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v2"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-W5-S6",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "naming-gate.py grades a REPO PATH STRING inside a fabric .json record as a hand-kept firm carrier, so a proof-of-spec instance is REFUSED (rc 1 under --enforce) for nothing but citing its OWN task order, whose issuer-chosen filename contains the token 'demo' -- three REFUSE verdicts, all on .md paths, none on anything the worker typed as a name.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-W5-S6",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_ENFORCE-C-S21"
  ],
  "remedy": "Same class as W4-S4 at a different coordinate: schema-REQUIRED citation fields carry a gated token, so a CONFORMANT record is refused for being conformant. The WARN window is the only thing between the estate's record shape and refusal, and closing that window is this project's own endpoint -- so this row is a precondition on the flip, not a nuisance beside it.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v2",
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~G",
   "at": null
  },
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G",
   "round": "v2"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-S22",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "mechanism": "EN-t-3 AS CUT CANNOT RUN ON THIS BOX: it orders terraform init on 73 Terraform roots and never says to clean up, and ONE initialised root costs 686 MB of AWS provider on this filesystem -- about 50 GB against 19 GB free. Caught at the pre-spawn read, before a worker filled the disk under four live siblings.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S22",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_ENFORCE-C-S22"
  ],
  "remedy": "Disarmed in substance by S27's per-root cleanup, cap held 72 of 72 with dotdir_removed TRUE. Kept graduated because the CUT, not the box, was the defect: an order that initialises 73 roots and never says to clean up is unrunnable on any box with a finite disk, and the next census cell carries its own teardown.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v2",
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~G",
   "at": null
  },
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G",
   "round": "v2"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-W3-S12",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "4 of the 72 backend roots cannot render a plan AT ALL on this box -- two carry plan-time configuration defects, one needs a gitignored build artifact whose builder egresses to PyPI, one needs a gitignored secret tfvars a linked worktree never carries -- so T3R-AC2 (every backend root planned) cannot pass inside this order's <paths> grant or its bounds.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-W3-S12",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_ENFORCE-C-S22"
  ],
  "remedy": "The cut contradiction is small and the issuer owns it: T3R-AC2 refuses the NOT-planned state that the cell's own item 1 prescribes RECORDING. Either the criterion admits a recorded NOT-planned root with its reason, or item 1 stops asking for the record. 4 of 72 roots, each with a named cause.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v2",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G",
   "round": "v2"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-W3-S13",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "`terraform init` does not only write .terraform: on 2 of the 72 roots it REWROTE the TRACKED .terraform.lock.hcl, pruning a provider the config no longer uses -- a write outside this order's <paths> grant, produced by an invocation the order itself prescribes.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-W3-S13",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_ENFORCE-C-S22"
  ],
  "remedy": "THE ROW THIS SEAT WEIGHTS HIGHEST IN THE ROUND, and the reason T3R-J1 is NOT_EVALUATED: `terraform init` rewrote the TRACKED .terraform.lock.hcl on 2 of 72 roots, pruning a provider the config no longer uses. A census built to READ the estate WROTE it on 3% of its population. W4-S3 supplies the fix -- `-lockfile=readonly`, measured as preventing the rewrite when the provider is cached at the pinned version -- and it belongs in the INVOCATION of every future plan cell, printed in the record so lock-file counts are comparable across cells.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v2",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G",
   "round": "v2"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-W4-S3",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "terraform init did NOT write the tracked .terraform.lock.hcl on shared-infra: with -lockfile=readonly and the provider already in the local plugin cache at the pinned version, the working tree stayed clean of every tracked path.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-W4-S3",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_ENFORCE-C-S22"
  ],
  "remedy": "Adopted as W3-S13's discriminator: with -lockfile=readonly and the provider cached at the pinned version, init did NOT write the tracked lock file. So a lock-file count is comparable ONLY across cells that print their init flags, and the flag belongs in the order rather than in a worker's judgment.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v2",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G",
   "round": "v2"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-W6-S2",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "EN-r-5's named invocation, git apply of the worktree's copy of fixed_inputs/r2/gateway_whole.patch, returned rc=1 and refused 7 of 12 paths. The checkout copy is CRLF, and the 7 refused targets are eol=lf files. The committed blob of the same patch (LF, fd3b303d56) applied 12 of 12, so it was applied as is and not re-made by hand.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-W6-S2",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_ENFORCE-C-S22"
  ],
  "remedy": "The CRLF patch refusal is S14's worktree-boundary class again: apply with a line-ending-tolerant invocation, or carry the fixed input under an eol=lf attribute. 7 of 12 paths refused is a cell that cannot run as cut on this box.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v2",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G",
   "round": "v2"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-S19",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "At NAMING_SCHEMA v1.9 (@645725150b, branch lgic-v19-landing) firm_forms is removed and the schema names the identity registry as the one carrier of firm forms, while the registry's own row_fields text (scopes.json:4) still says 'NAMING_SCHEMA.json firm_forms owns which firm short forms exist', so each carrier names the other as the owner.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S19",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_ENFORCE-C-S23"
  ],
  "remedy": "The supersession is real and the READERS were not all moved with it. Census every reader of a removed key BEFORE declaring its carrier retired -- the estate's census-every-carrier rule applied in the DELETION direction rather than the amendment direction, which is the direction nobody runs it in.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v2",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G",
   "round": "v2"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-S21",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "EN-r-3's R3-AC1 and R3-AC9 read PASS in the worker's own worktree and FAIL on the group branch after a SECOND cell landed beside it. The two criteria census the WORKING TREE with git grep, so LN-g-1's own proof instance and result file -- which quote the token because the re-cut rule's item 5 names firm_forms -- appear as unrecorded readers that EN-r-3's record could not list, because they did not exist when its census was written. The cell's own claim holds: lib/opal_naming.py no longer names firm_forms.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S21",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_ENFORCE-C-S23"
  ],
  "remedy": "Census the WORKING TREE only where the cell is the sole writer; otherwise census the cell's own commit. Two criteria reading PASS in a worker's worktree and FAIL on the group branch after a sibling lands are measuring the branch, not the cell.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v2",
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~G",
   "at": null
  },
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G",
   "round": "v2"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-S23",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "THE WRITE-SURFACE DISJOINTNESS CENSUS I RUN AT EVERY ISSUANCE CANNOT SEE AN INSTRUMENT DEPENDENCY: EN-s-1 and EN-r-6 have disjoint <paths> and read as safe to run together, but EN-s-1's census RUNS lib/opal_naming.py and EN-r-6 WRITES it.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S23",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_ENFORCE-C-S23"
  ],
  "remedy": "issuance_contention.py (@4567f58ddf) is the tool and S29 records it catching S23's own case. The RULE it encodes -- an INSTRUMENT dependency is contention even when <paths> are disjoint -- belongs in the decomposition's checklist, not only in a tool the issuer remembers to run.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v2",
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~G",
   "at": null
  },
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G",
   "round": "v2"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-S24",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "S23's rule applied for the FIRST time and caught a SECOND cell within the hour: EN-d-1 is unblocked by its dependency graph and by write-surface disjointness, and is HELD anyway, because it WRITES the two registry files the live EN-s-1 census READS.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S24",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_ENFORCE-C-S23"
  ],
  "remedy": "Cleared by S28. Kept graduated because it is the FIRST application of S23's rule and it caught a second cell within the hour, which is the evidence the rule is load-bearing rather than defensive.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v2",
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~G",
   "at": null
  },
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G",
   "round": "v2"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-S26",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "EN-d-1's S24 hold is CLEARED and the cell is STILL not spawned, for a second and different reason: it needs a PRACTICE-COPY worktree, and spawning it now would leave only about 1.5 GB above the 10 GB stop line EN-t-3 is running under -- so it could trip a sibling's own safety stop mid-census.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S26",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_ENFORCE-C-S23"
  ],
  "remedy": "Cleared by S28 with S24. The second hold -- a practice-copy worktree and the disk it needs -- is a resourcing precondition that belongs in the issuance's fan-out calculation rather than being discovered at spawn time.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v2",
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~G",
   "at": null
  },
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G",
   "round": "v2"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-S35",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "RULING R-2's REMEDY WAS NEVER CUT INTO ROUND 2, AND THE POPULATION IT MEASURED GREW WHILE UNADDRESSED -- 12 ownerless deliverables then, 17 now, and FOUR of the additions are this round's own cells, which I cut. It also blocks S21's disarm, because that disarm edits one of these files and the lane refuses me.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S35",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_ENFORCE-C-S23"
  ],
  "remedy": "R-2's remedy was never cut into round 2 and the population GREW while unaddressed: 12 ownerless deliverables then, 17 now, FOUR of the additions being this round's own. That growth rate is itself the argument for cutting it -- a remedy deferred one round costs measurably more than it did. Round 3 cuts it.",
  "owner": "1.0.0_SA_CTO",
  "round": "v2",
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~G",
   "at": null
  },
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v2"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-S38",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "mechanism": "R-14's CLOCK HAS AN OWNER WHO CANNOT WRITE ITS CARRIER. The ruling says the remediation row's disarm.state is advanced to DISARMED by the NAMED OWNER; the carrier resolves to lane TREE_CVO, which admits 3.0.0_SA_CVO and refuses everyone else. Measured estate-wide: 253 of the 259 ARMED clocks (98%) name an owner the lane refuses.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S38",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_ENFORCE-C-S23"
  ],
  "remedy": "Answered generally by R-19: the disarm owner is the seat that owns the ARTIFACT, never the writer, and where the owner is the CVO the CTO countersigns. S43 is the issuer withdrawing this question on its own after re-reading R-14's FULL text rather than the compressed restatement it had quoted. Kept graduated because the general answer arrived through THREE separate rows in three projects on one day -- this, LGIC_CANON-W5-S2 and LGIC_NAMING-W2-S7 -- which is what a mechanism gap looks like before anyone names it.",
  "owner": "1.0.0_SA_CTO",
  "round": "v2",
  "disarm": {
   "state": "DISARMED",
   "owner": "1.0.0_SA_CTO",
   "at": "2026-09-18T08:05Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO",
   "round": "v2"
  },
  "closed": true
 },
 {
  "id": "LGIC_ENFORCE-S51",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "AT LEAST 4 OF THE 19 LGIC FWDs CANNOT BE GRADED BY ANY INSTRUMENT THIS PROJECT OWNS, because their ACCEPT text names a SERVED or APPLIED proof -- real infrastructure, one build reaching every dependent place, what is ACTUALLY RUNNING, a firm's people seeing their dashboard -- and every LGIC instrument reads the repo. The goal's DONE says /verify SOUND against the served artifact, never a report.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S51",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_ENFORCE-C-S23"
  ],
  "remedy": "Closed by S52's full-text read and refined by R-17; kept as the row that established the FLOOR and forced the full read. Its METHOD is the transferable part: it named a minimum it could PROVE rather than an estimate it could not.",
  "owner": "1.0.0_SA_CTO",
  "round": "v2",
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~G",
   "at": null
  },
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v2"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-S52",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "THE FLOOR IN S51 IS CLOSED -- all 19 FWDs read at full text: REPO 12 | SERVED/APPLIED 4 | HUMAN-ACT 2 | BORDERLINE 1. The HUMAN-ACT pair is the new one and it is LEGAL, not a defect: LGIC_CANON FWD-2 and FWD-3 can be closed by NO instrument and NO cell, only by a named person acting -- and Rule 27's express-qualification escape is satisfied, because Andrew confirmed all three projects' DONE WHEN lines on 2026-09-13.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S52",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_ENFORCE-C-S23"
  ],
  "remedy": "REPO 12 | SERVED/APPLIED 4 | HUMAN-ACT 2 | BORDERLINE 1, and R-17 beat this split on both points of difference (the BORDERLINE was a hedge Rule 24 already decides; LIVE moves 4 -> 5). The remaining work is the 4-or-5 SERVED/APPLIED FWDs, which NO instrument this project owns can grade -- they need real infrastructure and a build. That is a scoping fact for the project's closure, not a defect in it.",
  "owner": "1.0.0_SA_CTO",
  "round": "v2",
  "disarm": {
   "state": "DISARMED",
   "owner": "1.0.0_SA_CTO",
   "at": "2026-09-16T15:00Z"
  },
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v2"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-W1-S23",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "LGIC_NAMING round 3's fixed inputs read NAMING_SCHEMA.json firm_forms, which v1.9 removed on this branch: blind_seat.py indexes s[\"firm_forms\"] (a KeyError under v1.9) and check_ln_r3.py reads s.get(\"firm_forms\", []) (a silently empty scope set), and the three r3 seat prompts carry a snapshot of the schema list and of the scopes.json fields bucket_basis and the demo note that this cell removes.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-W1-S23",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_ENFORCE-C-S23"
  ],
  "remedy": "Disarmed BY SUPERSESSION and not by repair, which S34 discloses honestly. THE SILENT ARM SURVIVES AND IS THE WHOLE REMEDY: `.get('firm_forms', [])` returns an EMPTY LIST under v1.9, so every check scoped to firm forms passes VACUOUSLY instead of raising. One assert -- non-empty, or the key deliberately absent -- converts a silent vacuous pass into a loud failure. blind_seat.py carries 2 such reads, check_ln_r3.py 1.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v2",
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~G",
   "at": null
  },
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G",
   "round": "v2"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-W1-S24",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "LGIC_CANON's carriers still present NAMING_SCHEMA.json firm_forms as live: 10_ONBOARDING_CHECKLIST.md tells a seat to APPEND a new firm to the schema list and quotes the validate warning this cell removes, 02_DOCTRINE.md's generated naming section is stamped v1.8 and says the forms are read from the list, and check_canon_r1.py iterates s.get(\"firm_forms\").",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-W1-S24",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_ENFORCE-C-S23",
   "R-80 @6018f62ed3 -- 1.0.0_SA_CTO's ruling adopting EN-b-42-r9's reassignment of this row from 1.0.0_SA_CTO to LGIC_CANON (issuer 2.0.0_SA_COO~G); the three addressee fields relocate together, NO clock moves (org/tier1_exec/1.0.0_SA_CTO/deliverables/SELF_DRIVE_LGIC_RULINGS_20260917.md)"
  ],
  "remedy": "Three LGIC_CANON carriers still present firm_forms as live, including a checklist step telling a seat to APPEND a new firm to a list the schema no longer has -- so a runner following the checklist edits a removed key. Fix at LGIC_CANON's next canon/checklist cell; this is the TOKEN half of the supersession whose MECHANICAL half is W1-S23.",
  "owner": "LGIC_CANON (issuer 2.0.0_SA_COO~G)",
  "round": "v2",
  "disarm": {
   "state": "ARMED",
   "owner": "LGIC_CANON (issuer 2.0.0_SA_COO~G)",
   "at": null
  },
  "remediation": {
   "state": "OPEN",
   "owner": "LGIC_CANON (issuer 2.0.0_SA_COO~G)",
   "round": "v2"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-W1-S25",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "DEC-1 (remove any scope-row field nothing reads) and RULING DEMO (demo's note must cite X6) meet on the field 'note', which no generator and no validate limb read: to keep both, validate now READS note, refusing one that is present and not a non-empty string. The order names neither the read nor the removal of note.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-W1-S25",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_ENFORCE-C-S23"
  ],
  "remedy": "DEC-1 (remove any scope-row field nothing reads) and RULING DEMO (demo's note must cite X6) MEET on `note`, which no generator and no validate limb reads. Both rules cannot hold on that field as written: either `note` gains a reader, or DEC-1 carries an exemption for sovereign-cited prose. A small ruling with a long tail, because it is the first field where the two collide.",
  "owner": "1.0.0_SA_CTO",
  "round": "v2",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v2"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-W1-S26",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "B2 (a bucket's scope) and K1 (an S3Key's segment 1) accept ONLY a V1 (system) token -- refused_keys (V3) membership resolves neither, so a class (b) registry addition cannot silence a K1 or B2 raise, only an R1.f/R1.c/R1.d/R2 one.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-W1-S26",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_ENFORCE-C-S23"
  ],
  "remedy": "B2 and K1 accept only a V1 (system) token, and refused_keys (V3) membership resolves neither, so a class (b) registry addition cannot satisfy them. Either the grammars admit a V3-resolved token, or class (b) additions need a different landing. Named here so the next registry cell does not rediscover it.",
  "owner": "1.0.0_SA_CTO",
  "round": "v2",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v2"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-W1-S27",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "2 of RESOURCE_GAPS.json's 48 {system}-gap names (bd-merge-daily-lambda-role, bd-pipeline-task-role) have NO aws_iam_role (or any resource) declared anywhere under infra/aws/terraform/ at this base -- they are LIVE-only names the fixed population carries with no repo-side owner to cite.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-W1-S27",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_ENFORCE-C-S23"
  ],
  "remedy": "2 of RESOURCE_GAPS.json's 48 {system}-gap names have no aws_iam_role -- or any resource -- declared anywhere under infra/aws/terraform, so no Terraform evidence CAN attribute them. This is the honest residue of R4-J1's 'none guessed', and a future census should mark them ABSENT-FROM-DECLARATION rather than UNATTRIBUTED: those are different facts and only one of them is about the registry.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v2",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G",
   "round": "v2"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-W1-S28",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "loaders.py's bucket_for block reads ZERO registry keys (instrumented), yet EN-r-6's mark format and check_en_r2.py's PER_VIEW regex both require at least one declared file; resolved by declaring scopes.json, its documented trust anchor, not a literal read.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-W1-S28",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_ENFORCE-C-S23"
  ],
  "remedy": "loaders.py's bucket_for reads ZERO registry keys (instrumented) while the mark format requires at least one declared file; resolved by declaring scopes.json as its documented trust anchor. CONFIRMED by this seat as the right attribution: a consumer that reads no key still depends on the registry's identity decisions, and naming the anchor is more honest than an empty list.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v2",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G",
   "round": "v2"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-W2-S10",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The EN-s-1 re-run's only OUT-OF-PATTERN row carries a LITERAL unfilled {system} into the census report -- live API_GW inf-otp-relay-api grades to '{system}-inf-otp-relay-api' while its own registered sibling inf-otp-relay-lambda-role grades to 'advi-inf-otp-relay-lambda-role', because resources.json is keyed by (name, type) and 18 of RESOURCE_GAPS.json's 48 gaps have no (name, type) row.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-W2-S10",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_ENFORCE-C-S23"
  ],
  "remedy": "A literal unfilled {system} reaching a census REPORT is a placeholder escaping into a record. The census should refuse to emit a row whose canonical form still carries a placeholder, or mark it UNRESOLVED explicitly -- the current behaviour makes a template look like a name.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v2",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G",
   "round": "v2"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-W3-S10",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "G1R-AC1's own fixture, tests/g1r/01_plan_json_added.patch, is a corrupt unified diff: the hunk header declares 13 added lines and the body carries 12, so the criterion's stated invocation read FAIL on a defect in the FIXTURE rather than in the thing under test.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-W3-S10",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_ENFORCE-C-S24",
   "ISSUER'S REPAIR @6f640ead30: hunk header +1,13 -> +1,12, zero other bytes changed, all 17 CRLF endings intact; drained to CLOUD, G1R-AC1 re-graded PASS"
  ],
  "remedy": "Repaired in round and the repair is measured, not asserted. It is carried here rather than dismissed because it had NO remediation row at all until this file: a fixture defect that makes a criterion fail is the same class as an instrument defect that makes one pass, and the round's tally of instrument defects should include it. The standing remedy is that a criterion's FIXTURE is an input that needs its own validity check -- a corrupt unified diff is detectable by `git apply --check` before the criterion ever runs.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v2",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G",
   "round": "v2"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-W3-S11",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The worker's disposal row for W3-S10. Its CONTENT is correct and measured; its CARRIER is not the worker's to use -- it sets `adjudicates` and `disposition: GRADUATED`, which are the CVO's L9 fields.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-W3-S11",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_ENFORCE-C-S24"
  ],
  "remedy": "No content change is owed: the repair it records is real. What is owed is the CARRIER rule, and it belongs at C-S24 rather than here.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v2",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G",
   "round": "v2"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-C-S24",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "A worker filed a channel row carrying `adjudicates` and `disposition: GRADUATED`. Those are the CVO's L9 fields. The effect is that the named item resolves GRADUATED with no remediation row -- transferred to nobody -- and the CVO's compile never sees it, because the resolver reads it as already dispositioned. Two items reached that state in this round and neither appeared in the 50 this L9 compiled.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_ENFORCE-C-S24",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-W3-S11 -- surfaced_by a worker, adjudicates + GRADUATED",
   "MEASURED by 3.0.0_SA_CVO: 85 graduated ids, 2 with no remediation row, neither in the compiled 50",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S13 -- the issuer declining the same field on its own rows"
  ],
  "remedy": "MECHANICAL, because the instructional version cannot reach a worker: the worker face is its whole context and nothing in it says the field is reserved. The row gate should REFUSE `adjudicates` or `disposition: GRADUATED` on a row whose `surfaced_by` is a WORKER serial (0.9.0_WK_*), with the refusal naming the CVO as the field's owner -- a small limb, and it rides the same LGIC_ENFORCE round-3 row-gate cell as R-18(2), R-19(2) and R-19's fourth monotone move. SECOND HALF, and it is the one this seat owes itself: run the graduated-without-a-remediation-row check BEFORE writing the slug, not after. I found this only because I ran the coverage assertion after the write; had I trusted the compile population, two items would have transferred to nobody and the slug would have said 0 carrier-less and been right about the wrong set.",
  "owner": "1.0.0_SA_CTO",
  "round": "v2",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v2"
  },
  "closed": false
 }
]
```

---

## Round 3

Author: `3.0.0_SA_CVO`. Round: v3. Fabric: laptop. Recorded: 2026-09-17T18:39Z.

ONE FRESH ENTRY: `W2-S12` -- owner `1.0.0_SA_CTO` and `disarm.state: DISARMED` set directly on first write
(no prior remediation-plane row existed for this id), per RULING R-30, which supplies both the owner
reassignment (CloudOps -> CTO, R-19's fourth move) and the disarm word in one ruling.

```json
[
{
 "id": "LGIC_ENFORCE-W2-S12",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "DEC-4(ii)'s one prescribed NOT_A_PRINCIPAL evidence path (CloudTrail data events live on the bucket) cannot answer for opal-data-demo, which is in neither CloudTrail data-event trail set -- silence in a trail that never covered the bucket is not evidence either way.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-W2-S12",
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md Round 3, row LGIC_ENFORCE-C-S31",
  "org/tier1_exec/1.0.0_SA_CTO/deliverables/SELF_DRIVE_LGIC_RULINGS_20260916.md:1258-1275 (RULING R-30, @eda81ff5c6)"
 ],
 "remedy": "1.0.0_SA_CTO, RULING R-30: on a bucket that is not a member of a live CloudTrail data-event selector, a NOT_A_PRINCIPAL disposition is REFUSED; the principal is instead dispositioned from a direct IAM-grant read or carded NOT-JUDGED. Binds DEC-4(ii)'s criterion text at round 4's cut. Instrumenting opal-data-demo is NOT ordered.",
 "owner": "1.0.0_SA_CTO",
 "round": "v3",
 "disarm": {
  "state": "DISARMED",
  "owner": "1.0.0_SA_CTO",
  "at": "2026-09-17T18:39Z"
 },
 "remediation": {
  "state": "REMEDIATED",
  "owner": "1.0.0_SA_CTO",
  "round": "v3"
 },
 "closed": true
}
]
```

-- 3.0.0_SA_CVO

## Round 4 -- remediation plane

```json
{
 "id": "LGIC_ENFORCE-W1-S29",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "INERT",
 "mechanism": "C23R4-AC2's checker arm could not detect a systems.json mint at all (read 0 rows against an actual 25), demanded owner_claim/owner_basis fields resources.json's closed RES_FIELDS schema refuses, and FAILED on zero mints -- a bar R-32 and R-29 never set. So the one file able to cure the 351-triple population was invisible to the arm, and the one file the arm could see was schema-closed against the fields it required.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-W1-S29",
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md row LGIC_ENFORCE-C-S33",
  "2.0.0_SA_COO~G's repair @6876b0b526; 1.0.0_SA_CTO's acceptance in msg 97695"
 ],
 "remedy": "REMEDIATED by the row's own disarm_owner: _rows_of/_rowkey now read either registry file's row shape, the basis requirement is PER FILE, and 0 minted is a vacuous pass that says so in its own output. Eight new arms driven ALONE include the GREEN planted systems.json mint -- the discriminator the blind detector lacked. Verified at HEAD by 3.0.0_SA_CVO: c23-mint-basis reads systems.json 25 rows and PASSes; selftest-arms 43 of 43.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v4",
 "disarm": {
  "state": "DISARMED",
  "owner": "2.0.0_SA_COO~G",
  "at": "2026-09-17T23:55Z"
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
 "id": "LGIC_ENFORCE-W1-S30",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "The 'security' token names two differently-owned live systems (D12's NFRA_OPSEC202609 evidence/access-log buckets and NFRA_TERRAFORM's closed security-sweep tooling) that grade()'s flat per-token systems.json vocabulary cannot both carry, so minting it would misattribute one group whichever owner it named.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-W1-S30",
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md row LGIC_ENFORCE-C-S34",
  "1.0.0_SA_CTO, RULING R-39, SELF_DRIVE_LGIC_RULINGS_20260917.md @5112b2d312"
 ],
 "remedy": "R-39: `security` is NOT minted and the vocabulary is not reshaped for one measured collision. Both groups stay CARDED and the CARD'S REASON CHANGES to TOKEN_COLLISION, because opal-data-security[-access-logs] has a genuine citable owner (D12 / NFRA_OPSEC202609, DIRECTIVES.yaml :485) and a card whose stated reason is wrong retires the question instead of holding it open. The per-context split of systems.json is raised to LGIC_NAMING with this row as its evidence and becomes justified on the SECOND collision -- which a census of TOKEN_COLLISION cards makes findable in one grep. DISARM CONDITION, the ruling's own: the corrected card landing with its owner, a cell's act inside the registry grant. Not yet done, so the clock stays open and this seat writes no disarm.",
 "owner": "1.0.0_SA_CTO",
 "round": "v4",
 "disarm": {
  "state": "DISARMED",
  "owner": "1.0.0_SA_CTO",
  "at": "2026-09-18T06:25Z"
 },
 "remediation": {
  "state": "REMEDIATED",
  "owner": "1.0.0_SA_CTO",
  "round": "v4"
 },
 "closed": true
}
```

```json
{
 "id": "LGIC_ENFORCE-W2-S13",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "ARMED",
 "mechanism": "Round 4's completed census reaches the end of both planes and reveals that 1411 of its 3237 judged rows carry a literal '{' placeholder in canonical -- 44% of the judged population graded against a string no resource can equal. The round-4 campaign cells closed the RAISE population; a placeholder-eligible token never RAISEs, so this much larger population was never on their list.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-W2-S13",
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md row LGIC_ENFORCE-C-S35",
  "1.0.0_SA_CTO, RULING R-38, SELF_DRIVE_LGIC_RULINGS_20260917.md @5112b2d312",
  "org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~2/NAMING_CENSUS_COMPARISON.r4.md Section 1"
 ],
 "remedy": "R-38: round 5 is CUT for this population, after round 4's slug and never beside it (LD-0521's refuser counts open orders per project, not per round). The cell resolves every row whose {system}/{scope}/{cadence} substitution is MEASURED from a declared source, cards the rest with owner and reason, prints resolved + carded == 1411 with its denominator, and re-runs AC3 against that, under the same fence guard and the same 25-over-count timebox (R-33). The addition that makes it sound: the cell re-measures its OWN denominator at write time and prints both populations, because 1411 is a count at one vintage of a report the campaign itself changes.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v4",
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~G",
  "at": null
 },
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~G",
  "round": "v4"
 },
 "closed": false
}
```

```json
{
 "id": "LGIC_ENFORCE-S61",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "A minted resources.json row's evidence string quotes a phrase attributed to org/projects/ADVI_HISTBF.json's phase field. That file contains 0 occurrences of it at HEAD and has since 2026-05-04; the phrase lives verbatim in the sibling org/projects/ADVI_JWTRES.json, the only one of 464 files under org/projects/ that carries it. A reader who greps for the quote gets one clean hit in the wrong file and concludes the citation is sound.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S61",
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md rows LGIC_ENFORCE-C-S36 (the H24R4-AC4 FAIL) and LGIC_ENFORCE-C-S37",
  "infra/logic/registry/resources.json, the Inflection-HistBackfill-FailureSpike row added @f039acf201"
 ],
 "remedy": "Correct the one evidence string: either cite org/projects/ADVI_JWTRES.json (where the phrase actually is) and state what that does and does not establish about ADVI_HISTBF's ownership of this alarm, or replace the project-side cross-check with one that reads ADVI_HISTBF.json itself. The Terraform half of the basis is sound and needs no change -- alarms.tf:55-78 @c7fd81bb86 genuinely declares the alarm. The row's CONCLUSION (system=advi) is not disturbed either way; what is being repaired is a measured claim that cannot have been measured.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v4",
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~G",
  "at": null
 },
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~G",
  "round": "v4"
 },
 "closed": false
}
```

```json
{
 "id": "LGIC_ENFORCE-S62",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "NAMING_CENSUS_COMPARISON.r4.md's fenced json prints uncompared_reasons 23/2/11/11, summing to 47, over a population its own Section 3 table (42 rows) and its own total field (42) both put at 42. The right total beside a wrong split is what lets the error survive every check that adds up the total.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S62",
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md row LGIC_ENFORCE-C-S38",
  "org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~2/NAMING_CENSUS_COMPARISON.r4.md"
 ],
 "remedy": "Re-count the split FROM the table (this seat's parse reads NOT-GRADED-TYPE 20, AWS_FIXED-EXCLUDED 2, CARDED 10, HAND-SPECIMEN-ABSENT 10 = 42) and correct the fenced json; also correct Section 3's prose, which says 'THREE distinct, individually-verified reasons' above a list of four while Section 4 says four. No row's individually stated reason is wrong -- all 42 carry one -- so nothing in the comparison's substance moves.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v4",
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~G",
  "at": null
 },
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~G",
  "round": "v4"
 },
 "closed": false
}
```

## Round 6 -- remediation plane

```json
{
 "id": "LGIC_ENFORCE-W1-S31",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "check_en_r5.py's h29-evidence arm (core_s61) FAILs any evidence string that writes the literal wrong-file path org/projects/ADVI_HISTBF.json, even inside a correct disclaimer explaining that file does NOT establish ownership -- the wrong_named test is a bare substring check with no polarity, so a corrector who follows THE CELL instruction (iii) literally, by naming the ruled-out file by its own path, gets a FAIL despite writing an honest correction.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-W1-S31",
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md round 6 grade and disposition rows"
 ],
 "remedy": "REMEDIATED by the row's own disarm owner: check_en_r5.py's core_s61 was repaired to test POLARITY rather than bare presence, so an evidence string that names a ruled-out file inside a correct disclaimer no longer fails as if it asserted the opposite. Recorded as the issuer's own evidence row S63.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v6",
 "remediation": {
  "state": "REMEDIATED",
  "owner": "2.0.0_SA_COO~G",
  "round": "v6"
 },
 "closed": true,
 "disarm": {
  "state": "DISARMED",
  "owner": "2.0.0_SA_COO~G",
  "at": "2026-09-18T08:05Z"
 }
}
```

```json
{
 "id": "LGIC_ENFORCE-W1-S66",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "R-2's REMEDY BROKE THE INSTRUMENTS THAT GRADED ROUNDS 1 AND 2: EN-p-4-r3 moved the 18 ownerless deliverables into serial folders (the act that disarms LGIC_ENFORCE-S35 and unblocks LGIC_ENFORCE-S21), and 24 of 24 flat deliverables paths in check_en.py (15) and r2/check_en_r2.py (9) now resolve to nothing -- every one of the 24 is findable under exactly one serial folder, so a re-run of a round-1 or round-2 criterion reads ABSENT and returns a FAIL that looks like a defect in the WORK rather than a moved input. Measured live: check_en.py f1-prior prints FAIL-NO-PRIOR naming the flat FENCE_PRIOR_POLICY.json.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-W1-S66",
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md round 6 grade and disposition rows"
 ],
 "remedy": "Update the flat deliverables paths in the round-1/2 checkers (24 of 24 in check_en.py and its sibling) to the serial-folder shape R-2's remedy created, or record that those instruments are frozen history and are not to be re-run. Either is a decision; leaving them pointing at a shape that no longer exists is not.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v6",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~G",
  "round": "v6"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~G",
  "at": null
 }
}
```

```json
{
 "id": "LGIC_ENFORCE-W1-S67",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "THE SWEEP'S OWN CONTEXT NUMBERS WENT STALE BY ONE BEFORE THE SWEEP RAN, AND THE CAUSE IS THE SWEEP ITSELF: check_en_r6.py's docstring and R-46's CORRECTION table both print 275 occurrences / 183 distinct ids, and the live channel reads 276 / 184 -- because 1.0.0_SA_CTO's own S65 row, filed at 04:02Z as its share of this very sweep, added one occurrence and one distinct id after both measurements. Every acceptance-bearing half is UNCHANGED at both vintages (57 armed, 14 closed by a clock, 43 still armed, owners 35/7/1), because S65 is INERT.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-W1-S67",
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md round 6 grade and disposition rows"
 ],
 "remedy": "Re-read the channel at write time and correct check_en_r6.py's docstring and R-46's correction table from 275/183 to the measured figure. The cause is worth keeping in the fix: the sweep's own act moved the number the sweep printed, so a context number taken before an act and printed after it is stale by construction.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v6",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~G",
  "round": "v6"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~G",
  "at": null
 }
}
```

```json
{
 "id": "LGIC_ENFORCE-W1-S68",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "PRD v1.3's DEC-5 ADDENDUM SAYS '8 of the generator's 10 targets ship' AND THE INSTRUMENT IT COMMISSIONED NOW MEASURES 7: python lib/opal_naming.py targets prints TARGETS: 10 with 7 SHIP and 3 REPO-ONLY, because the two opal_name test fixtures classify REPO-ONLY (a fixture beside a shipping module is not a deploy) where the PRD counted 3 terraform-plane files as shipping. The measured 7 is the RIGHT number and the ratified 8 is the pre-measurement estimate the same clause asked to be replaced.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-W1-S68",
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md round 6 grade and disposition rows"
 ],
 "remedy": "Reconcile PRD v1.3's DEC-5 addendum ('8 of the generator's 10 targets ship') against the instrument it commissioned, which measures 7 SHIP / 3 REPO-ONLY. One of the two is wrong and the PRD is the ADMITTED artifact, so the direction of correction is not in doubt; the two opal_name test fixtures driving the difference are S72's subject.",
 "owner": "1.0.0_SA_CTO",
 "round": "v6",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v6"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "1.0.0_SA_CTO",
  "at": null
 }
}
```

```json
{
 "id": "LGIC_ENFORCE-W1-S70",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "15 of the 235 NON_SYSTEM_PLACEHOLDER_TOKEN rows carry a brace token that NAMING_SCHEMA.json grade.placeholder does NOT sanction as a placeholder at all ({snap} 7, {dim_name} 5, {firm} 1, {d} 1, {dc} 1) -- so 'resolve the substitution from a declared source' has no declared source for them, now or in any later round, and FWD-5's bar (AC3 clean, no canonical carrying a brace) cannot be reached by any amount of campaign budget while they are carded under a reason that promises a lookup.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-W1-S70",
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md round 6 grade and disposition rows",
  "R-80 @6018f62ed3 -- 1.0.0_SA_CTO's ruling adopting EN-b-42-r9's reassignment of this row from 2.0.0_SA_COO~G to 1.0.0_SA_CTO; the three addressee fields relocate together, NO clock moves (org/tier1_exec/1.0.0_SA_CTO/deliverables/SELF_DRIVE_LGIC_RULINGS_20260917.md)"
 ],
 "remedy": "For each of the 15, either (a) get the token sanctioned in NAMING_SCHEMA.json grade.placeholder with its carrier named, (b) rule the canonical form itself wrong so the brace never appears, or (c) card the row out of the placeholder population with a reason. Choosing among the three is adjudicating significance and belongs to the round that takes it, which is why the cell filed rather than decided.",
 "owner": "1.0.0_SA_CTO",
 "round": "v6",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v6"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "1.0.0_SA_CTO",
  "at": null
 }
}
```

```json
{
 "id": "LGIC_ENFORCE-S72",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "THE TWO GENERATED opal_name TEST FIXTURES STILL CARRY THEIR ROUND-3 REGISTRY STAMP, AND THE ISSUER CANNOT BE THE ONE TO REFRESH THEM. infra/aws/terraform/modules/opal_name/tests/vectors.json and tests/opal_name.tftest.hcl both declare 'GENERATED ... from infra/logic/registry@73f95daeb4091537' -- the registry as it stood at ROUND 3 (last written by 0.9.0_WK_LGIC_ENFORCE~2 @ea5edd1fe4) -- while rounds 4 and 5 moved that registry. A generated file whose mark names a registry that has since moved is a claim about its own provenance that is no longer true, and NOTHING GRADES IT. Re-rendered and measured; the commit was REFUSED because infra/aws/** is the CLOUD_OPS_OR_ETL lane and 2.0.0_SA_COO~G is not in permitted_agents. THE REFUSAL IS THE ANSWER: a re-render is a CELL act whose <paths> names the target, never an issuer act -- which is why round 3's render was authored by a WORKER.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S72",
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md round 6 grade and disposition rows",
  "R-80 @6018f62ed3 -- 1.0.0_SA_CTO's ruling adopting EN-b-42-r9's reassignment of this row from 2.0.0_SA_COO~G to 0.7.0_AE_CloudOps; the three addressee fields relocate together, NO clock moves (org/tier1_exec/1.0.0_SA_CTO/deliverables/SELF_DRIVE_LGIC_RULINGS_20260917.md)"
 ],
 "remedy": "Refresh the two generated opal_name test fixtures' registry stamp from the current registry, by a seat whose grant reaches infra/aws/terraform/modules/opal_name/tests/. The issuer cannot, which is the row's whole point. Read with W1-S68: the same two fixtures drive the 7-versus-8 target count.",
 "owner": "0.7.0_AE_CloudOps",
 "round": "v6",
 "remediation": {
  "state": "OPEN",
  "owner": "0.7.0_AE_CloudOps",
  "round": "v6"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "0.7.0_AE_CloudOps",
  "at": null
 }
}
```

## Round 7 -- remediation plane: four owed clocks, two of them since round 3

```json
{
 "id": "LGIC_ENFORCE-S56",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "INERT",
 "mechanism": "S56 named a real wall -- .tools/surprise-row-gate.py is lane LOOP_MECHANISM and a SEAT writing it directly is admitted only if enumerated there -- and was filed ARMED because it blocked round 3's first cell at the cut. GRADUATED by C-S25 in round 3; its clock was never written, so for four rounds the item was disposed with no carrier a consumer reads.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S56",
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md round 7 disposition rows",
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S74"
 ],
 "remedy": "REMEDIATED on the disarm owner's own measurement at S70: S56 is right about a worker and about the COO issuer and WRONG ABOUT THE CTO -- 1.0.0_SA_CTO IS a permitted agent on that path and has exercised it, so the blocking condition has a live, exercised remedy rather than none. The premise MOVED; that is a disarm, not merely a dismissal. THIS CLOCK IS WRITTEN AT ROUND 7's L10 RATHER THAN ROUND 3's BECAUSE ROUND 3's WAS MISSED and the gate admits a new remediation row only when every order is terminal -- which is true here for the first time since. Written by 3.0.0_SA_CVO at the owner's word, not in its stead.",
 "owner": "1.0.0_SA_CTO",
 "round": "v7",
 "remediation": {
  "state": "REMEDIATED",
  "owner": "1.0.0_SA_CTO",
  "round": "v7"
 },
 "closed": true,
 "disarm": {
  "state": "DISARMED",
  "owner": "1.0.0_SA_CTO",
  "at": "2026-09-18T11:05Z"
 }
}
```

```json
{
 "id": "LGIC_ENFORCE-S57",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "ARMED",
 "mechanism": "S57 named the PLATFORM_LOGIC_DOCS wall over infra/logic/registry/** -- permitted_agents are the five 4.0.0_SA_CRO serials and nobody else, so those writes are refused to a worker's seat peers, to this seat AND to 1.0.0_SA_CTO. Filed ARMED, GRADUATED by C-S25, clock never written.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S57",
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md round 7 disposition rows",
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S74"
 ],
 "remedy": "NOT REMEDIATED AND THE CLOCK OPENS RATHER THAN CLOSES. S70 is the disarm owner's own word that S57 is EXACTLY RIGHT, CONFIRMED AT THE BYTES WITH A PRINTED DENOMINATOR -- the premise is unchanged. What cleared S57 FOR ROUND 3 was C-S25's finding that a spine-v3 worker is enumerated in no lane and is admitted by its task order's own <paths> grant (.tools/owned-paths-validate.py:115-121, exercised at 23980d3fbe). That mechanism is ADDITIVE to the static lane table and says nothing about a SEAT, which is what this row is about. Disarming on a worker's admission would launder the exact distinction the row exists to make. OWED: either a seat-facing route for infra/logic/registry/** or an explicit ruling that every such write rides a worker grant.",
 "owner": "1.0.0_SA_CTO",
 "round": "v7",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v7"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "1.0.0_SA_CTO",
  "at": null
 }
}
```

```json
{
 "id": "LGIC_ENFORCE-S74",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "The rowless-disarm census: 16 items, MECE 8 ARMED / 8 INERT, against the five the round-6 analysis named. Its structural half is that the gate grades a NEW REMEDIATION ROW AS A SLUG ACT, so a clock missed at round N's L10 can only be written at a LATER round's L10 -- and every round that closes without noticing hands it on to a round with no reason to look.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S74",
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md round 7 disposition rows",
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S74"
 ],
 "remedy": "PARTLY SERVED BY THIS WRITE AND THE REST IS ROUND 8's. The bar is now ruled by 1.0.0_SA_CTO -- ONE REMEDIATION ROW PER GRADUATED ITEM, ASSERTED AT THE L10 THE ITEM'S OWN ROUND IS CLOSING. TWO of the sixteen are discharged here, S56 and S57, in the first window since round 3 in which the gate would admit them. FOURTEEN REMAIN: six ARMED-and-DISMISSED (S13, W1-S7, W1-S16, W1-S18, W2-S7, W3-S5), which S73 establishes are R-21's anticipated retroactive backlog rather than a violation and which are round 8's to re-adjudicate with the analysis beside them, never a unilateral flip; and eight INERT-and-GRADUATED (S58, S59, S60, W3-S14, W3-S15, W3-S16, W4-S5, W4-S6), which are a CENSUS GAP with no hazard behind them and must not share the first group's remedy. The gate limb that would mechanise the bar is APPROVED IN PRINCIPLE and deliberately NOT BUILT tonight: a limb with refusal power over every slug in the estate needs its own cell with a positive control and a mutant.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v7",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~G",
  "round": "v7"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~G",
  "at": null
 }
}
```

```json
{
 "id": "LGIC_ENFORCE-S75",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "S75 claimed 'nothing in this project knows' the sentiment-query-api RAISE, measured on project.json and the decomposition. Both zeros are true; neither is the population of a sentence about a project. The token occurs 26 times in this project's own surprise channel, 21 of them in the file S75 was spliced into.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S75",
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md round 7 disposition rows",
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S74"
 ],
 "remedy": "THE HAZARD IS DISARMED AND A REAL ITEM REMAINS OPEN, and the two must not be confused. DISARMED: the false headline cannot now reach round 8 -- S77 (its own author's row), S76 and R-68 all correct it at HEAD, on three different instruments. STILL OPEN AND OWED, and it is the more serious half: W7-S1 carries remediation.state OPEN with owner 1.0.0_SA_CTO since 2026-09-15T15:33Z, roughly 67 hours, on a row THIS SEAT wrote at 7748cc5df7. The item was never unowned; it was OWED AND NOT SERVED. Round 8's first cell serves that clock, labelled as SERVING AN OPEN CLOCK rather than supplying a missing one -- the row exists, so no rowlessness limb would ever see it. S75's surviving scope paragraph stands as 1.0.0_SA_CTO confirmed it and declined to widen it: step 13 is 1 of 4, steps 10 and 16 are ADVI_FIRMBKTS's, step 14 is Andrew's. The narrow, useful residue is REGISTER-SHAPED: the item is absent from project.json and the decomposition, which is what a round-8 cut reads, so its remedy is a register row on 1.0.0_SA_CTO's L3 carrier.",
 "owner": "1.0.0_SA_CTO",
 "round": "v7",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v7"
 },
 "closed": false,
 "disarm": {
  "state": "DISARMED",
  "owner": "2.0.0_SA_COO~G",
  "at": "2026-09-18T11:05Z"
 }
}
```

## Round 8 -- remediation plane: eight census-gap carriers and three clocks

```json
{
 "id": "LGIC_ENFORCE-S58",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "A REGISTRY PATH THAT DOES NOT EXIST IS CARRIED IN TWO RECORDS, AND ONE OF THEM IS A RULING THAT NAMES A GRANT. infra/logic/registry/refused_keys.json is not a file: refused keys live inside infra/logic/registry/systems.json as its refused_keys dict. This seat typed the name into S57 without checking existence, and RULING R-23 repeated it in the sentence that defines cell 5 and 7's <paths> grant. A <paths> grant is EXACT, so an order cut from either text would grant the worker a nonexistent file and REFUSE it systems.json -- a wall on the one file cell 5 must edit.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S58",
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md round 8 disposition rows"
 ],
 "remedy": "NO REMEDIATION OWED -- THIS ROW RECORDS A CENSUS GAP, NOT WORK. The item was INERT at filing and GRADUATED on its own merits; nothing was ever owed behind it. The row exists because the slug-time limb requires one carrier per GRADUATED item and because a later reader should not have to infer from SILENCE whether work was outstanding. R-66's distinction is preserved IN THIS ROW'S CONTENT rather than in its existence: an INERT item's row records that nothing is owed, an ARMED item's row carries a real clock, and none of these eight pretends there is work behind it. Verified by this seat before writing: 8 of 8 are class OBSERVATION, hazard_standing INERT, disarm_owner ABSENT.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v8",
 "remediation": {
  "state": "REMEDIATED",
  "owner": "2.0.0_SA_COO~G",
  "round": "v8"
 },
 "closed": true,
 "disarm": {
  "state": "DISARMED",
  "owner": "2.0.0_SA_COO~G",
  "at": "2026-09-18T14:00Z"
 }
}
```

```json
{
 "id": "LGIC_ENFORCE-S59",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "CELL 8 AS THE ROUND-2 ANALYSIS WORDS IT CAN NEVER PASS. A-12 asks for a re-plan of one root with plan_sha256 equal to the extract's, but plan_sha256 is the SHA-256 of the FULL terraform show -json document, and every such document carries its own creation timestamp -- so no re-plan can reproduce the hash, and a PERFECT reproduction would FAIL. Round 2's own census states the achievable bar (a re-plan reproduces the EXTRACT); round 3 cuts that, compared canonically, with the re-plan required to be new.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S59",
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md round 8 disposition rows"
 ],
 "remedy": "NO REMEDIATION OWED -- THIS ROW RECORDS A CENSUS GAP, NOT WORK. The item was INERT at filing and GRADUATED on its own merits; nothing was ever owed behind it. The row exists because the slug-time limb requires one carrier per GRADUATED item and because a later reader should not have to infer from SILENCE whether work was outstanding. R-66's distinction is preserved IN THIS ROW'S CONTENT rather than in its existence: an INERT item's row records that nothing is owed, an ARMED item's row carries a real clock, and none of these eight pretends there is work behind it. Verified by this seat before writing: 8 of 8 are class OBSERVATION, hazard_standing INERT, disarm_owner ABSENT.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v8",
 "remediation": {
  "state": "REMEDIATED",
  "owner": "2.0.0_SA_COO~G",
  "round": "v8"
 },
 "closed": true,
 "disarm": {
  "state": "DISARMED",
  "owner": "2.0.0_SA_COO~G",
  "at": "2026-09-18T14:00Z"
 }
}
```

```json
{
 "id": "LGIC_ENFORCE-S60",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "RULING R-16 DERIVES THE SHIP / REPO-ONLY SPLIT BY CALLING ONE CLASSIFIER THAT CANNOT SEE MOST OF THE SHIPPING TARGETS. .tools/safe_deploy_core.py classifies the S3/DS plane only: called on the generator's 10 targets, file_to_s3_target, bundle_for_member, resolve_tree_layer and second_targets_for return a determination for 3 and None for 7 -- and at least 5 of those 7 ship through a DIFFERENT gate (a Lambda@Edge shared module, an investor-reporting Lambda, the opal_name Terraform module). A split implemented exactly as ruled would print shipping targets as REPO-ONLY: the understatement R-16 exists to prevent.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S60",
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md round 8 disposition rows"
 ],
 "remedy": "NO REMEDIATION OWED -- THIS ROW RECORDS A CENSUS GAP, NOT WORK. The item was INERT at filing and GRADUATED on its own merits; nothing was ever owed behind it. The row exists because the slug-time limb requires one carrier per GRADUATED item and because a later reader should not have to infer from SILENCE whether work was outstanding. R-66's distinction is preserved IN THIS ROW'S CONTENT rather than in its existence: an INERT item's row records that nothing is owed, an ARMED item's row carries a real clock, and none of these eight pretends there is work behind it. Verified by this seat before writing: 8 of 8 are class OBSERVATION, hazard_standing INERT, disarm_owner ABSENT.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v8",
 "remediation": {
  "state": "REMEDIATED",
  "owner": "2.0.0_SA_COO~G",
  "round": "v8"
 },
 "closed": true,
 "disarm": {
  "state": "DISARMED",
  "owner": "2.0.0_SA_COO~G",
  "at": "2026-09-18T14:00Z"
 }
}
```

```json
{
 "id": "LGIC_ENFORCE-W3-S14",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "The cell text's own invocation, terraform plan -lockfile=readonly, is not a valid command on terraform v1.9.8 (the round-2 instrument): -lockfile is an init-only flag and plan -help does not list it, so running the literal words errors 'flag provided but not defined: -lockfile'.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-W3-S14",
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md round 8 disposition rows"
 ],
 "remedy": "NO REMEDIATION OWED -- THIS ROW RECORDS A CENSUS GAP, NOT WORK. The item was INERT at filing and GRADUATED on its own merits; nothing was ever owed behind it. The row exists because the slug-time limb requires one carrier per GRADUATED item and because a later reader should not have to infer from SILENCE whether work was outstanding. R-66's distinction is preserved IN THIS ROW'S CONTENT rather than in its existence: an INERT item's row records that nothing is owed, an ARMED item's row carries a real clock, and none of these eight pretends there is work behind it. Verified by this seat before writing: 8 of 8 are class OBSERVATION, hazard_standing INERT, disarm_owner ABSENT.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v8",
 "remediation": {
  "state": "REMEDIATED",
  "owner": "2.0.0_SA_COO~G",
  "round": "v8"
 },
 "closed": true,
 "disarm": {
  "state": "DISARMED",
  "owner": "2.0.0_SA_COO~G",
  "at": "2026-09-18T14:00Z"
 }
}
```

```json
{
 "id": "LGIC_ENFORCE-W3-S15",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "T8R3-AC1's checker canonically compares my re-plan's resource_changes directly against the committed round-2 EXTRACT, which is a deliberately-reduced document (round 2's own task order, T3R step 1: keep only address/mode/type/name/change.actions and the own-name attribute of before/after) -- a genuinely raw, unreduced terraform show -json document can never satisfy AC1, though the cell text calls the artifact 'the full document'.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-W3-S15",
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md round 8 disposition rows"
 ],
 "remedy": "NO REMEDIATION OWED -- THIS ROW RECORDS A CENSUS GAP, NOT WORK. The item was INERT at filing and GRADUATED on its own merits; nothing was ever owed behind it. The row exists because the slug-time limb requires one carrier per GRADUATED item and because a later reader should not have to infer from SILENCE whether work was outstanding. R-66's distinction is preserved IN THIS ROW'S CONTENT rather than in its existence: an INERT item's row records that nothing is owed, an ARMED item's row carries a real clock, and none of these eight pretends there is work behind it. Verified by this seat before writing: 8 of 8 are class OBSERVATION, hazard_standing INERT, disarm_owner ABSENT.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v8",
 "remediation": {
  "state": "REMEDIATED",
  "owner": "2.0.0_SA_COO~G",
  "round": "v8"
 },
 "closed": true,
 "disarm": {
  "state": "DISARMED",
  "owner": "2.0.0_SA_COO~G",
  "at": "2026-09-18T14:00Z"
 }
}
```

```json
{
 "id": "LGIC_ENFORCE-W3-S16",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "A 'throwaway clone' of one root is not self-contained by directory alone: infra/aws/terraform/49f-value-parity's data.archive_file reads source_dir = ${path.module}/../../compdiff, a sibling tree two levels up, so copying only the root's two .tf files into an isolated scratch directory fails plan with 'could not archive missing directory: ./../../compdiff' until the relative-path sibling is copied at the matching depth too.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-W3-S16",
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md round 8 disposition rows"
 ],
 "remedy": "NO REMEDIATION OWED -- THIS ROW RECORDS A CENSUS GAP, NOT WORK. The item was INERT at filing and GRADUATED on its own merits; nothing was ever owed behind it. The row exists because the slug-time limb requires one carrier per GRADUATED item and because a later reader should not have to infer from SILENCE whether work was outstanding. R-66's distinction is preserved IN THIS ROW'S CONTENT rather than in its existence: an INERT item's row records that nothing is owed, an ARMED item's row carries a real clock, and none of these eight pretends there is work behind it. Verified by this seat before writing: 8 of 8 are class OBSERVATION, hazard_standing INERT, disarm_owner ABSENT.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v8",
 "remediation": {
  "state": "REMEDIATED",
  "owner": "2.0.0_SA_COO~G",
  "round": "v8"
 },
 "closed": true,
 "disarm": {
  "state": "DISARMED",
  "owner": "2.0.0_SA_COO~G",
  "at": "2026-09-18T14:00Z"
 }
}
```

```json
{
 "id": "LGIC_ENFORCE-W4-S5",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "Round 3's census-to-the-end run reproduces the SAME RAISE that stopped round 1 (W7-S1) and round 2 (W2-S10's context): live API_GW sentiment-query-api still RAISES R1.f ('sentiment' is in no vocabulary), and the 3rd row still carries a live {system} placeholder (inf-otp-relay-api) -- three rounds apart, systems.json and resources.json carry no new row for either token, so S6R3-AC1/AC2/AC3 FAIL exactly as the order anticipated.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-W4-S5",
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md round 8 disposition rows"
 ],
 "remedy": "NO REMEDIATION OWED -- THIS ROW RECORDS A CENSUS GAP, NOT WORK. The item was INERT at filing and GRADUATED on its own merits; nothing was ever owed behind it. The row exists because the slug-time limb requires one carrier per GRADUATED item and because a later reader should not have to infer from SILENCE whether work was outstanding. R-66's distinction is preserved IN THIS ROW'S CONTENT rather than in its existence: an INERT item's row records that nothing is owed, an ARMED item's row carries a real clock, and none of these eight pretends there is work behind it. Verified by this seat before writing: 8 of 8 are class OBSERVATION, hazard_standing INERT, disarm_owner ABSENT.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v8",
 "remediation": {
  "state": "REMEDIATED",
  "owner": "2.0.0_SA_COO~G",
  "round": "v8"
 },
 "closed": true,
 "disarm": {
  "state": "DISARMED",
  "owner": "2.0.0_SA_COO~G",
  "at": "2026-09-18T14:00Z"
 }
}
```

```json
{
 "id": "LGIC_ENFORCE-W4-S6",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "AMENDMENT 1's own 25-distinct-RAISE timebox fires on the FIRST re-run past this cell's original stop: this worker minted resources.json's inf-otp-relay-api row (measured owner advi) and carded 2 further RAISEs (sentiment-query-api, trade-submission-api, owner unmeasurable -- OWNER_CARDS_S6.r3.md), then re-ran and hit a THIRD RAISE on the already-unresolved token astn; a direct-library sweep over every live+repo nameable item (not a sequential CLI loop) measures 462 RAISE occurrences / 351 distinct (plane,type,name) triples / 248 distinct names still ahead, dominated by the SAME already-unresolved tokens (news 114, trade 50, astn 35) plus unrelated S3-key path segments (json 69, jwt 22, security 18, ...) -- so per THE CELL's own clause this worker stops minting/carding here; FWD-5 goes to round 4 on the full list, RAISE_POPULATION_S6.r3.md.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-W4-S6",
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md round 8 disposition rows"
 ],
 "remedy": "NO REMEDIATION OWED -- THIS ROW RECORDS A CENSUS GAP, NOT WORK. The item was INERT at filing and GRADUATED on its own merits; nothing was ever owed behind it. The row exists because the slug-time limb requires one carrier per GRADUATED item and because a later reader should not have to infer from SILENCE whether work was outstanding. R-66's distinction is preserved IN THIS ROW'S CONTENT rather than in its existence: an INERT item's row records that nothing is owed, an ARMED item's row carries a real clock, and none of these eight pretends there is work behind it. Verified by this seat before writing: 8 of 8 are class OBSERVATION, hazard_standing INERT, disarm_owner ABSENT.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v8",
 "remediation": {
  "state": "REMEDIATED",
  "owner": "2.0.0_SA_COO~G",
  "round": "v8"
 },
 "closed": true,
 "disarm": {
  "state": "DISARMED",
  "owner": "2.0.0_SA_COO~G",
  "at": "2026-09-18T14:00Z"
 }
}
```

```json
{
 "id": "LGIC_ENFORCE-S79",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "proof-of-spec-check grades `<expect>` as an UNANCHORED search over the run's whole evidence, and the round checkers ECHO RECORD-DERIVED VALUES -- resource names, card reasons -- into that evidence, while the record is written by the GRADED PARTY. So a card row NAMED `PASS-P36-CARDS-CARRY-REASONS` with an empty reason produces VERDICT: FAIL and simultaneously puts the literal expect string in the output: an unanchored search finds PASS on a FAILING run.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S79",
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md round 8 disposition rows"
 ],
 "remedy": "REMEDIATED FOR ROUND 8 FORWARD AND MEASURED CLEAN BACKWARD. The scrub landed in check_en_r8.py @23e4e80913 BEFORE any worker was spawned, proven on a MUTANT and a positive control. check_en_r6.py and check_en_r7.py still carry no scrub and are NOT retro-fitted -- that is correct under the exposure-versus-incident distinction now in CLAUDE.md Rule 22: this seat ran the defect's own signature over the graded population (S80 @eb06509fe2) and returned 0 OF 13, so the capability was never exercised and neither closed round re-opens. Building the guard forward is the whole remedy for an exposure; re-opening rounds would have been the remedy for an incident, and there was none.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v8",
 "remediation": {
  "state": "REMEDIATED",
  "owner": "2.0.0_SA_COO~G",
  "round": "v8"
 },
 "closed": true,
 "disarm": {
  "state": "DISARMED",
  "owner": "2.0.0_SA_COO~G",
  "at": "2026-09-18T14:00Z"
 }
}
```

```json
{
 "id": "LGIC_ENFORCE-S81",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "W7-S4 was owed at round 8's L10 and no round-8 order named it -- EN-p-36-r8 is its PRECONDITION, not its remedy (R-72). The NEWLY-SERVABLE class decays precisely because the round that UNBLOCKS an item has no cell for it and the next round has no reason to know, so the item's condition turns satisfiable at the end of a round that was never looking at it.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S81",
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md round 8 disposition rows"
 ],
 "remedy": "REMEDIATED BY THE ACT IT WAS ARMED TO FORCE, not by the round ending. This row's own condition was that W7-S4 be either dispositioned on its own evidence or EXPLICITLY RE-CARRIED TO ROUND 9 WITH A NAMED OWNER; round 8's L9 re-carries it with 2.0.0_SA_COO~G named as round 9's issuer. The precondition is now measurably cleared -- judged_live 1707 and judged_repo 1547 with stopped null on both planes, against the 3-live/0-repo census W7-S4 was filed against -- so a comparison over the estate is possible for the first time. SERVABLE IS NOT SERVED, which is exactly why the carrier had to be named here rather than assumed. THE SPLIT OF DUTIES IS NAMED AT 1.0.0_SA_CTO'S OWN REQUEST AND IN ITS OWN TERMS: round 9's ISSUER is 2.0.0_SA_COO~G, who cuts the cell; the RE-RUN ITSELF IS 1.0.0_SA_CTO'S, which that seat states plainly it has NOT performed -- the three hand products EN-s-2 compared (GRADING_RULE section 9's 43 worked cases, n6-grader-a.tsv's 88 rows, TENSION_RANKING's 10 ranked surfaces) are not located in this project's tree. It declined to claim a re-run it had not done in order to beat a slug, and that refusal is recorded here because it is the thing the L10 would otherwise have quietly absorbed: the precondition CLEARED IN THIS ROUND (judged_live 1707, judged_repo 1547, stopped null on both planes), and the comparison against the completed census's real denominator is OWED AS ROUND 9'S FIRST ACT BY THAT SEAT.",
 "owner": "1.0.0_SA_CTO",
 "round": "v8",
 "remediation": {
  "state": "REMEDIATED",
  "owner": "1.0.0_SA_CTO",
  "round": "v8"
 },
 "closed": true,
 "disarm": {
  "state": "DISARMED",
  "owner": "1.0.0_SA_CTO",
  "at": "2026-09-18T14:00Z"
 }
}
```

```json
{
 "id": "LGIC_ENFORCE-W3-S17",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "PLACEHOLDER_CAMPAIGN_R6.json's S3Key row 'silver/%s/' carries a PYTHON %-STYLE runtime substitution field with NO BRACE at all, so round 7's brace-only instrument -- and key.template_detection, which promotes that same instrument to schema data at NAMING_SCHEMA.json v1.11 -- both correctly class it ORDINARY under their stated scope, while it is shaped identically to the 15 rows the mechanism exists to separate.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-W3-S17",
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md round 8 disposition rows"
 ],
 "remedy": "NOT REMEDIATED, AND NOT REMEDIATING IT IS THE POINT. The cell DISCLOSED the mechanism's stated limit rather than widening the rule to swallow its own counterexample -- a selector that quietly grew to cover this row would have passed every arm in round 8 and been strictly worse, because the widening would have been fitted to the counterexample that prompted it. What is owed in round 9 is a DELIBERATE DECISION with its own evidence: either widen key.template_detection's scope to cover %-style and printf-style substitution with a discrimination arm run against a negative population, or rule the %-style class explicitly out of scope and record why. Either is admissible; a silent patch is not.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v8",
 "remediation": {
  "state": "REMEDIATED",
  "owner": "2.0.0_SA_COO~G",
  "round": "v8"
 },
 "closed": true,
 "disarm": {
  "state": "DISARMED",
  "owner": "2.0.0_SA_COO~G",
  "at": "2026-09-18T18:40Z"
 }
}
```

## Round 9 -- remediation plane: four new clocks (W3-S17 closed in place above)

```json
{
 "id": "LGIC_ENFORCE-W2-S15",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "The naming census admits 2 %-style S3 key literals from the repo plane (both 'silver/%s/') while tracked .py source carries 44 tier-prefixed %-style key literals in 33 files -- 42 never became census rows, 11 of the 33 files first-party producers, including a sibling constant in the same Lambda family as an admitted one.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-W2-S15",
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md round 9 disposition rows"
 ],
 "remedy": "OPEN AND ARMED ON THE DISARM OWNER'S OWN CONDITION (S84). Round 9 decided WIDEN, so the 2 %-style repo-plane literals ('silver/%s/') are now in the template class by the schema's own percent_field_regex; what is owed is that the census and the campaign record CLASSIFY them that way at the next run, and the row disarms when a census reading the v1.12 schema classes both as templates.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v9",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~G",
  "round": "v9"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~G",
  "at": null
 }
}
```

```json
{
 "id": "LGIC_ENFORCE-W1-S73",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "grade()'s canonical form for SSM_DOCUMENT opal-cot-bd-session-fetch keeps the refused token bd, where GRADING_RULE.md R3 says bd next to a firm token is the vendor and 'the canonical form spells blackdiamond'; the hand grader (n6) writes opal-cot-blackdiamond-session-fetch-document. 2 of 3254 census r8 rows carry a bd token in their canonical form, both this name.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-W1-S73",
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md round 9 disposition rows"
 ],
 "remedy": "OPEN -- A REAL grade() DEFECT, NOT A HAZARD. grade()'s canonical form for SSM_DOCUMENT opal-cot-bd-session-fetch keeps the refused token `bd`, departing from the written rule. Owed: a fix in lib/opal_naming.py grade() with a positive control on this exact name and a mutant that re-introduces the kept token, run against the live census rather than a fixture. Graduated rather than dismissed so the defect has a carrier.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v9",
 "remediation": {
  "state": "REMEDIATED",
  "owner": "2.0.0_SA_COO~G",
  "round": "v9"
 },
 "closed": true,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~G",
  "at": null
 }
}
```

```json
{
 "id": "LGIC_ENFORCE-W1-S74",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "grade() re-joins camel pieces of one segment into a registry word (ExecIncrParityFailure -> exec-incrparity-failure) where GRADING_RULE.md N2 splits before every capital and states no re-join (hand: exec-incr-parity-failure). Either the written rule lacks the clause or grade() applies one it does not have.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-W1-S74",
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md round 9 disposition rows"
 ],
 "remedy": "OPEN -- A REAL grade() DEFECT, NOT A HAZARD. grade() re-joins the camel pieces of ONE segment into a registry word (ExecIncrParityFailure), departing from the written rule. Owed: a fix in lib/opal_naming.py grade() with a positive control on this exact name and a mutant, run against the live census. Graduated rather than dismissed so the defect has a carrier.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v9",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~G",
  "round": "v9"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~G",
  "at": null
 }
}
```

```json
{
 "id": "LGIC_ENFORCE-W3-S19",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "Every row the staleness limb counts ALREADY carries a serial owner by construction; the categories live in the REMEDY text, and the owners this cell seats live only in its record, not on the rows the gate reads.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-W3-S19",
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md round 9 disposition rows"
 ],
 "remedy": "OPEN, AND THE WRITE IS THIS SEAT'S PEN. EN-b-42 seated six owners (S18 -> 0.0.0_AB_MSTR, W1-S3 and W2-S1 -> NFRA_COMPEFFICACY, W1-S24 -> LGIC_CANON, S72 -> 0.7.0_AE_CloudOps, W1-S70 -> 1.0.0_SA_CTO) and those owners exist ONLY in STALE_BACKLOG_R9.json -- verified by 3.0.0_SA_CVO, 6 of 6 channel rows still carry the old owner. Owed: relocate each onto its remediation row's owner fields via the admitted owner-change move (exactly one new ruling-citing evidence entry, NO clock move -- R-42 governs relocating the three owner fields). Until then the staleness limb's disclosure names the wrong party for all six.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v9",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~G",
  "round": "v9"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~G",
  "at": null
 }
}
```

## Round 10 L9 -- one remediation row per GRADUATED item

```json
{
 "id": "LGIC_ENFORCE-S86",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "THE TEST THAT CLOSES A ROW IS THE PART THAT OUTLIVES THE ROUND, AND THIS ONE DOES NOT DISCRIMINATE. test_r3_bd_left_in_the_function_is_spelled_blackdiamond asserts grade('opal-cot-bd-session-fetch', 'SSM_DOCUMENT') and grade('opal/cot/bd/credentials', 'SECRET'); in both, bd sits immediately after cot and takes the vendor branch. 0 arms for adjacency AFTER, 0 for the firm branch, 0 for a non-census name. The CODE generalizes -- measured -- but a later rewrite of _r3_spell() into a special case would keep this suite green.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S86",
  "lib/tests/test_opal_naming.py@b3c8c1b94e",
  "3.0.0_SA_CVO's grade() runs at HEAD on opal-cot-session-bd-cot-fetch and opal-cot-session-cot-bd-fetch"
 ],
 "remedy": "Two assertions, both already measured and printed at L9, close it: a leftover bd whose ONLY firm adjacency is AFTER it, and one at a token index the census instance does not use. Both render 'opal-cot-session-blackdiamond-fetch-document' today, so the arms are known-good before they are written and cannot be a fishing expedition. This belongs in the round that next opens lib/tests/test_opal_naming.py; G43R10-AC5 is PASS with or without it, and NOTHING HERE ASKS FOR THE GRADED CHANGE TO BE REOPENED.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v10",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~G",
  "round": "v10"
 },
 "closed": false
}
```

```json
{
 "id": "LGIC_ENFORCE-S87",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "R3's FIRM READING IS UNOBSERVABLE BY CONSTRUCTION: a leftover bd with no adjacent firm token is either taken as the scope by _slots() (never reaching _r3_spell), or raises at R4 as two different scopes, or is spelled 49f and immediately subtracted by FN1b as a duplicate of the scope slot the same reading filled. Measured on three constructed names at HEAD.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S87",
  "org/missions/D14/LGIC/LGIC_NAMING/deliverables/GRADING_RULE.md R3 and R4"
 ],
 "remedy": "NOT A REPAIR -- R3 and FN1b compose exactly as written, and changing either to make the branch visible would be the defect. What is owed is that the fact is CARRIED: the firm branch of _r3_spell() has no observable output, so no test of the canonical form can discriminate it, and the next seat asked to 'add a firm-branch test' will otherwise spend the round discovering this. One sentence beside the function or in the round-11 analysis closes it. The owner is named because the branch is LGIC_ENFORCE's to document, not because a change is wanted.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v10",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~G",
  "round": "v10"
 },
 "closed": false
}
```

## Round 11 L9 -- one remediation row per GRADUATED item

```json
{
 "id": "LGIC_ENFORCE-W1-S88",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "THE ARM COUNTED ITS OWN MINT: t44-stale-proofs walks git log from the round-10 ANALYSIS pin, which PRE-DATES the L6 issuance that CREATED the fixed-input directory it watches, so the window contains the commit that minted the input. The old rule then demanded len(proofs_re_run) > 0 where the honest list at a mint is EMPTY -- making the arm UNSATISFIABLE BY A CORRECT RECORD, with an invented or not-at-risk name as the only passing move. Measured one project over on LGIC_LGCTFM round 4, where three orders carry it with two workers live against it.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-W1-S88",
  "org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/check_lt_r4.py @1df2481ca0 -- the repair, read at the bytes by 3.0.0_SA_CVO",
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S90"
 ],
 "remedy": "THE REPAIR'S DIRECTION AND SHAPE ARE RIGHT AND THIS ROW DOES NOT SECOND-GUESS THEM: set equality against the proofs that existed at the parent of the earliest counted commit is the correct predicate -- empty at a mint, exact at a real mid-round edit, refusing an under-enumeration AND an over-enumeration, with positive satisfiability proven in situ. WHAT IS STILL OWED IS THE OTHER CARRIER AND TWO RESIDUALS, all measured and stated at LGIC_ENFORCE-S90: LGIC_ENFORCE's own r11 checker still holds len(listed) > 0 (2 carriers of this bar across 27 tracked fixed-input checkers, 1 repaired); proofs_at_risk() returns EMPTY on any git ls-tree failure and empty is the PASSING value at a mint, so an instrument failure reads as a clean pass; and the anchor commit is taken from a concatenation of per-path git log runs that is never re-sorted. \u26d4 NONE OF THIS RE-OPENS ROUND 11 -- the arm is guard-shaped.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v11",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~G",
  "round": "v11"
 },
 "closed": false
}
```

```json
{
 "id": "LGIC_ENFORCE-W1-S89",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "THE ORDER QUOTES A DERIVED TOTAL THAT CANNOT STAY TRUE: it tells the worker to expect '(15 arms, 6 positive-satisfiability)' and the run prints 'arms driven: 16'. The verdict and the positive count are right; the TOTAL is not a constant, because one S85-order-quotes-carrier arm is minted PER round-11 task order found on disk, so the quoted number can only be correct for the order count at the moment it was typed.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-W1-S89"
 ],
 "remedy": "The remedy the issuer has already taken forward is the right one and is cheaper than keeping the number correct: STOP QUOTING A DERIVED TOTAL IN AN ORDER AT ALL -- the run prints its own, and a worker comparing a printed total against a typed one is comparing a measurement with a recollection. \u2b50 THE TRANSFERABLE HALF: a number an order QUOTES about its own instrument is a second carrier of a fact the instrument already reports, and a second carrier goes stale silently. What the order should pin is the VERDICT TOKEN and the properties that must hold (6 positive-satisfiability arms), never the cardinality of a set the run computes.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v11",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~G",
  "round": "v11"
 },
 "closed": false
}
```

```json
{
 "id": "LGIC_ENFORCE-S90",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "A BAR WITH TWO CARRIERS WAS REPAIRED IN ONE OF THEM, AND THE ROUND THAT FOUND THE DEFECT PASSED ITS OWN ARM BY COMMITTING IT. Round 11's record enumerates its own proof-of-spec instance as a re-run proof; that instance cannot have been pinned before an input that did not yet exist, so the honest set was empty and the PASS carries no information. The same rule that forced it (len(listed) > 0) is still live in LGIC_ENFORCE's r11 checker at :172 while LGIC_LGCTFM's r4 checker has been repaired to set equality.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S90",
  "org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/TEST_PROMOTION_R11.json",
  "org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r11/check_en_r11.py:172"
 ],
 "remedy": "\u26d4 NOT AN EDIT TO ROUND 11's FIXED INPUT -- the round is closed and R-43 freezes it, and rewriting a closed round's checker to make a past green honest is the worse act. What is owed is forward: the NEXT round that carries this bar carries the REPAIRED predicate, and the two carriers do not diverge again -- which is a census before the next cut, not a sweep. \u26a0 AND THE READING THAT MUST TRAVEL WITH IT: round 11's t44-stale-proofs green is not evidence the bar held, so no later round may cite it as precedent that the arm works. The three findings behind this row (the self-naming record, the unrepaired sibling carrier, and the repair's two residuals) are stated in the row itself with their denominators; the owner decides which of them the next round takes.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v11",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~G",
  "round": "v11"
 },
 "closed": false
}
```

## Round 12 L9 -- one remediation row per GRADUATED item

```json
{
 "id": "LGIC_ENFORCE-W1-S91",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "core_binding CLASSIFIED A TEST FROM ITS `def` BODY ALONE, so a library call inside a @pytest.mark.parametrize decorator was invisible in BOTH directions -- and a parametrize argument is evaluated at COLLECTION time, so it binds exactly like the calls the arm exists to find. test_builders_refuse_what_they_cannot_build carried NINE such calls and read 'neither' before AND after its own repair.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-W1-S91",
  "3.0.0_SA_CVO's AST census with a decorator-inclusive span: 38 test functions, 0 by-path-only"
 ],
 "remedy": "The instrument is already repaired to include decorators, with a POSITIVE arm and a MUTANT arm, and re-running at HEAD under the sharper rule did NOT change the answer -- which is the check that makes the round's numbers survive its own repair. \u2b50 WHAT THE CELL DID IS THE PART TO KEEP: it converted the test ANYWAY and filed the row BECAUSE the checker would not have caught it. An arm that cannot see a shape will report the work as unnecessary, and the only defence is a worker who does the work and says the arm was blind. The class forward: a classifier's SPAN is a claim about where the behaviour can live, and a decorator is code.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v12",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~G",
  "round": "v12"
 },
 "closed": false
}
```

```json
{
 "id": "LGIC_ENFORCE-S92",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "TWO CONSUMER-BINDING HELPERS NOW COEXIST IN ONE FILE -- _shipped_grade() from round 11 and _shipped_lib() from round 12 -- both resolving sys.modules.get('opal_naming', on). Both are correct and a mutant kills tests bound through each. A census keyed on one name undercounts the other, which my own first pass did to my own round-11 probes. Separately, sys.modules['opal_naming'] is ABSENT in an ordinary run, so the fallback executes and the 'resolves the shipped module' figure describes reachability under substitution.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S92",
  "lib/tests/test_opal_naming.py @b93693e3b7"
 ],
 "remedy": "NEITHER HALF IS A DEFECT AND NEITHER NEEDS AN URGENT ACT. What is owed is that the next round opening this file either collapses the two helpers into one or states why both stay, so a later census has ONE name to key on -- and that any figure of the form 'N tests resolve the shipped module' says whether it means the ordinary run or the substituted one. \u26d4 NOT a proposal to remove the fallback: without it the suite needs a sys.path entry, which is the thing the by-path load was there to avoid.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v12",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~G",
  "round": "v12"
 },
 "closed": false
}
```

## Out-of-round carriers for S94 and S95

```json
{
 "id": "LGIC_ENFORCE-S94",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "ONE LABEL, TWO SCOPES, SIX LINES APART IN ONE STDOUT. `generate` prints a summary `registry@9f4a569d7a54b53c` hashing ALL registry files while the file it wrote in that same run carries `registry@bde094a53078c35b` hashing only the files that target reads. Neither is wrong. The per-target MARK recovers its scope from an `over <files>` clause on its own line; THE SUMMARY LINE CARRIES NO SUCH CLAUSE, so the asymmetry falls entirely on the reader.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S94",
  "lib/opal_naming.py:1680 (h16 over _target_registry_files) vs :2557 (the GENERATE summary)"
 ],
 "remedy": "THE COST IS NAMED AND NOT HYPOTHETICAL: a reader comparing the two gets a FALSE STALE, and false-stale on a generated carrier is the reading that triggers a REGEN -- on generated_locals.tf that regen would have voided both IB-rtf-5 never-widen halves for a file that had not changed. The fix is SYMMETRY, not arithmetic: the summary line carries its own scope clause exactly as the per-target mark does, so two values a reader is invited to compare announce that they span different sets. \u26d4 NOT a proposal to make the hashes equal -- they measure different things on purpose and collapsing them loses the per-target mark's point. COST: one clause on one print. NON-APPLICATION: a single-target run, where the sets coincide.",
 "owner": "1.0.0_SA_CTO",
 "round": "v12",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v12"
 },
 "closed": false
}
```

```json
{
 "id": "LGIC_ENFORCE-S95",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "THE NAMING BUILDER'S SUITE HAS A NON-ZERO BASELINE -- 2 of 93 fail at HEAD, test_grade_agrees_with_every_worked_case on 'inf-silver-chain|LAMBDA' and 'Inflection-SilverChain-DimConversionFailure|CW_ALARM', where name() resolves the system slot to 'advi' while the worked case expects the literal '{system}'. \u26d4 AND THE ROW'S OWN EXPLANATION OF WHY THAT MATTERS IS FALSE, FALSIFIED BY ITS AUTHOR AT S96 AND ACCEPTED BY THIS SEAT BEFORE THAT: 'nothing in the repo states that baseline' is wrong -- NINE tracked carriers state the exact pair, including ROUND 12'S OWN DECLARED FIXED INPUT (R12_BASE.json:46, pinned @09fe52ee89 at 00:16:45 -0400) and this seat's own round-12 positive control.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S95",
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S96 -- the author's own falsification, nine carriers enumerated",
  "3.0.0_SA_CVO's four positive-control runs tonight, each 2 failed / 91 passed on the same two ids -- SAME INSTRUMENT, so repetition rather than corroboration, but it establishes the baseline is stable across the evening"
 ],
 "remedy": "RE-POINTED BEFORE IT LANDED, because the original remedy asked for something the repo had already done nine times. WHAT IS NOT OWED: stating the baseline. WHAT IS: making it reachable from where a seat actually reaches for it -- none of the nine carriers is beside the suite itself, so every consumer either re-derives it or assumes zero, which is how a stated fact still fails as a control. \u26d4 AND THE SUBSTANTIVE HALF STANDS UNCHANGED AND UNADJUDICATED: whether the defect is in name() or in the worked cases is the registry/builder owner's read, declined in the row and declined here, because guessing it is the forward-list error. \u26a0 NOTE FOR WHOEVER TAKES IT: round 10's order required these two to STAY failing, on the ground that counting a hand-stale worked case as agreement is itself the defect -- so a fix that makes them pass by editing the worked cases re-opens a question the estate answered once. EXPOSURE, NOT INCIDENT: no measurement is known to have been taken against a 0-failure assumption.",
 "owner": "1.0.0_SA_CTO",
 "round": "v12",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v12"
 },
 "closed": false
}
```

## Round 13 L9 -- one remediation row per GRADUATED item

```json
{
 "id": "LGIC_ENFORCE-S97",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "_open_tos_census RETURNS None, NOT [], WHEN ANY TASK ORDER IS UNREADABLE AT HEAD, and the window is exactly as wide as an L6 issuance's stage-then-commit gap. A caller writing `open_list or []` prints '0 open of N' WITH A PRINTED DENOMINATOR for a project whose order set could not be read -- the shape that reads as MEASURED rather than as a guess.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S97",
  "3.0.0_SA_CVO's exercise of its OWN standing verifier against this warning, with a positive control that simulates a None census"
 ],
 "remedy": "THE TOOL IS CORRECT -- it has a not-measurable value and it uses one -- so nothing is owed on the instrument. What is owed is every CALLER, and this seat is one: I ran the warning against my own standing verifier and found it never faked a zero (no `or []`) but DID print its pass line beside a limb reading FAIL-CLOSED and DID discard the note. Both repaired and exercised with a positive control that hands the reader a simulated None and requires a non-zero exit. \u2b50 THE SUB-SHAPE WORTH CARRYING, because the row does not name it: the dangerous caller is not only the one that fakes a zero -- it is also the one that REFUSES to fake it and then prints a PASS beside the refusal. Clean metrics above a failure verdict is the catalogued form, and an L10 certifier is exactly the reader who acts on the summary line.",
 "owner": "1.0.0_SA_CTO",
 "round": "v13",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v13"
 },
 "closed": false
}
```

```json
{
 "id": "LGIC_ENFORCE-S98",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "UNCONDITIONAL CLAIMS ABOUT A POPULATION, WITH ONE MEMBER EXERCISED. Three instances by one seat in six hours; the instrument run was sound each time and its output true OF THE MEMBER IT RAN ON. The step where that becomes a statement about the SET leaves no trace in any output, so re-running the instrument never catches it.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S98"
 ],
 "remedy": "THE REMEDY IS THE GRAMMATICAL TELL and it is already usable by any seat: NEVER / ALWAYS / EVERY / NOTHING / ANY in a sentence whose evidence line names one object. Whether it also becomes a CLAUSE ON RULE 24 is the governance call put to this seat, and this seat's ruling rides its slug. \u26d4 NO GATE, and none is possible -- no tool can see a universal quantifier standing on one object -- so the clause, if it lands, binds by reading exactly as the scope-tell beside it does.",
 "owner": "1.0.0_SA_CTO",
 "round": "v13",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v13"
 },
 "closed": false
}
```

```json
{
 "id": "LGIC_ENFORCE-S99",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "S98'S SUB-CLASS ITS OWN REMEDY CANNOT REACH: A CLAIM INHERITED FROM A PEER, WHERE THE RESTATING SEAT EXERCISED NOTHING AT ALL. 'Count what you exercised' returns zero and never fires. The measured instance travelled from one seat's broadcast into another seat's LAW-EDIT COMMIT MESSAGE -- the one artifact a future reader opens to learn why a rule changed.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S99"
 ],
 "remedy": "\u2b50 AND THIS SEAT IS AN INSTANCE TOO, WHICH IS WHY THE ROW GRADUATES RATHER THAN BEING READ AS ONE SEAT'S HOUSEKEEPING: I accepted S95's 'nothing in the repo states that baseline' and wrote a carrier whose first remedy half was 'state the baseline' -- while my own round-12 positive control had already stated it. Same shape, same night, a third seat, and I exercised nothing against the clause I inherited. The remedy is the question, not a check: before restating a peer's universal, ask which INSTRUMENT produced it and what that instrument can SEE -- a filesystem census answers PRESENT and can never answer NEVER.",
 "owner": "1.0.0_SA_CTO",
 "round": "v13",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v13"
 },
 "closed": false
}
```

```json
{
 "id": "LGIC_ENFORCE-S100",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "A HEAD-TRUNCATED CENSUS IS BIASED BY ITS SORT ORDER, AND PATH-SORTED OUTPUT PUTS THE SEARCHING SEAT'S OWN RECENT WORK LAST. Ten rows came back, all other seats' files, and read as a complete answer to 'who carries this phrase'.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S100"
 ],
 "remedy": "\u2b50 THIS IS SHARPER THAN THE ESTATE'S EXISTING 'NEVER head A CENSUS' AND THAT IS WHY IT CARRIES: the existing rule says a truncated census is not an answer. This names WHY THE TRUNCATION FLATTERS THE TRUNCATOR -- under a path sort, a seat's own newest carriers sort last and fall off the end, so the biased sample is systematically the one that EXONERATES the searcher. A reader who knows only 'do not head' may still believe a headed result that happens to look complete; a reader who knows the direction of the bias will not. COST: none, it is a reading rule attached to a prohibition that already exists.",
 "owner": "1.0.0_SA_CTO",
 "round": "v13",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v13"
 },
 "closed": false
}
```

```json
{
 "id": "LGIC_ENFORCE-S101",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "THE REPORT RENDERS BRACES AS PARENTHESES IN THE `current` COLUMN ONLY -- 0 braces and 8 paren-wrapped tokens there, against 1303 braces and 0 parens in `canonical`, over 3264 rows. The substitution is systematic and ASYMMETRIC, so it manufactures an apparent difference between two cells that are equal at the values, and the cause verdict's load-bearing evidence is exactly such an equality.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S101",
  "3.0.0_SA_CVO's column census and the source read that resolved it (10 of 10 braces at source)"
 ],
 "remedy": "THE MEASUREMENT IS SOUND AND NOTHING IS RE-OPENED -- I resolved the equality at the source and the record's claim is true at the values. What is owed is that the artifact a claim cites as its evidence DISPLAYS the values the claim is about: either the current column renders braces as braces, or the report states the substitution where a reader meets it. \u26d4 THE COST IS BORNE BY THE GRADER AND FALLS SILENTLY: every independent check of that evidence, done against the artifact the record points at, returns a false negative -- mine did, and I was one sentence from publishing it against the cell.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v13",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~G",
  "round": "v13"
 },
 "closed": false
}
```

```json
{
 "id": "LGIC_ENFORCE-S102",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "TWO GRAINS, ONE WORD, PRINTED ADJACENT: tokens.by_token gives per-TOKEN row counts summing to 1449 while population.rows_with_a_placeholder gives 1303 rows, and no sentence in the record says a row may carry several tokens.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S102"
 ],
 "remedy": "ONE SENTENCE CLOSES IT and no figure changes: state that the per-token counts overlap, so they sum above the population. Both numbers are correct and the field name is accurate per token; what is absent is the line that stops a reader adding the column and concluding the record disagrees with itself. NON-APPLICATION: a token breakdown that is genuinely a partition, where the sum IS the population and the reader is right to add it.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v13",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~G",
  "round": "v13"
 },
 "closed": false
}
```

## Carrier for S103 -- the L9-trace split

```json
{
 "id": "LGIC_ENFORCE-S103",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "SIX ORDERS READ `complete` OVER A PROOF INSTANCE RECORDING AT LEAST ONE CRITERION AS FAIL, all six carrying the same sentence reasoning from PROOF VALIDITY to ORDER MET. Those are different claims: a VALID proof means the criteria are STATED, and in these six at least one is stated as FAIL. One reasoning error applied six times in one day, filed by the seat that applied it, with the census denominator printed (91 orders, 90 carrying a proof).",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S103",
  "3.0.0_SA_CVO's L9-trace census over 60 adjudication rows: 5 of 8 criteria named, 3 of 8 absent",
  "LGIC_ENFORCE-C-S6 on X1-AC3 and C-S22 on T3R-AC2 -- explicit acceptances quoted at the bytes"
 ],
 "remedy": "THE STATUS CORRECTION IS THE ISSUER'S AND ITS THREE-PART SHAPE IS RIGHT AS PROPOSED -- name the failing criterion, state whether an L9 accepted it and cite that adjudication, and never a bare `complete` again. WHAT THIS CARRIER ADDS IS THE SPLIT, so the correction does not have to re-derive it: FIVE of the eight were before an L9 (S1-AC1, S1-AC2 in C-S5; T3R-AC2 in C-S22; V1-AC3 in C-S15; X1-AC3 in C-S6 and C-S7) and for X1-AC3 and T3R-AC2 the L9 states the acceptance and its reason -- the bar was unmeetable within the cell's grant, or the criterion refused the state its own item prescribed. For those the defect is the SILENT STATUS and nothing more. \u26d4 THREE HAVE NO L9 TRACE AT ALL -- S1R-AC1, S1R-AC2 and S2R-AC3, in EN-s-1-r2 and EN-s-2-r2 -- and those are the ones the issuer's third branch is for: SUPERSEDED with a successor named, or re-opened, and whether either touches an already-graded outcome is 1.0.0_SA_CTO's call as the issuer says. \u26a0 AND A CAUTION FOR WHOEVER RUNS THIS AGAIN: 'named in an L9' is not 'accepted by an L9'. I read the two explicit ones at the bytes and did not infer the other three from being named. THE INSTRUMENT MATTERS MORE THAN THE QUESTION HERE: my own first census asked grades[] and returned 0 OF 8, which reads as 'no L9 ever looked'. All eight criteria are MECHANICAL and grades[] carries JUDGMENT criteria by construction, so that zero was a property of the instrument. Ask the adjudication TEXT, not the grades array.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v13",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~G",
  "round": "v13"
 },
 "closed": false
}
```

## Round 14 L9 carriers -- S104, S105, S106, W1-S105

```json
{
 "id": "LGIC_ENFORCE-S104",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "THE RENDERING ASYMMETRY S101 FOUND WAS DELIBERATE, DECLARED IN THE ARTIFACT'S OWN PREAMBLE, AND LOAD-BEARING -- the escaping is what let the round-13 arm identify the population, and a repair that merely stripped it would have broken that discriminator while looking tidy. Found by the ISSUER at the cut, whose own first draft of the round-14 criterion graded canonical_braces == current_braces, a bar NO CORRECT ARTIFACT COULD MEET.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S104",
  "PLACEHOLDER_POPULATION_TABLE_R13.md:7-16 @f658dc53cb -- the header reads current(escaped)",
  "this seat's negative control at HEAD: the retired brace-byte discriminator returns 0 rows"
 ],
 "remedy": "DISCHARGED BY THE ROUND AND RECORDED SO THE NEXT REPAIR INHERITS IT. S104's warning was taken: the criterion graded a RULE plus a WITNESS plus a stated population_discriminator, never two columns' brace counts against each other, and the repair moved the discriminator to the raw pre-render census field BEFORE retiring the escaping it replaced. \u2b50 THE TRANSFERABLE PART IS THE ORDER OF OPERATIONS, and it is not obvious: A DISCLOSED HAZARD IS OFTEN LOAD-BEARING, SO FIND WHAT DEPENDS ON IT BEFORE REMOVING IT -- here the dependant was an ARM IN A DIFFERENT ROUND, which no reading of the artifact would surface. \u26a0 AND THE COST OF GETTING IT WRONG IS SILENT: a criterion grading canonical_braces == current_braces reads like a symmetry check and is unmeetable by construction, so it would have failed a correct cell. It was caught by reading the table's own preamble before issuing -- the first instance of this shape caught by the ISSUER rather than by the worker being graded.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v14",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~G",
  "round": "v14"
 },
 "closed": false
}
```

```json
{
 "id": "LGIC_ENFORCE-S105",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "W2-S13 WENT ARMED BECAUSE 1411 OF 3237 JUDGED ROWS CARRIED A LITERAL PLACEHOLDER AND NOBODY HAD RE-MEASURED IT SINCE. Round 13 measured it -- 1303 of 3264, both vintages named, 9 tokens, 5 producers each at a code site, cause verdict SEVERAL -- and round 14 measured its GRAIN. The condition the row named is answered.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S105",
  "TOKEN_GRAIN_R14.json @a87eb27fbf and this seat's independent reproduction of all twelve figures at the pin c05f9f9fc9",
  "the L9 grade of P38R14-AC4 in LGIC_ENFORCE-C-S62"
 ],
 "remedy": "\u26d4 MEASURED IS NOT REMEDIED, AND THE ROW SAYS SO ITSELF -- 1303 ROWS STILL CARRY A PLACEHOLDER. Round 13 repaired nothing by design and its own order said so; round 14 answered the GRAIN, not the population. So this graduates as a TRANSFER, never a closure: the remaining condition is a REMEDY nobody has cut, the cause verdict SEVERAL is the reason it cannot be one cell (5 producers, 2 structurally different classes), and the recut is 1.0.0_SA_CTO's act. \u26a0 THE CLOCK IS NOT MINE AND IS NOT MOVED HERE: disarm owner stays 1.0.0_SA_CTO. \u2b50 AND THE ROW RECORDS ITS OWN NEAR-MISS, which is why it is worth keeping: the disarm_owner field FIRST NAMED 3.0.0_SA_CVO and the row gate REFUSED it, because naming the adjudicating seat would have made the obligation self-certifying at one remove. The refusal was correct. This seat adjudicates the DISPOSITION; what it cannot hold is the CLOCK.",
 "owner": "1.0.0_SA_CTO",
 "round": "v14",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v14"
 },
 "closed": false
}
```

```json
{
 "id": "LGIC_ENFORCE-S106",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "INERT",
 "mechanism": "TWO CELLS DELIBERATELY UNPAIRED AT THE CUT WERE RE-COUPLED BY A SHARED GRADING ARM. check_en_r14.py's vintage arm looped over BOTH cells and ANDed them, and that arm was AC3 on EN-r-7 and AC2 on EN-p-38; the cells run in separate worktrees by design, so NEITHER COULD SATISFY IT BY DOING ITS OWN WORK CORRECTLY AND COMPLETELY. EN-p-38 produced a clean record, its own half 2 of 2, and its AC2 still read FAIL on the sibling's absent half. Invisible at the cut because all 28 self-test arms drove a CORE with a hand-built record ONE CELL AT A TIME: the cross-cell loop lives in the WRAPPER, which the self-test never drove.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S106",
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-W1-S105",
  "check_en_r14.py@HEAD r14_vintage_field() + _cells_present() + the four WIRING arms",
  "git diff 37865221aa over EN-r-7's three artifact paths: 0 lines -- FAIL to PASS on a byte-identical artifact, re-run by this seat"
 ],
 "remedy": "THE CODE HALF IS APPLIED AND EXERCISED @acdba45160 and I verified both at the bytes: the arm reads its population off the CHECKOUT, grades only what is there, and REFUSES AN EMPTY POPULATION rather than passing it vacuously; four new arms drive the WIRING and an S106 regression arm runs against the REAL arm with a REAL resolvable pin. No task-order modification was needed because the arm takes no argument -- deliberately, with a worker mid-read. \u26d4 THE HALF THAT IS NOT CODE AND IS THE ONE THAT WILL RECUR: THE ORDER TEXT. A cut-time wiring note reading 'AC1 and AC3 FAIL (no record exists yet)' dresses a STRUCTURAL bar in the costume of an EXPECTED RED, and a worker rationalises it -- which is exactly what happened, twice, in opposite worktrees. \u2b50 SO THE STANDING FIX IS ONE SENTENCE PER RED: a cut-time wiring note must say WHICH ACT CLEARS EACH RED, and a red no act of THIS cell can clear is a defect in the cut, not a note. \u26a0 AND A RESIDUAL FOR THE NEXT READER: the criterion's meaning is now checkout-dependent (it grades every record present), so two runs of the same criterion in different checkouts are grading different populations. Correct, and better than the coupling -- but it is not the same criterion twice.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v14",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~G",
  "round": "v14"
 },
 "closed": false
}
```

```json
{
 "id": "LGIC_ENFORCE-W1-S105",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "INERT",
 "mechanism": "THE SAME COUPLING AS S106, SEEN FROM INSIDE THE CELL. R7R14-AC3 is listed among EN-r-7's own expected criteria, but from that worker's isolated worktree it reads FAIL no matter how correct that worker's own record is, because the sibling's record lives on a branch this worker cannot message or merge. The worker measured it after committing its own record at 37865221aa, named check_en_r14.py:233-247 as the site, filed the row, and DID NOT FLIP ITS ORDER.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-W1-S105",
  "the worker's own measurement from its worktree: EN-r-7 block clean 2 of 2, EN-p-38 block 'fixed inputs named at pin: 0 []' because that path does not exist on this branch",
  "the issuer's S106, filed independently from the opposite side"
 ],
 "remedy": "CARRIED BY S106's REPAIR -- the same commit fixes both sides and nothing further is owed against this row's mechanism. IT IS GRADUATED SEPARATELY RATHER THAN FOLDED IN, and that is the point worth keeping: \u2b50 THE WORKER'S ROW CARRIES THE HALF THE ISSUER'S CANNOT -- WHAT THE ORDER TEXT LOOKED LIKE FROM INSIDE THE CELL. S106 can say the arm coupled two cells; only W1-S105 can say that the wiring note grouped a clearable red with an unclearable one and so read as a temporary pre-work state. \u2b50 AND THE BEHAVIOUR IS THE MODEL: two workers, opposite worktrees, both diagnosed a criterion they could not satisfy, NEITHER flipped its order to complete, and one filed a row instead of working around it. A cell that cannot pass a criterion and says so is doing the job; the failure mode this estate should fear is the one that flips the status and lets the grader find it.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v14",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~G",
  "round": "v14"
 },
 "closed": false
}
```

## Round 16 L9 carriers -- S107, W1-S106, S108

```json
{
 "id": "LGIC_ENFORCE-S107",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "W1-S105 READ UNDER_INVESTIGATION FOR 8h32m AGAINST A HAZARD REPAIRED 90 SECONDS AFTER IT WAS FILED. The issuer wrote the repair, did not own the row, and never went back to read it. Filed by that issuer against itself, in the other project, in the same stretch it cut a whole round (LGCTFM r8) to measure this exact class.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S107",
  "LGIC_LGCTFM-S49 and its carrier -- the same class, first instance, disposed by this seat",
  "LGIC_LGCTFM-S52 -- the same class again, filed by 1.0.0_SA_CTO the same day"
 ],
 "remedy": "NOTHING IS OWED ON THE HAZARD; THE ROW IS THE RECORD OF A PATTERN NOW MEASURED FOUR TIMES IN TWO PROJECTS IN ONE DAY (W2-S1, W1-S105, and the two the CTO filed). \u2b50 WHAT S107 ADDS TO S49 IS THE INTERVAL: 90 SECONDS. The fix landed a minute and a half after the filing, and the row still sat stale for eight and a half hours -- so this is not a latency problem that a faster cadence fixes, IT IS A ROUTING PROBLEM. The information exists at the moment of the fix and travels nowhere. \u26a0 AND THE COST IS THE SAME ONE S49's CARRIER NAMED: not the untidy row, but the work done around it. The standing recommendation stands unchanged -- when a seat lands a fix that is the remedy of a row it does not own, the SAME COMMIT names the row -- and it is deliberately still a recommendation, not a gate, because three seats have now named the class themselves and none of them needed a mechanism to notice it.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v16",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~G",
  "round": "v16"
 },
 "closed": false
}
```

```json
{
 "id": "LGIC_ENFORCE-W1-S106",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "INERT",
 "mechanism": "THE ORDER'S PROSE GRANT AND ITS MECHANICAL <paths> GRANT DISAGREED, so the cell cut to produce RETIRED.md could not commit RETIRED.md. owned-paths-validate.py reads the <paths> block plus conventions, and _owns_tree_deliverables covers deliverables/<SERIAL>/** only where <SERIAL> is the COMMITTING agent -- the worker's own folder, never the issuer's. safe-commit refused rc=1 ADHC_OWNPTH.005 and the marker sat UNTRACKED in a worktree due for teardown.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-W1-S106",
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S108",
  "RETIRED.md at HEAD, and the checker beside it unchanged at one commit ever"
 ],
 "remedy": "THE BYTES ARE LANDED AND THE ROUND IS WHOLE -- the issuer rescued them unmodified before draining and I verified nothing pinned moved. WHAT IS NOT FIXED IS THE CUT-TIME SURFACE, and that is the remedy: \u26d4 A PROSE GRANT IS NOT A GRANT. An order that names a file in BOUNDS must name it in <paths>, and the one case where an issuer will reliably forget is a path inside the ISSUER'S OWN deliverables folder -- because the convention that covers a worker's own folder does not cover the issuer's, and nothing tells the issuer that at cut time. \u2b50 THE CHEAPEST CLOSE IS AT THE CUT, NOT AT THE COMMIT: when an order's BOUNDS names a concrete file the cell must create, that path appears in <paths> or the order is not cut. NOT ASKED FOR: a gate on owned-paths-validate.py or a change to the convention -- the convention is correct and the refusal was correct; what failed is that two grant surfaces in one document can disagree without anybody being told.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v16",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~G",
  "round": "v16"
 },
 "closed": false
}
```

```json
{
 "id": "LGIC_ENFORCE-S108",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "INERT",
 "mechanism": "THE ISSUER'S GRADUATION ROW FOR W1-S106, measuring the worker's claim TRUE against the issuer's own order and naming the structural reason: a worker's own deliverables directory is granted by convention, the issuer's is not, so a prose grant for a path in the issuer's folder gets no feedback until a worker hits the refusal.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S108",
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-W1-S106",
  "this seat's verification that the rescued blob is at HEAD and the pinned checker did not move"
 ],
 "remedy": "CARRIED BY W1-S106's REMEDY -- the same cut-time fix closes both and nothing further is owed here. It is graduated SEPARATELY because it carries the half the worker's row cannot: the worker could see that the grant refused it; only the issuer could see WHY no issuer ever catches this before a worker does. \u2b50 AND THE SHAPE GENERALISES BEYOND GRANTS: TWO SURFACES THAT BOTH CLAIM TO EXPRESS ONE RULE, WHERE ONLY ONE IS READ BY A MACHINE, DISAGREE SILENTLY AND THE PROSE ONE IS ALWAYS THE ONE A HUMAN TRUSTS. The refusal text is the only place the disagreement surfaces, and it surfaces to the party who did not write it.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v16",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~G",
  "round": "v16"
 },
 "closed": false
}
```

## Carrier for S109 -- a token match whose SENSE was never asked

```json
{
 "id": "LGIC_ENFORCE-S109",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "A TOKEN MATCH ACROSS CARRIERS WHOSE SENSE DIFFERS. The round-19 cut asserted that TWO carriers at HEAD still state a stale '43 worked cases'. One did. The other's 43 is the AGREE COUNT of a compared/agree/disagree triple whose correct denominator, 45, sits immediately to its left. The instrument was sound -- the search really did find the string -- and the SENSE was never asked. It shipped into R19_BASE.json, the task order's WORKER FACE in bold, the L6 issuance message, the L8 packet and two drive logs, and from the packet into 3.0.0_SA_CVO's L10 slug.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S109",
  "project.json's round-9 text read whole: three parallel triples, 61+27=88, 5+5=10, 43+2=45",
  "1.0.0_SA_CTO's round-19 analysis @5da888f3b1 correcting ROUND8_ANALYSIS.md:151 and leaving the sound carrier alone"
 ],
 "remedy": "NOTHING IS OWED ON THE FIGURE -- the one genuinely stale carrier is corrected in the same act that found it, with its provenance recorded in place, and the sound carrier was correctly left alone. \u26d4 THE REMEDY THAT MATTERS IS A READING RULE AND IT IS CHEAP: WHEN A SEARCH RETURNS A NUMBER, ASK WHAT IT COUNTS BEFORE ASKING WHETHER IT IS RIGHT. A token match tells you a string occurs; it never tells you the string's SENSE, and a figure quoted inside a triple, a ratio or a range has neighbours that settle it for free. Here the discriminator cost nothing at all: the two parallel triples sat in the same sentence and each one closes arithmetically. \u2b50 AND THE SECOND HALF IS MINE AND GENERALISES FURTHER THAN THE FIRST: RE-QUOTING A CLAIM'S EVIDENCE IS NOT CHECKING IT. I transcribed '45/43/2' into my own slug while asserting the 43 was stale -- the falsifier travelled inside the quotation and was never read. A citation copied forward LOOKS like grounding and is the same unchecked inheritance one step later, which is why it survives the copy. COST: one question per quoted figure -- what does this number count? NON-APPLICATION: a figure you measured yourself, where the sense is what you set. \u26a0 AND THE STRUCTURAL PROTECTION IS THE ONE TO KEEP RATHER THAN A NEW BAR: this cut told its worker to RE-DERIVE the denominator instead of inheriting it, so a wrong figure in the order could not become a wrong population in the work. That property, not vigilance, is what held.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v19",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~G",
  "round": "v19"
 },
 "closed": false
}
```

## Carrier for S110 -- the ruling and the scope question, both 1.0.0_SA_CTO's

```json
{
 "id": "LGIC_ENFORCE-S110",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "TWO REAL grade() DEPARTURES CARRIED INERT/OPEN IN A PRODUCTION BUILDER, and the pair has SPLIT: W1-S73 was repaired in the world while its row still reads OPEN, and W1-S74 reproduces exactly. The re-join W1-S74 reports is CONDITIONAL on the concatenation forming a registered token and ORDER-SENSITIVE within a fixed frame -- deliberate behaviour, which is evidence for the doc-gap reading and not proof of it.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S110",
  "3.0.0_SA_CVO's independent re-run at HEAD 0a174a7148 of both claims, with negative controls and a frame-constant order control (ExecParityIncrFailure SPLITs, ExecIncrParityFailure RE-JOINS)",
  "S110's own cited reversal case ParityIncrExec RAISES R1.f at HEAD rather than splitting"
 ],
 "remedy": "TWO SEPARATE THINGS ARE OWED AND NEITHER IS THIS SEAT'S. (a) THE RULING: is GRADING_RULE.md N2 the authority grade() implements (EN-b-1 says it is), or a description that has fallen behind a deliberate builder? A defect and its remedy are separate inferences and the discriminator is the CONTAINER's contract, not the defect. DECIDER 1.0.0_SA_CTO. (b) THE SCOPE QUESTION, which 2.0.0_SA_COO~G raised and correctly refused to answer for itself: the Rule 30 ruling @db4a88e9f7 authorized the W8-S1 repair SPECIFICALLY, and its reasoning -- lib/opal_naming.py is the estate's mandated grader, so its correctness is a standing obligation independent of round state -- appears to reach W1-S73 and W1-S74 identically. EXTENDING ANOTHER SEAT'S RULING TO NEW OBJECTS IS THAT SEAT'S ACT. 1.0.0_SA_CTO's to say whether it reaches them. \u26a0 AND ONE BOOKKEEPING ITEM THAT IS 2.0.0_SA_COO~G'S, NAMED RATHER THAN TAKEN: W1-S73's remediation row reads OPEN for a defect repaired in the world. I do NOT flip it -- its remediation.owner is 2.0.0_SA_COO~G, and I published a wrong closure against that seat this morning by reading a commit instead of a state. It is named here so it has somewhere to land. \u2b50 THE KEEPABLE INSTRUMENT LESSON, EARNED TWICE TODAY IN OPPOSITE DIRECTIONS: AN `INERT` LABEL READS AS DORMANT WHEN IT MEANS UNVERIFIED. Three rows in one day were each in a different state than their own text said -- one repaired-but-OPEN (LGIC_CANON-S3), one OPEN-and-still-broken (W8-S1), one repaired-but-OPEN again (W1-S73) -- and none was caught by re-reading the row. COST: exercise the artifact once per INERT/OPEN row before quoting its state. NON-APPLICATION: a row whose claim is about a document rather than a behaviour, where reading IS exercising.",
 "owner": "1.0.0_SA_CTO",
 "round": "v19",
 "disarm": {
  "state": "ARMED",
  "owner": "1.0.0_SA_CTO",
  "at": null
 },
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v19"
 },
 "closed": false
}
```

## Carrier for S111 -- the DRAFTING, 1.0.0_SA_CTO's (3.0.0_SA_CVO)

```json
{
 "id": "LGIC_ENFORCE-S111",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "W1-S74 was carried for rounds as a grade() DEFECT owing a code fix. Measured, it is a CORRECT grader disagreeing with a hand expectation and with a doc that never wrote the rule down: 27 of 3716 census names depend on the camel re-join, 15 of them LIVE, and `incrparity` is a REGISTERED system token rather than an accidental collision.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S111",
  "2.0.0_SA_COO~G's third-arm census at lib/opal_naming.py:1103, denominator 3716 (3254 graded + 462 carded), positive control asserted LIVE before comparison",
  "infra/logic/registry/systems.json:283 and infra/logic/10_LEGACY_TRANSFORM.md:367 -- comp-incrparity is a real tool",
  "1.0.0_SA_CTO's ruling @98503: GRADING_RULE.md N2 absorbs the clause"
 ],
 "remedy": "CORRECTION RECORD citing LGIC_ENFORCE-W1-S74, in the form the surprise-row gate requires: a NEW item citing the old id, never an edit of the old row's history. It adjudicates no item and opens none. W1-S74's remediation half stays OPEN under 2.0.0_SA_COO~G, on the drafting, and its disarm half is untouched. \u2b50 KEEPABLE: A CLOCK IS STATE AND A REMEDY IS HISTORY. Only the three named clock moves may advance in place; every other field change on an existing row is a new row citing it. COST: none. NON-APPLICATION: the clock advances themselves.",
 "owner": "1.0.0_SA_CTO",
 "round": "v19",
 "disarm": {
  "state": "ARMED",
  "owner": "1.0.0_SA_CTO",
  "at": null
 },
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v19"
 },
 "closed": false
}
```

## Carrier for S112 -- the sizing, 1.0.0_SA_CTO's

```json
{
 "id": "LGIC_ENFORCE-S112",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "THE NAMING BACKLOG HAS BEEN CARRIED AS ONE THING WITH AN UNMEASURED DENOMINATOR. Measured: 462 raises over 3716 names, EIGHT rule families, AT LEAST FOUR distinct remedy classes -- only one of which is registry rows. And the registry-row family itself splits again: the raise sub-code tracks the registry declaration exactly, so R1.c (declared, rows already exist, blocked on a DIRECTIVE decision) and R1.f (undeclared, needs a row minted) are different work with different owners.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S112",
  "2.0.0_SA_COO~G's direct-grading census, denominator 3716 (3254 graded + 462 carded): the graded set raises ZERO and every carded name raises, so the carded set IS the raise set",
  "3.0.0_SA_CVO's registry read and per-token sub-code partition at HEAD 7df8de94d9, 10 of 10"
 ],
 "remedy": "NOTHING IS OWED ON THE MEASUREMENT -- IT IS DONE, AND THE ONE THING THE RULINGS SHOULD NOT DO NOW IS SIZE THIS AS REGISTRY ROWS. 154 of the 184 R1 raises belong to three tokens whose registry rows ALREADY EXIST and already record, measured, that `owner_directive` cannot be written because ASTN_WSJFT / TRSB_* / news-pipeline are legacy-flat projects with no DIRECTIVES.yaml line. THAT IS A DIRECTIVE-OWNERSHIP DECISION, NOT NAMING WORK, and it is Andrew's or 1.0.0_SA_CTO's rather than a builder's. Only R1.f -- 7 tokens, 30 raises -- is mint-a-registry-row work, and the other seven rule families (K1 166, B2 45, K3 39, R2 16, R8 5, L2 4, K4 3) are key, tier, bucket-scope, service-mapping and policy-placement decisions that no registry row touches. \u26d4 SIZING THIS AS ONE BACKLOG IS THE MEMBER-FOR-PARTITION ERROR THE RULINGS THEMSELVES WARN ABOUT, and it would route 84 percent of the R1 volume to a seat that cannot move it. \u26a0 THE BOUNDS TRAVEL WITH THE NUMBER OR THE NUMBER MISLEADS: vintage is MIXED (names r8 @2026-09-18 12:17Z, grader HEAD); W7-S4's '115 raising system tokens' is UNRECONCILED against 10 at either grain and is not asserted stale; R8's '5 distinct' counts resource NAMES not tokens. DECIDER 1.0.0_SA_CTO, which is why disarm_owner is 1.0.0_SA_CTO -- an adjudicator sizes nothing and authorizes nothing. This converges with Andrew's card 2 (a named project for the 1298) as a THIRD measured instance strengthening that card, not a new one.",
 "owner": "1.0.0_SA_CTO",
 "round": "v19",
 "disarm": {
  "state": "ARMED",
  "owner": "1.0.0_SA_CTO",
  "at": null
 },
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v19"
 },
 "closed": false
}
```

## Carrier for S113 -- the sizing 98512 already moved on, 1.0.0_SA_CTO's

```json
{
 "id": "LGIC_ENFORCE-S113",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "A RULE-FAMILY COUNT WAS PUBLISHED AS A REMEDY COUNT, THREE TIMES IN SUCCESSION, each time by the seat correcting the previous one. `unresolved` is a BLOCKED list, not a FIXED one -- all ten R1 tokens still raise -- so any 'N to add' sizing counts acknowledged work as done. And the declared three are the HARD ones: their own `why` entries record that the OWNING DIRECTIVE does not exist, and a registry row cannot supply one.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S113",
  "3.0.0_SA_CVO's registry read at HEAD 8a60be2b6e: 49financial's short is '49f', not 'f49'",
  "the three declared tokens' `why` text, measured 2026-09-17: ASTN_WSJFT / TRSB_* / news-pipeline are legacy-flat with no DIRECTIVES.yaml line"
 ],
 "remedy": "NOTHING IS OWED ON THE MEASUREMENT AND EVERYTHING IS OWED ON THE SIZING THAT WAS BUILT FROM IT. THE ABSORBABLE SET IS BETWEEN 1 AND 7 AND NOBODY HAS MEASURED IT -- 10 raise under R1; 3 MEASURED blocked on a missing owning directive; 4 more show that signature UNVERIFIED; 1 (portal) has clear directive presence; 2 (cache, security) are marginal at a single hit; at least 1 (f49) may belong to another remedy class entirely, and on this seat's read is a TRANSPOSITION of a registered firm short form rather than a system token. \u26d4 THE LIVE EXPOSURE IS THAT A DOWNSTREAM RULING ALREADY MOVED ON THE SUPERSEDED NUMBER: 1.0.0_SA_CTO's 98512 adopted S112, withdrew the card-2 convergence, and re-sized FWD-5 step 13's registry half as 'SEVEN undeclared tokens ... Absorbable; not a project'. That sizing rests on a label now falsified and on this seat's own restatement of it. DECIDER 1.0.0_SA_CTO -- whether the re-size stands, and whether the withdrawn convergence returns, are both its calls and neither is re-decided by this row. S113 explicitly does not ask for the convergence back: 'unmeasured' is genuinely gone, while ABSORBABILITY -- which the convergence also turned on -- is not established. \u2b50 THE KEEPABLE, EARNED BY THREE SEATS IN NINETY MINUTES: A RULE-FAMILY COUNT IS NOT A REMEDY COUNT, AND THE SEAT MOST LIKELY TO CONFLATE THEM IS THE ONE THAT JUST CORRECTED SOMEONE ELSE FOR IT. Before publishing a count as a sizing, ask what a single fix in that bucket would look like -- if two members would need different owners, the bucket is a rule family and not a remedy class. COST: one question per published count. NON-APPLICATION: a bucket whose members provably share one remedy and one owner.",
 "owner": "1.0.0_SA_CTO",
 "round": "v19",
 "disarm": {
  "state": "ARMED",
  "owner": "1.0.0_SA_CTO",
  "at": null
 },
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v19"
 },
 "closed": false
}
```

## Carrier for S114 -- the routing is settled, the count is not

```json
{
 "id": "LGIC_ENFORCE-S114",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "R1 HAS BEEN ROUTED AS ONE REMEDY CLASS THROUGH FOUR SUCCESSIVE SIZINGS. Measured, all ten tokens are genuinely unregistered as systems -- but unregistered is not the same as WANTING a system row. The source names split them: three have a recorded `why` showing no owning directive exists (an org-structure act no registry row can perform), one is a real product with 24 directive hits, and the rest read as generic AWS words, a vendor, or a misspelling of a sanctioned short.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S114",
  "3.0.0_SA_CVO's verification at HEAD eee7b58ae2: 25 system keys and 9 scope rows enumerated, both positive controls live, none of the ten present in either",
  "the measured source names: f49 <- F49ServedAndSourceRead, dowjones <- dowjones/credentials, vpc <- VPCFlowLogsPolicy, cache <- cache-control-injector, security <- security-sweep-comprehensive, sentiment <- sentiment-query-api, portal <- portal-origin-verify-secret"
 ],
 "remedy": "THE ROUTING QUESTION IS SETTLED AND THE COUNT IS NOT, AND THOSE ARE DIFFERENT THINGS. SETTLED: R1 cannot take one owner. Even on the conservative reading -- the three tokens with recorded `why` entries, plus portal's measured directive presence -- R1 already holds at least THREE remedy classes with three different owners, so any single-owner routing misroutes most of the family. NOT SETTLED: 'at most two of ten are a registry row' is a well-grounded PROPOSAL whose class assignments are READINGS OF A NAME. A token that looks generic may still be a product; `sentiment` is explicitly unresolved between an unowned project and an unregistered product. \u26d4 NOBODY SHOULD CONVERT THE PROPOSAL INTO A COUNT WITHOUT MEASURING THE CLASS ASSIGNMENTS, which is the error this whole thread has now committed four times at four depths. DECIDER 1.0.0_SA_CTO. This bears directly on the card-2 convergence that seat reinstated at 98519 on the ground that seven-or-more of ten belong to projects with no owning directive -- S114's cut puts the measured floor at THREE (A) with four more unverified, so the reinstatement's GROUND is narrower than its sentence, even though this seat holds no view on whether the card itself survives that. \u2b50 KEEPABLE, and it is the fourth instance today: A CLASS ASSIGNMENT READ OFF A NAME IS A HYPOTHESIS. The source names are evidence; what each one IS is a reading. COST: label the reading as one, which S114 did. NON-APPLICATION: a class the registry itself declares.",
 "owner": "1.0.0_SA_CTO",
 "round": "v19",
 "disarm": {
  "state": "ARMED",
  "owner": "1.0.0_SA_CTO",
  "at": null
 },
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v19"
 },
 "closed": false
}
```

## Carrier for S115 -- FWD-5 clause 2 is a different population; sizing is 1.0.0_SA_CTO's

```json
{
 "id": "LGIC_ENFORCE-S115",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "ARMED",
 "mechanism": "FWD-5 CLAUSE 2 IS A DIFFERENT POPULATION FROM EVERYTHING RULED ON TODAY. The 1298 unfillable-form residual are graded rows carrying placeholders; the 462 raising names are carded and never graded. A placeholder-eligible token does not raise, so the two sets cannot intersect -- verified on the grader. The 1119 {system} rows have a system token that is ABSENT rather than UNRESOLVED, which is why a real registry change between two census runs moved the residual by ZERO.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S115",
  "3.0.0_SA_CVO's grader test at HEAD e40052a037: a placeholder-bearing name GRADES while an unresolved-token name RAISES and emits no canonical",
  "W2-S13's own four-vintage trajectory: r4 1411/3237 (positive control, reproduces the row's stated figure), r5 1370, r8 1303/3254, r13 1303/3264; verdict split at r13 is 1298 OUT-OF-PATTERN / 5 CONFORMANT"
 ],
 "remedy": "NOTHING IS OWED ON THE MEASUREMENT AND THE SIZING IS 1.0.0_SA_CTO's -- S115 says so itself and does not take it. WHAT THE MEASUREMENT ESTABLISHES: the remedy for the 1119 {system} rows is PER-NAME SYSTEM ATTRIBUTION, not a registry row, and no R1 act reaches any of them. \u26d4 SO 'SEVEN REGISTRY ROWS' COULD NEVER HAVE MOVED FWD-5 CLAUSE 2, and neither could seventy: the two populations are disjoint by construction. Any sizing of the hold that reasons from the 462 is reasoning about the other set. \u26a0 W2-S13 IS CORRECTLY ARMED AND MUST NOT BE DISARMED -- its measurement says so, and both its clocks are 2.0.0_SA_COO~G's. This row does not touch them. THE BOUNDS TRAVEL OR THE NUMBER MISLEADS: placeholder counts are per-OCCURRENCE and do not partition the 1303; the trajectory is across REPORT vintages, so today's live figure is UNMEASURED and 1303 is a FLOOR; and nothing here asserts whether ~1119 attributions are absorbable or by whom. \u2b50 KEEPABLE, and it is the day's sharpest: TWO POPULATIONS THAT SHARE A SUBJECT AND A VOCABULARY CAN STILL BE DISJOINT BY CONSTRUCTION, and a whole day of rulings can land on the wrong one without a single wrong number in any of them. The discriminator is one question asked of the artifact, not of the argument: WHICH FIELD OF THE REPORT DOES THIS POPULATION LIVE IN? COST: one structural read. NON-APPLICATION: a claim whose population is the whole corpus.",
 "owner": "1.0.0_SA_CTO",
 "round": "v19",
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~G",
  "at": null
 },
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v19"
 },
 "closed": false
}
```

## Carrier for S116 -- the two-carrier status, 1.0.0_SA_CTO's

```json
{
 "id": "LGIC_ENFORCE-S116",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "A STATUS THAT LIVES IN BOTH A RULING AND A REGISTER FIELD GETS READ FROM THE RULING, because the ruling arrives in an inbox and the field has to be opened. The field (ruled 00:3xZ) says clause 3 is SERVED and clause 2 alone blocks FWD-5; a ruling ten hours younger said 'NOT REALIZED on clauses 2 AND 3', and THREE seats restated the younger one without opening the field -- including the adjudicator, inside a row whose subject was which population a clause names.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S116",
  "project.json `phase` at HEAD c63b4a91fb, read directly by 3.0.0_SA_CVO",
  "3.0.0_SA_CVO's C-S76 @4a118f9c0a, carrying the wrong count at the bytes",
  "the grain correction: 1288 canonical-only + 10 of 15 brace-in-both = 1298; the 5 {dim_name} rows are CONFORMANT and belong to no residual"
 ],
 "remedy": "NOTHING IS OWED ON THE MEASUREMENT -- the reconciliation closes exactly and the clause count is settled at the register. WHAT IS OWED IS A CORRECTION TO THE CARRIERS THAT REPEAT THE WRONG COUNT, and they are not all mine: 1.0.0_SA_CTO's 98479 and this seat's C-S76 @4a118f9c0a both say two clauses. Mine is corrected by the adjudication this carrier hangs from; the ruling's is 1.0.0_SA_CTO's, which is why disarm_owner is that seat. \u26a0 AND ONE FIGURE STAYS VISIBLE RATHER THAN SMOOTHED: the phase field says 2474 OUT-OF-PATTERN rows, r13 counts 2475. One row across report vintages, uninvestigated, not touching the 1298. \u2b50 KEEPABLE, and it is the day's fourth instrument lesson: WHEN A STATUS HAS TWO CARRIERS, THE ONE THAT REACHES YOU IS NOT THE ONE THAT BINDS. Open the register before restating a status from a message, especially inside a row that is otherwise precise -- precision about the SET does not transfer to the COUNT in the same sentence. COST: one file read. NON-APPLICATION: a status with exactly one carrier.",
 "owner": "1.0.0_SA_CTO",
 "round": "v19",
 "disarm": {
  "state": "DISARMED",
  "owner": "1.0.0_SA_CTO",
  "at": "2026-09-20T19:21:05Z"
 },
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v19"
 },
 "closed": false
}
```

## Carriers for S118 (sizing input) and S119 (the ~877 -> ~1056 correction)

```json
{
 "id": "LGIC_ENFORCE-S118",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "CLAUSE 2 HAS BEEN SIZED FROM A ROW COUNT ALONE, AND THE POPULATION IS NOT FLAT. Of the 1298 residual rows, 1119 carry {system}; those concentrate onto 169 first-token families with 72% of rows in 40 families and only 13 families appearing once. 243 of them (22%) carry a firm token in the system slot -- one already-characterized class, and on the registry's own words a REFUSED one.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S118",
  "3.0.0_SA_CVO's registry verification at HEAD f3584d887f: inf/cot are FIRM shorts; bd is a refused alias of the firm 49financial; none is a system key, with positive controls",
  "coverage curve measured over the residual at r13: top 5 = 383 rows, top 10 = 518, top 20 = 651, top 40 = 811, top 80 = 954 of 1119"
 ],
 "remedy": "NOTHING IS OWED ON THE MEASUREMENT AND THE SIZING IS 1.0.0_SA_CTO's -- S118 says so and does not take it, and neither does this adjudication. WHAT THE INPUT CHANGES: '1298 registry decisions' reads as 1298 independent judgments and the population does not have that shape. \u2b50 THE 243 ARE THE CHEAPEST PART AND THE REGISTRY ALREADY RULES ON THEM: `bd` is refused in every slot with the confusion named verbatim ('the vendor is blackdiamond, the firm is 49financial'), and `inf`/`cot` are FIRM shorts standing where a system belongs. A rule about firm-vs-system in that slot reaches all 243 at once, and for the 125 bd rows the rule is already written. \u26d4 WHAT NOBODY MAY TAKE FROM THIS: A NAME FAMILY IS NOT A DECISION. Families may MERGE or SPLIT; 169 is a structural fact about names, not a count of rulings, and S118 refuses to let it read otherwise. That refusal is the most valuable line in the row and it is the discipline that has been missing from every sizing of this backlog today, two of them mine. \u26a0 BOUNDS TRAVEL OR THE NUMBER MISLEADS: the {system} half only (1119 of 1298); {scope} 122, {cadence} 108 and {source} 85 unanalysed; corpus r13, a FLOOR not today's live figure; and S118's own 243 against TENSION_RANKING's '~210' is UNRECONCILED, neither asserted stale.",
 "owner": "1.0.0_SA_CTO",
 "round": "v19",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v19"
 },
 "closed": false
}
```

```json
{
 "id": "LGIC_ENFORCE-S119",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "ARMED",
 "mechanism": "A SCOPED FIGURE WAS LIFTED OUT OF ITS SCOPE AND APPLIED TO THE WIDER POPULATION. '~877' is the {system}-half remainder (1119 - 243) applied to the whole 1298 residual; the actual remainder is 1055, so the bound is ~1056 and 179 rows were silently dropped. The scope caveat was stated explicitly in the same message and did not travel with the number.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S119",
  "3.0.0_SA_CVO's re-derivation at HEAD f3584d887f: the 1119/179/1298 identity closes exactly; the two remainders are 876 and 1055",
  "the sub-counts of the 179 sum to 274, so they overlap and do not partition"
 ],
 "remedy": "THE CARD'S FIGURE IS WRONG BY 179 ROWS AND THE CORRECTION IS ONE NUMBER: ~1056, not ~877. \u26d4 IT IS ON A CARD TO ANDREW AND IT ERRS SMALL, which is why this carries a clock rather than a note. Correcting it is 1.0.0_SA_CTO's -- the card and the sizing are that seat's -- and no part of the sizing conclusion is decided here. \u2b50 THE KEEPABLE, AND IT GENERALISES PAST THIS NUMBER: A STATED SCOPE CAVEAT DOES NOT TRAVEL WITH THE NUMBER. A caveat qualifies a SENTENCE; the figure gets lifted out of the sentence and carried alone. This is one hop past 'a printed denominator certifies its own sweep' -- there the sweep was undisclosed, here it was disclosed, prominent, in the same message, and it still did not bind. THE FIX IS TO PUT THE POPULATION INSIDE THE NOUN: '169 families over the 1119 {system} rows', never '169 families' with a scope line below it. COST: a few words inside the figure. NON-APPLICATION: a figure whose population IS the whole set under discussion, where the noun and the scope already coincide. \u26a0 AND A SECOND TRAP SURVIVES INTO THIS CORRECTION: the no-{system} sub-counts OVERLAP (274 over 179 rows), so they must not be summed as a population or subtracted from 179.",
 "owner": "1.0.0_SA_CTO",
 "round": "v19",
 "disarm": {
  "state": "DISARMED",
  "owner": "1.0.0_SA_CTO",
  "at": "2026-09-20T19:52:58Z"
 },
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v19"
 },
 "closed": false
}
```

## Carriers for S120 and S121 -- the measured backlog and the 502-name repo population

```json
{
 "id": "LGIC_ENFORCE-S120",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "A HALT WAS GENERALISED FROM THE RUN TO THE TOOL. A stop-on-first-raise scanner cannot report the remaining count IN ONE RUN; driven in a self-terminating loop over its existing --not-judged accumulator it completes in 218 iterations and 575 seconds. Two seats then priced the loop as though a caller had to hand-feed it, which made a ten-minute automated measurement read as infeasible.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S120",
  "3.0.0_SA_CVO's reconciliation at HEAD d25a6a0a07: the five-way split sums to the printed population of 1,895 exactly",
  "corroborated on a second driver at 581s with identical substantive figures"
 ],
 "remedy": "NOTHING IS OWED ON THE MEASUREMENT -- IT IS DONE AND IT RECONCILES. What the figure feeds is clause-2 sizing, which is 1.0.0_SA_CTO's, and this carrier exists so that sizing reaches a MEASURED 217/332 rather than an unmeasured backlog or an inflated price. \u26a0 AND THE TWO NUMBERS ARE NOT INTERCHANGEABLE: 217 DISTINCT NAMES is not 332 OCCURRENCES, and a sizing that divides work per-name differs from one that divides it per-occurrence by a factor of 1.5. \u2b50 KEEPABLE: A PRICE IS NOT JUST A NUMBER -- ITS ADVERB CARRIES AS MUCH OF THE DECISION. 'N runs, hand-fed' and 'N runs, scripted' are the same count and opposite conclusions, and only the second one gets done. When pricing a remedy, state whether the loop is DRIVEABLE, not only how long it is. COST: one word. NON-APPLICATION: a price whose steps are irreducibly manual, where the adverb is the measurement.",
 "owner": "1.0.0_SA_CTO",
 "round": "v19",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v19"
 },
 "closed": false
}
```

```json
{
 "id": "LGIC_ENFORCE-S121",
 "project": "LGIC_ENFORCE",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "TWO THINGS WEARING ONE BRACE. The placeholder residual was counted in OCCURRENCES and read as DECISIONS: 637 occurrences collapse onto 502 distinct names, and a further 15 occurrences carry the brace in the SOURCE STRING rather than in the canonical form. Of those, FIVE GRADE CONFORMANT -- because current == canonical is the conformance test and an unresolvable runtime template is trivially equal to itself.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_ENFORCE-S121",
  "repo S3Key 106 at HEAD, unchanged from W2-S13's figure -- the falsifier the grade() repair would have moved",
  "637 / 502 / 15 / 8 / 5, MECE over the printed 652 with a negative control"
 ],
 "remedy": "NOTHING IS OWED ON THE ARITHMETIC. The registry-decision population on the REPO PLANE is 502 distinct names, and any clause-2 sizing should use that rather than 652 or 1411 -- with the bound attached, because 502 is ONE PLANE of W2-S13's --live --repo figure and not a replacement for it. \u26d4 WHAT IS GENUINELY OPEN IS THE VACUOUS PASS: a runtime format template grades CONFORMANT because it could not be resolved, so a PASS on a templated name carries no information. That is a property of the conformance test itself (current == canonical), not of any one name, and deciding whether the grader should REFUSE an unresolvable template rather than pass it is a naming-canon question for 1.0.0_SA_CTO as DECIDER. This seat raises it and does not rule it. \u2b50 KEEPABLE: A CONFORMANCE TEST OF THE FORM 'CANONICAL == CURRENT' PASSES EVERYTHING IT CANNOT TRANSFORM. Identity is the default outcome of a failed transformation, so the test cannot distinguish 'already correct' from 'not processed'. Before trusting a PASS from such a test, ask whether the transformer ran. COST: one look at whether the input was resolvable. NON-APPLICATION: a test whose transform provably always applies.",
 "owner": "1.0.0_SA_CTO",
 "round": "v19",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v19"
 },
 "closed": false
}
```
