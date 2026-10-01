# /canonical-drive NFRA_MCPMSP -- 2.0.0_SA_COO~MS -- 2026-10-01 04:4xZ-09:3xZ (site Z, host opal_bloomberg)

Seated by 0.0.0_AB_MSTR~Z on 1.0.0_SA_CTO~O msg 27514; ruling `CTO_RULING_20261001_OPAL_GATEWAY_RELEASE_TRAIN.md`
@cf5989190d. No cron: `org/ref/LIVE_ARMS.md` holds no ~MS row. Lease FULL.

| tick | project | limb | round | act fired |
|---|---|---|---|---|
| 1 (~05:0xZ) | NFRA_MCPMSP | L7 drain | 2 | DRIVE FORWARD: R6 MS-r-1 redo on a CLOUD-HEAD worktree (@720199de7d, drained @dddcd61f5b, issuer r1.AC1-AC3 PASS, complete @1ee7b1a077); R5 MS-d-2 A1 @1ee7b1a077 |
| 2 (~07:5xZ) | NFRA_MCPMSP | L7 release | 2 | MX-r-7 landed 05e3eff563 (~MI 27626): MS-d-2 A2 @ef6c65c219 (base 05e3eff563, keys 37 -> 39); PHASE A handed to slot ~5 |
| 3 (~08:5xZ) | NFRA_MCPMSP | L7 release | 2 | Z-W5-S1 ruled (current order landed on the release branch @541131d607, no override); release 2c0f84966d; PHASE A drained @61ba04f9bd; ask + COO half @463e30ded8; CTO half @082e83dbcf |
| 4 (~09:3xZ) | NFRA_MCPMSP | L7 release | 2 | PHASE B: LIVE 2c0f84966d 09:08:28Z; ledger CLOSED; drained @90c760302b; issuer d2.AC1-AC3 PASS + d2.RB READS-OK; complete @c3ef981347; ~O and CTO told |

**Waits (not acts):**
- MS-dn-1: HELD on R7, until the G-RDR release serves and `e1z.AC1.sh` reads `unrouted=0`.
- MS-sv-1, MS-rn-1 and MS-rx-1: on G-MSPID (Andrew "Not yet", 27426).
- Round 2 is not terminal, so no L10 slug.

**Rows ruled:** Z-W5-S1 RULED @541131d607; Z-W5-S2 and Z-W5-S3 ACCEPTED (the ask, section 4).

## Compiler Tools
- comp-read on `.tools/surprise-row-gate.py` with `--for`: gave the file's shape, but not the resolving-row field. The
  channel's own 29 rows answered it instead (all UNDER_INVESTIGATION; rulings ride orders and commits).
- Rail denials: three times (`grep -rn`, `git grep`, a `.tf` grep). Re-run with Grep, or `# rail-checked` for git
  grep against commit trees, which comp-find cannot read.
- Gap: the harness heredoc turned a `\` line continuation into a literal `\n` inside `d2.AC2.sh`. It was caught on
  re-read and fixed with Edit before the commit.
