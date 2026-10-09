# CTO never-widen half (RE-SIGNED) -- partner_roster T-1 correction into its two live readers (1.0.0_SA_CTO, owner, 2026-10-09 ~00:3xZ)

**Supersedes** section 2 of `CTO_HALF_NFRA_CTLPLN_STEP_G_AND_PARTNER_ROSTER_20261009.md` @21a5ceab0f, which covered the deprecated
loose key `s3://opal-data-mdpf/code/scripts/gold/partner_roster.json` (left untouched).
**Counterpart read** (to the end of leg B's expected outcome): `org/tier1_exec/2.0.0_SA_COO~G1/deliverables/COO_HALF_PARTNER_ROSTER_DEPLOY_20261009.md`
@58e5631eb7 (origin box/dell1 5f2ab28b0d), signed by 2.0.0_SA_COO~G1. Executor `0.7.0_AE_CloudOps~DELL1`.
**Authority:** Andrew-direct 2026-08-27, "Yes that config is what needs to change" (HEAD b3ed0e8d69: Cottonwood cadence T-1).

## What this half signs

- **Leg A:** re-mint `bundles.accrual_bridge` from HEAD (LF): roster changes, script byte-identical. Served value delta 0; the
  accrual output's roster stamp changes at its next run. Rollback: re-point to version BtC_0xCV5wIH1yJmIYw1XdDVh5UN_YC6.
- **Leg B:** the emitter's vendored roster, on a PINNED build: B0 must reproduce the live CodeSha256 (n/Tu1ns1..) from a commit
  near 9abdfa4c30, or leg B stops and returns; B1 is that tree with ONLY `partner_roster.json` replaced by HEAD's bytes; B2 is a
  targeted 0/1/0. In plain words: which Cottonwood days are accepted or refused does not change and no figure changes; only the
  label of a one-missed-day Cottonwood partition moves from "at declared cadence" to "within slip tolerance", so a missed day
  shows as late.

## Explicitly NOT covered

The four emitter commits newer than the live code and never deployed (ae106b1124, aaf2be288f, 650df7371e, 85dd7adc26). A build
from HEAD ships them; that is a separate pair.

**SIGNED** -- `1.0.0_SA_CTO`
