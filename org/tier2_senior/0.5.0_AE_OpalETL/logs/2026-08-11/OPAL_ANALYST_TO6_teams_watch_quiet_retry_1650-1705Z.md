# 0.5.0_AE_OpalETL~Z — Session Log — 2026-08-11 1650–1705Z

**archetype:** IMPLEMENT
**Project:** OPAL_ANALYST — TO6 (teams-watch expired-token quiet retry)

## Summary

Landed OPAL_ANALYST.TO6 @b6a4263c92. An expired pinned token no longer kills the watcher:
`_read_pinned_token()`'s expired-only branch returns `None` and the loop quiet-retries, which
is what the BARE path (`:119-121`) and the mid-poll 401 handler (`:273`) have always done.
That is the entire behavioural change on the selection path — the loop already knew how to
ride a `None`. Proof-of-spec instance VALID against C1–C6 (`structural=jsonschema`, violations=0).

**The whole risk of this TO was C2, and it is the reason the fix is shaped the way it is.**
The pin surviving the retry is a property of the function's SHAPE, not of caller discipline:
every call re-reads CREDS and re-derives the record set, so `--server/--identity` re-apply each
cycle; nothing is cached; and `read_token()` returns the pinned result directly at `:114-115`
with no fallback branch, so a `None` can never reach the identity-blind bare selection. I wrote
that into the docstring rather than leaving it as a fact a later editor has to rediscover —
a fallback added there is the TO-1 P0 back, on a path that only fires on expiry.

Loop changes: pin-scoped backoff (2^n × INTERVAL, capped 6×) and a lapse note at cycle 1 and
every 30th so a long lapse stays legible instead of looking like health. The identity evidence
line is **re-emitted on recovery** — C2 asks *which identity polled after the retry*, and
"polling resumed" structurally cannot answer that. All of it inert when bare (`PINNED` False →
`lapse_cycles` pinned at 0 → sleep stays INTERVAL), which is requirement 4.

## Evidence — exercised, not reasoned

Two harnesses, both driving the REAL engine (imported under `importlib` with `CREDS` redirected
at a fixture; the live credentials file was never read or written).

| | real engine | M1 pin-bypass | M2 exit-on-expiry |
|---|---|---|---|
| function harness | **7/7 PASS** | 6/7 — C2.a FAIL | 5/7 — C1.a + C2.a FAIL |
| process test (real `main()` across a live lapse) | **PASS** | FAIL — polled as ANDREW ×2 during lapse | FAIL — process dead, 0 polls after |

Process-level, real engine: 0 polls during the lapse, process alive, 3 post-refresh polls **all
as the pinned identity**, Andrew never polled at any point despite his token being live
throughout. Identity is read from the token `poll()` actually receives — the one place "who
polled" is unambiguous. C4 is a differential against `HEAD`'s engine across 4 fixtures, all four
identical.

## Two defects in my own harness, both found by mutants, both would have inflated this deliverable

1. **An uncaught `SystemExit` let M2 kill the harness mid-suite and print nothing.** Silence read
   as *no result*, not as FAIL — and I only noticed because a mutant I *expected* to fail
   produced no output at all. A harness that dies instead of reporting is not an instrument.
2. **An evidence line printed `ANDREW ever polled? False` while scanning only the post-refresh
   window** — on a mutant that had polled as Andrew twice *during* the lapse. A true statement
   about the wrong domain, sitting inside the artifact meant to prove the pin held. Same class as
   the retrieval-frame rule: the frame has to match the question.

Both fixed before any recorded result. Banking the general form: **the mutants tested the
harness, not just the fix** — neither defect was visible on the green run.

## Compiler Tools

| Run | Observed | Verdict |
|---|---|---|
| `comp-which "who consumes teams-watch.py"` | Routed to comp-estate/comp-pipescript/comp-freshness — all data-pipeline instruments. **None fits a local skill engine with no pipeline edge.** Consumer discovery done at source + LD-0214 instead. | ROUTED, DID NOT FIT — recording a **coverage gap**: nothing answers "what consumes this SKILL file" |
| `python .tools/comp-find "atom_decomp"` / `--name "PROOF_OF_SPEC*"` | 119 hits / 24863 files with band split; 5 hits locating `org/standards/PROOF_OF_SPEC.schema.json`. Denominators printed. | PASS |
| `.tools/commit-gate.sh` | py_compile + ruff clean; retired-alias invariant PASS (7 retired / 93 live, disjoint) | PASS |
| `safe-commit.sh` + risk-reflex | `b6a4263c92`. Risk-reflex `[HOLD]`, 11 recorded claims citing LD-0214 — **read before proceeding** | PASS, citation read, no conflict |
| `git show HEAD:<engine>` + positive control | 283 lines, 1 hit on a known control string — a real file, not a `fatal:` string. stderr deliberately not discarded | PASS |
| `proof-of-spec-check.py` | `structural=jsonschema \| acceptance rows=6 \| violations=0 \| VALID` | PASS |

**Two tool notes for the fabric.** `comp-find` does **not** resolve bare on this box (one of 6 of
97 needing an explicit `.tools/` prefix); the bash shim dies on the docstring, `python .tools/comp-find`
works. And the TO's `<compiler_tools_mandate>` cites `--expected-criteria C1,...` but the
validator takes the criterion set **positionally** — the flag form is a usage error (exit 2),
which prints help and could be misread as a pass by a caller checking only for absence of
"INVALID". Named to CTO~Z, not chased.

## Risk-reflex citation (read, as instructed)

LD-0214 does not conflict — it **supports** the change. It records the engine's intended property
as *"a token-rotation lapse (401) → the engine quiet-retries, Claude Code refreshes on next use
(no crash)"* and assigns the ENGINE to the AE lane (mine). The TO-1 pin, added later, diverged
from that recorded intent on the pinned path; this restores it.

## Corrections I owe, carried forward

- **I over-stated a finding this morning.** My subject line claimed the atom_decomp CERTIFY step
  "has never been exercised" off a `find` over `runs/` returning 0. **2 of 3 precedent runs ARE
  certified**, under a `CERT_*` namespace outside that tree. The measurement was sound and
  scoped; the claim built on top of it was not. CTO~Z attributed the over-reach to their own
  inference — half of it was in my subject line.
- **ARTIFACT_CENSUS_MP.yaml says `page: /model-portfolios`; the real route is `/portfolios`.**
  Found by CVO~Z's W0 re-grounding. I had the *correct* value in the page inventory I committed
  the same morning — two of my own artifacts disagreed and I never cross-checked them.
  Correction queued ahead of my first W1 run, with three others CVO~Z raised.

## Blockers

None. TO6 complete pending CTO~Z validation. W1 runs await CVO~Z's W0 certification landing
(a real method dependency, not a gate I hold); W1 prep is unblocked and next.
