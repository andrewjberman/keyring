# MDPF all-firms serve -- deploy completion ledger
**Status:** CLOSED -- publish complete, 6/6 served keys byte-identical with size+ETag cited -- closed 20260723T1852Z

<!-- LEGIBILITY STAMP ONLY, NOT A STATE CHANGE (0.7.0_AE_CloudOps, 2026-07-24T~1400Z).
     This ledger has read CLOSED since 20260723T1852Z on the `CLOSED:` line at :18 below. The stamp above
     restates that, verbatim in the canonical spelling, because `deploy_ledger.py`'s reader could not parse
     the existing marker and flagged this entry `BYPASS: UNINDEXED OPEN LEDGER` -- a false RED on a deploy
     that was fully closed and fully evidenced.
     WHY IT WAS UNREADABLE: both reader limbs are line-anchored. `_md_status()` needs `**Status:**` /
     `**Status: X**` / `## Status:` (no `Status` keyword existed here at all); `_has_close_marker()` needs a
     BOLDED `**Closed:**` span (`:18` is a bare unbolded `CLOSED:`). Exercised, not inferred -- both
     functions were imported from the live module and run against this file, returning None/False, with two
     known-readable ledgers as positive controls returning parsed terminal statuses.
     AUTHORIZED: CTO ruling 214257Z, which assigned this entry's disposition to 0.7.0_AE_CloudOps and
     permits evidence-cited stamps ONLY where closure is unambiguous. It is: `CLOSED:` at :18, plus 6/6
     byte-identical served keys each carrying size + ETag, plus the authority chain at :3-4 (CTO serve-fire
     184804Z on COO counter-sign 184724Z + DE render @5ae6762da).
     SAFE BECAUSE THIS ENTRY IS UNINDEXED -- it has NO sentinel and was hand-authored, never produced by
     `deploy_ledger.py`. The `.md`-is-a-RENDERING contract binds writer-managed entries reconstructed from a
     sentinel; adding a status line here neither races the writer nor trips Layer-3 drift. This stamp would
     NOT be safe on a sentinel-backed entry.
     NOT DONE HERE: no mechanical/mass pass. The two other flagged ledgers (cot-advi-fix-silver-coerce,
     cottonwood-mdpf-served-publish -- both DS-authored, both closed in fact via a MID-LINE `**Closed:**`
     the line-anchored reader cannot see) are deliberately LEFT UNTOUCHED. They are the standing instances
     for the reader-loosening decision at CTO's gate. Full analysis:
     org/tier2_senior/0.7.0_AE_CloudOps/deliverables/DEPLOY_LEDGER_RECONCILIATION_20260724.md -->

OPENED: 2026-07-23T18:49Z by 0.4.0_DS_ClientPlatform
AUTHORITY: CTO serve-fire 184804Z on COO clean counter-sign 184724Z + DE render evidence @5ae6762da
(never-widen co-sign satisfied: CTO+COO). Andrew tonight-completion order standing.
PATTERN: per key, staged-md5 assert (gate-cited prefixes matched) -> put -> fresh-GET
byte-compare -> ListObjectsV2 key+size -> served ETag cited.

SERVED (opal-data-portal-v2), all 6/6 byte-identical:
1. json/mdpf/49financial/aggregate-aua-timeseries.json  171,643B ETag d68f2f4bb3337738817c55a5a9ad8fed
2. json/mdpf/inflection/aggregate-aua-timeseries.json   136,236B ETag 904df9f29cd469725ed593e00704aaf9
3. json/mdpf/aggregate-aua-timeseries.json              242,414B ETag 8b6de1d5b506f6504426078c30e53edc
   (GLOBAL: measured frontier 2026-07-22 = $1,951,676,164.42, cottonwood=measured)
4. json/portfolios/aum-metrics.json                       7,234B ETag 4580938e4aab3e978807eeb8d487dc94
5. json/mdpf/global/account-distribution.json             7,220B ETag 0a2978d46352932d3f53c52161cedfb4
6. json/mdpf/cottonwood/aggregate-aua-timeseries.json    66,999B ETag 55f3c6fed26852de218748263a671a28
   (band w/ measured 07-21/22 tail; supersedes the 1203Z serve per V6 measured-beats-interpolated)

CLOSED: 2026-07-23T18:52Z -- publish complete, report to CTO+COO+DE+DT sent same turn.
Downstream: DE live-render check -> DT DEV cfb0afb7 -> PROD promote -> COO confirms live to Andrew.

## AMENDMENT (0.7.0_AE_CloudOps, 2026-07-23T19:36Z) -- publisher cutover leg (CTO order 190518Z)
Pre-invoke grounding per the order: (a) read-surface -- ModelPortfolios.tsx:497 ->
/api/general/mdpf/global/aggregate-aua-timeseries.json -> CF public-data-router /json/* rewrite;
the aum.ts:444 "platinum" cite is a STALE 2026-05-18 comment; the DEPLOYED opal-portal-data-proxy
(sha LpodJICu..., unmodified since 2026-06-10) contains ZERO 'platinum' references and NO
/aum/aggregate-mdpf route (positive control: 20 PORTAL_DATA_BUCKET hits) -- the HANDOFF_AE route
diff was never applied. (b) STAGING_ROOT == gold/mdpf_revamp confirmed at source. (c) census
11/11 staged. .tools/mdpf-preflip-check: PASS, flip-set == PUBLISH_MAP both directions (11).
FINDING AT INVOKE: the DEPLOYED publisher ran the pre-3F-F1 9-KEY map -- 9/9 all_present=True
with COTTONWOOD ABSENT (the exact RF-1 false-green its own source comment warns of; deployed
artifact @2026-07-20 predated 8ec253b34). Redeployed from committed source (zip b64sha
ZEqfKEq01ryL1168FB9cbI2J0/U92yVfx9c7yznGzkA=, applied via safe-apply -target=module.mdpf_publisher,
live CodeSha256 ties). Re-invoke: 11/11 all_present TRUE incl both cottonwood keys.
Byte-verify: 11/11 dst ETag == src ETag on opal-data-assets json/* (same-bucket copy, ETag=MD5).
CONSUMED-KEY VERIFY (portal-v2): json/mdpf/global/aggregate-aua-timeseries.json AND the root key
byte-tie gold ETag 8b6de1d5b506f6504426078c30e53edc; opal_aggregate_aua last == $1,951,676,164.42
@ 2026-07-22. The Andrew platinum-overwrite architecture (gold append + portal platinum overwrite)
is a follow-on build: grounded, NO live reader consumes platinum/mdpf today (proxy zero-refs;
FE reads json tier; mdpf-freshness-checker reads platinum as an instrument) -- routed to COO/CTO
with DE's key map as the denominator before any platinum write claims the unblock.
