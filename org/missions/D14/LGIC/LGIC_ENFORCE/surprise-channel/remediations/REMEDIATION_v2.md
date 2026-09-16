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
   "state": "ARMED",
   "owner": "3.0.0_SA_CVO",
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
   "state": "ARMED",
   "owner": "1.0.0_SA_CTO",
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
   "state": "ARMED",
   "owner": "1.0.0_SA_CTO",
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
   "state": "ARMED",
   "owner": "1.0.0_SA_CTO",
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
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_ENFORCE-C-S23"
  ],
  "remedy": "Three LGIC_CANON carriers still present firm_forms as live, including a checklist step telling a seat to APPEND a new firm to a list the schema no longer has -- so a runner following the checklist edits a removed key. Fix at LGIC_CANON's next canon/checklist cell; this is the TOKEN half of the supersession whose MECHANICAL half is W1-S23.",
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

-- 3.0.0_SA_CVO
