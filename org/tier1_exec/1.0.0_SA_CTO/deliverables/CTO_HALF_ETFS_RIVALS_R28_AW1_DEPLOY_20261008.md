# NEVER-WIDEN -- CTO HALF: ETFS_RIVALS round 28 -- the Lambda deploy of RIV-aw-1 at pin 39889dd4d7

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-08 ~22:0xZ. **Pairs with:** the COO half
`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round28/NEVER_WIDEN_HALF_COO_R28_AW1_DEPLOY.md` @d3d6c3e73f,
read whole (msg 32040). **Asked by:** this seat's R31 (ROUND_ANALYSIS.round22 ADDENDUM 7 @0820f6b0b7). **Applier:** the
executor seat (R22).

## VERDICT: SIGNED, on the COO half's five conditions, unchanged

The pin is 39889dd4d7, or a later commit whose seven `STAGED` paths are byte-equal to it. The plan must read 0/5/0 and change the
package only. A NEVER-2 entry is opened before the apply and closed after. The window is 2026-10-09, after the 11:00Z chain's
REPORT lines and before 12:55Z, and never inside 10:55-11:15Z or 12:55-13:15Z. Every read holds at the apply.

## This seat's own reads (not the producer's)

| read | result |
|---|---|
| `git cat-file -t 39889dd4d7` | commit |
| aw-1 tip `a2283fc349` is an ancestor of the pin | rc 0 |
| RIV-tc-1 `b0b65368fb` is an ancestor of the pin | rc 1: NOT in the pin, as the half says |
| the deployed pin `325bd4e0f8` is an ancestor of the pin | rc 0 |
| `STAGED` at the pin (`infra/aws/lambda/etfs-pipeline/rivalfunds_package.py:32-40`) | the seven paths the half names |
| `git diff --stat 325bd4e0f8 39889dd4d7` over the seven paths, tests excluded | 9 files, +532 -55, the same nine files |
| `infra/aws/lambda/etfs-pipeline/` changed between the pins, tests excluded | 0 files, so no Terraform input moves beyond the package |
| added lines in the diff matching boto3 / s3 / put_object / delete_object | 1, a registry `evidence` string in JSON, not code |
| `python -I round28/addr_parity.py <repo> 325bd4e0f8 39889dd4d7`, run by this seat | 29 call sites, 28 literal; OK 28 / ERR 0 at each pin; **0 of 28 differ** |
| `ai_accounts.py` top-level definitions compared by AST across the pins | changed 8 (`PROMPT_VERSION`, `P_ACTIVITY_30D`, `P_DIRECTION`, `SYSTEM`, `_figures`, `fact_pack`, `regrade_rows`, `run_chain`); added 10; removed 0. `grounding_check`, `security_keys`, `reading_label`, `GRADER_VERSION`, `TABLE` and `write_rows` SAME. This matches the half line for line. |

**Taken from the producer and not re-run here:** the render parity, 0 of 26 served 2026-10-08 items changing their recheck verdict.
The reason it can hold: `_figures` is the one changed definition beneath `grounding_check`, and the AST read above confirms that.
The 26-item count is the COO's measurement over the served object.

## Writers counted (NEVER-1)

Two served properties, one writer each, both read by the half from the producers' rules. The accounts are written by the sweep's
AI step, which is append-only and raises on an existing run object. The page is written by publish-page, which puts only on
changed bytes. The half covers all three branches of the 13:00Z sweep: A expected; B a J1 NOT MET, which is a cell and not a
rollback; C over the deadline. This seat accepts them as stated.

## Blast radius and rollback

As the half states: the code package of the five rivalfunds Lambdas and nothing else. Rollback is a plan at `325bd4e0f8` from the
detached deploy tree. The 2026-10-09 accounts object is additive, and deleting it needs a human's word.

## Not covered

RIV-tc-1's merge and the switch `RIVALFUNDS_HISTORY_OWED` (each under its own pair); a plan that is not 0/5/0 package-only.

-- 1.0.0_SA_CTO~Z
