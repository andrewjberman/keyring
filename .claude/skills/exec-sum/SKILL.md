---
name: exec-sum
description: Executive STAGE REPORT of a directive, macro, project or the whole fabric in plain language with /draw card frames: what stage, how many steps from done, what done means, one WAITING-ON-YOU line. No TO ids, serials, hashes or tool names in the report body. Grounded each run on telemetry + git and comp-state (self-test gated), never recollection. Read-only. `/exec-sum D2`; loop-friendly.
---

# /exec-sum — the plain-language STAGE REPORT (card-style, loopable)

**Authority (Andrew-direct, 2026-08-28 ~20:2xZ, base CTO terminal, VERBATIM):** after asking *"high
level WHAT STAGE ARE WE AT RIGHT NOW? I do not want to see TO references, I want to see natural
language descriptions of what it is and what stage we're at and how many steps away from completion
we are, and what completion is understood to be, all in plain natural language"* and reading the
reply: *"I like the format, update exec-sum accordingly, except needs more /draw card-style
formatting and clean bullet points."* Record:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260828_202xZ_EXEC_SUM_STAGE_REPORT_FORMAT.md`.
Prior authority (the 2026-08-18 card-first design) stands underneath: the report is GROUNDED, not
recollected; the human-readable half is the deliverable; the instruments are how it is made honest.

> **What this is:** the one-call answer to *"where is this actually at?"* for someone who has not
> been watching. It leads with what the thing IS and what DONE means, then one framed card per
> stage saying where that stage stands in plain words, then a numbered list of the steps still
> between here and done with realistic timing, then the single line that is waiting on the human.
> **What it is NOT:** a status dump, a TO roster, a serial roll-call. Those belong in `/to-check`,
> `/fabric-check`, `/registry-check`. If a sentence needs the fabric's vocabulary to parse, it does
> not belong in the report.

## Invocation forms

| Form | Behavior |
|---|---|
| `/exec-sum <D-code>` (e.g. `D2`, `D3`) | **The primary form.** Stage report for ONE directive: its member projects resolved from the register, its PRD's own DONE definition, its critical-path brief if one exists. |
| `/exec-sum <MACRO>` / `<MACRO_PROJECT>` / `--macro <CODE>` | Stage report for a program or one project (enumerate members from the filesystem, never memory). |
| `/exec-sum` (bare) | Whole-fabric form: one short card per LIVE directive (the D-code, one plain sentence on where it stands, its next step) + one fabric health line. Same grounding. |
| `/loop [interval] /exec-sum <scope>` | Recurring. Each fire leads with a **CHANGED SINCE LAST** block (which stage moved, which step closed) before the current report. |

## Step 0 — Scope + posture

- **Any agent may run it.** READ-FIRST: it reports, it does not drive. The most it does to the
  fabric is ONE surface to the coordinator (COO) -- genuine idle capacity or a genuine record drift.
  Never a lane-dispatch; never manufactured work.
- **Resolve the scope from the register**, never from memory: `python .tools/directives-check.py
  --json` -> the directive's `projects[]`; `org/projects/<CODE>.json` per member; the directive's
  PRD (`docs/architecture/<D>_*_PRD.md`) for the DONE definition; the critical-path brief under
  `docs/briefs/` if one exists (its P-stage list is the stage skeleton). A project scope resolves to
  its own phases/TOs as the "stages".
- **Honor any sovereign hold on a member** (parked / suspended): report it as its own stage card
  in the state it is in; never re-open or re-close.

⛔ **THE ONE NAMING EXCEPTION (Andrew-direct, 2026-09-10, after reading a report that described
NFRA_OUTSET's whole night without ever naming it): "it is ok to mention the macro_project code,
that is an exception."** The DIRECTIVE code (`D11`) and the MACRO / PROJECT code (`NFRA_OUTSET`,
`ADVI_INSURE`, ...) MAY be named anywhere in Parts 1-5, and the report's own header SHOULD carry
them. They are the reader's handle on the thing — without one, a correct plain-language report
leaves him unable to say which of five live programs he just read about, and he has to ask. Nothing
else is admitted by this exception: serials, TO ids, criterion ids, commit hashes, tool names and
fabric jargon stay out of Parts 1-5 and appear once, in Part 6.

## Step 1 — Ground it (the same two instruments, every run)

### 1a. Activity — who is actually working, from telemetry + git (never the broker's prose alone)

```bash
# python only (jq is not installed -- Rule 16). NEVER 2>/dev/null this read.
python - <<'PY'
import json, pathlib
files = sorted(pathlib.Path('org/mcp/agent_telemetry').glob('*.jsonl')); rows = 0
for f in files:
    w = y = None
    for line in f.open(encoding='utf-8', errors='replace'):
        line = line.strip()
        if not line: continue
        try: r = json.loads(line)
        except Exception: continue
        rows += 1; y = r.get('ts') or y
        if r.get('kind', 'work') == 'work': w = r.get('ts') or w
    print(f"{f.stem} work={w} any={y}")
print(f"DENOMINATOR: {rows} telemetry rows scanned across {len(files)} files")
PY
git log --all --oneline --since="30 minutes ago" --pretty=format:"%aI %an %h %s"
```
Then `get_live_agents()`. Classify each LIVE seat ACTIVE / IDLE / STALE / time-gated. **A stale
broker summary + a recent commit = WORKING (git wins).** Only live seats matter; dead historical
serials in the telemetry dir are ignored.

### 1b. Record drift — comp-state, self-test gated

```bash
comp-state --self-test        # MUST print its own N/N PASS line; if not, say so and do not trust 1b
comp-state                    # drift-only; triage: keep only rows whose evidence commits are ABOUT that record
```
Most BEHIND rows are lexical. A real drift (a face/JSON still describing a superseded state) is a
one-line surface to COO, never an edit from this skill.

### 1c. Per-member grounding (the stage cards are built from this, never from memory)

For every member project: `status`, `phase`, `blocking` from its JSON; the last commit touching it;
its open TOs (`python .tools/to-check.py --all --project <CODE>` -- **roster only**; a TO's status
is grounded on its face line, `to-check` mis-renders free-prose `<status>`); the acceptance state
on its proof-of-spec instance where one exists; the PRD's DONE section; the brief's P-stage list.
Cross-check status against phase + commits + faces together -- a "complete" with a live phase, or
an "active" with month-old commits and a finished phase, is drift to name, not a label to repeat.

### 1d. Translate, then check the translation

Map every stage to plain words BEFORE writing: what the stage produces (a noun a reader can
picture), where it stands (done / running / built-not-yet-live / queued-behind-X / waiting on the
human / parked), and the one thing that moves it. Then re-read every sentence and strike anything
that is a serial, a TO id, a criterion id, a hash, a tool name, or fabric jargon ("face", "cell",
"ledger row", "arm-(a)"). Those go to the grounding appendix. **KEEP the directive code and the
macro/project code** — they are the exception above, and the header is where they belong.

## Step 2 — Surface (optional, one message, coordinator-routed)

If 1a-1c found genuine idle capacity on the scope, or a face/JSON still describing a superseded
state, send ONE message to COO and `date -u +%s > org/mcp/.last-stimulus-scan`. Otherwise skip and
say "zero to surface" in the appendix. Never lane-dispatch.

## Step 3 — Render the STAGE REPORT (this order, these frames)

House style = `/draw` framing: ASCII rails only (`+`, `-`, `|`), no box-drawing, no emoji, no
right-edge padding; every bullet ONE line; every card the same shape. **Zero serials, TO ids,
hashes, tool names in Parts 1-5.** They appear once, in Part 6.

```
+=======================================================================+
|  <PLAIN NAME> (<D-CODE> / <MACRO_PROJECT>) -- WHERE THIS IS AT <UTC>  |
+=======================================================================+
   the header CARRIES the codes: the plain name tells him what it is,
   the codes tell him WHICH of the live programs he is reading about.

+-- 1. WHAT IT IS --------------------------------------------------------+
|  - <one plain sentence: the product/outcome, for whom>                   |
|  - <one sentence: how it is produced, in nouns a reader can picture>     |
|  - <one sentence: the check that makes it trustworthy, if one exists>    |
+-------------------------------------------------------------------------+

+-- 2. WHAT YOU SEE TODAY, AND WHY -----------------------------------------+
|  - <what a user of the thing sees right now (empty page? partial data?)> |
|  - <the plain reason, measured: nothing served yet / gate off by design> |
+-------------------------------------------------------------------------+

+-- 3. WHAT "DONE" MEANS (the program's own definition) --------------------+
|  - <half 1, plain words>                                                 |
|  - <half 2, plain words>                                                 |
|  - <any deadline that was set and whether it held; if it slipped, why>   |
+-------------------------------------------------------------------------+

+-- 4. THE STAGES ----------------------------------------------------------+
|                                                                         |
|  [x] STAGE 1 -- <plain name>                     DONE                    |
|      - <what it produced>                                               |
|                                                                         |
|  [>] STAGE 2 -- <plain name>                     RUNNING NOW             |
|      - <where it is, with the one number that matters (e.g. 120/534)>   |
|      - <when it is expected to land, and what could slip it>            |
|                                                                         |
|  [~] STAGE 3 -- <plain name>                     BUILT, NOT YET LIVE     |
|      - <what is built>                                                  |
|      - <the one thing that makes it live>                               |
|                                                                         |
|  [ ] STAGE 4 -- <plain name>                     WAITING ON YOU          |
|      - <the decision, in one line>                                      |
|                                                                         |
|  [ ] STAGE 5 -- <plain name>                     QUEUED BEHIND STAGE N   |
|      - <why it waits, in one line>                                      |
|                                                                         |
|  [p] STAGE 6 -- <plain name>                     PARKED (your word)      |
|      - <the condition that un-parks it>                                 |
+-------------------------------------------------------------------------+
   glyphs:  [x] done   [>] running   [~] built-not-live   [ ] not started   [p] parked/held

+-- 5. STEPS FROM HERE TO DONE ---------------------------------------------+
|  1. <step>                                  -- <when: tonight / tomorrow AM / +N days>  |
|  2. <step>                                  -- <when>                                   |
|  3. <step>                                  -- <when>                                   |
|  ...                                                                                    |
|  REALISTIC READ: <N working days to <milestone>>, assuming <the one named risk>.         |
|  WAITING ON YOU: <the single decision, when it will be askable, or "nothing">            |
+-----------------------------------------------------------------------------------------+
```

**Rules for Part 4 (the stage cards):**
- One card row per stage, in dependency order; the running stage carries the ONE number that
  matters (e.g. `120 of 534 days`) and its expected landing time with the named risk.
- A stage that is built but gated says **what makes it live** in one line -- that is the sentence
  a reader most needs.
- "WAITING ON YOU" is a stage status, not a footnote: if the human's word is what moves it, say so
  on the card.
- Parallel stages are still listed in order; say "runs alongside Stage N" on the bullet.

**Rules for Part 5:** numbered, each step ONE line with a plain "when"; the REALISTIC READ names the
milestone a reader cares about (usually "a page you can look at with real numbers") and the one
risk that would slip it; WAITING ON YOU is a single line (the decision + when it becomes askable).

**Whole-fabric form (bare `/exec-sum`):** one short card per live directive in the Part-4 shape
(D-code + plain name, glyph, one where-it-stands bullet, one next-step bullet), then a single
`FABRIC HEALTH:` line and a single `WAITING ON YOU:` line.

### Part 6 — the grounding appendix (the ONLY place serials / ids / hashes appear)

```
+-- 6. HOW THIS REPORT WAS GROUNDED (for the fabric, not the reader) ---------+
|  register: <k> directive(s) -> <m> project(s); claims scan <n>/<N> JSONs   |
|  telemetry: <rows> rows / <files> files; git: <c> commits in 30 min       |
|  comp-state: self-test PASS <n/n>; real drift: <list or none>              |
|  live seats on scope: <serial: role/state> ...                             |
|  pins behind the cards: <stage -> commit/artifact> ...                     |
|  surfaced to COO: <one line or "zero">                                     |
+----------------------------------------------------------------------------+
```
Every plain-English claim in Parts 1-5 must be traceable to a line here. If a claim has no pin,
one of them is wrong.

## Step 4 — Loop delta (only when looped)

```bash
LAST=$(cat org/mcp/.exec-sum-state 2>/dev/null | head -1)
git log --all --oneline ${LAST:+$LAST..}HEAD --since="45 minutes ago" --pretty=format:"%an %s"
git rev-parse HEAD > org/mcp/.exec-sum-state
```
Lead with a `CHANGED SINCE LAST` card: which stage changed glyph, which numbered step closed, any
new risk. A quiet interval says "no stage moved since <time>" in one line and still prints the
full report (the reader may be cold).

## Discipline / risk notes

- **Plain language or it is broken.** The #1 failure is the draw's jargon in prose. If a reader
  needs to know what a serial, a TO, a "face" or a "cell" is, rewrite the sentence. **The directive
  and macro/project codes are the exception and are NOT jargon here** — they are the name of the
  thing, and a report that withholds them makes him ask "is this NFRA_OUTSET?", which is a question
  the report should never have left open. Measured 2026-09-10: it did.
- **Ground it, never recollect it.** Every card claim comes from Step 1; a report asserted from
  memory is the stale-record failure this skill exists to avoid.
- **comp-state self-test is a gate**; no PASS -> say so, lean on 1a/1c.
- **git wins over the broker summary.** A seat heads-down in a long build reads stale on the
  broker and ACTIVE in git.
- **A deadline that slipped is said plainly, with the reason** (the reader asked "where is this
  at", and a missed date is part of the answer).
- **Read-first.** At most one surface to COO. Never dispatch, never manufacture work.
- **Loop-friendly, idempotent.** Nothing it writes is load-bearing beyond delta display.

## Cross-references

`/draw` (the frame style) · `/open-calls` (the sovereign-decision cards -- Part 5's WAITING ON
YOU line is the same decision, distilled) · `/stimulus-scan`, `/comp-state` (the instruments) ·
`/overview`, `/fabric-check`, `/registry-check`, `/to-check` (the technical status lenses this
report deliberately is not).
