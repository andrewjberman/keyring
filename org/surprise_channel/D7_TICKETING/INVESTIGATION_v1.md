# D7_TICKETING -- SURPRISE CHANNEL INVESTIGATION v1

**Channel owner:** `3.0.0_SA_CVO~Z` · **Round:** v1 · **Opened:** 2026-08-21 ~19:20Z
**Protocol:** `org/ref/SURPRISE_CHANNEL_PROTOCOL.md` (stage 5) · CLAUDE.md Rule 27
**Vintage of every measurement below:** HEAD `940cf8595d` unless a row states otherwise.
**Status:** APPEND-ONLY during this round. A correction is a NEW item citing the prior id, never an
edit in place.

---

## 0. WHY THIS DOC EXISTS AND WHAT IT IS NOT

Stage 3 (atom-decomp) opened on D7_TICKETING at ~19:10Z (`1.0.0_SA_CTO~Z`, msg 4475), with
`2.0.0_SA_COO~Z` as decomp author and this seat as **certifier of record**. This is the channel
that runs concurrently with that execution.

⛔ **THE HANDOVER POSTURE, AND IT IS THE ONE THING THAT MUST SURVIVE INTO THIS RECORD.**
`0.0.0_AB_MSTR~Z` held three items in an interim queue
(`org/tier0_exec/0.0.0_AB_MSTR/deliverables/laneZ_SURPRISE_QUEUE_INTERIM_20260821.md`) and handed
them over at 19:15Z (msg 4478), stating explicitly: **ALL THREE ARE `FILED`. NONE IS `ASSESSED`.**
They parked them; they did not look at them in any sense that counts. That queue file is now
**HISTORY, superseded by this directory** -- one home, not two.

**S1-S4 below are those inherited items plus one from `2.0.0_SA_COO~Z`. S5-S6 are new, found at
this seat during startup assessment.** Where a row reads `GROUNDED`, this seat **re-derived** the
measurement rather than accepting the filer's report -- a relayed self-report does not clear the
grounding bar (protocol section 2), and `0.5.0_AE_OpalETL~Z` explicitly asked to be re-run rather
than trusted (msg 4500).

---

## 1. THE ROUND'S FINDING: THE SAME QUERY IS WRONG IN BOTH DIRECTIONS AT ONCE

Five seats measured `to-check.py --assignee` today. **Every one of them measured only the
direction that REMOVES rows.** On a single TO, at HEAD, the tool simultaneously:

- **MISSES** the true assignees (`0.0.3_BG_BBGTerminal`, `0.5.0_AE_OpalETL~Z`) -- they live in
  `<status>`, which the assignee filter never reads. *This is the filed OBS-1 (S1).*
- **REPORTS** a non-assignee (`0.0.0_AB_MSTR~Z`) **as** the assignee -- because they are named in
  `<issued_to>` as the one who **assigned** it. *This is S5, and nobody had named it.*

The mechanism is one sentence: **`<issued_to>` is PROSE carrying two roles, and a substring filter
cannot separate "assigned BY" from "assigned TO".**

> **The false positive is the worse half** (`0.0.0_AB_MSTR~Z`, msg 4526, self-correcting at the
> same reach as their original broadcast): *an undercount makes you miss work you hold, and it
> announces itself the moment someone notices a leg absent. An overcount makes you believe you
> hold work you do not, and it makes the assigner look like the worker.* **Nobody audits a TO that
> appears correctly in their own list.**

---

## 2. ITEM NARRATIVE

### S1 -- `--assignee` is blind to assignments recorded in `<status>` (inherited OBS-1)

Filed 16:24Z by `0.0.3_BG_BBGTerminal` as a curiosity; moved **INERT -> ARMED** at ~19:12Z when
stage-1 ASSESS started, because ASSESS is exactly the act it breaks. Re-surfaced BLOCKING.

Re-derived at this seat:

```
python .tools/to-check.py --all --assignee 0.0.3_BG_BBGTerminal   -> total=1   (BG holds 2)
positive control  --assignee 0.5.0_AE_OpalETL~Z                    -> total=7   (query WORKS)
negative control  --assignee zzz_no_such_serial_9999               -> total=0   (discriminates)
```

Mechanism, source-confirmed at `.tools/to-check.py` @ `940cf8595d`:
`:140` populates `assigned_to` from the `assigned_to`/`issued_to` tags **only**; `:507` filters
against that field alone; `<status>` is parsed separately at `:143` into `status_raw` and is never
consulted by the filter. **The tool is not broken -- the data is recorded where it does not look.**

**Disarm:** `1.0.0_SA_CTO~Z` Ruling 2 (msg 4507) -- **file enumeration is the standing method for
directive-leg assessment, effective immediately**, and it does not wait on any build.

### S2 -- `teams-watch` deaf duration is agent-activity-dependent (inherited OBS-2)

Filed 16:24Z by `0.0.3_BG_BBGTerminal`: deaf duration = time from token lapse to the seat's NEXT
MCP call; measured **4h (seat idle)** vs **~15s (seat active)**, same day, same mechanism.
Bears on D7's **A1 attended condition**.

⛔ **NOT re-derived at this seat.** Reproducing it requires provoking a token lapse across an idle
window. It is recorded `INFERRED / UNDER_INVESTIGATION` and **cannot seed a remediation row** in
this round (protocol section 2). Carried to `2.0.0_SA_COO~Z` as a decomp input regardless -- an
ungrounded item is still a surface the decomp should enumerate.

### S3 -- `CLIENT_LINK_MAP` populate instruction goes silently wrong at the merge (inherited OBS-3)

Filed 19:12Z by `0.5.0_AE_OpalETL~Z` -- **the first item filed under the new taxonomy, and correct
on first use**: class x standing rather than "latent hazard" as a class, disarm owner named,
disarm and remediation tracked separately.

Re-derived: `infra/aws/terraform/ticket-center/main.tf:278` -> `CLIENT_LINK_MAP = "{}"`. The
disarm is **landed and committed** at `a4b1981cd5` (comment-only, at the config site), and the
comment itself encodes the two-state rule verbatim: *"The empty map is what makes this inert today;
empty is NOT the same as disarmed... DISARMED != REMEDIATED: remediation is the correct repoint at
rollout."*

⚠ **A SCHEMA OBSERVATION ON MY OWN AXIS, recorded rather than silently resolved.** This item is
`INERT` **today** (the map is `"{}"`, it cannot fire) but has a **known arming trigger** -- the
ticket-center merge, which is future *normal* operation. The `hazard_standing` axis as written
evaluates standing at surfacing and has no way to say *"INERT now, ARMS at a scheduled event."*
The filer chose `INERT` and pre-emptively placed the disarm anyway, which is the right behaviour
and is **not expressible in the field**. I am not patching the axis mid-round; it is carried as a
v2 input under Rule 24.

### S4 -- the live directive register has no D8 row (from `2.0.0_SA_COO~Z`, msg 4486)

Re-derived at this seat over `org/missions/DIRECTIVES.yaml`:

```
DENOMINATOR: 9 rows.  CODES: D0 D1 D2 D3 D4 D5 D6 D7 D9.   D8 present: False
```

This fabric's own step-1 instruction names *"D6/D7/D8/D9"*. **I did NOT determine which side is
wrong** -- whether the register is missing a row or the instruction names a directive that does not
exist. The remedy is *reconcile*, not *add D8*. Nothing depends on it today; it does not touch
D7's decomp.

### S5 -- the assigner is reported AS the assignee, live today (NEW, this seat)

```
python .tools/to-check.py --all --assignee 0.0.0_AB_MSTR~Z
  -> RETURNS D6_ANALYST.TO-CDBFG-SITEZ, displayed "-> AB_MSTR~Z"   (total=7)

<issued_to> line 4, verbatim:
  "site Z, seats assigned by 0.0.0_AB_MSTR~Z (multi-workstream -- see the per-row table)"
```

`0.0.0_AB_MSTR~Z` is the **assigner** in that sentence. Their own `total=7` is inflated by a TO
they do not hold. Confirmed independently at the CTO seat on all four measurements (msg 4529) and
self-confirmed by MSTR on their own serial (msg 4526).

**Role census of the one `<status>` block, which is what makes the naive fix dangerous:**

```
DENOMINATOR: 3 distinct serial-shaped tokens, 3 DIFFERENT ROLES, in 1 file
  0.0.0_AB_MSTR~Z        "seats assigned by ..."                  ASSIGNER
  0.0.3_BG_BBGTerminal   "TO-D duty + runtime-exerciser -> ..."   ASSIGNEE
  0.5.0_AE_OpalETL~Z     "build/author rows -> ..."               ASSIGNEE
```

A serial-token sweep over `<status>` -- the obvious implementation of the ruled fix -- **passes the
BG exercise and converts "mentioned" into "assigned" while doing it**, trading a false negative for
a false positive. **Fix C must resolve ROLE, not PRESENCE.**

### S6 -- the acceptance criteria pinned a control to a number the fix was designed to move (NEW, this seat)

The amended criteria (msg 4516) held both:

```
cond 3: "Fix the assignee half: <status> / per-row tables as well as <issued_to>"
cond 5: "positive control --assignee 0.5.0_AE_OpalETL~Z -> 7 must KEEP passing"
```

Measured, and they cannot both hold:

```
<issued_to> line 4 contains 0.5.0_AE_OpalETL~Z      -> 0 occurrences
D6 TO present in AE~Z's current result set          -> NO (not in the 7)
<status> line 8 names AE~Z as an assignee           -> YES
D6 TO is ACTIVE and parses clean                    -> [PENDING], parse_errors=0
```

Condition 3 implemented correctly makes AE's answer **8**. Condition 5 pins it at **7**.
**A correct fix fails the regression control.**

**Disarmed same-turn by `1.0.0_SA_CTO~Z`** (msg 4529), who named the general form better than the
instance: *"A CONTROL OVER A DOMAIN THE FIX DELIBERATELY WIDENS MUST BE EXPRESSED AS A
RECONCILIATION, NEVER AS A CONSTANT."* Condition 5 re-pinned to reconciliation; a **direction-2
exercise** added (`--assignee 0.0.0_AB_MSTR~Z` must NOT return that TO); mutant discipline now
binding on **three** defects.

⛔ **This is S5's consequence, not S5.** They are filed separately because **one remedy does not
move both** (Rule 24(iv)): S5 is repaired by role-resolving code in the tool, S6 by re-wording an
acceptance condition. Different owners, different artifacts, different clocks.

### S7 -- the prevalence bound, narrowed and CERTIFIED (from `0.5.0_AE_OpalETL~Z`, re-derived here)

S1/S5/S6 were filed with `PREVALENCE UNMEASURED` (one file). `0.5.0_AE_OpalETL~Z` had swept it
fifteen minutes earlier while designing Fix C (msg 4535). **They asked to be re-run rather than
trusted, so I ran an independent census with my own corpus definition and my own regex:**

```
                                          AE      CVO~Z (independent)
corpus of TO files                        2,077   2,077        EXACT
<status> contains a serial-shaped token      78      78        EXACT
schema: attribute-form                      106     106        EXACT
schema: child-form                          655     655        EXACT
schema: neither                           1,316   1,316        EXACT
  -- notation split --
TARGET notation  (-> / =>)                    4       3        DIFFERS
ACTOR  notation  (by / per)                  50      53        DIFFERS
OTHER position (UNCLASSIFIED)                 84     100        DIFFERS
```

**The load-bearing claim is CONFIRMED: the ACTOR notation outnumbers the unambiguous ASSIGNEE
notation by an order of magnitude** (AE 50:4, mine 53:3). A token sweep over `<status>` would have
misattributed at ~50-file scale. **That is what makes the re-cut condition 3 -- *resolve ROLE, not
presence* -- the difference between a fix and a fifty-file misattribution, rather than a
refinement.**

⛔ **AND THE DIVERGENCE IS THE SECOND FINDING, not noise.** The **file-level** counts reproduce
byte-for-byte across two independently-written instruments; the **notation split** does not (up to
~19% apart, from different lookbehind windows and per-occurrence vs per-file handling -- my three
buckets total 156 occurrences across 78 files, AE's total 138). **So: the DENOMINATORS are robust
and the SPLIT is an artifact of the classifier.** Two honest implementations disagree on it.
**Nobody quotes the split as precise; quote the direction.**

AE's own bound stands and I am not softening it: **the 84/100 "other" are UNCLASSIFIED BY THE
REGEX, not classified as non-assignments.** Their 7-item sample found a committer, a GO recipient,
a location reference, a serial inside an XML comment, a filesystem path that means nothing -- and
**a genuine re-lane assignee in a notation neither bucket catches.** So the mechanism is grounded
and the rate remains **partial**: the actor notation demonstrably dominates, but **what fraction of
the 78 are true assignments is still unmeasured**, and Fix C is deliberately narrow-and-declared
rather than broad-and-indefensible.

### S8 -- CORRECTION TO S5's OWN SUB-CLAIM, plus the role-less class quantified

**Append-only means a correction is a NEW item citing the prior id (protocol section 1). This one
corrects me.**

**S5 warned that a token-sweep implementation "PASSES the BG exercise" while converting
mentioned -> assigned. AT BG's OWN SERIAL THAT IS FALSE -- it fails loudly.** Measured here,
independently of `0.0.3_BG_BBGTerminal` (who found it) and of `1.0.0_SA_CTO~Z` (who confirmed it):

```
DENOMINATOR: 2,077 TO files scanned under org/**/task_orders/
  files mentioning 0.0.3_BG_BBGTerminal : 13     <- matches BG and CTO~Z EXACTLY
  files ASSIGNING work to them          :  2     (D6 TO-D duty, D7 serve half)
  => a presence-based reader returns 13 against an expected 2: ~6.5x discrimination
```

**So my warning was right in general and wrong about this specific fixture.** The correct
statement: *a token sweep defeats a fixture whose mentions are mostly assignments; BG's serial is
the opposite case, and that is exactly what makes it a STRONG overcount test.* Condition 5's
reconciliation stays pinned at BG's serial. **Nobody weakens it on the grounds that I called it
weak.**

⛔ **AND THE CLASS `1.0.0_SA_CTO~Z` NAMED BUT NOBODY HAD SIZED -- A SERIAL INSIDE A PATH IS A
DIRECTORY NAME.** `org/tier0_utility/0.0.3_BG_BBGTerminal/refs/...` is not an assigner, not an
assignee, **not a role at all.** Measured at BG's serial:

```
total occurrences of the serial across those 13 files : 22
occurrences that are a PATH COMPONENT (role-less)     :  7   (32%)
files where EVERY occurrence is a path component      :  2
```

**Roughly a third of occurrences occupy no role.** Every role frame used tonight -- CTO's
role-not-presence condition, AE's actor/target notation split, and **my own 3-token role census in
S5** -- assumed the serial occupies *some* role. **Path components must be excluded before role
reasoning starts, or the narrow reader inherits a class its own vocabulary cannot express.**

**The C-mutant is a FORWARD GUARD, not a live defect** -- confirmed at this seat: the current tool
returns `OPAL_ANALYST.W6` for BG **0** times, because `<issued_to>` does not name them there. It
becomes reachable only once Fix C reads `<status>` and sibling blocks -- at which point a
presence-based reader converts *"NO new work routes to that seat"* into an assignment. **A fix that
passes every other exercise and fails this one has built the false-positive half of the defect it
was sent to remove.**

---

## 3. WHAT THIS ROUND DOES *NOT* CLAIM

- **PREVALENCE WAS UNMEASURED WHEN S1/S5/S6 WERE FILED, AND IS NOW *PARTIAL* -- SEE S7.** Every
  number in S1/S5/S6 is **one file**, the D6 TO. `0.0.3_BG_BBGTerminal` set this bound on OBS-1
  first (*"OBS-1's denominator is 1 -- my own"*) and it bound my items identically. **S7 narrows it
  and does not close it:** the file-level denominators are certified (78 of 2,077, reproduced
  exactly by two independent instruments), the notation split is a classifier artifact, and **what
  fraction of the 78 are true assignments remains unmeasured.** **A mechanism is grounded; a RATE
  is not.** The fix is justified by the mechanism and sized by the direction, never by the split.
- **The BG/COO root-split is NOT reopened.** `1.0.0_SA_CTO~Z`'s Ruling 1 superseded it. The
  structural half of BG's argument stands (a datum *absent* from a field is not a datum *present
  and unreachable*); only the conclusion moved.
- **`to-check` is NOT a Rule 27 project.** CTO ruled it a defect fix in shared tooling
  (`.tools/**`, lane ANY) -- no decomp, no PRD. These rows record it; they do not wrap ceremony
  around it.
- **This channel gates nothing.** Surfacing is mandatory, holding is prohibited
  (no-inferred-gates law). The build proceeds on the issuer's word, not mine.

---

## 4. MACHINE BLOCK

```json
[
  {
    "id": "D7_TICKETING-S1",
    "surfaced_by": "0.0.3_BG_BBGTerminal",
    "surfaced_at": "2026-08-21T16:24Z",
    "one_line": "to-check.py --all --assignee <serial> cannot see an assignment recorded in a TO's <status> instead of <issued_to>; BG's own D6 leg is invisible to it.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".tools/to-check.py:140 @940cf8595d -- assigned_to populated from assigned_to/issued_to tags only",
        ".tools/to-check.py:507 @940cf8595d -- filter matches that field alone; :143 parses <status> into status_raw, never consulted",
        "re-derived: --all --assignee 0.0.3_BG_BBGTerminal -> total=1, BG holds 2",
        "positive control --assignee 0.5.0_AE_OpalETL~Z -> total=7; negative control zzz_no_such_serial_9999 -> total=0"
      ]
    },
    "disposition": "GRADUATED",
    "disarm_owner": "1.0.0_SA_CTO~Z",
    "notes": "Filed 16:24Z as OBSERVATION/INERT; moved ARMED and re-surfaced BLOCKING at ~19:12Z when stage-1 ASSESS began. Disarmed by Ruling 2: file enumeration is the standing leg-assessment method, effective immediately, not waiting on any build."
  },
  {
    "id": "D7_TICKETING-S2",
    "surfaced_by": "0.0.3_BG_BBGTerminal",
    "surfaced_at": "2026-08-21T16:24Z",
    "one_line": "teams-watch deaf duration equals time from token lapse to the seat's next MCP call -- measured 4h when idle vs ~15s when active, same day, same mechanism.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "INFERRED",
      "evidence": [
        "filer's measurement, BG session log 2026-08-21 sec6 -- NOT re-derived at this seat",
        "re-derivation requires provoking a token lapse across an idle window; not run this round"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Bears on D7's A1 attended condition. Cannot seed a remediation row while INFERRED (protocol section 2). Carried to 2.0.0_SA_COO~Z as a decomp input anyway -- an ungrounded item is still a surface worth enumerating. An open item blocks a zero-graduation close."
  },
  {
    "id": "D7_TICKETING-S3",
    "surfaced_by": "0.5.0_AE_OpalETL~Z",
    "surfaced_at": "2026-08-21T19:12Z",
    "one_line": "CLIENT_LINK_MAP's populate instruction names /submit-request, which retires at the Ticket Center merge, after which the same instruction points at a page double-gated away from every firm -- and resolve_client_link feeds it into a client-facing email.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/terraform/ticket-center/main.tf:278 -- CLIENT_LINK_MAP = \"{}\", re-derived at this seat",
        "disarm landed and committed @a4b1981cd5, comment-only at the config site, plan -detailed-exitcode = 0 per filer",
        "committed comment encodes the rule verbatim: empty is NOT the same as disarmed; DISARMED != REMEDIATED"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "INERT today because the map is empty, but it ARMS at the ticket-center merge -- a known trigger the hazard_standing axis cannot currently express. Filer chose INERT and pre-emptively disarmed anyway, which is right and is not expressible in the field. Carried as a Rule 24 v2 input; axis NOT patched mid-round. Remediation is the correct repoint at rollout, owned by the rollout."
  },
  {
    "id": "D7_TICKETING-S4",
    "surfaced_by": "2.0.0_SA_COO~Z",
    "surfaced_at": "2026-08-21T19:11Z",
    "one_line": "The live directive register carries 9 rows -- D0-D7 and D9 -- and no D8 row, while D8 is named in this fabric's own step-1 instructions.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/DIRECTIVES.yaml re-derived at this seat: DENOMINATOR 9 rows, codes D0 D1 D2 D3 D4 D5 D6 D7 D9, D8 present False",
        "step-1 launch instruction on this fabric names D6/D7/D8/D9"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Which side is wrong is UNDETERMINED -- register missing a row, or an instruction naming a directive that does not exist. The remedy is RECONCILE, never 'add D8'. Nothing depends on it today; does not touch D7's decomp."
  },
  {
    "id": "D7_TICKETING-S5",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-08-21T19:25Z",
    "one_line": "to-check --assignee reports the ASSIGNER as the ASSIGNEE: --assignee 0.0.0_AB_MSTR~Z returns the D6 TO today on the strength of 'seats assigned by', while the real assignees sit unread in <status>.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "--all --assignee 0.0.0_AB_MSTR~Z returns D6_ANALYST.TO-CDBFG-SITEZ displayed '-> AB_MSTR~Z', total=7, measured at HEAD 940cf8595d",
        "issued_to line 4 verbatim: 'site Z, seats assigned by 0.0.0_AB_MSTR~Z (multi-workstream -- see the per-row table)'",
        "role census of that <status> block: DENOMINATOR 3 distinct serial-shaped tokens in 3 roles -- MSTR assigner, BG assignee, AE assignee",
        "independently re-derived on all four measurements at 1.0.0_SA_CTO~Z (msg 4529) and self-confirmed by 0.0.0_AB_MSTR~Z on their own serial (msg 4526)"
      ]
    },
    "disposition": "GRADUATED",
    "disarm_owner": "1.0.0_SA_CTO~Z",
    "notes": "The opposite-direction error five seats walked past -- all of them measured only the direction that removes rows. Mechanism: <issued_to> is prose carrying two roles and a substring filter cannot separate 'assigned BY' from 'assigned TO'. Disarmed same-turn: Fix C re-cut to resolve ROLE not PRESENCE, plus a direction-2 exercise the prior set structurally could not fail. PREVALENCE UNMEASURED -- one file."
  },
  {
    "id": "D7_TICKETING-S6",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-08-21T19:25Z",
    "one_line": "The build's acceptance criteria pinned a regression control to a constant the fix was designed to move: condition 3 (read <status>) makes AE's count 8 while condition 5 requires it stay 7, so a correct fix fails the control.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "issued_to line 4 contains 0.5.0_AE_OpalETL~Z -> 0 occurrences; D6 TO absent from AE's current 7 -> confirmed 0",
        "<status> line 8 names AE as an assignee: 'build/author rows (TO-B/C/E/F/G-scaffold + TO-D build) -> 0.5.0_AE_OpalETL~Z'",
        "D6 TO is ACTIVE and parses clean: --all --project D6_ANALYST -> [PENDING], parse_errors=0",
        "criteria as written at msg 4516 conditions 3 and 5; disarm and re-cut at msg 4529"
      ]
    },
    "disposition": "GRADUATED",
    "disarm_owner": "1.0.0_SA_CTO~Z",
    "notes": "Filed separately from S5 because ONE REMEDY DOES NOT MOVE BOTH (Rule 24(iv)): S5 is repaired by role-resolving code, S6 by re-wording an acceptance condition -- different owners, artifacts, clocks. Caught PRE-BUILD; 0.5.0_AE_OpalETL~Z had not started, so the cost was zero. Issuer's general form: a control over a domain the fix deliberately widens must be expressed as a reconciliation, never as a constant."
  },
  {
    "id": "D7_TICKETING-S7",
    "surfaced_by": "0.5.0_AE_OpalETL~Z",
    "surfaced_at": "2026-08-21T19:22Z",
    "one_line": "The prevalence S1/S5/S6 declared unmeasured: 78 of 2,077 TO files carry a serial in <status>, and the ASSIGNER notation outnumbers the unambiguous ASSIGNEE notation by an order of magnitude -- so a token sweep would misattribute at ~50-file scale.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "filer's sweep (msg 4535): corpus 2077, status-carries-serial 78, target 4, actor 50, other 84; schema attribute 106 / child 655 / neither 1316",
        "INDEPENDENTLY RE-DERIVED at this seat with a separate corpus definition and regex: corpus 2077, status-carries-serial 78, schema 106/655/1316 -- ALL EXACT",
        "notation split re-derived as target 3 / actor 53 / other 100 -- DIFFERS from the filer's 4/50/84",
        "direction confirmed both ways: actor notation dominates target notation by an order of magnitude (50:4 and 53:3)"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "TWO findings. (1) The load-bearing claim reproduces: role-not-presence resolution is the difference between a fix and a ~50-file misattribution, not a refinement. (2) THE DIVERGENCE IS ITSELF A FINDING -- file-level denominators reproduce byte-for-byte across two independent instruments while the NOTATION SPLIT does not (~19% apart; 156 occurrences over 78 files here vs 138 there, from different lookbehind windows and per-occurrence handling). The denominators are robust, the split is a classifier artifact: quote the direction, never the split. The filer's own bound stands unsoftened -- the 84/100 'other' are UNCLASSIFIED, not non-assignments, and their sample found a genuine re-lane assignee in a notation neither bucket catches. Mechanism GROUNDED, rate still PARTIAL. GRAIN, per 1.0.0_SA_CTO~Z: 78 is a FILE count and 138/156 an OCCURRENCE count -- two grains, stated explicitly so no downstream cell inherits one and reasons about the other."
  },
  {
    "id": "D7_TICKETING-S8",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-08-21T19:32Z",
    "one_line": "CORRECTION TO S5's OWN SUB-CLAIM: I warned a token sweep would PASS the BG exercise -- at BG's serial it fails loudly (13 mentions vs 2 assignments, ~6.5x), so that fixture is a STRONG overcount test, not a weak one. And ~32% of occurrences at that serial are PATH COMPONENTS occupying no role at all.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "re-derived at this seat: 2,077 TO files scanned, 13 mention 0.0.3_BG_BBGTerminal, 2 assign work -- matches BG (msg 4542) and 1.0.0_SA_CTO~Z (msg 4545) EXACTLY",
        "occurrence census at that serial: 22 total occurrences, 7 are path components (32%), 2 files are path-component-only",
        "C-mutant is a FORWARD GUARD not a live defect: current tool returns OPAL_ANALYST.W6 for BG 0 times, confirmed at this seat",
        "specimen verbatim, OPAL_ANALYST.W6.guardrails-review.md:66 -- '0.0.3_BG_BBGTerminal -- probe provenance only; NO new work routes to that seat'"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Filed as a NEW item rather than an edit to S5, per the append-only rule -- and it corrects the channel owner. My warning was right IN GENERAL and wrong about THIS fixture: a token sweep defeats a fixture whose mentions are mostly assignments, and BG's serial is the opposite case. Condition 5 stays pinned there; nobody weakens it because I called it weak. THE ROLE-LESS CLASS: every role frame used tonight -- CTO's role-not-presence, AE's actor/target split, and MY OWN 3-token census in S5 -- assumed the serial occupies SOME role. A path component occupies none, and at ~32% of occurrences it must be excluded BEFORE role reasoning starts or the narrow reader inherits a class its vocabulary cannot express."
  }
]
```

---

## 5. ROUND STATE

| | |
|---|---|
| Items | **8** (4 inherited FILED-NOT-ASSESSED, 3 new at this seat incl. one correcting the channel owner, 1 filed post-handover) |
| Graduated | **7** (S1, S3, S4, S5, S6, S7, S8) |
| Under investigation | **1** (S2 -- INFERRED, blocks a zero-graduation close) |
| Dismissed | 0 |
| Decomp-invalidating | 0 |
| ARMED items | **3** (S1, S5, S6) -- **all three DISARMED**, disarm owner `1.0.0_SA_CTO~Z` |
| Remediation | **all OPEN.** DISARMED != REMEDIATED |

**This round CANNOT close.** S2 is `UNDER_INVESTIGATION`, and an open item is not a zero
(protocol section 7). Termination requires a round that graduates nothing and reopens nothing.

**REMEDIATION_v1 is cut at round close and handed to the issuer at completion of the round's TOs**
-- not now. Its rows re-enter at **stage 3** as the next round's decomp inputs, never as TOs
themselves.

-- `3.0.0_SA_CVO~Z`, 2026-08-21, under the ratification of the same day
