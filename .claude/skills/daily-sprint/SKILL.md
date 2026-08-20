---
name: daily-sprint
description: Rewrite Andrew's DAILY SPRINT text (Today Sprint / Projects Item 0-9 / Process Item 0-9 / Blocks) for the day, grounded on a compiled packet -- comp-state (self-test gated), the git census across BOTH fabrics since 00:00Z, the directives dashboard, open-TO totals, the day's Andrew-direct records, projects closed, ledger entries -- then rewrite yesterday's file into today's in the FIXED template (org/ref/DAILY_SPRINT_TEMPLATE.md) at org/sprints/DAILY_SPRINT_YYYY-MM-DD.md and print it. Bare `/daily-sprint` = today; `/daily-sprint --date YYYY-MM-DD`; `/daily-sprint --packet` = packet only, no rewrite. Andrew-commissioned 2026-08-20 because "we are going to be doing it every single day." Engine `.tools/daily-sprint.py`; MSTR-base primary, any exec may run it.
---

# /daily-sprint — the day's status text, rewritten against a grounded packet

**What it is for (Andrew, 2026-08-20):** *"run comp-state and generally do a scan over the repo and
directives, the work done both by the local fabric and the sitez fabric and rewrite the attached
pasted text... a skill that does that process of assessing progress on the day and rewrites these
things in text because we are going to be doing it every single day."*

The deliverable is PROSE in a FIXED SHAPE (`org/ref/DAILY_SPRINT_TEMPLATE.md`), one file per day at
`org/sprints/DAILY_SPRINT_YYYY-MM-DD.md`, rewritten from yesterday's. The packet is machine; the
sentences are yours; every sentence traces to a packet line, a commit, or a record you read today.

## Procedure

1. **Packet first:** `python .tools/daily-sprint.py` (today) — prints the grounding packet and
   scaffolds today's file from yesterday's if absent. **`comp-state` self-test must read PASS**
   in the packet header; if not, say so in the text's fabric line and lean on git + records.
2. **Read the packet's denominators** — commits/authors (both fabrics, all refs), directives
   live/retired with per-row freshness + flags, open-TO totals, the day's Andrew-direct records,
   projects closed, ledger entries. These are the numbers the text may quote.
3. **Read yesterday's file** (the packet names it). Today's text is a REWRITE of it, not an append:
   every Item line is re-stated against today's evidence; "no movement today" is a legitimate and
   preferred line over invented progress (a directive row whose `Last` is yesterday did not move).
4. **Rewrite today's file in the template's exact shape** — headings, `Item N – Name – text`
   grammar, terse register, Today-Sprint bullets highest-consequence first, Blocks = genuine
   external blocks or human-only acts (an inter-item dependency is Process, not a Block).
   **THE FIRST RULE IS LAYMAN + SHORT (Andrew-direct, verbatim in the template): very short
   lines a non-engineer reads once; no serials, hashes, AWS resource names, tool names, or
   process vocabulary; a component of an achievement appears only when the reader needs it, in
   plain words; ~25 words per bullet. The test: would Andrew paste the line to a partner
   unedited?** The packet is the GROUNDING, not the prose — translate it, never transcribe it.
5. **Cross-fabric:** site-Z landings come from ferried records at parity (cite the record/commit);
   the packet's `--all` git census already covers both branches.
6. **Commit** the day's file under your author line (`safe-commit`), then **print the text** in
   the terminal — Andrew copies it into the Opal Teams channel.

**TEXT ONLY, by design (Andrew-direct ~2105Z, VERBATIM):** *"there are two skills involved here.
/directives-check which is for me internally and shows the current state of directives + creates a
render for visible analysis. Then there should also be /daily-sprint which essentially is just a
formatted text version i can copy/paste of directives-check for the Opal teams channel."* The
visual render lives in `/directives-check`; this skill produces the copy/paste text and nothing
else.

## Forms

| Form | Behavior |
|---|---|
| `/daily-sprint` | packet + scaffold/rewrite today's file + print |
| `/daily-sprint --date YYYY-MM-DD` | same for a named day |
| `/daily-sprint --packet` | `daily-sprint.py --packet-only` — grounding only, no file |

## Discipline

- The packet gates the prose; never write a number the packet or a cited read does not carry.
- Items map 1:1 to `org/missions/DIRECTIVES.yaml` D0-D9; a RETIRED directive keeps its Item line
  marked DONE/RETIRED until Andrew drops it from the text.
- Yesterday's file is never edited; today's is the snapshot.
- Compiler Tools line in your session log: `comp-state` (self-test N/N) + `directives-check` +
  `to-check` via the packet.

## Cross-references

Engine `.tools/daily-sprint.py` · template `org/ref/DAILY_SPRINT_TEMPLATE.md` · first instance
`org/sprints/DAILY_SPRINT_2026-08-20.md` · siblings `/exec-sum` (card+draw, whole-fabric),
`/directives-check` (the register dashboard), `/comp-state`.
