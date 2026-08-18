# Portal DEV -> PROD promote v2.1.163 -- naming centralization FE legs + declared T-A rider -- 0.4.0_DT_ClientPlatform

**Date:** 2026-08-18 (session ~1520Z-~1817Z; promote window ~1800-1816Z)
**Task Order:** ad-hoc, Andrew-direct at the CTO~X terminal (relayed 175947Z, VERBATIM: *"If everything is ready to go with this, I want you to issue a request to 0.4.0_DT_ClientPlatform for a /prod-deploy ."*) -- recorded here as relayed; scope = this promote, nothing wider
**Status:** COMPLETE -- PROD live at `portal-v2.1.163` (e27dd5fa); payload 3 DECLARED; CI success; served bytes verified with controls
**Archetype:** deploy-promote

---

## Objective

Promote CTO~X's naming-centralization FE legs (8dbaf56b Attribution ETF_NAME_FALLBACKS retirement; 12058841 tickerRegistry displayName strip) DEV->PROD via /prod-deploy, with MSTR executing both shared-branch pushes (LD-0367), CI verified by `gh run view --json`, and a served-bytes acceptance read.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-find | `comp-find 'platinum/advi' portal/src` + `comp-find '49financial' portal/src` | PASS | startup grounding of the ADVI wire path for the 08-22 TO (denominators printed: 10/409, 25+/409) |
| /watcher | armed once at load | PASS | Monitor bppzooji0; delivered every CTO~X/MSTR/COO message this session |
| /prod-deploy | full skill sequence | PASS | this log is its record |
| comp-pipescript io | not run | -- | frontend-only promote; no gold script deployed (DT minimum row does not apply) |

**What worked:** the 08-15 mechanics transferred whole -- exact-ref push handoffs to MSTR (both pushes independently re-derived at their seat before executing), CI enumerated by headSha, annotated-tag peel, served-bytes read with positive controls. Marker validation BEFORE the bundle read caught two bad candidate markers (one string absent from the file I assumed it was in; one surviving in a comment) -- deriving markers from `git show <old>:<file>` vs `<new>:<file>` first is now my standing pre-read step.
**What failed:** `cd "$(git rev-parse --show-toplevel)"` from inside the ephemeral worktree resolved to the WORKTREE (my own 08-15 lesson, re-hit once) -- one dead `cat`/`git -C portal` pair before switching to absolute paths.
**Gap found:** none new.

## Sequence

| Step | Action | Result |
|------|--------|--------|
| 0 | Verify + gate | CTO~X request arrived **Sender-unverified** (unregistered ~X lane); resolved on ON-DISK evidence, not the from-line: cited log `naming_centralization_execute_1840-2000Z.md` exists (mtime precedes the message), both commits on local DEV authored `1.0.0_SA_CTO~X`, stat matches, tracked tree clean. No pending `[STOP]` (both probes + top-level ls; the `~B` dir holds a May-25 lane orient bundle, not mine, not a STOP). Freeze declared to COO 180249Z |
| 1-2 | DEV tree + typecheck | branch DEV, tracked-clean, 0 behind origin; local ahead = exactly the 2 CTO~X commits; `bun run typecheck` rc=0 |
| 1a | DEV push (integrator) | handed MSTR 180348Z; landed 180622Z, VALGATE D-1 PASS; **MSTR CORRECTION: payload = 3, not 2** -- `edcc503e` (DE MDPF_PROVENANCE.T-A) was on origin/DEV since 16:27Z and is 8dbaf56b's parent. My 15:41Z PROD..DEV=0 baseline was stale by one integrator push |
| rider call | edcc503e disposition | MY CALL: proceed with the rider DECLARED (validated+closed T-A, PA-6 zero-pixel @89cf1dc3de; on origin/DEV before my freeze; excluding = banned history rewrite). Declared to COO 180733Z; COO's independent concur crossed mine (180718Z): "widen the declaration, do not strip the commit"; GO stayed mine |
| 3 | re-assert local PROD | `update-ref` no-op, local PROD == origin/PROD 449a6a0e |
| 4 | worktree + merge | `.runtmp/portal-promote-20260818T180416Z`; `bun install` FOREGROUND 420 pkgs rc=0; `merge --no-ff origin/DEV -F <msgfile>` -> **e27dd5fa** (parents 449a6a0e + 12058841); message names all 3 payload commits + Base/Rollback 449a6a0e; **parity `git diff origin/DEV HEAD` = 0 lines** |
| 4d | PROD push (integrator) | handed MSTR 180828Z with 5 re-verify claims; MSTR reproduced all 5 from their seat, pushed 180950Z; my remote read-back: origin/PROD = e27dd5fa |
| 5 | CI + tag | run **32169492889** `Deploy to Production` conclusion=**success** (`gh run view --json`, polled; never `watch`); **1 of 1 workflows on headSha e27dd5fa** (enumerated by sha); tag `portal-v2.1.163` peels (`^{commit}`) to e27dd5fa == PROD head |
| 5b | served-bytes read | fetched served index.html -> entry `index-DyUJgWOr.js` -> ALL **44/44** referenced chunks. NEGATIVE markers (source-validated first: present @449a6a0e, absent @e27dd5fa) `Invesco Variable Rate Preferred` + `Pathfinder Focused Opportunities ETF`: **0 hits** across entry+44. POSITIVE controls `Attribution Breakdown` + `Structured Credit`: hit in `index-CX7Ika0j.js` (the Attribution chunk) -- retrieval discriminates, right chunk in set |
| 6 | gitlink | already 12058841 == portal DEV HEAD (CTO~X's CLOUD bump); 0-line diff -> no bump commit (08-15 precedent) |
| 7 | teardown | `worktree remove` "Filename too long" (documented class; dir persists gitignored+inert); `prune` OK; `worktree list` clean; main tree **DEV** @12058841; cwd workspace root |
| 8 | reports | CTO~X ask-3 report 181624Z; COO completion + FREEZE RELEASE 181637Z |

## Decisions Made

- **Acted on a Sender-unverified request only after grounding it on committed artifacts** (the log + the authored commits) -- the from-line proved nothing; the object DB did.
- **Rider edcc503e: proceed-with-declaration, not hold** -- validated+closed work, pre-freeze on origin/DEV, structurally inseparable (parent of the payload); holding for permission nobody required would be an inferred gate. COO's independent concur crossed in flight.
- **No audited override on either push** -- same grounds as 08-15/earlier today; both pushes routed to MSTR with re-verify data, both independently re-derived before execution.
- **No gitlink bump commit** -- pointer already paired; an empty commit dressed as a record adds nothing.

## Files Modified

- portal: `refs/heads/DEV` -> origin (12058841, MSTR push 1); `refs/heads/PROD` -> e27dd5fa (merge, MSTR push 2); tag `portal-v2.1.163` (CI-minted)
- workspace: none this promote (gitlink pre-paired); this log
- scratchpad (session-local, not committed): served-bundle chunk set + markers

## Blockers

None. Both LD-0367 handoffs resolved in <3 minutes each.

## Surprise channel (one line each, no action)

1. My 15:41Z baseline went stale within one integrator push (edcc503e 16:27Z) -- for the 08-22 P4-PROMOTE-49F I will re-measure PROD..DEV at GO-time, never carry a baseline across hours.
2. Earlier this session: worktree-residual thread (stale `_portal_hotfix_wt`) closed end-to-end -- MSTR reaped the worktree, deleted merged remote branch `hotfix/global-monthly-axis-key` on my verified decision, validated from my seat with a positive control.

## Current State

PROD = `portal-v2.1.163` @e27dd5fa, live and served (bytes verified with controls). Main portal tree on DEV @12058841 == origin/DEV; PROD..DEV = 0 again (P4X-1 baseline exact for 08-22). Freeze released. Pending TO: OPAL_ADVIPOINTERS.P4-PROMOTE-49F @744841dba1, executes on DE's P4R-5 handoff 08-22.

## Next Steps

1. `[1.0.0_SA_CTO~X]` -- run their independent PROD bundle-marker validation (ask-3 data delivered 181624Z).
2. `[0.0.0_AB_MSTR]` -- push CLOUD (this log commit) as integrator.
3. `[me, 08-22]` -- P4-PROMOTE-49F on DE's P4R-5 handoff; re-measure PROD..DEV at GO-time.
