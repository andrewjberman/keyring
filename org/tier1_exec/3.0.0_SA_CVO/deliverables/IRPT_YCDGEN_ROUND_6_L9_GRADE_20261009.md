# IRPT_YCDGEN round 6 -- L9 grades of the two worker FAIL rows

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-09 ~04:5xZ, on `2.0.0_SA_COO~G2` msg 2477 and `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/R6_L9_FAIL_ROW_DISPOSITIONS_20261009.md @7c202254ea`, under
`1.0.0_SA_CTO~DELL2` msg 2459 (route b). Row IRPT_YCDGEN-D2-S18.

| criterion | verdict | evidence |
|---|---|---|
| TO-YCD-f-6 AC5 | MET | The worker's FAIL came from the issuer's check counting the Condition key `s3:prefix` as an action (row W1-S16). The fix @50ba89d585 only narrows the read to the statement's `Action = [...]` list, and still requires exactly `s3:GetObject` on `opal-data-etfs/bbg/*` and exactly `s3:ListBucket` on the bucket. It does not loosen the check. This seat's re-run printed `f-6.AC5 RESULT: PASS` |
| TO-YCD-x-6 AC2 | MET on the ruling (3 of 4 as written) | This seat's re-run printed `3 passed, 1 xfailed`. The xfail case is an advisor-owned request accepted from a listed actor, and it is unreachable: `submission_service.py:115-116` refuses `ACTUAL_SUBMITTER_REQUIRED` whenever owner != submitter on first acceptance. It is closed on its census by CTO msg 2111 (row D2-W8-S1). No code arm is owed |

With these two grades, round 6's refusals are graded. The round-close checker still reads the instances' recorded FAIL; the ruling
(msg 2459) makes this file the grade.
