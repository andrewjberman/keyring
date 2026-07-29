# MDPF D3 · PIN-1 DIFF — written `platinum/mdpf/**` vs pinned design set @d6c9562318

**Author:** 3.0.0_SA_CVO · 2026-07-29 ~12:45Z · **archetype:** VALIDATE
**Standing:** PRE-FIRE CHECK, not the D3 certification. D3 certifies on the ~16:15Z UNATTENDED
publish (PIN-4/PIN-5); this record pins the hand-run-publish state so the post-fire diff has a
baseline. All timestamps below UTC (listing rendered local UTC-4 and converted — law #11).

**Method:** full recursive `s3 ls` of `s3://opal-data-portal-v2/platinum/mdpf/` — **457 keys total**
(saved listing: session tool-results bbcv2cg4y). Written set = keys of shape
`platinum/mdpf/{scope}/{type}.json`. Pinned set = the 11-pair enumeration at commit d6c9562318
(authored by AE post-WO-1, pre-WO-2, per PIN-1).

## Direction A — pinned → written: 11/11 PRESENT ✓

All 11 pairs exist, written 2026-07-29T00:35:21–23Z (the WO-2 publisher's first invoke):
49financial/{aggregate-aua-timeseries, account-distribution} · inflection/{same 2} ·
cottonwood/{aggregate-aua-timeseries, account-distribution, aum-metrics, account-units} ·
global/{aggregate-aua-timeseries, account-distribution, non-model-assets}.

## Ruled-DRIFT pairs — ABSENT ✓ (both required checks pass)

`49financial/aum-metrics.json` · `inflection/aum-metrics.json` · `global/aum-metrics.json` — none
exist. The publisher did not invent them (enumeration's "must NOT invent" clause honoured).

## Direction B — written → pinned: 4 excess member groups, ALL ATTRIBUTED

| excess members | written | attribution | disposition |
|---|---|---|---|
| `{49financial,global,inflection}/aggregate_aua_timeseries.json` (underscored) + top-level `aggregate_aua_timeseries.json` | 00:32:32Z | **dispatch Stage-4 rollup twin** — grounded @cc35d80925 (deployed dispatch `:375`), independently found by my diff and by AE~A's twin hunt | KILLED repo-side; S3 deploy of the kill HELD post-17:15Z (D2 freeze). Post-fire diff must show these keys STOP advancing |
| `etf_ownership_timeseries/{DIVZ,IDVZ,PFDE,PFOE}.json` | 00:32:44Z | same legacy dispatch run (ETF product co-tenant) | ETF pivot queue (E-items); BELOW MDPF per Amendment 4 |
| `aggregate_aua/` date-keyed accrual, **434 objects**, newest `2026-07-28.json` @00:31:51Z — LIVE DAILY | daily ~10:59Z + chain runs | Stage-3/WS-A accrual feed (known; feeds DDB until 4c) | retires at 4c post-fires; teardown wave = COO's |
| `_g6_fixture/` 4 objects | 07-12 | G6 test fixtures | inert; teardown wave hygiene |

**Content discrimination (not just names):** downloaded both `global/` variants. Canonical
(hyphenated) carries `meta.generated_at 2026-07-29T00:33:43Z`, `cohort_provenance`, `point_class`,
`count_basis` — the TO-1 D1=SERVE-REAL product. Twin (underscored) carries the old
`backfill_methods` meta lineage. **Different products, not a rename** — sizes differ (163,342 vs
200,059 B for global). The twin kill is retiring a genuinely divergent writer, which is exactly why
D3 needs both directions.

## Verdict

**PRE-FIRE D3 DIFF: CLEAN.** Written ≡ pinned in both directions once the four excess groups are
named — and every excess group has an owner and a scheduled retirement. NOTHING UNEXPLAINED remains
in the namespace.

**What still gates D3 certification (post-fires):** (1) the ~16:15Z publish must be UNATTENDED
(PIN-4 trigger identity from the run's own log — `source: aws.events` + rule ARN); (2) re-diff:
the 11 canonical keys advance, the 4 twin keys do NOT advance (post-twin-kill deploy), or if the
kill deploy hasn't landed, twin advancement is EXPECTED and noted, not a fail; (3) vintage/ETag per
object vs the gold tree. This record is the baseline for that diff.

— 3.0.0_SA_CVO
