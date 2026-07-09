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

## UPDATE 2026-07-09T15:10Z (CTO) -- B2 partial LANDED; incident GREW (2nd principal + possible detection-gap)
- **B2 APPLIED + ledger CLOSED 4/4 in-session.** market-update's worst capability (DELETE bd/gold/* + OVERWRITE the SEV1 platinum artifact) is GONE, verified 3/3 implicitDeny vs allowed-baseline. Immediate partial-remediation landed.
- **2nd FOREIGN PRINCIPAL found: `lambda-execution-role`** -- a SHARED role behind 13 LIVE Lambdas (NOT dark), cross-firm PutObject to opal-data-bd/* incl bd/platinum (the SEV1 artifact -- can OVERWRITE from a live role; cannot delete). Legacy remnant (bd Lambdas migrated to dedicated roles; none of the 13 reference the firm buckets). **Highest-priority belt row** (live, not dark).
- **POSSIBLY UNMANAGED grant (detection-gap):** the S3Access policy is not in the 5 TF states checked (exhaustive walk TIMED OUT -> "not-found," NOT "proven-unmanaged"). If unmanaged, it is the data-plane analogue of the SecretsManagerReadWrite lesson: INVISIBLE to a grant-shape lint over authored TF -> **firm-sep DETECT must include a LIVE-vs-TF reconcile, not just a TF-lint.** (Why DETECT-on-live matters -- an unmanaged grant is exactly the partial-signal a TF-lint proxy misses.)
- **SWEEP 3/6, STRADDLED the apply** (not one clean snapshot); owner-census too-narrow (false-FOREIGN, verdict unaffected) -> 0.5.0 re-runs CLEAN post-B2 before certifying scope. **Not "just these" yet** -- the universe is not yet proven.
- **Scope GREW, shape UNCHANGED:** full belt-on-clean-swept-universe; Andrew-relay-on-sweep-close now covers 2 principals + a possible detection-gap. Timing-gate (sweep-close) HOLDS. CTO gates the belt-apply when the clean sweep + managed/unmanaged resolve.

## Tracking / disposition
- **Incident-gravity** (a NEVER#1 miss that shipped). This file is the durable record.
- **Andrew-relay ON SWEEP-CLOSE** (NOT premature): when the 180-role sweep closes + the belt lands -> relay to Andrew as "a data-plane firm-sep gap found + closed" (honest, scoped, with remediation-plan). Tracked in ANDREW_SOVEREIGN_QUEUE (relay-gated-on-sweep-close).
- **Sequence to drive:** B2 partial (GO'd) -> 0.5.0 180-role sweep (prove universe) -> full bucket-deny belt on the swept set + opal-news read-removal -> COO+CTO verify belt landed (live get-bucket-policy / simulate) -> Andrew-relay. COO coordinates to completion.
