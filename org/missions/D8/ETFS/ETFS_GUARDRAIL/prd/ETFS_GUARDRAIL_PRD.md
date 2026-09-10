# ETFS_GUARDRAIL -- the monthly ETF ownership report cannot go out over data it does not have, and if a hole survives every repair, Andrew is told exactly what is missing

```json
{
 "project": "ETFS_GUARDRAIL",
 "directive": "D8",
 "fabric": "laptop",
 "prd_version": "v0.7",
 "step": 4,
 "brief_ref": "docs/briefs/ETFS_COVERAGE_GUARDRAIL_BUILD_SPEC_20260901.md@1890d7785c",
 "endpoint_outcomes": ["FWD-1", "FWD-3", "FWD-4", "FWD-5", "FWD-6", "FWD-8", "FWD-9", "FWD-10"],
 "status": "RATIFIED"
}
```
*PRD_HEADER block -- schema `org/standards/PRD_HEADER.schema.json`. First fenced block in the file by contract; it is what a monitor and the step-6 gate read. `status: RATIFIED` = step 5 may proceed. The step-6 RED/HOLD that `3.0.0_SA_CVO~A` set @`0d272d257c` was LIFTED by `3.0.0_SA_CVO` 2026-09-02 21:26Z -- RC1-RC7 GREEN, limb 5 GREEN, `org/tier1_exec/3.0.0_SA_CVO/deliverables/CANONICAL_LOOP_RC7_LIMB5_GRADE_AND_HOLD_LIFT_20260902.md`; step 6 proceeds at `2.0.0_SA_COO`'s sequencing.*

**PRD v0.1 (stage 2, purpose-level) -- `1.0.0_SA_CTO` -- 2026-09-02**
**Pipeline position:** step 1 brief (`4.0.0_SA_CRO`, `1890d7785c`) -> step 2 `/endpoint --forward` (`153f59c3ef`) -> **step 3/4 PRD (this document)** -> step 5 `2.0.0_SA_COO` atom-decomp, BEFORE any TO.
**Project code:** `ETFS_GUARDRAIL` -- ratified Andrew-direct 2026-09-02 (*"ETFS_GUARDRAIL is good"*).
**Directive:** **D8** (Model Portfolios Pipeline Fortification) · **fabric: `laptop`** -- Andrew-direct 2026-09-02,
verbatim: *"laptop fabric but this would go under D8 Pipeline Fortification"*. **Not D4**, despite the `ETFS_*`
code: D8's stance names this exact defect class -- *"the staleness is INSIDE THE PAYLOAD ... every object-mtime
freshness instrument reads HEALTHY and is correct about the FILE. That blindness is the condition D8 exists to
end."* D8 is itself LAPTOP-placed, so membership and fabric agree rather than one overriding the other.
**Source brief:** `docs/briefs/ETFS_COVERAGE_GUARDRAIL_BUILD_SPEC_20260901.md` @`1890d7785c` (18,680 bytes, read 299/299).

---

## 0. AUTHORITY -- his words, verbatim

**(1) The original ask, 2026-09-01** (carried in the brief header):
> *"I'd like to be able to have it go out to aj@opalinvest.com via email but I'm hesitant in the event that
> there are holes for whatever reason in backfill. What I'm thinking is maybe we can build in some kind of
> guardrail that checks for holes pre-publishing and if there it it has a remediation process that checks the
> source files, if they are not there it does targeted egress."*
> Then: *"yes do all of the above."*

**(2) The rulings, 2026-09-01**, against `/open-calls` (5 cards):
> *"I agree with the reporting obligation window."*
> *"All recs approved. ALso I want to be on the email as well as aj@opalinvest.com should be him and me at
> andrew@opalinvest.com."*

**(3) The terminal-notification ruling, 2026-09-02** (this terminal, on the step-2 endpoint):
> *"there is one point that is missing however, which i would call FWD-7 and make your 7 entry at 8. There
> needs to be a SES Urgent email that I receive at andrew@opalinvest.com if we are unable to backfill and have
> missing dates in the final output. This email must be a last resort, the backfill strategy must be effective
> enough that it doesnt happen, but if with egress from the usual sources still cannot get the information
> then i need to know. Your Fwd-7 actually can be folded into this because in that email there should be a
> structured report of exactly what dates were missing and from what provider and for what partner."*

### The rulings table (card 3 is an OVERRIDE, not an approval)

| Call | Rec put to him | RULING |
|---|---|---|
| 1 | align three partners onto one date basis before automating the send | **APPROVED.** PREREQUISITE to the send (s.6a of brief). |
| 2 | restate published figures, or forward-only | **APPROVED FORWARD-ONLY.** No restatement, no partner notification. |
| 3 | `aj@` REPLACE or JOIN `andrew@` | **NOT AS RECOMMENDED -- RULED JOIN.** Both addresses. |
| 4 | standing pre-auth for targeted egress | **APPROVED KEEP PER-USE.** Rung 3 stays per-use-authorized. |
| 5 | activate `ETFS_CANON` now | **APPROVED LEAVE AT SCOPING.** Sequenced after this project. |

> **CARD 3 IS THE ONE THAT GETS LOST.** *"All recs approved"* arrived in the same message as a sentence
> contradicting card 3's rec. **The specific instruction governs the general one.** A seat reading only the
> blanket phrase implements REPLACE and silently drops Andrew from the distribution of his own report.

> **A STALE OPEN QUESTION SURVIVES INSIDE THE BRIEF AND IS SUPERSEDED HERE.** Brief s.6a still carries
> *"OPEN -- ANDREW'S CALL: does `aj@` replace `andrew@`... Spec assumes REPLACE"*. That line sits LATER in the
> document than the ruling that answers it. **JOIN governs.** A builder reading the brief top-down would hit
> the ruling first and the stale question second, and the second reads like the live one.

### MORATORIUM CARVE-OUT -- widened 2026-09-02, and the width is stated so it is not inherited

CLAUDE.md carries a standing ban on building **alerts / alarms / SNS / SES-sends / notifications /
freshness-checkers / monitors "unless Andrew explicitly asks."** He asked, twice, in the words above.

```
  AUTHORIZED (2026-09-01)  a coverage PRECONDITION inside the existing render path
                           a catch-up inside the EXISTING producers
  AUTHORIZED (2026-09-02)  ONE SES send, on the TERMINAL FAILURE PATH ONLY  <- NEW, ruling (3)
  STILL BANNED             a new monitor, a new alarm, a new SNS topic, a standing
                           freshness service, or any send on a SCHEDULE rather than
                           on the terminal failure of the ladder
```

> **THE NEW SEND IS NOT A MONITOR AND MUST NOT BECOME ONE.** It has no schedule and no polling loop. It is
> emitted by the remediation ladder when the ladder terminates unresolved -- the same act that already writes
> the refusal. **A send that fires on a timer, or on any condition short of "every rung failed", is outside
> this carve-out.** His own constraint is the governing one: *"This email must be a last resort, the backfill
> strategy must be effective enough that it doesnt happen."*

---

## ENDPOINT (step 2, /endpoint --forward)

Emitted at step 2 from the brief alone, before any task order existed. `FWD-n` ids are **permanent and never
reused**; a retired outcome leaves its number vacant. **FWD-7 was inserted and the prior FWD-7 renumbered to
FWD-8 on Andrew's explicit instruction 2026-09-02, BEFORE this list had ever landed in a PRD and while nothing
cited it** -- which is the only condition under which a renumber is safe.

> ⛔ **"FROZEN" IS A CONTRACT HERE, NOT A CONTROL -- and I wrote "frozen" before I could back it.**
> Measured by `3.0.0_SA_CVO` (msg 92483, 2026-09-02) against its own gate: `.tools/surprise-row-gate.py:53`
> @`c6c3627269` validates an `outcome_ref` with `^FWD-[0-9]+$` -- **it checks the SHAPE of the id and never its
> EXISTENCE.** The permanence rule is asserted in the comment directly above that line (`:51-52`) and is
> **checked by nothing.** A row citing `FWD-9` when no FWD-9 was ever cut PASSES; so does a row citing `FWD-7`
> meaning the PRE-renumber FWD-7, which is exactly the object that no longer exists.
> **Corroborating census, with its denominator and a positive control:** zero surprise-channel rows cite any
> `ETFS_GUARDRAIL` FWD-n (0 hits / 26 files), positive control 29 hits / 144,514 files including this PRD --
> so the renumber broke no live citation. **That census certifies TODAY and does not make the freeze
> enforceable.** No fix is proposed here: existence-checking needs a resolvable per-project FWD-n registry that
> does not exist, and building one on this seat's own judgment would be an agent-made gate Andrew never asked
> for. **Named as the residual so the word "frozen" is not read as a mechanism.**

```
  FWD-1  A day that went missing from the monthly ETF report gets filled in
         on its own, before anyone has to notice it was gone
         DONE WHEN  EXERCISED -- a real missed day has actually been caught up
                    without a person intervening
         ACCEPT     a day the report should have covered but did not gets picked
                    up on its own before the month goes out -- including one
                    where the partner's own data does not reach us until nearly
                    two weeks later
         SOURCE     brief s.3 (81-129), lag table 93-110

  FWD-3  The report states how complete it is, on its own face
         DONE WHEN  APPLIED -- the statement is in the report itself
         ACCEPT     someone reading the report can tell, without asking anyone
                    and without opening anything else, how much of the month it
                    really covers and how much was filled by repeating the
                    previous day
         SOURCE     brief s.4 (155-158)

  FWD-4  A day that is legitimately empty is never "repaired" into a number
         nobody measured
         DONE WHEN  EXERCISED -- the system has actually met such a day and left
                    it alone
         ACCEPT     on a day the market was shut, or a day the partner sent us
                    holdings with no prices attached, nothing is invented and
                    nothing is reported as broken. AMENDED v0.6: "nothing is
                    invented" is measured ON THE SLICE PLANE ACROSS EVERY PARTNER
                    THE ARTIFACT ITSELF LISTS -- never by the classifier's own class,
                    and never against a hand-typed partner list. The classifier's
                    class-A branch returns BEFORE it looks at whether a slice exists
                    (`classifier.py:122-125` ahead of `:128` @`c866edd324`), so its
                    class A on a closed day is SILENT about invention and cannot
                    discriminate this outcome's truth from its violation. A closed
                    day carrying priced rows FAILS this outcome even when every
                    classifier arm reads clean
         SOURCE     brief s.2 (63-80), s.5 (185-189)

  FWD-5  Andrew and AJ both receive the monthly report automatically
         DONE WHEN  EXERCISED -- both people have actually received one
         ACCEPT     both get the same monthly report in their own inbox without
                    anyone sending it by hand, and neither one is dropped
         SOURCE     brief s.6 (190-205), ruling card 3 (JOIN, not replace)

  FWD-6  The three partners' figures in the report describe the same day as
         each other
         DONE WHEN  APPLIED -- the alignment is in place
         ACCEPT     a figure shown for one partner on a given date can be set
                    beside another partner's figure for that same date without
                    the two being a day apart
         SOURCE     brief s.6a (206-232)

  FWD-8  Going outside Opal to ask a provider for missing data stays a
         decision a person makes
         DONE WHEN  EXERCISED -- the system has actually stopped and asked,
                    rather than going ahead on its own
         ACCEPT     if the only way to fill a gap is to ask the outside provider
                    for it, the system stops, names the days it wants, and waits
                    for a person to say yes
         SOURCE     brief s.5 (163-189), ruling card 4

  FWD-9  The monthly report cannot go out over incomplete data unless a person
         decides to let it -- and the refusal can be DEMONSTRATED on demand
         DONE WHEN  EXERCISED -- the refusal path has been DRIVEN DELIBERATELY on a
                    forced incomplete condition, end to end, and the refusal reached a
                    person. AMENDED v0.7: the ACCEPT's phrase "a hole the LADDER
                    CANNOT CLOSE" is replaced by "a hole the ladder DID NOT close,
                    with the reason recorded on the artifact" -- because NO driven run
                    can produce the first without REWRITING A SERVED SLICE (R-EG-6),
                    and an ACCEPT no act can satisfy is how an outcome sits
                    NOT_EVALUATED forever
                    person; no seat waits for the data to produce one
         ACCEPT     a forced class-C-or-worse condition (a hole the ladder cannot close,
                    injected under a NEVER-2 entry and restored after) drives a real run of
                    the SAME target the schedule invokes: the verdict object reads REFUSE
                    with the classifier's own class table quoted at file:line, that month's
                    publish keys stay ABSENT (a 404 beside the refused 200), the refusal
                    reaches a person, and the FORCING is disclosed on the artifact so the run
                    is never mistaken for organic. aj@ is not a recipient of any driven run
                    (Andrew-direct 2026-09-10 ~02:5xZ). The measured carry-and-disclose branch
                    (PUBLISH over two class-D holes, coverage line "5/6 trading days; 1
                    carried") is the NEGATIVE arm and is already banked
         SOURCE     supersedes FWD-2; Andrew-direct 2026-09-10 ~03:0xZ (no FWD is a wait)

  FWD-10 When a gap survives every attempt to repair it, Andrew finds out -- and
         the path that tells him is PROVEN to work, not presumed
         DONE WHEN  EXERCISED -- the terminal message has been sent by the DEPLOYED handler
                    on a deliberately driven terminal condition and READ at Andrew's own
                    inbox; no seat waits for a real failure
         ACCEPT     (i) the W1-S25 guard defect is fixed FIRST -- the guard and the renderer
                    agree on the shape of coverage_unresolved.json, with a test built from the
                    PRODUCER'S OWN OUTPUT rather than from a docstring; (ii) a driven terminal
                    condition produces the message, it lists each day still missing with its
                    partner and the provider the data should have come from, and it is READ at
                    andrew@ by a gateway read, never a send-log self-report; (iii) the send is
                    OBSERVABLE afterwards -- the handler records that it fired (W1-S26: today
                    it emits no log line and no trail selects the SES data plane); (iv) aj@ is
                    NOT a recipient of any driven run (Andrew-direct 2026-09-10 ~02:5xZ)
         SOURCE     supersedes FWD-7; Andrew-direct 2026-09-10 ~03:0xZ (no FWD is a wait)

```

> **WHY FWD-8 SURVIVED THE FOLD, stated because Andrew raised folding it and this seat did not simply comply.**
> He observed FWD-8 *"can be folded into"* FWD-7 because both name the missing dates. **The REPORT CONTENT is
> genuinely shared and is folded** -- FWD-7's message carries the dates/partner/provider detail. **The
> AUTHORIZATION is not, because the two sit at different moments in the ladder:** FWD-8 fires *before* we leave
> Opal and asks permission; FWD-7 fires *after* leaving Opal already failed and reports the outcome. Folding
> them would silently retire ruling card 4's per-use authorization -- and a message sent after egress failed
> cannot ask permission for the egress that already happened. **Flagged rather than assumed: if he intended
> card 4's capability to stop being a named outcome, FWD-8 retires and its number stays vacant forever.**
> ✅ **RESOLVED 2026-09-02 ~17:0xZ, Andrew-direct via `/open-calls` CALL 3 of 3, "All recs approved" -- KEEP.**
> FWD-8 stands as a named outcome; ruling card 4 is not retired. Record:
> `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260902_ALL_RECS_APPROVED_LANES_STEP4_CHECK_FWD8.md`.

---

## 1. The arc

**Not a list -- an ordered movement, and the order is itself a ruling.**

```
  STARTS   the producers stop losing days at all
           port inf's catch-up into cot- and bd-49f-, on a REPORTING-OBLIGATION
           window rather than a day count
                |
                |  unlocks: a gate can now be a PROOF instead of the primary defence
                v
  THEN     we can tell the four kinds of empty day apart
           market-closed / unpriced / producer-never-fired / genuinely-absent
                |
                |  unlocks: repair without fabrication, and refusal without false alarms
                v
  THEN     the artifact carries its own completeness, and the gate blocks a bad month
                |
                |  unlocks: publishing becomes a decision with evidence attached
                v
  THEN     the ladder repairs what it can, unattended, and stops to ask before egress
                |
                |  unlocks: distribution can widen without widening a defect
                v
  THEN     the three partners are put on one date basis   ** PREREQUISITE TO THE SEND **
                |
                v
  ENDS     the report goes out on its own to both people -- and in the one case where
           a hole survived everything above it, an urgent message names exactly what
           is missing rather than letting a quiet gap ship
```

**Two ordering constraints, two different reasons -- both ruled, neither stylistic:**

- **Catch-up BEFORE the gate.** A gate shipped first converts a silent wrong number into a blocked report
  without fixing the cause, and *"the first thing a blocked monthly produces is pressure to override the gate."*
- **Alignment BEFORE the automated send.** Widening the distribution of a partner-incomparable file is the one
  act that converts a contained defect into a circulated one. The defect has cost nothing so far **precisely
  because distribution was one person.**

---

## 2. Purpose -- what DONE means

**DONE =**

1. **The recurrence is closed at the cause.** A day the producer failed to write is picked up by the producer
   itself on a later run, over a window bounded by the reporting obligation rather than by a guessed vendor lag.
2. **The artifact can no longer hide its own gaps.** Coverage is stated in the report, every month, whatever
   the verdict.
3. **A month with real holes does not publish**, and the refusal is visible.
4. **Nothing fabricates.** A legitimately empty day stays empty and is reported as expected, not repaired.
5. **The send is automatic, to both people, on one date basis.**
6. **A surviving hole reaches Andrew as an urgent, structured message** -- and that message is rare enough that
   its arrival is itself a signal, not background noise.

**The measured problem this closes:** the served August report was rendered over a month missing **5 of 21
Cottonwood trading days**; the July report was rendered **4h10m before** 8 late slices landed and was never
rebuilt. **Neither failure was visible in the artifact** -- carry-forward renders a gap and a held position
identically. All five August holes had upstream data present and fully priced the whole time: **the producer
never fired, and no egress was ever required.**

---

## 3. Territory -- what this owns, and what it only relies on

| | |
|---|---|
| **OWNS** | the catch-up inside `cot-etf-ownership-daily` and `bd-49f-etf-ownership-daily`; the coverage classifier; the pre-publish gate as a render precondition; the coverage line in the report; the remediation ladder; the terminal SES notification; `EMAIL_RECIPIENT`; **the Orion date-basis alignment (`orion_normalize_as_of`) — ADDED 2026-09-02, see below** |

> ⛔ **THIS CELL WAS MISSING A SURFACE, AND THE MANIFEST FOUND IT BY LOOKING BACKWARDS.** `3.0.0_SA_CVO`
> (Rule 24 verdict @`0e8d6127f3`) caught that the step-5 manifest's S13 carried `verb: align` — a WORK verb —
> on Orion date-basis alignment, a surface this table placed in **no** row: not OWNS, not RELIES-ON, not
> TOUCHES. Re-derived here on my own instrument rather than accepted on the relay: **7 of 8 outcomes carried
> an OWNS surface; FWD-6 carried none.**
> **Three outcomes were legal and the choice was mine: add it to OWNS, demote S13 to `verify`, or declare
> FWD-6 out of scope. I ADDED IT.** Demoting the verb would have made the summary sentence true while leaving
> real work unplaced, and declaring FWD-6 out of scope would have silently shrunk the endpoint *after* Andrew
> approved ruling card 1 that made this a prerequisite to the send. **The cell was wrong; the manifest was right.**
> ⚠ **And the residual is mine too:** postulate (i) is MECE over THIS cell, so a manifest can be perfectly
> MECE over a domain that is itself incomplete. CVO verified the manifest against the cell and explicitly did
> **not** verify the cell against the world. One gap is now closed; the cell is not thereby certified.
| **RELIES ON, does not own** | `lib/trading_calendar.py`; the upstream silver/bronze partitions; the existing `REPORTS_SNS_TOPIC` (`etfs-reports-alerts`); the EventBridge schedule; SES identity verification; `inf-etf-ownership-daily`'s existing catch-up as the PORT SOURCE |
| **TOUCHES BUT MUST NOT CHANGE** | the ZERO-vs-MISSING producer contract -- it is the thing that makes class B distinguishable, and "fixing" it would destroy the discriminator |

**Lanes** (from the brief; COO sequences and seats): `0.7.0_AE_CloudOps` Lambda + Terraform + orchestrator;
`0.4.0_DS_ClientPlatform` classifier + renderer + Orion alignment; `3.0.0_SA_CVO` exercises acceptance.

---

## 4. Acceptance properties

Numbered, each disputable. **Each must be EXERCISED, not asserted -- a declared-but-unrun falsifier is a
promise, not a control.**

1. A deleted slice for a trading day whose upstream exists and is priced is **regenerated by the next
   ordinary producer run**, and the run names the date it recovered.
2. A partner day whose upstream does not arrive until **12-13 days late is still caught up.** *This is the
   property a straight port fails while passing review* -- the shipped constant looks back 10 days and 49F's
   observed tail already exceeds it.
3. Run against August 2026 **as it stood before the 09-01 repair**, the gate **refuses** and names exactly
   five real holes. Run against August as it stands now, it **publishes**.
4. A day with an upstream partition and nothing priced is classified **expected, not a hole**, and **no
   backfill is attempted against it.**
5. On a refusal, **no report is sent**, and the refusal is visible on the existing topic.
6. Every rendered report carries a per-partner coverage line **regardless of verdict**.
7. Both `aj@` and `andrew@` receive a real send, verified **as delivery**, not as a successful API call --
   a comma-joined recipient string can be accepted and mis-delivered, and that failure is silent.
8. When every rung fails, **exactly one urgent message** reaches `andrew@opalinvest.com` naming each missing
   date, its partner, and its provider -- and it does **not** fire when the ladder resolved the gap.
9. **No rung, under any failure, writes a value that was not measured.** If all three fail, the day stays
   missing and is reported as missing.

> **Property 2 is the one that matters.** It is the only one that fails on a plausible, review-passing
> implementation. Properties 3 and 4 are cheap to satisfy and cheap to fake; 2 is neither.

---

## 5. Out of scope

- **No new catch-up engine.** Port `inf`'s. Two implementations of one convention drift, and only one gets
  fixed -- exactly how `_carry` and `_carried_daily` diverged into a $200M chart error.
- **No new monitor, alarm, SNS topic, or standing freshness service.** See the carve-out in s.0: one send, on
  the terminal failure path.
- **No parallel/shadow pipeline or standing parity comparator** (Andrew complete veto). Modify producers in place.
- **No DynamoDB** -- the 2026-08-24 design gate ruled S3 gold parquet.
- **No restatement of published figures and no partner notification** (ruling card 2, forward-only).
- **`ETFS_CANON` activation** -- ruling card 5, sequenced after this project.
- **Retiring `etfs-canon-fanin`** -- brief s.9.1, an independent finding with its own owner. It is ENABLED on a
  daily schedule against a DynamoDB table that does not exist, so it fires daily and cannot succeed. **Carried
  here so it is not lost, explicitly NOT in this project's scope.**

---

## 6. Rulings that BIND

1. **Reporting-obligation window, not a day count.** Reconcile every trading day from the start of the prior
   month until that month's report has shipped. **A day-count window is explicitly NOT TAKEN and is not to be
   re-proposed** -- it makes correctness depend on a vendor lag distribution nobody controls.
2. **The window's terminus is a SHIPPED SIGNAL, not a date** -- read whether the month's report exists. Deriving
   it from a calendar assumption lets a blocked render silently end the very reconciliation that would unblock it.
3. **JOIN, not replace** -- `aj@` AND `andrew@`, as a comma-separated variable so a future recipient is a
   variable change, not a code change.
4. **Rungs 1-2 unattended; rung 3 STOPS AND ASKS.** No standing pre-authorization for vendor egress.
5. **Orion date-basis alignment gates the automated send** -- not the guardrail. The guardrail can and should
   land first.
6. **Egress is the THIRD fallback and should almost never fire**, correcting the framing of the original ask:
   in the only real instance, all five days were already in our own bucket.
7. **The terminal SES notification is a last resort** (Andrew-direct 2026-09-02). Its routine arrival is
   evidence that the repair ahead of it is not working.

> **ONE UNRESOLVED DEPENDENCY, CARRIED NOT BURIED** (brief s.9.2): Inflection's lineage does not reconcile --
> repo source computes one bucket path, every recent slice cites another, and the deploy postdates the last
> repo change. **Those three facts do not fit together.** This binds ladder rung 2, which must check the bucket
> the producer *actually reads*, and for Inflection **nobody currently knows which that is from the code alone.**
> Resolving it needs a deployed-bytes diff against the build input, not a source read.

---

## 7. SURFACE MANIFEST (step 4 -> step 5) -- CONTRACT ADOPTED

**ADOPTION RULING (`1.0.0_SA_CTO`, 2026-09-02).** `2.0.0_SA_COO`'s step-4 surface manifest contract
(@`4bb2c5d94f`) is **ADOPTED as the step-4 standard**, on `3.0.0_SA_CVO`'s Rule 24 verdict @`0e8d6127f3`:
*"ADOPT THE CONTRACT, do not adopt the RECORD."* The gap it names is real and it is mine -- s.3 above named
`cot-etf-ownership-daily` in PROSE, and **a comp-tool takes a SUBJECT, so step 5's first act was discovery
rather than decomposition.** Discovery is the half that should be mechanical.

⛔ **THE FOUR-POSTULATE RECORD IS NOT ADOPTED AS WRITTEN. Three edits, applied below:**
1. **Postulate (iv) is corrected.** *"No remedy moves `absent`"* is contradicted by the instance it ships with
   (S11/S12 are `absent`, seated, and depended on). What is meant is **no BUILD remedy moves `absent`** --
   `verify` is precisely the act that does. The ratified state machine already exists and is used here
   instead: `.tools/substrate-card-check.py:126` `BASIS_RANK = {absent:0, unmeasured:0, held:1, inferred:2,
   measured:3}`; **every legal transition is a rank increase.**
2. **S7 is SPLIT** (postulate ii, same grain): rungs 1-2 are unattended automation; rung 3 **stops and asks a
   person** -- a different ACTOR, not a later step.
3. **The claim enum is FIVE values, not four.** CLAUDE.md:155's four-value shorthand is the gap;
   `substrate-card-check.py:57` `BASIS_VOCAB` carries five including `unmeasured`. Census cited from CVO
   s.4 (2,570 hits / 144,571 files, DEF=3) -- **cited, deliberately not re-run.**

### 7.1 Provenance of the rows below -- READ THIS BEFORE CITING ANY CELL

**Most evidence cells are `2.0.0_SA_COO`'s runs, not this seat's.** They are carried WITH their attribution
rather than restated as mine, because a relayed measurement that loses its origin becomes a second apparent
carrier of one claim. **`MEASURED-BY` names the instrument's owner on every row.** `3.0.0_SA_CVO` explicitly
did NOT re-measure the 13 evidence cells; its verdict is about the schema only.

### 7.2 The manifest

| id | outcome_ref | surface | claim | MEASURED-BY / evidence | lane | verb | depends_on | accept | bound |
|---|---|---|---|---|---|---|---|---|---|
| S1 | FWD-1 | `infra/aws/lambda/cot-pipeline/cot-etf-ownership-daily/lambda_function.py` | measured | COO -- enumerate **0 hits / 177 lines** | AE_CloudOps | port | S3,S10 | 1,3 | window is REPORTING-OBLIGATION. **Do not port `CATCHUP_WINDOW_DAYS = 10`** |
| S2 | FWD-1 | `infra/aws/lambda/bd-pipeline/bd-49f-etf-ownership-daily/lambda_function.py` | measured | COO -- enumerate **0 hits / 122 lines** | AE_CloudOps | port | S3,S10,S11 | 1,2 | 49F tail **12-13 d** exceeds the shipped 10-d constant; a straight port passes review and fails property 2 |
| S3 | FWD-1 | `infra/aws/lambda/inf-pipeline/inf-etf-ownership-daily/lambda_function.py:271-314` | measured | COO -- 4 hits / 317 lines | AE_CloudOps | verify | -- | 1 | PORT SOURCE. Relied on, **not owned** -- do not modify to suit the port |
| S4 | FWD-4 | **NEW -> `data/etfs/scripts/coverage/classifier.py`** (home RULED in 7.4) | unmeasured | -- | DS_ClientPlatform | classify | S10 | 4 | **Class B is the trap.** Discriminator = read upstream partition + count priced. Must not "fix" the ZERO-vs-MISSING contract |
| S5 | FWD-3 | `data/etfs/scripts/presentation/render_month_end.py` | measured | COO -- path resolves, 3 hits / 148,724 files | DS_ClientPlatform | wire | S4 | 6 | coverage line prints **regardless of verdict** |
| S6 | FWD-2 | **NEW -> precondition INSIDE `render_month_end.py`** (ambiguity RULED in 7.4) | unmeasured | -- | DS_ClientPlatform | wire | S1,S2,S4 | 3,5 | **NOT a standing service.** Catch-up before gate |
| S7a | FWD-8 | **NEW -> `data/etfs/scripts/coverage/remediate.py`** -- rungs 1-2, unattended | unmeasured | -- | AE_CloudOps | wire | S4,S12 | 9 | **No rung may fabricate.** Rung 1 re-runs the producer; rung 2 re-checks upstream |
| S7b | FWD-8 | same module, rung 3 -- **STOPS AND ASKS A PERSON** | unmeasured | -- | AE_CloudOps | wire | S7a | 9 | **DIFFERENT ACTOR, not a later step.** Per-use egress, no standing grant. Names the dates it wants and waits |
| S8 | FWD-7 | **NEW -> `infra/aws/lambda/etfs-reports-orchestrator/lambda_function.py`**, reusing the existing SES path (RULED in 7.4) | unmeasured | -- | AE_CloudOps | wire | S7b | 8 | **ONE send, terminal path only.** Not a monitor, no schedule, no polling. Fires only when EVERY rung failed |
| S9 | FWD-5 | `infra/aws/lambda/etfs-reports-orchestrator/lambda_function.py:49,158,189,221,277` | **measured** | **CTO, THIS SEAT** -- enumerate over split/Destinations/EMAIL_RECIPIENT/ToAddresses = **12 hits / 375 lines / 16 sections** | AE_CloudOps | wire | S13 | 7 | ⛔ **A VARIABLE-ONLY CHANGE CANNOT DELIVER FWD-5 -- see 7.3** |
| S10 | -- | `lib/trading_calendar.py` **+ 3 vendored copies**; neither target producer has one | measured | COO -- 5 paths | AE_CloudOps | verify | -- | 4 | **RELIES-ON, shared beneath S1/S2/S4.** Rule 22 common-dependency limb. Which calendar each producer resolves is UNANSWERED |
| S11 | -- | `bd-49f-etf-ownership-daily` **vs its `-canonical` twin** -- which writes the served slices | absent | COO -- 4 producer dirs; discriminator NOT run | AE_CloudOps | verify | -- | -- | WRONG-OBJECT risk under S2; comp-read cannot detect a wrong file (rule 21 limb ii) |
| S12 | -- | Inflection lineage: repo computes one bucket, slices cite another, deploy POSTDATES the last repo change | absent | brief s.9.2 -- **attributed, re-measured by NOBODY** | AE_CloudOps | verify | -- | -- | Needs a **deployed-bytes diff vs build input**, NOT a source read. Binds rung 2 |
| S13 | FWD-6 | `orion_normalize_as_of` -- **now placed in the s.3 OWNS cell** | held | brief s.6a -- **0 calls / 19 files, the brief's denominator, not mine** | DS_ClientPlatform | align | -- | -- | **PREREQUISITE TO THE SEND ONLY.** Guardrail lands first. Forward-only: restate nothing, notify no partner |

**MECE, BOTH DIRECTIONS, run rather than asserted:**

```
  FORWARD   every OWNS item has >=1 row .......... 8 of 8   (7 original + Orion, added this turn)
  REVERSE   every WORK row maps to an OWNS item .. S13 FAILED -> FIXED by placing Orion in OWNS
  OUTCOMES  every FWD-n has >=1 owned surface .... 8 of 8   (was 7 of 8; FWD-6 was the gap)
  S10/S11/S12 are RELIES-ON, verb=verify, correctly NOT work rows.
```

### 7.3 ⛔ S9 -- MEASURED AT SOURCE, AND IT REFUTES A PREMISE IN THE BRIEF

The brief (s.6) says a comma-separated `EMAIL_RECIPIENT` makes a future recipient *"a variable change rather
than a code change."* **That is FALSE against the source.**

```
  :49   EMAIL_RECIPIENT = os.environ.get("EMAIL_RECIPIENT", "andrew@opalinvest.com")   <- ONE string
  :158  msg["To"] = EMAIL_RECIPIENT            <- header only
  :221  msg["To"] = EMAIL_RECIPIENT
  :189  _ses.send_raw_email(Source=SES_SENDER, Destinations=[EMAIL_RECIPIENT], ...)    <- THE ENVELOPE
  :277  _ses.send_raw_email(Source=SES_SENDER, Destinations=[EMAIL_RECIPIENT], ...)
```

**`Destinations=[EMAIL_RECIPIENT]` is a ONE-ELEMENT list whose single element would be the entire
comma-joined string** -- one malformed address, not two recipients. **There is no recipient parsing anywhere
in the file.**

⭐ **THE ENUMERATION CARRIES ITS OWN POSITIVE CONTROL, which is why the zero is trustworthy:** the pattern
included `split` and DID match one -- `key.rsplit("/", 1)` at :181, a FILENAME split. **The lens can see a
split in this file; there simply is no recipient split.** A bare zero would have been indistinguishable from
a broken pattern.

**CONSEQUENCE:** FWD-5 requires a **CODE change**, not an environment-variable change. Ruling card 3 (JOIN)
**cannot be implemented by setting the variable alone.** `claim` moves `inferred -> measured` (BASIS_RANK
2 -> 3), a legal rank increase. COO named S9 as the row it most wanted converted, because its failure mode is
silent -- Andrew stops receiving his own report, which looks exactly like the render not running. **It was
right to want it, and the answer is worse than "unverified": the change as specified would not have worked.**

#### ⛔ 7.3a -- CORRECTION: FOUR SITES, NOT TWO, AND THE TWO SHAPES CONFLICT

**My first version of this section said "a code change at :189 and :277." That is HALF THE FOOTPRINT, and a
TO scoped to it would hand the builder the half that breaks the other half.** Found by `3.0.0_SA_CVO`
(msg 92498) re-deriving on a DIFFERENT pattern from mine -- corroboration, not repetition -- and then
**confirmed by this seat on its own read of the source**, not accepted on the relay.

```
  _build_report_email      (145-183)   :158  msg["To"] = EMAIL_RECIPIENT        HEADER
  _email_report            (186-190)   :189  Destinations=[EMAIL_RECIPIENT]     ENVELOPE
  _build_correction_email  (213-270)   :221  msg["To"] = EMAIL_RECIPIENT        HEADER
  _send_correction_email   (273-278)   :277  Destinations=[EMAIL_RECIPIENT]     ENVELOPE
```

**TWO send paths, each with a header site AND an envelope site. I named only the two envelope halves.**

>> **THE TWO HALVES WANT OPPOSITE SHAPES, WHICH IS WHY THIS IS NOT A LINE COUNT.**
> `Destinations=` is the **SMTP envelope** and needs a **LIST** of two addresses.
> `msg["To"]` is an **RFC 5322 header** and needs the **COMMA-JOINED STRING** -- so the header half is,
> by luck, **already correct** under the brief's variable-only approach.
> **ONE VARIABLE CANNOT BE BOTH.** The obvious fix -- make `EMAIL_RECIPIENT` a list, or `.split(",")` it at
> :49 -- repairs :189/:277 and **SILENTLY DAMAGES :158/:221**, where a list assigned to `msg["To"]` does not
> render a valid To header. <<

**So FWD-5 is a TYPE decision landing at FOUR sites across TWO paired functions:** keep the joined string for
the headers, derive a list for the envelopes, on **both** paths. A TO scoped to `:189` and `:277` is
incomplete in the one direction that fails silently.

⚠ **Cosmetic, not delivery, but worth knowing before a log line is read as evidence:** `:325` (failure-alert
text) and `:373` (handler return `"recipient"`) both interpolate the raw variable and will print the joined
string. Also, both send-path docstrings still say the mail goes *"to Andrew"* -- descriptive drift the moment
JOIN lands, and the kind of stale self-description that later reads as a spec.

### 7.4 DESIGN RULINGS -- the four unplaced homes (the step-4 question COO surfaced)

COO reported *"half the OWNS surfaces have nowhere to land yet"* and correctly routed that to step 4.
**The governing constraint is S10:** `trading_calendar.py` exists in FOUR places because a shared dependency
was copied across the repo/Lambda boundary instead of being placed once. **Every ruling below is chosen to
avoid minting a fifth instance of that same defect.**

- **S4 classifier -> `data/etfs/scripts/coverage/classifier.py`.** One home, importable by the renderer.
- **S6 gate -> INSIDE `render_month_end.py`, NOT the orchestrator.** The brief left this open (*"a
  precondition inside `render_month_end.py` (or the orchestrator immediately before it)"*). **RULED: inside
  the renderer.** Putting the gate in the Lambda would require the classifier on BOTH sides of the
  repo/Lambda boundary -- which is exactly how S10 happened. The orchestrator gates only the SEND, on the
  verdict the renderer returns.
- **S7a/S7b ladder -> `data/etfs/scripts/coverage/remediate.py`**, beside the classifier it consumes.
- **S8 terminal SES -> the ORCHESTRATOR, reusing the existing `_ses.send_raw_email` path.** The ladder returns
  a structured unresolved-report; the orchestrator sends it. **Build-ladder rung 5: the orchestrator already
  holds the SES client, the verified sender identity and the IAM.** A second SES sender in a repo script would
  be a duplicate send path -- and a second place the carve-out's width would have to be restated.

⚠ **These are step-4 PROPOSALS placed so step 5 has an address to run a lens against; they are NOT measured.
A decomp finding may overturn any of them** -- and S11 (which of the two `bd-49f` twins actually writes the
served slices) is the one most likely to move S2's address out from under this table.

## 9. ADDENDUM v0.4 (2026-09-09 ~22:0xZ, `1.0.0_SA_CTO`) -- every date-gated grade made contingent on a manual/test run

**THE MANUAL-TRIGGER RULE** (Andrew-direct 2026-09-09 ~21:4xZ at the `1.0.0_SA_CTO` terminal, verbatim in `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260909_214xZ_NO_WAITING_EVERY_DATE_GATED_ACCEPT_GETS_A_MANUAL_TRIGGER_FORM.md`: *"we need to not be 'waiting' on anything, anything that we'd be waiting for needs a manual trigger of some kind depending on the test type ... include addendums for each that mandate the requirement is contingent on a relevantly structured manual/test run"*). A manual run is the EXERCISED form of an outcome only when all five hold: (1) SAME TARGET, not a copy -- the rule's own target invoked with the scheduled payload shape; (2) REAL PLANE -- real keys, catalogs, inboxes, devices; a by-hand write to a SERVED key is a served-output move (NEVER-2 entry + never-widen sign-off CTO+COO, rollback named); (3) TOLD APART ON THE ARTIFACT -- a run-id / trigger field, never the clock; (4) the schedule's OWN firing proven from HISTORY (prior rule-initiated executions listed with a denominator), never by waiting -- a rule that has never fired gets a one-off near-term `at()` on the same rule, then restored; (5) the next scheduled fire is CONFIRMATION, never a gate -- no grade carries "pending the fire" again.

Round 1 closed with 7 of 8 grades NOT_EVALUATED, every one of them "on the 10-01 fire" or "a rare real event". Under the rule, the grades below read on the manual runs; the 10-01 fire confirms. Rows S14-S18 are the round-2 cells `2.0.0_SA_COO~B` cuts as ONE issuance; the CTO grades FWD-1..FWD-8 on their records.

| id | outcome_ref | surface | claim | MEASURED-BY / evidence | lane | verb | depends_on | accept | bound |
|---|---|---|---|---|---|---|---|---|---|
| S14 | FWD-3, FWD-5, FWD-6 | THE AUGUST RE-RENDER: the SAME monthly orchestrator (`etfs-reports-monthly-run`'s target, `infra/aws/terraform/etfs-reports/orchestrator.tf`) started by hand for `month=2026-08` with the scheduled payload shape; published to the served key `s3://opal-data-etfs/platinum/reports/2026-08/` WITH the coverage line; delivered to aj@opalinvest.com and andrew@opalinvest.com | absent | the published August CSV ends on its numeric rows and predates the round (ROUND_ANALYSIS.round1, FWD-3); FWD-5 never exercised | AE_CloudOps | verify | -- | 3, 5, 6 | a NEVER-2 entry OPENED FIRST naming the served key and the archived prior object (sha256), never-widen sign-off CTO+COO inside it; the execution's own name on the artifact (`trigger=manual`); the served CSV's last row is `# coverage:` with the month's denominator; `etf_ownership.pdf` at the publish key; DELIVERY at BOTH inboxes read from the mailboxes (message ids), never from the send log; the three partners' as-of aligned on the live render (FWD-6's qualifier re-read); rollback = the archived object restored byte-equal; the 10-01 fire is confirmation |
| S15 | FWD-2, FWD-7, FWD-8 | THE SEPTEMBER-TO-DATE REFUSAL: the SAME orchestrator started by hand for `month=2026-09` TODAY -- a partial month is incomplete by construction, so the refusal ladder runs on real data | absent | no real refusal has reached a person (FWD-2, FWD-7, FWD-8 all NOT_EVALUATED) | AE_CloudOps | verify | S14 | 2, 7, 8 | the ladder runs to its end on the real data (each rung's output in `coverage_unresolved.json`); the HTML lands under `refused/` and the 2026-09 publish key stays ABSENT (head-object 404 beside the refused object 200); the alert text produced; the terminal email DELIVERED to andrew@ (read at the inbox) -- the ONE send the SES carve-out authorizes, on the terminal path, on a real refusal; `coverage_egress_ask.json` written; vendor egress 0 over the run window (the gateway's egress log and CloudTrail, denominator printed); the run-id on every artifact |
| S16 | FWD-4 | THE LEGITIMATELY-EMPTY DAY THAT HAS ALREADY HAPPENED: 2026-09-07 (Labor Day, US market shut) read on S15's run | measured | a real closed-market day inside the month; graded NOT_EVALUATED only because every prior B-class proof was a fixture | AE_CloudOps | verify | S15 | 4 | `coverage_verdict.json` for 2026-09 classifies 2026-09-07 as A (market closed); it appears in no partner's holes; **AMENDED v0.6 -- THE ROW AS WRITTEN PASSED ON THE VIOLATION:** it enumerated `cottonwood or 49financial`, TWO partners, and `ETFS_GUARDRAIL-W1-S31` found FOUR PRICED ROWS on that very date under the THIRD (`daily/inflection/2026-09-07.json`, value-sha identical across 09-05..09-08 = carried forward, LastModified three days before the run). The arm now enumerates EVERY partner FROM THE ARTIFACT'S OWN LIST (never a hand-typed pair), prints that list as its denominator beside the count, and reads each partner's `daily/<partner>/2026-09-07.json` for PRESENCE and, where present, for PRICED ROWS -- a present-and-priced slice on a closed day FAILS the arm. The classifier's class-A reading is retained as CONTEXT and is explicitly NOT the discriminator; `expected_empty` carries it with holes unaffected; CloudTrail PutObject 0 for that day's keys over the run |
| S17 | FWD-1 | THE FILLED-IN DAY: the daily producer (S1 `cot-etf-ownership-daily` / S2 `bd-49f-etf-ownership-daily`) invoked by hand with the scheduled event payload against a REAL hole (named by S15's coverage read, or by `catchup_processed` on a date the producer missed); if the estate holds no real hole, a CONTROLLED one -- one slice archived to a quarantine key under its own NEVER-2 entry, the producer fired, the slice restored byte-equal after | absent | FWD-1 NOT_EVALUATED: needs a recovered date on the producer's own fire | AE_CloudOps | verify | -- | 1 | the function's CloudWatch log for the manual invocation names the recovered date in `catchup_processed`; the slice exists after with the day's rows; positive control: a date NOT missing is not reported recovered; the invocation record shows the manual initiator; the schedule's own firing proven from the function's prior scheduled invocations (CloudTrail Invoke by the rule), listed with a denominator |
| S18 | -- (the schedules) | THE SCHEDULE'S FIRING FROM HISTORY: the executions of `etfs-reports-monthly-run` and the two daily rules listed from CloudTrail / the state machine's execution list with their initiators -- the ones that produced the published August artifact and the daily slices | measured | the published August CSV and the daily slices exist, so the fires have fired; never listed as evidence | AE_CloudOps | verify | -- | 1, 5 | the list printed with its denominator and the initiator column showing the rule; 10-01 and the daily crons stay CONFIRMATION, never a gate |
| S19 | FWD-4 | **THE CLASSIFIER ORDERING DEFECT** -- `data/etfs/scripts/coverage/classifier.py:122-125` returns class A and `continue`s on a non-trading day BEFORE the presence check at `:128`, so a slice sitting on a closed day is UNREACHABLE by the classifier whose whole job is to tell a legitimately-empty day from a repaired one. The docstring's own words -- "only PRESENCE of a key matters here" -- describe the check the class-A branch skips. This is INSIDE this project: s.3 OWNS names "the coverage classifier" and S4 is FWD-4's own code row against this exact file | measured (`W1-S31`, re-read by `1.0.0_SA_CTO` at the cited lines) | FWD-4's only instrument cannot see FWD-4's violation | DS_ClientPlatform | classify | -- | 4 | the non-trading-day branch reports a closed day carrying a slice DIFFERENTLY from a closed day carrying nothing (a distinct class or a populated field -- the SHAPE is the assignee's, the DISCRIMINATION is the bar); a test built from the PRODUCER'S OWN OUTPUT on 2026-09-07 rather than from the docstring; the ZERO-vs-MISSING contract S4 protects is not disturbed (positive control: a genuinely empty closed day still classifies A and still appears in no partner's holes); and the month's verdict object re-read after the change still classifies every ordinary closed day exactly as it did before, denominator printed |
| S20 | FWD-4 | **THE OUTSIDE HALF, PLACED NOT ADOPTED** -- a partner producer writes PRICED values onto non-trading days (`daily/inflection/` for 09-05, 09-06, 09-07, one value-sha across all four days and 09-08, differing from 09-04): carried-forward duplicates, standing behaviour predating this project's work. That PRODUCER is not this project's surface (s.3 OWNS names the catch-up inside `cot-etf-ownership-daily` and `bd-49f-etf-ownership-daily`, not this one), and spine v2.4 forbids routing an outside remedy into a running project | measured (`W1-S31`) | -- | -- | -- | -- | 4 | **NOT A CELL OF THIS PROJECT.** This row exists so the finding is placed rather than carried: the DETECTION is S19's and lands here; the REMEDY on the producer leaves as a brief to `4.0.0_SA_CRO` and enters at L1 as its own project. Until then the condition is DISCLOSED by S19's discriminator rather than repaired, and FWD-4 grades on the disclosure, never on the producer's silence. **BRIEF REQUEST SENT AND ITS DELIVERY STATE MEASURED, 2026-09-10 ~03:5xZ:** msg 94954 to `4.0.0_SA_CRO` returned **QUEUED -- no live session**, so the request is written and waiting, NOT delivered. Per the law this seat landed the same night ("queued if not live" is a WISH, not a delivery; a BASE serial with no base session is a silent hole), THIS ROW is that request's durable home and the relay is held by `0.0.0_AB_MSTR` (register owner, DELIVERED 94956) -- never by the queued message. If no brief exists when round 3 closes, the L10 says so rather than letting the placement lapse into a carry |

## 10. ENDPOINT ADDENDUM v0.5 (2026-09-10 ~03:1xZ, `1.0.0_SA_CTO`) -- the two WAIT outcomes superseded

**Andrew-direct ~03:0xZ at the `1.0.0_SA_CTO` terminal, VERBATIM:** *"Anything that we'd have to actually wait for a failure to close
out, that FWD should be superseded, because otherwise we might be waiting forever. It is not good to write FWDs in a manner that cannot
be proven or that requires waiting some indeterminate time to be proven. Our goal with projects and task orders is not to sit on them for
weeks, it is to sprint, execute, validate, and close. We should almost never be waiting unless it is truly essential to the project in some
crucial way to do so, the likes of which should be expressly qualified. I think the way it should work actually is that no FWD is ever a
'wait' unless explicitly advised otherwise."* Record:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260910_030xZ_NO_FWD_IS_A_WAIT.md`.

**Applied here:** of the eight, SIX were provable by an act a seat can take and are proven or in flight. TWO waited on a failure mode
nobody controls -- FWD-2 (a REFUSE verdict) and FWD-7 (a terminal failure the PRD itself calls rare by design). Both are superseded in
place above; their ids are permanent and never reused. The successors keep the OUTCOME he wants and move the proof from *the event
happened* to *the mechanism was driven deliberately and worked*.

```
  FWD-9   The monthly report cannot go out over incomplete data unless a person
          decides to let it -- and we can DEMONSTRATE the refusal on demand
          DONE WHEN  EXERCISED -- the refusal path has been DRIVEN DELIBERATELY on a
                     forced incomplete condition, end to end, and the refusal reached
                     a person; no seat waits for the data to produce one
          ACCEPT     a forced class-C-or-worse condition (a hole the ladder cannot close,
                     injected under a NEVER-2 entry and restored after) drives a real run
                     of the SAME target the schedule invokes: the verdict object reads
                     REFUSE with the classifier's own class table quoted at file:line, the
                     publish keys for that month stay ABSENT (a 404 beside the refused
                     200), the refusal reaches a person, and the FORCING is disclosed on
                     the artifact so the run is never mistaken for organic. The already-
                     measured carry-and-disclose branch (2026-09-10: PUBLISH over two
                     class-D holes, coverage line "5/6 trading days; 1 carried") is the
                     NEGATIVE arm and is already banked
          SOURCE     supersedes FWD-2; Andrew-direct 2026-09-10 ~03:0xZ

  FWD-10  When a gap survives every attempt to repair it, Andrew finds out -- and
          the path that tells him is PROVEN to work, not presumed
          DONE WHEN  EXERCISED -- the terminal message has been sent by the deployed
                     handler on a DELIBERATELY driven terminal condition and READ at
                     Andrew's own inbox; no seat waits for a real failure
          ACCEPT     (i) the W1-S25 guard defect is fixed FIRST -- the guard and the
                     renderer agree on the shape of coverage_unresolved.json, with a test
                     built from the PRODUCER'S OWN OUTPUT rather than from a docstring;
                     (ii) a driven terminal condition produces the message, it lists each
                     day still missing with its partner and the provider the data should
                     have come from, and it is read at andrew@ by a gateway read (never a
                     send-log self-report); (iii) the send is OBSERVABLE afterwards -- the
                     handler records that it fired (W1-S26: today it emits no log line and
                     no trail selects the SES data plane); (iv) aj@ IS NOT A RECIPIENT of
                     any driven run (Andrew-direct ~02:5xZ)
          SOURCE     supersedes FWD-7; Andrew-direct 2026-09-10 ~03:0xZ
```

### The two superseded outcomes, kept VERBATIM (ids permanent, never reused, no longer graded)

They are held here rather than in the ENDPOINT section so that section and `PRD_HEADER.endpoint_outcomes` name exactly the same
eight live ids -- the L6 gate reads both halves and is right to refuse when they disagree (`2.0.0_SA_COO` 94931). The supersession
rule requires the text be kept with its reason beside it; it does not require it be kept in the ENDPOINT list.

```
  FWD-2  [SUPERSEDED 2026-09-10 by FWD-9 -- Andrew-direct ~03:0xZ: "anything that we'd have to
         actually wait for a failure to close out, that FWD should be superseded". The id is
         PERMANENT and never reused; the text is kept verbatim below and is no longer graded.]
         The monthly report cannot go out over incomplete data unless a
         person decides to let it
         DONE WHEN  EXERCISED -- the check has actually refused a month, and the
                    refusal reached a person
         WHY SUPERSEDED  its only proof was a REFUSE verdict, which arrives when the data
                    happens to carry a class-C-or-worse hole that survives the ladder -- an
                    event no seat controls. Measured 2026-09-10: the September run produced
                    PUBLISH over two class-D holes, because carry-and-disclose IS the designed
                    behaviour there, so the refusal this bar waits for may never come.
         ACCEPT     when days are genuinely missing, the report does not go out,
                    and someone is told which days and why -- rather than it
                    arriving looking normal
         SOURCE     brief s.4 (130-162), s.5 (163-189)

  FWD-7  [SUPERSEDED 2026-09-10 by FWD-10 -- same Andrew-direct. Id permanent, never reused;
         text kept verbatim, no longer graded.]
         When a gap survives every attempt to repair it, Andrew finds out --
         and finds out exactly what is missing, without having to ask
         DONE WHEN  EXERCISED -- such a message has actually been sent and read
         WHY SUPERSEDED  two reasons, either alone sufficient. (1) Its bar waited on a real
                    terminal failure the PRD itself calls rare by design -- "he should almost
                    never receive one" -- so the outcome was written to be proven by an event we
                    hope never happens. (2) Measured 2026-09-10 (row W1-S25): the terminal send
                    CANNOT FIRE AT ALL -- lambda_function.py:439 guards it on
                    (unresolved_doc or {}).get("unresolved") while the renderer writes that
                    document KEYED BY PARTNER, so the guard reads [] and skips the send on a
                    genuine refuse; round 1's proof passed on a fixture built to the docstring
                    rather than to the producer's output. Waiting would have waited forever.
         ACCEPT     if every attempt to fill a gap has failed, including asking
                    the outside provider, Andrew receives an urgent message that
                    lists each day still missing, which partner it belongs to,
                    and which provider the data should have come from -- and he
                    can act on it without a follow-up question. He should almost
                    never receive one; if these become routine, the repair ahead
                    of it has failed, not succeeded
         SOURCE     Andrew-direct 2026-09-02, s.0 ruling (3)
```

**R-EG-4 (ruling, `1.0.0_SA_CTO` 2026-09-10 ~05:1xZ, answering `2.0.0_SA_COO`'s 94998 request for a harder arm THIS TICK): YES -- FOUR CONDITIONS ON EG-s-24, AND THE FIRST IS AN ORDERING.** The cell threads a forcing spec into the render command. CLAUDE.md's NEVER-1 says an override that lets a scheduled producer run off its own inputs creates a NEW REACHABLE STATE the sign-off must cover, and `2.0.0_SA_COO` is right that this one is worse-shaped than the `--month` override that rule was written about: **it makes the monthly report DROP ITS OWN INPUT DATA.** Default-off plus an adversarial arm is necessary and is not sufficient.

**(a) ORDER THE PAIR. EG-s-25 lands BEFORE, or in the SAME deploy as, EG-s-24 -- never after.** EG-s-25 is what makes a forced run record its own forcing (with an unforced run writing the same field with an explicit not-forced value, because a field absent in both cases discloses nothing). If forcing becomes REACHABLE while disclosure does not yet EXIST, there is a window in which a forced artifact is indistinguishable from an organic one -- which is precisely the state this whole cell exists to prevent. That is NEVER-2's half-landed shape applied to a CAPABILITY rather than to a deploy, and it is the one failure here that cannot be repaired afterwards: an artifact written in that window can never be told apart later.

**(b) COUNT THE WRITERS OF THE FORCING SPEC, BY SUBTRACTION.** NEVER-1 requires a writer census on the named property and rule 24 (i) now requires the enumeration be derived as a denominator MINUS exclusions rather than listed from recall. Enumerate every input the render command reads FROM THE COMMAND BUILDER'S OWN SOURCE -- event keys, environment, SSM parameters, any config the renderer opens -- and show which can carry a forcing value. **N writers means N proofs that the scheduled path sets none of them, and N is a number the sign-off PRINTS.** The AST census over the handler's four event keys covers ONE writer; it is not the census.

**(c) PROVE THE SCHEDULED PATH ON THE SCHEDULE'S OWN DEPLOYED PAYLOAD, NOT ON THE CODE.** "The handler cannot read a forcing key" and "the deployed rule does not send one" are DIFFERENT CLAIMS and only the second is about the world. Read the live rule's actual Input, with a POSITIVE CONTROL: a key the payload genuinely carries must read differently from the forcing key it does not. A source read cannot see a payload -- that is the same source-versus-run-log trap this project has now paid for three times in one night.

**(d) THE FORCING MUST NOT BE ABLE TO PERSIST.** Default-off is not the same property as cannot-be-left-on. Prove a forcing value cannot survive into a SUBSEQUENT invocation -- supplied per invocation, cached nowhere, no warm-container residue. A flag that can be left on converts a one-time test into a standing condition, and the artifact that would disclose it is the same artifact nobody re-reads.

**And the never-widen sign-off names the new reachable state IN ITS OWN WORDS** -- *a served monthly report produced over deliberately dropped input data* -- and prints the writer count from (b). This seat's half will say exactly that and will not sign a half that names the producer's decision instead of the act's blast radius.

**R-EG-6 (ruling, `1.0.0_SA_CTO` 2026-09-10 ~06:3xZ, on `2.0.0_SA_COO`'s 95058 and row W4-S6): SHAPE 1 ADOPTED. SHAPE 2 IS REFUSED AND IS NOT GOING TO ANDREW. FWD-9's ACCEPT IS AMENDED SO A DRIVEN RUN CAN SATISFY IT.**

**THE STRUCTURAL FACT, verified at source at this seat and not adopted:** `render_month_end.py:991` classifies from the fixture-mutated in-memory series; `:993` runs the ladder; `:999` RE-CLASSIFIES with `s3=s3` and NO series argument, its own comment saying *"re-classify from REAL current S3 state, never the in-memory series the ladder itself bypassed"*. The fixture never touched S3, so the date returns COVERED, C is 0, and the verdict is PUBLISH. The harness carries its own positive control -- identical fixture, month and probe, the ONLY difference being the flag: `ladder=False` REFUSE C=1 holes `['2026-08-04']`; `ladder=True` PUBLISH C=0 holes `[]` -- so the null is a MEASURED ABSENCE OF EFFECT, not a dead harness.

**FWD-9 as written cannot have BOTH a real ladder and no served write, and that is not a defect in anyone's cut.** It is a property of driving a REPAIR mechanism against a hole you invented: the ladder's function is to repair holes by invoking the producer, and a forced hole is indistinguishable to it from a real one.

**SHAPE 2 IS REFUSED HERE AND NOT CARRIED TO ANDREW, which is a decision and not a deferral.** It rewrites a SERVED daily slice to test a refusal -- NEVER-class, and the `W1-S24` harm BY DESIGN. Asking him to authorise damaging served data in order to demonstrate a guard is a bad trade WHEN A SUFFICIENT NON-DESTRUCTIVE PROOF EXISTS, and one does. Putting it to him anyway would be manufacturing a sovereign call to avoid making a technical one. If shape 1 proves inadequate on evidence, THEN it is his.

**SHAPE 1 ADOPTED with three requirements.** (i) The ladder's absence is DISCLOSED ON THE ARTIFACT, in the SAME field family as `forced: true`, so ONE read tells a reader both what was forced and what was SKIPPED -- `2.0.0_SA_COO`'s own rec, taken as written. (ii) Arm (d) grades THE DISCLOSURE, never the ladder's degenerate outputs. (iii) **THE GRADE CARRIES ITS OWN BOUNDARY:** FWD-9 grades on the GATE's refusal, with the ladder's ORCHESTRATION explicitly NOT covered and its REPAIR MECHANISM covered elsewhere -- `EG-s-19` drove the producer's catch-up against a REAL hole on Andrew's explicit approval, and the ladder's rung 1 invokes that same producer. `2.0.0_SA_COO` stated that boundary precisely rather than claiming the ladder was covered, and I am ratifying the boundary in those terms.

**WHY SHAPE 1 IS SUFFICIENT AND NOT A CONCESSION:** a ladder that RAN and failed to close a hole leaves the re-classification reading the hole still present -- class C, REFUSE -- which is the IDENTICAL code path shape 1 exercises on the identical input state. What `--no-ladder` removes is the ATTEMPT, not the gate. The gate is what FWD-9 is about.

⛔ **AND A DEGENERATE ARM THAT SAYS SO IS WEAKER THAN A REAL ONE AND STRONGER THAN A FORCED ONE NOBODY CAN TELL APART.** That is `2.0.0_SA_COO`'s sentence and it is the principle: a proof that discloses its own gap can be weighed; a proof that closes the gap by damaging the estate cannot be un-run.

**R-EG-5 (ruling, same tick): COMMITTED IS NOT SERVED, and round 3's L10 will not forget it.** `2.0.0_SA_COO` measured THREE `DEPLOYED != BUILT` gaps -- the classifier (EG-s-22), the egress ask (EG-s-23) and the renderer (pending EG-s-25) -- with the deployed bytes hashing EQUAL to their PRE-CHANGE blobs, and each cell says in its own record that its green is a property of the repository and not of the estate. That honesty is exactly right and it does not close the gap. **RULING: no outcome grades REALIZED at round 3's L10 on a repository green.** FWD-4 and FWD-8 each require their fix DEPLOYED and READ, as a measured sha256 pair, with an OWNER NAMED for each of the three deploys.

⛔ **AMENDED ~05:5xZ ON ROW `ETFS_GUARDRAIL-S33`, AND THE AMENDMENT IS TO A FALSE-GREEN RUNG IN MY OWN RULING.** As first written this ruling said "read on the DEPLOYED ARTIFACT", which names the S3 artifact prefix. **S33 measures that an upload to that prefix DOES NOT REACH THE BOX** (asserted from source at `4d666a0939`): `_render_command` copies exactly ONE object from it -- `render_month_end.py` at `:348` -- and the coverage package appears nowhere in the command; the renderer self-bootstraps that package ONLY inside an `except ImportError` branch at `:117-128`, so once `/opt/etfs-reports/coverage/` exists on EBS (which the render command's own text says persists across stop/start) the import succeeds and **the pull never runs again.** So a future upload would make DEPLOYED == BUILT AT THE PREFIX while the RUNNING BYTES STAYED UNCHANGED, and every rung of the ladder I wrote would read CLEAN. **The sha256 pair is therefore measured on the RUNNING PLANE -- the bytes on the box -- and a prefix read closes NOTHING.** This is COMMITTED-is-not-SERVED one level deeper than the law states it: committed, deployed-to-the-prefix and RUNNING are THREE states, not two, and my ruling collapsed the last two exactly as the FWD-5 envelope collapsed EMITTED and READ six hours earlier. **THE LIMIT IS THE ROW'S OWN AND IS KEPT:** the box's on-EBS bytes are UNMEASURED -- reading them needs an SSM command on the reporter box and that plane belongs to a live order -- and the falsifier is exact and written down: if the file is ABSENT on the box the bootstrap does deliver and the row is wrong; if PRESENT it does not. **THE FALSIFIER IS RUN BEFORE ANY DEPLOY CLAIM IS ACCEPTED AT L10**, and no cell is cut for the remedy this tick because it edits `render_month_end.py`, which is a LIVE worker's grant -- `2.0.0_SA_COO` was right to name it as a dependency rather than write into a running worker's surface. A decomposition that covers every code cell can still leave the deploy step unowned; that is how a project passes every criterion while the artifact the estate reads is unchanged. The deploys are placement work, they are placed here, and the L10 grades against them.

**R-EG-3 (measurement-surface fact, recorded by `1.0.0_SA_CTO` 2026-09-10 ~04:2xZ on `2.0.0_SA_COO`'s carried item; NOT a ruling, nothing to remedy): THIS PROJECT'S `daily/` CENSUS DENOMINATOR IS PERMANENTLY +1.** EG-s-19's controlled hole required archiving one slice, and `opal-data-etfs` has **versioning DISABLED**, so that archive object IS the standing rollback for the delete and cannot be removed; the order's bounds forbid a second delete besides. The one enumerator inside this project whose printed denominator already moved (273 -> 274) was ruled INERT on the assignee's own reasoning -- its only arm filters on a `LastModified` prefix of `2026-09-10T01:` and the archive is stamped 03:45:24Z, so the key cannot reach it.

**Why this is written HERE and not only in the message that found it.** It is a fact about the project's measurement surface that OUTLIVES the order that created it: every FUTURE bare-`daily/` census inherits the +1, and a later seat reading 274 against a record that says 273 will be reading a CORRECT number against a STALE one -- a discrepancy that looks exactly like drift and is not. **No remedy is proposed and none should be: the archive must stay.** A census that wants the pre-archive number SUBTRACTS A KNOWN KEY; it never deletes one. This is Rule 28's questions 5 (coverage + denominator) and 7 (a failure mode distinguishable from a genuine negative) answered in advance, for a resource this project is now load-bearing on. The second enumerator the same census found (`estate_report_runner.py:1031`) reads a DIFFERENT bucket and is out of scope, stated with its own denominator: 16 hits across 153,347 files.

**R-EG-2 (ruling, `1.0.0_SA_CTO` 2026-09-10 ~03:3xZ, on `2.0.0_SA_COO`'s 94940 request for PLACEMENT): THE FINDING SPLITS, AND THE HALF THAT IS OURS IS THE DETECTOR, NOT THE DATA.** The COO routed W1-S31 to this seat as "outside ETFS_GUARDRAIL's surface". Half of it is: the partner producer that carries priced values onto closed days is not an OWNS surface and does not enter this project (S20 places it; the remedy leaves as a brief at L1). **The other half is squarely INSIDE** -- s.3 OWNS names *the coverage classifier* in as many words, and S4 is FWD-4's own row against `classifier.py`. A defect in the instrument this project OWNS does not become an outside matter because the data that exposed it came from elsewhere. It goes to round 3 as S19.

**AND THE HALF THAT IS MINE, stated first because it is the one that would have cost a false grade.** FWD-4 was one row from being graded REALIZED on a violation. S16 -- FWD-4's ONLY grading row, written and ratified at this seat -- enumerates `cottonwood or 49financial`, and the four priced rows sit under `inflection`. Its other arm reads the classifier's class A for 2026-09-07, and the class-A branch is precisely the one that returns before it can see a slice. So every arm of S16 would have passed while a closed day carried numbers nobody measured, which is the exact property FWD-4 exists to protect. This is Rule 22's ordering in one row: DISCRIMINATION passing inside a wrong COVERAGE, with a second instrument agreeing about the same wrong thing. It is the FOURTH instance tonight of the uncovered member of a hand-typed domain (`NFRA_OUTSET-S36`, `NFRA_COMPEFFICACY-W1-S2`, the COO's own arm (d), this) and the first one found in an ACCEPT rather than in a worker's arm -- which is worse, because an accept is the thing a grade is read against. **A partner list typed by a human is a DECLARED DOMAIN and must be read from the artifact that owns it.** v0.6 amends both S16 and FWD-4's endpoint ACCEPT accordingly; nothing terminal re-opens.

**R-EG-1 (ruling, binding on this PRD and offered to the spine): NO FWD IS A WAIT.** An endpoint outcome is provable by an act a seat can
take ON DEMAND. An outcome whose only proof is an event nobody controls is written wrong: it is re-cut so its MECHANISM is driven
deliberately, with the organic case kept as the negative arm. Where a wait is genuinely essential it is EXPRESSLY QUALIFIED on the
outcome, with the reason and Andrew's word, and it is the exception that names itself.
