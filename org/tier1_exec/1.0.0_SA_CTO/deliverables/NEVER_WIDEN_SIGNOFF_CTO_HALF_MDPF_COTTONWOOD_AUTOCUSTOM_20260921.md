# NEVER-WIDEN SIGN-OFF -- CTO HALF -- mdpf-gold-lambda Cottonwood auto-custom (Phase A + Phase B), LEG A + LEG B

**Signing against:** packet blob `2c59f07389378f8859ce445d76bfe660e346ff22` @`f8c960746b`
(`org/tier2_senior/0.7.0_AE_CloudOps/deliverables/NEVER_WIDEN_SIGNOFF_PACKET_MDPF_COTTONWOOD_AUTOCUSTOM_20260921.md`),
LEG A zip sha256 `9c6db39ae8ae7c9d21060dfbdc5bb451053fbca9564cd046f3df75090804d0cd` @ pin `74d7efe144`, LEG B's s.5 table
as re-derived at push time. **Prepared by** `0.7.0_AE_CloudOps~V`; this seat did not build the package, and signs
only what it independently re-verified below.

**Authority:** Andrew-direct ~18:3xZ (record `@0b46309ec2`) + ~19:45Z "Sign first, then push" (record `@1ab93ec740`).
Sign-off covers LEG A (Lambda) and LEG B (EC2 runner's S3 code sync), per his own naming of both legs.

## Independent re-derivation (Rule 22 -- different instrument than the packet's, for each claim signed)

1. **EC2 Stage 6 import failure (packet s.5), re-fetched myself:** `aws s3 cp` of
   `s3://opal-data-mdpf/telemetry/mdpf-daily-runner/logs/mdpf_daily_20260921_125229.log` (own download, not the
   packet's), grepped independently. Confirmed verbatim: `dim_mdpf_aggregate_aua_timeseries.py:75 -> taxsma_assets.py:95
   -> ModuleNotFoundError: No module named 'lib.opal_naming'`, `STAGE6-REVAMP rc=1 dur=1s`, `NON-FATAL build-alongside;
   legacy chain + serving UNAFFECTED; no marker written`. This is upstream of any Cottonwood code path -- LEG B's write
   does not change today's EC2 outcome.
2. **Writer-count challenge (packet s.4), a candidate the packet's census could have missed:** read
   `dim_mdpf_account_distribution.py:80-94` directly (not the packet's `comp-find` instrument). Its `_stage_upload`
   writes `gold/mdpf_revamp/{firm}/account_distribution.json` -- the DS gold-STAGING prefix, not
   `portal/gold/mdpf/{cottonwood,global}/**`. Correctly excluded from N=3; the census holds under this challenge.
3. **R5 no-clobber safety property (packet s.4, load-bearing for "3 writers don't conflict"):** read
   `build_portal_gold_accrual.py:17,197-288` directly. `--allow-overwrite` OFF by default, an existing `{date}.json`
   key is R5-protected and skipped, not clobbered. Confirmed as stated.
4. **LEG B served-vs-HEAD delta for the one file that differs from the hotfix branch (`dim_mdpf_aggregate_aua_
   timeseries.py`):** re-verified earlier this turn (before the packet existed) via a direct `aws s3api get-object`
   on the exact served VersionId to a Windows path, diffed against `git show HEAD:<path>` -- a third instrument
   beside CRO's and MSTR's. 18-line diff, exactly Phase B's `GLOBAL_MODEL_KEYS` change. The packet's s.5/s.1
   claims (timeseries zip content = pin's file + exactly Phase B's hunk, no TAXSMA in LEG A; LEG B ships Phase B's
   hunk on top of already-served TAXSMA, not a new shipment of it) match this independently, and correct this
   seat's own earlier, retracted finding (`@0962ba51c5`).
5. **Build-pin composition (packet s.1):** this seat built the hotfix branch itself (`hotfix/mdpf-cottonwood-
   autocustom-20260921-cto`, from the then-live pin `48b8671569`, cherry-picking `58caa80b8a`/`db6b9fc948`/
   `4ce72c343d` directly) -- the first three of the five commits in the packet's table are this seat's own
   firsthand-verified work, not re-derived from the packet's claim.

## What this seat does NOT independently re-verify (relies on the packet + CRO's parallel half)

The exact zip byte content beyond what (4)/(5) cover, the targeted-plan text, and the S3/Lambda API read-backs in
packet s.3/s.6 -- `4.0.0_SA_CRO` holds the parallel half on those and the apply step itself reads back the running
plane per s.6 before this ships as accepted.

## Blast radius + rollback, both legs, both branches (restated from the packet, read and agreed, not copied blind)

- **LEG A:** touches one S3 zip version, one Lambda code + one env var, one repo literal. Rollback: prior artifact
  VersionId `9GsracvIPvfBMzF1dttMpew0TkQtt.qg` (== running CodeSha256, confirmed by re-download) + revert the literal.
  Both branches of the producer's own rule (cottonwood/global advance with Fixed Income off by_model, OR cottonwood
  refused and global skipped exactly as today) are covered -- neither is predicted, the fire decides.
- **LEG B:** touches 4 versioned S3 keys (rollback VersionIds in packet s.5, confirmed present) + one out-of-scope
  file from another seat's already-approved work (named, not covered by this signature). EC2 outcome unchanged today
  per (1) above; if the unrelated TAXSMA import break is fixed later, Stage 6 would then run the same reviewed code
  LEG A verifies.

## Signature

`1.0.0_SA_CTO` SIGNS both legs as described above, against the exact blob/sha256/pin named at the top. Push
proceeds on `0.0.0_AB_MSTR`'s own re-derivation of the LEG B table immediately before the push (packet s.5,
perishable range) and on `4.0.0_SA_CRO`'s parallel half landing.

**PUSH STATE:** LOCAL on CLOUD; `origin/CLOUD` `d32d3ad8b8` per `ls-remote` read this write; only `0.0.0_AB_MSTR`
pushes.
