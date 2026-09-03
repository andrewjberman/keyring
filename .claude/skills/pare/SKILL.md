---
name: pare
description: Subtractive editing by PURPOSE, shown before it is done: `/pare <path>` states what the artifact is FOR and renders a PARE VIEW -- a SIGNAL card and a NOISE card with line ranges -- and edits nothing; `/pare <path> go` cuts, exercises with a different instrument, and writes; `--for "<purpose>"` supplies the purpose. Stops at the measured inflection; never a size target; nothing is added or rephrased. Any agent; the invoking seat's lane governs the write.
---

# /pare -- keep the highest-context material, cut the rest, stop at the inflection, show it first

**Purpose (Andrew-direct, 2026-09-03 ~20:4xZ, MSTR terminal, verbatim):** *"I want to make a skill called
/pare which is all about taking the most effective, highest context material and cutting all the rest. can
be used on documents, schemas, scripts, etc. The premise is that a process is enacted where the agent looks
at the subject and says 1.) What is the purpose of this function? 2.) How can I enhance that function
through subtracting clutter? 3.) Based on the purpose of this function, at what point do subtractions
switch from increasing quality to decreasing it?"* -- and, same minute: *"i prefer if the skill contains a
variant of /draw where it surfaces the highest value pieces in a card and also surfaces the noise."* /
*"so i can see it before the cut"*.

`/pare` is the opposite of a rewrite. Nothing is added, nothing is rephrased for taste; material is REMOVED
until only what serves the purpose remains, and the removal stops at a point the record can defend. The
operator sees the SIGNAL and the NOISE side by side before anything is cut.

## Invocation

| Form | Behavior |
|---|---|
| `/pare <path>` | **THE DEFAULT: view only.** Steps 0-3, then the PARE VIEW. **Edits nothing.** |
| `/pare <path> go` | The view, then Step 4: the cut, the exercise, the write. `go` given up front still prints the view above the record. |
| `/pare <path> --for "<purpose>"` | The operator supplies the purpose; the consumer read still runs and a mismatch is surfaced, never silently resolved. Combines with `go`. |

## The three questions, and what an answer to each looks like

| Question | The answer on the record | The failure it prevents |
|---|---|---|
| **1. What is the purpose of this function?** | ONE sentence in the form *"<who> can <do what> from this alone."* Measured from the artifact's CONSUMERS (who reads it, what parses it, what exercises it), never from its title or its author's intent. Two purposes = name the primary and SPLIT the secondary out; never blend. | Paring to a purpose the artifact does not actually serve, so the cuts land on what its real reader needed. |
| **2. How can I enhance that function through subtracting clutter?** | The NOISE card. Each piece carries its line range, its class (table below), the phrase *"the purpose gains ___"*, and where the cut content survives if it must survive anywhere (git history, a ledger, a pointer). A cut that gains nothing for the purpose is preference, not paring, and is not made. | Cutting what you dislike instead of what does not serve. |
| **3. At what point do subtractions switch from increasing quality to decreasing it?** | The SIGNAL card, each piece with *"fails without it: ___"*, and the INFLECTION written BEFORE the edit: *"the next cut would be <X>; it removes <Y>; stop here."* After the edit, the purpose test (Step 4) either passes or the last cut is restored. | Paring past the purpose and shipping a shorter artifact that no longer does its job -- invisible to the author, who still remembers what was cut. |

## What is CLUTTER and what is LOAD-BEARING

The house doctrine already draws this line for rules (CLAUDE.md "Changing this file"): **a rule = imperative +
mechanism + pointer; the incident that taught it is not the rule; never cut a MECHANISM to save space.** `/pare`
applies the same line to every artifact type.

| Type | LOAD-BEARING -- keep unless the purpose itself changes | CLUTTER -- cut, naming where it survives |
|---|---|---|
| Document, rule, protocol | the imperative; its MECHANISM (the gate, tool, path, command); its POINTER; every QUALIFIER that limits, negates or corrects a nearby claim; the NON-APPLICATION clause and the STOP condition; the ONE specimen without which the rule is not actionable; a denominator beside a number; a citation with its vintage | the same rule said twice (keep ONE carrier, name it); incident narrative beyond the one line that makes the rule actionable; dated corrections whose replacement is now the text (git has the history); hedges that change no reader's act; descriptive prose around an authoritative line; options nobody chose; emphasis that repeats the imperative it decorates |
| Schema, contract, enum | every field a CONSUMER reads (enumerate the readers first); the claim/provenance field and its consuming check; the four postulates (Rule 24: MECE over a declared domain, one grain, one intent per axis, state coherence) | a field no reader reads; a retained legacy field that carries the same quantity twice; a value no producer emits; commentary that restates the field name |
| Script, code | every path a test or a real invocation exercises; the guard whose removal a battery would catch; the loud-failure branch; the docstring line that names the CONTRACT | commented-out code; branches no exercise reaches (prove it: the battery, the run log, a call census); duplicated helpers; logging no consumer reads; a flag nobody passes |
| Prompt, skill, persona | the trigger condition; the procedure's ORDER where order is the mechanism; the output shape the consumer parses; the non-application clause; the stop condition; the sibling contract (what this skill is NOT) | rationale that repeats the step; history of prior versions; examples beyond the one that disambiguates; restated house law that CLAUDE.md already binds |
| Message, report | the answer; the denominator; the push state; what is asked of whom | narration of how the answer was reached; hedges; restatement of the question |

**The tell for a mechanism:** if the sentence names a tool, a path, a command, a gate or a check, a reader can
ACT on it -- it stays. **The tell for clutter:** if the sentence could be deleted and the reader's next act is
unchanged, it goes. **A stale pointer is not noise** -- fixing it ADDS a correct name, which paring never does;
it is surfaced in the view's NOTES line for the owner.

## Procedure

**Step 0 -- Identify the subject and pick the instrument.** Read the whole artifact once (a pare from page 1
is a pare of page 1). Then the instrument by type:
- Document / rule / skill / prompt: `comp-read <path> --for "<the purpose as first guessed>"`. AUTHORITATIVE
  regions are SIGNAL candidates, DESCRIPTIVE regions are NOISE candidates, QUALIFIERS are SIGNAL by default,
  CONTRADICTIONS are cuts the purpose demands, and the UNREAD LEDGER is the part not yet judged -- a view
  with an unread ledger is not finished.
- Schema / contract: enumerate the CONSUMERS first (`comp-which "who reads <field or file>"`, then
  `comp-find`); a field is SIGNAL iff a reader is found, and a zero is checked with `--hidden` before it is
  called an absence.
- Script: the battery or exercise that reaches each path (`comp-pipescript io` for a gold script, the test
  module for a tool, the run log for a lambda); `.tools/commit-gate.sh` binds the write as it binds every
  `.py` edit.

**Step 1 -- Answer question 1.** Write the purpose sentence. If the artifact is a record whose purpose IS its
history (Non-application), stop and say so.

**Step 2 -- Answer question 2.** Walk the artifact top to bottom and sort every piece into SIGNAL or NOISE
with its line range. Repetition is cut to ONE carrier and the survivor is named. Two adjacent sentences that
both carry the imperative keep the one that names the mechanism.

**Step 3 -- Answer question 3, then SHOW IT.** Write *"fails without it"* for every SIGNAL piece and the
inflection sentence. Render the PARE VIEW (below) and stop. **This is where a bare `/pare` ends.** The
operator reads the SIGNAL card, the NOISE card and the inflection, and replies `go`, amends a piece ("keep b",
"cut 3"), or does nothing.

**Step 4 -- On `go`: cut, exercise with a different instrument, write.** The purpose test runs on the pared
text, never on memory of the original:
- Document / rule: a cold read for the ACT -- can a reader who has done nothing yet do the thing from the
  pared text alone; `test -f` every path the pared text still names.
- Schema: every reader enumerated in Step 0 still parses (run it, or `comp-transform schema-check`).
- Script: the battery passes and `.tools/commit-gate.sh` passes; a pare that no test can fail is a proposal.
- Skill / prompt: ONE invocation on a real subject, the output read against the output shape.
If the test fails, the inflection was passed: restore the last cut, rerun, record the restoration.
Then the write: in place when the invoking seat owns the lane (`safe-commit.sh -F` with the PARE RECORD as the
message body); otherwise the view goes to the lane's owner and nothing is written. **Never pare another seat's
law text in place** -- CLAUDE.md, XXX.md, doctrine and protocols take the view to their owner.

## Output 1 -- the PARE VIEW (the /draw variant; ASCII only, `+`/`-` frames, ragged right)

Pieces in SIGNAL are ordered by value, highest first; pieces in NOISE by position. Every piece cites its line
range so the operator can look at exactly what sits on each side before the cut.

```
PARE VIEW -- <path> (<type>; <n> lines; <date time>Z)
PURPOSE: <who> can <do what> from this alone.  [derived from <consumers> | --for, checked against <consumers>]

+-- SIGNAL (keep, <k> pieces) --------------------------------------------+
  1. L<a>-<b>  <the piece, quoted or in ten words>
     fails without it: <what the purpose loses>
  2. L<c>-<d>  ...
+------------------------------------------------------------------------+

+-- NOISE (cut, <m> pieces) ----------------------------------------------+
  a. L<e>-<f>  <the piece>  [<class>]
     the purpose gains: <what>  |  survives at: <git history | LD-NNNN | <pointer> | nowhere, and why>
  b. L<g>-<h>  ...
+------------------------------------------------------------------------+

+-- INFLECTION -------------------------------------------------------------+
  the next cut would be <X>; it removes <Y>; stop here.
+------------------------------------------------------------------------+

NOTES: <stale pointers or contradictions surfaced for the owner, or "none">
<n> -> <n-cut> lines.  Reply `go` to cut, "keep <letter>" / "cut <number>" to amend, or nothing.
```

## Output 2 -- the PARE RECORD (on `go`; the commit message when the write is in place)

```
PARE -- <path> (<type>; <before> -> <after> <lines|fields|bytes>; <date time>Z)
PURPOSE: <as in the view>
KEEP (<k>): <the SIGNAL pieces, one line each with "fails without it">
CUT (<m>):  <the NOISE pieces, one line each with class, gain, survives-at>
INFLECTION: <as in the view>
EXERCISE: <instrument> -> <PASS | RESTORED <piece>, then PASS>
WRITE: in place @<hash> | view handed to <owner>
```

## Rules of the discipline

- **Never a size target.** "Cut it to a page" is not a purpose; the inflection is measured from the purpose
  and the artifact is exactly as long as the SIGNAL card.
- **Nothing is added.** A pare that needs a new sentence to hold together has found a cut that was too deep;
  restore rather than write.
- **The view precedes the cut, always.** A `go` is a reply to a view the operator saw; a pare with no view in
  the record is an unexplained deletion, and the next reader restores it.
- **A cut you cannot exercise is a proposal.** Leave it in the view and name the instrument that would test it.
- **Do not pare a record.** See Non-application.

## Non-application

Artifacts whose purpose IS their history or their exact wording are not pared: ledger entries, audit logs,
session logs, verbatim Andrew-direct records, commit messages, ratification records, and any spec or
decomposition that is FROZEN mid-round (CLAUDE.md Rule 27). A pare of a frozen spec is a SCOPE_CHANGE routed
to L2, not an edit. A pare of another seat's law text is a view handed to its owner. A pare of a message
already sent is a second message.

## Provenance and acceptance

Andrew-direct 2026-09-03 ~20:4xZ at the `0.0.0_AB_MSTR` terminal (verbatim above); recorded at creation in
`org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20260903_204xZ_PARE_SKILL_COMMISSION.md`, LD-0533.
Authored by `0.0.0_AB_MSTR`. Accepted on an observed run of the default mode, never on the authoring commit
alone: the first view was `/pare org/tier0_exec/0.0.0_AB_MSTR/README.md` in the authoring session, printed at
the terminal for his `go`.
