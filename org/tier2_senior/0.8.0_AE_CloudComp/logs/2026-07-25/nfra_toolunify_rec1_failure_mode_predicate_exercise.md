# NFRA_TOOLUNIFY REC-1 — Predicate-Exercise the Register's failure_mode Column — 0.8.0_AE_CloudComp~D

**Date:** 2026-07-25
**Task Order:** NFRA_TOOLUNIFY.REC-1 (MCP dispatch, no XML TO filed — off-main-fabric census group per plan §3.1)
**Status:** COMPLETE

---

## Objective

Fleet-wide power-crash respawn session. Startup (watcher self-heal, `org/XXX.md` protocol) followed by the
queued dispatch from `1.0.0_SA_CTO~Z`: predicate-exercise the §2.D census register's `failure_mode` column
(currently AST-derived, never run against real input) against a sample of tools, seeded by the six §0.2
through-line silent-failure instances, with a positive-control + mutant acceptance gate per Rule 22a
discipline.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| `comp-manifest-check` | `check --file <synthetic> --mode blocking` | PASS | positive control — DECLARED LOUD, OBSERVED LOUD (rc=1, BLOCKED) |
| `comp-manifest-check` | `selfcheck` | PASS | AC4 synthetic anti-pattern self-test, 3 findings, 0 FP, used to derive the probe file's violation classes |
| `comp-manifest-check` | `existence` | PASS | 65 registered tools exist + git-tracked, used to sanity-check the tool before the real exercise |
| `comp-iam` | `service nonexistent-lambda-zzz-9999` | PASS | DECLARED FAIL-OPEN, OBSERVED matches (rc=0, human-readable note, no script-visible signal) |
| `comp-iam` | `simulate-self-test` | PASS | context only — confirms the newer `simulate` subcommand is well-guarded (4/4 labeled mutant cases pass); a different code path from `service`/`gaps` |
| `comp-freshness` | `artifact <nonexistent-s3-prefix>` | WARN | DECLARED LOUD, OBSERVED WARN/rc=0 on total absence — mismatch, flagged §5.1 of REC1_EXERCISE.md |
| `comp-glob` | `<0-match pattern> .` | PASS | DECLARED FAIL-OPEN, OBSERVED matches (rc=0, explicit labeled NO MATCH block) |
| `python3 infra/aws/globgrph/derive_stitch.py --out <scratch>` | direct read-only producer invocation | FAIL (by design) | mutant — DECLARED LOUD, OBSERVED LOUD at tool level (rc=2, GRAIN_SENTINEL_FAIL); SILENT-EMPTY at the production call site (post-commit hook discards it) — the headline finding |

**What worked:** `comp-manifest-check selfcheck`/`existence` gave a fast, safe, built-in way to derive a known
anti-pattern probe file without hand-guessing violation syntax. `comp-iam simulate-self-test` and
`comp-freshness`'s own printed exit-code contract in its `--help` text made classifying LOUD vs
WARN/FAIL-OPEN mechanical rather than judgment-based for those two.

**What failed:** two idiom-2 tools (`comp-freshness`, `comp-glob` — shebang-file-is-the-entry per D.md §3.1)
threw bash syntax errors when I first invoked them as `bash .tools/comp-X` instead of `python3 .tools/comp-X`
— an exerciser-side mistake, not a tool defect. Logged in REC1_EXERCISE.md §6 rather than silently discarded.
`comp-manifest-check completeness` hung past a 60s timeout on a bare invocation (likely a heavier
routable/self-routes sub-scan); worked around by using the faster `existence` + `selfcheck` subcommands
instead of diagnosing the hang (out of scope for this dispatch).

**Gap found:** the register's `failure_mode` column is a per-tool property with no way to represent that a
LOUD tool's only production call site can discard the signal entirely (comp-stitch-refresh case). Recommended
to CTO~Z/CVO~Z as a candidate register dimension, not actioned this session (read-only scope).

Appended to `org/compiler-tools-log.md`.

---

## Work Completed

### 1. Startup / fleet respawn

Registered `0.8.0_AE_CloudComp~D` (was NOT REGISTERED post power-crash), armed the persistent inbox Monitor
(`org/mcp/inbox-watch.sh` — noted this shell resolves absolute paths as `/cygdrive/c/...`, Cygwin-style, not
the `/c/...` Git Bash convention the `/watcher` skill assumes; used the correct path, Monitor confirmed live
and delivered the queued dispatch), wrote the session-keyed serial file (LD-0290), ran the audit-archive
invoker (0 findings), confirmed the owned-paths hook + `.comp-graph/.agent_context`, read recent logs +
`prompt.md` + `ORG_CHART.md` per `org/XXX.md` Steps 1-4. No stale cron found.

### 2. REC-1 exercise

Read `D.md`/`D.sidecar.json` (own prior census deliverable) and `CONSOLIDATED_ESTATE_MAP.md` §0.2 to identify
the six through-line silent-failure instances and confirm zero rows in the 92-tool register currently carry
`failure_mode=SILENT-EMPTY` (checked via grep across `D.md`, `D.sidecar.json`, `D.raw_evidence.json` — all
zero hits outside the vocabulary-definition line). Selected `comp-stitch-refresh` as the mutant (safest,
most concretely register-mapped of the six) after confirming via source read that its wrapper always
publishes to S3 with no dry-run flag, then exercised its underlying `derive_stitch.py` directly (confirmed
read-only via source read — no `put_object`/`upload_file` calls) instead. Ran the positive control
(`comp-manifest-check`) and mutant as separate invocations per Rule 22a. Sampled three more tools spanning
declared `LOUD`/`FAIL-OPEN`. Full detail, verbatim outputs, and the sidecar are in
`org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_TOOLUNIFY_CENSUS/REC1_EXERCISE.md` +
`REC1_EXERCISE.sidecar.json`.

**Headline finding:** `comp-stitch-refresh`/`derive_stitch.py` is genuinely LOUD at the tool boundary
(confirmed live: rc=2, explicit `GRAIN_SENTINEL_FAIL` stderr, matching the register's HIGH-confidence LOUD
declaration) — but its only production call site, `.tools/git-hooks/stitch-refresh-post-commit.sh:26`,
backgrounds it, redirects all output to a tmp log, and unconditionally `exit 0`s. Corroborated independently
via the pre-existing `stitch-refresh.log` (166 `GRAIN_SENTINEL_FAIL` lines = 83 commits, matching the estate
map's "83 straight since 07-08") and the live S3 marker's `LastModified=2026-07-08` (17 days stale, and
proof this exercise wrote nothing). **`failure_mode` is a per-tool property; a LOUD tool behind a
signal-discarding call site is operationally indistinguishable from SILENT-EMPTY** — this generalizes past
the census's own current scope and is the primary recommendation forwarded to CTO~Z/CVO~Z.

**Secondary finding:** `comp-freshness artifact` on a wholly nonexistent S3 prefix returns `STATUS=WARN`,
`rc=0` ("WARN alone does not block dispatch" per the tool's own `--help`) — a declared-LOUD row that does not
hold for the total-absence case on first individual verification. Flagged as input to the still-open §0.2
sixth-instance investigation (are the 9 freshness/vintage/absence-probe source dirs served elsewhere), not
asserted as a broken pipeline (NEVER-rule #1 discipline — absence of a Lambda deployment is a distinct
question from whether the local `comp-freshness` gate itself under-alarms on absence).

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Exercise `derive_stitch.py` directly instead of the `comp-stitch-refresh` wrapper | The wrapper always publishes to S3 on invocation with no dry-run flag (confirmed via source read); the plan's read-only discipline (§3.2) and this lane's own safety constraint rule out a production write for a test probe. |
| Treat the mutant result as two-layer (tool vs. call-site) rather than forcing a single LOUD/SILENT-EMPTY verdict | The clean binary the acceptance gate asks for would have misrepresented what was actually found — the tool genuinely is LOUD; the silence is a property of the invocation wrapper, not the tool. Reporting both layers is more accurate and more actionable than picking one. |
| Sample 5 tools (v1) rather than sweep the full 92-tool register | Matches the dispatch's own explicit scope ("one change-type is enough... does not need the full L0b vocabulary yet... for a sample of tools"); each exercise needed idiom identification + (for the mutant) a call-site trace, which is manual-inspection depth, not scriptable at full-register scale in one light cycle. |
| Did not diagnose the `comp-manifest-check completeness` 60s hang | Out of scope for REC-1; worked around with faster subcommands (`existence`, `selfcheck`) that answered the same positive-control question. Noted in the log so it isn't silently lost. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_TOOLUNIFY_CENSUS/REC1_EXERCISE.md` | New — full REC-1 write-up | No — owned-paths gates this tree to CTO~Z's BASE_EXEC lane; written to disk for CTO~Z to commit, per this lane's established D.md §8 convention |
| `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_TOOLUNIFY_CENSUS/REC1_EXERCISE.sidecar.json` | New — per-invocation raw results, verbatim output | No — same as above |
| `org/tier2_senior/0.8.0_AE_CloudComp/logs/2026-07-25/nfra_toolunify_rec1_failure_mode_predicate_exercise.md` | This log | Pending — committed this session under `0.8.0_AE_CloudComp~D`'s own lane |

---

## Blockers

None.

---

## Current State

REC-1 delivered. Acceptance gate satisfied: positive control (`comp-manifest-check`) reads LOUD as declared;
mutant (`comp-stitch-refresh`/`derive_stitch.py`, one of the six §0.2 through-line instances) reads LOUD at
the tool boundary and SILENT-EMPTY at its only production call site, both exercised and independently
corroborated (166 historical log lines, live S3 marker vintage). Three more tools sampled
(`comp-iam`/`comp-freshness`/`comp-glob`) spanning declared LOUD/FAIL-OPEN; `comp-freshness` surfaced a
second genuine declared-vs-observed mismatch. Denominator (5/92, v1 sample) stated explicitly in the
deliverable, nothing silently dropped. Files sit on disk at the CTO~Z-owned deliverables path per
established convention (not committed by this lane); this log is committed under my own lane's ownpath.

---

## Next Steps

1. **[1.0.0_SA_CTO~Z]** Commit `REC1_EXERCISE.md` + sidecar into the owned deliverables path; decide whether
   the per-tool-vs-call-site distinction (§4c) becomes a register dimension or a separate WS-item.
2. **[3.0.0_SA_CVO~Z]** Re-verify the positive-control + mutant pair per the acceptance-gate bar; both are
   independently re-derivable from the sidecar's raw output + the cited log/S3 evidence.
3. **[0.8.0_AE_CloudComp~D]** Event-driven, standing by. No self-initiated follow-on pending.
