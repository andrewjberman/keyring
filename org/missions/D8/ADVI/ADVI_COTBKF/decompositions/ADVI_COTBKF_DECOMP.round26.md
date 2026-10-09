# ADVI_COTBKF decomposition -- ROUND 26 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-09 ~01:5xZ)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2`'s round-24 analysis ADDENDUM 1 (round 25), `CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_24_20261009.md`
(msg 2113): `method_r25` is the default; pay date stays; the 39 carried levels are baseline errors. Enrichment E1 (the non-MATCH census
with its denominator), E2 (ASF sourced or carried NO-SOURCE), E3 (one endpoint line per FWD, REALIZED / NOT, with its instrument).

**Rule 24.** Domain: E1, E2, E3. Three cells, two chains: E2 may change the rule, and E1's census must run on the final rule, so E2
-> E1 run on one worker; E3 reads artifacts only and writes one deliverable, so it runs in parallel.

## Measured constraints

1. Round 25's real run on the trunk (@052a80dd0f): `method` -> `method_r25`, `months_after=3098/886/78609 regressions=0`; 82,593 graded
   months in all, of which MATCH 3,098, DIFF 886, UNGRADABLE 78,609.
2. `ASF` is the one unlisted type kept internal with no source (CB-y-1's source table @679c3c22b5).
3. The PRD carries 9 outcomes, FWD-1..FWD-9. Earlier analyses grade 6 of 9 REALIZED (CTO round 15); FWD-3 is this rule's.

## The cells

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-z-1` | E2: ASF sourced before the run (rule `method_r26`) or carried NO-SOURCE with its row count | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~48` |
| `CB-z-2` | E1: the default set to the final rule; the census of every non-MATCH month (DIFF and UNGRADABLE) by class, denominator printed, no class unexplained | FWD-3 | LOCAL | `CB-z-1` | `0.9.0_WK_ADVI_COTBKF~48` (continued) |
| `CB-z-3` | E3: the endpoint read -- one line per FWD-1..9, REALIZED / NOT with its instrument and evidence | FWD-1..9 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~49` |

**Fan-out:** `2 of 2 chains, cap 8`.
