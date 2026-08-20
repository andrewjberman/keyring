# DAILY SPRINT TEMPLATE — Andrew's daily status text (fixed format, rewritten every day)

Andrew-commissioned 2026-08-20 (MSTR terminal): *"run comp-state and generally do a scan over the
repo and directives, the work done both by the local fabric and the sitez fabric and rewrite the
attached pasted text... a skill that does that process of assessing progress on the day and
rewrites these things in text because we are going to be doing it every single day."*

**The output is PROSE IN A FIXED SHAPE, grounded on a MACHINE PACKET.** The packet
(`.tools/daily-sprint.py`) is compiled; the sentences are the seat's, and every claim in them
must trace to a packet line, a commit hash, or a record read that day. Rewritten daily as
`org/sprints/DAILY_SPRINT_YYYY-MM-DD.md` (yesterday's file is the base you rewrite FROM).

## THE SHAPE (verbatim structure — keep the headings, the `Item N – Name – text` grammar, the terse register)

```
Today Sprint:
<5-9 one-line bullets: the day's LANDINGS and DECISIONS, highest-consequence first, plain English,
 numbers where they exist ($, counts, times), both fabrics; the last bullet may be a fabric line
 (commits / authors / seats / parity)>
Projects:
Item 0 – Infrastructure – <state + what moved today>
Item 1 – Model Portfolios – <...>
Item 2 – Advisor Intelligence – <...>
Item 3 – Account-Level Model Overlay – <...>
Item 4 – ETF "Positioning" variant – <...>
Item 5 – Alt Research – <...>
Item 6 – Opal Analyst – <...>
Item 7 – Opal Ticketing – <...>
Item 8 – "Philosophy"/modal edits – <...>
Item 9 – Tax SMA Ops – <...>
Process:
Item 0 – <timing> – <status: Unblocked / Dependent on / Sequenced behind / DONE ...>
... Item 1-9 same grammar ...
 
Blocks:
<one line per genuine block: external (whose side, what it gates, self-heal/workaround) or a
 human act only Andrew can do; "none" if none — never pad>
```

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
