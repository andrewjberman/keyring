# MSTR~Z 0035-0950Z: five distinct staleness shapes in one session, three of them created BY the corrections, and a cross-fabric thread that found the last two

**archetype:** COORDINATE
**secondary_archetypes:** DIAGNOSE, RECORD, VALIDATE

Seat `0.0.0_AB_MSTR~Z`, site Z. Follows `mstrz_startup_bg_tenets_0000-0035Z.md`.
**Reason this log exists beyond convention:** the substance of this window lived in an SQS thread,
and a bus body survives only in a **session-scoped** Monitor output file. The commits carry the
artifacts; nothing carried the synthesis. Writing it is the durability act.

## 1. THE YIELD: FIVE STALENESS SHAPES, AND THE LAST THREE ARE SELF-INFLICTED

| # | shape | instance |
|---|---|---|
| 1 | a doc fell behind its **OWN** source | `XXX.md` + `watcher/SKILL.md` said `inbox-watch.sh` had "no exit path" for **six weeks**. I wrote the 2026-07-14 self-exit myself. `orphan-audit.log`: 85/85 self-exits here, 458/471 on the laptop. |
| 2 | a doc described a **NEIGHBOUR** correctly and the neighbour moved | `teams-watch.py:40` "exactly like inbox-watch.sh" was true when written; the referent gained a self-exit and the sentence began naming the one engine that self-exits as the model for the one that cannot. |
| 3 | a doc **MEASURED ITSELF** and changed the measurement by recording it | my own fix wrote "`ppid` occurrences = 0"; writing it made a whole-file grep return 2. Both hits my prose. |
| 4 | a doc **CITED ITSELF BY POSITION** and moved the positions by existing | the same 37-line insertion shifted six of its own citations by +36. Wrong on landing, inside the commit correcting a stale reference. |
| 5 | a correct NEW paragraph made an OLD paragraph **load-bearing in the wrong direction** | the peer's `PARENT_CHECK=0 at $PPID<=1` composed with two untouched "every healthy wrapper is ppid=1" lines into "the self-exit never fires" — contradicting their own measurement three paragraphs up. |

⭐ **3 and 4 are one family — A SELF-REFERENTIAL RECORD PERTURBS WHAT IT RECORDS** — and both were
TRUE when measured, moments before the write. **5 is the sharpest:** neither paragraph is wrong
alone, the defect exists only in their composition, **it was created by the fix**, and it is
invisible to the author because *the author only diffs what they wrote*. General form, now in the
law: **YOUR DIFF IS NOT YOUR BLAST RADIUS; THE UNIT UNDER TEST IS THE DOCUMENT, NOT THE EDIT.**

## 2. COMMITS (10, all on `origin/SITEZ` @c8baba4336, ls-remote read; zero deploy-scope writes)

`00b47a90c4` BG tenets · `3b4cbd3a24` BG record sweep · `3be9942889` log + retraction ·
`073b1679e2` **law: XXX.md + watcher/SKILL.md** · `8b56a17ad8` latent dependency ·
`627dfb42cb` teams-watch docstring · `892db24b8e` self-referential citation fix ·
`7162ded0dc` **/integrate Steps A+B** · `c8baba4336` **/integrate vintage-disclosure trigger**

## 3. TWO PROTOCOL STEPS THE RECONCILE EARNED

**A — IDENTICAL BASE-SIDE RANGES = ONE DEFECT CORRECTED TWICE. PICK, NEVER UNION.** The table had
only *disjoint→union* and *overlapping→read*. Both fabrics had independently corrected the same
false sentence: `XXX.md` line 336 both sides, `SKILL.md` (43,3) both sides. **Union would stack two
corrections of one defect.** And it needed no law owner — no disagreement about substance.

**B — AFTER PICKING A WINNER, AUDIT THE *LOSING* RENDERING FOR CONTENT.** A wholesale resolution
silently discards whatever only the other side knew, **and nobody is assigned to look, because the
question feels settled the moment a winner is named.** I conceded that CLOUD's text was better, then
audited mine anyway — and found shape 5 in the text both fabrics had just agreed to canonize.
**AUDIT THE LOSER FOR CONTENT; DO NOT DEFEND IT FOR PREFERENCE.**

⭐ **B HAD NO TRIGGER UNTIL the peer supplied one, and their point WAS the missing half of my own
step.** Nothing re-opens a settled question by itself. **The loss is not caused by anyone being
careless — it is caused by everyone being done** (theirs). So: **disclosing a vintage move is an
obligation, not courtesy.** They disclosed a post-assessment commit as routine bookkeeping; that
disclosure sent me back to files I had already conceded and closed; the re-verification carried the
audit; the audit found the defect. **The value was not in the content of the disclosure — it was in
the RE-OPENING.** Credit deliberately unassigned: *neither seat intended the thing that mattered.*

## 4. MY ERRORS THIS WINDOW

- **The three-option framing.** I put a decision to Andrew — free the peer, authorize me, or nothing
  — and **none of my options was "the seat judges it in-scope and does it,"** which is what happened.
  I treated their scope as more binding on them than they did. **Narrowing another seat's sovereign
  scope is the same banned act as widening it**, and I did it in the message where I said I was not
  adjudicating scope.
- **"~43h log retention."** Quoted from my own memory, wrong by ~9x (their oldest entry: 17 days).
  The memory had promoted a true 08-12 measurement to a standing property with *"permanently, by OEM
  design."* **Retention is a RATIO (buffer/rate); both terms drift.** ⛔ **The harm was not a wrong
  number: it MANUFACTURED URGENCY.** Their words — *"that estimate would have justified SKIPPING
  OTHER CHECKS to beat a clock that was not running."* **A stale FACT makes a claim wrong; a stale
  HORIZON distorts what gets checked at all, and the checks not run leave no trace.** Memory
  rewritten to bank inputs + date + RE-MEASURE AT USE.
- **`grep -c` returning 0 exits 1** and killed an `&&` chain mid-verification; and a `git show
  origin/CLOUD:.claude/...` mangled (slashed ref + dot-leading path) so **three "0" counts were a
  broken retrieval, not absence** — caught only by a positive control on the byte count.
- Adding a memory pushed `MEMORY.md` past its load limit (27.2KB vs 24.4KB warn), so entries were
  **silently dropping out of context at session start.** Trimmed to 24,169 B / 146 links / 0 broken.
  **A record that exceeds its own carrier stops being a record, and it fails quiet.**

## 5. STATE AT CLOSE

- **SITEZ: OWNER-CURRENT, DRIVER-EMPTY.** 1 live agent (me), 377-TO floor across 140 projects, six
  directives placed here at ~00:0xZ with **nothing seated**. Every routed seat QUEUED.
- **Register diverged:** SITEZ 9 rows vs CLOUD 12; **D8 absent here though its PRD exists**; D1 still
  reads LAPTOP. Any seat spawned here before the leg runs will not know D8 is theirs.
- **Merge:** overlap 5/1254 = **0.40%**. CLOUD→SITEZ is mine, **gated on Andrew's explicit word**,
  not run. Their gate is `git status --porcelain | wc -l`, red at 252. Resolution pre-agreed: **take
  CLOUD wholesale on both law files; portal is a fast-forward** (`is-ancestor` YES, reverse NO).
- **At Andrew, none blocking:** sitez seating · `0.5.0_AE_OpalETL~Z` dark on six messages holding
  every teams-watch engine item (self-exit port **with** the `:139` fail-open guard; the missing arm
  banner) · the Opal Client Tickets scope question, whose answer now has a recorded dependent.

## 6. COMPILER TOOLS

| tool | use | result |
|---|---|---|
| `git diff --unified=0 $BASE <side>` | conflict classification | **The instrument of the session.** IDENTICAL ranges proved *one defect corrected twice* without reading a hunk |
| `git merge-base --is-ancestor` (submodule) | portal | PASS, both directions tested — the reverse returning NO is what made it a fast-forward |
| `git ls-remote` / `branch -r --contains` | push state, every claim | PASS — never the push report |
| positive control beside every zero | absence verdicts | **PASS, and it earned its place twice**: caught a mangled `git show` and an unwritten temp file rendering three "0"s |
| `.tools/commit-gate.sh` | the `.py` docstring edit | PASS — plus an ASCII guard and a no-code-shaped-line check |
| a `:NNN` guard in my own patch script | refusing self-invalidating citations | **PASS — it fired on ITS AUTHOR**, against my sentence listing the stale numbers as history |
| `grep -c` in an `&&` chain | counting | **FAIL — 0 exits 1.** Use `;` when a legitimate zero is possible |
| `git show 'origin/CLOUD:.claude/...'` | reading the peer's text | **FAIL — MSYS mangle. `MSYS_NO_PATHCONV=1` + never `2>/dev/null`** |
