# PRE-FIRE ACCEPTANCE BASELINE -- 2026-07-29T13:51:02Z (2.0.0_SA_COO)

**archetype:** VALIDATE

Captured BEFORE the 15:00Z chain so tonight's acceptance is a COMPARISON against a
measured baseline, not a judgment against recollection. Persisted here because a
scratchpad dies with the session -- and this fabric lost an open ledger today to a
session that stopped rather than ended.

## Acceptance sheet (DS~A's pre-commitment -- CITED, not transcribed)

Source of truth: `org/mcp/inbox/2.0.0_SA_COO/read/20260729T131628Z_0.4.0_DS_ClientPlatform_A_ANSWERS_Q5-Q7__your_131331Z___measured_t.md`

Read the figures FROM THAT FILE. They are reproduced here for convenience and are
NON-AUTHORITATIVE: custody @07-24 463,015,162.92 (must equal the pair to the cent);
custody frontier @07-27 466,552,705.91; non_model @07-24 337,882,950.89 CONDITIONAL on
the slice's model_aua @07-24 equalling the pair's model_aum 125,132,212.03.
DS~A's falsifier, unchanged: custody still blank after 16:15Z = stage-6d failure.

> The `/handoff` block that carried this state into the session rendered the non_model
> figure as `337,882,95,212.03` -- two numbers fused. Recovered from the originating
> message. Load-bearing numbers travel by citation, never by transcription.

## Cottonwood served artifact -- the object the acceptance turns on

`s3://opal-data-portal-v2/platinum/mdpf/cottonwood/aggregate-aua-timeseries.json`
ETag `0ec286f214c0ea6e3f1ac04a0a496d83` / 37,518 B / LastModified 2026-07-29T00:35:22Z
Downloaded and md5-verified against the ETag before reading (not a listing read).

DENOMINATOR N=450, as_of 2024-11-01..2026-07-27, backfill_method=null
PREDICATE: array element is not None

| field | coverage | detail |
|---|---|---|
| `model_aua` | 2/450 | both 124,376,009.73 @07-21, @07-22 |
| `non_model_aua` | 0/450 | ALL NULL |
| `partner_custody_total` | 0/450 | ALL NULL |
| `account_count_total` | absent | not a key on this object |

MIS-AIM CORRECTED IN-SESSION: first measured `json/mdpf/cottonwood/...` (447 dates,
custody 56/447) -- the LEGACY plane, superseded by the flip. Real numbers, wrong object.
Enumerate what a number is OF before explaining why it differs.

## Trigger plane (grounded 14:02Z, direct describe-rule)

| clock | rule | trigger |
|---|---|---|
| 15:00Z chain | `mdpf-daily-refresh-trigger` | **NO ScheduleExpression** -- S3 ObjectCreated on opal-data-inf/gold/meta/pipeline-complete.json |
| 15:45Z accrual | `etfs-canon-fanin-daily` | `cron(45 15 * * ? *)` ENABLED |
| 16:15Z publisher | `opal-assets-mdpf-portal-publisher-daily` | `cron(15 16 * * ? *)` ENABLED |
| 17:15Z emitter | `opal-assets-daily-emitter-daily` | `cron(15 17 * * ? *)` ENABLED |

The 15:00Z leg certifies at most UNATTENDED-EVENT-PATH-EXERCISED. The pass and the
defect produce the same observation; the only discriminator is reading the trigger.
CVO PIN-4(i) -> automatic D2-as-scheduled FAIL for that leg (ruled before evidence).
Remedy = additive cron floor on the same Lambda, CTO-approved in principle, post-freeze.

## Retired-key state (AE~A's 15:15Z step-4 target)

`json/portfolios/non_model_assets.json` + `_preview` -- ABSENT (grep rc=1), positive
control run separately: same prefix lists 11 objects. Bucket-wide sweep for `non.model`
returns exactly ONE object, `platinum/mdpf/global/non-model-assets.json` -- a DIFFERENT
key on a different plane, legitimately present. A name-shaped check reads dirty on a
healthy estate; step 4 is key-exact by agreement.

## Pre-fire ETag snapshot -- all served MDPF objects

DENOMINATOR: 33 objects (platinum firm-level + legacy json plane). Per-date
`platinum/mdpf/aggregate_aua/` tree (434 objects) excluded -- census-excluded vintage tree.
Timestamps are true UTC from `list-objects-v2` (NOT `s3 ls`, which renders host-local).

```
json/mdpf/49financial/account-distribution.json	"d40065bed08a4c2a924b709767e0fb5f"	5396	2026-07-29T11:30:39.000Z
json/mdpf/49financial/aggregate-aua-timeseries.json	"501407448f554a77a7ff7e2a5dceb954"	183004	2026-07-28T13:41:07.000Z
json/mdpf/aggregate-aua-timeseries.json	"a8614a2622744685c34967239a5b57ba"	447154	2026-07-27T15:10:34.000Z
json/mdpf/cottonwood/account-distribution.json	"1b283841dd19d255fff22fb19e29775c"	6375	2026-07-23T04:04:42.000Z
json/mdpf/cottonwood/aggregate-aua-timeseries.json	"194e5bb05c4523abb2cc05988f53005f"	87262	2026-07-23T21:47:07.000Z
json/mdpf/cottonwood/aum-metrics.json	"55b1f1a48e0089ec081798683ecca110"	2862	2026-07-23T04:04:42.000Z
json/mdpf/global/account-distribution.json	"14d668ef3b0c048170f59fd5a1516f13"	7656	2026-07-23T20:57:18.000Z
json/mdpf/global/aggregate-aua-timeseries.json	"5f758b470372da18ad04e5248037cdd0"	254419	2026-07-28T13:41:05.000Z
json/mdpf/inflection/account-distribution.json	"40611352aaa12b638db3b580f0609b6b"	6889	2026-07-29T11:30:39.000Z
json/mdpf/inflection/aggregate-aua-timeseries.json	"e3c8db35d7bfedb15d0876eed6ffdbb4"	146290	2026-07-28T13:41:10.000Z
platinum/mdpf/49financial/account-distribution.json	"8b50e7381568558aa2a534dcafa56636"	5744	2026-07-29T00:35:21.000Z
platinum/mdpf/49financial/aggregate-aua-timeseries.json	"15cfa184018de68c036163986836ebdb"	105004	2026-07-29T00:35:22.000Z
platinum/mdpf/49financial/aggregate_aua_timeseries.json	"b55c6926262652d5afc6bcdda336604a"	158043	2026-07-29T00:32:32.000Z
platinum/mdpf/_g6_fixture/fresh-all.json	"3d5e1e010c73e0ca3c40c4b17d29cea4"	509	2026-07-13T00:33:53.000Z
platinum/mdpf/_g6_fixture/mixed.json	"37a4dfd5364d177f1dbbb0ead57e6146"	546	2026-07-13T00:33:57.000Z
platinum/mdpf/_g6_fixture/one-missing.json	"9d761448bdcf0053fdad511c43ebe604"	459	2026-07-13T00:33:59.000Z
platinum/mdpf/_g6_fixture/one-stale.json	"5754a985d27517b7e523dd1ff4e394b7"	509	2026-07-13T00:33:55.000Z
platinum/mdpf/aggregate_aua_timeseries.json	"6d77967a2cbc76fac0511c85ac190d99"	448241	2026-07-29T00:32:32.000Z
platinum/mdpf/cottonwood/account-distribution.json	"039100946682a5050352e5a468dd13b7"	6652	2026-07-29T00:35:22.000Z
platinum/mdpf/cottonwood/account-units.json	"3a1e520ca5e1d52b4707420610758955"	7614	2026-07-29T00:35:22.000Z
platinum/mdpf/cottonwood/aggregate-aua-timeseries.json	"0ec286f214c0ea6e3f1ac04a0a496d83"	37518	2026-07-29T00:35:22.000Z
platinum/mdpf/cottonwood/aum-metrics.json	"76c01a646e5e7fe4a13338d9cf168ee6"	3117	2026-07-29T00:35:22.000Z
platinum/mdpf/etf_ownership_timeseries/DIVZ.json	"955b5e49d9f644bfe81c16619fd05e8a"	49441	2026-07-29T00:32:44.000Z
platinum/mdpf/etf_ownership_timeseries/IDVZ.json	"89e4a9c1af4abe602b7464b828f8fc63"	49421	2026-07-29T00:32:44.000Z
platinum/mdpf/etf_ownership_timeseries/PFDE.json	"9f8937fae3f50ecd43e10ac40c0099bb"	36677	2026-07-29T00:32:44.000Z
platinum/mdpf/etf_ownership_timeseries/PFOE.json	"ede5a36bab2a1d00ce576eb03d7e55c5"	36591	2026-07-29T00:32:44.000Z
platinum/mdpf/global/account-distribution.json	"7add19557155c6af11f18f08f2090ae8"	7233	2026-07-29T00:35:22.000Z
platinum/mdpf/global/aggregate-aua-timeseries.json	"31e64570d3090eff4df3baab91d2a1dd"	200059	2026-07-29T00:35:22.000Z
platinum/mdpf/global/aggregate_aua_timeseries.json	"06128c54fb77e44ed1503a37229d154b"	163342	2026-07-29T00:32:32.000Z
platinum/mdpf/global/non-model-assets.json	"38fbf53ef5ac76a8ba6d5a3882b7dafd"	81931	2026-07-29T00:35:22.000Z
platinum/mdpf/inflection/account-distribution.json	"d2f121b5202c81a8f6db9c0db060c7aa"	7189	2026-07-29T00:35:23.000Z
platinum/mdpf/inflection/aggregate-aua-timeseries.json	"7cda0b01b1f2c0eca6992a69c0a7b776"	68026	2026-07-29T00:35:23.000Z
platinum/mdpf/inflection/aggregate_aua_timeseries.json	"15cca7eebfd692f7fe50564463434128"	124033	2026-07-29T00:32:32.000Z
```
