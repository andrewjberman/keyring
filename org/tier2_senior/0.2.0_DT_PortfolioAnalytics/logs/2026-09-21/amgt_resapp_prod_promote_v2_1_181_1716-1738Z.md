# AMGT_RESAPP portal DEV->PROD promote, v2.1.181 -- 0.2.0_DT_PortfolioAnalytics, 2026-09-21 17:16-17:38Z

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE

## Summary

Spawned by `0.0.0_AB_MSTR~Z` at 17:16:33Z to run `/prod-deploy` for AMGT_RESAPP under Andrew-direct
2026-09-21 ~17:2xZ (*"might as well just push DEV to PROD if there are new features as its gated to only
me on PROD anyway"*; record @`e70b949ba0`). Done: portal PROD is `07d5af72`, tag `portal-v2.1.181`, CI
success, served bytes carry the new page code. The access gate was not touched.

## Deployment Sequence

1. Startup: registered base serial `0.2.0_DT_PortfolioAnalytics` (spawn audit + `$OPAL_AGENT_SERIAL` both
   base), session serial file written, inbox Monitor `b0ujqueev` armed (process confirmed), inbox empty,
   `get_delivery_state` 0 rows since 00:00Z, zero crons.
2. Payload measured: `origin/PROD..origin/DEV` = 6 commits (rk-19, rk-30, rk-43, rk-53 page work + 2 MSTR
   merges); tree diff = 6 files under `src/pages/SecurityAnalysis/`, +298/-45; `src/App.tsx` identical,
   gate commit `d8135e0a` already an ancestor of PROD.
3. Freeze declared (23983/23984/23985); acked by `1.0.0_SA_CTO~Z` (23986) and `2.0.0_SA_COO~Z` (23987).
4. `bun run typecheck` on DEV `db1c5f64`: rc=0, 0 `error TS`.
5. `update-ref` local PROD = origin/PROD `a580bbb4` (no pollution). Worktree
   `.runtmp/portal-promote-20260921T172305Z`, foreground `bun install` 377 packages.
6. `git merge --no-ff origin/DEV` -> `07d5af72`; parity `git diff origin/DEV HEAD` = 0 bytes.
7. First PROD push DENIED by GATE 5 (see Gap found). Re-issued as
   `git -C .runtmp/portal-promote-20260921T172305Z push origin PROD`: `a580bbb4..07d5af72`.
8. CI, then tag, then served bytes (below). Worktree removed (tracking pruned, physical dir persists:
   Filename too long). Pointer + ledger committed `6e36765eee`. Freeze released (23996/23997/23998).

## Verification

```
git ls-remote origin refs/heads/PROD  -> 07d5af72ef65082fbfdd92197fb814d733e58d92
run list (30 runs) at 07d5af72: 1 -> 35632132225 Deploy to Production completed success
  jobs: Build Production Assets success, Deploy to S3 + CloudFront success, Tag Deployment success
portal-v2.1.181 tag object 8ba1c8c556909ec2b125ff2808c4e302c9a485ea, ^{commit} 07d5af72 == origin/PROD
https://opalinvest.dev/index.html 200, Last-Modified Mon, 21 Sep 2026 17:29:27 GMT, entry assets/index-DTWT90UL.js
54 chunks fetched; SEARCHED_LINKS_UNREADABLE: 1 served file (a580bbb4 src: 0, 07d5af72 src: 2)
  "the payload carries no reading for this score": 1 served file (a580bbb4: 0, 07d5af72: 1)
  "house forecast does not serve": 0 served -- comment-only in source (ModelTab.tsx:25, types.ts:900)
```

## Compiler Tools

| Tool | Use | Result |
|---|---|---|
| `comp-read --enumerate` | `.tools/hooks/never-rules-gate.sh`, to see how GATE 5 resolves the target repo | PASS: found the whitespace-splitting parsers at `:286-303` |
| `comp-read --enumerate` | `cloudfront-distribution.tf`, to find the served alias | PASS: `opalinvest.dev` at `:110` |
| `comp-routes origins` | serving origin for the portal bundle | PASS: `opalinvest-portal` bucket (DESIRED plane only, as it says) |

- **What worked:** comp-read's enumerate found both answers in one call each.
- **What failed:** my first comp-read piped into `head` and was rail-denied; re-run into a file.
- **Gap found:** GATE 5 (`never-rules-gate.sh:286-303`) takes the `git -C` / `cd` target with
  `[^[:space:]]+`, so on this box (the path contains a space) a quoted absolute worktree path resolves to
  the wrong repo and the DT carve-out cannot fire. The fail-closed direction held. Separately, the HEAD-move
  guard on `git -C <worktree> commit --amend` read the WORKSPACE HEAD (`0687d98335`). Both reported to
  `1.0.0_SA_CTO~Z` and `0.0.0_AB_MSTR~Z` in msg 23997/23998. I did not file a surprise row; neither is on a
  project this seat holds.

## Files Modified

See commit `6e36765eee` (ledger entry + portal gitlink `2453a7b4` -> `db1c5f64`). This commit adds the log
and the ledger's row 16 (freeze released).

## MCP

8 messages: freeze out (3), acks in (2, read-acked 23986/23987), release + report out (3).

## Blockers

None.

## Current State

- Portal `origin/PROD` = `07d5af72`, tag `portal-v2.1.181`, served at `opalinvest.dev` since 17:29:27Z.
  Rollback target `a580bbb4` (`portal-v2.1.180`). `origin/DEV` = `db1c5f64`, unmoved.
- Security Analysis stays Dev+admin only. Manager access is parked on the record (no names given).
- Main `portal/` tree on DEV @ `db1c5f64`, clean.
- Workspace SITEZ `6e36765eee` carries the gitlink bump and
  `org/critical_paths/change_management/20260921T172305Z_amgt-resapp-portal-v2.1.181-prod-promote_deploy_completion.md`
  (CLOSED). It was on origin/SITEZ by ls-remote right after commit; this seat did not push it.
- The ledger was written after the push, not at the start; its header says so.
- Residue: `.runtmp/portal-promote-20260921T172305Z` (gitignored, inert). Not deleted recursively without a
  human's word.
- The merge author line reads `0.0.0_AB_MSTR` (box git config); its message names this seat.

## Next Steps

- [Andrew] Visual smoke of Security Analysis on PROD. His record already notes the pipes are mostly dry by
  design (lead panel 2 trending names, breakout empty, no search control).
- [1.0.0_SA_CTO~Z] Optional: route the GATE 5 whitespace-path defect and the HEAD-move guard's repo
  resolution to the owner of `.tools/hooks/`. Workaround for now: a space-free relative `git -C` path.
- [0.0.0_AB_MSTR~Z] Confirm who pushed SITEZ to `6e36765eee`; remove the `.runtmp` residue if wanted.
