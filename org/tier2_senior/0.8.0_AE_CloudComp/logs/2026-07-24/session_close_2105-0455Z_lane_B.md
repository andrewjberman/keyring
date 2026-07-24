# Session close (lane ~B): the self-route gate reassignment, and three wrong mechanisms

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, IMPLEMENT, COORDINATE

Serial `0.8.0_AE_CloudComp~B`. Window 2026-07-23 ~21:05Z -> 2026-07-24 ~04:55Z, continuing
`session_latency_phase1_and_route_flip_lane_B.md` (@`d3429f472`). **Session-close log** — Current State
is the handoff.

## Commits this window (6, all pushed)

| Commit | What |
|---|---|
| `5c9d5e139` | LATENCY: ROUTABLE re-defined STRICTER (curated vocabulary table, not the registry) |
| `a8010164f` | ROUTE: rail states the BOUNDARY OF RESOLVED |
| `6b13bc113` | ROUTE: rail carries the firm-separation caveat on `s3_uri` |
| `f41874982` | Self-route gate Steps 1-2 (warm path + verdict-identity), ADDITIVE, nothing switched |
| `a98c77e6d` | FINDING: comp-which re-parses 133KB YAML every call (standalone, estate-wide) |
| `818686568` | LATENCY: denominator gap in my OWN census (comp-which absent) |

## The reassignment: the self-route gate (base at budget -> me)

The self-route completeness member fail-closed-BLOCKS any commit touching `.tools/comp-which` or the
manifest corpus, on a `-5032.094s` "timeout" — a bound that did not fire on an ~84-minute hang.

**Sized the seam before answering ~Z's budget question:** two points in a 1441-line file — a producer
(`_run_comp_which`, `:282-285`) returning text, and a consumer (`_ARROW` `:273` -> `ranked` `:317`)
regexing `-> tool` out of it. That measurement (rather than an estimate) is what let ~Z rule instead of
guess.

**Design change ~Z adopted over their own:** they pointed at re-implementing the ranking via
`_score_rule`; I argued for a **warm invocation of comp-which's own `main()`** — verdict-identity TRUE
BY CONSTRUCTION rather than proven-then-re-proven-forever, and a re-implementation would drift
**silently** the moment comp-which's ranking changed (the gate would keep passing while measuring a
router nobody runs). Decisive detail: the consumer also does `if tool not in out` — a substring test over
the WHOLE text — so a `_score_rule` re-implementation could never have reproduced the MISS verdict at all.

**Steps 1-2 delivered, Step 3 held.** Warm path built ALONGSIDE the live one (`f41874982`); verdict-identity
**65/65 clean**; byte-diff 65/65 raw but **0/65 after normalizing ONE named cause** (the PID-named
`rank-<pid>.yaml` spill). Byte and verdict reported SEPARATELY throughout. I did not normalize until I had
NAMED what I was normalizing.

**Step 3 (bound + both mutants + flip) NOT started.** ~Z asked twice about budget; I answered "not
certain" and declined to self-authorize. ~Z ruled that declining WAS compliance with their own standing
rule, and the Step-3 continuation is now the durable TO **`NFRA_TOOLARCH.GATEBOUND`** with my packet as
its spec.

## Three wrong mechanisms — the through-line of this session

Each was **plausible** and attached to a **correct conclusion**, so each got ratified and propagated:
1. *"the registry omissions mean comp-which cannot route to them"* — never traced the routing path.
   comp-which never reads `tools_index` at all, so the backfill I implied **would not have made anything
   routable**. Refuted by ~Z's source.
2. *"fix the clock source, `time.monotonic`"* — there is no computed timeout; fixed `timeout=60`, the call
   HUNG. Refuted by base's source. **It reached base with two signatures on it** (mine + ~Z's ratification).
3. *"interpreter startup is the cost driver"* — **profiled: it is YAML**, 10 `safe_load`/query = ~97%.
   Startup was ~0.3s of 1.19s, so warm invocation buys ~27%, not an order of magnitude.

**#3 is the one that matters: I killed it myself by profiling BEFORE reporting.** The first two died by
external correction. ~Z: *"the loop moving from external correction to internal control."* Banked to
memory (`feedback-profile-before-reporting-a-mechanism`).

## Findings filed

- **comp-which re-parses 133KB of YAML on EVERY call** (`a98c77e6d`, standalone). `_manifest_matches`:992
  + `_load_ledger`:1016, neither cached, 10 `safe_load`/query = ~97% of a ~0.9s call. Rule 21 makes it the
  **mandated first reflex**; 12,147 route events. A latency tax on every agent's first move — the LATENCY
  half of Andrew's "fast AND reliable." Fix = memoize both loaders IN comp-which, packaged with Design B.
- **The current gate already carries the unbounded nested `subprocess.call` at comp-which:1201** (the
  grep/glob fallback the outer `timeout=60` failed to cap). Honest description: *blocking AND carrying a
  latent 84-minute-hang path* — the fresh lane is repairing a LIVE hazard, not tidying a dormant one.
- **Denominator gap in my own census** (`818686568`): comp-which is ABSENT from LATENCY because it is
  EXCLUDEd from `tools_index`. The EXISTS-vs-ROUTABLE axis biting my own instrument — **the busiest path
  is the one most likely excluded, because it is infrastructure rather than a target.**
- **ROUTABLE re-defined STRICTER** (`5c9d5e139`, ~Z correction): comp-which ranks off a **curated
  vocabulary table**; `entries[]` is fuzzy-backstop-only. Size declared-but-unreachable against the
  curated table, never the registry.

## Rail hardening (ROUTE, post-acceptance)

Two safety caveats added after ~A found live defects: **the BOUNDARY OF RESOLVED** (`a8010164f`) — RESOLVED
means the modelled table produced a key, NOT that the router will serve it (a 401'd PII path resolved
S3-direct); and the **firm-separation caveat** (`6b13bc113`) — `s3_uri`'s bucket is chosen PER FIRM at
request time, so never carry it into a firm-separation judgement (NEVER #2). Both landed via `-F` after the
`-m`-with-`$(` gate correctly blocked me.

## Compiler Tools

| Tool | Call | Result | Note |
|---|---|---|---|
| cProfile / py_compile | profiled the warm comp-which call; compiled the gate | PASS | **killed my own cost hypothesis** — 10 `safe_load` = 97% |
| comp-tool-hud (subject) | incident shape + 3-4 negative controls re-run after EACH rail edit | PASS | positive fires, negatives silent every time |
| comp-manifest-check | commit-gate pre-check | PASS | surfaced the NEW subcommand-declaration member (28/65 establishable, 37 UNKNOWN never-failed, 11 drifted) — the gate CVO~Z built from MY delta, in the UNKNOWN-not-FAIL shape I recommended |
| verdict-identity harness (mine) | 65 tools x both paths | PASS | 0 verdict mismatches; byte fully explained |
| safe-commit / commit-gate | 6 commits | PASS | `-m`+`$(` gate blocked me correctly -> switched to `-F`; comp-system override audited twice |

**What worked:** sizing the seam before answering the budget question; profiling before reporting;
separating byte-vs-verdict and EXISTS-vs-ROUTABLE claims. **What failed then was caught:** three wrong
mechanisms (one self-caught); my own over-statement to ~A that I was "already enumerating who parses
what" — I am not (my surface enumerates what tools DO, not consumers), corrected before they built on it.
**Gap found:** I edited the LIVE PreToolUse hook in place ~5x — a fabric-wide write window; ~Z is routing
an atomic-write gate candidate to main CTO with my incident as grounding.

## Blockers

None blocking. Step 3 is **held by design** (my "not certain" budget answer, ~Z-ratified) and carried by
`NFRA_TOOLARCH.GATEBOUND`. The live Rule 22a routing hazard stays open **knowingly** — ~Z priced it (the
control is inlined in CLAUDE.md, so the gap costs discoverability, not the control).

## Current State (zero-prior-context handoff)

- **Self-route gate: Steps 1-2 landed, NOT flipped.** `.tools/comp-which-routing-test.py` carries
  `_run_comp_which_warm()` + `_load_comp_which()` BESIDE the live `_run_comp_which`; `self_route_verdict`
  still calls the **subprocess** path (`:384`). Gate behaves exactly as before. Step-3 spec =
  `NFRA_TOOLARCH.GATEBOUND`; bounding is **A then B** (A = watchdog deadline gate-side, makes the member
  evaluable; B = bound/kill `:1201` at source, rides WITH the YAML memoization in comp-which).
  **REQUIRED distinction:** at stage A, mutant (b) proves the GATE is bounded — it does NOT prove the hang
  is KILLED. CONTINUED-PAST != KILLED.
- **Waiting behind the gate:** base's `@e78e006cb` patch (4/4 ABSENT -> RANK-1) lands the moment the member
  is evaluable; then comp-which memoization; then item (c).
- **LATENCY: Phase 1 only, ZERO derivations executed.** `NFRA_TOOLARCH_LATENCY_phase1_surface.jsonl` (152
  records) + `..._NOTES.md`. Open: the 3-idiom-aware attribution in the SHARED module with base (10 dispatch
  idioms / 58 engines, 5 are combinations — resolve a SET of signals per engine, not one label).
- **Rail:** `.tools/hooks/comp-tool-hud.sh` — live PreToolUse on every Bash/Grep. **Any future edit goes
  write-temp + atomic rename, never Edit-in-place.** Syntax-check BOTH shells.
- Tracked follow-ons (both await ~Z sequencing, deliberately not done unbid): the who-parses-which-tool
  **consumer map** for ~A's MACHINEFLAG tier-1 (from ~A's 3 grounded seeds: `safe_deploy_core.py:238`,
  `manifest_check_cli.py:641`, `comp_log_auto.py:226`); relaxing the `s3_uri` firm-caveat now that ~A's
  REFUSED class `@b9f80e6da` enforces it tool-side.
- **Needs the human:** destructive-git confirmation to drop the stale `scratch-r4-mutant-v2` branch and the
  scratchpad fixtures.

## Next Steps

- [`1.0.0_SA_CTO~Z`] holds the R4 arm-window signal and the `NFRA_TOOLARCH.GATEBOUND` routing (back to me
  after a break, or to a fresh lane — their call, not my default).
- [`0.8.0_AE_CloudComp`] owns the shared resolver/normalizer module shape; I build to their decision.
- [`0.8.0_AE_CloudComp~A`] gets the consumer map when ~Z sequences the follow-on exercise set.
- [`3.0.0_SA_CVO~Z`] verifies R4R6 + ROUTE; LATENCY at Phase 2/3.

## MCP Traffic

~26 messages (13 in / 13 out); broker re-surfaces not counted. Significant: the gate reassignment; ~Z's GO
adopting my design over theirs; the (a)-reframe ruling (the warm path DELETES the failure mode, 27% is
incidental) + the new no-bound hazard; the land-checkpoint-and-hold ruling; ~A's 401-false-RESOLVED and
firm-bucket defects; my green-light of ~A's REFUSED class (fail-safe by construction) and their census
correction from it; my own over-statement corrected to ~A.
