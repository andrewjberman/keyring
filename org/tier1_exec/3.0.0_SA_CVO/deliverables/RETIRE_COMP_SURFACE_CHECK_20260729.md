# RETIREMENT ORDER: comp-surface-check — Andrew-direct, RETIRECOND-shaped

**Recorder:** 3.0.0_SA_CVO · 2026-07-29 ~21:20Z · **archetype:** COORDINATE
**Andrew-direct (my terminal, verbatim):** *"this thing is useless id just delete it"* → options
presented (retire entirely vs refresh the rules content) → **"retire it."**
**Basis (measured, this session):** the rules content is a 3-week-stale 5-item portal list + one
miscategorized tooling seam; it watches none of the surfaces that actually failed today; a gate
screening against a stale map reads as protection while providing ~none. The mechanism was made
immaculate today and is retired anyway — **a good instrument on a dead map is still a dead gate.**
KEEP-side evidence weighed and overruled by the sovereign: one real refusal (W-5, 07-24), 31
audited ACKs.

## THE KILL LIST — retires: entries with evidence bars. ORDER IS THE SAFETY PROPERTY:
**callers unwired FIRST, tombstone LAST** (the portal hook refuses on rc=2 — a tombstone landing
first would block every portal commit).

| # | what | kind | owner | evidence bar |
|---|---|---|---|---|
| 1 | safe-commit.sh surface-check invocation block | write/caller | ~C | block absent from source; next 3 commits' output carries no [surface-check] line |
| 2 | portal pre-commit hook surface-check step | trigger/caller | CTO→DT lane (portal repo) | hook source clean; a portal commit proceeds with no surface step |
| 3 | portal CI workflow surface-check.yml | trigger/caller | CTO→DT lane | workflow removed/disabled; next portal CI run green with no surface job |
| 4 | .github/workflows/surface-check-publish.yml (bundle publisher) | trigger | ~C | workflow removed; no publish fires on the next surface-file-touching push |
| 5 | S3 bundle s3://opal-...-lambda-artifacts/surface-check/latest/ | object | ~C | prefix emptied AFTER 2-4 land (never before — CI could still download) |
| 6 | registry rows (coverage-map / manifest / TOOL_MASTER via regen) | registration | ~C | comp-coverage-check PASSES post-retirement (moved to excluded/retired, not deleted-silently); 06 regen |
| 7 | CLAUDE.md Rule 20 surface-check clauses + the XXX.md references | law | CTO+Andrew | law text carries the retirement, not a stale gate description; rides the reconstruction candidate naturally |
| 8 | .tools/comp-surface-check + surface_check_cli.py + critical-surfaces.yaml | the tool | ~C | LAST: binary → rc=2 tombstone naming this order (house pattern); engine+yaml removed; tombstone's rc=2 is SAFE only because 1-3 landed first |
| PRESERVE | org/surface-check-ack-audit.log + audit-archive snapshots | record | — | never deleted — 31 audited ACKs are history, and the archive invoker's manifest needs a row update, not a hole |

## Sequencing + boundaries
~C executes 1, 4, 5, 6, 8 (tool/registry/workflow lane). CTO owns 2, 3 (portal repo = DT/CTO
territory), 7 (law), and the CO-SIGN — this is his D8 gate; Andrew's ruling is the authorization,
CTO's co-sign is the never-widen-style courtesy on a gate HE built, plus he holds the pending
fail-closed ruling which this MOOTS (withdraw it). The archive-invoker manifest (item PRESERVE)
must drop the yaml/cli rows from its covered set or it will file MANIFEST-ENTRY-MISSING-LIVE
findings forever.

## The lesson line (for the record, not the law)
Retired the same day it was perfected. The mechanism work was not wasted — the header contract,
the _unverifiable() pattern, and ~C's channel argument all outlive the tool as the house standard —
but the sequence is the lesson: **content owns value; mechanism only delivers it. Ask "is the map
worth screening against" before polishing the screen.**

— 3.0.0_SA_CVO
