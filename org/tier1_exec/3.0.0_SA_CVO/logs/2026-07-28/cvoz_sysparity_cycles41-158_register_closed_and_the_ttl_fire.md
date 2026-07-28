# NFRA_SYSPARITY cycles 41-158 (lane 3.0.0_SA_CVO~Z): register CLOSED at 22/22, the TTL fired once, and five of my own claims corrected

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE, SCRIBE

**Window:** since my cycle-40 log (`c03e6aee17`) -> 2026-07-28T1242Z. 28 commits.
**Lane:** `3.0.0_SA_CVO~Z` (NFRA/ontology, off main channel). Comms confined to {~Z} + {MSTR} + {0.8.0_AE} per LD-0325.

## Summary

The LD-0318 per-domain assumption sweep **CLOSED** in this window: the 22-unit register went to
**22 CLEAN / 0 PARTIAL / 0 DRIFTED, 22/22 pointer-backed** at cycle-59 and has held since. The
remaining ~100 cycles were gate-watch, not sweep. One real event (a TTL expiry at cycle-125) and
one real defect demonstration (a graph timeout) landed in that tail.

**The load-bearing content of this window is not the CLEAN verdicts -- it is the corrections.**
Five claims I had already stated, several of them publicly, turned out wrong and were retracted
with the mechanism named. That ratio is the honest output of a verification lane.

## Work completed

**1. Repair manifest executed (`c3b077a35a`, cycles 50-51).** 9 claim sites across 5 docs.
**4 sites EXCLUDED as legitimate records-of-then** (a doc describing what was true at its vintage
is not drift), **1 routed to CTO~Z** (outside my authorized surface). Post-repair re-verify moved
6 units to CLEAN, 1 to PARTIAL -- **every verdict established by READING the claim site, not by
counting matches.**

**2. Register closed (`6e8e5adbc6`, cycle-59).** ct-router landed; 22/22 CLEAN. The fix REFINED
the ruling it was made under rather than merely applying it.

**3. comp-kuzu SERVED-STALE: escalated, resolved, verified (`3e5693c3b1`, cycle-84).** Pin frozen
17.5h; resolved in 78 minutes; verified 115s -> 3.2s. The fix confirmed a hypothesis I had
explicitly labelled unproven -- which is the only reason the label was worth writing.

**4. TTL fired at cycle-125 (`434aa893c5` + `1c84012464`).** 06 crossed 24h; `--check` rc=2.
Regenerated per the gate's own prescription. **The diff is the finding: 8 lines, header timestamps
plus HEAD vintage `25b2e400e8 -> efd4146509`, 0 managed regions changed, 0 substantive delta.**
A scheduled expiry, not the estate moving. Recorded as a single CLEAN row with the expiry as a
residual -- a DRIFTED/CLEAN pair would have read as a defect found and fixed.

**5. Preconditions verified BEFORE that write.** `comp-system` is a WRITE, and it is the command
that caused an incident earlier this session by sweeping a peer's unlanded registration into 06.
`_dirty_sources()` empty, `infra/system/` clean. **Hazard measured absent, not presumed absent.**

## Corrections issued against my own prior claims (the substantive output)

| # | What I claimed | What was true | Mechanism of the error |
|---|---|---|---|
| 1 | cycle-77: the graph_marker finding degrades the estate's freshness contract, 3 consumers exposed | a 40s timeout constant against a graph answering in ~115s | reached for a conviction the instrument did not support |
| 2 | cycle-40: eng-synthesis CLEAN | defect was in prose I had skipped | verified the structured fields, called the whole unit |
| 3 | cycle-42/58: two findings open | RESOLVED BY RULING; I never re-read them against the ruling that governed them | carried state instead of re-deriving it |
| 4 | inf-plumbing F3 NOT LANDED (twice) | it HAD landed -- my sweep counts strings, and a string survives inside its own retraction | counted, did not read |
| 5 | cycle-119: age-past-TTL returns rc 0 | true of `--gate`, NOT of `--check` (rc 2 on any staleness) | read one function's self-test, applied it to the other surface |

**#5 is documented in the tool's own header** -- `.tools/comp-system:13`, *"Distinct from --check."*
I had the discriminating evidence available and read the wrong artifact.

**Same wrong-axis shape appeared twice more this window and was caught in-cycle, not published:**
`max()` over the register's `cycle` field returned `"cycles-16-19"` (STRING field, lexicographic
sort -- `"cycles"` outranks `"cycle-"` at char 6); and a `2>/dev/null` on a register query turned a
usage error into an apparently-empty register. Both caught because the output was implausible on
its face, not because the tool said anything.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-system --check` | every cycle, gate-first | PASS (rc 0) except cycle-125 (rc 2 STALE) | the loop's gate; now wrapped in `timeout 100` after a 2m hang |
| `comp-system` (regen) | cycle-125 | PASS (rc 0) | a WRITE -- preconditions checked first |
| `comp-system --gate` | source-read only | n/a | read `_gate_verdict` to correct claim #5 |
| `sysparity_register.py record` | cycles 41-59, 76-77, 125 | PASS | rejects non-UNRECORDED verdicts lacking a pointer |
| `safe-commit.sh` | 28 commits | PASS | pathspec-scoped, no pre-`git add` (Rule 14a) |

**What worked:** the register's write-time refusal to accept a pointerless verdict. It made
"22/22 pointer-backed" a property of the instrument rather than a claim by me.

**What failed:** `comp-system --check` **hung and was SIGTERM'd at 2m** immediately after the
cycle-125 regen -- the signature of the `timeout=40` defect routed to CTO~Z. **That defect is no
longer latent; it has now demonstrated itself.**

**Gap found:** my per-cycle check only ever read my LANE inbox (`~Z/`). The fabric's halt gate
reads the BASE inbox while the lane watcher reads the lane inbox, so a message addressed to
`3.0.0_SA_CVO` would have sat unread and invisible to me indefinitely. **Widened at cycle-95 to
cover both paths.** Same shape as the cycle-84 finding, where a resolution reached the dispatcher
and the executor but never the finder.

## Files modified

See commit messages: `c3b077a35a`, `6e8e5adbc6`, `434aa893c5`, `1c84012464`. Surfaces touched:
`infra/system/{00,01,03,05,06,07}*`, `infra/system/scope_contract.json`,
`infra/system/sysparity_register.jsonl`, `docs/doctrine/CONTROLS_OVER_CARE.md`.

## MCP traffic

Significant dispatches only (per the speed contract):
- **-> CTO~Z (cycle-85):** the fork-closing addressing convention base CTO adopted has a SECOND
  independent instance -- mine, from a different incident. Flagged the convergence; explicitly did
  NOT merge the cases.
- **-> MSTR (cycle-100):** measurement only -- register 22/22, last movement cycle-77, 23
  consecutive no-change cycles. **Deliberately withheld the cadence recommendation**, which was
  already with Andrew via CTO~Z; repeating it would be the volume problem it exists to solve.
- **-> MSTR (cycle-125):** new verdict, the TTL refresh, with correction #5 attached.

Inbound: nothing unread at any cycle in the tail. Two base-CTO messages surfaced via CTO~Z's
`read/` at cycle-85 were addressed to CTO~Z, not me -- read, not acted on.

## Blockers

**None.** The LD-0318 cadence question is with **Andrew** (CTO~Z correctly declined to discharge
it; the stop-condition is Andrew's). That is a pending decision, not a blocker -- the loop runs
fine meanwhile.

## Current state

- **NFRA_SYSPARITY register:** `infra/system/sysparity_register.jsonl`, **55 rows, 22 units, 22
  CLEAN, 22/22 pointer-backed.** Append-only, latest-wins. Query it; do not recall it -- and do
  **not** use `max()` on the `cycle` field (string, lexicographic).
- **Gate:** `comp-system --check` CURRENT, 06 age ~16h of a 24h TTL, 26 managed regions across 6
  files, 0 drifted. Next TTL fire in ~8h; response is a regen after checking `_dirty_sources()`.
- **Cycles 20-21:** **UNRECORDED, not clean.** CTO~Z ruled they must not be reconstructed. This is
  a permanent hole in the record and is meant to stay visible.
- **Open routed item:** `_kuzu_marker()` `timeout=40` at `org/modules/graph/comp_system.py:102`,
  with CTO~Z. Correctly low-priority while the graph answers in 3.2s; **it fired once at cycle-125.**
- **06's 20 `UNKNOWN-VINTAGE` values are steady state** (off-VPC probes), positive-controlled old
  vs new at 336 lines each. Do not open them as a regression.

## Next steps

- **[Andrew]** LD-0318 cadence. My recommendation on record: stand down to event-driven. Measured
  basis: gate CURRENT on 92.9% of checks; register unmoved for 48 cycles before the TTL fire, and
  that fire produced a zero-content-delta re-stamp.
- **[1.0.0_SA_CTO~Z]** `timeout=40` at `comp_system.py:102` -- no longer latent.
- **[3.0.0_SA_CVO~Z, me]** continue the minimal cycle: gate (timeout-guarded), both inbox paths,
  swept-surface change detection, delivery-state on routed items. Report to MSTR only on a new
  verdict.
