# ENDPOINT (step 2, /endpoint --forward) -- NFRA_IAMROLES202609

**L2 owner + author:** `1.0.0_SA_CTO~Z` · **Run:** 2026-09-09 ~17:1xZ · **Mode:** PHASE 0 (greenfield)
**Project:** `NFRA_IAMROLES202609` · **Directive:** `D12` -- both Andrew-direct 2026-09-09
**archetype:** SCRIBE (spec)

⛔ **NOT YET LANDED IN A PRD.** L3 registration and L4 authoring follow. This file is the endpoint's
durable carrier until pasted VERBATIM under a section titled exactly
`ENDPOINT (step 2, /endpoint --forward)`.
⛔ **AWAITING ANDREW'S `DONE WHEN` CONFIRMATION.** Cut, not ratified.
⭐ **ORDERING SATISFIED:** Andrew ruled *"process the infra report brief first"* (ruling 19). That
endpoint was cut and delta-confirmed at `62881a7369` before this one was begun.

---

## F1 -- THE INPUT

```
brief    docs/briefs/nfra-iamroles202609-least-privilege-brief-20260909.md
vintage  @39b106d036 (AMENDED 17:09Z) -- handed at @ae1edd6aae 17:01Z; clean at HEAD
size     ~23.7 KB / 5 amended hunks read against the handed version
handoff  msg 20530; amendment msg 20533; commissioning handoff @5d9497db65
```

⚠ **THE AMENDMENT WAS VERIFIED HERE, AND ONE OF THIS SEAT'S OWN CONTROLS WAS MIS-SCOPED.** A grep for
`## O<n>` across the diff returned 0 and would have read as *"Part I untouched"* -- **it is not.** It
matches only outcome HEADINGS, and the amendment changed an outcome's BODY (O7, hunk at line 73). The
discriminating reads were `exists only in prose` -> **0** and `.tools/comp-iam-usage` -> **4**.
⛔ And `AND NEVER BUILT` still returns **1** at HEAD -- that is the corrected finding QUOTING the
claim it overturns, not the claim surviving. **Third instance today of a marker matching inside its
own negation; the line number settles it, never the count.**

---

## F2 -- THE CAPABILITY OUTCOMES

⛔ **`FWD-n` IDS ARE PERMANENT AND NEVER REUSED.** These are THIS project's ids, unrelated to
`NFRA_OPSEC202609`'s `FWD-1..19` or to the infrastructure-reporting endpoint's.

```
  FWD-1  Someone can state our least-privilege posture with a number, what it is
         out of, and when it was taken
         DONE WHEN  EXERCISED -- a reviewer has actually answered the question with
                    that evidence attached, rather than an opinion
         ACCEPT     Asked "are we following least privilege?", someone answers with
                    how many things were checked, out of how many exist, and as of
                    when. "Nobody has measured it" stops being the honest answer.
         SOURCE     brief Part I, O1; Part II Owns (the over-grant question, its
                    census and its coverage). Today the coverage is zero of 208

  FWD-2  For any role, a reviewer can see which of its permissions it has never used
         DONE WHEN  EXERCISED -- real roles have been read and their unused
                    permissions named, over a stated lookback
         ACCEPT     Pick any role. A reviewer can see which of the things it is
                    allowed to do it has never actually done, and over what period
                    that was judged.
         SOURCE     brief Part I, O2. ⚠ This is the PERMISSION grain, and F5
                    (corrected) establishes it is the half that is NOT built -- the
                    role-level half already is

  FWD-3  For any policy, a reviewer can see what it REQUIRES of the caller, not only
         what it lets them touch
         DONE WHEN  EXERCISED -- at least one real policy has been surfaced as
                    perfectly scoped and yet requiring nothing of whoever calls it
         ACCEPT     A rule that is careful about WHAT someone can touch but asks
                    NOTHING about who they are or how they proved it is visible as
                    such. Being tightly scoped stops being able to hide asking for
                    no second factor.
         SOURCE     brief Part I, O3; the exhibit is F8. ⚠ Part VII item 5 bounds it:
                    that the estate is broadly silent on this axis is an INFERENCE
                    from ONE policy, never a measured population claim

  FWD-4  Every role we run is either written down in our code or is a recorded,
         owned exception
         DONE WHEN  APPLIED -- each one is either in code or carries a named owner
                    and a reason
         ACCEPT     There is no role running that nobody wrote down and nobody
                    decided to leave out. Something deliberately kept outside the
                    normal way of doing things says who decided that and why.
         SOURCE     brief Part I, O4; Part II Owns. F2/F3: 16 of 208 are governable
                    and undeclared, and are therefore invisible to every check that
                    reads our code
         BOUND BY   brief Part II -- these are TWO remedies, not one. Whether a role
                    should be in code at all is a different question from whether it
                    is over-granted, and a single cell doing both will do one badly

  FWD-5  An engineer can narrow a permission and know beforehand what it would break
         DONE WHEN  EXERCISED -- a real narrowing has been checked in advance and
                    the check was believed
         ACCEPT     Before anyone takes a permission away, they can find out what
                    would stop working -- and be right. Nothing breaks because we
                    tidied up.
         SOURCE     brief Part I, O5; the named failure mode at
                    docs/doctrine/CONTROLS_OVER_CARE.md:512. F11: the live-plane
                    instrument for this already exists

  FWD-6  Anyone can tell whether a past clean-up actually happened
         DONE WHEN  EXERCISED -- each of the known past plans has been established
                    as done or not done, on evidence
         ACCEPT     For work someone planned months ago, a reader learns whether it
                    was finished -- and does not have to guess from which folder the
                    document is filed in.
         SOURCE     brief Part I, O6; F10 -- three such plans exist with unknown
                    status, one of them untouched since February

  FWD-7  A reviewer can tell "this is unused" apart from "we cannot see whether it
         is used"
         DONE WHEN  APPLIED -- the assessment reports the two differently, at
                    permission grain
         ACCEPT     Something nobody has looked at never reads as something that was
                    looked at and found clean.
         SOURCE     brief Part I, O7 (AMENDED at @39b106d036)
         ⛔ DO NOT CUT AS GREENFIELD -- HALF OF THIS IS ALREADY BUILT. The existing
                    tool's own self-test already asserts that never-used is not the
                    same as cold, and it carries an explicit UNKNOWN band, on the
                    ROLE axis. A cell written as new work would re-buy passing,
                    self-testing code. What is missing is the same discipline at
                    PERMISSION grain

  FWD-8  The assessment can be re-run without doing it by hand again
         DONE WHEN  EXERCISED -- it has actually been re-run and produced a
                    comparable answer
         ACCEPT     Someone can ask the same question next quarter and get an answer
                    they can put beside this one. It does not quietly stop happening
                    because only one person knew how to do it.
         SOURCE     brief Part I, O8; F4 -- the closest existing thing is explicitly
                    marked as not schedulable
```

⭐ **EIGHT OUTCOMES FROM AN EIGHT-OUTCOME BRIEF, AND THE UNCOVERED CHECK RAN.** Part II's **Owns**
names four things: the over-grant question and its coverage (`FWD-1`, `FWD-2`, `FWD-8`); the
condition axis (`FWD-3`); declared-vs-live reconciliation and the governance of undeclared roles
(`FWD-4`); and completion evidence for past remediations (`FWD-6`). **All four are covered, so
nothing was added.** ⚠ Stated explicitly because the same check on the infrastructure brief an hour
ago DID find an uncovered Owns item and produced an eleventh outcome -- **a clean result here is a
measured clean, not a skipped step.**

---

## F3 -- BARS

Six **EXERCISED**, two **APPLIED**.

**`FWD-5` is the one where the bar is doing real work.** A pre-flight check that has never been run
against a real narrowing is indistinguishable from one that always answers "nothing breaks" -- and
the failure it exists to prevent is an outage this project caused itself. **`APPLIED` would let the
project ship the exact thing it was commissioned not to do.**

**`FWD-4` and `FWD-7` are APPLIED because they are properties of a state and of a report.** Every
role being in code or carrying a recorded exemption is either true or it is not; a report
distinguishing "unlooked-at" from "clean" is true once it does so.

⛔ **NO INVENTED NUMBERS.** The only figures anywhere are measured ones in `SOURCE` lines (208, 16,
zero-of-208, three plans). **No `ACCEPT` contains a number, a serial, a path, a tool name or any
fabric vocabulary** -- checked line by line, because an acceptance line written in system language
silently becomes a check the builder grades.

---

## F4 -- WHAT LANDS WHERE

**Section title, exact:** `ENDPOINT (step 2, /endpoint --forward)`
**PRD path:** `org/missions/D12/NFRA/NFRA_IAMROLES202609/prd/NFRA_IAMROLES202609_PRD.md`
Project code and directive are both **Andrew-direct and settled** -- unlike the infrastructure
endpoint, this one has no open L3 item. ⚠ The tree grammar's length check still runs at registration
rather than being assumed here.

---

## F5 -- PROVENANCE

```
GROUNDED ON: docs/briefs/nfra-iamroles202609-least-privilege-brief-20260909.md @39b106d036
             (handed @ae1edd6aae; the 5 amended hunks re-read with controls);
             msg 20530 (handoff), 20531 (Andrew ruling 18/19), 20533 (amendment);
             this seat's own live reads of .tools/comp-iam-usage (--help, limits,
             self-test, with a negative-flag control) that produced the correction.

NOT READ, BY DESIGN OF THIS PHASE: the task-order register, org/projects/*.json,
             directives-check, any decomposition. Phase 0 reads the BRIEF and nothing else.
NOT READ, AND IT MATTERS: brief Part VI (STATUS TODAY) is marked NOT OUTCOME-BEARING by
             its author; no outcome is cut from it.
```

**THE LIMITS THE BRIEF DECLARES ABOUT ITSELF, carried forward** (Part VII): the live IAM fleet was
never enumerated by its author and the 208/192/16 split is relayed at a **158.5h-stale** vintage from
a tool that calls itself a detector; **no `simulate-principal-policy` battery was run**, so every
scope statement is read from a document and never exercised; whether the February forty-policy
remediation executed is unknown; **the condition-axis claim is scoped to ONE policy**; and **no claim
whatever is made about Deny policies, permission boundaries, SCPs or session policies** -- a grant
that looks over-broad may be bounded by something no instrument here reads.

⚠ **AND ONE LIMIT THE AMENDMENT ADDED, which bounds this seat's own correction:** `comp-iam-usage`
was exercised only via `--help`, `limits` and `self-test` (all offline). **Its `role-cold`,
`who-can-reach` and `reach-check` modes were NOT run against live AWS by either seat**, so its
coverage at role and applied grain is read from the tool's own output and is **DESIRED, not
EXERCISED**. The tool being built is measured; the tool being *sufficient* is not.

---

## CONSTRAINTS THAT SHAPE THESE OUTCOMES (brief Part V)

- **D1 -- the live plane cannot currently be enumerated.** `comp-find --corpus aws` is BLOCKED and
  **UNOWNED**, and **it is the SAME dependency the infrastructure-reporting brief carries as its D4.
  One instrument, two projects.** `FWD-4` cannot be automated until it is repaired. An L5 observation
  for `2.0.0_SA_COO~Z`: whichever project cuts it first should own it.
- **D2 (CORRECTED) -- the question is no longer whether the instrument exists.** It does. The open
  question is what answers the PERMISSION axis, and **extending a working, self-testing tool that
  already names its own limits is a far smaller act than building one.**
- **D4 -- SETTLED BY ANDREW'S RULING 20, and this endpoint is amended to stop posing it as open.**
  Ruling 18 deferred the instrument fork until the prototype's state was established. **That state
  was established by this seat's L2 correction, not by any project act** -- so the condition was met
  EARLY and the fork became answerable ahead of the project meant to answer it. Andrew then ruled
  (*"rec approved"*, ~17:2xZ, brief amended `@39b106d036` -> `@efe60cf3e5`, PART V D4 only):
  **EXTEND `comp-iam-usage` TO PERMISSION GRAIN; AWS Access Analyzer is the FALLBACK, not the path.**
  Basis: the existing tool already FIXES comp-iam's three Rule-22a limits rather than inheriting
  them, already carries an UNKNOWN band, and is free and in-estate.
  ⛔ **THE PRICING OBLIGATION SURVIVES AS A CONDITIONAL AND MUST NOT BE READ AS DISCHARGED: no
  per-role price is recorded in the ruling, the brief, or any batch.** If Access Analyzer is ever
  taken off the fallback shelf, **pricing it is the FIRST act** and never a figure inherited from
  these records. ⚠ Ruling 20 settles INSTRUMENT DIRECTION only -- it authorises no build, cuts no
  cell and enables nothing.
  ⭐ **CONSEQUENCE FOR `FWD-2`:** its cell is now an EXTENSION of a working, self-testing tool to a
  new grain, not an instrument build. That is a materially smaller act, and `FWD-7`'s
  do-not-cut-as-greenfield clause applies to it for the same reason.
- **D5 -- the remediation must be designed not to cause an `AccessDenied`.** This constrains HOW
  grants are narrowed and is a design input, not a sequencing note. It is why `FWD-5` is EXERCISED.
