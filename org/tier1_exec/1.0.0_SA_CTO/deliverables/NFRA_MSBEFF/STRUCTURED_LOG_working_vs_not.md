# NFRA_MSBEFF — Structured log: what was working, what was not (agents' own words)

**Source:** 649 verified findings mined from the session-log `## Compiler Tools` corpus by a
10-agent fanout under `RUBRIC.md`. **Partial: 5 of 10 chunks landed** (01/03/04 complete, 08/09
partial) before the account spend limit stopped the fleet — chunks 02/05/06/07/10 pending
(`FANOUT_STATE.md` carries the relaunch). **Audit control PASSED: every one of 649 quotes verified
as a verbatim substring of its source log (0 fabricated rows; 610 exact, 39 ASCII-transliterated).**
Full provenance per finding (source path, serial, date, quote) in `findings_merged.jsonl`.

## The headline the corpus states in the agents' own words

**The framework's problem is COVERAGE and TRIGGERS, not correctness.** When a tool runs on something
it models, it works and agents say so (145 WORKED). The failures cluster on the tool answering about
a **smaller world than the question assumed** (227 FAILED_COVERAGE — 35%, the largest class) and on
**capability that exists but no one reaches for** (15 SUBSTITUTED + the trigger gaps). This is your
"truly understanding state and dependencies" thesis, measured.

## By layer (649 findings)

| Layer | Findings | What it says |
|---|---|---|
| MECHANICAL | 525 (81%) | Dominated by FAILED_COVERAGE (227): the graph/manifest/config doesn't cover the target. Real crashes (FAILED_TOOL 36) are a minority. |
| SEMANTIC | 90 (14%) | comp-which MISROUTE is the signature (19 of its 27 findings); the router can't route what no tool covers, and its argmax-as-confidence defect is observed live. |
| BEHAVIORAL | 34 (5%) | Small COUNT but high stakes — SUBSTITUTED (15) is agents bypassing a fitting tool ("typecheck sufficient", "went straight to build"), plus the zero-trigger gaps from Case Study 1. |

## MECHANICAL — the coverage boundaries agents hit repeatedly (verbatim)

- comp-pipescript is the highest-volume complaint (74 FAILED_COVERAGE of 111): *"comp-pipescript
  deployed is bd-tree/.py-scoped — inf gold .sh dispatch scripts are UNCOVERED... had to hand-roll
  an S3 sha256"* · *"structurally blind to etf_netassets_watch/"* · *"missed the dynamic-prefix
  holdings read"* (the AST extractor can't see dynamically-keyed I/O — a deep, recurring one).
- comp-blast: *"the graph indexes only 23 COMPONENT nodes, missing the whole market-performance
  dir"* · *"comp-blast does not resolve shell-script callers"* (37 of 52 coverage).
- comp-iam: *"parses TF = DESIRED only and is structurally blind to AWS-managed and unmanaged
  grants — which is the finding under test"* (the Rule-22a limitation, felt in the field).
- comp-freshness: *"cannot do a forensic mtime-vs-key-date sweep to detect in-place rewrites"* ·
  *"lacks an arbitrary/raw-prefix mode (the recurring aws_freshness override)"*.

## SEMANTIC — the router can't route what isn't covered (verbatim)

- *"comp-which has no clean route for a 'is this infra build materialized / live?' project-state"*
- *"no exact tool for EventBridge rule enable-state"* · *"pre-fix: pointed at a command that did
  not exist"* · *"role-resolve isn't directly comp-which-discoverable"*.
- The healthy case, also in the corpus: *"all-zero-ish score vector, near-tie... correctly REFUSED
  to guess and routed to comp-grep. The argmax-as-confidence defect ~Z is redesigning, observed
  live."* — the router fails safe, but the miss is a coverage miss surfacing as a routing miss.

## BEHAVIORAL — where agents chose not to reach (verbatim)

- *"authoring 4 TOs without running comp-blast first is a process miss vs the COO mandate"*
- *"the session was inbox-triage-driven... I went straight to build without comp-* checks"*
- *"comp-transform schema-check not run this session — typecheck-only gate sufficient"* (recurs — a
  fitting tool judged redundant against a cheaper habit).
- Plus Case Study 1's zero-trigger gaps: comp-state 0 runs during a live registry drift;
  dump_enriched_templates never run in 4 months.

## The NAMED GAPS the agents themselves filed (signal-3, verbatim — these are the ask list)

- *"the estate has no generator for a new Opal data pipeline / partner firm (the #1 archetype gap)"*
- *"no comp-tool answers 'what is the live ALB/perimeter shape of this host?'"* (comp-routes
  perimeter / comp-aws alb — filed + approved)
- *"comp-* cannot answer a DATA-FLOW question ('does this assign a value that did not come from the
  canonical source?')"* — **this is Andrew's exact "understand state and dependencies" gap, named by
  an agent 07-13.**
- *"no comp-tool enumerates per-table partition dates"* · *"comp-freshness lacks a raw-prefix mode"*
  (= the CS1-4 rail-override demand signal, corroborated from the NL side)
- *"output-key COLLISION (2+ producers -> one sink)... comp-dups scans code bodies, not write
  targets"* · *"no deploy check verifies a lib IMPORTS"* · *"the compiler-graph doesn't model
  field-threading at the typed-shape boundary"*.

## What WORKED (145, so the wins are on record too)

comp-grep (14/19 WORKED), comp-kuzu provenance-header currency checks, comp-freshness when pointed
at a modeled prefix, and the rail failing safe. The pattern: **tools win decisively inside their
coverage and lose silently at its edge** — which is why making coverage *visible at query time* is
the highest-leverage semantic fix.

## Feeds Phase 3

The ranked remedy list draws directly from the signal-3 named-gaps above + Case Study 1's cross-cuts
(CS1-1 triggers, CS1-2 coverage-invisible-at-query-time, CS1-3 vintage, CS1-4 rail demand). The
partial (5/10 chunks) is sufficient to rank; the remaining chunks refine frequencies, not direction.
