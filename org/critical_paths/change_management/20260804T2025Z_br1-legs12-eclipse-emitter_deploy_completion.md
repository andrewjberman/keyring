# Deploy-completion ledger: BR1 legs 1+2 -- inf-api-eclipse + inf-bronze-complete-emitter

**Opened:** 2026-08-04T20:25Z by 0.7.0_AE_CloudOps
**Status:** CLOSED 2026-08-04T20:33Z -- all legs proven, nothing stranded
**Authority:** TO OPAL_VENDORPROVENANCE.BR1-AE (P1); plan @7538cbc5f + Amendment 1 @bdd86c32b;
CTO TF-hold release 200757Z ("author against the amended plan... Full deploy law as always").

## Payload

Pure-add (16 resources, 0 change, 0 destroy): two Lambdas + roles/policies/schedules.
- Leg 1 inf-api-eclipse (DS script @6b43144022): staging prefix bronze/eclipse_qa, 13:33Z daily,
  consume-only JWT grants (GetSecretValue x2, no writes), overlap day-1 = first scheduled fire.
- Leg 2 inf-bronze-complete-emitter (DS script @ae78256663): staging-suffixed sentinel
  _BRONZE_COMPLETE_qa.json, 14:43Z daily, List+Put only.
- NOT here: row-2 silver floor + GF-1 (same wave, after their targets' contract reads).

## Legs

| # | leg | evidence | status |
|---|---|---|---|
| L1 | artifacts built+uploaded | both zips verified (write VERIFIED, sha256 metadata match) | DONE |
| L2 | targeted plan (14 targets) | 16/0/0, all creates, zero existing-resource touches | DONE |
| L3 | safe-apply targeted | "16 added, 0 changed, 0 destroyed" | DONE |
| L4 | 0-diff replan | "No changes. Your infrastructure matches the configuration." | DONE |
| L5 | live verify | inf-api-eclipse CodeSha256 wTv20qjB... 512MB/300s/py3.11; emitter n+Vrhm1m... 256MB/py3.12; rules cron(33 13) + cron(43 14) both ENABLED | DONE |
| L6 | 22a battery 8/8 | GetSecretValue x2 allowed (exact secret ARNs); staging PutObject allowed; ListBucket-with-context x2 allowed; sentinel PutObject allowed; NEGATIVES x2 implicitDeny (puller->production prefix, emitter->foreign prefix) -- one resource per call, controls isolated | DONE |
| L7 | tag inf-pipeline-v1.7.98 + MSTR push queue | annotated tag on the ledger commit | DONE |

**Day-1 clock:** first scheduled overlap fire = 2026-08-05 13:33Z (puller, staging), sentinel
first emit 14:43Z. Gate-1 acceptance = >=5 TD field-exact (DS harness). Floors (row-2 + GF-1)
= next wave in this lane, before Gate-2 reads "live + exercised."
