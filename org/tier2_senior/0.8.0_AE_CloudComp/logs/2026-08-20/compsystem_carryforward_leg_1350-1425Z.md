# 0.8.0_AE_CloudComp -- comp-system FORM (a) carry-forward leg (CTO ruling @4484d55608), 1350-1425Z

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE

## Summary

Morning re-form per Andrew's terminal directive (queue-drain): executed the CTO-dispatched
comp-system carry-forward leg of the device-axis ruling @4484d55608. Landed ahead of the ~1530Z
ETA: fix @cde1ddde7c + landing-regen @b90002e857, self-test 33/33 -> 39/39, both branches
exercised live 10/10, CTO gate pending on RAVC2 (sent 1419Z).

## Work done

1. Startup: /watcher (registered PID 29736, Monitor task bes4lk9f6 confirmed running via
   TaskOutput, 9 pending messages delivered + read), XXX.md A.1 serial file / A.2
   audit-archive-invoker (rc=0, 0 findings, snapshot not-due) / A.3 PATH check (97 of 99
   comp-tools resolve bare; comp-which exercised, banner produced), /cloud-ops loaded.
2. Read CTO ruling doc CTO_RULING_20260820_DEVICE_AXIS_INSTRUMENT_PAIR.md + Msg 63052 (GO) +
   Msg 63063 (pre-gate pin: a carry defeats the DRIFT verdict, never the AGE clock).
3. Scoped all four graph-grounded downgrade surfaces in org/modules/graph/comp_system.py:
   collect_cloud_resources unreachable branch, collect_system_content graph-infra freshness,
   collect_runtime_compilation, compute_metrics graph_marker.
4. Implemented FORM (a): carry helpers (_this_device via the estate's ONE device mechanism /
   _unwrap_carry / _carry_mark / _prior_06 committed-06-only / _carriable / _carry_class),
   the four surface carries (value VERBATIM, mark in vintage field ONLY -- the by-construction
   gate/check drift exclusion), the header age anchor (graph_carried_rows +
   graph_carried_since chained to the ORIGINAL derivation's emitted_at, preserved across
   re-carries), and the _staleness carried-age clause ("age " reason class -> gate WARN rc 0,
   never fail-closed DRIFT).
5. Self-test extended 23-28 (carry semantics, one-level no-nesting, no-fabrication,
   region-layer drift exclusion exercised in a scratch dir, age-clock pin both directions).
6. Exercised both branches live via scratch harness (scratchpad/exercise_carry.py,
   run-and-read): (A) kuzu forced unreachable + real committed prior @bd852b6e4c -> 4/4
   surfaces carried marked "on laptop", graph_carried_since == prior emitted_at exactly;
   (B) unreachable + all-UNKNOWN prior -> honest UNKNOWN, no header keys. First harness cut
   truncated evidence strings before checking and manufactured 1 false FAIL -- fixed to check
   full strings (the display limit is not the oracle).
7. Landing regen: comp-system full compile with the graph reachable (20,729 nodes) healed
   HEAD's 06 -- @ff58d8e687 (1337Z laptop regen) had already written the downgrade the ruling
   names (first UNKNOWN in 15 commits of 06 history, denominator printed). Surfaced in RAVC2,
   not chased beyond the heal.
8. Push to CLOUD correctly blocked by LD-0367 integrator-only gate -- commits await MSTR's
   integration window; no override used.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| comp-which | "how do I grep the repo" (A.3 exercise) | PASS | forwarder ran, banner produced |
| comp-system | --self-test (baseline, pre-edit) | PASS | 33/33 observed before any edit |
| comp-system | --self-test (post-edit) | PASS | 39/39 incl. new 23-28 carry checks |
| comp-system | --json (fresh path, no write) | PASS | real graph rows, no carry keys |
| comp-system | --check (pre + post regen) | PASS | rc 0, 26 regions / 6 files / 0 drifted |
| comp-system | --gate | PASS | rc 0, gate open |
| commit-gate.sh | comp_system.py | PASS | py_compile + AST + ruff py39 clean |
| kuzu_cli.py (comp-kuzu engine) | CloudNode count probe | PASS | 20,729 nodes, answers in seconds |

What worked: the pure-decision helper pattern (mirroring _gate_verdict) made the unreachable
branch fully testable offline; the value-verbatim/mark-in-vintage split made the drift
exclusion structural rather than a predicate patch.
What failed: first harness cut truncated strings pre-check (false FAIL A2) -- harness defect,
fixed same run.
Gap found: none new; the @ff58d8e687 silent downgrade is the ruling's own class, now closed.

## Files Modified

See commit messages: @cde1ddde7c (org/modules/graph/comp_system.py, 266 insertions), and
@b90002e857 (infra/system/06_current_state.md + .json, the landing regen).

## Deployment Sequence + Verification (AE)

No AWS deploy this window -- repo-local instrument change only. Verification pasted:
```
--- self-test: 39/39 passed (grounded-or-UNKNOWN, no fabrication, shape-locked) ---
--- exercise: 10/10 passed ---
SYSTEM CURRENT (06: sources unchanged, age 0h < TTL 24h; managed regions: 26 compared across 6 file(s), 0 drifted)
SYSTEM CURRENT (no genuine drift) -- gate open.
```

## MCP traffic

12 messages handled this window (9 backlog + 3 live). Significant: CTO Msg 63052 GO + 63063
pre-gate pin (implemented); COO 63065 canary-discharged + sequencing confirmed; COO 63068 W-15
grain-3 pre-notification (no action). Sent: RAVC ack 1402Z, COO movement-check answer 1402Z,
RAVC2 gate evidence 1419Z. READ-acked 63063/63065/63068.

## Blockers

None. (Push block is LD-0367 by design, not a blocker -- integration is MSTR's window.)

## Current State

- Fix landed local CLOUD @cde1ddde7c: org/modules/graph/comp_system.py carries graph rows
  forward marked ("carried-forward @<prior-vintage>: graph unreachable at <ts> on <device>")
  when comp-kuzu is unreachable; committed-06-only carry source (no history walk);
  header.graph_carried_since ages carried rows from the original derivation.
- Landing regen @b90002e857: infra/system/06_current_state.{md,json} healthy, real graph rows,
  as_of HEAD=754afdd59e, --check CURRENT.
- CTO gate PENDING on RAVC2 (sent 20260820T141935Z). CVO~Z cite-not-regen interim conditions
  met locally; lifts after MSTR integration + relay.
- Both commits UNPUSHED on local CLOUD awaiting MSTR's LD-0367 integration window.

## Next Steps

- [1.0.0_SA_CTO] close the arch gate on the RAVC2 evidence (their turn).
- [0.0.0_AB_MSTR] integration window publishes @cde1ddde7c + @b90002e857; site-Z relay per the
  ruling's routing so CVO~Z's cite-not-regen interim can lift.
- [0.8.0_AE_CloudComp] next queue item per COO sequencing: dot-truncation (Andrew-prioritized)
  -> NFRA_TRUNCLASS.SWEEP -> H8; then COO's W-15 grain-3 landing TO once CRO's naming word
  exists (pre-notified, not yet seated).
