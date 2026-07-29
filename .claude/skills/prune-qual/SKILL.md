---
name: prune-qual
description: The PROSE half of the prune pair (sibling: /prune-quant for code/pipelines/mechanisms). Apply to a PRD, proposal, design doc, rule, skill text, or any written artifact: "what is actually the PURPOSE of this thing, and how do we get there cleanly -- without being verbose and tacking on a bunch of bullshit?" (Andrew-direct 2026-07-29, verbatim premise). Purpose-first: state what the reader must be able to DO, then every clause survives only by serving that. Report + optional rewrite skeleton; the owner lands the edit.
---

# /prune-qual — what is this FOR, and how do we get there cleanly

**The pair:** `/prune-qual` is for things that are READ (PRDs, designs, docs, rules, skills-as-text).
`/prune-quant` is for things that RUN. Both start from the same question — material value — but a
document's value has exactly one root: **what it makes its reader able to do.**

**Invocation:** `/prune-qual <target>`. Output = the report below, optionally with a rewritten
skeleton. The owner lands the edit (for law files like CLAUDE.md, the file's own change rules bind).

## The method

**1. WRITE THE PURPOSE SENTENCE FIRST — one sentence, do-shaped.** *"This document exists so that
<who> can <do what> at <which moment>."* If you cannot write it, THAT is the finding: the document
has no purpose or has several fused together (split it, don't polish it). Everything after this
step is testing clauses against this sentence.

**2. NAME THE READER AND THEIR MOMENT.** A fresh implementer at execution time? A ruler deciding?
A future agent mid-incident? Every kept sentence is written to THAT reader at THAT moment — not to
the author's memory of writing it, and not to a reviewer who already knows the story.

**3. THE ACT TEST, per clause:** *would the named reader DO anything differently if this clause
vanished?* No → decoration; cut it, or demote it to a one-line pointer if the detail must remain
findable. Yes → keep, and keep WHOLE — never cut the mechanism that makes an instruction obeyable
(a bare prohibition loses to the reader's own instruments).

**4. THE SCAR IS NOT THE RULE.** The incident that taught a lesson justifies the rule; it is not
the rule. Imperative + mechanism stay in the document; the incident history, the measured numbers,
the who-caught-what move to a pointer (references/ledger). One paid-for example may stay ONLY if it
is the mechanism's clearest statement. (House precedent: Rule 22a went from 11,016 words to a
clause + two pointers, losing nothing an implementer acts on.)

**5. ONE HOME PER FACT.** A fact stated in two places WILL drift and the stale copy will speak with
authority. Keep each fact in its authority home; everywhere else points. Hand-copied counts,
restated tables, and quoted-from-memory rules are the recurring offenders.

**6. KILL THE VERBOSITY PATTERNS by name:** throat-clearing preamble; restating the ask back;
hedge-stacks ("may potentially, in some cases"); three examples where one carries; synonym chains
("clear, clean, and simple"); defensive completeness (clauses answering objections nobody raised);
importance-inflation (bold/caps on things the act test just failed). Cutting these is not editing
tone — each one costs every future reader attention that belongs to the load-bearing clauses.

**7. THE EXIT BAR:** hand the pruned version to the step-2 reader cold. If they can do the purpose
sentence without the cut material, the prune held. Judge by THAT test, never by word count — a
short document that lost its mechanism failed; a long one that passes every act test is done.

## Report format

```
# PRUNE-QUAL: <target>
PURPOSE: <the one do-shaped sentence — or "UNSTATEABLE: <why>, split proposed">
READER/MOMENT: <who, when>
| section/clause | verdict | why (act test) |
KEEP    <clause>  -- reader acts on it: <how>
POINTER <clause>  -- detail moves to <home>, one line remains
CUT     <clause>  -- decoration class: <which pattern from step 6>
NET: <words before -> after; what the reader can still do (the exit bar, stated)>
```

## Notes
- Report-first; the owner lands the edit through their lane's normal gates.
- Self-application: this file obeys its own act test. If a step here fails it, cut the step.
- Premise verbatim (Andrew-direct 2026-07-29): *"what is actually the purpose of this thing and
  how do we get there cleanly without being verbose and tacking on a bunch of bullshit."*
