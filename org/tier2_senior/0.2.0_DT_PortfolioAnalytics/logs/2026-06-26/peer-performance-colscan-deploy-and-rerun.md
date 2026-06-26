# yang-generate-peer-performance col-scan fix — deploy + wide-source force-rerun (yang-v2.4.13)
**archetype:** DEPLOY

**Agent:** 0.2.0_DT_PortfolioAnalytics
**Date:** 2026-06-26
**Window:** 16:02Z -> 16:20Z; ~14 MCP messages, 1 deploy/tag, 1 wide-source rerun

## Summary

Andrew-direct: /Peers tab Model toggle missing ST/LTC/LTA. DE diagnosed to the PRODUCER
(yang-generate-peer-performance parse_peer_excel hardcoded section columns [0,20]; the wider
06-18 source has its 2nd block at col 26, so col-26 models ST/LTC/LTA were silently dropped).
DS committed the fix (d4ae41b84, dynamic Return/Risk header scan) as data-owner; DT deployed +
force-reran. /Peers data now correct (5 models) at 06-18 vintage, end-to-end proven.

## What happened

1. **Lane coordination:** DE handed off (gate-blocked as DE on infra/aws/lambda). DS CLAIMED the
   parser commit (data-correctness lane), I HELD (only reviewed the diff). DS committed d4ae41b84;
   I took TF deploy + rerun. Clean split — no override needed by me on the source.
2. **Independent grounding (not self-report):** DS source-confirmed the fix load-bearing on the
   exact archive file — pre-fix parser -> 2 models [INT,UST] (== broken served artifact), post-fix
   -> 5. I verified the final served artifact directly (below).
3. **Deploy (override-FREE):** build-and-upload -> sha ww5iYBD/BU+XCbPXMkzW9hNdumptIjwCvxPklXHnhj8=;
   committed source map + CHANGELOG with NO GIT_COMMIT_AUTHOR_OVERRIDE (via the YANG_PIPELINE_DEPLOY
   lane landed earlier this session, 6cf07635b) -- gap-close validated in a real deploy. safe-apply
   1-change -> 0-diff. F5 live CodeSha256 == artifact. Tag yang-v2.4.13. Ledger closed.
4. **Dangling-manifest finding (DE + DT + DS convergent):** manifest json/latest/peer_excel.json
   s3_key = uploads/...20260618.xlsx but that key was rotated out of uploads/ after the 06-21 run
   (only the narrow 202512 file remained). A naive rerun would NoSuchKey or regress /Peers to stale
   Dec-2025 data. The wide 06-18 file (577188B, col-26 layout) survived in archive.
5. **Force-fix (Andrew chose force-now via AskUserQuestion):** restored the wide file
   archive(exec-ef9c2e9f2b37) -> uploads/...20260618.xlsx (repairs the dangling pointer) + direct-
   invoked peer-performance with manifest peer_excel=that file (deterministic, bypasses SFN
   selective-branch uncertainty). StatusCode 200, model_count 5. CF invalidated.

## Deployment Sequence + Verification (actual output)

```
build sha:       ww5iYBD/BU+XCbPXMkzW9hNdumptIjwCvxPklXHnhj8=
TF plan/apply:   ~ generate_peer_performance source_code_hash -> ww5iYBD...; 1 change; 0-diff "No changes"
F5 live:         CodeSha256 ww5iYBD/BU+XCbPXMkzW9hNdumptIjwCvxPklXHnhj8=  2026-06-26T16:14:50Z
Tag:             yang-v2.4.13 (origin/CLOUD)
Rerun invoke:    StatusCode 200, FunctionError None, model_count 5 (wide 06-18 source)
SERVED VERIFY (json/peers/peer_performance.json, authoritative):
  models = {INT, LTA, LTC, ST, UST} (5); data_as_of 2026-06-18 (correct vintage)
  col-26 pair LTA+LTC present + ST present (the exact 3 the old [0,20] dropped)
  INT 1Y: model=6.3888 bm=7.7631 p50=6.6365  == DE/DS target EXACTLY
  => same wide file: old code=2 models, new code=5 -> fix proven load-bearing on the SERVED artifact
CF invalidate:   live dist EVTSA9VEHNZVH InProgress (dead E2LPCXXBLDGWXY NoSuchKey, pre-existing harmless)
```

## Compiler Tools

| Tool | Target | Result | Note |
|---|---|---|---|
| comp-blast | yang-generate-peer-performance | PASS | blast radius = json/peers/peer_performance.json -> portal_data_proxy -> portal; pure parser fix, no new edges/IAM. Rule 20 pre-infra check |

Gap: none new. (comp-pipescript io is OUT-OF-SCOPE for this globgrph-owned lambda, as with the
benchmarks one -- known boundary.)

## Files Modified

Parser fix d4ae41b84 (DS-authored/committed). My commits: 387ff121d (source map), record-deploy
CHANGELOG, 464f2ee9c (deployment_map -> yang-v2.4.13). All override-free via YANG_PIPELINE_DEPLOY.

## Blockers

None.

## Current State

- yang-generate-peer-performance LIVE with the col-scan fix (CodeSha256 ww5iYBD..., yang-v2.4.13).
- Served json/peers/peer_performance.json = 5 models {INT,LTA,LTC,ST,UST}, data_as_of 06-18,
  INT 1Y model=6.3888. /Peers Model toggle data is correct.
- Dangling manifest pointer REPAIRED: the wide 06-18 file is back at uploads/...20260618.xlsx
  (matches json/latest/peer_excel.json s3_key).
- CF invalidation InProgress (~5-10min to fully serve fresh).

## Next Steps

- [0.2.0_DS_PortfolioAnalytics] independent served-data verify (proof gate) — confirm 5 models +
  null/magnitude sanity.
- [0.2.0_DE_PortfolioAnalytics] /Peers visual: confirm all 5 models render in the Model toggle
  once CF clears.
- [0.5.0_AE_OpalETL / 0.7.0_AE_CloudOps] (low-pri, on record) the manifest-pointer-dangling-after-
  uploads-rotation pattern + the dead CF distribution id E2LPCXXBLDGWXY in yang-invalidate-cloudfront.

---

## ADDENDUM — yang-v2.4.14 period-map redeploy (false-green correction)

Andrew flagged the peer NUMBERS looked wrong. Root cause = a SECOND, deeper bug: the wide
06-18 workbook added leading 1Day+MTD periods (3 cols each), shifting every period column right
by 6; the parser's hardcoded stat offsets [1,4,7,10,13,16] read the WRONG period for every cell
(served "1Y" was actually 1-Quarter; Since Inception never read). DS fix b72df1095 maps period
-> stat-col by HEADER LABEL (build_period_stat_cols). Deployed yang-v2.4.14 (sha
qhjMKxByTyspQpCJY9zz3KiM0YYTwdh46k7s95l+Z1A=, 0-diff, F5-verified, ledger closed, override-free)
+ reran wide source.

SERVED VERIFY (corrected): INT 1Y 6.3888->14.4275; UST 3.802; ST 4.1995; LTC 20.0293; LTA
22.4009; Since Inception POPULATED all 5 (was null). All 5x6 present.

**FALSE-GREEN LESSON:** the yang-v2.4.13 "verify PASS" matched target INT 1Y=6.3888 — but that
target was computed by the SAME buggy offset code (DE's local parser + deployed parser shared the
offset bug), so it was self-consistently WRONG. A numeric verify target derived from the same
code path is NOT independent verification. This pass verified against an invariant the bug could
not satisfy (Since Inception non-null) + corrected absolute values. See memory
[[diag-verify-target-from-same-buggy-code-is-false-green]].
