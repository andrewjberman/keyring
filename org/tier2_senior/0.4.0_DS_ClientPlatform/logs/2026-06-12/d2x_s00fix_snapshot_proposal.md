# 0.4.0_DS_ClientPlatform — D2X sweep -> S_00 inject fix+deploy -> cot snapshot-first proposal
**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, IMPLEMENT, SCRIBE
**Window:** 2026-06-12 ~19:25Z -> ~20:35Z (since session_1833Z_debtscan_to_d2.md)

## Summary

Three chained workstreams, each reframing the next:

1. **DEBTSCAN D2X composition follow-up (inf/cot/mdpf)** — COO [DRIVE] GO 192948Z. UNKNOWN-VINTAGE
   caveat LIFTED via TOOL-01 `deployed --firm` (inf 61 / cot 47 MATCH; mdpf 15 MATCH + 3 known
   MISSING = TOOL-01-F01). Honesty catch: `io`/`postdeps` were never extended past bd/inf — `io
   --pipeline cot-gold` silently falls back to the bd 29-ID graph (header prints `[bd-gold]`);
   mdpf io = 0/18 analyzed. A naive GAP-grep counts "Unknown script" as clean -> false "all CLEAN".
   Findings D2X-DS-01 (postdeps bd-only, pipeline_cli.py:2321), -02 (io no cot/mdpf graph),
   -03 (cot inject guard fork-shadow), -04 (cot missing AUAGAP guard candidate) + 1 verified-FP
   (inf inject = v1 stub). Precision 3/3 = 1.00, CVO promoted; CVO regraded DS-03 SEV3->SEV2
   (latent S_00 hard-crash). Ledger: `org/modules/graph/debtscan/2026-06-12_D2X_composition_ds_infcotmdpf.md`
   @ 648ff8e83. TOOL-02 (extend io+postdeps) cut to AE 0.6 per my rec.

2. **cot S_00 inject fix (D2X-DS-03+04)** — COO correction ordered "build the missing inject fork";
   Andrew-direct (sovereign) countermanded: cot needs NO scoped-inject functionality (49F-only
   workaround for corrupted txn history). COO [STOP] arrived post-commit pre-deploy; I falsified the
   build-fork premise with file content: `aua_overrides.json` = AUA exclusions (`ghost_accounts`,
   `nna_transaction_exclusions`; consumer `lib/exclusions.py`) NOT inject input; cot has neither
   `_SCOPED_PRICE_OVERRIDES` nor `scoped_price_exceptions.json` -> zero silent-wipe exposure. CVO
   re-verified 3/3 + RETRACTED (b5d89a948); COO unblocked. **Fix @ 319a716cb:** removed inject
   auto-chain from `data/cot/scripts/gold/build_canonical_prices_v2.py` (function, const, --skip-inject,
   subprocess import, docstring) + removed orphan yaml guard + ADDED B_03->C_00 AUAGAP [BLOCKING]
   guard (confirmed real: C_00 reads account_gains, `--chain partial` exists). DELTA=0 (step-6 write
   untouched). S_00 hard-crash mooted before first full COTETL 02:00Z.

3. **cot snapshot-first restructure proposal (Andrew-direct)** — surveyed the 5-table BD pull
   (qt1 holdings 226355 snapshot reconciles 0.1% to certified AUA + catches transferred-in positions
   FIFO misses; qt4 = per-lot cost-basis table; holdings lands since 06-09 only), 43-script gold
   census (only 3 = txn-reconstruct core; Schwab merge legs DEAD — no schwab/ in opal-data-cot).
   Proposal: SNAP_00 daily-state assembler; retire A_03/B_01/S_00 + Schwab legs; txns -> flows-only;
   B_03/C_*/D_* unchanged; 4 phases shadow-validated; 04-22..06-08 backfill = probe-BD-as-of-then-floor.
   `docs/briefs/cot-snapshot-first-restructure-proposal-20260612.md` @ 9e045e02f. **CTO ARCH RULING
   a96b9f098: CONCUR** — 5 SNAP_00 design conditions, shadow gate N=3 explained-not-identical, P2 =
   never-widen drift-acceptance, bd-securities stays shared, A-then-C ratified / B rejected-by-default.
   P0 = FULL write-side hold tonight (clean baseline); ACK'd all conditions.

## Deployment Sequence + Verification (Rule 13, 319a716cb)

```
commit 319a716cb -> origin/CLOUD (carried by COO push; pre-push safe-deploy fired .py upload)
comp-pipescript deployed --firm cot:
  [cot:gold] build_canonical_prices_v2.py  MATCH
  Summary: 47 MATCH, 0 STALE, 0 MISSING_ON_S3, 0 LOCAL_MISSING, 0 TIMEOUT, 0 AWS_UNREACHABLE
gold_pipeline_deps.yaml: S3 copy was STALE (06-09) — .py-only sweep blind to yaml; manual
  `aws s3 cp` + SERVED-object readback verified (do-not-re-add note + AUAGAP guard live).
```
Tooling gap flagged to COO (not a TO): deploy sweep does not cover .yaml config.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| comp-pipescript deployed | `--firm inf` / `--firm cot` / `--firm mdpf` | PASS | TOOL-01 binding works; vintage caveat lifted |
| comp-pipescript io | per-script sweeps, all trees | PARTIAL | inf 46/47 clean; cot/mdpf = silent bd-fallback / Unknown -> D2X-DS-02 |
| comp-pipescript postdeps | no-arg | FAIL (gap) | hardcodes bd yaml -> D2X-DS-01 |
| comp-pipescript deployed | `--firm cot` post-deploy | PASS | 47/47 MATCH verify |
| comp-surface-check | auto in safe-commit x3 | PASS | no critical surface |

What worked: `deployed --firm` per-tree binding; manifest-header inspection as a fallback-detector.
What failed: naive GAP-grep over io output (counts Unknown as clean) — corrected with 3-bucket accounting.
Gap found: io/postdeps bd(+inf)-only (-> TOOL-02, AE 0.6); deploy sweep .py-only (yaml blind).

## Briefs Written (DS)

| Brief | Path | Commit | Status |
|---|---|---|---|
| cot snapshot-first restructure proposal | docs/briefs/cot-snapshot-first-restructure-proposal-20260612.md | 9e045e02f | CTO CONCUR a96b9f098; COO P0-hold; awaiting project registration + TO cut |

## MCP Traffic

~18 messages handled (excl. broker re-surfaces). Significant: COO [DRIVE] GO (D2X) ->
RAVC2/RAVC3 ACCEPTED 1.00 -> COO correction + [STOP-SAFETY] (build-fork) -> my falsification ->
CVO retraction (b5d89a948) -> DEPLOY UNBLOCKED -> deploy RAVC2/RAVC3 ACCEPTED -> proposal routed
COO+CTO -> CTO ARCH RULING a96b9f098 -> my ACK (one from_agent fat-finger, self-corrected 203339Z;
CTO hygiene flag answered).

## Blockers

None. P0 deploy is HELD by design (CTO+COO joint, clean-baseline night), not blocked.

## Current State (zero-context handoff)

- **cot S_00 safe for tonight:** `data/cot/scripts/gold/build_canonical_prices_v2.py` @ 319a716cb
  deployed to `s3://opal-data-cot/code/gold/` (MATCH); no inject dependency remains.
  `gold_pipeline_deps.yaml` deployed (manual cp + readback): AUAGAP guard B_03->C_00 live; orphan
  `B_00.hybrid_price_fill.py` precondition REMAINS (deliberately deferred -> proposal P3).
- **Tonight 02:00Z:** first full COTETL 5/5 (post 9abd0181b qt3/qt4 template fix) = clean baseline;
  ZERO restructure changes riding; `templates/holdings.json` +2-line delta left UNCOMMITTED on purpose.
- **DEBTSCAN:** D2-DS-01, D2X-DS-01..04 all CLOSED or routed (TOOL-02 @ AE 0.6). Ledgers in
  `org/modules/graph/debtscan/`.
- **Proposal pair of record:** brief 9e045e02f + CTO ruling a96b9f098 (no re-authored PRD; brief is
  PRD-grade per CTO). **Project REGISTERED: ADVI_COTSNP** (`org/projects/ADVI_COTSNP.json`, COO
  203458Z); P0-P3 TO decomposition = COO next cycle.

## Next Steps

1. Tomorrow AM: qt3/qt4 landing artifact review (5/5 COTETL validation) — observe-only.
2. Then: cot_silver_merge TABLE_CONFIG extension deploy (P0); holdings.json parity-diff vs live S3
   + commit.
3. SNAP_00 P1 build on [2.0.0_SA_COO] ADVI_COTSNP TO cut, under CTO's 5 design conditions + N=3
   shadow gate (CVO verification queue at P1).
4. [0.6.0_AE_PartnerETL] owns TOOL-02 (io/postdeps all-trees extension).
5. Pending queue: NFRA_COT_RULE15 future-import backfill TO (awaiting COO drive).
