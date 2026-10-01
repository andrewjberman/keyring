# /canonical-drive NFRA_MCPINDEX -- 2.0.0_SA_COO~MI -- 2026-09-30 14Z-15Z (host opal_bloomberg)

Lease FULL, round 5, limb L7. Thread y.

## The gateway incident, and its close

- **14:36:48Z** 2.0.0_SA_COO~RV deployed 4ce7946426 (ETFS_RIVALS) to opal-gateway.
- **14:41:23Z** worker ~19, under my GO, deployed MX-r-6 v2 (2e2254156e, built on 288fa78c93) over it.
  - The `/rivalfunds` routes were removed.
  - The targeted schwab reader-policy apply also landed.
  - The GO's base guard (G1) had been read at PHASE B start (~13:58Z), not at the upload. All halves were VOID.
- **~14:44Z** I stopped ~19 and escalated to ~RV and the CTO (msgs 27204/27205). I opened ledger
  `nfra-mcpindex-r5-rollback-4ce7946` @249b9233a6.
- **My three restore attempts of 4ce7946426:**
  1. blocked: no serial file in the worktree;
  2. blocked: the sparse tree lacked the `org/tier*` agent folders;
  3. hung in the halt-gate message scan.
  I stopped it at ~15:10Z when ~RV changed its plan. Nothing had uploaded (S3 read).
- **15:12Z** CTO ruling (msg 27224): PLAN A. ~RV restores its own 4ce7946426; this seat rolls back IAM. ~RV's plan B,
  which would have kept an unsigned combination live, was refused.
- **15:23:02Z** ~RV's host read-back (msg 27230): host == 4ce7946426 on 80 of 80 files, /rivalfunds 401, no schwab,
  FIRM_ROLE_ARNS kept.
- **~15:5xZ** IAM rolled back: `safe-apply` of the saved targeted plan, 0 added / 1 changed / 0 destroyed.
  - Getting there took:
    - reviewing the halt gate's 208 pending items (0 STOP-class; automated ledger nudges), then HALT_ACK;
    - plan-only placeholders for the two MCPORTAL variables;
    - MCPORTAL's gitignored layer zip and `.build/staged` copied into the rollback tree.
  - Live read at 15:59:18Z: dim_transaction explicitDeny on both masters; positions/balances allowed; re-plan
    "No changes".
- **Ledgers closed:** `nfra-mcpindex-r5-rollback-4ce7946` @4b14925ac4; `nfra-mcpindex-r5-schwab-enable` ROLLED-BACK
  @0c79bc5c0b (on the worker branch).
- **Row Z-S68** @1d03eb4130 (BLOCKING/ARMED): base guard not re-read at upload; two issuers on one host.
- **Disarm:** plan A (done), plus the stale-base guard by ref in deploy-to-ec2.sh, which ships in v3 (CTO msgs 27210,
  27231).

## Also this span

- Andrew "agreed" (@29bc46d827, CTO msg 27198): ONE new Schwab grant to Alyssa (two masters, four datasets). It is
  written after the v3 release lands.
- MX-t-12 record drained @2a10e3c247; ruled by Z-S67 @12746a5c6d (held, carried to L10).
- MX-r-6 A6 @4f7032da3b: v3 on 4ce7946426 by REF with the guard. ~19 spawned at ~16:0xZ.

## State at 16:10Z

- Round 5: 3 of 7 complete. MX-r-6 v3 PHASE A in flight.
- HELD:
  - MX-t-13 and MX-r-7 (R20 gate edit cb4296f508 NOT yet on CLOUD here);
  - MX-t-12 (to L10).
- Round 4: MX-t-10 (same gate edit); MX-s-14 (fires).

## Compiler Tools
- None. The reads were S3 list-objects, SSM host reads, `iam simulate-principal-policy`, `terraform plan`,
  `deploy_ledger.py`, and the halt gate's own output.
