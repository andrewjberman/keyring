# /canonical-drive NFRA_MCPINDEX -- 2.0.0_SA_COO~MI -- 2026-10-07 00Z -> 01:2xZ (host opal_bloomberg)

**archetype:** COORDINATE

Lease FULL. Round 7 at L7: 5 of 7 orders terminal. MX-s-18 is applied with its ledger open on one leg. MX-s-19 has not
started.

## Decisions closed

- **CTO half AMENDMENT 1 @02b8f2267a** (msg 30456): MX-s-18 only, same four conditions.
- **GO re-stated @c7b79a0e06** (msg 30462, READ by the seat 00:13Z). The first commit attempt lost an `index.lock` race
  with a peer; the retry landed. The repository was asked, not the tool's output.
- **MX-s-18 PHASE B LANDED** (seat msg 30478, branch `wk-nfra_mcpindex-r7-24` @c04f1615e0).
  - `safe-apply` at 00:49:58Z: 0 added / 2 changed / 0 destroyed.
  - One IAM statement, `ReadBackBdBronzeSentinel`: 7 added lines, 0 removed.
  - Pins re-read at the first act: 7 of 7 equal.
  - Controls on the grant: a non-sentinel bronze key reads implicitDeny; the cot plane reads explicitDeny.
  - Row Z-W24-S11 DISARMED.
  - Evening rules still ENABLED; SSM documents still 3 = 3.
- **Issuer's own live read at 00:51Z**, taken before the seat's report:
  - `bd-49f-runner` CodeSha256 `9PbO1/mVokBTWGNn8NjjTyjkhWvBdZ6pZk2zcCE0/eY=` (LastModified 00:50:44Z), equal to the
    built zip's sha in ANNOUNCE_MX-s-18.
  - `simulate-principal-policy` GetObject on `bronze/2026-10-07/_BRONZE_COMPLETE.json` = allowed.
  - The 10-07 sentinel was written at 00:11:33Z by the old code.

## Open (each with its condition)

- **MX-s-18 ledger `nfra-mcpindex-r7-bd-runner-sentinel`:** OPEN on leg V1. V1 closes on the scheduled 00:00Z run of
  2026-10-08, the first live exercise: an `OK` line after the read-back, or a `WARN` naming tables. s18.AC4 and the
  proof instance follow.
- **MX-s-18 A2 reads:** Monday 2026-10-12 and Tuesday 2026-10-13, with the evening rules still enabled.
- **MX-s-19:** the two-rule disable, after those reads, under its own never-widen halves.
- **Drain of `wk-nfra_mcpindex-r7-24`:** at the ledger close. Until then the open entry lives on the branch (NEVER-2:
  read every live worktree, not the shared tree).
- **L8 compile and the round-7 slug:** at the round's drain-end. Rows Z-S78, Z-S80 and Z-S82 are carried.

## Compiler Tools

`safe-commit.sh`, `get_delivery_state`, `.tools/aws` reads (lambda get-function, iam simulate-principal-policy, s3api
head-object).
