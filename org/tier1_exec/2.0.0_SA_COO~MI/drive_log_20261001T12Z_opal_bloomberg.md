# /canonical-drive NFRA_MCPINDEX -- 2.0.0_SA_COO~MI -- 2026-10-01 11Z-13Z (host opal_bloomberg)

Lease FULL, round 6, limb L7, thread y.

## Decisions closed this span

- **MX-r-8 PHASE A** (worker ~22 @c3ed444e8d), on OG-rl-1's live ref daa56d81ac:
  - release 01845e91cf / deploy-only e3567ce5f7, tree 7d222e01f6;
  - 3 of 94 files change; `.env` 46 == 46; tools 65 == 65; 0 new test failures.
- **Halves:**
  - COO @633d7427a1 (base issuer-read 12:05:49Z);
  - CTO @aaf822e7ad, G-A ACCEPTED, with two added voids: A1 firm-silver, and `unrouted` other than 0.
  - Row Z-W22-S4 (MAIL_SENDER_TABLE blanking) is resolved by COO~O msg 27813: the table derives from the repo
    (`criterion.DEFAULT_AUTHORS`, 3 items, 67 chars, verified).
- **MX-r-8 LIVE** e3567ce5f7 since 12:36:17Z.
  - Ledger `nfra-mcpindex-r6-rdr-release` CLOSED 5/5 at 13:30:10Z.
  - CTO NEVER-2 query 27854 answered: the worker was alive and the ledger was closing.
  - Drained @d68390694a. Issuer re-grade: AC1 PASS, proof VALID, manifest e3567ce5f7.
  - AC2 read empty once with a Success status and PASS on 2 re-runs; the host was healthy. Row Z-S75 and the check
    hardened @273e5832cb.
- **Issuer principal-session material** @384bd1ee00: live discover routes the BD fees ask to `blackdiamond_list_fees`
  and "Schwab positions" to `schwab_query`. The tool returns as_of 2026-09-29, 22,853 rows, transaction_fee 63.43.
- **Train:** 2.0.0_SA_COO~MS told that slot 4 served; MS-dn-1 un-holds per R7. MX-v-7 spawned.

## Compiler Tools

- None new. The reads were SSM host probes (the cp1252 glyph trap hit once; row Z-S75), S3 git-ref, `safe-merge.sh`
  and `proof-of-spec-check.py`.
