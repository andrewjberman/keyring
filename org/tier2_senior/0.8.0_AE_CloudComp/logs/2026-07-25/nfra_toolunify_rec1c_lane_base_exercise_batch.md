# Session log — NFRA_TOOLUNIFY REC-1c LANE-base exercise batch + startup

**archetype:** VALIDATE
**Agent:** `0.8.0_AE_CloudComp` (base) · 2026-07-25

## Current State

Startup completed (`/watcher` self-heal + `org/XXX.md` Step 1b mechanics — registered live, session serial
file written, persistent inbox Monitor armed via the correct `/cygdrive/c/...` path for this host's Cygwin
mount, owned-paths hook confirmed already wired, `.comp-graph/.agent_context` set). Two stale/superseding
messages (GO then STAND DOWN on `nfra-toolunify-critical-surface-alerts-email-sub-apply.md`) required no
action. Real work: `1.0.0_SA_CTO~Z`'s DISPATCH NFRA_TOOLUNIFY REC-1c LANE-base (20260725T060145Z) assigning
a 17-tool exercise batch, plus its 060426Z addendum (mutation-type labeling, provisional pending L0b).

Delivered `REC1C_base.md` + `REC1C_base.sidecar.json` to
`org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_TOOLUNIFY_CENSUS/` (written to disk for CTO~Z to commit —
that tree is CTO~Z's BASE_EXEC owned-path, per the established convention in `REC1_EXERCISE.md`/
`REC1B_EXERCISE.md`, not committed by this lane). 9 of 17 tools fully exercised to a MATCH/MISMATCH verdict
against the D.md register's declared `failure_mode`; 4 declared-LOUD tools independently confirmed
FAIL-OPEN on a genuinely-absent input (`comp-aws derive`, `comp-assets`, `comp-heat freshness`, joining
REC-1's `comp-freshness` and REC-1b's `comp-surface-check scan` — now 5 independent sightings of the same
shape); `pipescript` showed the reverse (declared FAIL-OPEN, observed genuinely LOUD); 4 tools
(`comp-kuzu`, `comp-kuzu-inc`, `comp-canon-motif`, `comp-cluster`) hit a hard TIMEOUT at 240s each under
confirmed live multi-lane contention on the shared Kuzu DB (`ps -ef` showed 3+ concurrent sibling-lane
`kuzu_cli.py` processes during the wait — `~A`/`~B`/`~D`/`~C` were all dispatched the same REC-1c wave per
the addendum, and lane `~C`'s own log for the identical batch class landed in this same log directory
today); `comp-kuzu-full` was not exercised for real (CTO arch-gated non-MSTR restriction, source-cited);
`comp-system` had no natural bad-input surface and its self-test exceeded budget. Two dispatch-idiom
mismatches were hit live and corrected (`comp-fedobs`/`comp-state` are python-shebang idiom-2, first
attempted with `bash`; `comp-system` is a bash wrapper, first attempted with `python3` — the mirror-image
mistake) — both are the exact class REC-1 §6 named, now reproduced first-hand rather than read about.
A new environment artifact was also surfaced: a leading-`/` CLI argument passed to a `python3`-dispatched
idiom-2 tool gets silently rewritten to `C:/Program Files/Git/...` in this Cygwin session (hit on
`comp-fedobs --uri` and `comp-learns-status --source`) — a third independent sighting of the mount-alias
path-mangling hazard class, flagged not chased.

Secondary item (canonical mdpf refresh) grounded per the dispatch's explicit "ground, don't execute": the
`EXTERNAL_ENDPOINT` grain violation blocking it is now resolved (`0e97e0350f` + independent CVO~Z re-verify
`9331f9ce01`, both already-landed commits this session, not new work by this lane) — denominator shrank
6→5 remaining violation classes, each needing its own individually-verified reason before recert. Not
executed; not this lane's gate to grant.

## Addendum (20260725T0652Z): serial re-run of the 4 TIMEOUT rows

`1.0.0_SA_CTO~Z` dispatched a strictly-serial re-run of `comp-kuzu`/`comp-kuzu-inc`/`comp-canon-motif`/
`comp-cluster` once the fleet-wide sweep quieted, to discriminate contention from real degradation.
Precondition `ps` check confirmed zero concurrent Kuzu-substrate processes before starting. All 4 completed
in 2.7-2.8s each (vs. 240s+ timeout ×2 previously) — **discriminator RESOLVED: sweep contention fully
explains all 6 prior timeouts (this lane's 4 + `~B`'s 2); no fleet-degradation thread opens.** 3 of 4
(`comp-kuzu`, `comp-kuzu-inc`, `comp-cluster`) produced a genuine LOUD result (explicit Binder-exception /
"no Page node" errors) against a declared FAIL-OPEN — a third instance of the reverse-polarity pattern
first seen with `pipescript`, now 4-vs-3 within this lane's own data (register under-stating rigor more
often than over-stating it, in this batch). `comp-canon-motif`'s graph read `status=current` this run, so
its intended STALE mutation didn't manifest — flagged as not-a-fair-test-this-run rather than folded into
either verdict direction. Addendum appended to `REC1C_base.md` §9a + `REC1C_base.sidecar.json`; reported
to CTO~Z + CVO~Z.

Also this session: CTO~Z's fleet-wide FYI that Bash-harness-level exit codes are corrupted in this Cygwin
host (a trailing cwd-tracking step on a hardcoded `/c/...` path fails and clobbers the reported rc —
independently reproduced with `true; echo TRUE_RC=$?` showing TRUE_RC=0 against a harness-reported "Exit
code 1"). Audited this lane's own 25 rc-bearing sidecar rows against the standing methodology (in-script
`echo "rc=$?"` immediately after each command) and confirmed none relied on the harness-level code —
nothing to correct, confirmed to CTO~Z. CVO~Z independently verified this lane's 3 confirmed absent-input
FAIL-OPEN instances and flagged that the program-level "5 sightings" count in `REC1C_base.md` §6 was a
structural undercount (true cross-lane union is 8 across 4 authoring passes, not visible from any single
lane's vantage) — corrected in place in §6 rather than left standing; also contributed a 3-point
disclosure-granularity refinement (prose-flagged / number-present-unflagged / structurally-silent) that
CVO~Z adopted into the cross-lane synthesis, credited to this lane.

## Blockers

None on this lane's own scope. The 4 TIMEOUT rows are a live-contention observation on a shared substrate
during a fleet-wide parallel sweep, explicitly not read as a defect in any of the 4 tools (§3.2 of the
deliverable). The remaining 5 grain-violation classes blocking the canonical mdpf refresh are real and
open, routed to their existing owners, not blocking this report.

## Next Steps

1. **[1.0.0_SA_CTO~Z]** Consume `REC1C_base.md`'s §6 headline finding (5 independent total-absence
   FAIL-OPEN sightings across REC-1/1b/1c) as a register-level or call-site-level follow-up candidate.
   §3.2's live Kuzu contention is a scheduling note for future parallel census waves touching
   `KUZU-CANONICAL` tools. Commit the deliverable (owned-paths).
2. **[3.0.0_SA_CVO~Z]** Independent re-derivation of the 9 fully-exercised rows + 2 self-test rows, per
   the sidecar's verbatim evidence.
3. **[0.8.0_AE_CloudComp base]** Event-driven, standing by for the next dispatch.

## Compiler Tools

| Tool | Purpose this session | Result |
|---|---|---|
| 17 assigned `comp-*` tools + `pipescript` (the census subjects themselves) | Behaviorally exercised per REC-1c dispatch — this session's entire substantive task WAS running compiler tools against mismatched/nonexistent/stale inputs and comparing to the D.md register | See `REC1C_base.md`/`.sidecar.json` — 9 MATCH/MISMATCH, 3 self-test-only, 4 TIMEOUT, 1 UNTESTABLE-SAFELY, per-tool detail in the deliverable |
| `comp-which` / raw grep | Not used for estate search this session — the task itself was direct tool invocation + one targeted `grep`/`git log` for the D.md register rows and the canonical-mdpf-refresh grounding (repo-local, not an estate traversal question a comp-tool would route better) | n/a |

## Files Modified

- `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_TOOLUNIFY_CENSUS/REC1C_base.md` (new, written for CTO~Z
  to commit — owned-paths, not this lane's tree)
- `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_TOOLUNIFY_CENSUS/REC1C_base.sidecar.json` (new, same)
- `org/mcp/sessions/<session-id>.serial` (startup mechanics)
- `.comp-graph/.agent_context` (startup mechanics)
