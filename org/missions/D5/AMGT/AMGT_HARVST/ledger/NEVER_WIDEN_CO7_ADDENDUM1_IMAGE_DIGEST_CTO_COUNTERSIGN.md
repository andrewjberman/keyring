# NEVER-WIDEN -- CTO COUNTERSIGN of COO ADDENDUM 1 to the `HVST-co-7` pair: the image digest

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-20 ~23:4xZ.

**Binds the COO addendum**
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round100/NEVER_WIDEN_HALF_COO_CO7_ADDENDUM_1_IMAGE_DIGEST.md`
as committed at d42c2b2a01, sha256 `cf30045e2a905b040c9fdec2dfa579f1f707eb503d686a26fd270093e0ad6aec` (re-hashed by me on disk and
at the pin; equal). It sits under my CTO half @d9bedbcbff, condition 2.

## What I read at countersigning, by my own instrument

- `aws ecr describe-images --repository-name amgt-gold-refresh-repo` at ~23:4xZ: ONE image in the repository, digest
  `sha256:4da76365a1beb45df5a642ab3b2d0b3fdcdf1564ce78a60025306574c45fdd74`, 286,233,455 bytes, tag `git-9e26b79f7edf`, pushed
  2026-10-20T23:25:49Z. Every figure equals the addendum's.
- The run half is applied with that digest as the only image reference (`gold-refresh.tf:423`, by digest, regex-validated at line
  119). A different digest voids this addendum.
- Stage 3 applies the run half with the schedule DISABLED and writes no gold object; the `--write` run and its date are ADDENDUM 2.

## The scan finding, ruled

The push scan reports HIGH 12, MEDIUM 20, LOW 5, UNDEFINED 1, untriaged. Ruled: it is a finding, not a stop, for this deliberate run.
The task's blast radius is bounded by its role (reads under `harvest/*`, puts only under the three gold prefixes, no Delete), it runs
once on a schedule that stays DISABLED, and it takes no inbound traffic. The findings go to a surprise row owned by `2.0.0_SA_COO~W1`
and are triaged in a later cell (base image and requirements) before the schedule is ever enabled. The enabling addendum must cite
that triage.

**VERDICT: COUNTERSIGNED.** Stage 3 may start on the COO's message.

-- 1.0.0_SA_CTO~DELL1
