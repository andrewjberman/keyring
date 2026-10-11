# /canonical-drive log -- 2.0.0_SA_COO~B1 (dell1), ADVI_FIRMBKTS round 4 issued and drained, 2026-10-11 12Z-14Z

**archetype:** COORDINATE

Loop: none armed. Same session as the earlier logs; round 4 is issued in six commits (three issuances and the amendments
between them), each with its `fanout:` line.

| UTC | limb | project/round | TOs t/T | act fired |
|---|---|---|---|---|
| 11:5xZ-12:2xZ | L5/L6 | ADVI_FIRMBKTS 4 | 0/9 | decomposition v4, ONE issuance FB-g-1..9 (@f33c93ce43), dep_stage EXECUTING; six workers and two seat orders; FB-g-9 (the SEV1 test text) carried as crossbox ORDER e318 |
| 12:3xZ | L7 | ADVI_FIRMBKTS 4 | 3/11 | second issuance FB-g-10 (INFJWT) and FB-g-11 (BRONZELIVE) on the CTO's ADDENDA 2 and 3; FB-g-6 withdrawn (S12 not reconcilable, ADDENDUM 5); FB-g-7, FB-g-10, FB-g-11 merged |
| 12:4xZ-13:3xZ | L7 | ADVI_FIRMBKTS 4 | 8/14 | the naming gate refused FB-g-1/FB-g-2 and FB-g-12 in turn: ADDENDUM 4 (generate), issuer rulings on the registered-owner rule; FB-g-12, FB-g-13, FB-g-3 merged; FB-g-1, FB-g-2 re-seated and merged; FB-g-14 cut on ADDENDUM 6 (D1-S24) |

## Rulings by the issuer in this stretch

- D1-W26-S1..S3 (table repair): the CTO's S10 is the later specific ruling over the S5 difference control; one skip marker row for S7 with the duplicate-key test told apart by marker kind; a QA-named class with no writer in code is a FAULT row citing S6, and previously placed rows are not re-judged.
- D1-W33-S3 (builder format string refused): OWNERSHIP_KEYS lists only firms that own a REGISTERED legacy ownership-map address; legacy is the row's template; no per-tenant row is invented.
- D1-W34-S1/S2 (mark lines in the dormant arm; a null scope guard): the check ignores a generated file's mark line; the worker's guard is accepted.
- D1-W37-S2 (a bare product token in the builder): the product key comes from `lookup()`, never typed.
- D1-S23 (dell1 identity denied two plan reads): not widened; AC1 and AC2 of FB-g-10 are graded from the laptop lane.

## Defects in this stretch's own row, stated

- The CTO's ADDENDUM 1 premise (the bronze-home rule resolves to opal-data-bd) was false; measured at HEAD before any cell was cut on it, and corrected by the CTO's ADDENDUM 3.
- My `r4_scope.py` read a worktree's portal gitlink as a changed path; three workers' AC3 read FAIL on it (D1-W29-S1, D1-W25-S2, D1-W24-S1). Fixed in the check and every instance re-graded.
- My git helpers decoded `git show` as cp1252 and the file as UTF-8, so files with non-ASCII bytes read as value-changed (FB-g-11 AC1). Fixed.
- My first FB-g-1 and FB-g-2 faces typed key templates, a policy name and ARNs, which the enforcing naming gate refuses; both workers passed my checks and could not commit. The CTO's ADDENDUM 4 and two builder cells followed. I read the gate's context rule only after the refusal.
- The decomposition named "IRPT consumers" and "the three gold scripts" as regenerate-only readers; the flip rehearsal and a head-object read showed their keys are absent in the new bucket (D1-S24).

## Left open

- Act 0 (FB-g-8) and the window's four staged acts (FB-f-9 phase B, -10, -11, -13) stay parked: each waits on its pair and on the readers' merge; act 4 waits on the CTO's print and on D1-S24's cell.
- FWD-7 and FWD-8, the SEV1 text's arrival (Andrew's phone), the AWS Support case if it did not arrive.
- Push state: LOCAL on `box/dell1` except the commits MSTR pushed with the crossbox ORDERs.

## Compiler Tools

| tool | result |
|---|---|
| `r4_flip.py` (issuer, new) | flip rehearsal: 17 targets, 5 then 4 value-changing |
| `r4_mapping.py`, `r4_validator.py`, `r4_grant.py`, `r4_okeys.py`, `r4_modgrant.py`, `r4_dormant.py`, `r4_irptlive.py`, `r4_e24.py`, `r4_reader.py`, `r4_agree.py`, `r4_scope.py`, `r4_secretver.py`, `r4_sms.py` (issuer, new) | each dry-run at base (FAIL as expected, controls PASS) before its cut; re-run at the merged head at the drain |
| `safe-merge.sh` | seven fast-lane merges; one refusal while another seat's merge was open |
| `safe-commit.sh` naming limb | refused three builds on NEW hand-kept carriers: the gate was right each time |
| `comp-rail` | denied recursive greps and a piped census; named-file reads and native Grep were free |
