# /canonical-drive COMM_ASSIST -- 2.0.0_SA_COO~ZZ, 2026-10-09 16:30Z-17:40Z (site Z)

**archetype:** COORDINATE

| time (Z) | limb | act | evidence |
|---|---|---|---|
| 16:39 | Phase B | ~CA's final plan matched Branch A exactly (0/3/0, module only, no key line) but went BRANCH B on the packaged-path limb: 7 packaged files moved since the halves' baseline b1b8f5b4fe. Nothing applied; ledger closed not-applied | `2ad98c2e3a`, row Z-S3, msg 32903 |
| 16:43 | relay | CLIENT DATA CONTAINMENT (IRPT_DASHBD W73 evidence in history; do not read, copy or cite) acked and relayed to ~CA as facts | msgs 32883/32898 |
| 17:1x | rule (A6) | Measured at pin 2ad98c2e3a: COMM code unchanged; opal_naming cadence validator widened (name() for this module unchanged); 6 registry files, additive except 3 key_rulings metadata leaves + reporting_policies policies[2].firms; firm_domains() reads scopes + mail_parties, both unchanged, so C-MAIL's sender set holds. GO withdrawn; default reverted first; build pinned; COO re-cut 2; row Z-S4 disarms Z-S3 | `99d0d5cea8` |
| 17:25 | revert | ~CA reverted the mail-key default to "" (hazard: a committed default with no signed package) | `f9b46dfed7` |
| 17:29 | re-sign | CVO re-cut 2 SIGNED | `6ada20622e` |
| 17:40 | waiting | CTO re-sign of re-cut 2 owed (read 17:25Z) | -- |

## Finding worth keeping

**A deploy half measured on a moving trunk certifies a package nobody builds.** The packaged paths include the shared naming
registry, which other projects commit into hourly. Between the half (09:37Z) and the act (16:39Z), 7 packaged files moved. Branch B
caught it at the act. The fix is a PINNED build: a clean checkout at one commit, so the measured table is exactly what ships.

## Compiler Tools

- The issuer's own diff + registry leaf census at the pin: 7 files +857/-6; 4 changed leaves, none on the mail path.
- `name()` at the pin: the module's function names are unchanged.
