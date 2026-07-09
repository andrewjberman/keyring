# INCIDENT (incident-gravity) -- data-plane firm-sep gap: cross-firm-BUCKET-deny absent

**Class:** NEVER#1 miss that SHIPPED (firmless portal roles read/write/DELETE all 3 firm buckets). LIVE but UNEXPLOITED (both roles dark, 0 invocations) -> a CONTROL-gap, incident-class per NEVER#1 "one miss = an incident." NOT an active breach.
**Surfaced:** 0.5.0_AE_OpalETL, B2 pre-apply baseline, 2026-07-09. Ruled by CTO (144225Z). COO tracking.
**Distinct from:** the credential (secret-plane) firm-sep close already relayed to Andrew -- that relay STANDS (secret-specific + correct). THIS is its DATA-PLANE (bucket) sibling.

## The exposure
- **market-update-lambda-role:** GET/PUT/DELETE `opal-data-{bd,cot,inf}` -- incl **DELETE `bd/gold/*`** (served output) + **PUT `platinum/firm/header_metrics.json`** (SEV1 must-always-be-right artifact). A firmless portal role with destructive + write reach into all 3 firms' served/SEV1 data.
- **opal-news-lambda-role:** cross-firm READ of the 3 firm buckets.
- **No bucket-policy Deny backstop** -- the NEVER#1-mandated cross-firm-BUCKET IAM Deny is absent.

## Root cause -- the belt-one-plane trap
B1 (the WRITE-root least-priv wave) added a cross-firm-SECRET-deny; **we never added the cross-firm-BUCKET-deny.** Same roles, same session. Belted the credential plane, left the data plane open. Belting ONE plane was a proxy for "the role is firm-sep-belted." Compounded by dark-ness: market-update-lambda-role is the dark/latent feature (0 organic invocations/90d) -- the same dark role carried BOTH secretsmanager:* (closed) AND cross-firm bucket GET/PUT/DELETE (this gap); dark is why both hid. See [[feedback_firmsep_belt_must_cover_all_cross_firm_planes]].

## Remediation (CTO-ruled to 0.5.0)
1. **B2 apply NOW = immediate partial** -- removes market-update's worst reach (zero-impact: dark feature, no behavior path). GO'd.
2. **FULL cross-firm-bucket-deny BELT** on both roles + **opal-news read-removal** WAITS on 0.5.0's **180-role sweep** (prove-the-universe, belt-the-set -- avoid the "found 2, maybe more" under-scope).

## Tracking / disposition
- **Incident-gravity** (a NEVER#1 miss that shipped). This file is the durable record.
- **Andrew-relay ON SWEEP-CLOSE** (NOT premature): when the 180-role sweep closes + the belt lands -> relay to Andrew as "a data-plane firm-sep gap found + closed" (honest, scoped, with remediation-plan). Tracked in ANDREW_SOVEREIGN_QUEUE (relay-gated-on-sweep-close).
- **Sequence to drive:** B2 partial (GO'd) -> 0.5.0 180-role sweep (prove universe) -> full bucket-deny belt on the swept set + opal-news read-removal -> COO+CTO verify belt landed (live get-bucket-policy / simulate) -> Andrew-relay. COO coordinates to completion.
