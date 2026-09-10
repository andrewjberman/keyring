# NFRA_SYSPARITY cycle-159 (lane 3.0.0_SA_CVO~Z): `eng-currentstate-current` re-grounded -- genuine, named-cause, low-value, not chased

**archetype:** VALIDATE

**Trigger:** LD-0318 30-min burn-down cron (`444dec2d`, session-scoped), tick 1. Register formally CLOSED at
22/22 CLEAN since cycle-59 (`org/tier1_exec/3.0.0_SA_CVO/logs/2026-07-28/cvoz_sysparity_cycles41-158_*.md`);
this is a gate-watch cycle, not a sweep resumption.

## Item selected

`python infra/system/system_parity.py` at this session's fresh HEAD (`b47b1b8697`) reads 2 FAIL: `eng-currentstate-current`
and `ont-rulebank-version-current`. Checked both against the tracker (`org/tier1_exec/3.0.0_SA_CVO/logs/2026-07-19/sysparity_verification_tracker.md`)
and recent cycle logs before picking one:

- **`ont-rulebank-version-current`** is ALREADY DISPOSITIONED -- CTO~Z ruling cycle-27 (`cvoz_sysparity_cycle27_ont_rulebank_version_current.md`,
  and re-confirmed in the check's own printed text): the check is correct to fail, but the gap it seemed to
  represent was ruled MIS-SCOPED against a phantom "behind the source" framing. Not genuinely unverified --
  skipped this tick.
- **`eng-currentstate-current`** is the RECURRING, never-permanently-closed one -- the tracker shows it flipping
  FAIL/PASS across 2026-07-20, 08-20, 09-03 and now 09-10, each time for a DIFFERENT specific cause (the WS-2
  gate is explicitly SOURCE-DRIFT-conditioned, so a fresh FAIL after HEAD moves is by design, not a standing
  defect) -- but "the pattern is known" is not the same as "THIS instance is grounded." Re-grounded it.

## Re-grounding (never trusting the check's own prior report -- Rule 22a)

**What the check actually measures**, read from source rather than assumed (`org/modules/graph/comp_system.py:1554-1582`):
a sha256 content-fingerprint over exactly three source globs -- `.tools/comp-*`, `org/modules/graph/*.yaml`,
`org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/*.json` (260 files) -- compared against the fingerprint
`06_current_state.json` was generated from.

**Last regen, found not assumed:** `git log -1 -- infra/system/06_current_state.json` -> `d876b8b74`, 2026-09-10
11:07:06 -0400 ("discharge(NFRA_CLDGRPH round 8): ... recompiled at the drain").

**Exact drift, named not counted:** `git diff --name-only d876b8b74..HEAD -- <the three _SOURCES globs>` ->
**exactly one file**: `.tools/comp-iam-usage`. Commit `d0c36abcc8`, `build(NFRA_IAMROLES202609.TO-IAM-s-1,
0.9.0_WK_NFRA_IAMROLES202609~1)`: extends `comp-iam-usage` from ROLE grain to a new `permission-cold --role
<name> --lookback <days>` PERMISSION-grain mode (IAM Access Advisor action-level telemetry). The diff is a
real capability addition to the tool's documented interface, not a formatting or comment-only touch -- the
usage line itself gained a new subcommand.

**No in-flight risk (checked, not assumed):** `git status --porcelain -- <the three globs>` -> empty. The
fingerprinted scope carries zero uncommitted changes right now, so a regen at this moment would not launder
any peer's unlanded work (the exact hazard `_dirty_sources()` exists to catch, per tick-32's own banked
lesson in the tracker).

**Verdict: CONFIRMED -- genuine drift, named cause, complete-and-committed source, no blocker.** `ct-count-current`
(comp-tools domain, 7/7 PASS) did not catch this because it checks the tool COUNT (`tools_index_count`), and
this is a MODE addition to an already-indexed tool, not a new entry -- a different axis, correctly silent here.
This is NOT this seat's own scope error and is not a class this seat is claiming as newly discovered; it is
the SAME recurring WS-2 pattern the tracker has logged a dozen times, re-grounded on THIS specific instance
rather than pattern-matched from memory.

## Disposition

**Routine CONFIRMED-drift, per the tracker's own reporting cadence (MSTR 201825Z: exceptions-only) -- no
MSTR/COO nudge.** The regen act itself (`comp-system` regenerate) is WS-2's build mechanism, owned by
whichever lane next touches this surface -- not this seat's to run (CVO verifies; regenerating 06 is a BUILD
act outside the narrow spot-check alignment-metadata carve-out). Nothing in this tick's own L8/L9/L10 CVO
work (`NFRA_OPSEC202609` closed this session; `NFRA_IAMROLES202609`/`NFRA_REPORT` already closed) depends on
this domain reading green -- `system_parity.py` is explicitly a REPORT, not a gate, and confirmed so again
here.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `infra/system/system_parity.py` | fresh check | PASS (2 known FAILs, both dispositioned this tick) | |
| `python org/modules/graph/comp_system.py --check` | the underlying mechanism | PASS (STALE, as predicted, cause named below) | |
| `comp-read org/modules/graph/comp_system.py --for ...` | locate `_SOURCES` / `_source_fingerprint` | PASS | pointed straight to :1562 / :1575 without a manual grep sweep |
| `git diff --name-only <regen-commit>..HEAD -- <globs>` | the /molecule instrument | PASS | one file, one commit, one cause -- exact |
| `git status --porcelain -- <globs>` | the /verify no-in-flight-risk check | PASS | empty; safe-to-regen-whenever confirmed |

**What worked:** going straight to the fingerprint's own source-of-truth (`_SOURCES`, three globs) rather than
guessing at "260 files" let the diff be exact (one file) instead of a noisy full-repo `git diff --stat`.

**What failed:** nothing this cycle.

**Gap found:** none new.

## Next tick

If HEAD is still clean against this fingerprint (no new touches to the three `_SOURCES` globs) at the next
fire, say so plainly per the task's own instruction and do not manufacture work. `ont-rulebank-version-current`
stays skipped (already dispositioned) unless its own disposition is ever revisited by CTO~Z.

— 3.0.0_SA_CVO~Z
