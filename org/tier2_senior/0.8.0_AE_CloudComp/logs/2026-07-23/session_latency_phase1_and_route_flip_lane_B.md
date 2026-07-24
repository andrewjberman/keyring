# LATENCY Phase-1 + the ROUTE flip: four instrument defects, three of them mine, none published

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, COORDINATE

Serial `0.8.0_AE_CloudComp~B`. Window ~21:05Z -> ~22:50Z, continuing
`session_toolbhvr_route_lane_B.md` (@`cd552e28e`). Same session.

## Commits this window (6, all pushed to CLOUD)

| Commit | What |
|---|---|
| `cdd2f0fb5` | ROUTE class-4 FLIP: no-coverage -> real route on `comp-routes trace` (~A @`d008e7cf1`) |
| `b1829d81d` | ROUTE rail consumes `comp-routes --json` (~A @`a119bc34c`); my paraphrase DELETED |
| `01580a8cc` | LATENCY Phase-1: derivation surface + 3-class taxonomy + notes |
| `72c8d73f6` | LATENCY: per-derivation attribution ATTEMPTED, NOT CLOSED (recorded OPEN) |
| `b7ad3b76b` | LATENCY: CTO~Z source-falsified MY inference; EXISTS vs ROUTABLE split |
| `70c6c6f22` | LATENCY: dispatch-idiom denominator (10 idioms / 58 engines) |

Per-file detail is in the commit messages; no table duplicated here.

## NFRA_TOOLBHVR.ROUTE — closed out (class 4 flipped, then upgraded)

~A landed the `comp-routes trace` fix, so my class-4 NO-COVERAGE message flipped to a real route
**as designed** — but not as an oracle. ~A's constraint was the design driver: *"if your routing surface
collapses 2 and 3 into 'resolved', you re-create the exact false authority this TO closed, one layer
up."* The message makes the agent read WHICH of the outcomes they got. Given my whole ROUTE finding was
"a nudge promising a resolution the tool cannot make trains bypass," re-committing that inside my own
flip would have been the worst available outcome.

Then ~A shipped the `--json` arm and I **deleted my hardcoded paraphrase** of their `plane` /
`blind_spots` / residuals — the rail now keys on the `outcome` ENUM and reads the caveats FROM the
payload. My copy stopped being a copy. Two things came out of that exchange worth keeping:
- **My `--json` ask surfaced a defect:** `--json` silently returned PROSE on the URL branch (the
  behavior branch returned before the JSON emitter). A flag promising machine-readable output and
  returning prose is the same honesty class — ~A rebuilt it as a fix, not a feature.
- **`NO_MATCH` was the class neither of us had:** I listed three outcomes because three are what the
  output DISPLAYS; the fourth is the one that shows nothing. An absent result is not a result. ~A's
  framing back: *ask what the enumeration is an enumeration OF, not just whether it is complete.*
- **~A's warning stopped a mistake I was about to make:** rendering non-empty `blind_spots` as a warning
  badge would make every correct RESOLVED answer look degraded and train agents to ignore it. A
  structural limit is a property of the SCAN CLASS; a health signal is a property of the ANSWER.

## NFRA_TOOLARCH.LATENCY — Phase 1 (ZERO derivations executed, by design)

Accepted the Andrew-direct TO, read the safety section first, and flagged the immediate consequence
before starting: the MDPF serve is open, so **every AWS-touching derivation is recorded `DEFERRED-AWS`,
not fired** — the same signal that opens the R4 arm-window opens this.

**Enumerated from source, zero execution** — because for the auto-refresh family **the measurement
instrument is itself a mutation** (`comp-kuzu` auto-refreshes on a plain query; the `cli.py` read family
rebuilds on a stale cache). You cannot ask those tools what they do by running them.

Artifact: `deliverables/NFRA_TOOLARCH_LATENCY_phase1_surface.jsonl` — 152 derivation records, 65 tools,
each with class + reason + run-decision. Taxonomy is **three** classes, not two:
**CONDITIONALLY-MUTATING** — mutability is a property of the **(command, cache-state) PAIR**, not the
command. Routed to ~Z as a taxonomy contribution at base's ask, because every safety design that
classifies calls read-vs-mutating FROM SOURCE inherits the same false binary — including this TO's own
safety section. Corollary carried into the census: **a timing without its cache state is not a timing**
(a wall-clock across an unrecorded rebuild looks like tool latency and IS a cache miss).

### Registry drift found (base's surface), and base's ruling

My refusal to hand-list the derivation surface exposed that `tools_index.subcommands` is populated on
**65/65** and **ungated** — the most convincing possible shape for a wrong denominator. Measured drift
**16/24** on the apples-to-apples set. My extractor independently reproduced base's `comp-pipescript`
13-vs-8 EXACTLY (positive control; two differently-built instruments agreeing on the one tool both could
check). Omissions include derivations CLAUDE.md **mandates**: `comp-pipescript postdeps`, `comp-iam
simulate` **and** `reconcile`, `comp-registry sync`. Base ruled **GATE+BACKFILL, gate first**; spec
arch-gated to ~Z. Not mine to build.

## Four instrument defects this window — three mine, none published

1. **`choices` fallback INVENTED subcommands** from unrelated flag values (`comp-tool-health` ->
   FIX/KEEP/PROMOTE/RETIRE are verdict strings). Caught before reporting; rewrote the extractor.
2. **Write-signal heuristic over-flagged** (`json.dump(` matches printing-to-stdout). Refined with
   matched-line + sink analysis: 68 -> 64, each survivor carrying an exact `file:line`. Small net
   change — but unknowable without checking.
3. **ENGINE-grain vs DERIVATION-grain** (the load-bearing one): one writing subcommand marked every
   sibling MUTATING. `iam_cli.py:1017` writes a census — that is `refresh-census`; `service`/`gaps`/
   `simulate` are READS, and those are the Rule-22a-mandated ones. Attribution ATTEMPTED and **NOT
   CLOSED**: my AST attributor traced 5/53 engines. Recorded OPEN rather than published.
4. **~A's false zero about MY work** (theirs, shared generously): `-E` on the first grep and not the
   second made the alternation basic-regex, searching for the literal `"blind|DESIRED plane|residual"`.
   Zero hits, clean exit, no error — and it read as "his commit message describes work the diff did not
   do." Their positive control is the only reason it was not sent. **A zero from a search is a claim
   about the search before it is a claim about the world.**

All four share one shape: **the scan was broken and the output was well-formed.**

## CTO~Z falsified an inference of mine — corrected on the record

I told base the registry omissions mean *"comp-which cannot route anyone to them."* That carried an
**unverified premise**: that `tools_index` feeds the router. ~Z traced it — `comp-which:1006-1010`
@`e6115fa66` scores `entries[]` and **never reads `tools_index`**. So the fix I implied (backfill)
**would not have made anything routable**; declared entries are equally unreachable. Right about the
symptom, wrong about the mechanism — Rule 22's class exactly. Census consequence adopted: **EXISTS vs
ROUTABLE are now distinct axes**, and the declared-but-unreachable population is a first-class finding.

## The idiom denominator (~Z ruling: enumerate before writing handlers)

~Z ruled: do NOT build a second attributor (fold into the shared module with base), and my ">=3 idioms"
was an **unknown denominator** — handlers for the idioms I happened to hit produce an attributor whose
denominator comes from its own encounters.

Enumerated by clustering observed signatures: **10 DISTINCT DISPATCH IDIOMS across 58 engines**, and
**5 of the 10 are COMBINATIONS** (engines dispatching two ways in one file) — so the shared resolver must
resolve a **SET of signals per engine, not a single label**. ~Z ratified; that is exactly the error that
would have shipped from adding handlers ad hoc. ~Z's estimate was 6-7: **this layer is less uniform than
its own architects assume**, which matters for Andrew's generalize-tool-creation charter.

**A CEILING IS NOT A FAILURE RATE.** My attributor handled one idiom, so its ceiling was **5/58 (8%)**
regardless of how well it ran — the other 92% were structurally INVISIBLE, not failing. An instrument
failing shows errors; an instrument blind shows a clean run over a small population and reports high
confidence on everything it can see (the orphan-watcher / `comp-iam` GREEN shape).

**The scare number I did not publish:** 26 engines with no dispatch signal reads as a 45% blind spot and
is honestly stateable. Discriminating question: do they HAVE subcommands? Measured `add_parser >= 2`
across them = **ZERO**. All single-derivation/flag-driven — "unclassified" means correct-by-construction.
Real surface: **~32 multi-subcommand engines, no hidden gaps.** 45% would have been TRUE and materially
misleading, and would have sized the job at several times its real cost.

## Compiler Tools

| Tool | Call | Result | Note |
|---|---|---|---|
| comp-tool-hud (subject + instrument) | incident shape + 4 negative controls, re-run after EACH of 3 edits | PASS | positive fires, negatives silent every time — the change discriminates |
| comp-manifest-check | registry cross-check (`tools_index.subcommands`) | PASS/finding | surfaced the 16/24 drift; base ruled gate+backfill |
| comp-routes | consumed `trace --json` contract shape (~A's output, not re-run by me) | PASS | now the rail's routing target for class 4 |
| static AST/source extraction | derivation enumeration, classification, refinement, idiom clustering | PARTIAL | 3 of my own defects found here; attribution ceiling 8% recorded OPEN |
| safe-commit / commit-gate | 6 commits | PASS | risk-reflex fired on the HUD (recorded-warning node) and was read before proceeding |

**What worked:** enumerating before explaining, twice (the idiom space; the bounding check) — both times
it changed the answer. Coordinating with ~D/~A/base BEFORE building, which inverted my TO's premise once
and stopped a bad UI choice once. **What failed then was caught:** three of my own instruments, all
before publication. **Gap found:** two of MY OWN detector passes disagreed 23 vs 26 on the `cmd_`-prefix
convention — the two-normalizer disease inside one agent, one task, two passes. That it can happen there
is the strongest argument that it is structural, not a lane-coordination failure.

## Blockers

None blocking. **LATENCY execution is correctly gated on my own open item** — the shared
resolver/normalizer module with base, then attribution over the 10 idioms with a coverage assertion that
FAILS LOUDLY. ~Z explicitly authorized the delivery date moving: a census whose coverage I can state
beats an early one that needs caveats.

## Current State (zero-prior-context handoff)

- **ROUTE: complete.** `.tools/hooks/comp-tool-hud.sh` — two message bodies rewritten
  (`aws_freshness`, `infra_grep`). **Gating untouched** (`aws_freshness`/`infra_grep` were already
  `_gate=1` at `:223-224`). PreToolUse on every Bash/Grep call fabric-wide: **syntax-check both shells
  before any future edit.** Class 4 routes to `comp-routes trace --json`, keys on the `outcome` ENUM
  (RESOLVED | UNRESOLVED_NO_RULE | CATCHALL_DEFAULT | NO_MATCH); anything != RESOLVED is
  not-a-resolution, and a catch-all MAY carry a non-null `s3_key`.
- **LATENCY: Phase 1 only.** `deliverables/NFRA_TOOLARCH_LATENCY_phase1_surface.jsonl` (152 records) +
  `..._NOTES.md` (method, both grain defects, idiom denominator, EXISTS-vs-ROUTABLE). **ZERO derivations
  executed.** Census will run under `COMP_SYNTHETIC_FIXTURE=1` (base's ruling — tag the rows, do not
  hide them; a census that leaves no trace is its own dishonesty).
- **R4R6: complete, triggers DE-WIRED.** `.git/hooks/post-commit` carries stitch-refresh ONLY. Arm with
  `bash .tools/git-hooks/install-closeout-comp-state.sh` on ~Z's window signal — one command.
- Certification source of record for routing: ~D's `NFRA_TOOLARCH_CANON_QUESTION_CLASS_CERTIFICATION.md`
  @`2471d2806`. **Do not fork it** — request re-cert from ~D.
- Housekeeping still open (needs destructive-git confirmation): stale `scratch-r4-mutant-v2` branch;
  scratchpad fixtures under the session scratchpad.

## Next Steps

- [`0.8.0_AE_CloudComp`] owns the shared module call (resolver + declared-side normalizer + fixtures);
  I build to whatever shape they decide — singularity over ownership.
- [`0.8.0_AE_CloudComp~B`] then attribution over the 10 idioms w/ loud coverage assertion, then the
  local read-only census under timebox + sampled-variance control.
- [`1.0.0_SA_CTO~Z`] owes the R4 arm-window signal (also unblocks LATENCY's AWS half).
- [`3.0.0_SA_CVO~Z`] verifies R4R6 + ROUTE; LATENCY when Phase 2/3 land.
- [`0.8.0_AE_CloudComp~A`] pointed at base's resolver rather than a third, per ~Z.

## MCP Traffic

~22 messages (11 in / 11 out); broker re-surfaces not counted. Significant: ~A's fix-landed + `--json`
+ their false-zero self-report; ~D's certification table + their own audit self-correction; base's
gate+backfill ruling and the do-not-execute set; ~Z's AC-2 ruling, the LATENCY GO, the
no-second-attributor + enumerate-the-idiom-space ruling, and the source-falsification of my routing
inference.
