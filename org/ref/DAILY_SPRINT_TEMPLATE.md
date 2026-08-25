# DAILY SPRINT TEMPLATE — Andrew's daily status text (fixed format, rewritten every day)

Andrew-commissioned 2026-08-20 (MSTR terminal): *"run comp-state and generally do a scan over the
repo and directives, the work done both by the local fabric and the sitez fabric and rewrite the
attached pasted text... a skill that does that process of assessing progress on the day and
rewrites these things in text because we are going to be doing it every single day."*

**The output is PROSE IN A FIXED SHAPE, grounded on a MACHINE PACKET.** The packet
(`.tools/daily-sprint.py`) is compiled; the sentences are the seat's, and every claim in them
must trace to a packet line, a commit hash, or a record read that day. Rewritten daily as
`org/sprints/DAILY_SPRINT_YYYY-MM-DD.md` (yesterday's file is the base you rewrite FROM).

## THE SHAPE (Andrew-direct 2026-08-25 ~2245Z: **"format these with better spacing and bullet points and etc"** -- the Teams-paste render below SUPERSEDES the prior dense form; keep the section order, the item axis and the terse register)

```
**TODAY SPRINT**

<5-9 bullets, each on its OWN line with a BLANK LINE between them ("• " prefix), highest-consequence
 first, plain English, numbers where they exist; the last bullet may be the fabric line>

&nbsp;

---

**PROJECTS**

**Item N — Name**
<the state + what moved today, as a short paragraph under its own bold header -- NOT an inline
 "Item N - Name - text" run-on; blank line between items>

&nbsp;

---

**PROCESS**

| Item | Timing | Status |
|---|---|---|
| N — Name | <timing> | <Unblocked / Held / Sequenced behind / Idle today / DONE> |

&nbsp;

---

**BLOCKS**

• **For Andrew — <subject>:** <the call, and what it gates>

• **Carried, not revisited today:** <items carried from yesterday WITHOUT a measurement today,
  labelled as such -- never restated as if measured>
```

**WHY THE `&nbsp;` AND `---` LINES:** Teams collapses consecutive blank lines, so a bare blank line
between sections disappears on paste and the whole text renders as one wall. The `&nbsp;` holds the
gap and the rule gives the eye a section break. **Andrew pastes this straight into the Opal channel
-- it has to survive the paste, not just look right in the repo.**

## THE FIRST RULE — LAYMAN, SHORT (Andrew-direct 2026-08-20, VERBATIM)

> Something key to mention for the daily sprint skill is that the sprint lines (and descriptions
> in general) must be very short and tailored to be understood by a layman. do not get too deep
> into specifics about microprocesses and aws resources, items that are components of the
> achievement. it is ok to get into detail to the extent that detail directly supports a
> high-level achievement, but it must be written as a short bullet and in laymans terms.

**So:** every line answers "what did we achieve / where does it stand" in words a non-engineer
reads once. NO seat serials, NO commit hashes, NO AWS resource names, NO internal tool names, NO
process vocabulary (no "ferry", "gate", "lane", "tripwire", "mutant", "RAVC"). A number is welcome
when it IS the achievement ($17.8M ingested, 17 accounts, 3 items shipped). A component of an
achievement is mentioned only when the reader needs it to understand the achievement — and then
in plain words ("the fix went live before Friday's run"), never as the mechanism. If a bullet runs
past ~25 words, it is two bullets or it is too deep. **The test: would Andrew paste this line to a
partner without editing it?**

## WRITING RULES (what makes a line true)

- **Items map 1:1 to DIRECTIVES.yaml D0-D9** (the register is the item axis; a RETIRED directive
  keeps its Item line, marked DONE/RETIRED, until Andrew drops it from the text).
- **"No movement today" is a legitimate line** — say it rather than inventing progress
  (`directives-check` Last column = per-row freshness; if a row's last commit is yesterday, it did
  not move).
- **Numbers come from the packet or a cited read** (dollar figures, counts, hashes are fine but
  the text stays readable — hashes only where Andrew would click them).
- **Both fabrics in one text** — site-Z landings are ferried records; cite the ferry/record, not
  a recollection.
- **Blocks are BLOCKS** — an engineering dependency between items is Process, not a Block; a Block
  is external (vendor, feed) or a human act only he can do.
- **Superseded lines get rewritten, not appended** — the file is a snapshot, yesterday's lives in
  yesterday's file.
- **Packet first, prose second** — `comp-state --self-test` must PASS before the packet is trusted;
  the packet prints its denominators (commit count, author count, open TOs, directives live/retired,
  Andrew-direct records, projects closed) and the prose quotes them where it uses them.
