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
- **Commit counts, author counts, seat counts.** They measure typing, not delivery. **The fabric
  line is CUT** — it was in the shape and Andrew named it directly.
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
