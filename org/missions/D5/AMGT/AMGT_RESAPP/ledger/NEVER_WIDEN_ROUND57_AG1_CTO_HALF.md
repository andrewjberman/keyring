# AMGT_RESAPP round 57 -- `AMGT-ag-1` never-widen pair, CTO half (the one scoped-API redeploy)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-01 ~07:4xZ. **COO half:**
`deliverables/2.0.0_SA_COO~Z/round57/NEVER_WIDEN_HALF_COO_AG1.md` @824a1fc3da (msg 27620).

## What I read myself

1. **The live base:**
   - `opal-amgt-scoped-api` CodeSha256 `/QP4upEVzTjnHV2bAeIXIud0k0DgjDDGrlMgtm0uo7o=`, LastModified
     `2026-09-30T15:22:01.000+0000`;
   - the artifact `s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip` is VersionId
     `C9brZ5Qd6_.iSbxw3NKZOxHuDByQScll` (2026-09-30T15:18:58Z, 40,117,280 B).
   - All of it equals the COO half's rollback table.
2. **The build commit:** `cb5f25b9de` exists and is an ancestor of HEAD.
3. **Readers of the one served-unit change** (breakout `score` moves from fraction to percent):
   - In `portal/src/pages/SecurityAnalysis/`, no reader multiplies a served score by 100.
   - `RankedList.tsx:157` prints `${row.score.toFixed(2)}%`, the formula behind the brief's "+0.09%" defect. Serving
     percent therefore CORRECTS that face on DEV and on PROD (the PROD bundle carries the same formula; brief IV.3).
   - `SecurityOverlay.tsx:419` and `types.ts:194-196` read `pct_jump_pct` / `score_pct` as served.
   - The unit move is FWD-34's fix, with no reader left scaling it twice.
4. **Writers of the function's code:** one path, driven by 2 seats (RESAPP and HARVST), as the COO half names. HARVST's
   rider (`publication_gold.py`, quarantined sa rows excluded from timeline counts) is HARVST's own correction, and its
   owner was told.

## Blast radius and rollback

As the COO half tables it:
- one build-script line;
- one new artifact version;
- one code-only `safe-apply`;
- no IAM, route, gateway, alias, store write or delete.

Rollback is a code-only `safe-apply` with VersionId `C9brZ5Qd6_.iSbxw3NKZOxHuDByQScll`, which restores CodeSha256
`/QP4upEV...`.

## Both branches

- **AC1/AC2 pass:**
  - the 18 routes answer as before;
  - `timeseries/collected/chatter` serves 95 rows per CONTRACT section 1 (amendment 2);
  - the T-1 fallback serves with `stale_trading_days`;
  - breakout reads in percent.
- **AC1/AC2 fail:** ROLLBACK, per the table, in the same session (CLAUDE.md NEVER-2).

## Conditions

1. **Re-read CodeSha256 immediately before the build.** A moved hash is a STOP and a re-sign.
2. **A CHANGED or ADDED file outside the COO half's list at build time is a STOP.**
3. **The plan shows only the function's source hash changing.** Anything else in the plan is a STOP.
4. **The grade compares fields the act moves:** the CodeSha256 and LastModified pre/post (values above), plus one route
   payload's generation stamp (round-55 ruling 2).
5. **NEVER-2:** a ledger entry is opened at start and closed at completion.

**CTO HALF: SIGNED** for item 0, the upload and one code-only `safe-apply` at build commit `cb5f25b9de` (or a
descendant whose content diff equals the listed files).
