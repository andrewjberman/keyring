# Sprint visual system — design session to committed infrastructure (03:45–05:30Z)

**archetype:** IMPLEMENT
**secondary_archetypes:** COORDINATE

Live design session with Andrew at this terminal, end to end: iterated the V6 interactive
prototype through four voice/text feedback rounds, then graduated it into committed
infrastructure (`daily_reports/`) on his word.

## What happened, in order

1. **V6 iteration rounds** (Desktop prototype `Opal_Sprint_V6_Interactive.html`, each round
   render-verified via local http + playwright screenshots before presenting):
   - Round 1: hover affordance (faint indigo) + selected outline; project cards uniform height
     (`grid-auto-rows:1fr`); corner commits/workers lockup removed; brand title tuned; legend
     dots aligned to the first card chip; perf-reporting viz rebuilt as REAL dashboard
     components with sample data; gloss pass on all six SVG generators (drop shadows, tinted
     ground panel, gradients). Mid-round Andrew added: replace the dead stat card with a
     designated **Team Activity** element mapping agents to plain work types.
   - Round 2: card headlines rewritten to FIT WHOLE (his non-negotiable; ~50 char budget) +
     a mechanical guard (shrink max 2px then red-flag, never ellipsize); Team Activity gained
     the second cut — commits BY PROJECT, stable 12-color palette keyed to project number.
     Ruled two stacked bars over side-by-side pies (12 slices unreadable; shared axis).
   - Round 3: **WHO / WHAT / WHERE / WHY** block added to the stage per item — four fixed
     small-caps labels, one line each, B2B touchpoints bold (Cottonwood, 49 Financial, Global,
     Fidelity, dashboard pages), never an individual investor. WHEN deliberately dropped
     (lives in Process + chips).
2. **Graduation to infrastructure (Andrew-direct, recorded verbatim in the deliverable):**
   headline is a STANDALONE feature (kind of day + biggest win / amalgamation — never a sprint
   item); everything rigidly templated; delivered as structured JSON mapped 1:1 to the visual;
   commit types re-derived under Rule 24; all grouped in a `daily_reports/` root.
   - Built: `daily_reports/{README,schema/DAILY_REPORT.schema.json,templates/
     daily_report_template.html,scripts/{render_daily_report.py,commit_census.py},
     data/DAILY_REPORT_2026-08-27.json,out/DAILY_REPORT_2026-08-27.html}`. Renderer validates
     and fails loud (card budget, enums, both team-activity cuts must sum to the commit
     denominator). Template is the V6 design frozen, fully data-driven.
   - **commit_kind enum, Rule-24 record in the README:** axis = AUTHOR SEAT CLASS (mechanical
     first-match on the git author string), which dissolves the build-vs-architecture
     ambiguity Andrew named — the "kind of work" display language is a DECLARED PROXY for seat
     class. 8 values incl. OPERATOR + itemised UNATTRIBUTED residual. DRAFT: word-boundary
     token census + CVO routing is the named open step before any consumer beyond this report.
   - First census run (2026-08-26): **423 commits, 28 distinct workers, 0 unattributed** —
     measured shape was steering-heavy (ARCHITECTURE 104, COORDINATION 94, VERIFICATION 74,
     BACKEND 69, DATA 63, FRONTEND 19), which replaced my illustrative "execution-forward"
     verdict in the shipped JSON. by_project remains claim=inferred until a measured mapper
     exists.
   - `.claude/skills/daily-sprint/SKILL.md` rewritten: step 6 = census -> JSON -> validate/
     render (retires the 08-26 render_sprint.py step, superseded text preserved); new
     "The visual shape" section tells any runner exactly what to author.
3. **The owned-paths gap + Andrew's SoD set-aside:** new root matched no path rule; safe-commit
   refused all 8 files UNDEFINED. Followed the org/sprints/** precedent — queued the grant ask
   to 0.0.0_AB_MSTR (dark, NOT REGISTERED) and surfaced the call to Andrew live. His word,
   VERBATIM: **"you land it, cto should be the writer for this."** Landed
   `daily_reports/** -> TIER0_TIER1_STARTUP_DOCS` (lane reused, not minted) with the set-aside
   recorded in the rule comment; the previously-refused paths then passed the gate — the
   10-min-earlier refusal is the discriminating negative control. MSTR follow-up sent
   superseding the queued ask.

## Commits (all LOCAL on CLOUD; push refused by the LD-0367 integrator-only gate, correctly — they ride MSTR's next integration window; ls-remote UNREAD)

- @bad519ba75 — skill rewrite + ANDREW_DIRECT record
- @5f2e059    — owned-paths grant + record amendment (his verbatim word)
- @dd16d7e07b — the daily_reports/ system + first rendered instance

## ANDREW-DIRECT, OPEN — sourcing process for sprint-item materials (his words at this /log)

> "we need to expand on how the materials are sourced for this, i want to make sure that we
> have a process where when the highest quality sprint items are selected, we actually
> comp-find and scan the logs of the relevant agents involved and actually make sure that
> who what where why is cohesive and tells a story."

What this changes: today the JSON's sprint items are authored from the packet + the runner's
working context. The required process adds a SOURCING PASS between item selection and
authoring: for each selected item, `comp-find` the relevant surfaces and READ the session logs
of the agents who did the work, then write WHO/WHAT/WHERE/WHY from those reads so the four
lines are cohesive and tell one story (not four disconnected clauses). This belongs in the
skill's step 6 (a 6a "source the items" sub-step) + a "sourcing" section in
`daily_reports/README.md`, and the schema could carry a per-item `sources` field (log paths /
records read) so the claim is auditable. NOT YET IMPLEMENTED — next session's first act on
this surface, before or with the first production run.

## Current State (zero-context handoff)

- `daily_reports/` at workspace root is the daily-report system of record; README = the law +
  the commit_kind Rule-24 record. Renderer:
  `python daily_reports/scripts/render_daily_report.py --date YYYY-MM-DD`; census:
  `python daily_reports/scripts/commit_census.py --date YYYY-MM-DD --json`.
- First instance rendered + browser-verified: `daily_reports/out/DAILY_REPORT_2026-08-27.html`.
- Desktop prototypes (`Opal_Sprint_V4/V5/V6*.html`) are now design history; the template is
  canonical. Ownership per Andrew: CTO is the WRITER for this surface (template + schema);
  daily data/out belong to the day's runner.
- Temp http.server on 127.0.0.1:8642 (serves Desktop) may still be running — kill on session
  close.
- Morning set unchanged: allocation unfreeze gates flow-remediation TOs; 12:45Z ADVI AC4 read;
  13:30Z MDPF serve fire on armed arm-(a); charter ratification at Andrew.

## Next Steps

- [1.0.0_SA_CTO] Implement the sourcing pass (comp-find + agent-log reads -> cohesive
  WHO/WHAT/WHERE/WHY, per-item `sources` field) in SKILL.md step 6 + README + schema.
- [1.0.0_SA_CTO] commit_kind ratification: word-boundary token census + route to 3.0.0_SA_CVO
  (R-0006/R-0009 form) before any consumer beyond the daily report.
- [0.0.0_AB_MSTR] Integration window moves @bad519ba75 @5f2e059 @dd16d7e07b; two inbox
  messages (grant ask + its supersession) resolve together.
- [any exec] First production run: tomorrow's /daily-sprint exercises census -> JSON ->
  render end to end.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| commit_census.py (new) | --date 2026-08-26 | PASS — 423/28, 0 unattributed, itemisation branch not exercised (empty residual) |
| render_daily_report.py (new) | --date 2026-08-27 | PASS — validated + rendered 29,381 bytes |
| owned-paths-validate.py | .owned-paths.yaml | PASS — 58 lanes, 253 path rules, all refs resolve |
| safe-commit gate | 3 commits | PASS x3; the UNDEFINED refusal before the grant = live negative control on the new rule |

What worked: render-LOOK-fix loop per /frontend-dev on every design round; the gate refusal
doubling as the grant's negative control. What failed: first commit batch mixed lane-clean and
UNDEFINED paths and the whole batch refused — split batches earlier next time. Gap found: a
new root folder has no path rule by construction; minting the rule belongs in the same act as
minting the folder.
