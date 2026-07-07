# 0.7.0_AE_CloudOps~B -- stitch-produce resume: L4 CodeBuild verify catches a real portal/src zip-scope defect

**archetype:** DIAGNOSE
**secondary_archetypes:** IMPLEMENT, COORDINATE

Session start 2026-07-07 ~1310Z (post-reboot re-registration). Window: ~1310Z -> ~1400Z.

## Summary

Resumed the globgrph-stitch-produce deploy (COO DRIVE GO Wave-1, blocked on 0.8.0's extractor fix)
after 0.8.0_AE_CloudComp confirmed commit 75d93eaf7 (extract_eventbridge.py ENAMETOOLONG fix +
recognizer#2) landed + verified on HEAD (`git merge-base --is-ancestor`, not self-report). Manually
triggered the `opal-stitch-produce` CodeBuild project (in-window, rather than wait for tomorrow's
03:00Z EventBridge nightly, which would have breached the ledger's 4h completion window) to close
L4 (first-run content-validity verify).

**Result:** extractor bug confirmed fixed (derive_stitch.py ran cleanly past the old crash point).
But GRAIN-SENTINEL FAILED: REACT_QUERY_KEY 0 vs baseline 32, PORTAL_COMPONENT 0 vs baseline 27,
API_ROUTE 77 vs baseline 263 (0.29x) -- all three outside the [0.4, 2.5]x band.

**Root cause (source-grounded, verify-don't-trust):** downloaded stitch-source/source.zip directly
and inspected its contents -- 0 entries under `portal/src` (org/modules=366, infra/aws=6791,
.tools=160 all correctly present). Cross-checked the live GHA run log (run 28868558323, line 46):
`submodules: false` on the `actions/checkout@v4` step in `.github/workflows/stitch-source-push.yml`.
Deeper: `portal` isn't even a properly registered git submodule -- `git ls-files -s portal` shows a
bare gitlink (mode 160000) with **no corresponding entry in `.gitmodules`** -- so `submodules: true`
alone would not have fixed it either; GH's checkout action has nothing to resolve the gitlink against.
`zip -r ... portal/src` silently zips nothing (the other paths in the same command succeed, so
`set -e` never trips -- no error surfaced anywhere in the 7-run history of this workflow).

## Compiler Tools

| Tool | Use | Result |
|---|---|---|
| comp-which/rail | HUD-nudged mid-session on aws/grep inspections; used native Bash aws s3/logs/codebuild + git for live-state grounding (no comp-tool covers CodeBuild-run-log inspection or S3-zip-content diff) | rail acknowledged; off-rail legitimate for this class of live AWS/GHA forensics |
| deploy_ledger.py (manual .md/.json edit, no CLI subcommand for append-only correction note) | corrected a concurrent-session's presence-only L3 close with a grounded content-invalid finding rather than silently accepting a misleading CLOSED | ledger now accurately reflects L4 OPEN + why |

## Files Modified

- `org/critical_paths/change_management/20260707T1147Z_globgrph-stitch-produce_deploy_completion.md`
  -- appended correction note (L3 proof was presence-only; L4 content-validity check correctly caught
  the portal/src omission). No code changes this window (fix is BASE_EXEC-lane, `.github/**`).

## Blockers

- **globgrph-stitch-produce L4 OPEN** -- needs a BASE_EXEC-committed fix to
  `.github/workflows/stitch-source-push.yml` (a second explicit checkout step pulling
  `Opal-Capital/portal` at the pinned gitlink SHA `b96562720505fa143aad7cc5dd75115e6c609912`, since
  `portal` has no `.gitmodules` registration for plain `submodules: true` to resolve). Routed to
  [2.0.0_SA_COO] 135822Z with the full grounding + proposed patch. Ledger window opened 11:47Z, red
  15:47Z -- not stranded (root cause found + fix specified + routed same-turn), but time-boxed.
- DATA_PLATFORM.DC1/DC2 (orion-crawl, eclipse-crawl) remain correctly PENDING -- checked
  DATA_PLATFORM.DC0.crawl-harness.md status = `active` (not complete), so the DC0.4 live-crawl
  arch-gate hasn't fired and these stay gated behind it per the 2026-07-02 re-slot note. Not
  actionable this window; no action taken (correctly deferred, not neglected).

## Current State (zero-context handoff)

- Registration/watcher: re-registered live this session (was NOT REGISTERED at session start,
  a window-exit artifact); persistent inbox Monitor armed.
- stitch-produce: L1/L2 CLOSED (Terraform applied clean, workflow landed). L3 closed presence-only
  by a concurrent session -- corrected in-record, not reversed (the tool has no reopen primitive;
  the correction note is the durable signal). L4 OPEN pending the portal-checkout fix; re-trigger
  `aws codebuild start-build --project-name opal-stitch-produce` the moment the fix lands.

## Next Steps

- [2.0.0_SA_COO / BASE_EXEC] land the portal-checkout fix in stitch-source-push.yml.
- [0.7.0_AE_CloudOps~B] re-trigger `opal-stitch-produce` CodeBuild immediately once the fix is live;
  confirm GRAIN-SENTINEL passes + stitch_graph.json/marker land in S3; close L4; RAVC2 COO+CTO.
- Watch the ledger window (red 15:47Z) -- escalate louder if the fix hasn't landed by ~15:15Z.
