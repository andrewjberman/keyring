# Deploy-completion ledger -- OPAL_MDPFCLEANUP.TO-4: S3 unused-artifact deletes (Andrew ~1500Z word, as scoped)
**Opened:** 20260819T0057Z by 0.7.0_AE_CloudOps, BEFORE the first delete (NEVER#8).
**Release:** COO fixture verdict 005714Z (chain PASS; TO-4 + mint released this window).
**Authorization chain:** Andrew-direct ~1500Z ("any unused mdpf artifacts should be deleted especially if no active producer", record ANDREW_DIRECT_20260818_ALL_RECS_APPROVED...) -> COO NEVER#3 half 163649Z vs manifest.tsv -> CTO NEVER#3 half 170518Z (G-B) vs the same manifest.
**Copy-manifest:** .scratch-ae/to4_manifest/manifest.tsv -- 10 rows, sha256 + bytes per object, local rollback copies sha-verified. ROLLBACK = same-window aws s3 cp from the local copies.
**HELD (not in scope tonight):** json/mdpf/49financial/aggregate-aua-timeseries.json (mdpf-gold-lambda FLAG-2 daily reader; deletes only after MDPF_PROVENANCE T-B proves on a scheduled 13:30Z run, >=08-20).
**EXCLUDED (grounds in exec plan):** mdpf/feeds/ + telemetry/ (LIVE today); bmkaud-evidence/ (PERMANENT declared evidence-class exception, COO 163649Z).

## Structural oracle (PASS_WITH_DISCLOSURE basis -- no access-log instrument exists; Andrew's word made the CF-logging question MOOT)
1. ROUTE NEGATIVE (applied): no CF path resolves json/mdpf/* (default behavior -> S3-opalinvest-portal; /json-tiered/* only /json* behavior; /api/general/mdpf/* -> /platinum/mdpf/* in deployed public-data-router :6 sha==HEAD-built-07-29). Read 160xZ 08-18.
2. DEPLOYED-CODE READERS: mdpf-gold-lambda -> HELD key only; opal-smartx-ingestion-pipeline generate_smartx_timeseries_and_metrics.py:482 (global key) INERT -- zero invocations since the 08-14 TO-3 trigger kill, no lambda resource policy (GetPolicy ResourceNotFound), try/except fail-soft. RE-CONFIRMED AT EXEC below.
3. LIVE-POLICY PRINCIPAL CENSUS: at-exec, below.
4. GUARDED-SET SPELLING: account_units/account-units in delete scope = 0/0 both spellings.

## Rows (filled at execution)
| # | key | pre-delete head (mtime/bytes vs manifest) | delete | absence + positive control | DELTA |
|---|---|---|---|---|---|
| 1 | s3://opal-data-portal-v2/json/mdpf/cottonwood/aum-metrics.json | pre=[Thu, 23 Jul 2026 04:04:42 GMT	2862]==manifest 2862B | delete-object OK | post=404-ABSENT | bytes per manifest |
| 2 | s3://opal-data-portal-v2/json/mdpf/cottonwood/account-distribution.json | pre=[Thu, 23 Jul 2026 04:04:42 GMT	6375]==manifest 6375B | delete-object OK | post=404-ABSENT | bytes per manifest |
| 3 | s3://opal-data-portal-v2/json/mdpf/global/account-distribution.json | pre=[Thu, 23 Jul 2026 20:57:18 GMT	7656]==manifest 7656B | delete-object OK | post=404-ABSENT | bytes per manifest |
| 4 | s3://opal-data-portal-v2/json/mdpf/cottonwood/aggregate-aua-timeseries.json | pre=[Thu, 23 Jul 2026 21:47:07 GMT	87262]==manifest 87262B | delete-object OK | post=404-ABSENT | bytes per manifest |
| 5 | s3://opal-data-portal-v2/json/mdpf/aggregate-aua-timeseries.json | pre=[Mon, 27 Jul 2026 15:10:34 GMT	447154]==manifest 447154B | delete-object OK | post=404-ABSENT | bytes per manifest |
| 6 | s3://opal-data-portal-v2/json/mdpf/global/aggregate-aua-timeseries.json | pre=[Tue, 28 Jul 2026 13:41:05 GMT	254419]==manifest 254419B | delete-object OK | post=404-ABSENT | bytes per manifest |
| 7 | s3://opal-data-portal-v2/json/mdpf/inflection/aggregate-aua-timeseries.json | pre=[Tue, 28 Jul 2026 13:41:10 GMT	146290]==manifest 146290B | delete-object OK | post=404-ABSENT | bytes per manifest |
| 8 | s3://opal-data-portal-v2/json/mdpf/49financial/account-distribution.json | pre=[Fri, 14 Aug 2026 11:30:39 GMT	5397]==manifest 5397B | delete-object OK | post=404-ABSENT | bytes per manifest |
| 9 | s3://opal-data-portal-v2/json/mdpf/inflection/account-distribution.json | pre=[Fri, 14 Aug 2026 11:30:39 GMT	6865]==manifest 6865B | delete-object OK | post=404-ABSENT | bytes per manifest |
| 10 | s3://opal-data-mdpf/cache/custody_crosswalk.json | pre=[Tue, 19 May 2026 15:54:14 GMT	317362]==manifest 317362B | delete-object OK | post=404-ABSENT | bytes per manifest |

## Execution record (00:57-01:0xZ 08-19)
- FIRST ATTEMPT: 0 of 10 -- my head-object parser read awk $2 of an HTTP-date line (= day-of-month) as ContentLength; the size guard STOPPED every row (fail-closed on the author's own bug, zero mutations). Re-run with $NF: 10/10.
- 10 of 10 DELETED-AND-ABSENT (per-row pre-head==manifest, post-head 404). DELTA: 10 objects / 1,281,642 B, fully manifest-accounted; local sha256 copies retained (.scratch-ae/to4_manifest/objects/) = rollback instrument (same-window aws s3 cp).
- POST-DELETE LISTINGS: json/mdpf/ recursive count = 1 = EXACTLY the HELD key (49financial/aggregate-aua-timeseries.json, positive control head 183,004 B == its manifest-era bytes, SURVIVES); opal-data-mdpf cache/ = 0; positive control telemetry/ survives (status.json 08-18).
- AT-EXEC RE-CONFIRMS: smartx-ingestion Invocations 08-14T15Z..08-19T00:55Z = ZERO datapoints (metric window re-pulled at exec); live principal census (denominator: 4 roles read) -- mdpf-daily-runner-ec2-role: JsonMdpfServingRW Allow Get/Put json/mdpf/* AND P0DenyJsonMdpfClobber20260728 Deny PutObject json/mdpf/* APPLIED (writer barred since 07-28); mdpf-gold-lambda-role: GoldServedPreserveRead GetObject json/mdpf/* (the FLAG-2 reader -- HELD key only at deployed bytes); smartx-ingestion-lambda-role: ZERO json/mdpf references inline, only AWSLambdaBasicExecutionRole attached; opal-assets publisher json/mdpf prefixes are on opal-data-ASSETS (different tree, not a portal-v2 principal).
- NEVER#3: COO half 163649Z + CTO half 170518Z, both vs manifest.tsv sha-set, no rows added since.
**CLOSED 2026-08-19T01:0xZ by 0.7.0_AE_CloudOps. PASS_WITH_DISCLOSURE (structural oracle in lieu of the nonexistent access log) -> PASS. CTO validation requested same-window.**
