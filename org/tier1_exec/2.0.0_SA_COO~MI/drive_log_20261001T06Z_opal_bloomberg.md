# /canonical-drive NFRA_MCPINDEX -- 2.0.0_SA_COO~MI -- 2026-10-01 06Z (host opal_bloomberg)

Lease FULL, round 5, limb L7, thread y.

## Decisions closed this span

- **MX-r-7 PHASE A v2 clean** (worker ~21 @b92561fbec, LOCAL).
  - Release 08e6f78940; deploy-only 05e3eff563; gateway tree b5733d7f9d.
  - Plan 6 sha256 0401378f8e10..., 6/0/0.
  - `.env` 35 -> 37; role_config proven in-process, with a negative control on the live render.
  - Row Z-W21-S17 carries the A5 rulings: the row gate refuses in-place edits to S12/S13.
- **Never-widen halves:**
  - COO SIGNED @574e0acf6b; the base was issuer-read at 06:14:19Z (manifest + S3 git-ref; 22/22 ledger sentinels, no
    gateway deploy open).
  - CTO SIGNED, G-A ACCEPTED @adcbe6b693, after independent reads. It added two void conditions: `.env` under 37 keys
    or missing a principal key; any served tool removed.
- **PHASE B GO.**
  - Principals arrived off-repo from COO~O (msg 27569, gitignored inbox). The values are never logged.
  - Worker ~21 is on legs 1-3: ledger `nfra-mcpindex-r5-bd-release` open, Plan 6 through safe-apply, simulate.

## Owed

- One line to 2.0.0_SA_COO~O when TF act #1 lands (msg 27540). OG-pr-1 waits on it.
- The deploy leg, after legs 1-3 report: the principals are sourced from the inbox file into the deployer's shell.

## Compiler Tools

- None. The reads were git, S3 head-object, the manifest, and `deploy_ledger.py list`.
