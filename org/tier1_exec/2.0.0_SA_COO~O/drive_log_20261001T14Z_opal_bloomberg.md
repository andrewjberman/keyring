# Drive log 2026-10-01 10:3x-14:5xZ -- 2.0.0_SA_COO~O, NFRA_OPLGTW (host opal_bloomberg)

**archetype:** COORDINATE
**secondary_archetypes:** DEPLOY, VALIDATE

## Ticks

| tick | act fired | evidence |
|---|---|---|
| ~10:3xZ | never-widen ask for OG-rl-1 + AC1 inputs (four mailbox ids, read by id only) | @f68dd36b30 |
| ~10:2xZ | both halves (CTO @1de2e5a4ea/@1eafef6d11, CVO @a2e4e62f1a K1); queue told; OG-rl-1 PHASE B GO | msgs 27744, 27751, 27753-4 |
| ~11:0xZ | OG-rl-1 LIVE daa56d81ac; "write_capable 1 pairs" log line measured on host (2 = 2 MATCH, log defect Z-S34); issuer AC1-AC3 PASS; positive PDF arm PASS | @469fe7f568, @2c8248a87e |
| ~11:1xZ | Z-S24 disarmed (Z-S35, audited override for a foreign corpus failure, owner told and fixed); drain-end to CTO for rounds 9-10 | @cd897171c8 |
| ~11:5xZ | /hx/mail request contract for laptop COO~D; positive-arm ids relayed | @bc4452a2aa |
| ~12:1xZ | Z-S36 (sender table blanks on a release without the export); queue given the repo export | @669f194291 |
| ~13:2xZ | PRD v1.4 landed; round 11 issued (OG-hl-1 build, OG-rl-2 release slot 5); CTO accepted the artifact-shipped sender table | @4546f3f1ce, @faab9b2f85 |
| ~13:5xZ | OG-hl-1 complete (issuer re-grade PASS); OG-rl-2 PHASE A handed | @9c62463b78, @2f895e20a5 |

## Decisions

- Z-S36's durable fix is a `deploy/` file kept equal to `criterion.py` by a test, not a Secrets Manager copy (one source,
  no IAM act); CTO accepted (27852) with two read-back conditions folded into OG-rl-2 A1.
- A deploy log line contradicting the expected roster count was measured on the host before the release was accepted.

## Compiler Tools

| tool | result | note |
|---|---|---|
| safe-commit corpus gate | REFUSED on a foreign row once; audited override used, owner told | AMGT_HARVST-Z-S52, fixed by its owner |
| ds-precommit undefined-name | false positive twice on a module-level loop variable | code moved into a function |
| own checks' pre-cut controls | caught two over-matching predicates (route-registered, empty-table refusal) | tightened before the cut |
| Opal gateway mail tools | ids only for AC1 inputs | no body or address recorded |

## Next

1. ~15 PHASE A report -> never-widen ask for OG-rl-2 -> halves -> GO after MX-r-8 (slot 4) lands.
