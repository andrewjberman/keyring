# 2.0.0_SA_COO~MI -- NFRA_MCPINDEX: MX-r-9 PHASE B hardened (A3-A5), re-cut on r29, both never-widen halves SIGNED; queued behind OG-ap-4 and MP-x-4 -- 2026-10-09 11:3xZ-14:5xZ (host opal_bloomberg)

**archetype:** COORDINATE

## Ticks and events

| time | act |
|---|---|
| 11:3xZ | The applier's row Z-S90: the `.env` count is 52 after r29 (OG-md-1's `MAIL_SENDER_DOMAIN_TABLE` rides r29), and the order's `Z-AMX-S<k>` id is refused by the row gate. A3 @18ad3e7a14 makes the equality a RULE and the id `Z-S<k>`; Z-S91 disarms Z-S90 |
| 11:54Z | r29 halt-gate BLOCKED from a sparse tree (NFRA_OPLGTW-Z-S74). A4 @77fc31c41c pre-empted it with the HALT_GATE_* env roots |
| 12:24Z | NFRA_OPLGTW-Z-S75: `infra/aws/ec2/safe-ec2-deploy.sh:57` resets HALT_GATE_REPO_ROOT, so A4 could not work. A5 @db83d9d163 supersedes it: materialise `org/tier2_senior/0.7.0_AE_CloudOps` in the sparse deploy tree, and prove it through the wrapper's own path |
| 12:4xZ | The applier proved A5: negative rc=3 `unknown-base`, positive rc=0. r29 DEPLOYED 12:31:40Z. Partial GO: re-cut on r29 and announce; the apply held |
| 13:4xZ | ANNOUNCE_MX-r-9_PHASEB @5f9d189083: deploy-only 5133f082bc, 2 files; preservation 96/98; `.env` 52=52; tools 66=66; integrations 7=7 |
| 13:4xZ | The issuer re-measured: S3 git-ref and EC2_MANIFEST both 91811b648a at 13:47:55Z; 24 of 24 ledger sentinels with no gateway deploy in flight; the git re-read of the cut matches. NEVER_WIDEN_ASK_MX-r-9 with the COO half SIGNED @f041d208e6 |
| 13:5xZ | `1.0.0_SA_CTO~O` reads NOT REGISTERED (6 unread). The half ask was re-addressed to `1.0.0_SA_CTO~Z` |
| 14:01Z | CTO~Z: G-A PASSED, and the CTO half SIGNED @cd2a361f8d on the same pins |
| 14:27Z | COO~O msg 32803: OG-rl-15 read + grant done @796695e622. Host queue: OG-ap-4 -> MP-x-4 -> MX-r-9 -> E2. The r29 pins will VOID by the BASE-MOVED clause: re-cut and re-sign after MP-x-4's ledger closes. The applier was told to hold |

## State at 14:55Z

- Round 8: 3/4 terminal and drained. MX-r-9 is PHASE B part 1 done, with both halves on r29 pins that will VOID when the
  base moves.
- Round 9: staged unissued @f4cc1c96d4 (1.0.0_SA_CTO~Z ruling @ff362e8444).
- J1: booking asked of `0.0.0_AB_MSTR~Z`, runnable after r9.AC2/AC3 pass.

## Compiler Tools

- `deploy_ledger.py list`: 24 of 24 sentinels.
- `git diff --stat` and `rev-parse` of the cut against r29: 2 files, trees f3844dae4c / dbcced0bf1.
- `.tools/aws s3api head-object` on `-latest`: git-ref r29.
- Gap found: a memory write was blocked by the lesson hook (seats do not bank lessons, Andrew-direct 2026-09-24). The
  stray index line was removed; the lesson lives in NFRA_OPLGTW-Z-S75 and A5.

Push state: 18ad3e7a14, 77fc31c41c, db83d9d163 and f041d208e6 are on origin. origin box/sitez read 48864ff38b at 14:55Z
(ls-remote), checked by is-ancestor.
