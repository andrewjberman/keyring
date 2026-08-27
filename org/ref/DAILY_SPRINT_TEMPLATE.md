# DAILY SPRINT TEMPLATE — Andrew's daily status text (fixed format, rewritten every day)

Andrew-commissioned 2026-08-20 (MSTR terminal): *"run comp-state and generally do a scan over the
repo and directives, the work done both by the local fabric and the sitez fabric and rewrite the
attached pasted text... a skill that does that process of assessing progress on the day and
rewrites these things in text because we are going to be doing it every single day."*

**The output is PROSE IN A FIXED SHAPE, grounded on a MACHINE PACKET.** The packet
(`.tools/daily-sprint.py`) is compiled; the sentences are the seat's, and every claim in them
must trace to a packet line, a commit hash, or a record read that day. Rewritten daily as
`org/sprints/DAILY_SPRINT_YYYY-MM-DD.md` (yesterday's file is the base you rewrite FROM).

## THE SHAPE - THE DELIVERABLE IS AN IMAGE (Andrew-direct 2026-08-26 ~23:0xZ; SUPERSEDES every Teams-text formatting rule)

**The sprint is no longer a Teams TEXT post. It is a RENDERED PAGE Andrew drops into Teams as an
image.** His call, verbatim: *"it may actually be better to have this be an image that i output,
there is no reason this should be text and f***ing around with illegible teams formatting."*

⛔ **WHAT THAT RETIRES, COMPLETELY:** the `&nbsp;` gap-holders, the `---` section rules, the
spacer-bullet-carrying-a-non-breaking-space, the no-Markdown-heading rule, the PROCESS table, and
every other workaround that existed only because Teams' renderer collapsed or resized things.
**None of it is law any more.** The reason those rules kept multiplying is the reason they are
gone: each was a presentation constraint living in PROSE, where any reader could "tidy" it away
and silently degrade the next paste. **Presentation now lives in CODE
(`.claude/skills/daily-sprint/render_sprint.py`), where it cannot be tidied by accident.**

### THE SOURCE FILE IS CONTENT, THE RENDERER IS PRESENTATION

Write `org/sprints/DAILY_SPRINT_YYYY-MM-DD.md` as CLEAN MARKDOWN in the four-section shape below.
No spacers, no gap hacks, no layout tricks -- the renderer owns all of that.

```text
TODAY SPRINT

* <highest-consequence outcome first, plain English, one line each>
* <...>
* <THE VOLUME LINE - always last: "N commits across M agents today", plus the operating-scale
  clause where it is true and grounded. FOURTH RULE governs it.>

PROJECTS

* Item N - <the directive HEADLINER name, verbatim from DIRECTIVES.yaml `title:`>

  <what moved today, indented beneath the title, short prose>

PROCESS

* Item N - <same name>
  **Timeline: <when>.**
  Status: <Unblocked / Build complete / Held / Idle by design / ...>

BLOCKED

* <blocked item name>

  <what gates it, and what unblocks it>
```

**ITEM NAMES ARE THE DIRECTIVE TITLES, VERBATIM.** Since 2026-08-26 the register's `title:` fields
ARE Andrew's operating-report names (D0 "Agent Infrastructure (Process Management)" ... D11
"Substrate/Tooling Enhancements"), so the tie-to-the-headliner rule is now a STRING MATCH rather
than a paraphrase. If an item name and its directive title differ, one of them is wrong.

### RENDERING

```bash
python .claude/skills/daily-sprint/render_sprint.py --date YYYY-MM-DD
```

Writes `Desktop/Opal_Daily_Sprint.html` -- ONE self-contained file (no external CSS, fonts or
images, so it renders identically on any box, at any time, offline). Surface it inline with
`SendUserFile` + `display: render`, the same pattern `/to-check` and `/registry-check` use. Andrew
screenshots it into Teams.

⛔ **THE RENDERER MUST NEVER SILENTLY DROP A SECTION.** It parses both the current shape and the
retired table form, and prints its per-section line counts on every run. *Measured on the first
render: PROCESS came out EMPTY because the day's file still carried the retired table, and an
empty section is indistinguishable from an absent one at the reader.* Read the counts line.

⚠ **STATUS PILLS ARE DERIVED, AND DERIVED THINGS LIE QUIETLY.** The PROCESS pill
(ON TRACK / HELD / IDLE / ACTIVE) is classified from the Status text by WORD-BOUNDARY TOKEN
matching, never substring. *Measured on the first render: a substring classifier found "rest"
inside "restore" and "complete" inside "completed" -- stamping IDLE on a shipping item and ON
TRACK on one idle by design.* The pill is the first thing a reader's eye lands on, so a wrong
pill is worse than no pill. Its arms are unit-tested; if you edit the vocabulary, run them.

## TONE AND STYLE - CTO OPERATING REPORT (Andrew-direct 2026-08-26 ~22:5xZ, verbatim)

> *"Write these updates as CTO operating reports: concise, decisive, technically grounded, and
> centered on operating outcomes. The scale of the work should emerge through concrete evidence --
> teams allocated, management layers coordinated, architectural and product decisions made,
> dependencies resolved, controls installed, releases certified, and every action preserved through
> an auditable operating record. The underlying reality is that I am governing a distributed
> technical organization whose active contributor base is larger than the company itself; this is
> organizational design and systems-level execution, not ad hoc querying of a browser AI. Make that
> distinction legible without forcing it into every section or resorting to self-congratulatory
> language. Use the first person for my decisions, approvals, directives, sequencing, and
> accountability, while accurately attributing implementation to the teams and operating structure
> I manage."*

- **SCALE EMERGES FROM EVIDENCE, NEVER FROM ADJECTIVES** -- teams allocated, layers coordinated,
  decisions made, dependencies resolved, controls installed, releases certified, records preserved.
  ⛔ *"without forcing it into every section or resorting to self-congratulatory language"*: the
  scale line goes where it is TRUE and GROUNDED; the rest simply reads like someone who runs an org.
- **FIRST PERSON FOR THE DECISION, TEAMS FOR THE IMPLEMENTATION.** *I* ruled, approved, sequenced,
  cleared, seated, chartered, moved the target. *The teams* built, migrated, certified, delivered.
  "I built it" is as wrong as "the fabric decided."
- **DECISIVE AND TECHNICALLY GROUNDED** -- name the surface, the decision, the outcome. No hedging,
  no mechanism narration, no internal process vocabulary (FIRST + SECOND RULES still bind).
- **THE AUDITABLE RECORD IS PART OF THE OUTCOME** -- it is what makes the scale claim checkable
  rather than boastful.

## THE SECOND RULE — HIGHLIGHTS, NOT A CHANGE LOG (Andrew-direct 2026-08-25 ~2250Z)

> **VERBATIM:** *"need better than this, tell me about the actual work done today on the directives,
> explaining bugs and commit counts and shit doesnt sound good to anybody, we need HIGHLIGHTS, the
> entire point of this is highlights"*

**THE POINT OF THIS TEXT IS HIGHLIGHTS.** Every line answers *what did we DELIVER on this directive
today* — a capability that now exists, a number that got better, **a decision that got made**
(⚠ **the decision is a highlight; the DECIDER is not named — see THE THIRD RULE.** This line
previously read *"a decision Andrew made"*, which instructs the writer to produce the exact phrasing
the voice rule forbids. Amended 2026-08-26 for consistency, not as a new rule.)

⛔ **DO NOT LEAD WITH, AND MOSTLY DO NOT INCLUDE:**
- ~~**Commit counts, author counts, seat counts.** They measure typing, not delivery. **The fabric
  line is CUT** — it was in the shape and Andrew named it directly.~~
  ⛔ **PARTIALLY REINSTATED 2026-08-26 — SEE THE FOURTH RULE.** The volume line is BACK, in ONE
  fixed place: **the final line of TODAY SPRINT**. It is still barred from every other position,
  and counts still never carry an Item line. **Struck rather than deleted so a reader can see the
  cut happened and was narrowed, not reversed wholesale.**
- **Bugs and internal defects AS THE STORY.** A defect belongs in the text only where it changed
  what the business gets — *"release is held on two fixes"* is status; the mechanism of the bug is
  not. **A day narrated through its defects reads as a bad day even when it was a strong one.**
- **Process vocabulary and the machinery of how work is run.**

**THE TEST, applied per line:** *does this tell Andrew something he would want a partner to know?*
If the honest answer is "it tells him the machine is working", cut it.

**AND THE FAILURE THIS RULE CLOSES, recorded because it is easy to repeat:** the packet hands you
denominators (commits, authors, closed counts), and a writer grounding every sentence in the packet
drifts into REPORTING THE PACKET. **The packet is the grounding; the highlights are the deliverable.
Ground on it, then say what got BUILT.**

## THE SECOND RULE, AMENDED — **A FIX IS A WIN. SAY IT LIKE ONE.** (Andrew-direct 2026-08-26)

> **VERBATIM:** *"it needs to be specified that we are looking for highlights and to make shit
> sound good, if we fix a bug that sounds good, if we build something that sounds good, we do not
> want pedantic stuff, and we want to tie it back to directives.yaml headliner items for the most
> part."*

⛔ **THIS AMENDS THE RULE ABOVE AND THE TWO ARE EASY TO READ AS CONTRADICTING. THEY DO NOT.**
The 08-25 rule bars **the MECHANISM of a defect** as the story. This one says **the OUTCOME of
fixing it is a headline.** One sentence settles it:

> **DO NOT NARRATE THE BUG. DO CLAIM THE FIX.**

| do not write | write |
|---|---|
| "a filter was dropping accounts whose parent model was not flagged Opal" | **"Found and fixed a gap that was under-reporting $43.7M of client money in the model views."** |
| "the identity gate refused on a delta beyond rounding tolerance" | **"Our own checks caught it before it reached a client. Fixed same day."** |
| "added a registry entry and tightened a derivation predicate" | **"Fixed today, verified, and serving tomorrow."** |

**WHY THE AMENDMENT EXISTS:** read alone, the 08-25 rule makes a writer *omit* a day whose main
achievement was a repair — and **a fix IS delivery.** A day spent finding and closing a real
problem is a GOOD day and must read as one. **The prior rule stops the text sounding like a
change log; this one stops it sounding like nothing happened.**

### MAKE IT SOUND GOOD — AND THAT IS NOT SPIN

**We did the work. Say so in the register a partner would recognise as a win.** Confident, plain,
active. *"Shipped." "Fixed." "Live." "Caught it before it reached a client."*
⛔ **THE ONE LINE THAT DOES NOT BEND: never invent a win.** Sounding good is about REGISTER, never
about CONTENT — if nothing shipped on a directive, that item says so briefly and moves on. **The
rule is: when there IS a win, do not bury it in hedging, qualifiers, or the machinery that
produced it.** A real achievement written timidly is the failure this rule closes.

### NO PEDANTRY

⛔ **CUT:** counts of anything internal · sequencing and process detail · caveats a partner would
not act on · "which lane did it" · anything that reads as showing the work rather than the result.
**If a clause exists to be precise for an internal reader, it is pedantry HERE** — precision lives
in the logs, the certs and the records. **This text is the highlight reel.**

### TIE IT TO THE HEADLINER — "FOR THE MOST PART"

**Each Item is a directive, and each directive has a HEADLINER in `org/missions/DIRECTIVES.yaml`
(`title:`)** — *MDPF asset-category views · ADVI 49F end-to-end · Account-level model overlay ·
ETF positioning variant · Model Portfolios Pipeline Fortification · Tax SMA ops · Substrate
Analysis*, etc.
**Write the day's line as PROGRESS AGAINST THAT HEADLINE**, in the headline's own words where they
fit. The reader should be able to see *what this directive is for* and *how much closer it got*
without knowing anything else.
**"For the most part" is his and it is deliberate:** if the day's real highlight does not belong to
a headliner — a sovereign decision, a partner-facing outcome, something new that matters — **it
still goes in.** Do not drop a genuine win because it lacks a directive to hang on. **The tie is
the default, not a filter.**

## THE FOURTH RULE — THE VOLUME LINE CLOSES **TODAY SPRINT** (Andrew-direct 2026-08-26 ~21:5xZ)

> **VERBATIM:** *"how many commits over how many agents today? i think that should be the final line
> of the 'Sprint' section"*

**THE LAST BULLET OF `TODAY SPRINT` IS THE VOLUME LINE. Every day. Fixed position.**

```
• 348 commits across 28 agents today.
```

**Register: bare and flat.** It is the scale of the day, not an achievement — no adjectives, no
"impressive", no comparison to yesterday unless the comparison is itself the point.

### ⛔ THIS NARROWS THE 08-25 CUT, IT DOES NOT REVERSE IT

The 08-25 rule cut the fabric line because counts *"measure typing, not delivery"* — **that reasoning
still holds everywhere else.** So:
- **ONE line, LAST, in TODAY SPRINT only.**
- **NEVER in an Item line, never in PROCESS, never in BLOCKS, never as a lead bullet.**
- **A count never stands in for a highlight.** If the day's Item lines are thin, the volume line does
  not compensate — it sits at the bottom and says what it says.

### ⛔ HOW TO COUNT IT, AND THE TRAP THAT MAKES THE SECOND NUMBER SOFT

```
commits: git log --all --since='<DAY>T00:00:00Z' --oneline | wc -l
agents:  git log --all --since='<DAY>T00:00:00Z' --pretty='%an' | sort -u | wc -l
```
**`--all` is load-bearing — it spans BOTH fabrics and every ref.** Without it the count is one
branch's and reads low.

⚠ **THE SECOND NUMBER IS DISTINCT AUTHOR IDENTITIES, NOT A HEADCOUNT OF LIVE AGENTS.** Measured
2026-08-26: `3.0.0_SA_CVO` shows **62** commits of which the base seat wrote **10** — the other 52 are
`~X`'s work **committed under the base author line.** Lanes that commit under a base identity are
INVISIBLE to `%an`, so the number can undercount seats; a seat using two identities would overcount.
**It is the right number for a scale line and the WRONG number to quote as "we had N agents running."**
**Write "across N agents" and never "N agents were running."**

## THE THIRD RULE — WRITTEN IN ANDREW'S VOICE (Andrew-direct 2026-08-26 ~21:2xZ, VERBATIM)

> *"These have to be written in my voice, do not refer to me as im the one who is allegedly saying
> these things"*

**Andrew pastes this text into the channel AS HIS OWN MESSAGE. A line that says "Andrew ruled…" /
"Andrew approved…" / "Andrew set the labels…" reads as someone reporting ABOUT him inside his own
post — absurd on arrival.** Never write his name as the actor.

**HOW DECISIONS RENDER INSTEAD:**
| wrong (third person about him) | right (his voice) |
|---|---|
| "Andrew ruled the client labels himself" | "Set the client-facing labels: …" / "I set the labels: …" |
| "Andrew opened the floodgates: all products drive to done" | "Opening the floodgates: performance reporting, insurance views, … all drive to done this week" |
| "Andrew's Black Diamond decisions unblocked the build" | "The Black Diamond calls are made — advisor keying is settled and the build is unblocked" |
| "waiting on Andrew's look and word" | "ships on my sign-off" / "ships once I've seen the demo" |

**Bare-outcome form is usually better than first person** — "Ruled: …", "Approved: …", "Target
moved to today" — it reads naturally whether or not the reader knows who decided. First person
("I ruled…") is fine where ownership of the call is the point. **The test: read every line as if
YOU are Andrew posting it — any line that mentions Andrew as a third party fails.** This binds the
whole file: Today-Sprint bullets, Item lines, Process cells, and Blocks (a "For Andrew" block
renders as "**Pending my call:** …").

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
