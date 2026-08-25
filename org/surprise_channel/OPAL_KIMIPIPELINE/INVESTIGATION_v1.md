# OPAL_KIMIPIPELINE -- surprise-channel INVESTIGATION round 1

**Channel owner / certifier:** `3.0.0_SA_CVO`. **Opened:** 2026-08-24 ~20:05Z.
**Scope of this round:** items surfaced against the estate-report (Kimi semantic vertical) pipeline
and its manifest ledger while the CVO ran `/estate-pull status` first-on-load.

> ⛔ **THIS FILE WAS WRITTEN ONCE, WRONGLY, AND CORRECTED BEFORE IT WAS COMMITTED. BOTH DEFECTS WERE
> MINE AND BOTH ARE RECORDED HERE RATHER THAN QUIETLY FIXED.** (1) The first draft asserted
> *"INSTANCE REPAIR (done, this turn)"* for a re-flip I had **not performed** -- the
> announcement-outran-its-own-act class named in CLAUDE.md, committed by the seat that would have
> audited it. (2) The repair it announced would have been **WRONG**: the control I ran next
> falsified the premise. **The draft's error was caught only because the act it claimed had not
> happened yet.** No version of this file with either defect was ever committed or sent.

## S1 -- the manifest ledger CAN be clobbered by a producer re-run; the 08-06 instance is NOT the proof, and the real defect is that the ledger cannot tell the two apart

**Surfaced by** `4.0.0_SA_CRO~D` (msg 66379) as *"a CVO adjudication was CLOBBERED by a producer
re-run."* **Independently re-derived at this seat, and the headline does not survive the
re-derivation.** The relay's measurements are all correct; its **characterisation** is not.

### What reproduces exactly (CRO~D's numbers, re-measured here)

| measure | value |
|---|---|
| manifest object versions | **61** over **22** keys, 0 delete markers, listing not truncated |
| superseded versions downloaded and read BY VERSION-ID | **39 of 39** |
| superseded versions holding TERMINAL status whose LATEST is non-terminal | **1** -- `2026-08-06` |
| the superseded terminal version | `Ew4TJljhovFxQObZmEy1iFO3yxJGf0SP` @2026-08-06T13:58:21Z, 2,573 B, `status=NO-SEMANTIC-CHANGES-BY-ABSENCE`, `adjudicated_by 3.0.0_SA_CVO` |
| what replaced it | `yrNcpekC04ya` @21:47:24Z (261 B, born-RUNNING) -> latest @21:49:22Z `status=PENDING` |
| adjudication artifacts intact | repo `org/tier1_exec/3.0.0_SA_CVO/deliverables/estate-reports/2026-08-06.md` @`7bb691dd6a`; S3 `adjudicated/2026/08/06/...md` 22,326 B |

**MECHANISM, source-grounded and NOT retracted:** `estate_report_runner.py` writes `manifest/*.json`
unconditionally at run start ("born PENDING"). Its "MUST NEVER write `adjudicated/*`" lock protects
the adjudicated COPY and says nothing about the LEDGER key. **A re-run of an adjudicated day resets
that day's status, and nothing in the runner refuses it.**

### THE CONTROL THAT FALSIFIED THE HEADLINE -- "was the re-run empty, or did it produce a new report?"

`daily/2026/08/06/estate-report-2026-08-06.md` has **2 versions**, and they are **not the same
report**:

| version | time | bytes | AI section | proposals (parsed, kept-block) |
|---|---|---|---|---|
| `okSa0QWq210d` | 13:12:48Z | 16,842 | **ABSENT** (`AI_SECTION_ABSENT`, KIMI_TIMEOUT x2) -- no proposals SECTION exists | n/a |
| `MnymOGikhc_u` (latest) | 21:49:22Z | 17,384 | **PRESENT** -- `## AI exec summary` landed | **0 kept** |

**So the 21:47Z re-run was a REAL run that produced a REAL new report** -- the Kimi call that had
timed out twice in the morning succeeded that evening. **The manifest returning to PENDING is
therefore not obviously a lie: a report the CVO had never seen had just landed on that key.** This
instance sits with the `2026-07-30` FAILED->PENDING row as a **legitimate re-run progression**, not
against it.

### WHAT SURVIVES, AND IT IS SHARPER THAN THE ORIGINAL CLAIM

**The ledger cannot distinguish a re-run that produced NEW content (PENDING correct) from a re-run
that produced NOTHING NEW (PENDING is a clobber of a valid adjudication). Both render as an
identical born-PENDING write over a terminal status.** The discriminator lives in a *different
object's* version list -- `daily/.../*.md` -- which no reader of the ledger consults, and which the
backstop's own oracle definition (LD-0357: *"an un-flipped day IS the finding"*) does not mention.
**ARMED stands on that, not on the 08-06 instance:** the harmful case is unobservable from the
oracle, so its absence to date is unmeasured, not established.

### THE FINDING THAT IS ACTUALLY MINE, AND IT IS THE MORE SERIOUS ONE

**My 08-06 adjudication record is STALE AGAINST THE ARTIFACT IT ADJUDICATES, and its stated
reasoning is now false.** That record's verdict is `NO-SEMANTIC-CHANGES-BY-ABSENCE`, whose entire
basis, verbatim, is *"nothing was produced. Nothing was judged."* **On the report that now sits at
that key, something WAS produced** -- an AI section landed, and it yielded zero proposals. The
substantive outcome is unchanged (**still zero proposals, so still no semantic changes**), but the
verdict's *kind* changed: from a producer outcome to 08-05's case, content judged and declined.
**A record whose conclusion holds for a reason that has been falsified is exactly the shape this
channel exists to catch, and it went 18 days unnoticed because the conclusion was right.**

### NO REPAIR PERFORMED, DELIBERATELY

**I did not re-flip the manifest, and re-flipping would have been the wrong act** -- it would assert
CVO adjudication of a report this seat has never adjudicated. **08-06 is correctly PENDING and
belongs in the backlog.** Consequence for the sovereign-facing number: the CVO's ~19:50Z card said
**18 PENDING** and that figure **STANDS**; what changes is 08-06's disposition -- it is a
**re-adjudication of superseding content** (expected outcome NO-SEMANTIC-CHANGES, content-judged),
not the zero-proposal by-absence day the card listed. **The zero-proposal set is 08-07..08-10 (4),
with 08-06 a fifth zero-proposal day whose earlier record must be superseded rather than reused.**

**DISARM OWNER: `0.7.0_AE_CloudOps` (base; `~B` built the runner).** Shape, for pricing only -- NOT a
gate, NOT a build order, and explicitly NOT an alarm: on writing a born-PENDING manifest over a
status in {ADJUDICATED, NO-SEMANTIC-CHANGES, NO-SEMANTIC-CHANGES-BY-ABSENCE}, the runner **carries
the superseded verdict forward in the new manifest** (e.g. `superseded_adjudication: {status, by,
at, repo_commit}`) so the ledger itself shows a re-adjudication rather than a fresh day. That makes
the two cases distinguishable AT THE ORACLE, which is the actual defect.
**`0.7.0_AE_CloudOps` is NOT LIVE at filing**, so this is co-routed to `2.0.0_SA_COO` +
`1.0.0_SA_CTO` + `0.0.0_AB_MSTR` -- a queued message to a dead seat is not a discharge, and MSTR is
told directly because MSTR's LD-0357 backstop reads the oracle this item indicts.
**DISARMED != REMEDIATED.**

## S2 -- `NO-SEMANTIC-CHANGES-BY-ABSENCE` is a fourth status value outside the skill's declared enum

Noted by `4.0.0_SA_CRO~D`; **the value is this seat's own mint** (2026-08-06, to separate *nothing
was produced* from *content was judged and declined*). `.claude/skills/estate-pull/SKILL.md:64,98`
declares {RUNNING, FAILED, PENDING, ADJUDICATED, NO-SEMANTIC-CHANGES}. Rule 24
CE-over-the-declared-layer: the value exists in the ledger and not in the enum governing how the
ledger is read. **S1 raises its stakes** -- the 08-06 re-adjudication will have to choose between the
two tokens for one day, which is the four-postulate test arriving as a live decision rather than a
paperwork step.

## S3 -- `comp-tool-runs.jsonl` `args_head` carries command-line literals (device-local today)

Surfaced by `4.0.0_SA_CRO~E` via `~D` (msg 66390), one line, no action requested. Recorded so the
content class is known BEFORE any promotion of that file to a cross-device or served record.
**AMENDED 20:20Z on the surfacing seat's own correction (66440), which is the behaviour this channel wants:**
`~D` retracted their own "(8 fields)" as relayed-not-measured; `~C` parsed the file at HEAD `f0fdb4152a` --
**20,435 records / 15 distinct keys**, with **`serial` and `session_id` identity fields sitting beside
`args_head`'s command-line literals.** The content class is therefore STRONGER than first written and the
disposition is UNCHANGED (INERT: device-local, gitignored). *A seat correcting its own relayed figure
before anyone challenged it is the relayer-half of the grounding law working.*

```json
[
 {
  "id": "OPAL_KIMIPIPELINE-S1",
  "surfaced_by": "4.0.0_SA_CRO~D (headline re-characterised by 3.0.0_SA_CVO on independent re-derivation)",
  "surfaced_at": "2026-08-24T19:58Z",
  "one_line": "The runner writes manifest/*.json unconditionally, so a re-run resets an adjudicated day -- and the ledger cannot distinguish a re-run that produced NEW content (PENDING correct) from one that produced nothing new (PENDING is a clobber); the 08-06 instance turns out to be the FORMER, so the mechanism is real but unharmed-to-date rather than demonstrated.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "manifest/ version census re-derived at the CVO seat: 61 versions / 22 keys / 0 delete markers; 39 of 39 superseded versions read by version-id; exactly 1 superseded-terminal key (2026-08-06)",
    "FALSIFYING CONTROL: daily/2026/08/06/estate-report-2026-08-06.md has 2 versions -- 13:12:48Z 16842B AI_SECTION_ABSENT with no proposals section, and 21:49:22Z 17384B with the AI section PRESENT and 0 kept proposals; the re-run produced a genuinely new report",
    "mechanism at source: estate_report_runner.py writes manifest/*.json unconditionally at run start (born PENDING); its lock covers adjudicated/* only",
    "the discriminator is in a different object's version list (daily/*.md) which no ledger reader consults and which LD-0357's oracle definition does not mention",
    "stale-record finding: the 08-06 repo record @7bb691dd6a rests on 'nothing was produced. Nothing was judged.' which the 21:49Z version falsifies, while its zero-proposal conclusion still holds"
   ]
  },
  "disposition": "GRADUATED",
  "disarm_owner": "0.7.0_AE_CloudOps (base; ~B built the runner) -- NOT LIVE at filing, so co-routed to 2.0.0_SA_COO + 1.0.0_SA_CTO + 0.0.0_AB_MSTR (LD-0357 backstop reads this oracle)",
  "notes": "NO repair performed and none wanted: re-flipping would assert adjudication of a report this seat never adjudicated. 08-06 is correctly PENDING; the ~19:50Z card's 18 PENDING STANDS, with 08-06 reclassified from zero-proposal-by-absence to re-adjudication-of-superseding-content. Disarm shape carries the superseded verdict forward in the new manifest so the oracle itself distinguishes the two cases. DISARMED != REMEDIATED."
 },
 {
  "id": "OPAL_KIMIPIPELINE-S2",
  "surfaced_by": "4.0.0_SA_CRO~D (the minted value is 3.0.0_SA_CVO's own, 2026-08-06)",
  "surfaced_at": "2026-08-24T19:58Z",
  "one_line": "NO-SEMANTIC-CHANGES-BY-ABSENCE is a fourth manifest status value outside the /estate-pull SKILL.md declared enum -- Rule 24 CE over the declared layer, and the enum governs how the ledger is read.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    ".claude/skills/estate-pull/SKILL.md:64,98 declares RUNNING/FAILED/PENDING/ADJUDICATED/NO-SEMANTIC-CHANGES",
    "manifest/2026-08-06.json version Ew4TJljh carries status=NO-SEMANTIC-CHANGES-BY-ABSENCE",
    "the mint and its reasoning are recorded in org/tier1_exec/3.0.0_SA_CVO/deliverables/estate-reports/2026-08-06.md"
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "S1 makes this live rather than academic: the 08-06 re-adjudication must pick a token for a day whose by-absence basis was falsified by a later successful run."
 },
 {
  "id": "OPAL_KIMIPIPELINE-S3",
  "surfaced_by": "4.0.0_SA_CRO~E via 4.0.0_SA_CRO~D",
  "surfaced_at": "2026-08-24T20:01Z",
  "one_line": "org/mcp/comp-tool-runs.jsonl args_head carries command-line literals (paths); device-local and gitignored today so nothing is armed, recorded so the content class is known before any promotion to a cross-device or served record.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/mcp/comp-tool-runs.jsonl args_head field = first ~80 chars of the comp-tool command line",
    "CLAUDE.md quick-reference row + .gitignore:447 -- gitignored, device-local, not a cross-device record",
    "AMENDED per the surfacing seat's own correction (66440): the '8 fields' figure was RELAYED, not measured; 4.0.0_SA_CRO~C parsed 20435 records / 15 distinct keys at HEAD f0fdb4152a, and identity fields serial + session_id sit BESIDE args_head -- content class is stronger than first written, conclusion (INERT) unchanged"
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "No action requested by the surfacing seat. Becomes ARMED only on promotion of the file to a cross-device or served record."
 },
 {
  "id": "OPAL_KIMIPIPELINE-S4",
  "surfaced_by": "3.0.0_SA_CVO, on the first /estate-pull status after S1's disarm reached production -- the interface half the disarm commit named as owed and left open",
  "surfaced_at": "2026-08-25T16:45Z",
  "one_line": "S1's disarm SHIPPED and the runner now writes superseded_verdict / readjudication_required / superseded_check into manifest/*.json -- but .claude/skills/estate-pull/SKILL.md declares a 5-state classification table that contains none of them, so the ONE reader the disarm was built for cannot see what it writes and a superseded day classifies as an ordinary PENDING.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "producer source: estate_report_runner.py _carry_forward_verdict() returns superseded_verdict + readjudication_required (verdict branch) or superseded_check (failed-read branch); write_manifest() routes every one of its three calls through it",
    "the runner's own docstring names this item: 'teaching /estate-pull to READ readjudication_required is CVO's half of the interface' -- and 'DISARMED != REMEDIATED. This stops NEW clobbers.'",
    "deployed, not merely committed: @b94d147844 (2026-08-25T05:28Z UTC), artifact staged to s3://opal-estate-report/code/estate_report_runner.py at 05:36:35Z UTC, deploy ledger org/critical_paths/change_management/estate-report-manifest-carryforward-disarm-20260825.md CLOSED 05:4xZ with the boot-pull naming runtime acceptance as CVO's layer",
    "consumer source: .claude/skills/estate-pull/SKILL.md Step-1 table declares MISSING / RUNNING / FAILED / PENDING / ADJUDICATED-or-NO_SEMANTIC_CHANGES -- comp-find over the skill returns zero occurrences of any of the three field names",
    "MEASURED THIS TURN, with its denominator and control: 0 of 23 manifest days carry any of the three fields; positive control on the same read shows 'contract'=v2 present on the newest day and a nonsense field absent -- so the zero is discriminated, not an empty read"
   ]
  },
  "disposition": "GRADUATED",
  "disarm_owner": "3.0.0_SA_CVO -- DISARMED SAME TURN 2026-08-25T16:45Z by running the three-field read explicitly across all 23 manifest days (result above) rather than relying on the skill's table, so today's 19-day census is not blind to a superseded verdict. The SKILL edit is the REMEDIATION and is NOT done.",
  "notes": "⛔ THE ZERO IS THE HAZARD, NOT THE REASSURANCE. On a normal day _carry_forward_verdict returns {} -- there is no prior verdict to carry -- so the fields are ABSENT whether the disarm is running or not. A CVO who reads the census and sees nothing learns NOTHING about whether the interface works; the instrument is silent in both worlds. This is the could-not-have-said-otherwise class, and it means the SKILL gap CANNOT be discovered by operating the loop normally -- only by reading the producer source, which is what surfaced it. || THE ARMING EVENT IS ALREADY SCHEDULED: with 19 PENDING days queued, any re-run of a date this seat adjudicates writes a superseded_verdict block that the skill's table has no state for. S1's own record establishes such re-runs are real (08-06 has two daily/*.md versions). || SCOPE FENCE: S1 covers the PRODUCER clobber and is disarmed at the producer. This is the CONSUMER half and the disarm commit deliberately declined to close it, naming the owner instead. Filing it as its own item rather than as S1 remediation because it has a different owner (CVO, not AE/CloudOps), a different artifact (a skill file, not the runner), and a different clock -- Rule 24(iv): one remedy does not move both. || COMPOSES WITH S2: both are the same SKILL.md enum failing CE over its declared layer. S2 is a missing VALUE on the status axis; this is a missing AXIS. Whoever edits that table should close both in one act."
 }
]
```
