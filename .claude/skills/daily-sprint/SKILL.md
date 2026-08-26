---
name: daily-sprint
description: Rewrite Andrew's DAILY SPRINT text (Today Sprint / Projects Item 0-9 / Process Item 0-9 / Blocks) for the day. THE DELIVERABLE IS A HIGHLIGHT REEL, NOT A CHANGE LOG (Andrew-direct 2026-08-26) -- a fix is a WIN and reads like one ("do not narrate the bug, claim the fix"), a build is a WIN, no pedantry (no internal counts, sequencing, lane attribution or partner-irrelevant caveats), and every line ties to the directive's HEADLINER (`title:` in org/missions/DIRECTIVES.yaml) as progress against it -- "for the most part", so a genuine win with no directive to hang on still goes in. Register only, never content: never invent a win; nothing shipped = say so in one line. Grounded on a compiled packet -- comp-state (self-test gated), the git census across BOTH fabrics since 00:00Z, the directives dashboard, open-TO totals, the day's Andrew-direct records, projects closed, ledger entries -- then rewrite yesterday's file into today's in the FIXED template (org/ref/DAILY_SPRINT_TEMPLATE.md) at org/sprints/DAILY_SPRINT_YYYY-MM-DD.md and print it. Bare `/daily-sprint` = today; `/daily-sprint --date YYYY-MM-DD`; `/daily-sprint --packet` = packet only, no rewrite. Andrew-commissioned 2026-08-20 because "we are going to be doing it every single day." Engine `.tools/daily-sprint.py`; MSTR-base primary, any exec may run it.
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
   every Item line is re-stated against today's evidence. **"No movement today" is legitimate and
   is always better than invented progress** (a directive row whose `Last` is yesterday did not
   move) — **but it is the fallback, NOT the target. Look for the win first.** If the day held a
   fix, a build, a decision or a number that got better, **that is the line**; a quiet item gets
   one short sentence and the space goes to the items that moved.
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

- **WRITTEN IN ANDREW'S VOICE (Andrew-direct 2026-08-26 ~21:2xZ, VERBATIM):** *"These have to be
  written in my voice, do not refer to me as im the one who is allegedly saying these things."*
  He pastes the text as HIS OWN channel message — **never write "Andrew ruled/approved/set…"**;
  decisions render as bare outcomes ("Ruled: …", "Approved: …", "Target moved to today") or first
  person where ownership is the point, and a "For Andrew" block renders "**Pending my call:** …".
  The test: read every line as if you are Andrew posting it. Full form + before/after table: the
  template's **THIRD RULE**.
- **HIGHLIGHTS, AND MAKE IT SOUND GOOD (Andrew-direct 2026-08-26).** *"if we fix a bug that sounds
  good, if we build something that sounds good, we do not want pedantic stuff, and we want to tie
  it back to directives.yaml headliner items for the most part."*
  **DO NOT NARRATE THE BUG — DO CLAIM THE FIX.** A repair is delivery and reads as a win; the
  mechanism that produced it does not appear. Confident, plain, active register.
  ⛔ **Register only, never content: NEVER invent a win.** Nothing shipped on an item = say so in
  one line. The rule bites the other way — **when there IS a win, do not bury it in hedging or in
  the machinery behind it.**
  **NO PEDANTRY:** internal counts, sequencing, lane attribution, caveats a partner would not act
  on. Precision lives in the logs and certs; this text is the highlight reel.
  Full rule + worked before/after table: the template's **SECOND RULE, AMENDED**.
- **Tie each line to the directive's HEADLINER** — its `title:` in `org/missions/DIRECTIVES.yaml`
  (*"MDPF asset-category views"*, *"ADVI 49F end-to-end"*, *"Model Portfolios Pipeline
  Fortification"*…). Write the day as **progress against that headline**, in its own words where
  they fit. **"For the most part" is deliberate: a genuine win with no directive to hang on still
  goes in.** The tie is the default, not a filter.
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
