# NFRA_MSBEFF Phase 4 — How agents actually SELECT tools (July), and the S2 inversion

**Andrew's questions (2026-07-23):** comp-which as a % of tool use in July · the architecture
preceding the decision to use it · whether agents lean into comp-tools WITHOUT it · the behavioral
dynamics of selection.

## S2 IS FALSE — and it failed the same way M2 did (third instance of the class, this time inverting a headline)

**Phase 0/1 reported comp-which at <1% of flow. That was an artifact of measuring comp-which in a log
comp-which does not write to.**

| Measurement | July count | Source |
|---|---|---|
| comp-which rows in `compiler-tools-log.md` | **42** | the md log (what I originally measured) |
| comp-which routing invocations | **12,380** | `comp-which-rail.log` ROUTE-family events |
| **Under-report factor** | **295x** | |

**Source-confirmed cause:** `.tools/comp-which` contains **zero** calls to `comp_log_auto.py`. Every
other tool self-reports (`.tools/comp-blast:7` is the pattern). comp-which is the **only major tool
that never appears in its own estate's tool telemetry** — it writes to the rail log instead, and the
two were never joined. `comp_tool_health.py:315` even documents that its catalog "DROPS
ROUTE-POSTERIOR" rows.

**The corrected picture: comp-which is not near-absent — it is the single most-invoked comp surface
in the estate**, at ~12,380 July invocations against 5,033 logged tool RUNS.

## Is it agents asking, or the harness asking for them? — 98% agents

The HUD's PreToolUse pipe does invoke comp-which (`.tools/comp-which:1386`, "the HUD's PreToolUse pipe
filled the flywheel"), so the population needed splitting. Classifying July's 12,380 queries by shape:

- **12,137 (98.0%) natural-language-shaped** — agent-typed questions: *"where does certified_aua come
  from and what serves it to the portal"* · *"where is the cross-firm IAM deny enforced"* · *"Is a
  served value GENUINELY changing, or FROZEN-BUT-FRESH"*.
- **243 (2.0%) shell-fragment/terse** — the HUD-piped tail.

**Agents ask the router constantly, in their own words.** The behavioral layer is far healthier than
Phase 1 concluded.

## THE REAL GAP: routing and running are not linked — conversion is unmeasurable

The rail log records how a RUN was reached (`src=`), and for July:

| src | runs | share |
|---|---|---|
| `direct` | 1,103 | **98.1%** |
| `comp-which` | 21 | 1.9% |

Naively this reads "agents bypass the router." **It almost certainly does not.** The dominant flow is:
agent asks comp-which → reads the recommendation → **runs the recommended tool as its own command**,
which logs as `src=direct` because the run carries no provenance back to the route that produced it.
12,380 routes and 21 attributed runs cannot both describe a fabric where the router is ignored *and*
where agents type 12,137 sincere questions into it.

**So the measurable hole is not adoption — it is that we cannot measure CONVERSION:** did the agent
take the advice, run something else, or run nothing? Nothing in the estate answers that today. This
is the R1/R3 "provenance in the answer" idea pointed at the router: **a route should stamp a
correlation id that the subsequent run carries**, making the router's true hit-rate measurable for
the first time. (New Phase-3 cell, **R8**, below.)

## How agents select tools when they do NOT use the router

Four distinct paths exist; only one of them is instrumented:

1. **Standing memory** — the CLAUDE.md situation→command table + XXX.md per-role minimums load every
   turn. The ~15 workhorses (kuzu 32.5%, pipescript 12.2%, blast 5.1% of July chosen runs) are
   selected from here, by habit, with no router hop. **This is correct and efficient** — a router hop
   for a tool you already know is pure latency.
2. **The HUD nudge** — a PreToolUse hook fires when a Grep/Glob/raw-aws/infra-grep would answer a
   question a comp-tool answers better. Push, not pull.
3. **The rail gate** — hard DENY on estate-grep/raw-aws-inspect, forcing comp-grep or an audited
   override. Coercion, not selection.
4. **comp-which** — pull-based, for the long tail the agent does NOT have memorized. 12,380 July uses.

**The dynamic, stated plainly:** *agents route by memory for the head of the distribution and by the
router for the tail.* That is the right division of labor. 20 of 48 tool-using agents never invoked
comp-which in July — consistent with lanes whose work sits entirely in the memorized head.

## R8 (new cell) — ROUTE→RUN correlation

**Defect:** the router's conversion rate is structurally unmeasurable; `src=direct` conflates "chose
independently" with "took the router's advice." **Remedy:** stamp a route id; have the run carry it
(env var or arg), so route→run is joinable. Also: make comp-which self-report via `comp_log_auto`
like every other tool, so the estate's own telemetry stops omitting its most-used surface.
**Acceptance:** a July-equivalent window reports router conversion rate with a denominator; comp-which
appears in `compiler-tools-log.md` at a count matching the rail log within tolerance.
**Owner:** ~Z specs → 0.8.0 (fits the R1R3 output-contract batch). Not a standard change (additive
telemetry) — but it touches the appender, so it rides the same build.

## What this does NOT change

R1 (coverage visibility), R2 (dataflow), R3 (vintage), R4 (triggers), R5 (key enumeration) stand
unchanged — they were grounded in coverage and trigger evidence, not in the comp-which share. **R7
(comp-which redesign) is re-scoped**: it is not a rescue of an ignored tool, it is a refinement of a
heavily-used one — the argmax-as-confidence defect matters *more* now, because 12,380 queries/month
ride on it.

## Method note (the doctrine earning its keep, third time)

This correction was found by asking "which artifact am I measuring, and what does it structurally
omit?" — the same question that corrected M2 and CVO~Z's census. **Three headline findings in one
program, each wrong for the same reason: a denominator that was its own configuration.** The
instrument that caught all three was not care; it was the habit of naming the denominator out loud.
