# ANDREW-DIRECT 2026-10-19 ~18:3xZ -- raise the opal-gateway EC2 to t4g.large

Channel: typed by Andrew at the `1.0.0_SA_CTO~Z` terminal (Claude Code session), ~18:3xZ (2:3x PM ET). It answered this seat's
explanation of the 17:30Z-18:26Z gateway hang. That explanation gave the instance as t4g.small (2 vCPU, 2 GiB) with the service
capped at MemoryHigh 1200M and MemoryMax 1400M. It recommended t4g.medium or t4g.large, done off-hours because a resize stops the
instance.

## VERBATIM

> lets raise it to large

## Applied

- **The act:** `infra/aws/terraform/opal-gateway/main.tf:172` `instance_type` changes from `t4g.small` to `t4g.large` (8 GiB),
  through `safe-apply`.
  - A stop and start of `i-07dccb1615503ac99` is part of the act. His word is the confirmation that stopping an EC2 instance
    requires.
  - The contract's `target_instance_type` (`infra/aws/ec2/opal-gateway/deploy/NFRA_OPLGTW_CONTRACT.json:351`) moves with it.
- **The companion:** the unit's memory limits (`deploy/opal-gateway.service:20,22`) rise to fit 8 GiB. The bounds in
  `tests/test_og_un1.py` move with them. This ships in a gateway release, because a bigger box with the same 1.4 GB cap would
  hang at the same point.
- **Timing:** after the 19:00Z session with Alyssa, off-hours, under one deploy ledger with a rollback (the type set back to
  `t4g.small`).
- **Owner:** NFRA_OPLGTW, `2.0.0_SA_COO~O` issuing to `0.7.0_AE_CloudOps~NFRA1`.
