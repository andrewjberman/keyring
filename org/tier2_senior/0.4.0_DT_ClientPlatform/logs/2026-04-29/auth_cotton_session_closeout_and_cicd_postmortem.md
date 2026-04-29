# Session Log — 0.4.0_DT_ClientPlatform
## AUTH_COTTON Complete + CI/CD Postmortem
**Date:** 2026-04-29
**Agent:** 0.4.0_DT_ClientPlatform
**Session scope:** AUTH_COTTON.TO2 + TO3 + status hotfix + CI/CD structural fix
**Status:** COMPLETE

---

## Work Completed This Session

| TO | Title | Result |
|----|-------|--------|
| AUTH_COTTON.TO2 | Portal firmAccess.ts Cottonwood allowlist + PROD push | Complete |
| AUTH_COTTON.TO3 | DDB seed — FIRM#cottonwood + USER profile + partner row | Complete |
| Hotfix | USER#user@cottonwood.com missing `status: active` | Complete |
| Hotfix | Remove `/security-scanner` from Cottonwood allowlist | Complete |
| Postmortem | CI/CD gap — pre-push hook + typecheck script + protocol update | Complete |

---

## Compiler Tools

| Phase | Check | Result |
|-------|-------|--------|
| TO2 Phase 1 | Read App.tsx — verify all 11 Route paths | PASS — all 11 confirmed exact string match |
| TO2 Phase 1 | Read firmAccess.ts — confirm no prior cottonwood entry | PASS — clean state |
| TO2 Phase 2 | `git diff firmAccess.ts` | PASS — 14 insertions, 0 deletions, 1 file |
| TO2 Phase 2 | `bun run tsc --noEmit` | EXIT:0 (see postmortem — this check is a no-op; replaced by `bun run typecheck`) |
| TO3 Phase 1 | `aws dynamodb describe-table opal-partner-cottonwood` | ACTIVE — TO1 gate clear |
| TO3 Phase 2 | get-item FIRM#cottonwood META | PASS |
| TO3 Phase 2 | get-item USER#user@cottonwood.com PROFILE | PASS — $2b$ hash, mustChangePassword=false |
| TO3 Phase 2 | get-item opal-partner-cottonwood email row | PASS — firmRole=user, no advisorRole |
| TO3 Phase 2 | scan COUNT | COUNT=1 — PASS |

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | firmAccess.ts — add cottonwood 11-path Set + domain | `bb723f01` portal DEV |
| 2 | portal PROD ff + push | bb723f01, tag portal-v2.1.65 |
| 3 | Workspace pointer bump | `0d94c953a` CLOUD |
| 4 | DDB seed — 3 put-items | FIRM META + USER PROFILE + partner row |
| 5 | status hotfix — `update_item` status=active | USER#user@cottonwood.com patched |
| 6 | Remove /security-scanner from Cottonwood allowlist | `ac5f11b4` portal DEV, portal-v2.1.66 |
| 7 | Workspace pointer bump | `da7366dec` CLOUD |
| 8 | PortfolioBalancePanel TS fix (unblocks CI) | `5898e16e` portal DEV/PROD |
| 9 | typecheck script + CI deploy.yml fix | `ba6abac7` portal DEV/PROD |
| 10 | Portal hooks + DT protocol update | `4aa60190a` CLOUD |
| 11 | Final workspace pointer bumps | `0b57043fc`, `4e3fe7253` CLOUD |

---

## Postmortem — CI/CD Silent Failure

### What happened

After completing TO2 (firmAccess.ts Cottonwood allowlist), I pushed to portal PROD (`bb723f01`) and declared the deployment complete. Andrew reported the live site showing only a background color for Cottonwood users while all other users worked normally. I initially investigated the auth Lambda (CloudWatch logs — no errors), the DDB seed, and then checked GitHub Actions.

**Root finding:** Both PROD pushes (`bb723f01` from TO2 and `ac5f11b4` from the security-scanner removal) had triggered CI runs that **failed** with a TypeScript build error in `PortfolioBalancePanel.tsx`:

```
error TS18048: 'item.amount' is possibly 'undefined'.
error TS2345: Argument of type 'number | undefined' is not assignable to parameter of type 'number'.
```

The live site was still serving the last successful build from 2026-04-28. The Cottonwood `firmAccess.ts` changes had never reached S3/CloudFront.

### Why my local check passed but CI failed

The portal `tsconfig.json` uses TypeScript project references:
```json
{ "files": [], "references": [{ "path": "./tsconfig.app.json" }, ...] }
```

- `tsc --noEmit` (what I ran): reads the root tsconfig, sees `"files": []`, compiles **nothing**. Always exits 0. It is a complete no-op on this repo.
- `tsc -b` (what CI runs via `bun run build`): follows project references, compiles all source under `tsconfig.app.json`. Catches real errors.

This discrepancy meant my local verification was structurally invalid — it could never catch a type error regardless of what the source contained.

A second gap: I did not verify CI status after the PROD push. I called it "deployed" based solely on `git push` succeeding, without checking that the build/deploy pipeline completed.

### Secondary issue — missing `status: active`

The DDB USER PROFILE I seeded was missing `status: "active"`. Every other working account in `opal-users-v2` has this field. The auth handler treats its absence as disabled, returning HTTP 500 "Account disabled". Patched with `update_item` immediately after Andrew reported login failure.

This field was omitted from the TO3 seed spec. Going forward: `status: "active"` must be explicit in every USER PROFILE seed — absence is not safe default.

### Fixes shipped

**1. `portal/package.json` — `typecheck` script**
```json
"typecheck": "tsc -b --noEmit"
```
`tsc -b --noEmit` follows project references (same paths as CI) but skips emit. This is the correct local type check for this repo. The old `tsc --noEmit` is now banned for local portal verification.

**2. `portal/.github/workflows/deploy.yml` — CI Type Check step**
Was: `bun run tsc --noEmit` (same no-op as local).
Now: `bun run typecheck` (runs `tsc -b --noEmit`).
This means type errors now fail the CI at the cheaper Type Check step before the full Vite build runs.

**3. `portal/.git/hooks/pre-push` (+ tracked source in `.tools/portal-hooks/`)**
Intercepts any push to `refs/heads/PROD` and runs `bun run typecheck`. If it fails, the push is blocked with a clear error before the commit reaches GitHub. This is the structural gate — it cannot be forgotten or skipped.

Verified live: the `ba6abac7` PROD push printed:
```
INFO: PROD push detected -- running typecheck (tsc -b --noEmit)
OK: typecheck passed -- proceeding with PROD push
```

Install at session start: `bash .tools/portal-hooks/install.sh` (idempotent).

**4. DT `README.md` — Portal Deployment Sequence**
Added explicit protocol section with `gh run watch` as a mandatory step after PROD push. The rule is stated plainly: *"A push is NOT a deploy. CI failure = live site unchanged."*

### What I should have done differently

- After `git push origin PROD`, run `gh run list --branch PROD --limit 1` immediately and wait for CI to show ✓ before writing "deployed" anywhere.
- Use `bun run typecheck` (or `bun run build`) as the local pre-push check — not `tsc --noEmit`.
- Both gaps are now structurally closed. The hook blocks bad pushes; the protocol requires CI confirmation.

---

## Next Steps

- [2.0.0_SA_COO] AUTH_COTTON.TO4 (smoke test) — awaiting GO. Infrastructure fully ready: portal allowlist live, DDB seeded, status=active confirmed.
- [DT startup] Run `bash .tools/portal-hooks/install.sh` at the top of every session to reinstall the pre-push hook (`.git/hooks/` is not tracked).
- [Backlog] `status: active` field must be added explicitly to all future USER PROFILE DDB seed TOs — surface to COO for TO authoring standard.
