# ADVI_COTBKF decomposition -- ROUND 88 (issuer 2.0.0_SA_COO~C1 on dell1; drafted 2026-10-15) -- ONE job reads the restricted CRM zip: grant, job, withdrawal

**Status: DRAFT -> ISSUED in one issuance, on the CTO's word to issue now (msg 6158) while round 87's last two workers finish.**

**Cut on:** Andrew-direct 2026-10-15 ~19:0xZ, VERBATIM: "I agree with (a), let's see what we can do with that for now." (laptop record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261015_190xZ_D3CC_A_ONE_JOB_READS_RESTRICTED_CRM_ZIP.md` @6e96dd543a, relayed by `0.0.0_AB_MSTR~DELL1` msg 6143), applied by
`ledger/CTO_RULING_DELL1_UNPARK_ACCELERATE_20261015.md` amendment 5 (msg 6146): three orders, in order. The never-widen pair is GIVEN on both halves:
COO `ledger/NEVER_WIDEN_R88_CRM_MATCH_GRANT_COO_HALF.md` @85e152e5ca (sha256 `472df1c92c5927d6c714d1ab5bb3f13096d2456b0662f2524f388be17ed3bbc3`) and CTO
`ledger/NEVER_WIDEN_R88_CRM_MATCH_GRANT_CTO_HALF.md` @438c699be3, conditions C1 (every AssumeRole on the role listed), C2 (the 23:59Z withdrawal is absolute), C3 (the CVO re-signs PRD v0.11's
ratified-text half before the apply). PRD v0.11 @438c699be3 carries the exception in C-RESTRICTED. FWD-9 stands: DETERMINISTIC only on a stable key, else CANDIDATE. Option (c), asking Cottonwood, is NOT sent.

**Rule 24.** Domain: amendment 5's three numbered orders. Subtraction: order 1 -> CB-cj-1; order 2 -> CB-cj-2; order 3 -> CB-cj-3; the report for Andrew (matched and unmatched over the 219) -> CB-cj-2's
record and the issuer's close. Uncovered: none.

| cell | item | serves | risk | depends_on | assignee |
|---|---|---|---|---|---|
| `CB-cj-1` | GRANT: one builder-named IAM role (`s3:GetObject` on the ONE key) and its ARN in the READ-deny readers list; targeted plan shows exactly those; `safe-apply`; read-back; ledger entry opened first | FWD-8, FWD-7 | WORLD | the pair (given), CVO re-sign (C3) | `0.7.0_AE_CloudOps~CB1` (CloudOps lane, seated for this project) |
| `CB-cj-2` | JOB: assume the role, `head-object`, read the zip in memory, join CRM identifiers to both sides, write ONLY `commonwealth_account, bd_account_id, rule, tier` plus counts; the run record is the log; matched/unmatched over the 219 | FWD-8, FWD-9 | WORLD | CB-cj-1 applied and read back | `0.9.0_WK_ADVI_COTBKF~177` |
| `CB-cj-3` | WITHDRAWAL: role and ARN removed the same day (23:59Z absolute); re-plan reads no changes; every AssumeRole event on the role listed; ledger closed | FWD-7 | WORLD | CB-cj-2 terminal, or 23:59Z | `0.7.0_AE_CloudOps~CB1` |

**One chain, three orders, two assignees** (the dependency edges cj-1 -> cj-2 -> cj-3 make ONE chain; the grant and the withdrawal are one CloudOps seat's, the job a worker's).
Fan-out to state at the cut: `1 of 1 chains, cap 8`.

**The clock.** The role, the job and the withdrawal all fall on ONE UTC day. cj-1 is PENDING (its preconditions are read by the seat). cj-2 and cj-3 are STAGED: cj-2 is un-parked by the issuer's amendment that names the role and the read-back; cj-3 by the issuer the moment the job's record is written (the CTO's msg 6158), or by the backstop at 23:30Z of the grant day, or at once on a half-landed grant.
